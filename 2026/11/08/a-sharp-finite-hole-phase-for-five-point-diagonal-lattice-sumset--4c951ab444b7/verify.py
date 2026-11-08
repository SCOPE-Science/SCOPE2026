"""Exact exhaustive independent checks for diagonal five-point sumsets."""

def direct(m,h):
    A=[(0,0),(1,0),(0,1),(m,m),(m+1,m+1)]
    S={(0,0)}
    for _ in range(h):
        S={(x+a,y+b) for x,y in S for a,b in A}
    return S

def polygon(m,h):
    M=(m+1)*h
    return {(x,y) for x in range(M+1) for y in range(M+1)
            if (m+1)*x-m*y<=M and (m+1)*y-m*x<=M}

def f(m,u):
    q,r=divmod(u,m+1)
    return q if r==0 else (q+1 if q+r>=m else q+2*r)

def predicted_holes(m,h):
    H=set()
    for r in range(1,m):
      for q in range(m-r):
        u=(m+1)*q+r
        for n in range(q+1,min(h,q+2*r-1)+1):
          v=h-n
          H.add((u+v,u)); H.add((u,u+v))
    return H

cases=0; checked_points=0
for m in range(2,9):
 for h in range(0,17):
    S=direct(m,h); P=polygon(m,h)
    assert S<=P
    H=P-S
    pred=predicted_holes(m,h)
    assert H==pred,(m,h,H^pred)
    assert len(S)==sum(2*(h-f(m,u))+1 for u in range((m+1)*h+1) if f(m,u)<=h)
    assert all(((x,y) in S)==(abs(x-y)+f(m,min(x,y))<=h) for x,y in P)
    if h>=2*m-2: assert len(H)==m*(m-1)*(2*m-1)//3
    if h==2*m-3: assert len(H)==m*(m-1)*(2*m-1)//3-1
    cases+=1; checked_points+=len(P)
print(f'PASS: {cases} parameter-degree cases; {checked_points} independently enumerated polygon points.')
print('PASS: five-generator sumsets, exact hole locations, minimum length, sharp constant phase.')
