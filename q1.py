st = '120345678'
goal = '012345678'
todolist = []
todolist.append(st)
count=0
while count < 50:








    st = todolist.pop(0)
    print(st)
    a=st.find('0')
    if a == 2 and st != goal:

        prev = st
        li_list = list(st)
        li_list[1], li_list[2] = li_list[2], li_list[1]
        st = ''.join(li_list)
        todolist.append(st)

        li_list = list(prev)
        li_list[2], li_list[5] = li_list[5], li_list[2]
        st = ''.join(li_list)
        todolist.append(st)
        print(todolist)
    elif a==0 and st != goal:
        prev = st
        li_list = list(st)
        li_list[0], li_list[1] = li_list[1], li_list[0]
        st = ''.join(li_list)
        todolist.append(st)

        li_list = list(prev)
        li_list[0], li_list[3] = li_list[3], li_list[0]
        st = ''.join(li_list)
        todolist.append(st)
        print(todolist)
    elif a == 1 and st != goal:
        prev = st
        li_list = list(st)
        li_list[1], li_list[0] = li_list[0], li_list[1]
        st = ''.join(li_list)
        todolist.append(st)

        li_list = list(prev)
        li_list[1], li_list[2] = li_list[2], li_list[1]
        st = ''.join(li_list)
        todolist.append(st)

        li_list = list(prev)
        li_list[1], li_list[4] = li_list[4], li_list[1]
        st = ''.join(li_list)
        todolist.append(st)
        print(todolist)
    elif a == 3 and st != goal:
        prev = st
        li_list = list(st)
        li_list[3], li_list[0] = li_list[0], li_list[3]
        st = ''.join(li_list)
        todolist.append(st)

        li_list = list(prev)
        li_list[3], li_list[6] = li_list[6], li_list[3]
        st = ''.join(li_list)
        todolist.append(st)

        li_list = list(prev)
        li_list[3], li_list[4] = li_list[4], li_list[3]
        st = ''.join(li_list)
        todolist.append(st)
        print(todolist)
    elif a == 4 and st != goal:
        prev = st
        li_list = list(st)
        li_list[4], li_list[1] = li_list[1], li_list[4]
        st = ''.join(li_list)
        todolist.append(st)

        li_list = list(prev)
        li_list[3], li_list[4] = li_list[4], li_list[3]
        st = ''.join(li_list)
        todolist.append(st)

        li_list = list(prev)
        li_list[4], li_list[5] = li_list[5], li_list[4]
        st = ''.join(li_list)
        todolist.append(st)

        li_list = list(prev)
        li_list[4], li_list[7] = li_list[7], li_list[4]
        st = ''.join(li_list)
        todolist.append(st)
        print(todolist)
    elif a == 5 and st != goal:
        prev = st
        li_list = list(st)
        li_list[5], li_list[2] = li_list[2], li_list[5]
        st = ''.join(li_list)
        todolist.append(st)

        li_list = list(prev)
        li_list[5], li_list[4] = li_list[4], li_list[5]
        st = ''.join(li_list)
        todolist.append(st)

        li_list = list(prev)
        li_list[5], li_list[8] = li_list[8], li_list[5]
        st = ''.join(li_list)
        todolist.append(st)
        print(todolist)
    elif a == 6 and st != goal:
        prev = st
        li_list = list(st)
        li_list[6], li_list[3] = li_list[3], li_list[6]
        st = ''.join(li_list)
        todolist.append(st)

        li_list = list(prev)
        li_list[6], li_list[7] = li_list[7], li_list[6]
        st = ''.join(li_list)
        todolist.append(st)
        print(todolist)
    elif a == 7 and st != goal:
        prev = st
        li_list = list(st)
        li_list[7], li_list[4] = li_list[4], li_list[7]
        st = ''.join(li_list)
        todolist.append(st)

        li_list = list(prev)
        li_list[7], li_list[6] = li_list[6], li_list[7]
        st = ''.join(li_list)
        todolist.append(st)

        li_list = list(prev)
        li_list[7], li_list[8] = li_list[8], li_list[7]
        st = ''.join(li_list)
        todolist.append(st)
        print(todolist)
    elif a == 8 and st != goal:
        prev = st
        li_list = list(st)
        li_list[8], li_list[5] = li_list[5], li_list[8]
        st = ''.join(li_list)
        todolist.append(st)

        li_list = list(prev)
        li_list[8], li_list[7] = li_list[7], li_list[8]
        st = ''.join(li_list)
        todolist.append(st)
        print(todolist)
    else:
        break

    count+=1


print("Total Nodes traversed",count)
