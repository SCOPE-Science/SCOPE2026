"""S5: closure/inverses/quaternion fingerprint of SL(2,3) matrix model + Q8:C3."""
import json
ART="/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-192/output/artifacts/"
def mat(a,b,c,d): return (a%3,b%3,c%3,d%3)
def mul(X,Y):
    a,b,c,d=X; e,f,g,h=Y
    return mat(a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
def mat_inv(X):
    a,b,c,d=X; return mat(d,-b,-c,a)
G=[mat(a,b,c,d) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if (a*d-b*c)%3==1]
S=set(G); idx={g:i for i,g in enumerate(G)}
ID=mat(1,0,0,1)
n=0
for X in G:
    for Y in G:
        assert mul(X,Y) in S; n+=1
    assert mul(X,mat_inv(X))==ID and mul(mat_inv(X),X)==ID
print("closure+inverses checked over",n,"products; |G|=24; identity unique:",G.count(ID)==1)
def order_of(X):
    Y=X;k=1
    while Y!=ID: Y=mul(Y,X);k+=1
    return k
def pw(X,m):
    R=ID
    for _ in range(m): R=mul(R,X)
    return R
Q8=[g for g in G if pw(g,4)==ID]
from collections import Counter
print("Q8 orders:",Counter(order_of(g) for g in Q8))
# Q8 centre: single element order 2 (=-I)
z=[g for g in Q8 if order_of(g)==2]
print("Q8 centre element:",z)
# Q8 cap <t> for t order 3/6: trivial
o3=[g for g in G if order_of(g) in (3,6)]
t6=[g for g in o3 if order_of(g)==6][0]
C=[ID]; Y=t6
while Y!=ID: C.append(Y); Y=mul(Y,t6)
print("|<t>|:",len(C),"cap Q8:",len(set(C)&set(Q8)))
# action nontrivial: conjugate of an order-4 element leaves Q8 (already) and is not identity on Q8
q4=[g for g in Q8 if order_of(g)==4][0]
print("t q t^-1 =",mul(mul(t6,q4),mat_inv(t6))," vs q =",q4)
json.dump({"closure_products":n,"Q8_order_dist":{str(k):v for k,v in Counter(order_of(g) for g in Q8).items()},
           "centre_minusI":z[0],"elt_order6":t6,"cap_size":len(set(C)&set(Q8))},
          open(ART+"sl23_struct.json","w"))
print("saved sl23_struct.json")
