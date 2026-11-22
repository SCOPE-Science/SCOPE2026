"""Standalone finite diagnostics for the circular-sector enclosing ellipse.

Run with Python 3.10+: python checker.py
These tests supplement the exact contact-moment and containment proof.
"""
import math

N = 0

def check(condition, description):
    global N
    N += 1
    if not condition:
        raise AssertionError(description)

def parameters(m):
    assert 0 <= m < 1
    s = math.sqrt(1-m*m)
    if m <= .25:
        return (1+2*m)/3, 2*(1-m)/3, 2*s/math.sqrt(3), "tip-corners"
    if m <= .75:
        return .5, .5, .5*math.sqrt((1+m)/m), "four"
    return 2*m/3, 2*m/3, 2*s/math.sqrt(3), "origin-corners"

def square_norm(x,y,c,a,b):
    return ((x-c)/a)**2+(y/b)**2

def contacts(m):
    c,a,b,reg=parameters(m)
    s=math.sqrt(1-m*m)
    if reg=="tip-corners":
        return [(1.,0.,1/3),(m,s,1/3),(m,-s,1/3)]
    if reg=="origin-corners":
        return [(0.,0.,1/3),(m,s,1/3),(m,-s,1/3)]
    v=2*m-1
    p=(3-4*m)/(8*(1-m))
    o=(4*m-1)/(8*m)
    t=1/(16*m*(1-m))
    return [(1.,0.,p),(0.,0.,o),(m,s,t),(m,-s,t)]

ms=[0,.001,.05,.24,.25,.250001,.35,.5,.65,.749999,.75,.750001,.8,.865,.9,.99,.999]
ms += [i/1000 for i in range(1,1000,17)]
for m in ms:
    c,a,b,reg=parameters(m)
    check(a>0 and b>0, f"nonpositive semiaxis at {m}")
    cs=contacts(m)
    check(abs(sum(w for x,y,w in cs)-1)<2e-12, f"total weight at {m}")
    check(all(w>=0 for x,y,w in cs), f"negative contact weight at {m}")
    u=[((x-c)/a,y/b,w) for x,y,w in cs]
    check(abs(sum(x*w for x,y,w in u))<2e-12, f"contact first x moment at {m}")
    check(abs(sum(y*w for x,y,w in u))<2e-12, f"contact first y moment at {m}")
    check(abs(sum(x*x*w for x,y,w in u)-.5)<2e-12, f"contact xx moment at {m}")
    check(abs(sum(y*y*w for x,y,w in u)-.5)<2e-12, f"contact yy moment at {m}")
    check(abs(sum(x*y*w for x,y,w in u))<2e-12, f"contact xy moment at {m}")
    for x,y,w in cs:
        check(abs(square_norm(x,y,c,a,b)-1)<3e-12, f"contact equation at {m}")
    theta=math.acos(m)
    for k in range(501):
        phi=theta*(2*k/500-1)
        x,y=math.cos(phi),math.sin(phi)
        check(square_norm(x,y,c,a,b)<1+2e-12,f"circle arc escaped ellipse at {m},{phi}")
    for k in range(101):
        t=k/100
        for sign in (-1,1):
            x,y=t*m,sign*t*math.sqrt(1-m*m)
            check(square_norm(x,y,c,a,b)<1+2e-12, f"radial edge escaped ellipse at {m},{t}")
    check(square_norm(0,0,c,a,b)<1+2e-12, f"sector origin escaped at {m}")

for m in (.25,.75):
    dc0,da0,db0,_=parameters(m)
    for h in (1e-4,1e-5,1e-6):
        cm,am,bm,_=parameters(m-h)
        cp,ap,bp,_=parameters(m+h)
        check(abs(cm-dc0)<3*h and abs(cp-dc0)<3*h, 'continuity center')
        check(abs(am-da0)<3*h and abs(ap-da0)<3*h, 'continuity x axis')
        check(abs(bm-db0)<5*h and abs(bp-db0)<5*h, 'continuity y axis')

print(f"PASS: {N} deterministic geometric and contact assertions")
