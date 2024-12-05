def main ():
    tp = "./output/profile/"
    dp = "./output/dp_profile/"
    pp = "./output/pp_profile/"

    file = ["0.txt", "1.txt", "2.txt", "3.txt"]


    for f in file:
        path = tp+f
        with open(path, "w") as frTime:
            frTime.truncate(0)

        path = dp+f
        with open(path, "w") as frTime:
            frTime.truncate(0)

    print("Finish clean records.")
    return 0

if __name__=="__main__": 
    main() 
