def check(regex, index, word, startflag, endflag):
    if index == len(regex):
        if endflag == 1 and len(word) == 0:
            return True
        elif endflag == 1 and len(word) != 0:
            return check(regex, 0, word[1:], startflag, endflag)
        else:
            return True
    elif index != len(regex) and len(word) == 0:
        return False
    elif regex[0] == "^" and regex[-1] == "$":
        return check(regex[1:-1], index, word, 1, 1)
    elif regex[0] == "^":
        return check(regex[1:], index, word, 1, endflag)
    elif regex[-1] == "$":
        return check(regex[:-1], index, word, startflag, 1)
    elif regex[index] == "\\":
        if regex[index+1] == word[0]:
            return check(regex, index + 2, word[1:], startflag, endflag)
        else:
            return check(regex, 0, word[1:], startflag, endflag)
    elif len(regex) >= 2 and index < len(regex) - 1 and regex[index + 1] == "?":
        if regex[index] == "." or regex[index] == word[0]:
            return check(regex, index + 2 , word[1:], startflag, endflag)
        else:
            return check(regex, index + 2, word, startflag, endflag)
    elif len(regex) >= 2 and index < len(regex) - 1 and regex[index + 1] == "*":
        if regex[index] == "." or regex[index] == word[0]:
            return check(regex, index, word[1:], startflag, endflag) or check(regex[0:index+1] + "?" + regex[index+2:], index, word, startflag, endflag)
        else:
            return check(regex, index+2, word, startflag, endflag)
    elif len(regex) >= 2 and index < len(regex) - 1 and regex[index + 1] == "+":
        if regex[index] == "." or regex[index] == word[0]:
            return check(regex, index, word[1:], startflag, endflag) or check(regex[0:index+1] + "?" + regex[index+2:], index, word, startflag, endflag)
        else:
            if startflag == 1:
                return False
            else:
                return check(regex, 0, word[1:], startflag, endflag)
    elif regex[index] == "." or regex[index] == word[0]:
        return check(regex, index + 1, word[1:], startflag, endflag)
    else:
        if startflag == 1:
            return False
        else:
            return check(regex, 0, word[1:], startflag, endflag)

z = input().split("|")
print(check(z[0], 0, z[1], 0, 0))




