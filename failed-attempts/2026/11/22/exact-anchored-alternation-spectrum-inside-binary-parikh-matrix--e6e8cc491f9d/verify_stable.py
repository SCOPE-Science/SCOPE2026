"""Independent partition recursion for stable distinct-part-size spectrum."""
from collections import Counter, defaultdict

def distinct_part_hist(C):
    ans=Counter()
    def rec(maxpart,left,used):
        if left==0:
            ans[used]+=1
            return
        for part in range(min(maxpart,left),0,-1):
            for mult in range(1,left//part+1):
                rec(part-1,left-part*mult,used+1)
    rec(C,C,0)
    return ans

def coefficient_hist(A,B,C):
    dp={(0,0,0):1}
    # process interior gap counts x_i; no initial / trailing b yet
    for i in range(1,A):
        new=defaultdict(int)
        for (b,c,j),v in dp.items():
            for x in range(min(B-b,(C-c)//i)+1):
                new[(b+x,c+i*x,j+int(x>0))]+=v
        dp=new
    out=Counter()
    for (used,cc,j),v in dp.items():
        for xA in range(min(B-used,(C-cc)//A)+1):
            if cc+A*xA==C:
                out[j]+=v
    return out

for C in range(0,36):
    A=C+1; B=C
    observed=coefficient_hist(A,B,C)
    target=distinct_part_hist(C)
    assert observed==target,(C, observed, target)
    if C>0 and C<=15:
        assert sum(target.values())==[0,1,2,3,5,7,11,15,22,30,42,56,77,101,135,176][C]
print({'stable_counts_checked':36,'p10_distribution':dict(distinct_part_hist(10)),'p20_distribution':dict(distinct_part_hist(20)),'comparison':'PASS'})
