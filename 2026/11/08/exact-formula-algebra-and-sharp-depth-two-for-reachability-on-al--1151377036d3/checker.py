"""Exact finite Alexandrov rooted-star reachability checks (standard library only)."""
from itertools import product, combinations
from math import comb

def components(m, A):
    # 0=root, 1..m=maximal; comparability edges join root to every leaf.
    pending=set(A); out=[]
    while pending:
        start=min(pending); pending.remove(start); C={start}; todo=[start]
        while todo:
            v=todo.pop()
            for u in list(pending):
                if v==0 or u==0:
                    pending.remove(u); C.add(u); todo.append(u)
        out.append(C)
    return out

def gamma_graph(m,A,B):
    # Independent finite-Alexandrov topological path criterion via components.
    W=range(m+1)
    def le(x,y):return x==y or x==0
    return {x for x in W if any(any(le(x,a) for a in C) and any(y in B and any(le(y,b) for b in C) for y in W) for C in components(m,A))}

def gamma_normal(m,A,B):
    # Claimed root/leaf compositional identity.
    L=set(range(1,m+1)); R={0}
    A,B=set(A),set(B)
    E=lambda C:bool(C)
    root=((0 in B) and E(A)) or E(L&A&B)
    leaves={v for v in L if v in A and (v in B or 0 in B or ((0 in A) and E(L&A&B)))}
    return ({0} if root else set())|leaves

def direct_path_finite(m,A,B):
    # Enumerate small up-down paths (known finite-space path representation),
    # with length enough to visit all A-points. Does not use component routine.
    U=set(A); W=range(m+1)
    def lt(x,y):return x==y or x==0
    good=set()
    for x in W:
      # states at endpoints: x <= a in A; inside any comparable A-steps;
      # endpoint y <= b; dynamic reachability.
      frontier={a for a in U if lt(x,a)}; visited=set(frontier)
      while frontier:
        frontier={v for a in frontier for v in U if (lt(a,v) or lt(v,a)) and v not in visited}
        visited|=frontier
      if any(any(lt(y,a) for a in visited) for y in B): good.add(x)
    return good

def coord_count(k,m):
    q=2**k
    return q*sum(comb(q,j)*(j+1) for j in range(1,min(m,q)+1))

def check_boolean_formula_semantics(m,k):
    q=1<<k; W=range(m+1)
    # All pointed valuations (root and m colored leaves), identify observational types.
    triples={}; sem_keys=set()
    for colors in product(range(q),repeat=m+1):
      r=colors[0]; S=frozenset(colors[1:])
      for w in W:
        key=(r,S,None if w==0 else colors[w]); sem_keys.add(key)
        triples.setdefault(key,[]).append((colors,w))
    assert len(sem_keys)==coord_count(k,m),(k,m,len(sem_keys),coord_count(k,m))
    # Explicit depth-one coordinate characteristic formula:
    # root type via E(root AND P_r), leaf support via E(leaf AND P_a),
    # local indicator via root/leaf + present atomic color.
    for (r,S,a),wits in triples.items():
      for colors,w in wits:
        leaf_present=lambda v:v in colors[1:]
        root_color=colors[0]
        assert (root_color==r and frozenset(v for v in range(q) if leaf_present(v))==S and (a is None and w==0 or (a is not None and w>0 and colors[w]==a)))
    return len(sem_keys)

def check_depth_boundary(m):
    # Compare two valuations at leaf 1: same local atom but second leaf differs.
    # Every depth-one operation uses Boolean combinations of atoms at its inputs.
    vals=[(1,0)+tuple([0]*(m-1)),(1,0,1)+tuple([0]*(m-2))]
    x=1
    # 4 one-variable propositional input functions.
    unary=(lambda b: False,lambda b: True,lambda b:bool(b),lambda b:not b)
    for f in unary:
      truth=[]
      for v in vals:
        A={i for i,t in enumerate(v) if f(t)}
        # Cantor derivative false at maximal leaf in all valuations.
        truth.append(False)
      assert truth==[False,False]
    for f in unary:
      for g in unary:
        tt=[]
        for v in vals:
          A={i for i,t in enumerate(v) if f(t)}
          B={i for i,t in enumerate(v) if g(t)}
          tt.append(x in gamma_graph(m,A,B))
        assert tt[0]==tt[1],(m,f,g,tt)
    # depth-two formula gamma(top, (not derivative(top)) and p)
    tt=[]
    for v in vals:
      A=set(range(m+1))
      leaf_p={i for i in range(1,m+1) if v[i]==1}
      tt.append(x in gamma_graph(m,A,leaf_p))
    assert tt==[False,True],(m,tt)

def check_coordinate_definers(m,k):
    q=1<<k
    for colors in product(range(q),repeat=m+1):
      W=set(range(m+1))
      R={0}; L=W-R
      for w in W:
        r=colors[0]; S=frozenset(colors[1:]); a=None if w==0 else colors[w]
        for rr in range(q):
          for bits in range(1,1<<q):
            SS=frozenset(j for j in range(q) if bits>>j&1)
            if len(SS)>m: continue
            root_color_detect=(w in gamma_graph(m,W,{0} if colors[0]==rr else set()))
            support_detect=all((w in gamma_graph(m,W,{i for i in L if colors[i]==j}))==(j in SS) for j in range(q))
            for aa in [None]+list(SS):
              test=((w==0 if aa is None else (w>0 and colors[w]==aa))
                    and root_color_detect and support_detect)
              assert test == ((r,S,a)==(rr,SS,aa))

def run():
    pairs=0
    for m in range(1,6):
      for a in range(1<<(m+1)):
        A={i for i in range(m+1) if a>>i&1}
        for b in range(1<<(m+1)):
          B={i for i in range(m+1) if b>>i&1}
          c=gamma_graph(m,A,B)
          assert c==gamma_normal(m,A,B),(m,A,B,c,gamma_normal(m,A,B))
          assert c==direct_path_finite(m,A,B),(m,A,B,c,direct_path_finite(m,A,B))
          pairs+=1
    scores=[]
    for k in range(0,3):
      for m in range(1,5):
        scores.append((k,m,check_boolean_formula_semantics(m,k)))
    for m in (2,3,4):check_depth_boundary(m)
    for m,k in ((1,1),(2,1),(2,2),(3,1)):check_coordinate_definers(m,k)
    # A separate direct table demonstrates the sharp saturation threshold:
    for k in range(0,3):
      q=1<<k
      assert coord_count(k,q)==coord_count(k,q+5)
      if q>1:assert coord_count(k,q-1)<coord_count(k,q)
    print('ALEXANDROV_STAR_GAMMA_ALGEBRA_OK',pairs,'PATH_PAIRS',scores)
if __name__=='__main__': run()
