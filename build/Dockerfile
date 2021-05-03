FROM quay.io/operator-framework/ansible-operator:v1.4.2

USER root

RUN yum install -y git
RUN yum clean all

USER ${USER_UID}

RUN curl --silent --location \
    -o ${HOME}/agnosticv_cli \
    https://github.com/redhat-cop/agnosticv/releases/download/v0.2.0/agnosticv_linux_amd64
RUN chmod +x ${HOME}/agnosticv_cli

COPY ansible.cfg /etc/ansible/ansible.cfg
COPY watches.yaml ${HOME}/watches.yaml
COPY playbook.yaml ${HOME}/playbook.yaml
COPY roles/ ${HOME}/roles/
