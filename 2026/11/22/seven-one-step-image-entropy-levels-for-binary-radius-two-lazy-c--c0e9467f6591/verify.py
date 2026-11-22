#!/usr/bin/env python3
"""Exact subset automata, spectral polynomials, and independent finite-word comparison.
Dependencies: Python 3.9+ and SymPy 1.12+. Execute in this directory.
"""
from collections import deque
from pathlib import Path
from fractions import Fraction
import csv
import sympy as sp

z=sp.symbols('z')
POLY={
 'A':z**5-z**4-z**3-z**2-z-1,
 'B':z**7-2*z**6+z**2-1,
 'C':z**5-2*z**4+z-1,
 'D':z**6-2*z**5+z-1,
 'E':z**5-2*z**4+z**2-2*z+1,
 'F':z**5-2*z**4+z**3-2*z**2+z-1,
 'G':z**5-2*z**4+z**2-z-1,
}
CLASS={0:'A',1:'B',2:'C',3:'D',4:'C',5:'E',6:'F',7:'B',8:'B',9:'C',10:'E',11:'C',12:'D',13:'C',14:'B',15:'G'}
# Disjoint rational intervals, all endpoints are exact integers / 10^9.
INTERVAL={
 'A':(1965948236,1965948237),
 'B':(1948935746,1948935747),
 'C':(1933184981,1933184982),
 'D':(1967168212,1967168213),
 'E':(1937629450,1937629451),
 'F':(1947891872,1947891873),
 'G':(1941713034,1941713035),
}
def image_local(a,b,c,d,e,p):
    return 1 if c==1 or (a+2*b+4*d+8*e==p) else 0

def graph(p):
    # De Bruijn input states (a,b,c,d) encoded a*8+b*4+c*2+d.
    local=[[0,0] for _ in range(16)]
    for s in range(16):
        a,b,c,d=(s>>3)&1,(s>>2)&1,(s>>1)&1,s&1
        for e in (0,1):
            label=image_local(a,b,c,d,e,p)
            local[s][label]|=1<<((2*s+e)&15)
    whole=(1<<16)-1
    states=[whole]; id_of={whole:0}; edges=[]; todo=deque([whole])
    while todo:
        mask=todo.popleft(); row=[]
        for label in (0,1):
            dest=0
            for v in range(16):
                if (mask>>v)&1: dest|=local[v][label]
            if dest!=0 and dest not in id_of:
                id_of[dest]=len(states);states.append(dest);todo.append(dest)
            row.append(id_of.get(dest,-1))
        edges.append(row)
    return states,edges

def word_count(edges,n):
    a=[0]*len(edges); a[0]=1
    for _ in range(n):
        b=[0]*len(edges)
        for i,(u,v) in enumerate(edges):
            if u>=0:b[u]+=a[i]
            if v>=0:b[v]+=a[i]
        a=b
    return sum(a)

def brute(p,n):
    # Independent direct local-window enumeration, no automaton states.
    words=set()
    for seed in range(1<<(n+4)):
        bits=[(seed>>i)&1 for i in range(n+4)]
        w=0
        for i in range(n):
            a,b,c,d,e=bits[i:i+5]
            w|=image_local(a,b,c,d,e,p)<<i
        words.add(w)
    return len(words)

def textcsv(rows):
    import io
    out=io.StringIO(newline='')
    csv.writer(out,lineterminator='\n').writerows(rows)
    return out.getvalue()


# A two-step local check uses nine source bits for every output at the origin.
def apply_local(initial,p,i):
    a,b,c,d,e=initial[i-2:i+3]
    return image_local(a,b,c,d,e,p)
nonidempotent=[]
for p in range(16):
    found=False
    for seed in range(512):
        window=[(seed>>j)&1 for j in range(9)]
        first=window[:]
        for i in range(2,7): first[i]=apply_local(window,p,i)
        second=apply_local(first,p,4)
        if first[4]!=second: found=True;break
    if found:nonidempotent.append(p)
assert nonidempotent==[1,3,7,8,12,14], nonidempotent

# Their fixed-point shifts exclude a single five-bit word; all share
# the same Perron polynomial, whereas their one-step images have two others.
fixed_poly=sp.Poly(z**4-z**3-z**2-z-1,z)
for p in nonidempotent:
    A=sp.zeros(16)
    for st in range(16):
        a,b,c,d=(st>>3)&1,(st>>2)&1,(st>>1)&1,st&1
        for e in (0,1):
            if c==0 and a+2*b+4*d+8*e==p: continue
            A[st,(2*st+e)&15]+=1
    cp=sp.Poly(A.charpoly(z).as_expr(),z)
    assert cp==sp.Poly(z**11*(z-1)*fixed_poly.as_expr(),z),(p,'fixed factor')
assert fixed_poly.count_roots(sp.Rational(1927561975,10**9),sp.Rational(1927561976,10**9))==1
assert fixed_poly.count_roots(sp.Rational(1927561976,10**9),sp.Integer(2))==0

rows=[['pattern_code','entropy_class','reachable_nonempty_states','perron_poly','root_lower_numerator','root_upper_numerator']]
counts=[['pattern_code']+[f'n{n}' for n in range(11)]]
for p in range(16):
    states,edges=graph(p)
    M=sp.zeros(len(states))
    for i, row in enumerate(edges):
        for j in row:
            if j>=0:M[i,j]+=1
    char=sp.Poly(M.charpoly(z).as_expr(),z)
    class_name=CLASS[p]; f=sp.Poly(POLY[class_name],z)
    assert char.rem(f)==sp.Poly(0,z), (p,'factor')
    low,high=INTERVAL[class_name]
    lo=sp.Rational(low,10**9); hi=sp.Rational(high,10**9)
    assert char.count_roots(lo,hi)==1,(p,'inside')
    assert char.count_roots(hi,sp.Integer(2))==0,(p,'outside')
    assert f.count_roots(lo,hi)==1,(p,'poly isolate')
    assert char.eval(2)!=0,(p,'at 2')
    assert len(states)<=14,(p,'state bound')
    numbers=[word_count(edges,n) for n in range(11)]
    for n in range(10):
        assert numbers[n]==brute(p,n),(p,n,'direct')
    counts.append([p]+numbers)
    rows.append([p,class_name,len(states),str(sp.expand(f.as_expr())),low,high])

for name,data in [('spectral_classes.csv',rows),('word_counts.csv',counts)]:
    expected=textcsv(data)
    saved=Path(name).read_text(encoding='utf-8')
    assert saved==expected, name
print('PASS: 16 complete subset automata; 7 isolated Perron factors; 160 direct-word tests; 16 exhaustive two-step tests; common fixed-shift polynomial for 6 non-idempotent patterns; both CSV catalogs.')
