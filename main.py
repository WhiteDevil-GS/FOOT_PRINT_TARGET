
import re
import requests
from bs4 import BeautifulSoup
from collections import Counter
import socket
import ssl
import csv
url = "https://www.google.com"
def domain_detect(lst):
    exact_domain = highest_word_in_list(lst)
    return exact_domain
    
    
def highest_word_in_list(lst):
    try:
        srt_list = sorted(lst)
        string_counts = Counter(srt_list)
        most_common_string = string_counts.most_common(1)[0][0]
        return most_common_string
    except Exception as e:
        print(e)

def url_domain(url):

    
    if dom := re.search(r".*\.(.+\.(com|edu|gov|net|org)?).*",url, re.IGNORECASE):
        return dom.group(1)

def ip_adress(domain_name):
     try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
     except Exception as e:
        print(e)

def href_links_import(url):
      domain_list = []
      response = requests.get(url)
      if response.status_code == 200:
         soup = BeautifulSoup(response.text, 'html.parser')
         link = soup.find('a', href=True)
         html_content = str(soup)
         href_pattern = r'href=["\'](https?://[^"\']+)["\']'
         href_links = re.findall(href_pattern, html_content)
      for link in href_links:
          if lnk := re.search(r".*\.(.+\.com).*",str(link),re.IGNORECASE):
              domain_list.append(lnk.group(1))
      return domain_list,href_links
      
def title_extract(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.get_text()
        return title

def ssl_certificate_extract(url):
    hostname = url.split('://')[1].split('/')[0]
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
           cert = ssock.getpeercert()
           subject = dict(x[0] for x in cert['subject'])
           issuer = dict(x[0] for x in cert['issuer'])
           contry_name = issuer['countryName']
           common_name = subject['commonName']
           serialNumber = cert['serialNumber']
           r = cert['subjectAltName']
           dns_server = r[0][1]
           
           return contry_name,common_name,serialNumber,dns_server
           


def choice(ch,ip,conty,comm,seri,dns,tit,dom,herf):
    try:
        

        if ch == 1:
            print("\n"+"[+]- IP :",ip)
        if ch == 2:
            print("\n"+"[+]- Contry_Name :",conty)
            print("\n"+"[+]- Common_Name :",comm)
            print("\n"+"[+]- Serial_Number:",seri)
            print("\n"+"[+]- Dns_Server:",dns)
        if ch == 3:
            print("\n"+"[+]- Title:",tit)
        if ch == 4:
            print("\n"+"[+]- Domain:",dom)
        if ch == 5:
            print("\n"+"[+]- Href Links:")
            for i in herf:
                print("\n"+str(i))
        if ch == 99:
            exit(0)
        
    except Exception as e:
        print(e)
try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    domain_lst,lis_herf = href_links_import(url)
    exact_domain = domain_detect(domain_lst)
    title = title_extract(url)
    ip_adress = ip_adress(str(url).removeprefix("https://"))
    contry_name,common_name,serialNumber,dns_server = ssl_certificate_extract(url)
    print(response,"\n")
    ch = int(input())
    choice(ch,ip_adress,contry_name,common_name,serialNumber,dns_server,title,exact_domain,lis_herf)
except Exception as e:
    print(e)

