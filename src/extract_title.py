def extract_title(markdown):
    for line in markdown.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No title found")
