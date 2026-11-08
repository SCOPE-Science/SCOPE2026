import math, heapq, random

def eval_form(n,p,m):
    Q=n*n+p*p; A=2*m*n; D=2*m*p; B=m*m-Q; C=m*m+Q
    assert m>Q and math.gcd(n,p)==1 and math.gcd(m,Q)==1 and (m+n+p)%2==1
    t=next(x for x in range(n) if (p*x-Q+m)%n==0)
    ell=Q+p*(n-t)-m
    ap=[None]*A
    for v in range(n):
      for z in range(-m,m):
        val=v*D+abs(z)*m*m+Q*z
        if t and ell>0 and z==m-1 and v>=n-t:
          val=(v+t-n)*D + (m+1)*m*m - (m+1)*Q
        r=val%A
        assert ap[r] is None, (n,p,m,r)
        ap[r]=val
    assert all(v is not None for v in ap)
    genus=(sum(ap)-A*(A-1)//2)//A
    form_num=n*(m**3-Q+1+2*m*(n*p-n-p))-2*t*max(0,ell)
    assert form_num%(2*n)==0, (n,p,m,t,ell,form_num)
    formula=form_num//(2*n)
    assert formula==genus,(n,p,m,genus,formula)
    # dijkstra mod A with + A omitted; shortest paths using remaining three generators
    dist=[10**50]*A;dist[0]=0;todo=[(0,0)]
    while todo:
       d,r=heapq.heappop(todo)
       if d!=dist[r]:continue
       for a in (D,B,C):
          rr=(r+a)%A
          if d+a<dist[rr]: dist[rr]=d+a;heapq.heappush(todo,(d+a,rr))
    if ap!=dist:
        for r,(x,y) in enumerate(zip(ap,dist)):
            if x!=y:raise AssertionError((n,p,m,r,x,y,t,ell))
    return genus,t,ell

if __name__=='__main__':
    K=0;cor=0;maxA=0
    for n in range(1,8):
      for p in range(1,8):
       if math.gcd(n,p)!=1:continue
       Q=n*n+p*p
       ms=sorted(set(list(range(Q+1,min(2*Q+7,Q+38)))+[Q+1, 2*Q-1,2*Q,2*Q+1]))
       for m in ms:
        if math.gcd(m,Q)>1 or (m+n+p)%2!=1:continue
        g,t,ell=eval_form(n,p,m);K+=1;cor+=bool(t and ell>0);maxA=max(maxA,2*m*n)
    print('EXACT_DIJKSTRA_AND_APERY_OK',K,'nonzero_corrections',cor,'max_modulus',maxA)
