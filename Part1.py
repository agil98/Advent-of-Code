def main():
     masses = []
     with open('input.txt') as f:
             for line in f.readlines():
                     masses.append(line.strip())
     masses = [int(mass) for mass in masses]
     fuel =  0
     for mass in masses:
              fuel += (mass //3) - 2
      print(fuel)
