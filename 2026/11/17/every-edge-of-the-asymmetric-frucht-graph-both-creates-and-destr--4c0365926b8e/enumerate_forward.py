#!/usr/bin/env python3
"""Exhaustive 12-vertex majority classification using direct forward trajectories."""
import json

N = 12
EDGES = ((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
         (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
ALL = (1 << N) - 1

def successor_table(removed):
    neighbors = [[] for _ in range(N)]
    for a,b in EDGES:
        if (a,b) != removed:
            neighbors[a].append(b)
            neighbors[b].append(a)
    table = []
    for state in range(1 << N):
        y = 0
        for vertex in range(N):
            count = sum((state >> u) & 1 for u in neighbors[vertex])
            degree = len(neighbors[vertex])
            bit = ((state >> vertex) & 1) if 2*count == degree else int(2*count > degree)
            y |= bit << vertex
        table.append(y)
    return table

def classify(table):
    depth = []
    basin = [0,0,0]  # eventual all-0, all-1, other
    for start in range(1 << N):
        x, y = start, table[start]
        t = 0
        while True:
            z = table[y]
            if z == x:
                if t >= len(depth): depth.extend([0] * (t - len(depth) + 1))
                depth[t] += 1
                if x == 0:
                    basin[0] += 1
                elif x == ALL:
                    basin[1] += 1
                else:
                    basin[2] += 1
                break
            x,y = y,z
            t += 1
            assert t <= 100
    F2 = [table[table[x]] for x in range(1 << N)]
    fixed = sum(table[x] == x for x in range(1 << N))
    osc = sum(F2[x] == x and table[x] != x for x in range(1 << N))
    return dict(unanimity=sum(basin[:2]),zero_basin=basin[0],one_basin=basin[1],
                fixed_points=fixed,temporal_two_states=osc,maximum_entry=len(depth)-1,
                max_count=depth[-1],entry_histogram=depth)

def unanimity_flags(table):
    image = list(range(1 << N))
    for _ in range(9):
        image = [table[y] for y in image]
    return tuple(y in (0, ALL) for y in image)

def main():
    out = {'graph':'Frucht, labelled by edge list', 'vertices':N,'edges':EDGES,'runs':[]}
    base_table = successor_table(None)
    base = classify(base_table)
    base_flags = unanimity_flags(base_table)
    for removed in (None,) + EDGES:
        f = base_table if removed is None else successor_table(removed)
        stat = base if removed is None else classify(f)
        flags = base_flags if removed is None else unanimity_flags(f)
        gain = sum(b and not a for a,b in zip(base_flags,flags))
        loss = sum(a and not b for a,b in zip(base_flags,flags))
        assert gain - loss == stat['unanimity']-base['unanimity']
        out['runs'].append({'deleted_edge':removed,'delta_unanimity':gain-loss,
                            'new_consensus_initials':gain,'lost_consensus_initials':loss,**stat})
    print(json.dumps(out,sort_keys=True,separators=(',',':')))
if __name__ == '__main__':main()
