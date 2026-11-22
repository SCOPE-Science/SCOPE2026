#!/usr/bin/env python3
"""Exact small-order checks for modular 3-flow cycle reversal sectors.
Only Python standard library is required. Vertex labels and shore sizes are fixed.
"""
from collections import defaultdict, Counter
from itertools import product, combinations
from math import comb


def count_formula(left_size, t):
    d = t // 3
    if left_size == 2:
        return 2*d+1
    assert left_size == 4
    return (2*d+1)*(8*d*d+8*d+3)//3


def check_one(left_size, t):
    # A word chooses the incoming pair at each vertex of the degree-left_size shore.
    patterns = tuple(combinations(range(left_size), left_size//2))
    # left_size=2: each column picks 1; left_size=4: picks 2.
    masks = [sum(1<<r for r in p) for p in patterns]
    code_of = {mask:i for i,mask in enumerate(masks)}
    base=len(masks); ncol=2*t
    powers=[base**j for j in range(ncol)]
    valid={}; degrees={}; pattern_words={}
    for word in product(range(base), repeat=ncol):
        counts=[0]*left_size
        for d in word:
            mask=masks[d]
            for r in range(left_size):
                counts[r]+=(mask>>r)&1
        if any((v-t)%3 for v in counts): continue
        code=sum(v*powers[j] for j,v in enumerate(word))
        valid[code]=code
        degrees[code]=tuple(counts)
        pattern_words[code]=word
    def find(a):
        while valid[a]!=a:
            valid[a]=valid[valid[a]]; a=valid[a]
        return a
    def union(a,b):
        a=find(a); b=find(b)
        if a!=b: valid[b]=a
    # Every checker edge is an actual directed 4-cycle flip: an alternating 2x2 switch.
    for code,word in pattern_words.items():
        for j in range(ncol):
            ma=masks[word[j]]
            for k in range(j+1,ncol):
                mb=masks[word[k]]
                for ra in range(left_size):
                    if not (ma>>ra&1) or (mb>>ra&1): continue
                    for rb in range(left_size):
                        if (ma>>rb&1) or not (mb>>rb&1): continue
                        na=ma ^ (1<<ra) ^ (1<<rb)
                        nb=mb ^ (1<<ra) ^ (1<<rb)
                        other=code+(code_of[na]-word[j])*powers[j]+(code_of[nb]-word[k])*powers[k]
                        if other not in valid: raise AssertionError('illegal switch')
                        union(code,other)
    classes=defaultdict(list)
    for code in pattern_words: classes[find(code)].append(code)
    sectors=defaultdict(set)
    for root,states in classes.items():
        sigs={degrees[c] for c in states}
        assert len(sigs)==1, 'cycle flip changed margins'
        sectors[next(iter(sigs))].add(root)
    assert all(len(roots)==1 for roots in sectors.values()), 'one sector disconnected'
    assert len(classes)==count_formula(left_size,t)
    singleton=sum(len(states)==1 for states in classes.values())
    assert singleton == (comb(left_size,left_size//2) if t%3==0 else 0)
    if left_size==2:
        for r,roots in sectors.items():
            assert len(classes[next(iter(roots))])==comb(ncol,r[0])
    else:
        # Independently obtain the coefficient of e_2(x)^ncol by dynamic programming.
        dp={(0,)*4:1}
        for _ in range(ncol):
            nxt=defaultdict(int)
            for r,v in dp.items():
                for i,j in combinations(range(4),2):
                    rr=list(r);rr[i]+=1;rr[j]+=1
                    nxt[tuple(rr)]+=v
            dp=nxt
        for r,roots in sectors.items():
            assert len(classes[next(iter(roots))]) == dp[r]
    sizes=Counter(map(len,classes.values()))
    print('PASS', 'K_%d,%d'%(left_size,ncol), 'flows',len(pattern_words),
          'components',len(classes),'isolated',singleton,
          'size_histogram',sorted(sizes.items())[:20])


def check_formula():
    for left_size in (2,4):
        for t in range(1,30):
            d=t//3; slots=range(-d,d+1)
            if left_size==2:
                count=sum(a+b==0 for a in slots for b in slots)
            else:
                count=sum(-d<=-a-b-c<=d for a in slots for b in slots for c in slots)
            assert count==count_formula(left_size,t)
    print('PASS', 'ALL_SMALL_CLOSED_FORMS t=1..29')



def exact_character_filter():
    # Eisenstein integers a+b*w, where w*w+w+1=0.
    units=((1,0),(0,1),(-1,-1))
    def mul(x,y):
        a,b=x; c,d=y
        return (a*c-b*d,a*d+b*c-b*d)
    profile=Counter()
    for tail in product(range(3),repeat=3):
        phase=(0,)+tail
        z=(0,0)
        for i,j in combinations(range(4),2):
            u=units[(phase[i]+phase[j])%3]
            z=(z[0]+u[0],z[1]+u[1])
        eigen=mul(mul(z,z),units[(-sum(phase))%3])
        profile[eigen]+=1
    assert profile == Counter({(36,0):1,(9,0):14,(0,0):12}), profile
    print('PASS EXACT_EISENSTEIN_CHARACTER_ORBITS',dict(profile))


def exact_totals():
    for t in range(1,11):
        n=2*t
        dp={(0,0,0,0):1}
        for _ in range(n):
            nxt=defaultdict(int)
            for z,c in dp.items():
                for i,j in combinations(range(4),2):
                    w=list(z);w[i]+=1;w[j]+=1
                    nxt[tuple(w)]+=c
            dp=nxt
        value=sum(c for z,c in dp.items() if all((r-t)%3==0 for r in z))
        assert value * 27 == 36**t+14*9**t, (t,value)
        assert sum(comb(n,t+3*s) for s in range(-(t//3),t//3+1))*3 == 4**t+2
    print('PASS EXACT_TOTAL_FLOW_COUNTS t=1..10')

if __name__=='__main__':
    exact_character_filter()
    exact_totals()
    check_formula()
    for left_size in (2,4):
        for t in range(1,5):
            check_one(left_size,t)
    print('VERIFY_OK')
