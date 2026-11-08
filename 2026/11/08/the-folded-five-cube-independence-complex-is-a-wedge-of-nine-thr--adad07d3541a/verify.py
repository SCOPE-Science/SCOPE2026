#!/usr/bin/env python3
"""Exact, standard-library verification of a finite graph independence-complex theorem."""
from collections import Counter, defaultdict, deque
from itertools import combinations

N=16
DIRECTIONS=(1,2,4,8,15)
PIVOTS=(6,13,7,8,14,11,4,0,3,10,5,15,12,1,2,9)


def graph():
    nbr = [sum(1 << (v ^ d) for d in DIRECTIONS) for v in range(N)]
    assert all(nbr[v].bit_count() == 5 and (nbr[v] >> v & 1) == 0 for v in range(N))
    assert all((nbr[u] >> v & 1) == (nbr[v] >> u & 1) for u in range(N) for v in range(N))
    assert sum(nbr[v].bit_count() for v in range(N)) // 2 == 40
    common_counts = Counter()
    for u in range(N):
        for v in range(u+1,N):
            count=(nbr[u] & nbr[v]).bit_count()
            common_counts[(bool(nbr[u] >> v & 1),count)]+=1
            assert count==(0 if (nbr[u] >> v)&1 else 2)
    assert common_counts=={(True,0):40,(False,2):80}
    # Independent five-cube description: take the antipodal quotient of Q_5.
    quotient=[0]*16
    for q in range(32):
        for i in range(5):
            r=q^(1<<i)
            a=min(q,q^31); b=min(r,r^31)
            quotient[a] |= 1<<b
    assert quotient==nbr
    return nbr


def all_faces(nbr):
    # Exhaustively enumerate every nonempty subset of 16 graph vertices.
    brute = {m for m in range(1,1<<N)
             if all(not(nbr[v] & m) for v in range(N) if m >> v & 1)}
    # Independent recursive enumeration, branching on the next legal vertex.
    rec=set()
    def visit(current,eligible):
        if current: rec.add(current)
        while eligible:
            bit=eligible & -eligible
            eligible ^= bit
            v=bit.bit_length()-1
            visit(current|bit, eligible & ~nbr[v])
    visit(0,(1<<N)-1)
    assert rec==brute
    f=Counter(m.bit_count() for m in brute)
    assert [f[i] for i in range(1,6)]==[16,80,160,120,16]
    return brute


def matching_and_acyclicity(faces):
    unmatched=set(faces)
    matching={}
    pair_sizes=[]
    for v in PIVOTS:
        bit=1<<v
        added=0
        for a in sorted(unmatched):
            b=a|bit
            if not(a&bit) and a in unmatched and b in unmatched:
                assert (b.bit_count()-a.bit_count())==1
                unmatched.remove(a)
                unmatched.remove(b)
                matching[a]=b
                added+=1
        pair_sizes.append(added)
    assert len(matching)==191 and len(unmatched)==10
    crit=Counter(m.bit_count()-1 for m in unmatched)
    assert crit=={0:1,3:9}
    # Every covering incidence is checked, with matched arrows reversed.
    indegree={m:0 for m in faces}
    outgoing=defaultdict(list)
    directed=0
    for upper in faces:
        bits=upper
        while bits:
            bit=bits & -bits
            bits^=bit
            lower=upper^bit
            if lower==0: continue
            if matching.get(lower)==upper:
                tail,head=lower,upper
            else:
                tail,head=upper,lower
            outgoing[tail].append(head)
            indegree[head]+=1
            directed+=1
    q=deque(m for m in faces if not indegree[m])
    visited=0
    while q:
        x=q.popleft(); visited+=1
        for y in outgoing[x]:
            indegree[y]-=1
            if indegree[y]==0:q.append(y)
    assert visited==len(faces), f'directed Hasse cycle; sorted {visited}/{len(faces)}'
    assert directed==sum((m.bit_count()) for m in faces if m.bit_count()>1)
    return crit,pair_sizes,directed


def binary_boundary_ranks(faces):
    bins={k:sorted(m for m in faces if m.bit_count()==k) for k in range(1,6)}
    ranks={}
    for k in range(2,6):
        idx={m:i for i,m in enumerate(bins[k-1])}
        basis={}
        rank=0
        for upper in bins[k]:
            bitmask=0
            bits=upper
            while bits:
                bit=bits&-bits
                bits^=bit
                bitmask ^=1 << idx[upper^bit]
            while bitmask:
                pivot=bitmask.bit_length()-1
                if pivot in basis:bitmask^=basis[pivot]
                else:
                    basis[pivot]=bitmask;rank+=1;break
        ranks[k-1]=rank
    assert [ranks[d] for d in range(1,5)]==[15,65,95,16]
    ordinary={}
    ordinary[0]=len(bins[1])-ranks[1]
    for d in range(1,4):
        ordinary[d]=len(bins[d+1])-ranks.get(d,0)-ranks.get(d+1,0)
    ordinary[4]=len(bins[5])-ranks[4]
    assert ordinary=={0:1,1:0,2:0,3:9,4:0}
    return ranks,ordinary


def main():
    nbr=graph()
    faces=all_faces(nbr)
    critical,pivcounts,arrows=matching_and_acyclicity(faces)
    ranks,bettis=binary_boundary_ranks(faces)
    redchi=sum((-1)**(m.bit_count()-1) for m in faces)-1
    assert redchi==-9
    print('GRAPH: vertices=16 edges=40 srg=(16,5,0,2)')
    print('FACES: nonempty=392 f_vector=(16,80,160,120,16)')
    print('MATCH: pairs=191 critical=(one 0-cell, nine 3-cells)')
    print('PIVOTS:',','.join(map(str,PIVOTS)))
    print('PAIR_COUNTS:',','.join(map(str,pivcounts)))
    print('HASSE: directed_incidence=%d topologically_sorted=392'%arrows)
    print('BOUNDARY_RANKS_F2:',','.join(map(str,(ranks[d] for d in range(1,5)))))
    print('BETTI_F2:',','.join(map(str,(bettis[d] for d in range(5)))))
    print('REDUCED_EULER_CHARACTERISTIC:',redchi)
    print('ALL_CHECKS_PASS')
if __name__=='__main__':main()
