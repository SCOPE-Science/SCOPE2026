#!/usr/bin/env python3
"""Independent integer transfer and labelled-colouring census for open ladders."""
from itertools import product

SIGNS=(-1,0,1)
def signed(delta):
    return (delta+1)%3-1

def face_charge(top0,bottom0,top1,bottom1):
    # Counterclockwise on the square; every value is -3, 0 or 3.
    return (signed(top1-top0)+signed(bottom1-top1)
            +signed(bottom0-bottom1)+signed(top0-bottom0))//3

def matrices():
    m={k:[[0]*3 for _ in range(3)] for k in SIGNS}
    for i,r in enumerate(SIGNS):
        for j,s in enumerate(SIGNS):
            for t in SIGNS:
                u=signed(t+s-r)
                k=(t+s-u-r)//3
                m[k][i][j]+=1
    return m

def count_by_transfer(n):
    m=matrices()
    zero=[1,1,1]
    last={(i,0):1 for i in range(3)}
    for _ in range(n-1):
        zero=[sum(zero[i]*m[0][i][j] for i in range(3)) for j in range(3)]
        new={}
        for (i,old),a in last.items():
            for s in SIGNS:
                if old==s and s!=0:continue
                for j in range(3):
                    new[(j,s)]=new.get((j,s),0)+a*m[s][i][j]
        last=new
    return 3*sum(zero),3*sum(last.values())

def brute(n):
    ct=[0,0,0]
    for x in product(range(3),repeat=2*n):
        f=[face_charge(x[i],x[n+i],x[i+1],x[n+i+1]) for i in range(n-1)]
        if any(f[i]!=0 and f[i]==f[i+1] for i in range(n-2)):
            ct[2]+=1
        elif any(f):
            ct[1]+=1
        else:
            ct[0]+=1
    return ct

def main():
    m=matrices()
    assert m[-1]==[[0,0,0],[1,0,0],[2,1,0]]
    assert m[0]==[[3,2,1],[2,3,2],[1,2,3]]
    assert m[1]==[[0,1,2],[0,0,1],[0,0,0]]
    z={1:9,2:57};q={1:9,2:81,3:723}
    total=0
    for n in range(2,31):
        if n>=3:z[n]=7*z[n-1]-4*z[n-2]
        if n>=4:q[n]=9*q[n-1]-q[n-2]+3*q[n-3]
        zt,qt=count_by_transfer(n)
        assert (zt,qt)==(z[n],q[n]),(n,zt,qt,z[n],q[n])
        assert 0<zt<=qt<=9**n
        if n<=6:
            a,b,c=brute(n)
            assert (a,a+b,c)==(z[n],q[n],9**n-q[n]),(n,(a,b,c),(z[n],q[n]-z[n],9**n-q[n]))
            total+=9**n
            print(f'n={n} zero={a} intermediate={b} maximal={c}')
    print(f'PASS: two transfer recurrences through n=30; independent enumeration {total} colourings at n=2..6.')
if __name__=='__main__':main()
