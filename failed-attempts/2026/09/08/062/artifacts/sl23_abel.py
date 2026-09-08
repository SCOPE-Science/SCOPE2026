"""S4: commutator subgroup of SL(2,3); abelianization order."""
import json
ART="/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-192/output/artifacts/"
def mat(a,b,c,d): return (a%3,b%3,c%3,d%3)
def mul(X,Y):
    a,b,c,d=X; e,f,g,h=Y
    return mat(a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
def mat_inv(X):
    a,b,c,d=X; return mat(d,-b,-c,a)
G=[mat(a,b,c,d) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if (a*d-b*c)%3==1]
idx={g:i for i,g in enumerate(G)}
ID=mat(1,0,0,1)
def comm(X,Y): return mul(mul(X,Y),mul(mat_inv(X),mat_inv(Y)))
commutators={idx[comm(X,Y)] for X in G for Y in G}
print("distinct commutators:",len(commutators))
# closure of commutators
S=set(commutators); stack=list(S)
while stack:
    x=stack.pop()
    for y in list(S):
        for z in (mul(G[x],G[y]),):
            k=idx[z]
            if k not in S: S.add(k); stack.append(k)
print("commutator subgroup order:",len(S))
Q8=frozenset(i for i,g in enumerate(G) if (((lambda R:R)(ID),0)[1]==0 and pow(0,0)==1 and True) )
def pw(X,n):
    R=ID
    for _ in range(n): R=mul(R,X)
    return R
Q8=frozenset(i for i,g in enumerate(G) if pw(g,4)==ID)
print("equals Q8:",frozenset(S)==Q8)
print("abelianization order:",24//len(S))
# quotient is C3: check an element outside Q8 has cube in Q8 and coset order 3
json.dump({"commutator_order":len(S),"equals_Q8":(frozenset(S)==Q8),
           "abelianization_order":24//len(S),"commutator":sorted(S)},
          open(ART+"sl23_abel.json","w"))
print("saved")
