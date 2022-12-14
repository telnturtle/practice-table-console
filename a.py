# data = list()

# Input data
# data = [
#     ['a', 'cdefg'],
#     ['ab', 'hij'],
# ]
# data = [
#     ['a']
# ]
# data = [
#     ['These components will be installed.'],
#     ['Name', 'Version', 'Size'],
#     ['gcloud app Python Extensions', '1.9.66', '6.1MiB']
# ]
# data = [
#     ["Community Courses -- Bath Autumn 1997"],
#     ['Course Name', 'Course Tutor', 'Summary', 'Code', 'Fee'],
#     ['After the Civil War', 'Dr. John Wroughton', 'The course will examine the turbulent years in England after 1646. 6 weekly meetings starting Monday 13th October.', 'H27', '$32'],
#     ['An Introduction to Anglo-Saxon England', 'Mark Cottle', 'One day course introducint the early medieval period reconstruction the Anglo-Saxons and their society. Saturday 18th October.', 'H28', '$18'],
#     ['The Glory that was Greece', 'Valerie Lorenz', 'Birthplace of democracy, philosophy, heartland of theater, home of argument. The Romans may have done it but the Greeks did it first. Saturday day school 25th October 1997', 'H30', '$18'],
# ]
# data = [
#     ["Community Courses -- Bath Autumn 1997"],
#     ['Course Name', 'Course Tutor', 'Summary', 'Code', 'Fee'],
#     ['After the Civil War', 'Dr. John Wroughton', 'The course ...', 'H27', '$32'],
#     ['An Introduction to Anglo-Saxon England', 'Mark Cottle', 'One day ...', 'H28', '$18'],
#     ['The Glory that was Greece', 'Valerie Lorenz', 'Birthplace of, ...', 'H30', '$18'],
# ]
# data = [
#     ['Application', 'Data Loss', 'Throughput', 'Time-Sensitive'],
#     ['File transfer/download', 'No loss', 'Elastic', 'No'],
#     ['E-mail', 'No loss', 'Elastic', 'No'],
#     ['Web documents', 'No loss', 'Elastic (few kbps)', 'No'],
#     ['Internet telephony/Video conferencing', 'Loss-tolerant', 'Audio: few kbps-1Mbps, Video: 10 kbps-5Mbps', 'Yes: 100s of msec'],
#     ['Streaming stored audio/video', 'Loss-tolerant', 'Same as above', 'Yes; Few seconds'],
#     ['Interactive games', 'Loss-tolerant', 'Few kbps-10 kbps', 'Tes: 100s of msec'],
#     ['Instant messaging', 'No loss', 'Elastic', 'Yes and no'],
# ]

def the_function(data):

    # ?????? ???????????? n??? 1 ????????? ??????
    n_col = 0 # ????????? ??????

    for i in data:
        if len(i) != 1 and len(i) != 0:
            n_col = len(i)
            break

    # 1????????? n???????????? ????????? ?????? ????????????
    n_col_lens = [0 for i in range(0, n_col)] # n????????? ??????
    a_col_len = 0 # 1????????? ??????

    for i in data:
        if len(i) == 1:
            a_col_len = len(i[0]) if len(i[0]) > a_col_len else a_col_len
        else:
            # len(i) == n_col
            for j in range(0,len(i)):
                n_col_lens[j] = len(i[j]) if len(i[j]) > n_col_lens[j] else n_col_lens[j]

    # print("n_col_lens[0]", n_col_lens[0])
    # print("n_col_lens[1]", n_col_lens[1])

    # 1????????? 3???????????? ????????? ???????
    a_col_GT_n_col = a_col_len > sum(n_col_lens) + 3*(n_col - 1)
    total_width = a_col_len if a_col_GT_n_col else sum(n_col_lens) + 3*(n_col - 1)
    width_diff = abs(a_col_len - (sum(n_col_lens) + 3*(n_col - 1)))

    # ?????? ??????????????? ???????????? ???????????? ?????????
    data_orig = data

    # print('len(data[0][1])', len(data[0][1]))


    for i in range(0,len(data)):
        if len(data[i]) != 1:
            for j in range(0,len(data[i])):
                if 0 != (n_col_lens[j] - len(data[i][j])) % 2:
                    print('i, j = %d, %d' % (i, j))
                    print('data[%d][%d] =' % (i, j), data[i][j], end='.\n')
                    temp = int((n_col_lens[j] - len(data[i][j]))/2)
                    data[i][j] = ' '*temp \
                        + data[i][j] \
                        + ' '*(temp + 1)
                    print('data[%d][%d] =' % (i, j), data[i][j], end='.\n')
                else:
                    print(' i, j = %d, %d' % (i, j))
                    print('data[%d][%d] =' % (i, j), data[i][j], end='.\n')
                    # temp = int((n_col_lens[j] - len(data[i][j]))/2)
                    # data[i][j] = ' '*temp \
                    # + data[i][j] \
                    # + ' '*temp
                    data[i][j] = ' '*int((n_col_lens[j] - len(data[i][j]))/2) \
                    + data[i][j] \
                    + ' '*int((n_col_lens[j] - len(data[i][j]))/2)
                    print('len(data[%d][%d]) =' % (i, j), len(data[i][j]))
                    print('data[%d][%d] =' % (i, j), data[i][j], end='.\n')
                    print('n_col_lens[%d] =' % j, n_col_lens[j])
                    print('int((n_col_lens[%d] - len(data[%d][%d]))/2) =' % (j, i, j), int((n_col_lens[j] - len(data[i][j]))/2))
        else:
            if 0 != (a_col_len - len(data[i])) % 2:
                data[i][0] = ' '*int((a_col_len - len(data[i][0]))/2) \
                    + data[i][0] \
                    + ' '*(int((a_col_len - len(data[i][0]))/2) + 1)
            else:
                data[i][0] = ' '*int((a_col_len - len(data[i][0]))/2) \
                    + data[i][0] \
                    + ' '*int((a_col_len - len(data[i][0]))/2)

    # 
    def draw_cel(ch, row, col, table):
        # print(ch, row, col)
        if ch == '-':
            if table[row][col] == ' ':
                # print("A")
                return '-'
            elif table[row][col] == '|':
                # print("B")
                return '+'
            elif table[row][col] == '+':
                # print("C")
                return '+'
            else:
                # print("D")
                return ch
        elif ch == '|':
            if table[row][col] == ' ':
                # print("E")
                return '|'
            elif table[row][col] == '-':
                # print("F")
                return '+'
            elif table[row][col] == '+':
                # print("G")
                return '+'
            else:
                # print("H")
                return ch
        else:
            # print("I")
            return ch

    # ??? ????????? ?????????
    # table = [[' ' for j in range(0,total_width + 4)] for i in range(0,2*len(data) + 1)]
    table = [['' for j in range(0,1024)] for i in range(0,25)]

    '''
    # Print table
    for i in table:
        print(i)
    '''

    # ?????? ?????????
    for i in range(0,len(data)): # for i in range(0,len(2*len(data)+1)):
        seek = 0
        
        # ??? ???????????? ??? ?????? ?????????
        table[2*i + 0][seek] = draw_cel('|', 2*i + 0, seek, table) # ???
        for ii in table[:3]:
            for j in ii:
                print(j, end='')
            print('')
        table[2*i + 0][seek] = draw_cel('-', 2*i + 0, seek, table) # ???
        for ii in table[:3]:
            for j in ii:
                print(j, end='')
            print('')
        table[2*i + 1][seek] = draw_cel('|', 2*i + 1, seek, table) # ??????
        for ii in table[:3]:
            for j in ii:
                print(j, end='')
            print('')
        table[2*i + 2][seek] = draw_cel('|', 2*i + 2, seek, table) # ??????
        for ii in table[:3]:
            for j in ii:
                print(j, end='')
            print('')
        table[2*i + 2][seek] = draw_cel('-', 2*i + 2, seek, table) # ??????
        for ii in table[:3]:
            for j in ii:
                print(j, end='')
            print('')
        seek += 1
        # print(seek)
        table[2*i + 0][seek] = draw_cel('-', 2*i + 0, seek, table)
        table[2*i + 1][seek] = ' '
        table[2*i + 2][seek] = draw_cel('-', 2*i + 2, seek, table)
        seek += 1
        # print(seek)
        for ii in table[:3]:
            for j in ii:
                print(j, end='')
            print('')

        for j in range(0,len(data[i])):
            # ?????? ???????????? ??? ?????? ?????????
            table[2*i + 1][seek:seek + len(data[i][j])] = list(data[i][j])
            # seek += len(data[i][j])
            for k in range(seek, seek + len(data[i][j])):
                table[2*i + 0][k] = draw_cel('-', 2*i + 0, k, table)
                table[2*i + 2][k] = draw_cel('-', 2*i + 2, k, table)
                seek += 1
                # print(seek)

            # ?????? ???????????? ??? ?????? ?????????
            table[2*i + 0][seek] = draw_cel('-', 2*i + 0, seek, table)
            table[2*i + 1][seek] = ' '
            table[2*i + 2][seek] = draw_cel('-', 2*i + 2, seek, table)
            seek += 1
            # print(seek)
            table[2*i + 0][seek] = draw_cel('|', 2*i + 0, seek, table)
            table[2*i + 1][seek] = draw_cel('|', 2*i + 1, seek, table)
            table[2*i + 2][seek] = draw_cel('|', 2*i + 2, seek, table)
            table[2*i + 0][seek] = draw_cel('-', 2*i + 0, seek, table)
            table[2*i + 2][seek] = draw_cel('-', 2*i + 2, seek, table)
            seek += 1
            # print(seek)
            table[2*i + 0][seek] = draw_cel('-', 2*i + 0, seek, table)
            table[2*i + 1][seek] = ' '
            table[2*i + 2][seek] = draw_cel('-', 2*i + 2, seek, table)
            seek += 1
            # print(seek)
        
        seek -= 1
        table[2*i + 0][seek] = ''
        table[2*i + 1][seek] = ''
        table[2*i + 2][seek] = ''
        

    # Print table
    print('\n\n\n')
    for i in table[:20]:
        for j in i:
            print(j, end='')
        print('')
    
    return table


