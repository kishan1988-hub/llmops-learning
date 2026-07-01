# A GCC is evaluating two LLM providers.
# Write a script that calculates and compares the monthly cost.
#
# Given:
input_tokens_per_day  = 500000    # tokens sent to the model
output_tokens_per_day = 150000    # tokens received from the model
days_per_month        = 30

# Provider A — AWS Bedrock (Claude Haiku)
bedrock_input_price   = 0.00025   # $ per 1000 tokens
bedrock_output_price  = 0.00125   # $ per 1000 tokens

# Provider B — OpenAI GPT-4o-mini
openai_input_price    = 0.00015
openai_output_price   = 0.00060

# Your task:
# 1. Calculate monthly cost for Provider A
# 2. Calculate monthly cost for Provider B
# 3. Calculate the savings if you pick the cheaper one
# 4. Print a formatted summary like this:
#
# === Monthly LLM Cost Comparison ===
# AWS Bedrock  : $312.50
# OpenAI       : $183.75
# Savings      : $128.75 (41.2% cheaper with OpenAI)

cost_provider_a = ((input_tokens_per_day * bedrock_input_price / 1000) +(output_tokens_per_day * bedrock_output_price /1000)) * days_per_month
cost_provider_b = ((input_tokens_per_day * openai_input_price /1000)+ (output_tokens_per_day * openai_output_price /1000)) * days_per_month


if cost_provider_a < cost_provider_b:
    cheaper_provider = "AWS bedrock"
    savings = cost_provider_b - cost_provider_a
    savings_percentage = (savings / cost_provider_b) * 100
else:
    cheaper_provider = "OpenAI"
    savings = cost_provider_a - cost_provider_b
    savings_percentage = (savings / cost_provider_a) * 100

print(f"=== Monthly LLM Cost comparison ===")
print(f"AWS Bedrock : ${cost_provider_a:.2f}")
print(f"OpenAI : ${cost_provider_b:.2f}")
print(f"Savings : ${savings:.2f} ({savings_percentage:.2f}% cheaper with {cheaper_provider})")
