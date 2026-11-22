"""Independent exhaustive factor-occurrence test of all two-position attractors."""
from itertools import combinations, product

def formula(a,b,c):
    def F(x,y,z):
        if y>x:
            return x+1 if z<=y else 0
        if z<=y:
            return x + (y if x==y else 0) + (z if x==z else 0)
        return y+1 if z>=x else 0
    return F(a,b,c)+F(c,b,a)

def direct(word):
    n=len(word)
    masks={}
    for i in range(n):
        for j in range(i+1,n+1):
            s=word[i:j]
            masks[s]=masks.get(s,0)|(((1<<(j-i))-1)<<i)
    good=[]
    for i,j in combinations(range(n),2):
        m=(1<<i)|(1<<j)
        if all(m & covered for covered in masks.values()):
            good.append((i,j))
    return good

def test():
    checks=0
    for a,b,c in product(range(1,11),repeat=3):
        word='0'*a+'1'+'0'*b+'1'+'0'*c
        good=direct(word)
        expect=formula(a,b,c)
        assert len(good)==expect, (a,b,c,len(good),expect)
        p=a;q=a+b+1
        for i,j in good:
            assert (p in (i,j)) != (q in (i,j)),(a,b,c,i,j)
        checks+=1
    print(f'PAIR_EXHAUSTIVE_OK triples={checks} max_run=10')

if __name__=='__main__':test()
