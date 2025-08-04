import subprocess

def ask_sael(prompt):
    # Run Ollama with your prompt
    result = subprocess.run(
        ["ollama", "run", "openhermes"],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )

    # Extract only the reply part
    output = result.stdout.decode()
    reply = output.split(">>>")[-1].strip()  # Remove model boilerplate
    return reply