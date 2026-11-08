from itertools import combinations, product

def classify(lengths):
    q=len(lengths); m=min(lengths); p=sum(lengths)
    seq=[i for i,L in enumerate(lengths) for _ in range(L)]
    actual={(u,v) for u,v in combinations(range(1,p),2) if all(seq[i] in (seq[(i+u)%p],seq[(i+v)%p]) for i in range(p))}
    predicted={(u,p-d) for u in range(1,m) for d in range(1,m+1-u)}
    return actual,predicted
cases=0
for q in range(2,7):
 for ls in product(range(1,6),repeat=q):
  actual,pred=classify(ls);cases+=1
  if actual!=pred:
   print('COUNTEREXAMPLE',ls,actual,pred);raise SystemExit(1)
print('PASS',cases,'exhaustive run profiles (q=2..6, lengths=1..5)')
