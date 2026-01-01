# -------------------------------
# Rule-Based Expert System
# Forward Chaining
# -------------------------------

# Rules: IF conditions THEN conclusion
rules = [
    {
        "if": ["fever", "cough"],
        "then": "flu"
    },
    {
        "if": ["flu", "body_pain"],
        "then": "viral_infection"
    },
    {
        "if": ["viral_infection"],
        "then": "consult_doctor"
    }
]

# Facts base
facts = set()

# Reasoning log
log = []

# Accept user input
user_input = input("Enter symptoms (comma separated): ")
for symptom in user_input.split(","):
    facts.add(symptom.strip())

# Forward chaining inference
new_inference = True

while new_inference:
    new_inference = False

    for rule in rules:
        # Check if all conditions are true
        if all(condition in facts for condition in rule["if"]):
            conclusion = rule["then"]

            # If conclusion not already inferred
            if conclusion not in facts:
                facts.add(conclusion)
                new_inference = True

                # Log the inference
                log.append(
                    f"Applied rule: IF {rule['if']} THEN {conclusion}"
                )

# Output results
print("\n--- Inference Log ---")
for step in log:
    print(step)

print("\n--- Final Facts ---")
for fact in facts:
    print(fact)
