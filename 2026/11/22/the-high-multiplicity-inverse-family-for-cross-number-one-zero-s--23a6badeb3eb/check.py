"""Reproducible finite cross-number-one checks over cyclic groups.

This script provides bounded finite checks; the universal theorem is proved separately.
Python 3, standard library only.
"""
from math import gcd


def has_cross_one_zero_sum(sequence, modulus):
    """Exact subset DP for weight=sum gcd(x,modulus)=modulus and sum=0 mod modulus."""
    states = [1] + [0] * modulus
    mask = (1 << modulus) - 1
    for x in sequence:
        weight = gcd(x, modulus)
        old = states[:]
        for w in range(modulus - weight + 1):
            bits = old[w]
            if not bits:
                continue
            rotated = (((bits << x) | (bits >> (modulus - x))) & mask) if x else bits
            states[w + weight] |= rotated
        if states[modulus] & 1:
            return True
    return False


def predicted_family(prime):
    modulus = 2 * prime
    output = set()
    for generator in range(1, modulus, 2):
        if gcd(generator, modulus) != 1:
            continue
        for h in range(1, prime):
            normalized = [(2*h+1) % modulus, (2*h+2) % modulus]
            values = sorted({generator*y % modulus for y in normalized if y not in (0, prime)})
            if len(values) == 1:
                output.add(tuple(sorted((generator,)*(modulus-1) + (values[0],)*(prime-1))))
            else:
                for a in range(prime):
                    output.add(tuple(sorted((generator,)*(modulus-1)
                                            + (values[0],)*a
                                            + (values[1],)*(prime-1-a))))
    return output


def exhaustive_avoiders(modulus):
    """Exhaustively enumerate every nondecreasing multiset at sharp length."""
    length = 3*modulus//2-2
    weights = [gcd(x,modulus) for x in range(modulus)]
    output = set()
    mask = (1 << modulus)-1
    def visit(start,depth,states,terms):
        if depth == length:
            output.add(tuple(terms))
            return
        for x in range(start,modulus):
            wt = weights[x]
            nxt = states[:]
            for w in range(modulus-wt+1):
                bits = states[w]
                if not bits:
                    continue
                rotated = (((bits << x) | (bits >> (modulus-x))) & mask) if x else bits
                nxt[w+wt] |= rotated
            if not nxt[modulus]&1:
                terms.append(x)
                visit(x,depth+1,nxt,terms)
                terms.pop()
    visit(0,0,[1]+[0]*modulus,[])
    return output


def main():
    for p in (3,5,7,11,13):
        family=predicted_family(p)
        expected=(p-1)**2*(p-2)
        assert len(family) == expected, (p,len(family),expected)
        assert all(len(s)==3*p-2 for s in family)
        assert all(not has_cross_one_zero_sum(s,2*p) for s in family)
        supp2=sum(len(set(s))==2 for s in family)
        supp3=sum(len(set(s))==3 for s in family)
        assert supp2 == 2*(p-1)*(p-2)
        assert supp3 == (p-1)*(p-2)*(p-3)
        if p<=7:
            whole=exhaustive_avoiders(2*p)
            assert whole == family,(p,len(whole),len(family),list(whole-family)[:2])
        else:
            whole=None
        print(f'p={p}; construction={len(family)}; support2={supp2}; support3={supp3}; '
              f'full enumeration={len(whole) if whole is not None else "not attempted"}; all checks PASS')

if __name__ == '__main__':
    main()
