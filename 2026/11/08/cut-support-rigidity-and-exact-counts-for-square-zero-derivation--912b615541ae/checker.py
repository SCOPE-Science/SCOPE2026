import itertools

def direct_test(n,q):
    pairs=[(i,j) for i in range(n) for j in range(i,n)]
    strict=[(i,j) for i,j in pairs if i<j]
    index={p:k for k,p in enumerate(pairs)}
    count=0; observed=0; failure=0
    for vals in itertools.product(range(q), repeat=len(strict)):
        N=dict(zip(strict,vals)); NZ=[(i,j) for (i,j),a in N.items() if a]
        prediction=(not NZ) or max(i for i,j in NZ)<min(j for i,j in NZ)
        D=[]
        for i,j in pairs:
            col={}
            for a in range(i):
                c=N.get((a,i),0)
                if c: col[index[a,j]]=(col.get(index[a,j],0)+c)%q
            for b in range(j+1,n):
                c=N.get((j,b),0)
                if c: col[index[i,b]]=(col.get(index[i,b],0)-c)%q
            D.append({k:v for k,v in col.items() if v})
        square_zero=True
        for col in D:
            comp={}
            for idx,c in col.items():
                for k,v in D[idx].items():
                    comp[k]=(comp.get(k,0)+c*v)%q
            if any(comp.values()):
                square_zero=False;break
        if square_zero != prediction:
            print('MISMATCH',n,q,vals,square_zero,prediction);failure+=1;break
        count+=int(square_zero);observed+=1
    expected=1+sum(q**(a*(n-b+1))-q**((a-1)*(n-b+1))-q**(a*(n-b))+q**((a-1)*(n-b)) for a in range(1,n) for b in range(a+1,n+1))
    assert failure==0 and count==expected
    print(f'n={n} q={q} cases={observed} actual={count} formula={expected} all_pass=True')

for n,q in [(2,3),(3,3),(4,3),(4,5),(5,3)]:direct_test(n,q)
# sharp char 2 boundary
n=4;q=2
N={(0,1):1,(2,3):1}
pairs=[(i,j) for i in range(n) for j in range(i,n)]
index={p:k for k,p in enumerate(pairs)}
D=[]
for i,j in pairs:
 col={}
 for a in range(i):
  c=N.get((a,i),0)
  if c:col[index[a,j]]=(col.get(index[a,j],0)+c)%q
 for b in range(j+1,n):
  c=N.get((j,b),0)
  if c:col[index[i,b]]=(col.get(index[i,b],0)-c)%q
 D.append({k:v for k,v in col.items() if v})
assert all(not any((sum(coef*D[idx].get(k,0) for idx,coef in col.items())%2) for k in range(len(pairs))) for col in D)
assert max(i for i,j in N)>=min(j for i,j in N)
print('characteristic_two_n4_off_cut_example=True')
print('UPPER_TRIANGULAR_SANDWICH_DIRECT_ADJOINT_PASS')
