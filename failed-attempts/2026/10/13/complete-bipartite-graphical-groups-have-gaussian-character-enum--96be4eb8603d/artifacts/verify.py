from itertools import product

def rank_mod(flat,a,b,q):
    M=[list(flat[r*b:(r+1)*b]) for r in range(a)]
    rank=0
    for c in range(b):
        piv=next((r for r in range(rank,a) if M[r][c]%q),None)
        if piv is None: continue
        M[rank],M[piv]=M[piv],M[rank]
        z=pow(M[rank][c]%q,-1,q)
        M[rank]=[(z*x)%q for x in M[rank]]
        for r in range(a):
            if r!=rank and M[r][c]%q:
                z=M[r][c]%q
                M[r]=[(M[r][j]-z*M[rank][j])%q for j in range(b)]
        rank+=1
        if rank==a: break
    return rank

def formula(a,b,i,q):
    if i==0: return 1
    num=den=1
    for j in range(i):
        num*=(q**a-q**j)*(q**b-q**j)
        den*=(q**i-q**j)
    assert num%den==0
    return num//den

def check(q,a,b):
    counts=[0]*(min(a,b)+1)
    for flat in product(range(q),repeat=a*b):
        counts[rank_mod(flat,a,b,q)]+=1
    assert counts==[formula(a,b,i,q) for i in range(len(counts))]
    chars=[q**(a+b-2*i)*counts[i] for i in range(len(counts))]
    assert sum(chars[i]*(q**i)**2 for i in range(len(chars)))==q**(a+b+a*b)
    return counts,chars

for case in [(3,2,2),(3,2,3),(3,3,3),(5,2,2),(5,2,3)]:
    print(case,check(*case))
assert check(3,2,2)==([1,32,48],[81,288,48])
print("VERIFY_OK")
