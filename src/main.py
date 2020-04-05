import re


def run():
    # Start coding here
    text = ''
    regex = re.compile(r'[a-zA-Z]')
    with open('./src/encoded.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    message = ''.join(re.findall(regex, text))

    return message


if __name__ == '__main__':
    run()
