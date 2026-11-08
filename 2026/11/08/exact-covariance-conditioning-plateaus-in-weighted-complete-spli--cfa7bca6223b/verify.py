"""Independent finite exact checks of weighted split graphical-zonotope vertex covariance.
Run: python3 verify.py  (Python standard library only).
"""
from itertools import permutations, product
from fractions import Fraction as F
from math import factorial


def predicted(p, q, weight):
    n = p + q
    a = (F(p*(p+1))*weight*weight + F(2*p*q)*weight
         + F(p*q*q+q*(p+2),p+1))/12
    b = F(p*(p+2),12)
    c = F((p+q)*(p+2),12)
    return a,b,c


def covariance_from_vertices(p,q,weight):
    scale=weight.denominator; a=weight.numerator
    size=p+q
    count=0
    sx=[0]*size
    sx2=[[0]*size for _ in range(size)]
    for order in permutations(range(p)):
        rank=[0]*p
        for j,i in enumerate(order): rank[i]=j+1
        for gaps in product(range(p+1),repeat=q):
            x=[a*(r-1)+scale*sum(g<r for g in gaps) for r in rank]
            x.extend(scale*g for g in gaps)
            count+=1
            for i in range(size): sx[i]+=x[i]
            for i in range(size):
                for j in range(i,size): sx2[i][j]+=x[i]*x[j]
    assert count==factorial(p)*(p+1)**q
    assert sum(sx)==count*(a*p*(p-1)//2+scale*p*q)
    C=[[F(0) for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(i,size):
            C[i][j]=C[j][i]=F(count*sx2[i][j]-sx[i]*sx[j],count*count*scale*scale)
    return C,count


def predicted_entry(p,q,a,b,c,i,j):
    n=p+q
    v_i = q if i<p else -p
    v_j = q if j<p else -p
    x=c*F(v_i*v_j,p*q*n)
    if i<p and j<p: x+=a*(F(int(i==j))-F(1,p))
    if i>=p and j>=p: x+=b*(F(int(i==j))-F(1,q))
    return x


def check_orientation_vertices(p,q,weight):
    den=weight.denominator; num=weight.numerator
    all_vectors=set()
    for perm in permutations(range(p+q)):
        where=[0]*(p+q)
        for j,i in enumerate(perm): where[i]=j
        v=[0]*(p+q)
        for i in range(p):
            for j in range(i+1,p):
                v[i if where[i]>where[j] else j]+=num
        for i in range(p):
            for j in range(p,p+q):
                v[i if where[i]>where[j] else j]+=den
        all_vectors.add(tuple(v))
    expected=factorial(p)*(p+1)**q
    assert len(all_vectors)==expected,(p,q,weight,len(all_vectors),expected)


def main():
    cases=0;entries=0;vertices=0; boundary=0; all_order_cases=0
    for p in (2,3,4):
      for q in (2,3,4):
       for weight in (F(1,5),F(1,2),F(1),F(3)):
        C,N=covariance_from_vertices(p,q,weight)
        a,b,c=predicted(p,q,weight)
        for i in range(p+q):
         for j in range(p+q):
          assert C[i][j]==predicted_entry(p,q,a,b,c,i,j),(p,q,weight,i,j,C[i][j])
          entries+=1
        assert all(sum(row)==0 for row in C)
        if p+q<=6:
            check_orientation_vertices(p,q,weight)
            all_order_cases+=1
        cases+=1; vertices+=N
    for p in range(2,151):
     for q in range(2,3*p+10):
      low_at_zero=F(p*q*q+q*(p+2),12*(p+1))
      small=F(p*(p+2),12)
      axial=F((p+q)*(p+2),12)
      assert (low_at_zero<small)==(q<=p)
      assert (low_at_zero<axial)==(q*q<(p+2)*(p+q+1))
      assert axial>small
      boundary+=1
    print(f'SPLIT_WEIGHTED_ZONOTOPE_COVARIANCE_CHECKS_PASSED cases={cases} entries={entries} sampled_vertices={vertices} phase_profiles={boundary} total_order_cases={all_order_cases}')

if __name__=='__main__': main()
