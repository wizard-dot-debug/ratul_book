def dict():
    dict = {'Dhaka':{'District':13, 'Upazilla':93, 'Council':1833},
            'Barishal':{'District':6,'Upazilla':39, 'Council':333},
            'Khulna':{'District':10, 'Upazilla':59, 'Council':270},
            'Rajshahi':{'District':8, 'Upazilla':70, 'Council':558},
            'Chitttagong':{'District':11, 'Upazilla':97, 'Council':336},
            'Shylet':{'District':4, 'Upazilla':38, 'Council':334},
            'Mymensingh':{'District':4, 'Upazilla':34, 'Council':350},
            'Rangpur':{'District':8, 'Upazilla':58, 'Council':536}
            }
    # x = dict.keys()
    # for i in x:
    #     print(f'{i} Division has {dict[i]['Upazilla']} Upazillas.')
    dis = 0
    up = 0
    co = 0
    for i in dict:
        # print(i)
        # print(dict[i])
        dis += dict[i]['District']
        up += dict[i]['Upazilla']
        co += dict[i]['Council']
    print(f'Total District In Bangladesh: {dis}.\nTotal Upazilla In Bangladesh: {up}.\nTotal Union In Bangladesh: {co}.')

dict()


