import re


def run():
    # Start coding here
    text = ''
    with open('./src/encoded.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    message = ''.join(re.findall(r'\w+(?a)', text))

    return message


if __name__ == '__main__':
    run()
