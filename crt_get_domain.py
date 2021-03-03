import requests
from bs4 import BeautifulSoup
import sys
import re

if __name__ == '__main__':

    url = "https://crt.sh/?q="

    target = sys.argv[1]
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    final = url+target
    print(final)
    response = requests.get(final,headers=header)
    result = response.content.decode()
    domain = []
    repeat = []
    #print(result)
    Match_domain = ".*?\."+target
    print(Match_domain)
    # domain_infomation = re.findall(r'.*?\.com', result)
    domain_infomation = re.findall(Match_domain, result)
    # print(domain_infomation)
    for i in domain_infomation:
        temp = i.replace("<BR>","")
        temp_TD = temp.replace("<TD>","")
        temp_br = temp_TD.replace(" ","")
        print(temp_br)
        temp_repeat = temp_br.split('.')
        if temp_repeat[0] != "*":
            if temp_repeat[0] in repeat:
                continue
            else:
                repeat.append(temp_repeat[0])
                domain.append(temp_br)
            # domain.append()
        else:
            if temp_repeat[1] in repeat:
                continue
            else:
                repeat.append(temp_repeat[1])
                domain.append(temp_br)
    # print(repeat)
    print(domain)