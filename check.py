#单一数据源原则
planets = {
    "Mercury":{
        "category":"terrestrial planet",
        "mean radius":2440,
        "number of satelltes":0
    },
    "Venus":{
        "category":"terrestrial planet",
        "mean radius":6052,
        "number of satelltes":0
    },
    "Saturn":{
        "category":"gas giant",
        "mean radius":58232,
        "number of satelltes":274    # 来源：NASA Planetary Fact Sheet, 2025-03
    },
    "Uranus":{
        "category":"ice giant",
        "mean radius":25362,
        "number of satelltes":28
    }
}

activate = True   # 设立循环标识

while activate:
    check_the_planet = input("Tell me which planet you want to kown(if you want to quit, enter 'q') : \n")
    if check_the_planet in planets:#问字典这个值是否存在于字典中,check_the_planet等价于星名
        info=planets[check_the_planet]#用名字取值，将信息赋予info
    
        Ca = info["category"]
        Me = info["mean radius"]
        Nu = info["number of satelltes"]

        print(f"\nPlanet Name:  {check_the_planet}")
        print(f"\tCategory: {Ca}\n\tMean Radius: {Me}\n\tNumber of Satellties: {Nu}")
    elif check_the_planet == "q":
            activate = False
    else:
        print(f"{check_the_planet} No found")
    

    
