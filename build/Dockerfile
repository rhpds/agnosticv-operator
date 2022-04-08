FROM quay.io/operator-framework/ansible-operator:v1.18.1

USER root

RUN yum install -y git
RUN yum clean all
COPY ipa.crt /etc/pki/ca-trust/source/anchors/
RUN update-ca-trust

USER ${USER_UID}

RUN curl --silent --location \
    -o ${HOME}/agnosticv_cli \
    https://github.com/redhat-cop/agnosticv/releases/download/v0.3.3/agnosticv_linux_amd64
RUN chmod +x ${HOME}/agnosticv_cli

COPY ansible.cfg /etc/ansible/ansible.cfg
COPY watches.yaml ${HOME}/watches.yaml
COPY playbook.yaml ${HOME}/playbook.yaml
COPY roles/ ${HOME}/roles/
