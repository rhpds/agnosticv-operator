#!/bin/bash
VERSION=${VERSION:-v0.0.17}

# Now build the Operator
operator-sdk build quay.io/gpte-devops-automation/agnosticv-operator:${VERSION}

docker push quay.io/gpte-devops-automation/agnosticv-operator:${VERSION}
