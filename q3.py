
iteration = 0
ite = 0
count = 0
t=False
count2 = 0
todolist = []
visited = []
while count2 < 10:
    st = '120345678'
    goal = '012345678'
    todolist.clear()
    visited.clear()
    todolist.insert(0, st)
    ite = 0
    iteration += 1
    while count < 30:
        if not todolist:
            break
        st = todolist.pop(0)
        visited.append(st)
        print(st)
        a=st.find('0')
        if ite < iteration and a == 2 and st != goal:
            ite+=1
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
        elif ite < iteration and a ==0 and st != goal:
            ite+=1
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
        elif ite<iteration and a == 1 and st != goal:
            ite+=1
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
        elif ite<iteration and a == 3 and st != goal:
            ite+=1
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
        elif ite<iteration and a == 4 and st != goal:
            ite+=1
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
        elif ite<iteration and a == 5 and st != goal:
            ite+=1
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
        elif ite<iteration and a == 6 and st != goal:
            ite+=1
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
        elif ite<iteration and a == 7 and st != goal:
            ite+=1
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
        elif ite<iteration and a == 8 and st != goal:
            ite+=1
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
        elif st == goal:
            print("goal reached")
            t = True
            break

        count+=1

    if t == True:
        break



print("Total Nodes traversed", count)