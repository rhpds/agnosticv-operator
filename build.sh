#!/bin/bash
echo -n "Version: "
read VERSION

set -xeuo pipefail

# Now build the Operator
operator-sdk build quay.io/redhat-gpte/agnosticv-operator:${VERSION}

docker push quay.io/redhat-gpte/agnosticv-operator:${VERSION}
