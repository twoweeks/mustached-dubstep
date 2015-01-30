#!/usr/bin/python
# -*- coding: utf-8 -*-


rooms=(
"""
╔═════╗
║     ║
║     ║
║     ║
║     ║
║     ║
╚═════╝
""",
"""
╔═════╗
║     ║
╜     ║
      ║
╖     ║
║     ║
╚═════╝
""",
"""
╔═════╗
║     ║
║     ║
║     ║
║     ║
║     ║
╚═╕ ╒═╝
""",
"""
╔═════╗
║     ║
╜     ║
      ║
╖     ║
║     ║
╚═╕ ╒═╝
""",
"""
╔═════╗
║     ║
║     ╙
║      
║     ╓
║     ║
╚═════╝
""",
"""
╔═════╗
║     ║
╜     ╙
       
╖     ╓
║     ║
╚═════╝
""",
"""
╔═════╗
║     ║
║     ╙
║      
║     ╓
║     ║
╚═╕ ╒═╝
""",
"""
╔═════╗
║     ║
╜     ╙
       
╖     ╓
║     ║
╚═╕ ╒═╝
""",
"""
╔═╛ ╘═╗
║     ║
║     ║
║     ║
║     ║
║     ║
╚═════╝
""",
"""
╔═╛ ╘═╗
║     ║
╜     ║
      ║
╖     ║
║     ║
╚═════╝
""",
"""
╔═╛ ╘═╗
║     ║
║     ║
║     ║
║     ║
║     ║
╚═╕ ╒═╝
""",
"""
╔═╛ ╘═╗
║     ║
╜     ║
      ║
╖     ║
║     ║
╚═╕ ╒═╝
""",
"""
╔═╛ ╘═╗
║     ║
║     ╙
║      
║     ╓
║     ║
╚═════╝
""",
"""
╔═╛ ╘═╗
║     ║
╜     ╙
       
╖     ╓
║     ║
╚═════╝
""",
"""
╔═╛ ╘═╗
║     ║
║     ╙
║      
║     ╓
║     ║
╚═╕ ╒═╝
""",
"""
╔═╛ ╘═╗
║     ║
╜     ╙
       
╖     ╓
║     ║
╚═╕ ╒═╝
"""
)


rooms_with_numbers=(
"""
╔══════╗
║  0   ║
║      ║
║      ║
╚══════╝
""",
"""
╔══════╗
╜  1   ║
       ║
╖      ║
╚══════╝
""",
"""
╔══════╗
║  2   ║
║      ║
║      ║
╚═╕  ╒═╝
""",
"""
╔══════╗
╜  3   ║
       ║
╖      ║
╚═╕  ╒═╝
""",
"""
╔══════╗
║  4   ╙
║       
║      ╓
╚══════╝
""",
"""
╔══════╗
╜  5   ╙
        
╖      ╓
╚══════╝
""",
"""
╔══════╗
║  6   ╙
║       
║      ╓
╚═╕  ╒═╝
""",
"""
╔══════╗
╜  7   ╙
        
╖      ╓
╚═╕  ╒═╝
""",
"""
╔═╛  ╘═╗
║  8   ║
║      ║
║      ║
╚══════╝
""",
"""
╔═╛  ╘═╗
╜  9   ║
       ║
╖      ║
╚══════╝
""",
"""
╔═╛  ╘═╗
║  10  ║
║      ║
║      ║
╚═╕  ╒═╝
""",
"""
╔═╛  ╘═╗
╜  11  ║
       ║
╖      ║
╚═╕  ╒═╝
""",
"""
╔═╛  ╘═╗
║  12  ╙
║       
║      ╓
╚══════╝
""",
"""
╔═╛  ╘═╗
╜  13  ╙
        
╖      ╓
╚══════╝
""",
"""
╔═╛  ╘═╗
║  14  ╙
║       
║      ╓
╚═╕  ╒═╝
""",
"""
╔═╛  ╘═╗
╜  15  ╙
        
╖      ╓
╚═╕  ╒═╝
"""
)


rooms_maps3=(
(1,1,1,1,0,1,1,1,1),
(1,1,1,0,0,1,1,1,1),
(1,1,1,1,0,1,1,0,1),
(1,1,1,0,0,1,1,0,1),
(1,1,1,1,0,0,1,1,1),
(1,1,1,0,0,0,1,1,1),
(1,1,1,1,0,0,1,0,1),
(1,1,1,0,0,0,1,0,1),
(1,0,1,1,0,1,1,1,1),
(1,0,1,0,0,1,1,1,1),
(1,0,1,1,0,1,1,0,1),
(1,0,1,0,0,1,1,0,1),
(1,0,1,1,0,0,1,1,1),
(1,0,1,0,0,0,1,1,1),
(1,0,1,1,0,0,1,0,1),
(1,0,1,0,0,0,1,0,1)
)

symbols = set()
for i in rooms:
    symbols.update(set(i.replace(' ', '').replace('\n', '')))

rooms_maps = []

rooms_maps_str = [i.replace('\n', '') for i in rooms]

for i in range(len(rooms)):
    for j in symbols:
        rooms_maps_str[i] = rooms_maps_str[i].replace(j, '1')
    rooms_maps_str[i] = rooms_maps_str[i].replace(' ', '0')


rooms_maps_str3 = [''.join(map(str, j)) for j in rooms_maps3]
rooms_list = [rooms[i].split('\n') for i in range(len(rooms))]
