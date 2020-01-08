def isValid(p):
    if ((p[0] == p[1] and p[1] != p[2]) or
        (p[0] != p[1] and p[1] == p[2] and p[2] != p[3]) or
        (p[1] != p[2] and p[2] == p[3] and p[3] != p[4]) or
        (p[2] != p[3] and p[3] == p[4] and p[4] != p[5]) or
        (p[4] == p[5] and p[4] != p[3])):
            return True
    return False
        

def hasRepeated(p):
    if (p[0] == p[1]or p[1] == p[2] or p[2] == p[3] or p[3] == p[4] or p[4] == p[5]):
        return True
    return False

def notDecreasing(p):
    if (p[0] <= p[1] <= p[2] <= p[3] <= p[4] <= p[5]):
        return True
    return False
    
def main():
    start = 248345
    end = 746315
    part1 =  0
    part2 = 0
    passwords = list(range(start, end))
    passwords = [str(password) for password in passwords]
    for password in passwords:
        if (hasRepeated(password) and notDecreasing(password)):
            part1+=1
            part2+=1
            if not (isValid(password)):
                part2-=1
    print("Part 1: ", part1)
    print("Part 2: ", part2)

if __name__ == '__main__':
    main()