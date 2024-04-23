import os
import markdown


def readfile(number: int):
    dirname = f"Proposal/OTP-{number}"
    dir = os.listdir(dirname)
    cfg = dict()

    if 'index.html' in dir:
        read_html(dirname)
    elif 'index.md' in dir:
        read_md(dirname)


def read_html(dirname):
    pass


def read_md(dirname):
    with open(f"{dirname}/index.md") as f:
        mdcode = f.read()
    htmlcode = markdown.markdown(mdcode)
    with open(f"{dirname}/index.html", 'w') as f:
        f.write(htmlcode)

    return read_html(dirname)

