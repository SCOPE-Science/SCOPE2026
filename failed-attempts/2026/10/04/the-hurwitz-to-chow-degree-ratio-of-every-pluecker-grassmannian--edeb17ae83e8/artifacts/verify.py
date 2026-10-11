from math import factorial

def degree_grassmannian(k,n):
    d=k*(n-k)
    num=factorial(d)
    for j in range(1,k):
        num*=factorial(j)
    den=1
    for j in range(n-k,n):
        den*=factorial(j)
    assert num%den==0
    return num//den

checks=0
for n in range(4,121):
    for k in range(2,n-1):
        D=degree_grassmannian(k,n)
        assert D==degree_grassmannian(n-k,n)
        d=k*(n-k)
        genus_num=(d-n-1)*D
        assert genus_num%2==0
        g=1+genus_num//2
        H=2*D+2*g-2
        assert H==(k-1)*(n-k-1)*D
        assert H>=D
        assert (H==D)==(k==2 and n==4)
        checks+=1

assert degree_grassmannian(2,4)==2
assert degree_grassmannian(2,5)==5
assert degree_grassmannian(2,6)==14
assert degree_grassmannian(3,6)==42

print("VERIFY_OK",checks)
