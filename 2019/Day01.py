def main():
     masses = []
     with open('input.txt') as f:
             for line in f.readlines():
                     masses.append(line.strip())
     masses = [int(mass) for mass in masses]
     fuel =  0
     for mass in masses:
              fuel += (mass //3) - 2
     print(fuel)                ## Part 1

     total_fuel = 0
     for mass in masses:
               total_fuel += get_fuel_per_mass(mass)
     print(total_fuel)          ##Part 2

def get_fuel_per_mass(mass):
    if (mass <= 5):             ##base case is 5 since 5//3 - 2 is -1
        return 0
    else:
        mass = int(mass//3) - 2
        return mass + get_fuel_per_mass(mass)

if __name__ == '__main__':
    main()