"""Standalone numerical diagnostics for a symmetry-plane cylinder benchmark.
No external dependencies. Analytic statements are established in RESULT.md, not by this checker.
"""
import math, random, itertools

HCRIT = math.sqrt(2.0 + math.sqrt(5.0))

def predicted(h, a):
    d = h * math.sqrt(max(0.0, 1.0-a*a))
    if d*d <= 1.0+a*a:
        return math.hypot(1.0, a)
    D = d+a
    return 0.5*(D+1.0/D)

def optimum(h):
    if h <= 1.0: return (1.0, 0.0)
    if h < HCRIT: return (0.5*(h+1.0/h), 0.0)
    a = math.sqrt((h*h-1.0)/(h*h+1.0))
    return (h*math.sqrt(2.0/(h*h+1.0)), a)

def enclosing_circle(P):
    """Independent exhaustive Euclidean MEC through 2 or 3 of five points."""
    candidates=[]
    for i,j in itertools.combinations(range(len(P)), 2):
        c=((P[i][0]+P[j][0])/2, (P[i][1]+P[j][1])/2)
        radius=max(math.dist(p,c) for p in P)
        if abs(radius-math.dist(P[i],c))<1e-8 and abs(radius-math.dist(P[j],c))<1e-8:
            candidates.append(radius)
    for i,j,k in itertools.combinations(range(len(P)),3):
        ax,ay=P[i]; bx,by=P[j]; cx,cy=P[k]
        det=2*((bx-ax)*(cy-ay)-(by-ay)*(cx-ax))
        if abs(det)<1e-10: continue
        v=(bx*bx+by*by-ax*ax-ay*ay)
        w=(cx*cx+cy*cy-ax*ax-ay*ay)
        ux=(v*(cy-ay)-w*(by-ay))/det
        uy=((bx-ax)*w-(cx-ax)*v)/det
        center=(ux,uy)
        radius=max(math.dist(p,center) for p in P)
        if abs(radius-math.dist(P[i],center))<1e-8 and abs(radius-math.dist(P[j],center))<1e-8 and abs(radius-math.dist(P[k],center))<1e-8:
            candidates.append(radius)
    assert candidates, "No determining circle found"
    return min(candidates)

def points(h,a):
    d=h*math.sqrt(max(0.,1.-a*a))
    return [(sgn*a,y) for sgn in (-1.,1.) for y in (-1.,1.)]+[(d,0.)]

def run():
    n=0
    rng=random.Random(168311)
    for h in [0.2,0.75,1,1.05,1.3,math.sqrt(2),1.8,2.0,HCRIT,2.2,3.,6.,20.]+[10**rng.uniform(-1.0,1.5) for _ in range(90)]:
        for a in [0,0.001,0.1,0.5,0.9,1.0]+[rng.random() for _ in range(70)]:
            r=predicted(h,a)
            brute=enclosing_circle(points(h,a))
            assert abs(r-brute)<5e-8 *max(1.,r), (h,a,r,brute)
            n+=1
        rstar,astar=optimum(h)
        assert abs(predicted(h,astar)-rstar)<1e-9, (h,rstar,astar)
        n+=1
        # Check global symmetry-plane minimum against a fine deterministic grid.
        for j in range(301):
            assert predicted(h,j/300.)+1e-9>=rstar, (h,j,rstar)
            n+=1
    assert abs(optimum(HCRIT)[0]-(HCRIT+1/HCRIT)/2)<2e-14
    assert (1+math.sqrt(5)/2)>1
    print('PASS',n+2,'independent MEC / extremal grid checks')
if __name__=='__main__':run()
