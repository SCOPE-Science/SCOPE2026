"""Exhaustive check of the local survival obstruction and sharp witness families."""
from itertools import product

def step(x,q):
    n=len(x)
    return tuple((v+1)%q if v else int(x[(i-1)%n]==1) for i,v in enumerate(x))

def survivor_set(x,q):
    n=len(x)
    return {i for i in range(n) if x[i]==1 and all(
        not (x[(i+d)%n]==1 or (x[(i+d)%n]>=2 and x[(i+d)%n]+d<=q))
        for d in range(1,q))}

def wave_from_survivors(s,n,q,t):
    y=[0]*n
    for i in s:
        for a in range(1,q):
            y[(i+t-(a-1))%n]=a
    return tuple(y)

def main():
    tested=0
    for q in range(4,8):
        for n in range(3,7):
            if q**n>140000:continue
            for x in product(range(q),repeat=n):
                s=survivor_set(x,q)
                y=x
                for _ in range(q+min(n,q-1)-2):y=step(y,q)
                assert y==wave_from_survivors(s,n,q,q+min(n,q-1)-2),(q,n,x,y,s)
                tested+=1
    print('PASS exact surviving-pulse reconstruction:',tested)
    for q in range(4,11):
        for n in [3,q-1,q,q+1,2*q]:
            x=[0]*n
            if n<q:x[-1]=1
            else:x[0]=x[q-1]=1
            y=tuple(x)
            T=q+min(n,q-1)-2
            for _ in range(T-1): y=step(y,q)
            z=y
            y=step(y,q)
            assert z!=wave_from_survivors(survivor_set(x,q),n,q,T-1)
            assert y==wave_from_survivors(survivor_set(x,q),n,q,T)
    print('PASS all sharp witness families')
if __name__=='__main__':main()
