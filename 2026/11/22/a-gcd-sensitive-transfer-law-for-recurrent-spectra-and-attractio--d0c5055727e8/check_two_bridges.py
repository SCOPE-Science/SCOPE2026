"""Direct complete finite functional-graph check for two incoming bridges.
The two added arcs are U_0->V_0 and U_s->V_0, 1<=s<a.
"""
from collections import Counter
from math import gcd,lcm,comb

def step(x,a,b,s):
    u=x&((1<<a)-1);v=x>>a
    un=sum(((u>>((i-1)%a))&1)<<i for i in range(a))
    vn=(((v>>(b-1))&1)&(u&1)&((u>>s)&1))
    vn|=sum(((v>>(j-1))&1)<<j for j in range(1,b))
    return un | (vn<<a)

def pred(x,a,b,s):
    g=gcd(a,b)
    u=x&((1<<a)-1);v=x>>a
    A={i for i in range(g) if all(((u>>t)&1) for t in range(i,a,g))}
    accepted={r for r in range(g) if r in A and (r+s)%g in A}
    filtered=sum((((v>>j)&1) if (j+1)%g in accepted else 0)<<j for j in range(b))
    return u | (filtered<<a),len(accepted)

def poly_multiply(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,pi in enumerate(p):
      for j,qj in enumerate(q): r[i+j]+=pi*qj
    return r

def poly_add(p,q):
    r=[0]*max(len(p),len(q))
    for i,x in enumerate(p):r[i]+=x
    for i,x in enumerate(q):r[i]+=x
    return r

def trace_poly(a,b,s):
    g=gcd(a,b);alpha=a//g
    w=(1<<alpha)-1
    h=gcd(g,s);m=g//h
    # trace [[w,w],[1,X]]**m via trace-recurrence (Cayley-Hamilton)
    t0=[2]
    t1=[w,1] # trace T = w + X
    # det(T)=w*(X-1), trace recurrence t_m=(w+X)t_m-1 - w*(X-1)t_m-2
    for i in range(2,m+1):
        u=poly_multiply([w,1],t1)
        v=poly_multiply([-w,w],t0)
        n=poly_add(u,[-x for x in v]);t0,t1=t1,n
    p=[1]
    for _ in range(h):p=poly_multiply(p,t1)
    return p

def case(a,b,s):
    L=lcm(a,b)
    total=1<<(a+b)
    f=[step(x,a,b,s) for x in range(total)]
    fl=list(range(total))
    for _ in range(L):fl=[f[x] for x in fl]
    assert all(fl[x]==pred(x,a,b,s)[0] for x in range(total)),(a,b,s,'projection')
    fibers=Counter(fl)
    g=gcd(a,b);beta=b//g
    kstats=Counter()
    for phase,num in fibers.items():
       _,k=pred(phase,a,b,s)
       assert num==(1<<(beta*(g-k))),(a,b,s,phase,k,num)
       kstats[k]+=1
    P=trace_poly(a,b,s)
    # Coefficient k of P is #upstream configurations with k accepting residue classes.
    for k,p in enumerate(P):
        assert kstats[k]==p*(1<<(beta*k)),(a,b,s,k,kstats[k],p)
    assert len(fibers)==sum(p*(1<<(beta*k)) for k,p in enumerate(P))
    no_surv_expected=sum(p*(1<<(b-beta*k)) for k,p in enumerate(P))
    no_surv_direct=sum(1 for x in fl if x>>a==0)
    assert no_surv_direct==no_surv_expected,(a,b,s,'survival')
    # Distinct temporal orbits and their basin sizes.
    seen=set();orbit_counts=Counter()
    for x in fibers:
        if x in seen:continue
        y=x;orbit=[]
        while y not in seen:
            seen.add(y);orbit.append(y);y=f[y]
        assert y==x,(a,b,s,'cycle')
        assert len(set(fibers[z] for z in orbit))==1
        d=len(orbit);orbit_counts[d]+=1
        assert d<=L and L%d==0
    assert len(seen)==len(fibers)
    for t in range(1,L+1):
        if L%t:continue
        du=gcd(a,t);dv=gcd(b,t);delta=gcd(du,dv)
        Pt=trace_poly(du,dv,s)
        fixed_formula=sum(q*(1<<(dv//delta*k)) for k,q in enumerate(Pt))
        fixed_observed=sum(length*num for length,num in orbit_counts.items() if t%length==0)
        assert fixed_formula==fixed_observed,(a,b,s,t,fixed_formula,fixed_observed)
    return len(fibers),dict(kstats),dict(orbit_counts)

def main():
    cases=0;states=0
    for a in range(2,8):
        for b in range(1,8):
            if a+b>11:continue
            for s in range(1,a):
                k,r,c=case(a,b,s)
                cases+=1;states+=1<<(a+b)
    print('PASS all',cases,'parameter triples;',states,'initial-state checks')
    for a,b in [(4,6),(8,8),(6,6),(4,4),(5,6),(3,2)]:
        g=gcd(a,b); beta=b//g
        for s in range(1,a):
            P=trace_poly(a,b,s)
            R=sum(p*2**(beta*k) for k,p in enumerate(P))
            print('a,b,s,g',a,b,s,g,'polynomial',P,'periodic',R)

if __name__=='__main__':main()
