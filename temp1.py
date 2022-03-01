# uid = input("Please Enter Id : ")
# upass = input("please enter pass : ")
with open('one.txt', 'r') as userfile:
    userline = userfile.readline()
    cnt = 0
    while userline:
        lines = ("{}".format(userline.strip()))
        userline = userfile.readline()
        print(userline)
        # if (uid in lines) and (upass in lines):
        #     print('Login Successfull')
        #     break
        # else:
        #     print('Login Unsuccessfull')
        #     break
        cnt += 1
            