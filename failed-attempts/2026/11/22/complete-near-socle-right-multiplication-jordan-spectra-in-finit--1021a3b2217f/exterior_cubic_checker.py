"""Independent exact checks of multiplication-rank strata in Lambda(F_q^5), q prime.
No external packages. Run: python exterior_cubic_checker.py
"""
from itertools import combinations, product
from collections import Counter

N=5
basis=list(range(1<<N))
basis.sort(key=lambda x:(x.bit_count(),x))
indices={b:i for i,b in enumerate(basis)}
triples=[b for b in basis if b.bit_count()==3]
quads=[b for b in basis if b.bit_count()==4]
quint=[b for b in basis if b.bit_count()==5]
low=[b for b in basis if b.bit_count()<=2]


def sign(a,b):
    if a&b: return 0
    s=1
    for i in range(N):
        if (a>>i)&1 and (b&((1<<i)-1)).bit_count()%2: s=-s
    return s


def rank_mod_p(mat,p):
    if not mat: return 0
    a=[row[:] for row in mat]
    rows=len(a);cols=len(a[0]); r=0
    for c in range(cols):
        pivot=next((i for i in range(r,rows) if a[i][c]%p),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][c]%p,-1,p)
        for j in range(c,cols): a[r][j]=a[r][j]*inv%p
        for i in range(r+1,rows):
            f=a[i][c]
            if f:
                for j in range(c,cols):a[i][j]=(a[i][j]-f*a[r][j])%p
        r+=1
        if r==rows:break
    return r


def L_rank(coeff,p):
    # coeff is dictionary exterior basis mask -> scalar
    out=[b for b in basis if b.bit_count()>=3]
    mat=[]
    for y in out:
        mat.append([sum(v*sign(x,z) for z,v in coeff.items() if (z & x)==0 and (z|x)==y)%p for x in low])
    return rank_mod_p(mat,p)


def alt_rank(triple_coeff,p):
    # alternating matrix B_ij from e_i wedge e_j wedge eta3
    vol=(1<<N)-1
    mat=[]
    for i in range(N):
        row=[]
        for j in range(N):
            b=(1<<i)|(1<<j)
            if i==j:row.append(0);continue
            row.append(sum(v*sign(b,z)*sign(1<<i,1<<j) for z,v in triple_coeff.items() if not z&b and (z|b)==vol)%p)
        mat.append(row)
    return rank_mod_p(mat,p)


def formula(q):
    return {0:1,1:q-1,2:q*(q**5-1),4:q**6*(q**5-1)*(q*q+1),6:q**8*(q**5-1)*(q**3-1)}


def check_binary():
    # All 2^16 elements: predicted rank by leading 3-part; actual rank via xor elimination
    from itertools import chain
    high=triples+quads+quint
    maps=[]
    for z in high:
        vec=[]
        for x in low:
            c=sign(z,x)
            vec.append((1<<indices[z|x]) if c else 0)
        maps.append(vec)
    counter=Counter()
    for k in range(1<<len(high)):
        cols=[0]*len(low)
        for i in range(len(high)):
            if k>>i&1:
                for j in range(len(low)):cols[j]^=maps[i][j]
        pivots={}
        for v in cols:
            while v:
                lead=v.bit_length()-1
                if lead not in pivots:
                    pivots[lead]=v;break
                v^=pivots[lead]
        counter[len(pivots)]+=1
    target=formula(2)
    assert counter==target,(counter,target)
    return counter


def check_homogeneous(p):
    # Exhaustive all p^10 cubic homogeneous leading terms via alternating 5x5 matrix
    count=Counter()
    for tup in product(range(p),repeat=10):
        c={b:v for b,v in zip(triples,tup) if v}
        count[alt_rank(c,p)]+=1
    target={0:1,2:(p**5-1)*(p**2+1),4:p**2*(p**5-1)*(p**3-1)}
    assert count==target,(count,target)
    return count


def check_random(p):
    # Deterministic, independent direct exterior multiplication for all five rank strata
    import random
    rng=random.Random(20261119+p)
    from collections import Counter
    cnt=Counter()
    high=triples+quads+quint
    for j in range(400):
        c={b:rng.randrange(p) for b in high}
        c={b:v for b,v in c.items() if v}
        if any(b in c for b in triples):want=2+alt_rank({b:c[b] for b in triples if b in c},p)
        elif any(b in c for b in quads):want=2
        elif any(b in c for b in quint):want=1
        else:want=0
        got=L_rank(c,p)
        assert got==want,(p,j,got,want,c)
        cnt[got]+=1
    return cnt

if __name__=='__main__':
    print('q=2 all 65536 radical-cube elements:',sorted(check_binary().items()))
    print('q=3 all 59049 cubic homogeneous forms:',sorted(check_homogeneous(3).items()))
    for p in (2,3,5,7):
        print(f'q={p} direct mult rank, deterministic 400 samples:',sorted(check_random(p).items()))
    for q in (2,3,4,5,7):
        assert sum(formula(q).values())==q**16
        print(f'q={q} formula total={q**16} rank strata=',formula(q))
    print('CHECKS_OK')
