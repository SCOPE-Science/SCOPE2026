"""Exact integer checks for signed perfect-matching sums on Möbius ladders."""
from collections import Counter


def transfer_fast(signs):
    a,b,c,d = 1,0,0,1
    for r in signs:
        a,b,c,d = a*r+b,a,c*r+d,c
    return a,b,c,d


def masks(n):
    N=2*n
    E=[(i,(i+1)%N) for i in range(N)]+[(i,i+n) for i in range(n)]
    adj=[[] for _ in range(N)]
    for e,(i,j) in enumerate(E):
        adj[i].append((j,e));adj[j].append((i,e))
    out=[]
    def rec(used,mask):
        if used==(1<<N)-1:
            out.append(mask); return
        i=next(k for k in range(N) if not((used>>k)&1))
        for j,e in adj[i]:
            if not((used>>j)&1):
                weight = (1<<n) if e==N-1 else (1<<(e-N)) if e>=N else 0
                rec(used|(1<<i)|(1<<j),mask^weight)
    rec(0,0)
    return out


def hadamard(a):
    a=a.copy();h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h];a[j]=u+v;a[j+h]=u-v
        h*=2
    return a


def signed_formula(n,index):
    signs=[-1 if (index>>k)&1 else 1 for k in range(n)]
    h=-1 if (index>>n)&1 else 1
    a,b,c,d=transfer_fast(signs)
    assert a*d-b*c==(-1)**n
    return a+h*d+(1+h)*(n%2)


def run():
    assertions=0
    for n in range(3,13):
        own=masks(n)
        a=[0]*(1<<(n+1))
        for m in own: a[m]+=1
        coeff=hadamard(a)
        assert all(coefficient==signed_formula(n,f) for f,coefficient in enumerate(coeff))
        assertions+=len(coeff)
        zeros=sum(v==0 for v in coeff)
        gap=min(abs(v) for v in coeff if v)
        assert (zeros>0)==(n%6==0)
        assert gap==(1 if n%3 else 2)
        assert sum(a)==len(own)
        if n==6: assert zeros==36
        if n==12: assert zeros==1392
        print('n=%d matchings=%d zero_reduced=%d smallest_nonzero=%d' %
              (n,len(own),zeros,gap))
        assertions+=5
    seeds={3:('+++',-1,2),4:('+++-',1,1),5:('++-+-',1,1),
           6:('+++++-',1,2),7:('++++--+',-1,1),8:('+++++--+',-1,1)}
    identity_blocks=['++-++-','+-++-+','+-+-+-','+--+--',
                     '-++-++','-+-+-+','-+--+-','--+--+']
    for word in identity_blocks:
        a,b,c,d=transfer_fast([1 if x=='+' else -1 for x in word])
        assert b==c==0 and a==d and abs(a)==1
        assertions+=1
    for n in range(3,207):
        seed=3+(n-3)%6
        word,h,target=seeds[seed]
        signs=word+identity_blocks[0]*((n-seed)//6)
        j=sum(1<<k for k,x in enumerate(signs) if x=='-')
        if h==-1:j|=1<<n
        assert signed_formula(n,j) in (target,-target)
        assertions+=1
        if n%6==0:
            a,b,c,d=transfer_fast([1 if x=='+' else -1 for x in identity_blocks[0]*(n//6)])
            assert a==d and b==c==0
            assertions+=1
    print('MOBIUS_WALSH_EXACT_TESTS_PASS',assertions)

if __name__=='__main__':
    run()
