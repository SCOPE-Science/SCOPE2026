"""Reproduce finite base certificates for the Perrin 23-adic image theorem.
Only Python standard library is needed. Independent of proof's infinite analytic step.
"""
from collections import Counter, defaultdict
P = 23
M = P * P

def mm(a,b):
    return tuple(tuple(sum(a[i][t]*b[t][j] for t in range(3)) for j in range(3)) for i in range(3))

def mp(a,n):
    out=((1,0,0),(0,1,0),(0,0,1))
    while n:
        if n & 1:out=mm(out,a)
        a=mm(a,a);n//=2
    return out

def tr(a):return sum(a[i][i] for i in range(3))

def mat_add(a,b,sign=1):return tuple(tuple(a[i][j]+sign*b[i][j] for j in range(3)) for i in range(3))

A=((0,1,0),(0,0,1),(1,1,0))
I=mp(A,0)
N=mat_add(mp(A,22),I,-1)
N2=mm(N,N);N3=mm(N2,N)
assert all(x%P==0 for row in N2 for x in row)
for r in range(3):
    Ap=mp(A,r)
    assert tr(mm(Ap,N))%P==0
    assert tr(mm(Ap,N2))%P==0
    assert tr(mm(Ap,N3))%M==0

seq=[3,0,2]
for n in range(3,70): seq.append(seq[n-2]+seq[n-3])
assert [tr(mp(A,n)) for n in range(70)]==seq

groups=defaultdict(list)
rows=[]
for r in range(22):
    a=seq[r]%M
    q=((seq[r+44]-2*seq[r+22]+seq[r])*pow(2,-1,M))%M
    b=(seq[r+22]-a-q)%M
    assert (q%P,b%P)==(0,0)
    u,v=q//P,b//P
    assert 0<u<P
    c=(-v*pow(2*u,-1,P))%P
    critical=(a+P*(u*c*c+v*c))%M
    values={ (a+P*(u*t*t+v*t))%M for t in range(P) }
    assert len(values)==12
    for t in range(P):
        # Exact recurrence modulo 23^2 for t in complete 23-adic residue system.
        z=[3,0,2]
        for n in range(3,r+22*t+1): z.append((z[n-2]+z[n-3])%M)
        assert z[r+22*t]%M==(a+P*(u*t*t+v*t))%M
    groups[a%P].append((r,a,u,v,c,critical,values))
    rows.append((r,a,u,v,c,critical))

expected={0:(12,1),1:(12,1),2:(22,2),3:(17,0),4:(12,1),5:(20,0),6:(12,1),7:(12,1),10:(12,1),12:(12,1),16:(12,1),17:(12,1),20:(12,1),21:(12,1),22:(20,0)}
assert set(groups)==set(expected)
full_classes=0;critical_classes=0
summary=[]
for base,grp in sorted(groups.items()):
    union=set().union(*(z[6] for z in grp))
    critical_only={value for value in union if all(value==z[5] for z in grp if value in z[6])}
    assert (len(union),len(critical_only))==expected[base]
    assert all(sum(value in z[6] for z in grp)==1 for value in critical_only)
    full_classes+=len(union)-len(critical_only)
    critical_classes+=len(critical_only)
    summary.append((base,tuple(z[0] for z in grp),len(union),len(critical_only)))
assert full_classes==198 and critical_classes==13

def square_count(m):
    if m<=0:return 1
    if m==1:return 12
    return 11*P**(m-1)+square_count(m-2)

def predicted(k):
    if k==1:return 15
    if k==2:return 211
    return 198*P**(k-2)+13*square_count(k-3)

for k in range(1,5):
    modulus=P**k;period=22*P**(k-1)
    a,b,c=3,0,2
    hist=Counter()
    for i in range(period):
        hist[a]+=1
        a,b,c=b,c,(a+b)%modulus
    assert (a,b,c)==(3%modulus,0,2%modulus)
    assert len(hist)==predicted(k),(k,len(hist),predicted(k))
    if k==1:
        cyclic=[]
        a0,b0,c0=3,0,2
        for _ in range(period):
            cyclic.append(a0); a0,b0,c0=b0,c0,(a0+b0)%modulus
        assert not any(all(cyclic[i]==cyclic[(i+d)%period] for i in range(period)) for d in (1,2,11))
    assert all(hist[v] for v in hist)
    print(f'LEVEL k={k} modulus={modulus} period={period} image={len(hist)} frequencies={dict(Counter(hist.values()))}')
print('BASE_TABLE',rows)
print('GROUP_CERTIFICATE',summary)
print('VERIFY_OK base_rows=22 base_groups=15 full_lift_classes=198 quadratic_classes=13 prime_power_levels=4')
