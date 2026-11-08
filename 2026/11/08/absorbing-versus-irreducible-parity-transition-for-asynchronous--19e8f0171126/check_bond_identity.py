"""Independent bond-word check of the local spin-flip identity and census."""
from math import comb

def predicted(n):
    if n%4 == 0:return 4
    if n%4 == 1:return n*(n*n+23)//12
    if n%4 == 2:return n*n//2
    return 2*n

def bcount(n):
    c = 0; maximum = -1
    for z in range(1<<n):
        if z.bit_count()%2 != n%2:continue
        ones=z.bit_count()
        adjacent=sum(((z>>i)&1) & ((z>>((i+1)%n))&1) for i in range(n))
        cut=n+ones-2*adjacent
        if cut>maximum:maximum=cut;c=2
        elif cut==maximum:c+=2
    return maximum,c

def local_tests():
    for a in (0,1):
      for b in (0,1):
       for c in (0,1):
        for d in (0,1):
         def score(a,b,c,d):return b+c-2*(a*b+b*c+c*d)
         delta=score(a,1-b,1-c,d)-score(a,b,c,d)
         assert delta == 4*a*b-2*a+4*c*d-2*d
         if b==c==1:assert delta>=0
         if (a,b,c,d)==(0,0,0,0):assert delta==0
         if (a,b,c,d)==(1,1,0,0):assert delta==2
    print('PASS: all 16 four-bond flip identities, particle annihilation and pair-creation/splitting moves')

if __name__=='__main__':
    local_tests()
    total=0
    for n in range(5,18):
        m,count=bcount(n)
        assert count==predicted(n),(n,count,predicted(n))
        total+=(1<<(n-1))
        print('n=%d even/odd bond words=%d maxcut=%d state_count=%d'%(n,1<<(n-1),m,count))
    print('PASS: %d parity-valid bond words, each with two spin lifts, n=5..17'%total)
