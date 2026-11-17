"""Independent computational checks of polygon boundary-sampling corner law.

Only the Python standard library is needed.  Statistical checks are diagnostics,
not a substitute for the asymptotic proof.
"""
import math, random, statistics


def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def convex_hull(points):
    s=sorted(points)
    low=[]
    for p in s:
        while len(low)>1 and cross(low[-2],low[-1],p)<=1e-14:
            low.pop()
        low.append(p)
    up=[]
    for p in s[::-1]:
        while len(up)>1 and cross(up[-2],up[-1],p)<=1e-14:
            up.pop()
        up.append(p)
    return low[:-1]+up[:-1]


def area(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[i][1]*poly[(i+1)%len(poly)][0] for i in range(len(poly)))/2)


def perimeter(poly):
    return sum(math.dist(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))


def info(poly):
    m=len(poly)
    lengths=[math.dist(poly[i],poly[(i+1)%m]) for i in range(m)]
    theta=[]
    for i in range(m):
        a=poly[(i-1)%m]; b=poly[i]; c=poly[(i+1)%m]
        x=(a[0]-b[0],a[1]-b[1]); y=(c[0]-b[0],c[1]-b[1])
        cos=(x[0]*y[0]+x[1]*y[1])/(math.hypot(*x)*math.hypot(*y))
        theta.append(math.acos(max(-1,min(1,cos))))
    return lengths,theta,sum(lengths)


def experiment(poly,n,rng):
    m=len(poly); lengths,angles,P=info(poly)
    cum=[0.]
    for l in lengths: cum.append(cum[-1]+l)
    side_pos=[[] for _ in range(m)]; pts=[]
    import bisect
    for _ in range(n):
        t=rng.random()*P
        k=min(bisect.bisect_right(cum,t)-1,m-1)
        u=t-cum[k]
        side_pos[k].append(u)
        p=poly[k]; q=poly[(k+1)%m]
        pts.append((p[0]+u*(q[0]-p[0])/lengths[k],p[1]+u*(q[1]-p[1])/lengths[k]))
    good=all(len(a)>=2 for a in side_pos)
    if not good: return None
    missing_area=0.; missing_perimeter=0.
    for i in range(m):
        x=lengths[i-1]-max(side_pos[i-1])
        y=min(side_pos[i])
        th=angles[i]
        missing_area+=.5*math.sin(th)*x*y
        missing_perimeter+=x+y-math.sqrt(x*x+y*y-2*x*y*math.cos(th))
    hull=convex_hull(pts)
    area_direct=area(poly)-area(hull)
    per_direct=P-perimeter(hull)
    assert abs(missing_area-area_direct)<1e-8, (missing_area,area_direct)
    assert abs(missing_perimeter-per_direct)<1e-8, (missing_perimeter,per_direct)
    return n*n*missing_area/P**2, n*missing_perimeter/P


def check():
    rng=random.Random(2026110109)
    shapes={
        'scalene triangle':[(0.,0.),(3.,0.),(.65,2.1)],
        'rectangle':[(0.,0.),(2.8,0.),(2.8,1.),(0.,1.)],
        'irregular pentagon':[(0.,0.),(2.,0.),(2.8,1.1),(1.9,2.6),(-.6,1.2)],
    }
    for name,poly in shapes.items():
        lengths,theta,P=info(poly)
        assert all(0<t<math.pi for t in theta)
        if name=='scalene triangle':
            # Sine rule: angle signatures recover triangle side ratios.
            sin_theta=[math.sin(t) for t in theta]
            vertex_opposite=[lengths[(i+1)%3] for i in range(3)]
            ratios=[sin_theta[i]/vertex_opposite[i] for i in range(3)]
            assert max(ratios)-min(ratios)<1e-12
        vals=[]
        for j in range(1200):
            z=experiment(poly,120 if name!='irregular pentagon' else 180,rng)
            if z is not None: vals.append(z)
        assert len(vals)>1100
        predicted_mean=.5*sum(math.sin(t) for t in theta)
        predicted_var=.75*sum(math.sin(t)**2 for t in theta)
        empirical_mean=statistics.mean(x for x,_ in vals)
        assert abs(empirical_mean-predicted_mean)<0.20*predicted_mean,(name,empirical_mean,predicted_mean)
        # Variance of the limiting law is nonzero and matches its product structure.
        lim=[]
        for _ in range(80000):
            lim.append(.5*sum(math.sin(t)*rng.expovariate(1)*rng.expovariate(1) for t in theta))
        lm=statistics.mean(lim); lv=statistics.pvariance(lim)
        assert abs(lm-predicted_mean)<.045*predicted_mean
        assert abs(lv-predicted_var)<.12*predicted_var
        # Exact finite-n comparison of a local corner product using integrals.
        k=120
        for i,t in enumerate(theta):
            a=lengths[(i-1)%len(poly)]
            b=lengths[i]
            exact=P*P/((k+1)*(k+2))*(1-(1-a/P)**(k+2)-(1-b/P)**(k+2)+(1-(a+b)/P)**(k+2))
            leading=P*P/((k+1)*(k+2))
            assert 0<exact<=leading*(1+1e-12)
        print(name, 'n samples',len(vals),'rescaled area mean',round(empirical_mean,5),
              'target',round(predicted_mean,5),'variance',round(lv,5),'target',round(predicted_var,5))
    # Jensen strictness, regular triangle versus scalene triangle.
    theta=info(shapes['scalene triangle'])[1]
    assert sum(math.sin(t) for t in theta)<3*math.sin(math.pi/3)
    print('BOUNDARY_POLYGON_CORNER_LAW_CHECKS_PASSED')

if __name__=='__main__': check()
