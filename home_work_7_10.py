#-------Задание №7-----------------

american_date = '13.05.2016'
day = str (american_date[0:2])
mounth = str (american_date[3:5])
year = str (american_date [6:])
print('American format:',american_date)
print ('Europian format: %s.%s.%s' % (mounth,day,year))

#--------Задание №8----------------

name = ('Mark Zuckerberg')
name_split = name.split(' ')
name_split = name_split[::-1]
name2 = ' '.join(name_split)
print(name2)

#--------Задание №9----------------

snake2camel = ('employee_first_name')
split = snake2camel.split('_')
word1 = str(split[0]).capitalize()
word2 = str(split[1]).capitalize()
word3 = str(split[2]).capitalize()
camel = word1 + word2 + word3
print(camel)

#-------Задание №10-----------------


info = "Leo Tolstoy*1828-08-28*1910-11-20"
info_split = info.split('*')
persons_name = info_split[0]
birth_date = info_split[1]
death_date = info_split[2]
birth_split = birth_date.split("-")
death_split = death_date.split("-")
birth_year = int(birth_split[0])
death_year = int(death_split[0])
age = death_year - birth_year
print("%s , %d" % (persons_name, age))