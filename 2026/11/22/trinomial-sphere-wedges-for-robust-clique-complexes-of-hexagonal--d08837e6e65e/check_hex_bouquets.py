#!/usr/bin/env python3
"""Standalone exact finite checks for the C6-bouquet robust-clique theorem.

No external packages. This is not the general proof; the finite local table
in RESULT.md supplies the uniform argument.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, product
from math import comb


def alpha_masks(m):
    n=5*m+1
    adjacency=[0]*n
    for j in range(m):
        v=[0]+list(range(1+5*j, 6+5*j))
        for i in range(6):
            x,y=v[i],v[(i+1)%6]
            adjacency[x] |= 1<<y
            adjacency[y] |= 1<<x
    @lru_cache(None)
    def independence(s):
        if s==0:return 0
        bit=s&-s
        v=bit.bit_length()-1
        return max(independence(s^bit),1+independence((s^bit)&~adjacency[v]))
    return n,independence


def face_poset(m,k):
    n,alpha=alpha_masks(m)
    faces=set()
    for cardinality in range(1,min(n,2*(k-1))+1):
        for choose in combinations(range(n),cardinality):
            s=sum(1<<i for i in choose)
            if alpha(s)<k:faces.add(s)
    return n,faces


def lex_matching(faces,n):
    remain=set(faces)
    pairs=set()
    for i in range(n):
        # The two sets differ ONLY at vertex i, so pairs never compete.
        matches=[(s,s|(1<<i)) for s in remain if not (s>>i)&1 and (s|(1<<i)) in remain]
        for lower,upper in matches:
            remain.remove(lower)
            remain.remove(upper)
            pairs.add((lower,upper))
    return remain,pairs


def expected_critical(m,k):
    result={1}
    # The three local critical states are: empty, d-e, b-c-d-e.
    for ranks in product(range(3),repeat=m):
        if sum(ranks)!=k-1:continue
        bits=0
        for j,r in enumerate(ranks):
            if r==1:
                bits |= (1<<(1+5*j+3)) | (1<<(1+5*j+4))
            elif r==2:
                bits |= sum(1<<(1+5*j+i) for i in range(1,5))
        result.add(bits)
    return result


def check_acyclic(faces,pairs):
    # Directed Hasse graph: matched edges upward; other face edges downward.
    adjacent={face:[] for face in faces}
    indegree=dict.fromkeys(faces,0)
    for upper in faces:
        bitset=upper
        while bitset:
            bit=bitset&-bitset
            bitset-=bit
            lower=upper^bit
            if not lower:continue
            if lower not in faces:raise AssertionError('missing face')
            if (lower,upper) in pairs:
                adjacent[lower].append(upper)
                indegree[upper]+=1
            else:
                adjacent[upper].append(lower)
                indegree[lower]+=1
    todo=deque(x for x in faces if indegree[x]==0)
    count=0
    while todo:
        x=todo.popleft();count+=1
        for y in adjacent[x]:
            indegree[y]-=1
            if indegree[y]==0:todo.append(y)
    return count==len(faces)


def check_local_table():
    # a-b-c-d-e is path on five vertices; z is adjacent to a,e.
    adj=[0]*5
    for i in range(4):adj[i]|=1<<(i+1);adj[i+1]|=1<<i
    @lru_cache(None)
    def alpha(s):
        if not s:return 0
        bit=s&-s;i=bit.bit_length()-1
        return max(alpha(s^bit),1+alpha((s^bit)&~adj[i]))
    groups={r:{s for s in range(32) if alpha(s)==alpha(s & 0b01110)==r} for r in range(3)}
    predicted={0:[0],1:[2,3,4,6,8,12,24],2:[10,11,14,15,26,27,30]}
    assert {r:sorted(x) for r,x in groups.items()}==predicted
    expected={0:{0},1:{24},2:{30}}
    for r,ss in groups.items():
        unmatched,pairs=lex_matching(ss,5)
        assert unmatched==expected[r],(r,unmatched)
    print('LOCAL_TABLE_PASS 15 local subsets, three critical patterns')


def main():
    check_local_table()
    cases=[(m,k) for m in range(1,4) for k in range(2,7)] + [(4,4)]
    for m,k in cases:
        n,faces=face_poset(m,k)
        remaining,matching=lex_matching(faces,n)
        prediction=expected_critical(m,k)
        assert remaining==prediction,(m,k,sorted(remaining^prediction))
        assert check_acyclic(faces,matching),(m,k,'directed cycle')
        beta=sum(comb(m,r)*comb(m-r,k-1-2*r) for r in range(m+1) if 0<=k-1-2*r<=m-r)
        crit=Counter(s.bit_count()-1 for s in remaining)
        assert crit.get(2*k-3,0)==beta and crit.get(0,0)==1 and sum(crit.values())==1+beta
        print('CASE_PASS',m,k,'faces',len(faces),'pairs',len(matching), 'beta',beta,'DAG_TRUE')
    print('ALL_16_CASES_PASSED')

if __name__=='__main__':main()
