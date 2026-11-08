"""Independent finite diagnostics for cyclic-factor desubstitution.

The finite checks do not replace the symbolic theorem and do not certify
unbounded lengths or bases.
"""
from itertools import product


def fixed_point(base: int, minimum: int) -> str:
    word = '0'
    while len(word) < minimum:
        word = ''.join(c * (base - 1) + ('1' if c == '0' else '0') for c in word)
    return word


def morph(word: str, base: int) -> str:
    return ''.join(c * (base - 1) + ('1' if c == '0' else '0') for c in word)


def canonical(word: str) -> str:
    return min(word[i:] + word[:i] for i in range(len(word)))


def factor_set(word: str, length: int) -> set:
    return {word[i:i+length] for i in range(len(word)-length+1)}


def lie_classes(factors: set, length: int) -> set:
    return {canonical(v) for v in factors if all(v[i:] + v[:i] in factors for i in range(length))}


def check_phase(base: int) -> int:
    blocks = ['0' * (base-2) + '10', '0' * (base-2) + '11']
    phases = {}
    for choices in product(blocks, repeat=3):
        template = ''.join(choices)
        for start in range(len(template)-base+1):
            segment = template[start:start+base]
            phases.setdefault(segment, set()).add(start % base)
    assert all(len(s) == 1 for s in phases.values())
    return len(phases)


if __name__ == '__main__':
    cases = 0
    phase_cases = 0
    for base in range(3, 9):
        phase_cases += check_phase(base)
        length = max(25000, base**5)
        word = fixed_point(base, length)
        limit = min(68, len(word)//80)
        factors_by_length = {}
        for n in range(1, limit+2):
            factors_by_length[n] = factor_set(word, n)
        for n in range(1, limit+1):
            classes = lie_classes(factors_by_length[n], n)
            if n == 1:
                assert len(classes) == 2
            elif n == 2:
                assert len(classes) == 3
            elif 3 <= n <= base:
                assert len(classes) == 4
            elif n == base+1:
                assert len(classes) == (3 if base == 3 else 2)
            elif n >= base+2 and n % base:
                assert not classes, (base, n, classes)
            elif n >= base+2:
                m = n//base
                fm = factors_by_length[m]
                fm1 = factors_by_length[m+1]
                extensions = {canonical(v) for v in fm if all((v+v)[j:j+m+1] in fm1 for j in range(m))}
                images = {canonical(morph(v, base)) for v in extensions}
                assert classes == images, (base, n, classes ^ images)
            cases += 1
        assert len(lie_classes(factors_by_length[2*base], 2*base)) == 3
    print(f'VERIFY_OK bases=3..8 length_tests={cases} phase_words={phase_cases} check=Lie_and_extension_equivalence')
