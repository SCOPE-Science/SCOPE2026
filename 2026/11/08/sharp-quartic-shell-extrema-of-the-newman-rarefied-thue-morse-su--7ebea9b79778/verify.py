# Independent finite check of rarefied Thue--Morse shell identities.
def tm(j): return 1 if j.bit_count()%2 == 0 else -1
M=4**8
F=[0]*(M+1)
for j in range(M): F[j+1]=F[j]+tm(3*j)
for m in range(M//4):
 s=0 if m%2==0 else tm((3*m-1)//2)
 a,b=tm(3*m),tm(3*m+1)
 deltas=(-s,-s+a,-s+2*a,-s+2*a-b)
 for r in range(4): assert F[4*m+r] == 3*F[m]+deltas[r], (m,r)
for k in range(1,7):
 lo,hi=4**k,4**(k+1)
 L=4*3**(k-1); U=4*3**k
 assert min(F[lo:hi])==L and max(F[lo:hi])==U
 assert [n for n in range(lo,hi) if F[n]==L]==[lo]
 assert [n for n in range(lo,hi) if F[n]==L+1]==[lo+1]
 n=(10*lo+2)//3
 assert 3*n == 10*lo+2 and F[n]==U
 print(f'k={k}: [{lo},{hi}): min={L} uniquely at {lo}; max={U}; witness={n}')
print('VERIFY_OK recurrence verified up to m=',M//4-1)
