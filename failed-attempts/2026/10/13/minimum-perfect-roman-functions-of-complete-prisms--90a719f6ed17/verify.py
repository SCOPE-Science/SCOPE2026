from math import comb

def exact_vectors(length,total,maxv=2):
    a=[0]*length
    def rec(i,rem):
        if i==length:
            if rem==0: yield tuple(a)
            return
        for x in range(min(maxv,rem)+1):
            a[i]=x
            yield from rec(i+1,rem-x)
    yield from rec(0,total)

def is_prd(n,lab):
    A=lab[:n]; B=lab[n:]
    for i,x in enumerate(A):
        if x==0:
            twos=sum(A[j]==2 for j in range(n) if j!=i)+(B[i]==2)
            if twos!=1:return False
    for i,y in enumerate(B):
        if y==0:
            twos=sum(B[j]==2 for j in range(n) if j!=i)+(A[i]==2)
            if twos!=1:return False
    return True

def predicted(n,lab):
    if sum(lab)!=4:return False
    A=lab[:n];B=lab[n:]
    return sum(x==2 for x in A)==1 and sum(y==2 for y in B)==1 and all(x in (0,2) for x in lab) and next(i for i,x in enumerate(A) if x==2)==next(i for i,y in enumerate(B) if y==2)

print('VERIFY_OK')
checked=0
for n in range(4,13):
    feasible=[]
    for w in range(5):
        for lab in exact_vectors(2*n,w):
            checked+=1
            ok=is_prd(n,lab)
            if ok: feasible.append(lab)
            if w<4: assert not ok,(n,w,lab)
    mins=[x for x in feasible if sum(x)==4]
    assert len(mins)==n,(n,len(mins))
    assert all(predicted(n,x) for x in mins)
    print(f'n={n}: gamma_pR=4, minimum_functions={len(mins)}')
print('bounded_labelings_checked =',checked)
print('all minima were matched pairs labelled 2, all other vertices 0')
