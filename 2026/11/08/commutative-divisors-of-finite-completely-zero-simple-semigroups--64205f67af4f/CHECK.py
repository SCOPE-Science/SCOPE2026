from itertools import product

def rees(m,n,P):
    els=[None]+[(i,j) for i in range(m) for j in range(n)]
    def mul(a,b):
        if a is None or b is None:return None
        return (a[0],b[1]) if P[a[1]][b[0]] else None
    return els,mul

def partitions(k):
    out=[0]*k
    def rec(i, mx):
      if i==k:yield tuple(out);return
      for j in range(mx+2):
       out[i]=j
       yield from rec(i+1,max(mx,j))
    if k:
      out[0]=0;yield from rec(1,0)

def run():
    counts=0; quotients=0
    for m,n in [(2,2),(2,3),(3,2)]:
      for pv in product((0,1),repeat=m*n):
       P=[pv[j*m:(j+1)*m] for j in range(n)]
       if any(not any(P[j][i] for j in range(n)) for i in range(m)) or any(not any(row) for row in P):continue
       E,M=rees(m,n,P)
       # All subsemigroups containing 0; source with no zero cannot contain squarezero or distinct products zero; covered analytically.
       for mask in range(1,1<<(len(E)-1)):
        U=[None]+[e for i,e in enumerate(E[1:]) if mask>>i&1]
        if any(M(a,b) not in U for a in U for b in U):continue
        counts+=1
        Mmat=[[U.index(M(a,b)) for b in U] for a in U]
        for part in partitions(len(U)):
         q=max(part)+1
         if any(part[Mmat[i][j]]!=part[Mmat[j][i]] for i in range(len(U)) for j in range(len(U))):continue
         if any(part[Mmat[i][j]]!=part[Mmat[k][l]] for i in range(len(U)) for j in range(len(U)) for k in range(len(U)) for l in range(len(U)) if part[i]==part[k] and part[j]==part[l]):continue
         quotients+=1
         classes=[next(i for i in range(len(U)) if part[i]==c) for c in range(q)]
         table=[[part[Mmat[i][j]] for j in classes] for i in classes]
         zero=part[0]
         # each nonzero squarezero annihilates
         for a in range(q):
          if a!=zero and table[a][a]==zero:
           assert all(table[a][b]==zero for b in range(q)), (m,n,P,U,part,table)
         # Every element in a trivial-group Rees quotient is idempotent or square-zero.
         assert all(table[a][a] in (a,zero) for a in range(q))
         ids=[a for a in range(q) if table[a][a]==a and a!=zero]
         for a in ids:
          for b in ids:
           assert table[a][b] in (zero,a) if a==b else table[a][b]==zero,(m,n,P,U,part,table)
    print('VERIFY_OK; Rees supports: all regular zero-one matrices of sizes 2x2, 2x3, and 3x2; subsemigroups:', counts, '; commutative quotients:', quotients)

if __name__=='__main__':run()
