# Ice Breaker

## Description

1. input one the person's name you want to know
2. search the linkedin url of the person
3. get the linkedin profile of the person
4. search the twitter url of the person
5. get the twitter profile and tweets of the person
6. summarize all the info

## How to run

Before running the app, you need to set the environment variables into the `.env` file:

```bash
AZURE_OPENAI_API_KEY="your_openai_api_key"
AZURE_OPENAI_ENDPOINT="https://api.openai.com"
OPENAI_API_VERSION="2020-08-01"

TAVILY_API_KEY="your_tavily_api_key"

PROXYCURL_API_KEY="your_proxycurl_api_key"

# linkedin api keys
...
# twitter api keys
...
```
