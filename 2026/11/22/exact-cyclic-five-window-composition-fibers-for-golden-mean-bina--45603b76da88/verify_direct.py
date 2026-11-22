"""Direct cyclic-window enumeration versus the exact gap-fiber theorem."""
from collections import Counter
from math import comb, factorial


def direct(n):
    obs=Counter()
    def extend(a):
        if len(a)==n:
            if a[0]==a[-1]==1:return
            c=[0,0,0,0]
            for i in range(n):c[sum(a[(i+j)%n] for j in range(5))]+=1
            obs[(sum(a),c[2],c[3])]+=1
            return
        extend(a+[0])
        if not a or a[-1]==0:extend(a+[1])
    extend([])
    return obs


def B(w,p,t):
    if p==0:return int(t==0)
    if p==w:return int(t==w)
    k=p-t
    if k<1 or k>min(p,w-p):return 0
    x=w*comb(p-1,k-1)*comb(w-p-1,k-1)
    assert x%k==0
    return x//k


def gap_fibers(n):
    out=Counter({(0,0,0):1})
    if n>=2:out[(1,0,0)]=n
    for w in range(2,n//2+1):
        for p in range(w+1):
            for q in range(w-p+1):
                for r in range(w-p-q+1):
                    h=w-p-q-r
                    E=n-(5*w-3*p-2*q-r)
                    if E<0 or (h==0 and E!=0):continue
                    excess=comb(E+h-1,h-1) if h else 1
                    places=comb(w-p,q)*comb(w-p-q,r)*excess
                    for t in range(p+1):
                        bc=B(w,p,t)
                        if not bc:continue
                        b=3*p+2*q+r-2*t
                        numerator=n*bc*places
                        assert numerator%w==0,(n,w,p,q,r,t,numerator)
                        out[(w,b,t)]+=numerator//w
    return out


def main():
    for n in range(5,20):
        a=direct(n);b=gap_fibers(n)
        assert a==b,(n, (a-b).most_common(4),(b-a).most_common(4))
        assert sum(a.values())==sum(b.values())
        print(n, 'profiles',len(a),'labeled words',sum(a.values()),'all exact fiber multiplicities match')
    print('PASS direct vs closed gap formula')

if __name__=='__main__':main()
