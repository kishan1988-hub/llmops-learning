# You need to respond in under 2 seconds for 95% of queries.
# A typical response is 200 tokens.
# Calculate what minimum tokens/sec your GPU needs.
#
# Then check if these GPUs meet the requirement:
gpu_specs = [
    ("MacBook Apple GPU",  41),
    ("AWS g4dn.xlarge",   380),
    ("AWS p3.2xlarge",    950),
    ("A100 on EKS",      2100),
]

response_token = 200
sla_seconds = 2

min_tps = response_token / sla_seconds
print(f"Minimum required: {min_tps} t/s to meet {sla_seconds}s SLA \n")
# Print which GPUs pass and which fail the 2-second SLA
# Expected output:
# MacBook Apple GPU  : 41 t/s   → FAIL (4.88s for 200 tokens)
# AWS g4dn.xlarge    : 380 t/s  → PASS (0.53s for 200 tokens)
# AWS p3.2xlarge     : 950 t/s  → PASS (0.21s for 200 tokens)
# A100 on EKS        : 2100 t/s → PASS (0.10s for 200 tokens)

for gpu_name, tokens_per_second in gpu_specs:
    time_for_200_tokens = 200 / tokens_per_second
    status = "PASS" if time_for_200_tokens <= 2 else "FAIL"
    print(f"{gpu_name:<20}: {tokens_per_second:<5} t/s → {status} ({time_for_200_tokens:.2f}s for 200 tokens)")
