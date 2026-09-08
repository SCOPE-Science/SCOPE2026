"""S1: SL(2,3) as 2x2 det-1 matrices over F3; order + conjugacy classes."""
import itertools, json

MOD = 3
def mat(a,b,c,d): return (a%3,b%3,c%3,d%3)
def mul(X,Y):
    a,b,c,d = X; e,f,g,h = Y
    return mat(a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h)
def det(X):
    a,b,c,d = X; return (a*d-b*c) % 3
def mat_inv(X):
    a,b,c,d = X
    return mat(d, -b, -c, a)  # det=1 so inverse = adjugate

G = [mat(a,b,c,d) for a in range(3) for b in range(3)
     for c in range(3) for d in range(3) if (a*d-b*c) % 3 == 1]
assert len(G) == 24, len(G)
idx = {g:i for i,g in enumerate(G)}
ID = mat(1,0,0,1)

# closure sanity: products stay in set
for X in G:
    for Y in (G[0], G[5], G[13]):
        assert mul(X,Y) in idx

# conjugacy classes by BFS
seen = [False]*24
classes = []
for i,X in enumerate(G):
    if seen[i]: continue
    cl = set()
    for A in G:
        Ai = mat_inv(A)
        cl.add(idx[mul(mul(A,X),Ai)])
    for j in cl: seen[j] = True
    classes.append(sorted(cl))
classes.sort(key=len)
sizes = sorted(len(c) for c in classes)
print("order:", len(G))
print("nclasses:", len(classes), "sizes:", sizes, "sum:", sum(sizes))
reps = [G[c[0]] for c in classes]
def order_of(X):
    Y = X; k = 1
    while Y != ID: Y = mul(Y,X); k += 1
    return k
print("rep orders:", [order_of(r) for r in reps])
json.dump({"sizes": sizes, "nclasses": len(classes),
           "rep_orders": [order_of(r) for r in reps],
           "reps": reps},
          open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-192/output/artifacts/sl23_classes.json","w"))
print("saved sl23_classes.json")
