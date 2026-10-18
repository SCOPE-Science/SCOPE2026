from collections import Counter

def ops(q):
    if q in (2,3,5,7):
        add=lambda a,b:(a+b)%q
        sub=lambda a,b:(a-b)%q
        mul=lambda a,b:(a*b)%q
        inv=lambda a: pow(a,-1,q)
        return add,sub,mul,inv
    if q==4:
        # GF(4)=F2[a]/(a^2+a+1), bit encoding c0+ c1*a.
        add=lambda a,b:a^b
        sub=add
        def mul(a,b):
            a0,a1=a&1,(a>>1)&1; b0,b1=b&1,(b>>1)&1
            c0=(a0*b0) ^ (a1*b1)       # a^2 = a+1
            c1=(a0*b1) ^ (a1*b0) ^ (a1*b1)
            return c0 | (c1<<1)
        def inv(a):
            assert a
            for b in range(1,4):
                if mul(a,b)==1:return b
            raise ValueError
        return add,sub,mul,inv
    raise ValueError(q)

def rank(M,q):
    add,sub,mul,inv=ops(q)
    A=[row[:] for row in M]
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]!=0),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        z=inv(A[r][c]); A[r]=[mul(z,x) for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]!=0:
                z=A[i][c]
                A[i]=[sub(A[i][j],mul(z,A[r][j])) for j in range(n)]
        r+=1
    return r

def det2(a,b,c,d,q):
    add,sub,mul,inv=ops(q)
    return sub(mul(a,d),mul(b,c))

def spectrum(q):
    add,sub,mul,inv=ops(q)
    C=Counter(); nA=0
    for a in range(q):
      for b in range(q):
       for c in range(q):
        for d in range(q):
         delta=det2(a,b,c,d,q)
         if delta==0: continue
         nA+=1
         for u in range(q):
          for v in range(q):
           M=[[sub(a,1),b,0],[c,sub(d,1),0],[u,v,sub(delta,1)]]
           C[3-rank(M,q)]+=1
    return C,nA*q*q

def formula(q):
    return {0:q**3*(q+1)*(q-2)**2,
            1:q*(2*q**4-q**3-4*q**2-q+1),
            2:(q**2-1)*(q+1),
            3:1}

for q in (2,3,4,5,7):
    C,total=spectrum(q)
    F=formula(q)
    assert {d:C.get(d,0) for d in range(4)}==F,(q,C,F)
    assert sum(C.values())==total==q**3*(q-1)**2*(q+1)
    burn=sum(C[d]*(q**d) for d in C)//total
    assert burn==3
    print(f'q={q} total={total} spectrum={dict(sorted(C.items()))} burnside_orbits={burn}')
print('VERIFY_OK')
