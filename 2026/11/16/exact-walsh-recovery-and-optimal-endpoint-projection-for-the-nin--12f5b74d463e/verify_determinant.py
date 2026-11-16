"""Independent exact signed-Laplacian cofactor census; Python 3 standard library."""
from collections import Counter
from itertools import product
# Grid vertices numbered r*3+c. Deliberately different edge construction order.
E=[]
for r in range(3):
    for c in range(2):E.append((3*r+c,3*r+c+1))
for c in range(3):
    for r in range(2):E.append((3*r+c,3*(r+1)+c))
assert len(E)==12

def det_bareiss(A):
    A=[row[:] for row in A]
    n=len(A);prev=1;sign=1
    for k in range(n-1):
        if A[k][k]==0:
            for z in range(k+1,n):
                if A[z][k]:A[k],A[z]=A[z],A[k];sign=-sign;break
            else:return 0
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                top=A[i][j]*pivot-A[i][k]*A[k][j]
                assert top%prev==0
                A[i][j]=top//prev
            A[i][k]=0
        prev=pivot
    return sign*A[n-1][n-1]

def signed_tree_count(mask):
    A=[[0]*8 for _ in range(8)] # delete vertex 8
    for e,(a,b) in enumerate(E):
        w=-1 if mask>>e&1 else 1
        if a<8:A[a][a]+=w
        if b<8:A[b][b]+=w
        if a<8 and b<8:A[a][b]-=w;A[b][a]-=w
    return det_bareiss(A)

spectrum=[signed_tree_count(mask) for mask in range(1<<12)]
EXPECT={0:1186,4:1536,8:496,12:320,16:176,20:64,24:48,28:64,32:68,36:64,40:16,64:24,72:16,80:16,192:2}
assert Counter(abs(x) for x in spectrum)==EXPECT
assert sum(v!=0 for v in spectrum)==2910
assert min(abs(v) for v in spectrum if v)!=0 and min(abs(v) for v in spectrum if v)==4
# Projection onto nonzero Fourier modes: integer-numerator inverse Walsh of support.
kernel=[0]*4096
for f,v in enumerate(spectrum):
    if v:
        for x in range(4096):
            kernel[x]+=1 if ((x&f).bit_count()%2)==0 else -1
assert sum(abs(k) for k in kernel)==40976
assert kernel[0]==2910
print('PASS weighted Matrix-Tree/Bareiss 4096 signs / projection norm 40976/4096')
