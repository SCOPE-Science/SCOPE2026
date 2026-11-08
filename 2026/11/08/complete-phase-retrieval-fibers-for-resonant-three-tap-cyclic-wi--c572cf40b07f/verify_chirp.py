"""Exact group-ring certificates for cyclic three-tap phaseless ambiguity.

Run with Python 3 (standard library only): python verify_chirp.py
The universal classification is proved algebraically in RESULT.md; these
checks independently verify the explicit full-spectrogram examples.
"""
from collections import defaultdict

def state(N, exponent, amplitude=1):
    return (int(amplitude), exponent % N)

def products(N, left, right):
    return (left[0] * right[0], (left[1] - right[1]) % N)

def rows(N, values):
    # Three Fourier coefficients of each squared, three-term windowed DFT.
    result = []
    for t in range(N):
        f0, f1, f2 = [values[(t+j) % N] for j in range(3)]
        u = [f0, (3*f1[0], f1[1]), (f2[0], (f2[1]-1) % N)]
        row = []
        for lag in (0,1,2):
            coefficients = defaultdict(int)
            for i in range(3-lag):
                weight, exponent = products(N,u[i],u[i+lag])
                coefficients[exponent] += weight
            row.append(tuple(sorted((k,v) for k,v in coefficients.items() if v)))
        result.append(tuple(row))
    return result

def run(N):
    m = N//2
    # zeta=e^(2 pi i/N), g=(1,3,zeta), rho=1.
    # f_{2j}=zeta^{2j(j-1)}, f_{2j+1}=2 zeta^{2j^2}.
    # h differs by zeta on even indices and by 1 on odd indices.
    f=[]
    h=[]
    for j in range(m):
        even=state(N,2*j*(j-1))
        odd=state(N,2*j*j,2)
        f.extend((even,odd))
        h.extend((state(N,even[1]+1),odd))
    assert f != h
    assert rows(N,f) == rows(N,h)
    return 3*N

if __name__ == '__main__':
    checks = sum(run(N) for N in range(6,42,2))
    print(f'CHIRPED_THREE_TAP_PASS dimensions=18 exact_correlation_rows={checks}')
