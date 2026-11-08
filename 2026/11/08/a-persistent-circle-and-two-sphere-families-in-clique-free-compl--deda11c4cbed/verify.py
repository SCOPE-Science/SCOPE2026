#!/usr/bin/env python3
"""Exact finite-chain and equivariant Lefschetz checks for clique-free edge books."""
from math import comb

def faces(q,k):
    m=q-2;n=2+m*k
    f=[[] for _ in range(n+1)]
    for a in range(1<<n):
        c=(a&3).bit_count()
        if all(((a>>(2+i*m))&((1<<m)-1)).bit_count()+c<=2 for i in range(k)):
            f[a.bit_count()].append(a)
    return f

def rank(fsrc,ftgt,p):
    rows={x:i for i,x in enumerate(ftgt)};base={}
    for x in fsrc:
        pos=[i for i in range(x.bit_length()) if x>>i&1]
        vec={rows[x^(1<<i)]:(1 if j%2==0 else p-1) for j,i in enumerate(pos)}
        while vec:
            lead=max(vec)
            if lead not in base:
                c=pow(vec[lead],-1,p)
                base[lead]={u:v*c%p for u,v in vec.items()}
                break
            c=vec[lead]
            for u,v in base[lead].items():
                z=(vec.get(u,0)-c*v)%p
                if z:vec[u]=z
                elif u in vec:del vec[u]
    return len(base)

def betti(q,k,p):
    ff=faces(q,k);r=[1]
    for s in range(2,len(ff)):
        if not ff[s]:break
        r.append(rank(ff[s],ff[s-1],p))
    r.append(0)
    return {j:x for j in range(len(r)-1) if (x:=len(ff[j+1])-r[j]-r[j+1])}

def predicted(q,k):
    m=q-2
    return {1:1,k:2*(m-1)**k,**({2*k-1:comb(m-1,2)**k} if m>=3 else {})}

def action(q,k,what):
    m=q-2;p=list(range(2+k*m))
    if what=='core':p[0],p[1]=p[1],p[0]
    if what=='inner':p[2],p[3]=p[3],p[2]
    if what=='pages':
        for i in range(m):p[2+i],p[2+m+i]=p[2+m+i],p[2+i]
    return p

def permute(a,p):return sum(1<<p[i] for i in range(len(p)) if a>>i&1)

def orientation(a,p):
    z=[p[i] for i in range(len(p)) if a>>i&1]
    return -1 if sum(x>y for j,x in enumerate(z) for y in z[j+1:])%2 else 1

def lefschetz(q,k,p):
    s=-1
    for d,fs in enumerate(faces(q,k)[1:],1):
        s+= (1 if d%2 else -1)*sum(orientation(a,p) for a in fs if permute(a,p)==a)
    return s

def predicted_trace(q,k,what):
    m=q-2;h=comb(m-1,2) if m>=3 else 0
    if what=='core':
        tr1=-1; low=0; high=h**k
    elif what=='inner':
        tr1=1;low=2*(m-3)*(m-1)**(k-1)
        high=((comb(m-2,2) if m>=4 else 0)-(m-2))*h**(k-1)
    else:
        tr1=1;low=-2*(m-1)**(k-1);high=h**(k-1)
    return -tr1 + (-1 if k%2 else 1)*low-high

def main():
    cases=0;fields=0;chars=0
    for q in range(4,8):
        for k in range(2,5):
            if 2+k*(q-2)>13:continue
            for p in (2,3):
                a=betti(q,k,p); b=predicted(q,k)
                assert a==b,(q,k,p,a,b)
                fields+=1
            for kind in ('core','inner','pages'):
                a=lefschetz(q,k,action(q,k,kind));b=predicted_trace(q,k,kind)
                assert a==b,(q,k,kind,a,b)
                chars+=1
            cases+=1
    print(f'ALL_VERIFY_OK cases={cases} modular_betti={fields} signed_lefschetz={chars} K4_two_pages={predicted(4,2)} K5_two_pages={predicted(5,2)}')
if __name__=='__main__':main()
