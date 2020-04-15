#!/bin/bash
echo -n "Version: "
read VERSION

set -xeuo pipefail

# Now build the Operator
operator-sdk build quay.io/gpte-devops-automation/agnosticv-operator:${VERSION}

docker push quay.io/gpte-devops-automation/agnosticv-operator:${VERSION}

# Build ocp3 compatible image
operator-sdk build --image-build-args "-f build/Dockerfile-ocp3" quay.io/gpte-devops-automation/agnosticv-operator:${VERSION}-ocp3

docker push quay.io/gpte-devops-automation/agnosticv-operator:${VERSION}-ocp3
