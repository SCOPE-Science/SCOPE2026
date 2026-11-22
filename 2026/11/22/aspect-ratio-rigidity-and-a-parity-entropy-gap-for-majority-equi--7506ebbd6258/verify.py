"""Independent finite checks for majority-stable Ferrers matrices and turn-path formulas.
Run: python verify.py. Python standard library only.
"""
from itertools import combinations
from functools import lru_cache
from collections import Counter


def actual_fixed(matrix):
    m=len(matrix); n=len(matrix[0]); deg=m+n-2
    rows=[sum(v) for v in matrix]
    cols=[sum(matrix[i][j] for i in range(m)) for j in range(n)]
    for i in range(m):
        for j in range(n):
            x=matrix[i][j]
            active_neighbors=rows[i]+cols[j]-2*x
            if x and 2*active_neighbors<deg: return False
            if not x and 2*active_neighbors>deg: return False
    return True

@lru_cache(None)
def shapes(m,n):
    if m==0:return ((),)
    return tuple((r,)+tail for r in range(n,-1,-1) for tail in shapes(m-1,r))

def ferrers_matrix(shape,n):
    return [[int(j<r) for j in range(n)] for r in shape]

def from_word(word):
    m=word.count('U');n=word.count('D')
    j=n;rs=[]
    for s in word:
        if s=='U':rs.append(j)
        else:j-=1
    return tuple(rs)

def word_from_shape(shape,n):
    ans=[];old=n
    for r in shape:
        ans.extend('D'*(old-r));ans.append('U');old=r
    ans.extend('D'*old)
    return ''.join(ans)

def turn_valid(word):
    m=word.count('U');n=word.count('D')
    h2=n-m
    for k,s in enumerate(word):
        h2+=2 if s=='U' else -2
        if k+1<len(word) and word[k+1]!=s:
            if s=='U' and h2<2: return False
            if s=='D' and h2>-2:return False
    return True

def insert_two_D(word):
    # insert at first and last D runs; positions are in the original word.
    a=word.index('D');b=word.rindex('D')
    # If first D is after a nonempty initial U run, insert before it.
    # If last D is before final U run, insert after it.
    # Insert one before first D and one after last D, including a=b.
    return word[:a]+'D'+word[a:b+1]+'D'+word[b+1:]

def a(m):
    if m==0:return 1
    seq=[1,2,3]
    for k in range(3,m+1):seq.append(2*seq[-1]-seq[-2]+seq[-3])
    return seq[m]


def words(m,n):
    for pos in combinations(range(m+n),m):
        ind=set(pos)
        yield ''.join('U' if k in ind else 'D' for k in range(m+n))


def main():
    for m in range(1,9):
        for n in range(m,15):
            count=sum(actual_fixed(ferrers_matrix(sh,n)) for sh in shapes(m,n))
            expected=2**m if (n-m)%2==0 else a(m)
            assert count==expected,(m,n,count,expected)
    print('Ferrers classification: 84 partition families OK (m <= 8, n <= 14).')
    nw=0
    for m in range(1,7):
        for n in range(m,10):
            valid=set()
            for w in words(m,n):
                sh=from_word(w)
                assert sh in shapes(m,n)
                assert word_from_shape(sh,n)==w
                isfixed=actual_fixed(ferrers_matrix(sh,n))
                assert turn_valid(w)==isfixed,(m,n,w)
                if isfixed:valid.add(w)
                nw+=1
            if n+2<=11:
                lifted={insert_two_D(w) for w in valid}
                target={w for w in words(m,n+2) if turn_valid(w)}
                assert lifted==target,(m,n,lifted^target)
    print('Turn-path conditions and width+2 bijection checked,',nw,'paths.')
    for m,n in [(2,2),(2,3),(3,3),(3,4),(4,4),(4,5),(5,3),(3,5)]:
        if m*n>20:continue
        total=0
        for bits in range(1<<(m*n)):
            mat=[[(bits>>(i*n+j))&1 for j in range(n)] for i in range(m)]
            if actual_fixed(mat):total+=1
        print('Independent labelled fixed configurations',m,n,total)
    print('All checks passed.')

if __name__=='__main__':main()
