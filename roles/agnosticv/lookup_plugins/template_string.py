# Copyright: (c) 2021, Johnathan Kupferer <jkupfere@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
    lookup: template_string
    author: Johnathan Kupferer <jkupfere@redhat.com>
    version_added: "2.9"
    short_description: 
    description:
      - Return evaluation of template
    options:
      _terms:
        description: list of templates
"""

EXAMPLES = """
- name: show templating results
  debug:
    msg: "{{ lookup('template_string', '{{ foo }}-{{ bar }}') }}"
"""

RETURN = """
_raw:
   description: boolean result of conditional evaluation
"""

from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):
    def run(self, terms, variables, **kwargs):
        return [ self._templar.template(str(term)) for term in terms ]
