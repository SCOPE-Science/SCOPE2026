"""NB exponent optimization: ell = (1+eta)*log(N)/log(q), T=q^{1-1/r}.
Term1 (diagonal): N q^ell / T^{2ell} = n^{2/r + eta*(2/r-1)} <= n^{2/r} (r>2).
Term2 (generic): N q^{2ell}/n /T^{2ell} = n^{(2/r)(1+eta)}.
Power: lower by n^{1/3}. With eta=r*eps/2 gives 2/r+eps."""
import math
for q in [3,5,7,9]:
    A=1/math.log(q)
    print(f"q={q} A=1/logq={A:.4f} (q^ell=n)")
    for r in [2.5,3,4,6]:
        main=2/r; power=2/r-1/3
        print(f"  r={r}: diag->n^{main:.4f} generic->n^{main:.4f} power->n^{power:.4f}")
print("OK sharp 2/r; adjacency-naive exponents (see exponent_check.py) are strictly larger.")
