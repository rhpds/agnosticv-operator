#!/usr/bin/env python
# Copyright (c) 2022 Red Hat
import re

from copy import deepcopy
__metaclass__ = type

from ansible.errors import AnsibleFilterError

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

    for v in allow_list:
        for k in v:
            if k not in ee:
                break

            regex = v[k]
            try:
                p = re.compile(regex)
                if not p.match(ee[k].strip()):
                    break
            except Exception as err:
                raise AnsibleFilterError("%s: wrong regex '%s'" %(function_name, regex))

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
