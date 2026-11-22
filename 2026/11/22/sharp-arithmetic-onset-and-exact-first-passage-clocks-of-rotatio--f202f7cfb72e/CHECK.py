"""Self-contained exhaustive checks for cyclic Boolean erosion symmetry theorem."""

def evolve(s, n):
    return s & ((s >> 1) | ((s & 1) << (n-1)))

def is_sym(s, n, d):
    return all(((s >> i) & 1) == ((s >> ((i+d)%n)) & 1) for i in range(n))

def heights(s, n):
    if s == (1<<n)-1:
        return None
    a=[(s >> i)&1 for i in range(n)]
    h=[0]*n
    for i in range(n):
        if a[i] and not a[(i-1)%n]:
            j=i
            while a[j%n]:
                j+=1
            h[i]=j-i
    return h

def predicted(s,n,d):
    h=heights(s,n)
    if h is None:
        return 0
    return max([0]+[max(h[i],h[(i+d)%n]) for i in range(n) if h[i]!=h[(i+d)%n]])

def check_clocks():
    total=0
    for n in range(2,13):
        for s in range(1<<n):
            h=heights(s,n)
            for d in range(1,n):
                t0=predicted(s,n,d)
                y=s
                for t in range(n+1):
                    assert is_sym(y,n,d)==(t>=t0),(n,s,d,t,t0,y,h)
                    y=evolve(y,n)
                total+=1
    return total

def check_onset():
    counts=[]
    for n in range(2,17):
        count=0
        for s in range(1,1<<n):
            if any(is_sym(s,n,d) for d in range(1,n)):
                continue
            y=s
            while y:
                y=evolve(y,n)
                if y and any(is_sym(y,n,d) for d in range(1,n)):
                    count+=1
                    break
        expected=(n>=10 and any(n%d==0 for d in range(2,n)))
        assert (count>0)==expected,(n,count,expected)
        counts.append((n,count))
    return counts

if __name__=='__main__':
    print('clock verifications',check_clocks())
    print('nonuniform symmetry births',check_onset())
    print('PASS')
