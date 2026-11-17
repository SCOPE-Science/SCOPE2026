"""Independently enumerate labelled binary majority states on matching-deleted cliques."""
from math import comb


def expected(r,u):
    n=2*r+u
    if u==0:
        return (2+(1<<r),(comb(n,n//2)-(1<<r))//2)
    if u%2==0:
        return (2,comb(n,n//2)//2)
    if u==1:
        return (2,comb(r,r//2))
    h=(n-1)//2
    return (2,comb(r,(h+1)//2) if (h%2==1 and h+1<=2*r) else 0)


def step(x,r,u):
    n=2*r+u
    total=x.bit_count()
    out=0
    for i in range(n):
        own=(x>>i)&1
        mate=((x>>(i^1))&1) if i<2*r else 0
        degree=n-2 if i<2*r else n-1
        near=total-own-mate
        bit=1 if 2*near>degree else 0 if 2*near<degree else own
        out|=bit<<i
    return out


def test(r,u):
    n=2*r+u; states=1<<n
    fixed=0; two_states=0; maxentry=0
    for x in range(states):
        seq=[x]
        for _ in range(4):seq.append(step(seq[-1],r,u))
        if seq[1]==x:fixed+=1
        elif seq[2]==x:two_states+=1
        if seq[2]!=seq[4]:
            assert seq[3]==step(seq[4],r,u), (r,u,x,'not eventually periodic')
        assert seq[3]==step(seq[4],r,u) and (seq[3]==seq[1] if not u%2 else True), (r,u,x)
    target=expected(r,u)
    assert (fixed,two_states//2)==target,(r,u,fixed,two_states//2,target)
    assert two_states%2==0
    return fixed,two_states//2


def main():
    runs=0; enumerated=0
    for u in range(0,8):
        for r in range(1,9):
            n=2*r+u
            if n>15: continue
            a,b=test(r,u)
            runs+=1; enumerated+=1<<n
            print(f"r={r} u={u} fixed={a} primitive_2_cycles={b}")
    print(f"PASS: {runs} families, {enumerated} labelled configurations, universal return identities checked")

if __name__=='__main__':main()
