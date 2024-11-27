# LLM Deployer

Deploy LLM on OpenShift

## Prerequisite

1. OpenShift 4.16+
2. OpenShift AI 2.13+

## Build

```shell
# replace jkeam with your own name
podman build -t quay.io/jkeam/llm-deployer -f ./Dockerfile .
podman push quay.io/jkeam/llm-deployer
```

## Deploy on OpenShift

```shell
cp ./.env.example ./.env  # then update .env with real values
oc apply -k ./openshift
```
