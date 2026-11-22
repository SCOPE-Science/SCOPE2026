"""Independent exact arithmetic oracle for every phase's block spectrum.
A compatible residue modulo p**h and one unconstrained high-valuation symbol
represent ALL starts in one residue class modulo n, by CRT.
No finite-prefix completeness assumption is made.
"""

def true_phase_count(p,q,n,r):
    h=1
    while p**h<=n:h+=1
    M=p**h
    pk=1
    a=n
    while a%p==0:
        a//=p;pk*=p
    results=set()
    for s in range(r%pk,M,pk):
        letters=[];hole=-1
        for i in range(n):
            x=s+i+1
            if x%M==0:
                letters.append(-1);hole=i
            else:
                v=0
                while x%p==0:x//=p;v+=1
                letters.append(v%q)
        if hole==-1:
            results.add(tuple(letters))
        else:
            for c in range(q):
                letters[hole]=c
                results.add(tuple(letters))
            letters[hole]=-1
    return len(results)

def predicted(n,p,q):
    vals={}
    m=n
    while m%p==0:m//=p
    for x in range(1,m+1):
        if x<=p:vals[x]=1+x*(q-1)
        elif x<2*p:vals[x]=1+(x-p)+x*(q-1)
        else:
            d,r=divmod(x,p);vals[x]=(p-r)*vals[d]+r*vals[d+1]
    return vals[m]

def main():
    tested=0
    for p in (2,3,5,7):
        for q in (2,3,4):
            upto={2:65,3:52,5:36,7:25}[p]
            for n in range(1,upto+1):
                want=predicted(n,p,q)
                for r in range(n):
                    got=true_phase_count(p,q,n,r)
                    if got!=want:raise AssertionError((p,q,n,r,got,want))
                    tested+=1
            print(f'p={p}, q={q}: all {sum(range(1,upto+1))} phases for n=1..{upto} matched exact count')
    print(f'PASS: {tested} complete CRT residue-class spectra verified')
if __name__=='__main__':main()
