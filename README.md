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
cp ./.env.example ./openshift/.env
# then update ./openshift/.env with real values
oc apply -k ./openshift
```

## Testing

### Curl

We can curl the endpoint and chat with it.

```shell
BOT_URL="$(oc get ksvc/granite-predictor -o jsonpath='{.status.url}' -n llm)"
curl -k "$BOT_URL/v1/chat/completions" \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{
            "model": "granite",
            "messages": [
              {"role": "system", "content": "You are a helpful bot.  Do not lie. Talk like a pirate."},
              {"role": "user", "content": "Hi nice to meet you!"}
            ]
        }'
```

### Chatbot App

We can deploy a very simple chatbot to interact with our model once it is deployed.

```shell
oc apply -f ./openshift/chatbot.yaml
BOT_URL="$(oc get ksvc/granite-predictor -o jsonpath='{.status.url}' -n llm)"
oc set env deployment/chatbot MODEL_URL="$BOT_URL/v1" -n llm-chatbot
echo "Open the following in a browser: https://$(oc get routes/chatbot -n llm-chatbot -o jsonpath='{.spec.host}')"
```
