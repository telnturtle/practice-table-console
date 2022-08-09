import a

data = list()
datas = list()

# Input data
data = [
    ['a', 'cdefg'],
    ['ab', 'hij'],
]
datas.append(a.the_function(data))

data = [
    ['a']
]
datas.append(a.the_function(data))

data = [
    ['These components will be installed.'],
    ['Name', 'Version', 'Size'],
    ['gcloud app Python Extensions', '1.9.66', '6.1MiB']
]
datas.append(a.the_function(data))

data = [
    ["Community Courses -- Bath Autumn 1997"],
    ['Course Name', 'Course Tutor', 'Summary', 'Code', 'Fee'],
    ['After the Civil War', 'Dr. John Wroughton', 'The course will examine the turbulent years in England after 1646. 6 weekly meetings starting Monday 13th October.', 'H27', '$32'],
    ['An Introduction to Anglo-Saxon England', 'Mark Cottle', 'One day course introducint the early medieval period reconstruction the Anglo-Saxons and their society. Saturday 18th October.', 'H28', '$18'],
    ['The Glory that was Greece', 'Valerie Lorenz', 'Birthplace of democracy, philosophy, heartland of theater, home of argument. The Romans may have done it but the Greeks did it first. Saturday day school 25th October 1997', 'H30', '$18'],
]
data = [
    ["Community Courses -- Bath Autumn 1997"],
    ['Course Name', 'Course Tutor', 'Summary', 'Code', 'Fee'],
    ['After the Civil War', 'Dr. John Wroughton', 'The course ...', 'H27', '$32'],
    ['An Introduction to Anglo-Saxon England', 'Mark Cottle', 'One day ...', 'H28', '$18'],
    ['The Glory that was Greece', 'Valerie Lorenz', 'Birthplace of, ...', 'H30', '$18'],
]
datas.append(a.the_function(data))

data = [
    ['Application', 'Data Loss', 'Throughput', 'Time-Sensitive'],
    ['File transfer/download', 'No loss', 'Elastic', 'No'],
    ['E-mail', 'No loss', 'Elastic', 'No'],
    ['Web documents', 'No loss', 'Elastic (few kbps)', 'No'],
    ['Internet telephony/Video conferencing', 'Loss-tolerant', 'Audio: few kbps-1Mbps, Video: 10 kbps-5Mbps', 'Yes: 100s of msec'],
    ['Streaming stored audio/video', 'Loss-tolerant', 'Same as above', 'Yes; Few seconds'],
    ['Interactive games', 'Loss-tolerant', 'Few kbps-10 kbps', 'Tes: 100s of msec'],
    ['Instant messaging', 'No loss', 'Elastic', 'Yes and no'],
]
datas.append(a.the_function(data))


print('\n\n\n\n\n\n\n\n\n\n\n\n')
for ii in datas:
    for i in ii[:20]:
        for j in i:
            print(j, end='')
        print('')
