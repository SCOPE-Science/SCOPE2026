"""Reproducible finite checks for the exact finite full-product collapse criterion.
Run with Python 3, no external packages.
"""
from itertools import product


def antichains_nonempty(n):
    sets=tuple(range(1,1<<n))
    out=[]
    for mask in range(1,1<<len(sets)):
        a=tuple(sets[i] for i in range(len(sets)) if mask>>i&1)
        if all(not (u & v==u or u & v==v) for i,u in enumerate(a) for v in a[i+1:]):
            out.append(a)
    return out


def is_S(a):
    return all(u.bit_count()==1 for u in a)

def is_P(a):
    return len(a)==1

def predict(a,b):
    return is_S(a) or is_P(b)

def exists_rec(p, a, b, m, n):
    for u in a:
        for v in b:
            if all((p>>(i*n+j))&1 for i in range(m) if (u>>i)&1 for j in range(n) if (v>>j)&1):
                return True
    return False

def exists_seq(p, a, b, m, n):
    # horizontal after vertical
    return any(all(any(all((p>>(i*n+j))&1 for j in range(n) if (v>>j)&1) for v in b)
                   for i in range(m) if (u>>i)&1) for u in a)

def exists_rev(p, a, b, m, n):
    return any(all(any(all((p>>(i*n+j))&1 for i in range(m) if (u>>i)&1) for u in a)
                   for j in range(n) if (v>>j)&1) for v in b)


def main():
    M={1:3, 2:6, 3:20}
    for m in range(1,4):
      aa=antichains_nonempty(m)
      assert len(aa)==M[m]-2
      for n in range(1,4):
        bb=antichains_nonempty(n)
        eo=0; jo=0
        for a,b in product(aa,bb):
          e=predict(a,b)
          f=predict(b,a)
          eo+=e
          jo+=e and f
          for p in range(1<<(m*n)):
            rect=exists_rec(p,a,b,m,n)
            hv=exists_seq(p,a,b,m,n)
            vh=exists_rev(p,a,b,m,n)
            assert not rect or (hv and vh)
            assert not(hv and not rect) or not e, (m,n,a,b,p,'horizontal')
            assert not(vh and not rect) or not f, (m,n,a,b,p,'vertical')
            if not e and hv and not rect: pass
          # converse failure witness can be constructed for all !e, verify one exists
          if not e:
            assert any(exists_seq(p,a,b,m,n) and not exists_rec(p,a,b,m,n) for p in range(1<<(m*n)))
          if not f:
            assert any(exists_rev(p,a,b,m,n) and not exists_rec(p,a,b,m,n) for p in range(1<<(m*n)))
        Tm,Tn=M[m]-2,M[n]-2
        Sm,Sn=(1<<m)-1,(1<<n)-1
        expected=Sm*Tn+(Tm-Sm)*Sn
        d=Tm - 2*Sm+m
        expected_both=m*Tn+2*(Sm-m)*Sn+d*n
        assert eo==expected and jo==expected_both, (m,n,eo,expected,jo,expected_both)
        print('pair',m,n,'all',Tm*Tn,'horizontal_eq',eo,'both_eq',jo)
    # T-axiom (point-containing) counts at the distinguished pair (0,0)
    for m in range(1,4):
      for n in range(1,4):
        aa=[a for a in antichains_nonempty(m) if all(u&1 for u in a)]
        bb=[b for b in antichains_nonempty(n) if all(v&1 for v in b)]
        actual=sum(predict(a,b) for a,b in product(aa,bb))
        expected=(M[n-1]-1 if n>1 else 1) + ((M[m-1]-2 if m>1 else 0)*(1<<(n-1)))
        assert actual==expected
        print('Tpair',m,n,'all',len(aa)*len(bb),'horizontal_eq',actual)
    # fully global oriented identity count, small frame orders
    for m,n in [(1,1),(1,2),(2,1),(2,2)]:
      aa=antichains_nonempty(m);bb=antichains_nonempty(n)
      actual=sum(all(predict(a,b) for a in f for b in g)
                 for f in product(aa,repeat=m) for g in product(bb,repeat=n))
      Sm,Sn=(1<<m)-1,(1<<n)-1
      Tm,Tn=len(aa),len(bb)
      expect=Sm**m*Tn**n+Tm**m*Sn**n-Sm**m*Sn**n
      assert actual==expect
      print('global',m,n,'all',Tm**m*Tn**n,'oriented_eq',actual)
    print('ALL_CHECKS_OK')

if __name__=='__main__':main()
