new_string = []
with open("arch_ejer2.txt", "r") as f:
    for line in f:
        for char in line:
            if char in "$@?!/_[]())\{\}^*+&%#\n":
                pass    
            else:
                new_string.append(char)

print(new_string)