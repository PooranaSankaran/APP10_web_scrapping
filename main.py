import  requests
import selectorlib
import smtplib,ssl

url = 'http://programmer100.pythonanywhere.com/tours/'

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source

# In the web site we use view sources code to view in html
# we find that our extracting tour is placed in tour key word in the html file
def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['tours']
    return value

#send mail if you got a scrape
def send_mail():

    host = 'smpt.gmail.com'
    port = 465

    username = 'app8flask@gmail.com'
    password = 'ecefefrfedwwd'

    recevier = 'app8flask@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context)
        server.login(username, password)
        server.sendmail(username, recevier, message)
    print('Email was sent!')

def store(extracted):
    with open('data.txt', 'w') as file:
        file.write(extracted + '\n')

def read(extracted):
    with open('data.txt', 'r') as file:
        return file.read()

if __name__ == '__main__':
    # set while = True if you need no stop runing.
    scraped = scrape(url)
    extracted = extract(scraped)
    print(extracted)
    store(extracted)
    content = read(extracted)
    if extracted != 'No upcoming tours':
        if extracted not in content:
            send_mail()