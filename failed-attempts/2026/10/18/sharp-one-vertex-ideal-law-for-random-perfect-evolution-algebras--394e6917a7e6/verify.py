"""Finite checks for invertible evolution-algebra support connectivity.
Use: python3 research10_simplicity_checker.py. Only enumerates small fields;
asymptotic claims are proved mathematically and not certified by this script.
"""
from itertools import product
from fractions import Fraction


def mul(a, b, q):
    if q == 4:  # F4 = F2[t]/(t^2+t+1)
        x = 0
        for i in range(2):
            for j in range(2):
                if (a >> i) & 1 and (b >> j) & 1:
                    x ^= 1 << (i + j)
        if x & 8:
            x ^= 0b1110
        if x & 4:
            x ^= 0b111
        return x
    return a*b % q


def add(a, b, q):
    return (a ^ b) if q == 4 else (a+b)%q


def inv(a, q):
    for b in range(1,q):
        if mul(a,b,q)==1:return b
    raise ValueError


def nonsingular(mat,n,q):
    m=[list(mat[i*n:(i+1)*n]) for i in range(n)]
    for i in range(n):
        piv=next((k for k in range(i,n) if m[k][i]!=0),None)
        if piv is None:return False
        m[i],m[piv]=m[piv],m[i]
        p=inv(m[i][i],q)
        m[i]=[mul(p,z,q) for z in m[i]]
        for j in range(i+1,n):
            a=m[j][i]
            if a:
                m[j]=[add(m[j][k], (mul(a,m[i][k],q) if q==4 else -mul(a,m[i][k],q)),q) for k in range(n)]
    return True


def strong(mat,n):
    def reach(transpose):
        visited={0}; todo=[0]
        for i in todo:
            for j in range(n):
                a=mat[j*n+i] if transpose else mat[i*n+j]
                if a and j not in visited:
                    visited.add(j);todo.append(j)
        return len(visited)==n
    return reach(False) and reach(True)


def has_outgoing_cut(mat,n):
    for bits in range(1,(1<<n)-1):
        if all(mat[i*n+j]==0 for i in range(n) if (bits>>i)&1 for j in range(n) if not (bits>>j)&1):
            return True
    return False


def gl_size(n,q):
    a=1
    for i in range(n):a*=q**n-q**i
    return a


def check(n,q):
    total=0; non=0; singleton_out=0; singleton_in=0
    for mat in product(range(q),repeat=n*n):
        if not nonsingular(mat,n,q):continue
        total+=1
        cut=has_outgoing_cut(mat,n)
        assert cut == (not strong(mat,n)), (n,q,mat)
        non+=cut
        singleton_out+=sum(all(mat[i*n+j]==0 for j in range(n) if j!=i) for i in range(n))
        singleton_in+=sum(all(mat[j*n+i]==0 for j in range(n) if j!=i) for i in range(n))
    assert total==gl_size(n,q),(n,q,total,gl_size(n,q))
    expected_single=Fraction(gl_size(n-1,q)*q**(n-1)*(q-1),1)
    assert singleton_out==n*expected_single,(n,q,singleton_out,n*expected_single)
    assert singleton_in==n*expected_single,(n,q,singleton_in,n*expected_single)
    print('q=%d n=%d GL=%d nonsimple=%d isolated_rows=%d isolated_cols=%d' % (q,n,total,non,singleton_out,singleton_in))


def main():
    for q,n in [(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2)]:
        check(n,q)
    print('VERIFY_OK: invertibility, directed connectivity, all-cut equivalence, exact singleton cut counts')

if __name__=='__main__':main()
