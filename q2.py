st = '120345678'
goal = '012345678'
todolist = []
visited = []
todolist.insert(0,st)
count=0

while count < 30:
    st = todolist.pop(0)
    visited.append(st)
    print(st)
    a=st.find('0')
    if a == 2 and st != goal:

        prev = st
        li_list = list(st)
        li_list[2], li_list[5] = li_list[5], li_list[2]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)

        li_list = list(prev)
        li_list[1], li_list[2] = li_list[2], li_list[1]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)

        print(todolist)
    elif a==0 and st != goal:
        prev = st
        li_list = list(st)
        li_list[0], li_list[1] = li_list[1], li_list[0]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)

        li_list = list(prev)
        li_list[0], li_list[3] = li_list[3], li_list[0]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)

        print(todolist)
    elif a == 1 and st != goal:
        prev = st
        li_list = list(st)
        li_list[1], li_list[4] = li_list[4], li_list[1]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)

        li_list = list(prev)
        li_list[1], li_list[2] = li_list[2], li_list[1]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)

        li_list = list(prev)
        li_list[1], li_list[0] = li_list[0], li_list[1]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)
        print(todolist)
    elif a == 3 and st != goal:
        prev = st
        li_list = list(st)
        li_list[3], li_list[0] = li_list[0], li_list[3]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)

        li_list = list(prev)
        li_list[3], li_list[6] = li_list[6], li_list[3]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)
        li_list = list(prev)
        li_list[3], li_list[4] = li_list[4], li_list[3]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)
        print(todolist)
    elif a == 4 and st != goal:
        prev = st
        li_list = list(st)
        li_list[4], li_list[1] = li_list[1], li_list[4]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)

        li_list = list(prev)
        li_list[3], li_list[4] = li_list[4], li_list[3]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)

        li_list = list(prev)
        li_list[4], li_list[5] = li_list[5], li_list[4]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)

        li_list = list(prev)
        li_list[4], li_list[7] = li_list[7], li_list[4]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)
        print(todolist)
    elif a == 5 and st != goal:
        prev = st
        li_list = list(st)
        li_list[5], li_list[2] = li_list[2], li_list[5]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)

        li_list = list(prev)
        li_list[5], li_list[4] = li_list[4], li_list[5]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)

        li_list = list(prev)
        li_list[5], li_list[8] = li_list[8], li_list[5]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)
        print(todolist)
    elif a == 6 and st != goal:
        prev = st
        li_list = list(st)
        li_list[6], li_list[3] = li_list[3], li_list[6]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)

        li_list = list(prev)
        li_list[6], li_list[7] = li_list[7], li_list[6]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)
        print(todolist)
    elif a == 7 and st != goal:
        prev = st
        li_list = list(st)
        li_list[7], li_list[4] = li_list[4], li_list[7]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)

        li_list = list(prev)
        li_list[7], li_list[6] = li_list[6], li_list[7]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)

        li_list = list(prev)
        li_list[7], li_list[8] = li_list[8], li_list[7]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)
        print(todolist)
    elif a == 8 and st != goal:
        prev = st
        li_list = list(st)
        li_list[8], li_list[5] = li_list[5], li_list[8]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)

        li_list = list(prev)
        li_list[8], li_list[7] = li_list[7], li_list[8]
        st = ''.join(li_list)
        if st not in todolist and st not in visited:
            todolist.insert(0,st)
        print(todolist)
    else:
        break

    count+=1



print("Total Nodes traversed", count)