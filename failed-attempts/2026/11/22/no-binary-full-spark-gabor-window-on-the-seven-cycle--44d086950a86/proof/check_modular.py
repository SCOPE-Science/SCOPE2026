"""Finite-field cross-check using direct Gaussian elimination.

The characteristic-zero proof is in check_exact.py; modular ranks are a
separately implemented arithmetic check and are not a replacement for it.
Run: python proof/check_modular.py
"""
import json
from pathlib import Path

N = 7
Q = 998244353
GENERATOR = 3
WITNESSES = json.loads(Path(__file__).with_name('witnesses.json').read_text(encoding='utf-8'))['witnesses']


def rank_over_field(matrix):
    m = [row[:] for row in matrix]
    rank = 0
    for col in range(len(m[0])):
        pivot = next((i for i in range(rank,len(m)) if m[i][col] != 0), None)
        if pivot is None:
            continue
        m[pivot],m[rank] = m[rank],m[pivot]
        scale = pow(m[rank][col], Q-2, Q)
        for i in range(rank+1,len(m)):
            factor = m[i][col]*scale % Q
            for j in range(col,len(m[0])):
                m[i][j] = (m[i][j] - factor*m[rank][j]) % Q
        rank += 1
        if rank == len(m):
            break
    return rank


def main():
    primitive = pow(GENERATOR, (Q-1)//N, Q)
    assert pow(primitive,N,Q) == 1 and primitive != 1
    roots = [pow(primitive,j,Q) for j in range(1,N)]
    assert len(set(roots)) == N-1
    for r in WITNESSES:
        mask, cols = r['mask'], r['columns']
        g = [1]+[-1 if (mask >> (j-1)) & 1 else 1 for j in range(1,N)]
        rank_list = []
        for z in roots:
            powers = [pow(z,j,Q) for j in range(N)]
            mat = []
            for x in range(N):
                row = []
                for col in cols:
                    a,b = divmod(col,N)
                    row.append(g[(x-a)%N]*powers[b*x%N] % Q)
                mat.append(row)
            rank_list.append(rank_over_field(mat))
        assert all(v < N for v in rank_list), (mask, rank_list)
        print(f'mask={mask:2d}: ranks at six primitive roots {rank_list}')
    print('PASS: all nine witnesses are singular at every primitive seventh root in F_998244353.')

if __name__ == '__main__':
    main()
