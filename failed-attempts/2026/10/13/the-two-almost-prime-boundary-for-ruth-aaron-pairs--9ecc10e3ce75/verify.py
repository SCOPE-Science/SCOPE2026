#!/usr/bin/env python3
LIMIT=2_000_001

# Symbolic finite factor checks corresponding to the proof.
prime_semiprime=[]
for a in range(2,20):
    for b in range(a,20):
        if (a-1)*(b-1)==2:
            prime_semiprime.append((a,b))
assert prime_semiprime==[(2,3)]

semiprime_prime=[]
for a in range(2,20):
    for b in range(a,20):
        if (a-1)*(b-1)==0:
            semiprime_prime.append((a,b))
assert semiprime_prime==[]

integer_shapes=[]
for a in range(2,30):
    for b in range(a,30):
        for t in range(-10,11):
            if t*(b-a-t)==1:
                integer_shapes.append((a,b,t,a+t,b-t))
assert all((b==a+2 and t==1 and c==d==a+1) for a,b,t,c,d in integer_shapes)

# Smallest-prime-factor sieve for a corroborative finite sweep.
spf=list(range(LIMIT+1))
spf[0]=0
spf[1]=1
for p in range(2,int(LIMIT**0.5)+1):
    if spf[p]==p:
        for m in range(p*p,LIMIT+1,p):
            if spf[m]==m:
                spf[m]=p

def sopfr_omega(n):
    s=0
    om=0
    while n>1:
        p=spf[n]
        s+=p
        om+=1
        n//=p
    return s,om

S=[0]*(LIMIT+1)
O=[0]*(LIMIT+1)
for n in range(2,LIMIT+1):
    p=spf[n]
    S[n]=S[n//p]+p
    O[n]=O[n//p]+1

hits=[]
all_ra=0
for n in range(1,LIMIT):
    if S[n]==S[n+1]:
        all_ra+=1
        if O[n]<=2 and O[n+1]<=2:
            hits.append((n,n+1,O[n],O[n+1],S[n]))

assert hits==[(5,6,1,2,5)], hits
assert S[8]==S[9]==6 and O[8]==3 and O[9]==2
print('VERIFY_OK', f'limit={LIMIT-1}', f'ruth_aaron_pairs={all_ra}', f'low_layer={hits}', 'sharp=(8,9)')
