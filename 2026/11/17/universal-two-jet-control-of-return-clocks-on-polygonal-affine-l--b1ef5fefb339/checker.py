"""Reproducible finite checks for all-sector local return-clock control.

Python 3 standard library only. Run `python3 checker.py`.
Analytical identities, not these finite experiments, establish the theorem.
"""
import math


def make_data(vertices, speeds, contractions):
    n = len(vertices)
    assert n >= 3 and len(speeds) == n and len(contractions) == n
    data = []
    for i, p in enumerate(vertices):
        z = vertices[(i+1)%n]
        e = (z[0]-p[0],z[1]-p[1])
        E = e[0]*e[0]+e[1]*e[1]
        delta=p[0]*z[1]-p[1]*z[0]
        assert delta>0 and E>0
        omega=speeds[i]
        c=contractions[i]
        k=omega*c
        q=math.exp(-c)
        alpha=(e[0]*p[0]+e[1]*p[1])/E
        mu0=k/delta*(alpha-q/(1-q))
        B=delta*(1-q)/(k*omega)
        data.append(dict(p=p,z=z,e=e,E=E,delta=delta,
                         omega=omega,c=c,k=k,q=q,alpha=alpha,mu0=mu0,B=B))
    return data


def leg(r, d, mu):
    alpha,delta,k,omega = d['alpha'],d['delta'],d['k'],d['omega']
    b=alpha-mu*delta/k
    t=1/omega
    for _ in range(12):
        decay=math.exp(-k*t)
        f=omega*t-1-r*((b+1)*decay-b)
        derivative=omega+r*k*(b+1)*decay
        t-=f/derivative
    assert t>0
    out=r*math.exp(-k*t)
    e,p,z=d['e'],d['p'],d['z']
    norm=(e[1],-e[0])
    integral=delta*r*(1-math.exp(-k*t))/k
    x=((1+r)*p[0]+omega*t*e[0]-integral*(mu*e[0]+k/d['E']*norm[0]),
       (1+r)*p[1]+omega*t*e[1]-integral*(mu*e[1]+k/d['E']*norm[1]))
    assert max(abs(x[j]-(1+out)*z[j]) for j in (0,1)) <2e-11
    return t,out


def return_map(r,data,mu):
    total=0.0
    for d,gain in zip(data,mu):
        tau,r=leg(r,d,gain)
        total+=tau
    return total,r


def numerical_jets(data,mu,h=0.0009):
    tp=return_map(h,data,mu)[0]
    tm=return_map(-h,data,mu)[0]
    t0=return_map(0,data,mu)[0]
    return (tp-tm)/(2*h),(tp+tm-2*t0)/(2*h*h)


def expected_jacobian(data):
    Q=1.0
    first=[];second=[];ratios=[]
    for d in data:
        first.append(Q*d['B'])
        ratio=Q*d['c']*d['q']/(1-d['q'])
        ratios.append(ratio)
        second.append(-Q*d['B']*ratio)
        Q*=d['q']
    assert all(ratios[i]>ratios[i+1] for i in range(len(data)-1))
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            det=first[i]*second[j]-first[j]*second[i]
            assert det>0,('minor',i,j,det)
    return first,second,ratios


def check_case(name,vertices,omegas,cs,checked_indices):
    data=make_data(vertices,omegas,cs)
    mu=[d['mu0'] for d in data]
    T=sum(1/v for v in omegas)
    Q=math.prod(d['q'] for d in data)
    for s in [-.025,-.01,-.001,0.0,.001,.01,.025]:
        t,out=return_map(s,data,mu)
        assert abs(t-T)<2e-12
        assert abs(out-Q*s)<2e-12
    G,H=numerical_jets(data,mu)
    assert abs(G)<1e-8 and abs(H)<1e-8
    first,second,ratios=expected_jacobian(data)
    for i in checked_indices:
        delta=.004
        plus=mu.copy();minus=mu.copy()
        plus[i]+=delta;minus[i]-=delta
        gp,hp=numerical_jets(data,plus)
        gm,hm=numerical_jets(data,minus)
        dg=(gp-gm)/(2*delta)
        dh=(hp-hm)/(2*delta)
        assert abs(dg-first[i])<8e-6,(name,i,dg,first[i])
        assert abs(dh-second[i])<8e-6,(name,i,dh,second[i])
    print(name,'N=',len(data),'T=',round(T,9),'q_total=',round(Q,9))
    print('  jet Jacobian G row=',[round(x,9) for x in first])
    print('  jet Jacobian H row=',[round(x,9) for x in second])
    print('  strictly decreasing curvature ratios=',[round(x,9) for x in ratios])


def main():
    tri=[(1.0,0.0),(0.0,1.0),(-1.0,-1.0)]
    c=math.log(2)
    check_case('equal-decay triangle',tri,[1,1,1],[c]*3,range(3))
    ang=[0.0,1.2,2.4,3.7,5.0]
    radii=[1.0,1.5,0.8,1.2,1.1]
    five=[(r*math.cos(a),r*math.sin(a)) for r,a in zip(radii,ang)]
    check_case('inhomogeneous pentagon',five,[1,1.4,.9,1.2,1.8],
               [.3,1.1,.7,1.5,.5],range(5))
    print('All sector-boundary, jet, and strict minor checks passed.')

if __name__=='__main__':
    main()
