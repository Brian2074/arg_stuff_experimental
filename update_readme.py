import datetime

readme_path = "README.md"
start_tag = "<!--START_SECTION:time-->"
end_tag = "<!--END_SECTION:time-->"
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

start_index = content.find(start_tag) + len(start_tag)
end_index = content.find(end_tag)

new_content = (
    content[:start_index]
    + "\n"
    + f"> Updated at {now}"
    + "\n"
    + content[end_index:]
)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(new_content)
