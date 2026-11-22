"""Direct border-occurrence oracle for maximal closed substrings in palindromic five-run binary words."""

def closed(v):
    if len(v) == 1:
        return True
    n=len(v)
    for h in range(1,n):
        u=v[:h]
        if u == v[-h:] and sum(v[j:j+h] == u for j in range(n-h+1)) == 2:
            return True
    return False

def oracle(word):
    n=len(word)
    return {(i+1,j+1) for i in range(n) for j in range(i,n)
        if closed(word[i:j+1]) and (i==0 or not closed(word[i-1:j+1]))
        and (j==n-1 or not closed(word[i:j+2]))}

def predicted(a,b,c):
    n=2*a+2*b+c
    bounds=[(1,a),(a+1,a+b),(a+b+1,a+b+c),
            (a+b+c+1,a+2*b+c),(a+2*b+c+1,n)]
    ans=set(bounds)
    for t in range(1,min(a,c-1)+1):
        ans.add((a-t+1,a+b+t))
        ans.add((a+b+c-t+1,a+2*b+c+t))
    for t in range(1,b):
        ans.add((a+b-t+1,a+b+c+t))
    for t in range(min(a,c),a+1):
        ans.add((a-t+1,a+2*b+c+t))
    return ans

if __name__=='__main__':
    cases=0; occurrences=0
    for a in range(1,7):
        for b in range(1,7):
            for c in range(1,7):
                w='0'*a+'1'*b+'0'*c+'1'*b+'0'*a
                got=oracle(w); want=predicted(a,b,c)
                assert got==want, (a,b,c, sorted(got-want), sorted(want-got))
                expect=a+b+4+min(a-1,c-1)+2*(c>a)
                assert len(got)==expect,(a,b,c,len(got),expect)
                cases+=1; occurrences+=len(got)
    print('DIRECT_BORDER_ORACLE PASS cases',cases,'MCS_occurrences',occurrences,'max_length',30)
