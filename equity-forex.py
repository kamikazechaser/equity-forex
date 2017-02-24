# Import required modules
from bs4 import BeautifulSoup
from tabulate import tabulate
from requests import get
import time

# send GET request to Equity Banks website
equity_bank_website = get('http://ke.equitybankgroup.com').text

# parse the HTML with beautifulsoup
parser = BeautifulSoup(equity_bank_website, 'html.parser')

# strip the data
data = parser.find('marquee').find_all('span')

#USD/KES
usdkes_tag = data[0].text.strip().replace('\n','').replace(' ','').replace(':', '')
usdkes_buying = data[1].text.strip().replace('Buying: ', '')
usdkes_selling = data[2].text.strip().replace('Selling: ', '')

# GBP/KES
gbpkes_tag = data[3].text.strip().replace('\n','').replace(' ','').replace(':', '')
gbpkes_buying = data[4].text.strip().replace('Buying: ', '')
gbpkes_selling = data[5].text.strip().replace('Selling: ', '')

# EUR/KES
eurkes_tag = data[6].text.strip().replace('\n','').replace(' ','').replace(':', '')
eurkes_buying = data[7].text.strip().replace('Buying: ', '')
eurkes_selling = data[8].text.strip().replace('Selling: ', '')

# ZAR/KES
zarkes_tag = data[9].text.strip().replace('\n','').replace(' ','').replace(':', '')
zarkes_buying = data[10].text.strip().replace('Buying: ', '')
zarkes_selling = data[11].text.strip().replace('Selling: ', '')

# JPY/KES
jpykes_tag = data[12].text.strip().replace('\n','').replace(' ','').replace(':', '')
jpykes_buying = data[13].text.strip().replace('Buying: ', '')
jpykes_selling = data[14].text.strip().replace('Selling: ', '')

# CHF/KES
chfkes_tag = data[15].text.strip().replace('\n','').replace(' ','').replace(':', '')
chfkes_buying = data[16].text.strip().replace('Buying: ', '')
chfkes_selling = data[17].text.strip().replace('Selling: ', '')

# CAD/KES
cadkes_tag = data[18].text.strip().replace('\n','').replace(' ','').replace(':', '')
cadkes_buying = data[19].text.strip().replace('Buying: ', '')
cadkes_selling = data[20].text.strip().replace('Selling: ', '')

# AUD/KES
audkes_tag = data[21].text.strip().replace('\n','').replace(' ','').replace(':', '')
audkes_buying = data[22].text.strip().replace('Buying: ', '')
audkes_selling = data[23].text.strip().replace('Selling: ', '')

# UGX/KES
ugxkes_tag = data[24].text.strip().replace('\n','').replace(' ','').replace(':', '')
ugxkes_buying = data[25].text.strip().replace('Buying: ', '')
ugxkes_selling = data[26].text.strip().replace('Selling: ', '')

# SSP/KES
sspkes_tag = data[27].text.strip().replace('\n','').replace(' ','').replace(':', '')
sspkes_buying = data[28].text.strip().replace('Buying: ', '')
sspkes_selling = data[29].text.strip().replace('Selling: ', '')

# SEK/KES
sekkes_tag = data[30].text.strip().replace('\n','').replace(' ','').replace(':', '')
sekkes_buying = data[31].text.strip().replace('Buying: ', '')
sekkes_selling = data[32].text.strip().replace('Selling: ', '')

# NOK/KES
nokkes_tag = data[33].text.strip().replace('\n','').replace(' ','').replace(':', '')
nokkes_buying = data[34].text.strip().replace('Buying: ', '')
nokkes_selling = data[35].text.strip().replace('Selling: ', '')

# DKK/KES
dkkkes_tag = data[36].text.strip().replace('\n','').replace(' ','').replace(':', '')
dkkkes_buying = data[37].text.strip().replace('Buying: ', '')
dkkkes_selling = data[38].text.strip().replace('Selling: ', '')

# RWF/KES
rwfkes_tag = data[39].text.strip().replace('\n','').replace(' ','').replace(':', '')
rwfkes_buying = data[40].text.strip().replace('Buying: ', '')
rwfkes_selling = data[41].text.strip().replace('Selling: ', '')

# TZS/KES
tzskes_tag = data[42].text.strip().replace('\n','').replace(' ','').replace(':', '')
tzskes_buying = data[43].text.strip().replace('Buying: ', '')
tzskes_selling = data[44].text.strip().replace('Selling: ', '')

# CNY/KES
cnykes_tag = data[45].text.strip().replace('\n','').replace(' ','').replace(':', '')
cnykes_buying = data[46].text.strip().replace('Buying: ', '')
cnykes_selling = data[47].text.strip().replace('Selling: ', '')

# Tabulate the data
table = [
        [usdkes_tag,usdkes_buying,usdkes_selling],
        [gbpkes_tag,gbpkes_buying,gbpkes_selling],
        [eurkes_tag,eurkes_buying,eurkes_selling],
        [zarkes_tag,zarkes_buying,zarkes_selling],
        [jpykes_tag,jpykes_buying,jpykes_selling],
        [chfkes_tag,chfkes_buying,chfkes_selling],
        [cadkes_tag,cadkes_buying,cadkes_selling],
        [audkes_tag,audkes_buying,audkes_selling],
        [ugxkes_tag,ugxkes_buying,ugxkes_selling],
        [sspkes_tag,sspkes_buying,sspkes_selling],
        [sekkes_tag,sekkes_buying,sekkes_selling],
        [nokkes_tag,nokkes_buying,nokkes_selling],
        [dkkkes_tag,dkkkes_buying,dkkkes_selling],
        [rwfkes_tag,rwfkes_buying,rwfkes_selling],
        [tzskes_tag,tzskes_buying,tzskes_selling],
        [cnykes_tag,cnykes_buying,cnykes_selling]]

# Output to console
header = '''
Equity Bank Foreign Exchange Rates

{}

'''

print(header.format(time.strftime("%Y-%m-%d %H:%M")) + tabulate(table, headers=['Currency','Buying','Selling']))
