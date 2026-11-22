from fractions import Fraction as F

def source(t):
    return min(F(1), F(1,2)+F(t,1000))

def run(K, steps=1100):
    a=a2=F(0); b=F(21,100)
    all_active=True; first_loss=None
    for t in range(steps):
        s=source(t)
        nodes=[a,a2,b]; src=[s]*K
        edges=[(0,1,F(1)),(0,2,F(1,2)),(1,2,F(1,2))]
        for j in range(K): edges.append((2,3+j,F(1)))
        values=nodes+src
        totals=[F(0)]*3;weights=[F(0)]*3
        for i,j,w in edges:
            if abs(values[i]-values[j])<=F(3,10):
                for n,m in [(i,j),(j,i)]:
                    if n<3:totals[n]+=w*values[m];weights[n]+=w
            elif i<3 and j<3:
                if first_loss is None:first_loss=t
                all_active=False
        assert all(weights), (K,t,values,weights)
        a,a2,b=(totals[i]/weights[i] for i in range(3))
        assert a==a2 and all(F(0)<=z<=1 for z in (a,b))
        if K>=3 and t==0:
            assert a==F(7,100) and b==F(K,2*(K+1))
        if K>=3 and t>=1:
            assert a==F(7,100)
            assert b==source(t) # at t=1 updating to t+1=2: b=source(1)
    return a,b,first_loss,all_active

for K in [1,2,3,4,6,30]:
    a,b,loss,full=run(K)
    if K<=2: assert full and abs(a-1)<F(1,10**30) and abs(b-1)<F(1,10**30),(K,a,b)
    else: assert a==F(7,100) and b==1 and loss==1,(K,a,b,loss)
    print('K',K,'limit vicinity',float(a),float(b),'first ordinary edge loss',loss)
for K in (1,2):
    x=F(21,100);y=F(29,100)
    for _ in range(100):
      if K==1: nx=x/6+y/2;ny=(x+y)/2+F(1,1000)
      else: nx=(x+2*y)/3;ny=(x+y)/3+F(1,1000)
      assert nx<=F(3,10) and ny<=F(3,10) and nx>=0 and ny>=0
      x,y=nx,ny
print('Exact rational checks passed')
