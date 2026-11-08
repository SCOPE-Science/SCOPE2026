"""Exhaustive rank-one Lie Rota-Baxter verification over GF(9)=GF(3)[t]/(t^2+1)."""
from itertools import product
q=9
add=[[(a%3+c%3)%3+3*((a//3+c//3)%3) for c in range(q)] for a in range(q)]
neg=[(-a%3)+3*((-a//3)%3) for a in range(q)]
mul=[[( (a%3)*(b%3)- (a//3)*(b//3))%3 + 3*(((a%3)*(b//3)+(a//3)*(b%3))%3) for b in range(q)] for a in range(q)]
# Note neg table computed as separate digit negations.
neg=[(-a%3)+3*((-(a//3))%3) for a in range(q)]
def sub(a,b):return add[a][neg[b]]
def br(a,b):
    x,y,z=a; X,Y,Z=b
    return (sub(mul[6][sub(mul[z][X],mul[x][Z])],0),
        mul[6][sub(mul[y][Z],mul[z][Y])],sub(mul[x][Y],mul[y][X]))
def tr(a,b):return add[add[mul[a[0]][b[1]]][mul[a[1]][b[0]]]][mul[6][mul[a[2]][b[2]]]]
def proportional(x,y):
    return all(sub(mul[x[i]][y[j]],mul[x[j]][y[i]])==0 for i in range(3) for j in range(i+1,3))
def scalar(c,v):return tuple(mul[c][e] for e in v)
def madd(u,v):return tuple(add[a][b] for a,b in zip(u,v))
def direct(a,b):
    basis=((1,0,0),(0,1,0),(0,0,1))
    for i in range(3):
      for j in range(i+1,3):
        u,v=basis[i],basis[j]
        ru=scalar(tr(b,u),a);rv=scalar(tr(b,v),a)
        w=madd(br(ru,v),br(u,rv))
        if br(ru,rv)!=scalar(tr(b,w),a):return False
    return True
els=[v for v in product(range(q),repeat=3) if any(v)]
counts=[0]*6
for a in els:
 for b in els:
    commuting=(br(a,b)==(0,0,0))
    root=(tr(b,b)==0 and proportional(br(a,b),b))
    rb=direct(a,b)
    assert rb==(commuting or root), (a,b,rb,commuting,root)
    if rb:
      counts[0]+=1;counts[1]+=commuting;counts[2]+=root;counts[3]+=(commuting and root)
      counts[4]+=(tr(a,b)==0);counts[5]+=(tr(a,b)==1)
counts=[v//(q-1) for v in counts]
assert counts==[2*q**3-q-1,q**3-1,(q+1)*(q*q-1),q*q-1,q**3+q*q-q-1,q*q],counts
print('GF9:',counts)
print('SL2_RANKONE_RB_GF9_DIRECT_PASS')
