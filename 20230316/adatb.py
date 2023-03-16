hajonev=[
    "Arizona",
    "Bismark",
    "California",
    "Duke of York",
    "Fuso",
    "Hood",
    "King George V",
    "Kirishima",
    "Prince of Wales",
    "Rodney",
    "Scharnhorst",
    "South of Dakota",
    "Tennessee",
    "Washington",
    "West Wirginia",
    "Yamashiro"
]

csatanev=[
    "Denmark Strait",
    "Pearl Harbour",
    "Surigao Strait",
    "North Cape",
    "Surigao Strait",
    "Denmark Strait",
    "Denmark Strait",
    "Guadalcanal",
    "Denmark Strait",
    "Denmark Strait",
    "North Cape",
    "Guadalcanal",
    "Surigao Strait",
    "Guadalcanal",
    "Surigao Strait",
    "Surigao Strait"
]

eredmeny=[
    "elsüllyedt",
    "elsüllyedt",
    "ok",
    "ok",
    "elsüllyedt",
    "elsüllyedt",
    "ok",
    "elsüllyedt",
    "sérült",
    "ok",
    "elsüllyedt",
    "sérült",
    "ok",
    "ok",
    "ok",
    "elsüllyedt"
]

query=""
for i in range(len(csatanev)):
    query+=f"INSERT INTO `Kimenetelek`(`Hajónév`, `Csatanév`, `eredmény`) VALUES ('{hajonev[i]}','{csatanev[i]}','{eredmeny[i]}');"

print(query)