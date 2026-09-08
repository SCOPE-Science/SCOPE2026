
from fractions import Fraction as Q
def _hits(P, w):
    hs = []
    for i in range(len(P) - 1):
        p, q = P[i], P[i + 1]
        sp = p[0] + p[1] - w; sq = q[0] + q[1] - w
        if sp == 0 and sq == 0: return ('seg', sorted([p[0], q[0]]))
        if sp == 0: hs.append(p[0])
        elif sq == 0: hs.append(q[0])
        elif (sp < 0) != (sq < 0):
            t = sp / (sp - sq); hs.append(p[0] + t * (q[0] - p[0]))
    return ('pts', sorted(set(hs)))
def _valid(c):
    return (len(c) >= 2 and c[0][1] == 0 and c[0][0] > 0 and c[-1][0] == 0 and c[-1][1] > 0
        and all(c[i+1][0] <= c[i][0] and c[i+1][1] >= c[i][1] for i in range(len(c)-1))
        and any(c[i+1][0] < c[i][0] for i in range(len(c)-1)))
def _clean(c):
    pts=[c[0]]
    for p in c[1:]:
        if p != pts[-1]: pts.append(p)
    return pts
def concave_weights(chain):
    P0=[(Q(x),Q(y)) for x,y in chain]; out=[]; stack=[P0]; g=0
    while stack:
        g+=1
        if g>500: raise RuntimeError('guard')
        P=stack.pop(); a=P[0][0]; b=P[-1][1]
        if a<=0 or b<=0 or len(P)<2: continue
        w=min([a,b]+[x+y for x,y in P])
        if w<=0: continue
        out.append(w)
        kind,h=_hits(P,w)
        if kind=='seg': x2,x3=h[0],h[1]
        elif not h: x2,x3=Q(0),w
        else: x2,x3=h[0],h[-1]
        y3=w-x3; y2=w-x2
        if y3!=0:
            sub=[p for p in P if p[0]>=x3]+([(x3,y3)] if not any(p[0]==x3 for p in P) else [])
            rp=_clean([(X+Y-w,Y) for X,Y in sub])
            if _valid(rp): stack.append(rp)
        if x2!=0:
            sub=([(x2,y2)] if not any(p[0]==x2 for p in P) else [])+[p for p in P if p[0]<=x2]
            up=_clean([(X,X+Y-w) for X,Y in sub])
            if _valid(up): stack.append(up)
    return sorted(out,reverse=True)
def chain_area(chain):
    A=Q(0); P=[(Q(x),Q(y)) for x,y in chain]
    for i in range(1,len(P)): A+=(P[i-1][0]-P[i][0])*(P[i-1][1]+P[i][1])/2
    return A
