import re
new_string = []
with open("arch_ejer3.txt", "r") as f:
	content = f.read()
   
new_string = re.findall('[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}', content)

print(new_string)

#Devolvió esto ['qIQNlQSLi', 'eOEKiVEYj', 'aZADnMCZq', 'bZUTkLYNg', 'uCNDeHSBj', 'kOIXdKBFh', 'dXJVlGZVm', 'gZAGiLQZx', 'vCJAsACFl', 'qKWGtIDCj']
#Si leeamos las letras minúsculas del centro dice 'linkedlist'.
#linkedlist.html = linkedlist.php