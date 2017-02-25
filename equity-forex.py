# Equity Forex Exchange Rates
#
# Mohammed Sohail <sohailsameja@gmail.com>
# Released Under AGPL-3.0 License

# import required modules
from prettytable import PrettyTable
from time import strftime
from requests import get
from lxml import html

# send GET request to Equity Banks website 
equity_bank_website = get('http://ke.equitybankgroup.com/').content

# parse the HTML with lxml library
parser = html.fromstring(equity_bank_website)

# strip the data
currency_code = parser.xpath('//span[@class="user-currency"]/text()')
price = parser.xpath('//span[@class="currency-value"]/text()')

# iterate over data
currency_codes = [i.replace('\n', '').replace(' ', '').replace(':', '') for i in currency_code]
prices = [i.replace(' ', '').replace(':', '').replace('Buying', '').replace('Selling', '') for i in price]

# split at specific index points
buying_prices = prices[::2]
selling_prices = prices[1::2]

# tabulate the data
table = PrettyTable()

table.add_column('Currency',currency_codes)
table.add_column('Buying',buying_prices)
table.add_column('Selling',selling_prices)

# Output to console
header = '''
Equity Bank Foreign Exchange Rates

{}

'''

print(header.format(strftime('%Y-%m-%d %H:%M')) + table.get_string())
