"""Exhaustive finite sanity checks for the two-reversal directed-flag classification.
Run: python verify.py
"""
from itertools import combinations
from collections import Counter

def transitive_faces(n, pairs):
    pairs = {tuple(sorted(p)) for p in pairs}
    bad = []
    for a,b,c in combinations(range(n),3):
        if ((a,b) in pairs) + ((a,c) in pairs) + ((b,c) in pairs) != 1:
            continue
        # A single reversed outer arc creates a directed triangle.
        if (a,c) in pairs:
            bad.append((1<<a)|(1<<b)|(1<<c))
    faces = [m for m in range(1,1<<n) if not any(m&t==t for t in bad)]
    return faces,bad

def forecast(n,pairs):
    p,q=sorted(map(lambda e:tuple(sorted(e)),pairs))
    v=sorted((*p,*q))
    a,b,c,d=v
    if a!=0 or d!=n-1: return {}
    if set(pairs)=={(a,b),(c,d)}:
        return {3:1} if c==b+1 and b>=a+2 and d>=c+2 else {}
    if set(pairs)=={(a,c),(b,d)}:
        return {1:1} if n==4 else {}
    if set(pairs)=={(a,d),(b,c)}:
        return {1:1,2:1} if b==a+1 and c==d-1 and c>=b+2 else {1:1}
    raise AssertionError(pairs)

def betti_mod_two(n, faces):
    groups=[[] for _ in range(n)]
    for f in faces:groups[f.bit_count()-1].append(f)
    ranks=[]
    for dim in range(1,n):
        lo={f:i for i,f in enumerate(groups[dim-1])}
        piv={}
        for face in groups[dim]:
            bits=[v for v in range(n) if face>>v&1]
            v=sum(1<<lo[face^(1<<x)] for x in bits)
            while v:
                i=v.bit_length()-1
                if i in piv:v^=piv[i]
                else:piv[i]=v;break
        ranks.append(len(piv))
    b={}
    for d,g in enumerate(groups):
        x=len(g)-(ranks[d-1] if d else 0)-(ranks[d] if d<n-1 else 0)
        if d==0:x-=1
        if x:b[d]=x
    return b

def collapse_certificate():
    n=5;pairs=[(0,3),(1,4)]
    faces,bad=transitive_faces(n,pairs)
    seq=[('13','123'),('12','012'),('14','014'),('02','024'),('04','034'),('34','234'),('1','01'),('0','03'),('3','23'),('4','24')]
    current=set(faces)
    for low,high in seq:
        s=sum(1<<int(i) for i in low);t=sum(1<<int(i) for i in high)
        assert s in current and t in current and t.bit_count()==s.bit_count()+1 and t&s==s
        assert sum(1 for f in current if (f&s)==s)==2, (low,high)
        current.remove(s);current.remove(t)
    assert current=={1<<2},current
    return len(seq)

if __name__=='__main__':
    assert collapse_certificate()==10
    cases=0;classes=Counter()
    for n in range(4,10):
        for v in combinations(range(n),4):
            a,b,c,d=v
            for pairs in (((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))):
                actual=betti_mod_two(n,transitive_faces(n,pairs)[0])
                expected=forecast(n,pairs)
                assert actual==expected,(n,pairs,actual,expected)
                cases+=1
                classes[tuple(sorted(expected.items()))]+=1
    print('verified_pairings',cases)
    print('class_counts', sorted(classes.items(),key=lambda kv:str(kv[0])))
    print('crossing_five_vertex_elementary_collapses',collapse_certificate())
    print('PASS')
