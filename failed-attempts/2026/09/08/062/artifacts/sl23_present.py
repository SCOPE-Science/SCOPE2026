"""S6: find Q8 gens + C3 elt with cyclic action; verify presentation relations."""
ART="/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-192/output/artifacts/"
def mat(a,b,c,d): return (a%3,b%3,c%3,d%3)
def mul(X,Y):
    a,b,c,d=X; e,f,g,h=Y
    return mat(a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
def inv(X):
    a,b,c,d=X; return mat(d,-b,-c,a)
G=[mat(a,b,c,d) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if (a*d-b*c)%3==1]
idx={g:i for i,g in enumerate(G)}
ID=mat(1,0,0,1); MI=mat(2,0,0,2)
def pw(X,m):
    R=ID
    for _ in range(m): R=mul(R,X)
    return R
def order_of(X):
    Y=X;k=1
    while Y!=ID: Y=mul(Y,X);k+=1
    return k
Q8=[g for g in G if pw(g,4)==ID]
o4=[g for g in Q8 if order_of(g)==4]
C3=[g for g in G if order_of(g)==3]
print(len(o4),len(C3))
# pick x,y in Q8 with yx != xy, x^2=y^2=-I, y^{-1}xy=x^{-1}
found=None
for x in o4:
    for y in o4:
        if mul(y,x)==mul(x,y): continue
        if not (pw(x,2)==MI and pw(y,2)==MI): continue
        if mul(mul(inv(y),x),y)==inv(x):
            found=(x,y); break
    if found: break
x,y=found
print("x=",x,"y=",y,"xy=",mul(x,y))
# find t order 3 with txt^-1=y, tyt^-1=xy (cyclic perm i->j->k->i, k=xy up to sign)
ti=None
for t in C3:
    tx=mul(mul(t,x),inv(t)); ty=mul(mul(t,y),inv(t))
    if tx==y and (ty==mul(x,y) or ty==mul(MI,mul(x,y))):
        ti=(t,tx,ty); break
print("t=",ti[0],"txt-1=",ti[1],"tyt-1=",ti[2],"xy=",mul(x,y))
t=ti[0]
# verify full relation set
rels={"x^4==1":pw(x,4)==ID,"x^2==y^2":pw(x,2)==pw(y,2),
 "y^-1xy==x^-1":mul(mul(inv(y),x),y)==inv(x),
 "t^3==1":pw(t,3)==ID,"txt^-1==y":mul(mul(t,x),inv(t))==y,
 "tyt^-1==+-xy":mul(mul(t,y),inv(t)) in (mul(x,y),mul(MI,mul(x,y)))}
print(rels); assert all(rels.values())
# generation: BFS words in x,y,t
gens=[x,y,t]+[inv(x),inv(y),inv(t)]
S={ID}; st=[ID]
while st:
    a=st.pop()
    for g in gens:
        b=mul(a,g)
        if b not in S: S.add(b); st.append(b)
print("generated:",len(S))
import json
json.dump({"x":list(x),"y":list(y),"t":list(t),
 "rels":{k:bool(v) for k,v in rels.items()},"generated":len(S),
 "tyt-1":list(ti[2]),"xy":list(mul(x,y))},open(ART+"sl23_present.json","w"))
print("saved")
