# Minimum unimodular zero counts for reciprocal Littlewood polynomials, even degrees 8–24

## Context
Borwein, Erdélyi and Littmann posed the question of determining Z_L(N), the
minimum number of modulus-one zeros of a reciprocal Littlewood polynomial of
degree N. Finite lower bounds exist (Mercer, Mukunda, Drungilas: >=4 for even
N>=14) and Bedert proved Z_L(N)->infinity, but no exact Z_L(N) values with
extremal witnesses were tabulated for small even degrees. This record supplies
the first exact table over the contiguous even interval 8..24.

## Definitions
Fix even degree N=2m. A reciprocal Littlewood polynomial is
P(z)=a_0+a_1 z+...+a_N z^N with a_n in {+1,-1} and a_n=a_{N-n}.
Define Z(P)=#{z:|z|=1, P(z)=0} counted with multiplicity, and
Z_L(N)=min Z(P) over the reciprocal class.

## Result (headline claim)
For even N=8,10,...,24:

| N | Z_L(N) | #minimizers (a_0=+1 halves) | witness full string a_0...a_N |
|---|--------|-----------------------------|-------------------------------|
| 8 | 2 | 2 | + + + + − + + + + |
| 10 | 2 | 2 | + + + + + − + + + + + |
| 12 | 2 | 2 | + + + + + + − + + + + + + |
| 14 | 6 | 22 | + + + + + + + − + + + + + + + |
| 16 | 4 | 6 | + + + + + + + − + − + + + + + + + |
| 18 | 4 | 2 | + + + + + + + + − − − + + + + + + + + |
| 20 | 6 | 12 | +^10 − +^10 |
| 22 | 6 | 12 | +^11 − +^11 |
| 24 | 6 | 8 | +^12 − +^12 |

(+ is +1, − is −1; +^k is k plus-ones. Each string is palindromic.)
In particular the sequence is non-monotone: spike Z_L(14)=6, dip
Z_L(16)=Z_L(18)=4. All counts are even. Full zero-count histograms per N are
in `output/artifacts/zl_table.json` (keys "dist").

## Proof / evidence
Reduction lemma (proved): Write x=cos θ. Then
P(e^{iθ})=e^{imθ} U(x), U(x)=c_0+sum_{k=1}^m c_k T_k(x),
with c_0=a_m, c_k=2a_{m-k}, T_k the Chebyshev polynomial (integer
coefficients). Hence e^{iθ} (θ in (0,π)) is a zero of P iff x=cos θ in (-1,1)
is a zero of U, with the same multiplicity. Since P(1) and P(-1) are sums of
N+1=2m+1 (odd) many ±1 terms, both are odd integers hence nonzero: ±1 are
never zeros. So every unit-circle zero lies in a conjugate pair e^{±iθ}, and
Z(P)=2×sum_{x in (-1,1)} mult_U(x); in particular Z(P) is always even.
Negating all coefficients preserves zeros, so fixing a_0=+1 and enumerating
the 2^m halves (a_1,...,a_m) covers the class exhaustively.

Counting (exact, auditable): U has exact integer coefficients in the Chebyshev
basis with Fraction arithmetic. Distinct roots in (-1,1): exact Sturm sequence
V(-1)-V(+1) (endpoints verified nonzero per polynomial). Total multiplicity:
iterate U <- gcd(U,U') and accumulate distinct counts (multiplicity ladder).
Exhaustion over the full 2^m half-strings per N (16+32+...+4096=8176
polynomials, a_0=+1 canonical) proves minimality: the census log records every
half-string's exact count, so no reciprocal polynomial of that degree attains
fewer. Cross-check per polynomial by independent numeric roots recount agrees
in all 8176 cases (0 mismatches).

Independent audit: the auditor re-ran the shipped stdlib-only replay
(REPLAY OK 9/9) and wrote an independent from-scratch Fraction
Chebyshev+Sturm+gcd implementation that exhaustively re-enumerated all halves
for every N=8..24, reproducing the minima, minimizer counts, and full
histograms exactly with histogram sums equal to 2^m.

## Limitations
Even degrees 8..24 and reciprocal Littlewood class only. Minimality is
certified exhaustion (exact arithmetic), not an analytic lower-bound proof.
No claim beyond N=8..24, no closed-form bound, no statement about
non-reciprocal or odd-degree classes.

## Reproducibility
- `output/artifacts/zl_table.json`: minima, histograms, witnesses, mismatch=0 logs.
- `output/artifacts/replay.py`: stdlib-only (Fraction, no numpy) exact recount
  of all nine witnesses from embedded strings. Run:
  `python3 output/artifacts/replay.py` → REPLAY: OK (9/9).

## References
- B. Bedert, On the zeros of reciprocal Littlewood polynomials,
  arXiv:2312.04454 (poses Z_L(N) question; proves Z_L(N)->infinity; surveys
  Mercer/Mukunda/Drungilas finite bounds; no exact table).
- T. Erdélyi, Do flat skew-reciprocal Littlewood polynomials exist?,
  arXiv:2001.08151 (flat near-skew-reciprocal existence; different symmetry).
- K.-U. Schmidt, On a problem due to Littlewood concerning polynomials with
  unimodular coefficients, arXiv:1302.2766 (L4 limits 2/pi, 4/pi^2; different
  statistic).
- D. Hokken, Counting (skew-)reciprocal Littlewood polynomials with square
  discriminant, arXiv:2301.05656 (discriminant asymptotics; different invariant).
