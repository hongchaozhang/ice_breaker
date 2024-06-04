import openai


def azure_openai_tester():
    client = openai.AzureOpenAI(
        api_key="b7ad46f3bc944a15a4ae018782505737",
        api_version="2023-05-15",
        azure_endpoint="https://test-ai.azure-api.net"
    )
    system_message = 'You are an assistant for daily work.'
    user_message = 'hello'
    messages = [{"role": "system", "content": system_message},
                {"role": "user", "content": user_message}]
    response = client.chat.completions.create(
        model='gpt-35-turbo-16k',
        messages=messages,
    )
    print(response.choices[0].message.content)


def aigc2d_openai_tester():
    client = openai.OpenAI(
        api_key="AIGC10470-dbpg1wwdde1m752QVYwwasp0bveuTn",
        base_url="https://api.aigc2d.com/v1"
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hi,AIGC2D"}],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    # azure_openai_tester()
    aigc2d_openai_tester()