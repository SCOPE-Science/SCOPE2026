"""Independent GF(25) arithmetic check for genus-three reciprocal octics.
No external modules are required; GF(25) = GF(5)[u]/(u^2-2).
"""
P=5
# packed e = c0+5*c1 for c0,c1 in F5
ADD=[[((x%5+y%5)%5)+5*((x//5+y//5)%5) for y in range(25)] for x in range(25)]
NEG=[(-e%5)+5*((-(e//5))%5) for e in range(25)]
MUL=[ [((x%5*y%5+2*(x//5)*(y//5))%5)+5*((x%5*(y//5)+(x//5)*(y%5))%5) for y in range(25)] for x in range(25)]
def plus(x,y):return ADD[x][y]
def neg(x):return NEG[x]
def mul(x,y):return MUL[x][y]
def sub(x,y):return ADD[x][NEG[y]]
def pw(x,n):
    r=1
    while n:
        if n&1:r=mul(r,x)
        x=mul(x,x);n//=2
    return r
chi=[0 if z==0 else (1 if pw(z,12)==1 else -1) for z in range(25)]
assert all(pw(z,24)==1 for z in range(1,25))

def valf(x,a,b):
    x2=mul(x,x);x4=mul(x2,x2);x6=mul(x4,x2);x8=mul(x4,x4)
    return plus(plus(x8,mul(a,x6)),plus(plus(mul(b,x4),mul(a,x2)),1))
def quartic_values(t,a,b):
    t2=mul(t,t);t3=mul(t2,t);t4=mul(t2,t2)
    v0=plus(plus(t4,mul(a,t3)),plus(plus(mul(b,t2),mul(a,t)),1))
    vp=plus(t4,plus(mul(sub(a,4),t2),plus(sub(b,mul(2,a)),2)))
    vm=plus(t4,plus(mul(plus(a,4),t2),plus(plus(b,mul(2,a)),2)))
    return (v0,vp,vm)

def smooth(a,b):
    return (sub(sub(mul(2,a),b),2)!=0 and plus(plus(mul(2,a),b),2)!=0 and plus(sub(mul(a,a),mul(4,b)),3)!=0)

def rank(a,b):
    aa=mul(a,a);bb=mul(b,b);A=plus(aa,mul(2,b));B=mul(2,a)
    return int(plus(A,B)!=0)+int(sub(A,B)!=0)+int(plus(plus(mul(2,aa),bb),2)!=0)
counts={1:0,2:0,3:0};exceptions=[];checks=0
for a in range(25):
 for b in range(25):
    if not smooth(a,b):continue
    rr=rank(a,b);counts[rr]+=1
    if rr==1:exceptions.append((a,b))
    Ns=[27,27,27]
    NC=27
    for x in range(25):
        NC+=chi[valf(x,a,b)]
        for j,v in enumerate(quartic_values(x,a,b)):
            Ns[j]+=chi[v]
    assert sum(Ns)-52 == NC,(a,b,Ns,NC)
    assert sum((26-n)%5!=0 for n in Ns)==rr,(a,b,Ns,rr)
    checks+=1
assert exceptions==[(0,0),(2,0),(3,0)],exceptions
print('HOWE5_GF25_INDEPENDENT_PASS smooth=',checks,'rank_counts=',counts,'rank_one=',exceptions)
