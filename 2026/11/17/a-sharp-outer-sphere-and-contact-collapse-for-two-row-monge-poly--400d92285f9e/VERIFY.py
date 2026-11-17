"""Exact finite checks for enclosing spheres of two-row normalized Monge polytopes."""
from fractions import Fraction as F
from itertools import combinations


def vectors(q):
    out = {}
    for k in range(1, q + 1):
        x = [F(0)] * (2*q)
        for j in range(q-k, q):
            x[j] = F(1,k)
        out['A'+str(k)] = tuple(x)
        x = [F(0)] * (2*q)
        for j in range(k):
            x[q+j] = F(1,k)
        out['B'+str(k)] = tuple(x)
    for j in range(q):
        x = [F(0)] * (2*q)
        x[j] = x[q+j] = F(1,2)
        out['C'+str(j+1)] = tuple(x)
    return out


def center(q):
    b = F(1,4*(q-1))
    c = [F(0)]*(2*q)
    c[q-1] = c[q] = q*b
    for j in range(1,q-1):
        c[j] = c[q+j] = b
    return tuple(c)


def norm2(x):
    return sum(a*a for a in x)


def dist2(x,y):
    return norm2(tuple(a-b for a,b in zip(x,y)))


def exact_circumball_checks():
    count=0
    for q in range(2,33):
        vs=vectors(q);c=center(q);r2=F(5*q-6,8*(q-1))
        alpha=F(q,4*(q-1));beta=F(1,2*(q-1))
        w={'A1':alpha,'B1':alpha}
        for j in range(2,q):w['C'+str(j)]=beta
        assert sum(w.values())==1
        assert all(sum(w.get(name,F(0))*v[i] for name,v in vs.items())==c[i] for i in range(2*q))
        count+=2*q+1
        contacts=set()
        for name,v in vs.items():
            d=dist2(v,c)
            assert d<=r2,(q,name,d,r2)
            if d==r2:contacts.add(name)
            if name[0] in 'AB':
                k=int(name[1:])
                expected=F(k-1,2*k) if k<q else F(q-2,2*(q-1))
                assert r2-d==expected,(q,name,r2-d,expected)
            else:
                j=int(name[1:])
                expected=F(q-2,4*(q-1)) if j in (1,q) else F(0)
                assert r2-d==expected,(q,name,r2-d,expected)
            count+=3
        predicted= set(vs) if q==2 else {'A1','B1'}|{'C'+str(j) for j in range(2,q)}
        assert contacts==predicted,(q,contacts,predicted)
        assert norm2(c)==F(q+2,8*(q-1))
        count+=2
    return count


def solve_unique(A,b):
    n=len(b)
    m=[list(map(F, row))+[F(bb)] for row,bb in zip(A,b)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if m[i][j]),None)
        if pivot is None:return None
        m[j],m[pivot]=m[pivot],m[j]
        d=m[j][j]
        m[j]=[x/d for x in m[j]]
        for i in range(n):
            if i!=j:
                a=m[i][j]
                if a:m[i]=[x-a*y for x,y in zip(m[i],m[j])]
    return tuple(row[-1] for row in m)


def enumerate_vertices(q):
    n=2*q
    ineq=[]
    for i in range(n):
        row=[0]*n;row[i]=1;ineq.append(row)
    for j in range(q-1):
        row=[0]*n
        row[j]=-1;row[j+1]=1
        row[q+j]=1;row[q+j+1]=-1
        ineq.append(row)
    exact=set()
    count=0
    for inds in combinations(range(len(ineq)),n-1):
        val=solve_unique([[1]*n]+[ineq[i] for i in inds],[1]+[0]*(n-1))
        count+=1
        if val is not None and all(sum(a*b for a,b in zip(row,val))>=0 for row in ineq):
            exact.add(val)
    assert exact==set(vectors(q).values()),(q,len(exact),len(vectors(q)))
    return count


def main():
    checks=exact_circumball_checks()
    for q in (2,3,4):
        checks+=enumerate_vertices(q)
    print('PASS: exact equalities, inequalities, center certificates, and complete vertex enumerations; checks:',checks)

if __name__=='__main__':main()
