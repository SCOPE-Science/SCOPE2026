#!/usr/bin/env python3
"""Independent finite sanity checks for antiprism penultimate-distance topology.
Only standard-library dependencies. Infinite-family proof is in RESULT.md.
"""
import itertools, math
from collections import Counter
from fractions import Fraction

def geom(n):
    a=math.pi/(2*n)
    R=1/(2*math.sin(math.pi/n))
    hh=1-4*R*R*math.sin(a)**2
    assert hh>0
    p=[(R*math.cos(math.pi*i/n),R*math.sin(math.pi*i/n),((-1)**i)*math.sqrt(hh)/2) for i in range(2*n)]
    def dst(i,j): return sum((x-y)**2 for x,y in zip(p[i],p[j]))
    formula=lambda k: 4*R*R*math.sin(math.pi*k/(2*n))**2 + (k%2)*hh
    for i in range(2*n):
        for j in range(i+1,2*n):
            k=min(j-i,2*n-(j-i))
            assert abs(dst(i,j)-formula(k))<1e-9
    values=sorted({round(dst(0,j),9) for j in range(1,2*n)})
    second,top=values[-2:]
    far={(i,j) for i in range(2*n) for j in range(i+1,2*n) if abs(dst(i,j)-top)<1e-8}
    if n%2:
        expect={(i,i+n) for i in range(n)}
        second_expected=4*R*R*math.cos(a)**2
        top_expected=second_expected+1
        typ='perfect_matching'
    else:
        expect={(min(i,(i+n-1)%(2*n)),max(i,(i+n-1)%(2*n))) for i in range(2*n)}
        second_expected=4*R*R
        top_expected=second_expected+1-1/(2*math.cos(a)**2)
        typ='single_cycle'
    assert far==expect,(n,far,expect)
    assert abs(second-second_expected)<1e-7 and abs(top-top_expected)<1e-7
    return second,top,typ,far

def betti_mod2(n,edges):
    # Exhaustively enumerate independent faces at the penultimate threshold.
    N=2*n
    ban=[0]*N
    for a,b in edges:ban[a]|=1<<b;ban[b]|=1<<a
    faces=[[] for _ in range(n+2)]
    for mask in range(1,1<<N):
        if all(not (mask&(1<<j)) or not(ban[j]&mask) for j in range(N)):
            k=mask.bit_count()
            faces[k].append(mask)
    ranks=[0]*(len(faces)+1)
    for k in range(2,len(faces)):
        if not faces[k]:continue
        index={s:i for i,s in enumerate(faces[k-1])}
        piv={}
        for face in faces[k]:
            x=face
            col=0
            while x:
                b=x&-x;x-=b
                col^=1<<index[face^b]
            while col:
                q=col.bit_length()-1
                if q in piv:col^=piv[q]
                else:piv[q]=col;break
        ranks[k]=len(piv)
    return {k-1:len(faces[k])-ranks[k]-ranks[k+1] for k in range(1,len(faces)) if len(faces[k])-ranks[k]-ranks[k+1] and k>=2}

for n in range(4,61):
    second,top,typ,edges=geom(n)
    if n<=9:
        actual=betti_mod2(n,edges)
        if n%2: expected={n-1:1}
        elif n%3==0:expected={2*n//3-1:2}
        elif n%3==1:expected={(2*n-2)//3:1}
        else:expected={(2*n-4)//3:1}
        assert actual==expected,(n,actual,expected)
    if n in (4,5,6,7,8,9,10,12,15,20,40,60):
        print('n=%d penultimate_sq=%.10f top_sq=%.10f forbidden=%s edges=%d'%(n,second,top,typ,len(edges)))
print('VERIFY_OK')
