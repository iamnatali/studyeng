import requests

if __name__ == '__main__':
    headers = {'Secret': '42'}
    proxies = {
    "http":"http://marideldaicher@f36854pi_f36854@proxy.server:3128"
    }
    r = requests.get('https://marideldaicher.pythonanywhere.com/categories/',
                     headers=headers, proxies=proxies)
    print(r.text)


