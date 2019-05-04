import mysql.connector
import bs4 as bs
import urllib

sauce = urllib.urlopen('http://acceptinglocations.com/rcard/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')



def main():

	connection = mysql.connector.connect(host='localhost',
	                             database='testdb',
	                             user='admin',
	                             password='rollinseats')

	restaurants = [[],[],[],[]]

	for name in soup.find_all('h4'):
		restaurants[0].append(name.string)

	for phone in soup.find_all('strong'):
		restaurants[1].append(phone.text)

	for address in soup.find_all('p'):
		soup.find('strong').decompose()
		restaurants[2].append(address.text)

	for url in soup.find_all('a'):
		if "#" not in url.get('href') and "https://rollins" not in url.get('href'):
			restaurants[3].append(url.get('href'))

	for i in range(len(restaurants[0])):
		insertIntoDatabase(connection, restaurants[0][i], restaurants[1][i], restaurants[2][i])



def insertIntoDatabase(connection, name, number, addr):
	name = name
	number = number
	addr = addr

	mycursor = connection.cursor()
	sql = "INSERT INTO testrest6 (name, phone_number, address, lat, lng, marker_icon_link, tag) VALUES (%s, %s, %s, NULL, NULL, NULL, NULL)"
	val = (name, number, addr)
	mycursor.execute(sql, val)

	connection.commit()

if (__name__ == '__main__'):
	main()
