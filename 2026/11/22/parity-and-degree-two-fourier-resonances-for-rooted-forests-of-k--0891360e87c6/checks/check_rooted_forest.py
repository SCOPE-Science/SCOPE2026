from math import factorial
from itertools import product

def H(a,b,c,d):
    return a*a-2*a*(b+c)+2*a*d+4*a-3*(b-c)**2-6*d*(b+c)-6*(b+c)-3*d*d+3

def coeff(a,b,c,d):
    h=H(a,b,c,d)
    val=((-1)**d)*(3**a)*h
    assert val %3==0,(a,b,c,d)
    return val//3

def direct_measure(n):
    N=1<<(2*n)
    mu=[0]*N
    for mask in range(N):
        p=list(range(n+2))
        def root(u):
            while p[u]!=u:
                u=p[u]
            return u
        cyc=False
        for j in range(n):
            for i in range(2):
                if (mask>>(2*j+i))&1:
                    u=root(i);v=root(j+2)
                    if u==v:cyc=True;break
                    p[u]=v
            if cyc:break
        if cyc:continue
        comps={}
        for v in range(n+2):
            r=root(v);comps[r]=comps.get(r,0)+1
        z=1
        for k in comps.values():z*=k
        mu[mask]=z
    return mu

def fwht(a):
    a=a.copy(); size=1
    while size<len(a):
        for i in range(0,len(a),2*size):
            for j in range(i,i+size):
                u,v=a[j],a[j+size];a[j]=u+v;a[j+size]=u-v
        size*=2
    return a

if __name__=='__main__':
    count=0
    for n in range(1,6):
        actual=fwht(direct_measure(n))
        for k,z in enumerate(actual):
            a=b=c=d=0
            for j in range(n):
                typ=(k>>(2*j))&3
                if typ==0:a+=1
                elif typ==1:b+=1
                elif typ==2:c+=1
                else:d+=1
            calc=coeff(a,b,c,d)
            assert z==calc,(n,k,z,calc,(a,b,c,d))
            count+=1
        zeros=actual.count(0)
        from math import comb
        print(n,'sum',actual[0],'zeros',zeros,'rank',len(actual)-zeros,
              'pred parity',n%2==0,'min+',min(abs(x) for x in actual if x))
    print('PASSED',count,'independent FWHT coefficient equalities')
