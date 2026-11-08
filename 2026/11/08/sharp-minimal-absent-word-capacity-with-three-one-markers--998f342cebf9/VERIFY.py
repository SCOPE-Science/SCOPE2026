from itertools import combinations

def formula(a,b,c,d,return_words=False):
    rect1=((a,b),(b,c),(c,d))
    def f1(p,q):return any(p<=x and q<=y for x,y in rect1)
    def rect2(h):
        out=[]
        if h==b:out.append((a,c))
        if h==c:out.append((b,d))
        return out
    def f2(h,p,q):return any(p<=x and q<=y for x,y in rect2(h))
    L=max(a,b,c); R=max(b,c,d); K=min(L,R)
    words=set()
    words.add('0'*(max(a,b,c,d)+1))
    if d>L: words.add('0'*(L+1)+'1')
    if a>R: words.add('1'+'0'*(R+1))
    for p in {a+1,b+1,c+1}:
        if not 1<=p<=L:continue
        H=max((y for x,y in rect1 if p<=x),default=-1)
        q=H+1
        if q>0 and not f1(p,q) and f1(p-1,q) and f1(p,q-1):
            words.add('0'*p+'1'+'0'*q)
    for h in range(K+1):
        if h not in (b,c):words.add('1'+'0'*h+'1')
    for h in {b,c}:
        r=rect2(h)
        lh=max(x for x,y in r);rh=max(y for x,y in r)
        if f1(lh+1,h): words.add('0'*(lh+1)+'1'+'0'*h+'1')
        if f1(h,rh+1): words.add('1'+'0'*h+'1'+'0'*(rh+1))
        for p in {x+1 for x,y in r}:
            if p<=0 or p>lh:continue
            H=max((y for x,y in r if p<=x),default=-1);q=H+1
            if q>0 and not f2(h,p,q) and f2(h,p-1,q) and f2(h,p,q-1):
                words.add('0'*p+'1'+'0'*h+'1'+'0'*q)
    for h in {b,c}:
        for k in {b,c}:
            if (h,k)!=(b,c) and f2(k,h,0) and f2(h,0,k):
                words.add('1'+'0'*h+'1'+'0'*k+'1')
    if f2(b,a+1,c):words.add('0'*(a+1)+'1'+'0'*b+'1'+'0'*c+'1')
    if f2(c,b,d+1):words.add('1'+'0'*b+'1'+'0'*c+'1'+'0'*(d+1))
    if b==c and a>=b and d>=b:words.add(('1'+'0'*b)*3+'1')
    return words if return_words else len(words)

def direct(s):
    f={s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)}|{''}
    ma={a+x+b for x in f for a in '01' for b in '01' if a+x in f and x+b in f and a+x+b not in f}
    ma|={x for x in '01' if x not in f}
    return ma

if __name__ == '__main__':
    # This test uses direct factor sets, not the rectangle characterization.
    tested = 0
    for n in range(3, 24):
        for idx in combinations(range(n), 3):
            a, b, c, d = (idx[0], idx[1]-idx[0]-1,
                          idx[2]-idx[1]-1, n-1-idx[2])
            w = '0'*a+'1'+'0'*b+'1'+'0'*c+'1'+'0'*d
            assert formula(a,b,c,d,True) == direct(w), (n,a,b,c,d)
            tested += 1
    print('CLASSIFICATION_OK', tested)

    # Finite base of the proof in RESULT.md, NOT an unbounded exhaustive search.
    cases = 0
    affine_equal_bases = []
    for aa in range(11):
      for bb in range(11-aa):
       for cc in range(11-aa-bb):
        other=(aa,bb,cc)
        M=max(other)
        for axis in range(4):
          for m in (M, M+1, M+2):
            v=list(other)
            v.insert(axis,m)
            n=sum(v)+3
            q=formula(*v)
            assert q <= n, (v,q,n)
            if n>=7 and q==n:
              assert tuple(v) in ((0,0,n-3,0),(0,n-3,0,0)), (v,q,n)
            cases += 1
          v=list(other)
          v.insert(axis,M+2)
          base=formula(*v)
          if base == sum(v)+3:
            # An affine equality can persist only with slope one.
            affine_equal_bases.append((axis,tuple(v)))
    assert sorted(affine_equal_bases)==[(1,(0,2,0,0)),(2,(0,0,2,0))], affine_equal_bases
    print('FINITE_REDUCTION_OK', cases, 'AFFINE_EQUAL_BASES',len(affine_equal_bases))
    for n in (7,8,9,20,100,1000):
        assert formula(0,0,n-3,0)==n
        assert formula(0,n-3,0,0)==n
    print('VERIFY_OK')
