from itertools import product

def exhaustive_reduced(q):
    best=-1
    winners=[]
    states=0
    for x1 in range(1,q):
        y1=q-x1
        s2=x1*y1
        for x2 in range(s2+1):
            y2=s2-x2
            s3=x1*y2+x2*y1
            for x3 in range(s3+1):
                y3=s3-x3
                s4=x1*y3+x2*y2+x3*y1
                for side4 in (0,1): # 0 => x4=s4,y4=0; 1 => x4=0,y4=s4
                    x4,y4=(s4,0) if side4==0 else (0,s4)
                    s5=x1*y4+x2*y3+x3*y2+x4*y1
                    for side5 in (0,1):
                        x5,y5=(s5,0) if side5==0 else (0,s5)
                        val=x1*y5+x2*y4+x3*y3+x4*y2+x5*y1
                        states += 1
                        rec=(x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)
                        if val>best:
                            best=val; winners=[rec]
                        elif val==best:
                            winners.append(rec)
    return best,winners,states

def build_code(q, xs):
    alphabet=tuple(str(i) for i in range(q))
    x1,x2,x3,x4,x5=xs
    L=[None,set(alphabet[:x1])]
    R=[None,set(alphabet[x1:])]
    targets=[None,x1,x2,x3,x4,x5]
    for k in range(2,6):
        universe=set()
        for j in range(1,k):
            universe |= {u+v for u in L[j] for v in R[k-j]}
        assert len(universe)==sum(len(L[j])*len(R[k-j]) for j in range(1,k))
        ordered=sorted(universe)
        L.append(set(ordered[:targets[k]]))
        R.append(set(ordered[targets[k]:]))
    C=set()
    for i in range(1,6):
        C |= {u+v for u in L[i] for v in R[6-i]}
    return L,R,C

def check_nonoverlap(C,n=6):
    P=set(); S=set()
    for w in C:
        assert len(w)==n
        for k in range(1,n):
            P.add(w[:k]); S.add(w[n-k:])
    assert P.isdisjoint(S)
    return len(P),len(S)

expected={7:7776,8:16807,9:33872}
expected_reduced={
    7:{(6,0,0,0,0,1,6,36,216,1296),(1,6,36,216,1296,6,0,0,0,0)},
    8:{(7,0,0,0,0,1,7,49,343,2401),(1,7,49,343,2401,7,0,0,0,0)},
    9:{(7,2,0,0,0,2,12,88,640,4656),(2,12,88,640,4656,7,2,0,0,0)},
}
all_states=0
for q in (7,8,9):
    best,winners,states=exhaustive_reduced(q)
    all_states += states
    assert best==expected[q], (q,best)
    assert set(winners)==expected_reduced[q], (q,winners)
    # direct lower-bound construction from first winner
    w=winners[0]
    xs=w[:5]
    L,R,C=build_code(q,xs)
    assert len(C)==best
    p,s=check_nonoverlap(C)
    print(f'q={q} best={best} reduced_states={states} winners={len(winners)} codewords={len(C)} prefix_types={p} suffix_types={s}')
# check the q=9 improvement over k=5 Blackburn construction
blackburn9=max(l**5*(9-l) for l in range(1,9))
assert blackburn9==33614
assert expected[9]-blackburn9==258
print(f'Q9_GAP best={expected[9]} blackburn_k5={blackburn9} improvement=258')
print(f'VERIFY_OK q=7,8,9 reduced_states={all_states} direct_codewords={sum(expected.values())}')
