#!/usr/bin/env python
# Copyright (c) 2022 Red Hat
import re

from copy import deepcopy
__metaclass__ = type

from ansible.errors import AnsibleFilterError

def sanitize_bool(s):
    if isinstance(s, bool):
        return s

    if isinstance(s, str):
        if s.lower() in ['true', 'y', 'yes']:
            return True
        if s.lower() in ['false', 'n', 'no']:
            return False

    return s

def ee_is_allowed(ee, allow_list):
    """Filter to validate an Execution Environment against a list of regexes.
    If one regex matches, the EE is allowed.
    If no match found, the EE is refused.
    'name' and 'image' keys cannot be defined at the same time in agnosticV.
    This test returns False in that case.
    Return True (allowed) or False (not allowed)."""
    function_name = "ee_is_allowed"

    if not isinstance(ee, dict):
        raise AnsibleFilterError(
            '%s: dict expected for Execution Environment' %(function_name))

    if not isinstance(allow_list, list):
        raise AnsibleFilterError(
            '%s: list expected for Execution Environment Allow list' %(function_name))

    if len(allow_list) == 0:
        return True

    if 'name' in ee and 'image' in ee:
        return False
    if 'name' in ee and 'pull' in ee:
        return False

    # Set default values in ee
    ee = deepcopy(ee)
    if 'pull' not in ee:
        ee['pull'] = 'missing'
    if 'private' not in ee:
        # Default to false
        ee['private'] = False
    else:
        ee['private'] = sanitize_bool(ee['private'])

    for v in allow_list:
        for k in v:
            if k not in ee:
                break

            if k == 'private':
                v[k] = sanitize_bool(v[k])
                if not isinstance(v[k], bool):
                    raise AnsibleFilterError("%s: wrong type '%s' for private, expect bool" %(function_name, v[k]))
                if v[k] != ee[k]:
                    break
            elif isinstance(v[k], str):
                regex = v[k]
                try:
                    p = re.compile(regex)
                    if not p.match(ee[k].strip()):
                        break
                except Exception as err:
                    raise AnsibleFilterError("%s: wrong regex '%s'" %(function_name, regex))
            else:
                raise AnsibleFilterError("%s: unexpected type for '%s'" %(function_name, v[k]))

        else:
            return True

    return False

# Ansible filters ----
class FilterModule(object):
    ''' URI filter '''

    def filters(self):
        return {
            'ee_is_allowed': ee_is_allowed,
        }
