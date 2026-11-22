#!/usr/bin/env python3
"""Complete affine and complement classification of Paley-23 recurrent orbits."""
from collections import Counter
from pathlib import Path

P=23
Q=sorted({j*j%P for j in range(1,P)})
MASKS=[sum(1<<j for j in range(P) if (j-i)%P in Q) for i in range(P)]
FULL=(1<<P)-1


def F(x):
    return sum(1<<i for i,m in enumerate(MASKS) if (x&m).bit_count()>=6)


def orbit_leader(x):
    phases=[]
    for _ in range(4):
        phases.append(x)
        x=F(x)
    assert x==phases[0] and len(set(phases))==4
    return min(phases)


def affine(x,a,s):
    result=0
    for i in range(P):
        if (x>>i)&1:
            result|=1<<((a+s*i)%P)
    return result


def components(S,canon):
    components=[]
    while S:
        rep=min(S)
        orb={canon(affine(rep,a,s)) for a in range(P) for s in Q}
        assert orb <= S
        components.append((rep,orb))
        S-=orb
    return components


def main():
    data=Path(__file__).with_name('census.out').read_text()
    assert 'BASIN_COUNTS\n' in data and 'LAST_DEPTH_STATES\n' in data
    rows=data.split('BASIN_COUNTS\n')[1].split('LAST_DEPTH_STATES\n')[0].strip().splitlines()
    basin={}
    fixed={}
    for row in rows:
        d,x,b=map(int,row.split())
        assert x not in basin and b>=d
        if d==1:
            assert F(x)==x
            fixed[x]=b
        elif d==4:
            assert orbit_leader(x)==x
            assert F(F(x))==(FULL^x)
        else:raise AssertionError((d,x))
        basin[x]=b
    assert fixed=={0:4159390,FULL:4159390}
    states={x for x in basin if x not in fixed}
    assert len(states)==3542 and sum(basin[x] for x in states)==69828
    groups=components(states.copy(),orbit_leader)
    assert len(groups)==14
    expected=[(15611,6),(20431,12),(22511,6),(23167,22),(30571,4),(38395,10),(44671,30),
              (56699,6),(61177,6),(61263,22),(73455,20),(81641,64),(105851,58),(105971,10)]
    got=[(rep,basin[rep]) for rep,orb in groups]
    assert got==expected,(got,expected)
    for rep,orb in groups:
        assert len(orb)==253
        assert len({basin[x] for x in orb})==1
        assert orbit_leader(FULL^rep) in orb
    assert sum(b for _,b in got)==276
    print('FOUR_CYCLE_CLASSES: representative,cycles_in_class,basin_size_per_cycle')
    for rep,orb in groups:
        print(rep,len(orb),basin[rep])
    print('FOUR_CYCLE_TOTAL',sum(len(orb) for _,orb in groups))
    print('FOUR_CYCLE_BASIN_TOTAL',sum(len(orb)*basin[rep] for rep,orb in groups))
    print('FOUR_CYCLE_BASIN_DISTRIBUTION',sorted(Counter(basin[rep] for rep,_ in groups).items()))
    last={int(x) for x in data.split('LAST_DEPTH_STATES\n')[1].split()}
    assert len(last)==1012
    last_groups=components(last.copy(),lambda x:x)
    assert [(rep,len(orb)) for rep,orb in last_groups]==[(23807,253),(32675,253),(61245,253),(103805,253)]
    mapping=[next(i for i,(_,orb) in enumerate(last_groups) if (FULL^rep) in orb)
             for rep,_ in last_groups]
    assert mapping==[1,0,3,2]
    print('TERMINAL_CLASSES', [(rep,len(orb)) for rep,orb in last_groups])
    print('TERMINAL_COMPLEMENT_PAIRS',mapping)
    print('AFFINE_BASIN_CLASS_OK')

if __name__=='__main__':
    main()
