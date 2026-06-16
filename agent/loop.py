import json

from agent.llm import call_llm
from tools.registry import TOOLS
from schemas.agent_schema import SYSTEM_PROMPT

MAX_STEPS = 5


def run_agent(user_query):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_query
        }
    ]

    for step in range(MAX_STEPS):

        response = call_llm(messages)

        print("\n" + "=" * 50)
        print(f"STEP {step + 1}")
        print(response)
        print("=" * 50)

        try:
            data = json.loads(response)
        except Exception:
            return "Invalid JSON returned by LLM"

        if data["type"] == "final":
            return data["output"]

        if data["type"] == "tool":

            tool_name = data["name"]
            args = data["args"]

            tool_function = TOOLS[tool_name]

            result = tool_function(**args)

            print("\nTOOL RESULT:")
            print(result)

            messages.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )

            messages.append(
                {
                    "role": "user",
                    "content": f"""
Tool execution completed.

Tool Name: {tool_name}

Tool Result:
{result}

Based on this result:
1. Call another tool if needed
2. Otherwise return a final answer

Return JSON only.
"""
                }
            )

    return "Agent failed to find a solution within the step limit."