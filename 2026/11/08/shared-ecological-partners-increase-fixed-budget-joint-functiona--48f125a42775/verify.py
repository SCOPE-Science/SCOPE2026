"""Exact checks for overlap and two-guild fixed-budget extinctions."""
from itertools import combinations
from math import comb

def C(n,k):
    return comb(n,k) if 0<=k<=n else 0

def joint_matrix(n,k,a,b,c):
    # (A, B) with fixed sizes and overlap; enumerate all k-sets
    A=set(range(a))
    B=set(range(c)) | set(range(a,a+b-c))
    counts={}
    for ss in combinations(range(n),k):
        s=set(ss); z=(len(s&A),len(s&B));counts[z]=counts.get(z,0)+1
    return counts

def increment_formula(n,k,a,b,c,r,s):
    # for threshold P(X>=r,Y>=s) when overlap goes c -> c+1
    val=0
    for h in range(c+1):
        val+=C(c,h)*C(a-c-1,r-1-h)*C(b-c-1,s-1-h)*C(n-a-b+c,k-r-s+1+h)
    return val

def tail(Z,r,s):
    return sum(v for (x,y),v in Z.items() if x>=r and y>=s)

def test():
    case_count=0; threshold_checks=0; strict_gap=0
    for n in range(2,10):
      for k in range(n+1):
        for a in range(1,n+1):
          for b in range(1,n+1):
            for c in range(max(0,a+b-n),min(a,b)):
              Z=joint_matrix(n,k,a,b,c)
              Znext=joint_matrix(n,k,a,b,c+1)
              # Check both exact hypergeometric marginals independently.
              for t in range(a+1):
                  expected=C(a,t)*C(n-a,k-t)
                  assert sum(v for (x,y),v in Z.items() if x==t)==expected
                  assert sum(v for (x,y),v in Znext.items() if x==t)==expected
              for t in range(b+1):
                  expected=C(b,t)*C(n-b,k-t)
                  assert sum(v for (x,y),v in Z.items() if y==t)==expected
                  assert sum(v for (x,y),v in Znext.items() if y==t)==expected
              # Pairwise-product is a supermodular test function.
              cross=lambda J:sum(x*y*count for (x,y),count in J.items())
              assert cross(Znext)>=cross(Z)
              for r in range(1,a+1):
                for s in range(1,b+1):
                  d=tail(Znext,r,s)-tail(Z,r,s)
                  exp=increment_formula(n,k,a,b,c,r,s)
                  assert d==exp>=0,(n,k,a,b,c,r,s,d,exp)
                  threshold_checks+=1
                  if d>0:strict_gap+=1
              case_count+=1
    print('parameters',case_count, 'threshold identities', threshold_checks, 'strict identities',strict_gap)
    n,k,a,b=7,3,3,3
    N=C(n,k)
    q=C(n-a,k)
    for c in range(4):
        cov_num=N*C(n-a-b+c,k)-q*q
        print('OR covariance c',c,':',cov_num,'/',N*N)
    assert N==35 and q==4
    assert [N*C(n-a-b+c,k)-q*q for c in range(4)]==[-16,-16,19,124]
if __name__=='__main__':test()
