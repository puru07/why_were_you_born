#!/usr/bin/env python

#this script gets info about the christiano ronaldo from wikipedia
from lxml import html
import requests
import sys
import calendar
from datetime import date 
from datetime import timedelta as td
print 'tell me the birth date in ddmmyyy format'

full_date = raw_input()

if len(full_date) != 8:
	print 'date is in wrong format'
	sys.exit()
day = int(full_date[0] + full_date[1])
month = int(full_date[2] + full_date[3])
year = int(full_date[4] + full_date[5] + full_date[6] + full_date[7]) 

event_month = 0

# making the date object
date_formatted = date(year,month,day)

# getting the date of event
date_formatted = date_formatted + td(days = -280)


# Lets do the search
day_delta = 1
	
while True: 
	#getting the name of the month
	monthname = calendar.month_name[date_formatted.month]
	#searching wikipedia
	page = requests.get('https://en.wikipedia.org/wiki/%s'  % str(date_formatted.year) )
	#creating XPath tree out of it
	tree = html.fromstring(page.content)

	#parsing the tree 
	# visit http://www.w3schools.com/xsl/xpath_nodes.asp for syntaxes 
	# for specifying address of a tree node
	monthday = str(monthname + " " + str(date_formatted.day))
	input_data ='//ul[following-sibling::h2[child::span[@id = "Births"]]]/li[child::a[@title = "%s"]]//text()' % monthday
	event = tree.xpath(input_data)
	str_of_event = ""

	# getting data out of event
	for tagn in range(2,len(event)):
		try:
			tag_data = str(event[tagn])
			if "\n" in tag_data:
				break
			if monthday in tag_data:
				break
			str_of_event = str_of_event + tag_data
			

		except UnicodeEncodeError: 
			continue

	if str_of_event is "":
		pass

	else:
		print "the date, around 280 days before you were born"
		print monthday
		print "And the event "
		print str_of_event
		break

	#iterating the date
	date_formatted = date_formatted + td(days = day_delta)





