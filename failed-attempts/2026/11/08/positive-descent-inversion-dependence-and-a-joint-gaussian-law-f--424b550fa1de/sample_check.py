import random,math,statistics
random.seed(314159)
n=500;c=1.;r=n
trials=4000
res=[]
for _ in range(trials):
  K=len({random.randrange(n) for i in range(r)})
  p=list(range(n));random.shuffle(p)
  deck=p[:K]+sorted(p[K:])
  d=sum(x>y for x,y in zip(deck,deck[1:]))
  tree=[0]*(n+1)
  def add(i):
    i+=1
    while i<=n: tree[i]+=1;i+=i&-i
  def query(i):
    s=0;i+=1
    while i>0: s+=tree[i];i-=i&-i
    return s
  inv=0
  for j,x in enumerate(deck):
    inv+=j-query(x)
    add(x)
  res.append((d/math.sqrt(n),inv/(n**1.5)))
md=statistics.mean(x for x,y in res);mi=statistics.mean(y for x,y in res)
vd=statistics.mean((x-md)**2 for x,y in res)
vi=statistics.mean((y-mi)**2 for x,y in res)
cov=statistics.mean((x-md)*(y-mi) for x,y in res)
b=math.exp(-c);a=1-b;t=b-(1+c)*b*b
truth=(a/12+t/4,(1-b**3)/36+b*b*t/4,b*t/4)
print('trials',trials,'empirical varD,varI,cov',vd,vi,cov,'limits',truth)
for empirical,pred in zip((vd,vi,cov),truth):
 assert abs(empirical-pred)<0.018
print('PASS: three stochastic moment diagnostics, tolerance=0.018')
