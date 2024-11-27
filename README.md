# LLM Deployer

Deploy LLM on OpenShift

## Prerequisite

1. OpenShift 4.16+
2. OpenShift AI 2.13+

## Build

```shell
# replace jkeam with your own name
podman build -t quay.io/jkeam/llm-deployer
podman push -t quay.io/jkeam/llm-deployer
```

## Deploy on OpenShift

```shell
oc apply -k ./openshift
```
