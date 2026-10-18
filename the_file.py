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


check_the_planet = "abc"#循环之外赋值
for planet_name,planet_info in planets.items():
    print(f"\nPlanet Name: {planet_name}")
    c=planet_info["category"]
    m=planet_info["mean radius"]
    n=planet_info["number of satelltes"]
    print(f"\tCategory: {c}\n\tMean Radius: {m}\n\tNumber of Satellties: {n}")

   
    
if check_the_planet in planets:#问字典这个值是否存在于字典中,check_the_planet等价于星名
    info=planets[check_the_planet]#用名字取值，将信息赋予info
    
    Ca = info["category"]
    Me = info["mean radius"]
    Nu = info["number of satellites"]

    print(f"\nPlanet Name:  {check_the_planet}")
    print(f"\tCategory: {Ca}\n\tMean Radius: {Me}\n\tNumber of Satellities: {Nu}")
else:
    print(f"{check_the_planet} No found")