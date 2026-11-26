"""Self-contained finite checks for modal-depth star normal forms.
Run: python verify.py (Python 3.9+, standard library only).
These checks test finite instances; the written proof handles arbitrary parameters.
"""
from itertools import product
from math import comb

def refinement(q,k):
    # Every valuation over a fixed rooted reflexive star, and every pointed world.
    # 0 is root, 1..k leaves. Both color and edges are explicit, not the proposed normal form.
    vals=list(product(range(q), repeat=k+1))
    states=[(v,w) for v in vals for w in range(k+1)]
    def classify(signatures):
        ids={}
        return [ids.setdefault(sig,len(ids)) for sig in signatures]
    parts=classify([v[w] for v,w in states])
    sequence=[len(set(parts))]
    for d in range(1,4):
        previous={(v,w):parts[i] for i,(v,w) in enumerate(states)}
        signatures=[]
        for v,w in states:
            nxt=range(k+1) if w==0 else (w,)
            signatures.append((parts[len(signatures)],frozenset(previous[v,j] for j in nxt)))
        parts=classify(signatures)
        sequence.append(len(set(parts)))
    return sequence

def predicted(q,k):
    if k==0: return [q,q,q,q]
    depth0=q
    depth1=q*sum(comb(q-1,j) for j in range(min(k,q-1)+1))
    depth2=q*sum(comb(q,j) for j in range(1,min(k,q)+1))
    return [depth0,depth1,depth2,depth2]

def check_characterizers(q,k):
    # At the root with nonuniform colors, theta_b := diamond(chi_b and box chi_b)
    # detects leaf support, including potential leaf of same root color.
    for v in product(range(q),repeat=k+1):
        root=v[0]
        leafset=set(v[1:])
        homogeneous= len(set(v)) == 1
        for b in range(q):
            theta=any(v[j]==b and all(v[t]==b for t in (range(k+1) if j==0 else (j,))) for j in range(k+1))
            target=(b in leafset or (homogeneous and root==b))
            assert theta==target,(q,k,v,b,theta,target)

def direct_term_closure_one_atom(k):
    """Enumerate all Boolean modal term functions on the whole fixed star."""
    from collections import deque
    vals=list(product((0,1),repeat=k+1))
    cells=[(v,w) for v in vals for w in range(k+1)]
    n=len(cells)
    mask=(1<<n)-1
    p=sum((v[w]<<i) for i,(v,w) in enumerate(cells))
    seen={0,mask,p}
    frontier=deque(seen)
    def box(t):
        result=0
        for i,(v,w) in enumerate(cells):
            key=vals.index(v)*(k+1)
            indices=(range(k+1) if w==0 else (w,))
            if all(t & (1<<(key+j)) for j in indices): result|=(1<<i)
        return result
    while frontier:
        a=frontier.popleft()
        new=[a^mask,box(a)]
        for b in tuple(seen):new.append(a&b)
        for c in new:
            if c not in seen:
                seen.add(c);frontier.append(c)
    return len(seen)

def main():
    total=0
    for q in (2,4,8):
        for k in range(5 if q<=4 else 4):
            actual=refinement(q,k)
            expected=predicted(q,k)
            assert actual==expected, (q,k,actual,expected)
            check_characterizers(q,k)
            total+=q**(k+1)*(k+1)
            print('q=',q,'k=',k,'depth types=',actual,'OK')
    for k in range(4):
        n=direct_term_closure_one_atom(k)
        expected=2**predicted(2,k)[2]
        assert n==expected,(k,n,expected)
        print('direct_closure k=',k,'term_functions=',n,'OK')
    print('VERIFY_OK',total,'pointed valuation cases')

if __name__=='__main__':main()
