print("Enter all obtained info on the target, Enter ! to fill null field.")


open('data.text', 'w').close()

#input
f = open('data.text', "a")
fname = raw_input("First Name: ")	
if fname != '!':
	f.write(fname)
	f.write('\n')

f = open('data.text', "a")
lname = raw_input("Last Name: ")
if lname != '!':
	f.write(lname)
	f.write('\n')

while True:
	f = open('data.text', "a")
	impnum = raw_input("Important number sequences (anniversary, date of birth, graduation, etc):  ")
	if impnum == '!':
		break
	f.write(impnum)
	f.write('\n')

f = open('data.text', "a")
spouse = raw_input("Significant Other: ")
if spouse != '!':
	f.write(spouse)
	f.write('\n')

f = open('data.text', "a")
pet = raw_input("Pet Name: ")
if pet != '!':
	f.write(pet)
	f.write('\n')

while True:
	f = open('data.text', "a")
	kid = raw_input("Child's Name: ")
	if kid == '!':
		break
	f.write(kid)
	f.write('\n')


f = open('data.text', "a")
color = raw_input("Favorite Color: ")
if color != '!':
	f.write(color)
	f.write('\n')

while True:
	f = open('data.text', "a")
	hob = raw_input("Enter Interest: ")
	if hob == '!':
		break
	f.write(hob)
	f.write('\n')





