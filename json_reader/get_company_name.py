import anthropic

def get_company_name_func(company_name,api_key):
    
    client = anthropic.Anthropic(api_key=api_key)

    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=4096,
        temperature=0,
        system="give me only,nothing extra, the full name, ticker, exchange it is listed in json format. If you did not find anything, return none. ",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": company_name
                    }
                ]
            }
        ]
    )

    return(message.content)