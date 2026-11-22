"""Brute-force exact finite-graph majority dynamics (standard Python, no dependencies).

The wheel has n labelled rim sites 0..n-1 and hub n. On a tie a vertex keeps
its current bit. Every one of 2**(n+1) states is evaluated, n = 3,...,17.
"""

def build_neighbors(n):
    nbr = []
    for i in range(n):
        nbr.append(((i-1)%n, (i+1)%n, n))
    nbr.append(tuple(range(n)))
    return nbr


def step(n, bits, nbr):
    out=0
    for i, neighbors in enumerate(nbr):
        ones=sum((bits>>j)&1 for j in neighbors)
        if ones*2 > len(neighbors) or (ones*2==len(neighbors) and ((bits>>i)&1)):
            out |= 1<<i
    return out


def count(n):
    nbr=build_neighbors(n)
    fixed=period2=flip0=still0=0
    for bits in range(1<<(n+1)):
        nxt=step(n,bits,nbr)
        if step(n,nxt,nbr)!=bits:
            continue
        if nxt==bits:
            fixed+=1
        else:
            period2+=1
            if ((bits>>n)&1)==0:
                if ((nxt>>n)&1)==1:
                    flip0+=1
                else:
                    still0+=1
    assert period2%2==0
    return fixed, period2//2, flip0, still0


def main():
    total=0
    for n in range(3,18):
        fixed,cycles,flips,static0=count(n)
        assert fixed==2
        assert static0 == (2 if n%2==0 else 0)
        assert cycles==flips+(2 if n%2==0 else 0)
        total+=1<<(n+1)
        print(f"n={n:02d} fixed={fixed} primitive_two_cycles={cycles} hub_flip={flips} hub_static_0_states={static0}")
    print(f"fully_enumerated_initial_states={total}")

if __name__=='__main__':
    main()
