FROM quay.io/operator-framework/ansible-operator:v0.8.1

USER root

RUN yum install -y git
RUN yum clean all

USER ${USER_UID}


COPY ansible.cfg /etc/ansible/ansible.cfg
COPY watches.yaml ${HOME}/watches.yaml
COPY playbook.yaml ${HOME}/playbook.yaml
COPY roles/ ${HOME}/roles/
