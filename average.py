
# instantiate
sum = 0
count = 0


def inputHandler():
    global sum
    global count
    # input message
    st = "avg({}): {:.3f}, + ".format(count,
                                      (sum/count) if count > 0 else 0)
    string = input(st)
    if (string.lower() == "r"):
        # reset
        sum = 0
        count = 0
    else:
        # normal input
        return string


if __name__ == "__main__":
    # inf loop until break
    while (True):
        try:
            # get input, try cast to float
            number = float(inputHandler())
            # sum total
            sum += number
            # increase counter
            count += 1
        except KeyboardInterrupt:
            print()  # print new line
            break
        except:
            # handle other exception
            pass
