"""Exact finite-state proof certificate for the second image of synchronous Rule 184.
Run with Python 3.10+ standard library: python3 verify_rule184.py
"""
from collections import deque
from itertools import product

FORBIDDEN = ('1100', '110100')
PROPER_PREFIXES = ('', '1', '11', '110', '1101', '11010')


def local184(a,b,c):
    return (b & c) | (a & (1-b))


def local_two(bits):
    return local184(local184(*bits[:3]), local184(*bits[1:4]), local184(*bits[2:5]))


def nfa_moves():
    moves = [[0,0] for _ in range(16)]
    for v in range(16):
        bits = [(v >> (3-j)) & 1 for j in range(4)]
        for b in (0,1):
            five = bits+[b]
            moves[v][local_two(five)] |= 1 << ((2*v+b)&15)
    return moves


def nfa_advance(mask, bit, moves):
    out = 0
    while mask:
        atom = mask & -mask
        index = atom.bit_length()-1
        out |= moves[index][bit]
        mask -= atom
    return out


def aho_advance(q, bit):
    w = PROPER_PREFIXES[q] + str(bit)
    if any(w.endswith(x) for x in FORBIDDEN):
        return -1
    for j in reversed(range(len(PROPER_PREFIXES))):
        if w.endswith(PROPER_PREFIXES[j]):
            return j
    assert False


def proof_certificate():
    moves = nfa_moves()
    # Pair starts at all 4-bit contexts, and at the zero-prefix forbidding monitor.
    root=( (1<<16)-1, 0)
    queue=deque([root])
    seen={root}
    while queue:
        mask,q=queue.popleft()
        assert mask != 0 and q >= 0
        for b in (0,1):
            nxt = nfa_advance(mask,b,moves)
            nextq=aho_advance(q,b)
            assert (nxt != 0) == (nextq >= 0), (mask,q,b,nxt,nextq)
            if nxt != 0:
                z=(nxt,nextq)
                if z not in seen:
                    seen.add(z)
                    queue.append(z)
    assert len(seen) == 17, len(seen)
    # Every accessible pair is checked against both outgoing letters.
    return seen


def subshift_counts(N):
    C=[0]*(N+1)
    d={'':1}
    for n in range(N+1):
        C[n]=sum(d.values())
        d={v+ch:count for v,count in d.items() for ch in ('0','1') if not any((v+ch).endswith(f) for f in FORBIDDEN)}
    return C


def count_sft(N):
    curr=[0]*6
    curr[0]=1
    ans=[]
    for n in range(N+1):
        ans.append(sum(curr))
        nxt=[0]*6
        for q,num in enumerate(curr):
            for b in (0,1):
                r=aho_advance(q,b)
                if r>=0:
                    nxt[r]+=num
        curr=nxt
    return ans


def brute_second_words(n):
    out=set()
    for x in product((0,1),repeat=n+4):
        yy=[local_two(x[j:j+5]) for j in range(n)]
        out.add(''.join(str(a) for a in yy))
    return out


def check():
    pairs=proof_certificate()
    seq=count_sft(17)
    assert seq == subshift_counts(17)
    assert seq[:12] == [1,2,4,8,15,28,51,92,165,294,522,924],seq[:12]
    # Characteristic polynomial of the six-state suffix adjacency (proved by direct determinant).
    # Denominator (1-z^2-z^3)(1-2z+z^2-z^3)
    p=[1,-2,0,0,1,0,1]
    # Exact characteristic determinant from the labeled prefix automaton.
    from itertools import permutations
    # Polynomial multiplication uses integer coefficient lists in ascending degree.
    def mul(p,q):
        result=[0]*(len(p)+len(q)-1)
        for i,a in enumerate(p):
            for j,b in enumerate(q):
                result[i+j]+=a*b
        return result
    matrix=[[[int(i==j),-(sum(aho_advance(i,b)==j for b in (0,1)))]
             for j in range(6)] for i in range(6)]
    characteristic=[0]*7
    for perm in permutations(range(6)):
        inv=sum(perm[i]>perm[j] for i in range(6) for j in range(i+1,6))
        term=[1]
        for i,j in enumerate(perm):
            term=mul(term,matrix[i][j])
        for i,k in enumerate(term):
            characteristic[i]+=(-1)**inv*k
    assert characteristic==p, characteristic
    # Cayley-Hamilton supplies the recurrence at every length, not just 17.
    # With the first six computed counts, the rational-series numerator is one.
    assert [sum(p[j]*seq[n-j] for j in range(n+1)) for n in range(6)] == [1,0,0,0,0,0]
    # Check exact recurrence through 17 terms
    for n in range(6,18):
        assert sum(p[j]*seq[n-j] for j in range(7)) == 0, (n,seq[n])
    for n in range(1,12):
        got=brute_second_words(n)
        expect={''.join(w) for w in product('01',repeat=n) if all(f not in ''.join(w) for f in FORBIDDEN)}
        assert got == expect,(n,got^expect)
    print('VERIFY_OK pairs=',len(pairs),' brute_lengths=1..11','counts=',seq[:12])

if __name__=='__main__':
    check()
