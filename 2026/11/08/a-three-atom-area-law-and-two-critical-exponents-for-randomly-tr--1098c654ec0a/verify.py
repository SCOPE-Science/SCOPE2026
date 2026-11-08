"""Independent finite checks for the translated-disk lattice-hull area law.

No output from this program is a proof of the all-radius identities.
"""
import math
import random

CORNER = ((0, 0), (0, 1), (1, 0), (1, 1))


def exact_lens(r):
    if r <= 1 / math.sqrt(2):
        return 0.0
    return 2 * r*r * math.acos(1 / (math.sqrt(2) * r)) - math.sqrt(2) * math.sqrt(r*r - .5)


def exact_fourfold(r):
    if r <= 1 / math.sqrt(2):
        return 0.0
    return r*r * (math.pi - 4 * math.asin(1 / (2*r))) - 2 * math.sqrt(r*r - .25) + 1


def area_hull(points):
    pts = sorted(set(points))
    if len(pts) < 3:
        return 0.0
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower = []
    for p in pts:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(pts):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:
            upper.pop()
        upper.append(p)
    loop = lower[:-1]+upper[:-1]
    return .5 * abs(sum(loop[i][0]*loop[(i+1)%len(loop)][1]-loop[i][1]*loop[(i+1)%len(loop)][0] for i in range(len(loop))))


def area_at(x,y,r):
    return area_hull([(i,j) for i,j in CORNER if (x-i)**2+(y-j)**2 <= r*r])


def integrate_simpson(f, n=16000):
    assert n%2==0
    h=1.0/n
    return h/3*(f(0)+f(1)+4*sum(f(i*h) for i in range(1,n,2))+2*sum(f(i*h) for i in range(2,n,2)))


def lens_vertical_slice(x,r):
    r2 = r*r
    a=r2-x*x
    b=r2-(1-x)**2
    if a<=0 or b<=0:
        return 0.0
    return max(0.0, math.sqrt(a)+math.sqrt(b)-1)


def fourfold_vertical_slice(x,r):
    r2=r*r
    a=r2-x*x
    b=r2-(1-x)**2
    if a<=0 or b<=0:
        return 0.0
    return max(0.0, 2*min(math.sqrt(a),math.sqrt(b))-1)


def run():
    for r in (.65, .708, .73, .80, .90, .99):
        L,Q=exact_lens(r),exact_fourfold(r)
        assert -1e-12<=Q<=L+1e-12
        p0,p3,p4=1-2*L+Q,2*(L-Q),Q
        assert min(p0,p3,p4)>=-1e-12 and abs(p0+p3+p4-1)<1e-12
        ln=integrate_simpson(lambda x:lens_vertical_slice(x,r))
        qn=integrate_simpson(lambda x:fourfold_vertical_slice(x,r))
        assert abs(ln-L)<1.2e-5,(r,L,ln)
        assert abs(qn-Q)<1.2e-5,(r,Q,qn)
        ct=[0,0,0]
        grid=240
        for i in range(grid):
            for j in range(grid):
                area=area_at((i+.5)/grid,(j+.5)/grid,r)
                assert area in (0.0,.5,1.0),area
                ct[round(area*2)] += 1
        assert abs(ct[2]/grid**2-p4)<.004, (r,'square',ct,p4)
        assert abs(ct[1]/grid**2-p3)<.006, (r,'triangle',ct,p3)
        assert abs((ct[1]/2+ct[2])/grid**2-L)<.004
        print('radius',r,'L',round(L,8),'Q',round(Q,8),'grid_frequency',ct)
    # Independently evaluate the onset constants without reducing finite sampling to an infinite proof.
    for delta in (1e-2,1e-3,1e-4):
        r=math.sqrt(.5+delta)
        l,q=exact_lens(r),exact_fourfold(r)
        assert abs(l/delta**1.5-4*math.sqrt(2)/3)<.01
        assert abs(q/delta**2-2)<.03
    rng=random.Random(271828)
    for r in (.73,.85,.95):
        L,Q=exact_lens(r),exact_fourfold(r)
        counts=[0,0,0]
        for _ in range(180000):
            a=area_at(rng.random(),rng.random(),r)
            counts[int(2*a)]+=1
        assert abs(counts[1]/180000-2*(L-Q))<.006
        assert abs(counts[2]/180000-Q)<.006
    print('DISPLACED_DISK_HULL_AREA_LAW_CHECKS_PASSED')

if __name__=='__main__':
    run()
