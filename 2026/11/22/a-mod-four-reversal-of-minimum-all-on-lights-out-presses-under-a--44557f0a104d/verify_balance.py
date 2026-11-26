"""Check full all-on affine fibers by exact binary column-syndrome elimination."""
from itertools import product


def fibers(n):
    size = 2*n
    pivots = {}
    kernel = []

    def reduce(syndrome, presses):
        while syndrome:
            lead = syndrome.bit_length()-1
            if lead not in pivots:
                break
            effect, combo = pivots[lead]
            syndrome ^= effect
            presses ^= combo
        return syndrome, presses

    for i in range(size):
        neighborhood = {i, (i-1)%size, (i+1)%size, (i+n)%size}
        assert len(neighborhood) == 4
        syndrome = sum(1 << j for j in neighborhood)
        residue, witness = reduce(syndrome, 1 << i)
        if residue:
            pivots[residue.bit_length()-1] = residue, witness
        else:
            kernel.append(witness)
    assert len(pivots) + len(kernel) == size

    residue, witness = reduce((1 << size)-1, 0)
    assert residue == 0
    result = {witness}
    for relation in kernel:
        result |= {presses ^ relation for presses in result}
    assert len(result) == 1 << len(kernel)
    return result


for n in (20, 24, 28):
    actual = fibers(n)
    expected = {
        sum(1 << i for i in range(2*n) if i%4 in (a, b))
        for a, b in product((0, 2), (1, 3))
    }
    assert actual == expected
    assert {x.bit_count() for x in actual} == {n}
    print(f'n={n}: {len(actual)} all-on patterns, all of weight {n}')
