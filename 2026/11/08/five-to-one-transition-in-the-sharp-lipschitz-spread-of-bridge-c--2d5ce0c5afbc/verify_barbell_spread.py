"""Exact checks for sharp variance on bridge-connected cliques.
Only the finite checks are experimental; the accompanying proof is universal.
"""
from itertools import product

def numerator(vals):
    N=len(vals)
    return N*sum(x*x for x in vals)-sum(vals)**2

def formula(m,n):
    H,L=max(m,n),min(m,n)
    C=max(0,H-5*L)
    return 9*m*n-4*(m+n)+(C*C)//4

def profiles(m,n):
    # vertex profiles for K_m (root 0) and K_n (root 1)
    # count all labellings; 0,±1 are potentials for clique on the left;
    # 1,0/2 on right. Redundant all-root assignments are harmless.
    left=[]
    for k in range(m):
        for sg in (-1,1):
            for subset in product((0,1),repeat=m-1):
                if sum(subset)==k:
                    left.append((0,)+tuple(sg*x for x in subset))
    right=[]
    for k in range(n):
        for sg in (-1,1):
            for subset in product((0,1),repeat=n-1):
                if sum(subset)==k:
                    right.append((1,)+tuple(1+sg*x for x in subset))
    return list(set(left)),list(set(right))

def check_direct():
    tests=0; profiles_count=0
    for m in range(2,8):
      for n in range(2,8):
        A,B=profiles(m,n)
        scores=[numerator(a+b) for a,b in product(A,B)]
        max_score=max(scores)
        assert max_score==formula(m,n), (m,n,max_score,formula(m,n))
        tests+=1;profiles_count+=len(scores)
    print('DIRECT_ALL_EXTREME_CLIQUE_POTENTIALS_OK',tests,profiles_count)

def check_integer_potentials():
    # independent labelled enumerator of every integral 1-Lipschitz function
    # after anchoring the left bridge endpoint at zero; includes both bridge signs.
    examined=0; pairs=0
    for m in range(2,7):
      for n in range(2,7):
        best=-1
        for b in (-1,0,1):
          for a_vals in product((-1,0,1),repeat=m-1):
            A=(0,)+a_vals
            if max(A)-min(A)>1: continue
            for b_vals in product((b-1,b,b+1),repeat=n-1):
              B=(b,)+b_vals
              if max(B)-min(B)>1: continue
              examined+=1
              best=max(best,numerator(A+B))
        assert best==formula(m,n),(m,n,best,formula(m,n))
        pairs+=1
    print('INDEPENDENT_LABELLED_INTEGER_LIPSCHITZ_ENUMERATION_OK',pairs,examined)

def check_reduced():
    tests=0
    for m in range(2,130):
      for n in range(2,130):
        N=m+n
        best=-1
        for k in range(m):
          # optimized over l by floor quadratic continuous vertex, plus boundaries
          opt=(3*m+n+2*k)//2 # integer floor of the unconstrained optimum
          assert 2*opt <= 3*N-2*n+2*k < 2*opt+2
          ls={0,n-1,opt,opt+1}
          for l in ls:
            if 0<=l<n:
              s=n-k+l; q=n+k+3*l
              best=max(best,N*q-s*s)
        assert best==formula(m,n), (m,n,best,formula(m,n))
        tests+=1
    print('EXACT_REDUCED_INTEGER_OPTIMA_OK',tests)

def check_phase():
    tests=0
    for L in range(2,100):
      for H in range(L,10*L+20):
        N=L+H
        k=L-1
        fs=[]
        for d in range(H):
          l=H-1-d
          s=H-k+l;q=H+k+3*l
          fs.append(N*q-s*s)
        c=max(0,H-5*L)
        best=max(fs)
        ds=[d for d,x in enumerate(fs) if x==best]
        target=[0] if c==0 else ([c//2] if c%2==0 else [c//2, c//2+1])
        assert ds==target,(L,H,c,ds,target)
        assert best==formula(L,H)
        tests+=1
    print('FIVE_TO_ONE_PHASE_AND_ALL_TIES_OK',tests)

def check_fixed_size_balance():
    tests=0
    for N in range(4,300):
        vv=[formula(L,N-L) for L in range(2,N//2+1)]
        assert all(vv[i+1]>vv[i] for i in range(len(vv)-1)),(N,vv)
        tests+=1
    print('STRICT_FIXED_ORDER_BALANCING_OK',tests)

if __name__=='__main__':
    check_direct();check_integer_potentials();check_reduced();check_phase();check_fixed_size_balance()
    print('ALL_BRIDGE_BARBELL_SPREAD_TESTS_OK')
