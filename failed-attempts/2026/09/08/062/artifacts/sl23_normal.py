"""S7: cyclic C3 action on three Q8 legs + 24 normal forms + word check."""
import json
ART="/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-192/output/artifacts/"
def mat(a,b,c,d): return (a%3,b%3,c%3,d%3)
def mul(X,Y):
    a,b,c,d=X; e,f,g,h=Y
    return mat(a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
def inv(X):
    a,b,c,d=X; return mat(d,-b,-c,a)
x=(0,1,2,0); y=(1,1,1,2); t=(0,1,2,2)
ID=mat(1,0,0,1); MI=mat(2,0,0,2)
xy=mul(x,y)
def conj(a,b): return mul(mul(a,b),inv(a))
print("t(xy)t-1 =",conj(t,xy)," vs x =",x)
assert conj(t,xy)==x, "third leg"
# Q8 normal forms: {1,x,x^2,x^3,y,xy,x^2y,x^3y}
def pw(X,m):
    R=ID
    for _ in range(m): R=mul(R,X)
    return R
Q8nf=[ID]+[pw(x,i) for i in (1,2,3)]+[mul(pw(x,i),y) for i in (0,1,2,3)]
Q8nf=list(dict.fromkeys(Q8nf))
print("Q8 nf:",len(Q8nf))
assert len(Q8nf)==8 and set(Q8nf)=={g for g in [mat(a,b,c,d) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if (a*d-b*c)%3==1] if pw(g,4)==ID}
NF=[mul(q,pw(t,c)) for q in Q8nf for c in (0,1,2)]
print("24 nf distinct:",len(set(NF))==24)
print("txt-1==y:",conj(t,x)==y,"tyt-1==xy:",conj(t,y)==xy,"t(xy)t-1==x:",conj(t,xy)==x)
# a sample relation consequence: every elt has a word (record indices)
json.dump({"txt-1":list(conj(t,x)),"tyt-1":list(conj(t,y)),"txyt-1":list(conj(t,xy)),
           "x":list(x),"Q8nf":len(Q8nf),"NF24":len(set(NF))==24},
          open(ART+"sl23_normal.json","w"))
print("saved sl23_normal.json")
