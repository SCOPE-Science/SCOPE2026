"""Independent exhaustive census of palindromic minimal absent factors (binary)."""
from itertools import product

def pal_maws(word):
    n=len(word)
    factors={word[i:j] for i in range(n) for j in range(i+1,n+1)}
    palcores={""}|{u for u in factors if u==u[::-1]}
    candidates={a+u+a for a in '01' for u in palcores}
    candidates|={'0','1'}
    return sorted((p for p in candidates if p not in factors and
                   (len(p)==1 or (p[:-1] in factors and p[1:] in factors))),
                  key=lambda p:(len(p),p))

def earliest_endpoint(word,p):
    if len(p)==1:return 0
    v=p[:-1]
    return word.index(v)+len(v)   # one-based inclusive position

def verify(nmax=16):
    for n in range(1,nmax+1):
        mx=0; winners=[]
        for tup in product('01',repeat=n):
            w=''.join(tup)
            ps=pal_maws(w)
            ep=[earliest_endpoint(w,p) for p in ps]
            assert len(ep)==len(set(ep)),(w,ps,ep)
            assert len(ps)<=(n if n>=2 else 2),(w,ps)
            if len(ps)>mx:mx=len(ps);winners=[w]
            elif len(ps)==mx:winners.append(w)
        assert mx==(n if n>=2 else 2),(n,mx)
        if n>=3:
            assert len(winners)==2 and set(winners)=={'0'+'1'*(n-2)+'0','1'+'0'*(n-2)+'1'},(n,winners)
        print('n',n,'max',mx,'maximizers',len(winners))
    print('EARLIEST_VERIFY_OK')

if __name__=='__main__':
    verify()
