"""Independent face-number checks and exact replay of the integral Morse certificate.

Run in the directory containing morse_certificate.cpp and morse_boundary.txt:
    python3 verify.py
Requires a C++17 compiler and SymPy for the exact Smith normal form.
"""
from collections import Counter
from functools import lru_cache
from pathlib import Path
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
import hashlib
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
N = 12
edges = set()
for i in range(N):
    for a,b in ((i,(i+1)%N),(i,N+i),(N+i,N+(i+5)%N)):
        edges.add(tuple(sorted((a,b))))
assert len(edges) == 36
nbr = [0]*24
for a,b in edges:
    nbr[a] |= 1 << b
    nbr[b] |= 1 << a

@lru_cache(None)
def matching_polynomial(vertex_mask):
    if not vertex_mask:
        return (1,)
    bit = vertex_mask & -vertex_mask
    vertex = bit.bit_length() - 1
    remaining = vertex_mask ^ bit
    out = list(matching_polynomial(remaining))
    candidates = remaining & nbr[vertex]
    while candidates:
        bit2 = candidates & -candidates
        candidates -= bit2
        smaller = matching_polynomial(remaining ^ bit2)
        for j, coefficient in enumerate(smaller):
            if len(out) <= j+1:
                out.extend([0]*(j+2-len(out)))
            out[j+1] += coefficient
    return tuple(out)

f = matching_polynomial((1 << 24)-1)
EXPECTED_F = (1,36,558,4884,26613,93888,216228,320256,293436,155024,41832,4608,120)
assert f == EXPECTED_F, (f, EXPECTED_F)
assert sum(f) == 1157484
reduced_euler = sum((-1)**(j-1) * value for j, value in enumerate(f))
assert reduced_euler == -92
print('NAURU_INDEPENDENT_MATCHING_POLYNOMIAL_PASS')
print('f_vector_by_matching_size=',list(f))

with tempfile.TemporaryDirectory() as temp:
    executable = Path(temp) / 'morse_certificate'
    subprocess.run(['g++','-O2','-std=c++17',str(ROOT/'morse_certificate.cpp'),'-o',str(executable)],check=True,timeout=60)
    completed = subprocess.run([str(executable)],check=True,capture_output=True,timeout=120)
    live = completed.stdout
    expected = (ROOT/'morse_boundary.txt').read_bytes()
    assert live == expected, 'The recorded integral boundary differs from replay.'
    report = completed.stderr.decode('utf-8')
    assert 'ACYCLICITY_PASS hasse=8344008 visited=1157484' in report, report
    assert 'NAURU_DISCRETE_MORSE_PASS' in report, report
    print(report.strip())
    print('NAURU_REPLAYED_BOUNDARY_SHA256=',hashlib.sha256(live).hexdigest())

lines = expected.decode('ascii').strip().splitlines()
r,c = map(int,lines[0].split())
assert (r,c) == (132,40)
rows = [list(map(int,line.split())) for line in lines[1:]]
assert len(rows)==r and all(len(row)==c for row in rows)
A = Matrix(rows)
assert sum(1 for a in A if a != 0) == 336
assert max(abs(int(a)) for a in A) == 2
D = smith_normal_form(A,domain=ZZ)
diagonal = [abs(int(D[i,i])) for i in range(min(D.shape))]
assert Counter(diagonal) == Counter({1:34,0:6}), Counter(diagonal)
assert r-34==98 and c-34==6
assert (-1)**7*98+(-1)**8*6 == reduced_euler
print('NAURU_INTEGRAL_SMITH_PASS: 34 unit factors and 6 zero factors')
print('NAURU_HOMOTOPY_WEDGE_PASS: 98 S7 plus 6 S8')
