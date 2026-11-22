#!/usr/bin/env python3
"""Exhaustive integer computation for cubic-surface line/tritangent Frobenius profiles.

Public mathematical data: the 27 (-1)-classes on the blow-up of P2 at six
points, their 45 anticanonical triples, and the Weyl E6 action.
Usage: python3 verify_e6.py [optional path to expected CSV]
"""
import csv
import io
import sys
from collections import Counter, defaultdict, deque
from itertools import combinations
from math import lcm


def picard_dot(a, b):
    return a[0]*b[0] - sum(x*y for x, y in zip(a[1:], b[1:]))


def line_classes():
    result = []
    for i in range(6):
        a = [0]*7; a[i+1] = 1; result.append(tuple(a))
    for i, j in combinations(range(6), 2):
        a = [1]+[0]*6; a[i+1] = a[j+1] = -1; result.append(tuple(a))
    for i in range(6):
        a = [2]+[-1]*6; a[i+1] = 0; result.append(tuple(a))
    return result


def tritangents(lines):
    anticanonical = (3, -1, -1, -1, -1, -1, -1)
    # Divisor-class construction
    from_divisors = set()
    for ids in combinations(range(27), 3):
        if tuple(sum(lines[i][j] for i in ids) for j in range(7)) == anticanonical:
            from_divisors.add(ids)
    # Independent intersection-graph construction
    from_graph = set()
    for ids in combinations(range(27), 3):
        if all(picard_dot(lines[i], lines[j]) == 1 for i, j in combinations(ids, 2)):
            from_graph.add(ids)
    assert len(from_divisors) == len(from_graph) == 45
    assert from_divisors == from_graph
    return tuple(sorted(from_divisors))


def root_reflection(v):
    root = (1, -1, -1, -1, 0, 0, 0)
    assert picard_dot(root, root) == -2
    k = picard_dot(v, root)
    return tuple(v[i]+k*root[i] for i in range(7))


def perm_generators(lines):
    lookup = {v:i for i,v in enumerate(lines)}
    def swap(v):
        a=list(v);a[1],a[2]=a[2],a[1];return tuple(a)
    def sixcycle(v):
        return (v[0], v[6], v[1], v[2], v[3], v[4], v[5])
    return [tuple(lookup[f(v)] for v in lines) for f in (swap,sixcycle,root_reflection)]


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def invert(p):
    result=[-1]*len(p)
    for i,j in enumerate(p):result[j]=i
    assert -1 not in result
    return tuple(result)


def group_generated(gens):
    identity=tuple(range(len(gens[0])))
    result=[identity]; visited={identity}; k=0
    while k < len(result):
        a=result[k];k+=1
        for b in gens:
            c=compose(a,b)
            if c not in visited:
                visited.add(c);result.append(c)
    assert len(result)==len(visited)==51840
    return result


def classes(group, gens):
    # Exhaustive conjugation by the group generators, not an assumption about class count.
    remaining=set(group)
    igens=[invert(g) for g in gens]
    conjugacy=[]
    while remaining:
        rep=min(remaining)
        queue=deque([rep]);remaining.remove(rep);count=0
        while queue:
            p=queue.popleft();count+=1
            for g,inv in zip(gens,igens):
                c=compose(compose(g,p),inv)
                if c in remaining:
                    remaining.remove(c);queue.append(c)
        conjugacy.append((rep,count))
    assert len(conjugacy)==25
    assert sum(size for _,size in conjugacy)==51840
    return conjugacy


def cycles(p):
    seen=set();sizes=Counter()
    for i in range(len(p)):
        if i not in seen:
            j=i;size=0
            while j not in seen:
                seen.add(j);size+=1;j=p[j]
            sizes[size]+=1
    assert sum(s*m for s,m in sizes.items())==len(p)
    return tuple(sorted(sizes.items()))


def induced(p, triples):
    idx={x:i for i,x in enumerate(triples)}
    return tuple(idx[tuple(sorted(p[i] for i in triple))] for triple in triples)


def fixed(cycles_,n):
    return sum(length*number for length,number in cycles_ if n%length==0)


def cycle_str(c):
    return ' '.join('%s^%s'%(n,m) for n,m in c)


def build():
    lines=line_classes()
    assert len(lines)==27 and len(set(lines))==27
    assert all(picard_dot(x,x)==-1 for x in lines)
    anticanonical=(3,-1,-1,-1,-1,-1,-1)
    assert all(picard_dot(anticanonical,x)==1 for x in lines)
    triples=tritangents(lines)
    gens=perm_generators(lines)
    for p in gens:
        assert len(set(p))==27
        assert all(picard_dot(lines[p[i]],lines[p[j]])==picard_dot(lines[i],lines[j]) for i in range(27) for j in range(27))
        assert {tuple(sorted(p[i] for i in t)) for t in triples}==set(triples)
    group=group_generated(gens)
    conjugacy=classes(group,gens)
    data=[]
    for representative,size in conjugacy:
        a=cycles(representative); b=cycles(induced(representative,triples))
        order=lcm(*(n for n,_ in a))
        assert order==lcm(*(n for n,_ in b)) if lcm(*(n for n,_ in b))==order else order%lcm(*(n for n,_ in b))==0
        data.append(dict(class_size=size,order=order,line_cycles=a,tritangent_cycles=b,
            profile=tuple((fixed(a,n),fixed(b,n)) for n in (1,2,3))))
    assert len({(x['line_cycles'],x['tritangent_cycles']) for x in data})==25
    assert len({x['line_cycles'] for x in data})==20
    assert len({x['tritangent_cycles'] for x in data})==24
    for k,n in ((1,19),(2,23),(3,25)):
        assert len({x['profile'][:k] for x in data})==n
    collision_blocks=defaultdict(list)
    for x in data:collision_blocks[x['profile'][:2]].append(x)
    collisions=[v for v in collision_blocks.values() if len(v)>1]
    assert len(collisions)==2 and all(len(v)==2 for v in collisions)
    assert {tuple(x['profile'][:2]) for x in collisions[0]} != {tuple(x['profile'][:2]) for x in collisions[1]}
    collision_sets={tuple(sorted(x['profile'] for x in pair)) for pair in collisions}
    expected={
        (((0,1),(0,3),(3,7)),((0,1),(0,3),(3,13))),
        (((0,3),(0,3),(15,15)),((0,3),(0,3),(27,45)))
    }
    assert collision_sets==expected
    data.sort(key=lambda d:(d['profile'],d['class_size']))
    dest=io.StringIO(newline='')
    columns=['class_id','class_size','element_order','line_cycle_type','tritangent_cycle_type',
             'lines_degree_1','tritangents_degree_1','lines_degree_2','tritangents_degree_2',
             'lines_degree_3','tritangents_degree_3']
    w=csv.writer(dest,lineterminator='\n');w.writerow(columns)
    for i,x in enumerate(data,1):
        w.writerow([f'C{i:02}',x['class_size'],x['order'],cycle_str(x['line_cycles']),cycle_str(x['tritangent_cycles']),
                    *[v for pair in x['profile'] for v in pair]])
    return dest.getvalue()


if __name__ == '__main__':
    result=build()
    if len(sys.argv)==2:
        with open(sys.argv[1],encoding='utf-8',newline='') as f:
            actual=f.read()
        assert result==actual, 'CSV does not match exact group computation'
    elif len(sys.argv)!=1:
        raise SystemExit('Usage: python3 verify_e6.py [table.csv]')
    else:
        print(result,end='')
    if len(sys.argv)==2:
        print('E6_27_LINES_45_TRITANGENTS_25_CLASSES_SHARP_THREE_EXTENSIONS_VERIFIED')
