from openai import OpenAI

client = OpenAI(
  api_key=os.environ['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'],  # this is also the default, it can be omitted
)

completion = client.completions.create(model='curie')
print(completion.choices[0].text)
print(dict(completion).get('usage'))
print(completion.model_dump_json(indent=2))