import os


def get_header():
    hd = os.open('./static/shared/header.html', os.O_RDONLY)
    header = os.read(hd, 5000)
    os.close(hd)
    return header


def get_footer():
    ft = os.open('./static/shared/footer.html', os.O_RDONLY)
    footer = os.read(ft, 5000)
    os.close(ft)
    return footer
