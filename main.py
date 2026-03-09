def convert_markdown_to_html(text):
    lines = text.split("\n")
    html = []

    for line in lines:
        if line.startswith("# "):
            html.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            html.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("### "):
            html.append(f"<h3>{line[4:]}</h3>")
        else:
            html.append(f"<p>{line}</p>")

    return "\n".join(html)


input_file = input("Enter markdown file: ")
output_file = "output.html"

try:
    with open(input_file, "r") as f:
        md_text = f.read()

    html_text = convert_markdown_to_html(md_text)

    with open(output_file, "w") as f:
        f.write(html_text)

    print("Conversion successful!")
    print("Output saved to:", output_file)

except FileNotFoundError:
    print("File not found.")
