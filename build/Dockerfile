FROM quay.io/operator-framework/ansible-operator:v1.25.0

USER root

RUN dnf install -y git

# Github CLI

RUN dnf install -y 'dnf-command(config-manager)'
RUN dnf config-manager --add-repo https://cli.github.com/packages/rpm/gh-cli.repo
RUN dnf install -y gh

RUN dnf clean all
COPY ipa.crt /etc/pki/ca-trust/source/anchors/
RUN update-ca-trust

USER ${USER_UID}

RUN curl --silent --location \
    -o ${HOME}/agnosticv_cli \
    https://github.com/redhat-cop/agnosticv/releases/download/v0.7.1/agnosticv_linux_amd64
RUN chmod +x ${HOME}/agnosticv_cli

COPY ansible.cfg /etc/ansible/ansible.cfg
COPY watches.yaml ${HOME}/watches.yaml
COPY playbook.yaml ${HOME}/playbook.yaml
COPY roles/ ${HOME}/roles/
