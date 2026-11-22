# Sharp triple-covering cutoff for hyperbolic sieve images

## Finding
Fix an odd prime \(p\) and any \(N\in\mathbb F_p^\times\). For a nonzero coefficient \(a\in\mathbb F_p^\times\), let
\[
H_a(N;p)=\{ax+N/x:x\in\mathbb F_p^\times\}.
\]
There exist **three pairwise distinct nonzero coefficients** \(a,b,c\) with
\[
H_a(N;p)\cup H_b(N;p)\cup H_c(N;p)=\mathbb F_p
\]
if and only if
\[
p\in\{5,7,11,13,17,19,23,29,31,37,41,43,47,53,61,73\}.
\]
This criterion holds for **every fixed** \(N\ne0\): the list does not depend on \(N\). In particular, \(73\) is the largest prime at which a three-image cover exists, and none exists at any prime \(p\ge79\).

At the extremal prime \(p=73\), every covering triple has the precise form
\[
\{4Na,4Nb,4Nc\}=\{s,8s,64s\}
\quad\text{for some nonzero square }s\in\mathbb F_{73}.
\]
There are exactly **12 distinct unordered** such normalized triples. The elements \(1,8,64\) have multiplicative order-three symmetry, so the 36 nonzero squares produce 12 triples, each repeated three times.

For completeness, the exact number \(T(p)\) of unordered covering triples of normalized parameters \(\{4Na,4Nb,4Nc\}\) for every odd prime \(p<149\) is:

| \(p\) | \(T(p)\) | \(p\) | \(T(p)\) | \(p\) | \(T(p)\) |
|---:|---:|---:|---:|---:|---:|
| 3 | 0 | 5 | 4 | 7 | 16 |
| 11 | 60 | 13 | 92 | 17 | 152 |
| 19 | 153 | 23 | 176 | 29 | 224 |
| 31 | 155 | 37 | 168 | 41 | 120 |
| 43 | 84 | 47 | 115 | 53 | 52 |
| 59 | 0 | 61 | 60 | 67 | 0 |
| 71 | 0 | 73 | 12 | 79 | 0 |
| 83 | 0 | 89 | 0 | 97 | 0 |
| 101 | 0 | 103 | 0 | 107 | 0 |
| 109 | 0 | 113 | 0 | 127 | 0 |
| 131 | 0 | 137 | 0 | 139 | 0 |

## Assumptions and scope
Only **prime fields of odd characteristic** are considered; \(N\), \(a\), \(b\), \(c\) are nonzero modulo \(p\), and the three coefficients must be distinct. For composite or prime-power coefficient rings this theorem makes no assertion. The count is of unordered triples, without identifying them up to further automorphisms. The base set \(H_a\) is the full image for nonzero inputs; no primitive-root restriction on coefficients is imposed.

## Proof
**Step 1 (exact discriminant criterion).** For \(t\in\mathbb F_p\), the equation \(t=ax+N/x\) with \(x\ne0\) is equivalent to \(a x^2-tx+N=0\), whose roots, if any, are automatically nonzero. Put \(A=4aN\). The quadratic formula thus gives
\[
t\in H_a(N;p)\quad\Longleftrightarrow\quad
\chi(t^2-A)\in\{0,1\},
\]
where \(\chi\) is the quadratic character with \(\chi(0)=0\). As \(a\) ranges over \(\mathbb F_p^\times\), so does \(A\), bijectively for every fixed \(N\ne0\).

**Step 2 (uniform large-prime exclusion).** Fix three distinct \(A,B,C\in\mathbb F_p^\times\) and let \(U\) count the targets \(t\in\mathbb F_p\) for which all three characters \(\chi(t^2-A),\chi(t^2-B),\chi(t^2-C)\) equal \(-1\). Define
\[
8M=\sum_{t\in\mathbb F_p}(1-\chi(t^2-A))(1-\chi(t^2-B))(1-\chi(t^2-C)).
\]
Away from the at most six zeros of the three discriminants, the summand divided by eight equals the indicator of being uncovered. At any discriminant zero its contribution to \(M\) is at most \(1/2\); hence \(U\ge M-3\).

For each nonzero \(A\), the standard quadratic-character sum is
\[
\sum_t\chi(t^2-A)=-1.
\]
For distinct nonzero \(A,B\), the smooth projective curve
\(y^2=(t^2-A)(t^2-B)\) has genus one and two rational points at infinity; if its Frobenius trace is \(\tau_{AB}\), then
\[
\sum_t\chi((t^2-A)(t^2-B))=-1-\tau_{AB},
\qquad |\tau_{AB}|\le2\sqrt p.
\]
Likewise, the squarefree sextic \(y^2=(t^2-A)(t^2-B)(t^2-C)\) has a smooth genus-two model and two rational points at infinity, giving
\[
\sum_t\chi((t^2-A)(t^2-B)(t^2-C))=-1-\tau_{ABC},
\qquad |\tau_{ABC}|\le4\sqrt p.
\]
Expanding the product and applying the Weil bounds yields
\[
8M=p+1-\tau_{AB}-\tau_{AC}-\tau_{BC}+\tau_{ABC}
\ \ge p+1-10\sqrt p,
\]
and therefore
\[
U\ge\frac{p-23-10\sqrt p}{8}.
\]
The right side is strictly positive for all primes \(p\ge149\) (indeed, \(149-23>10\sqrt{149}\), and the difference increases thereafter). Consequently, no three distinct nonzero coefficients cover \(\mathbb F_p\) for \(p\ge149\).

**Step 3 (finite exhaustive census).** For each odd prime \(p<149\), enumerate all \(A\in\{1,\dots,p-1\}\) and form the bitmask
\[
B_A=\{t\in\mathbb F_p:\chi(t^2-A)=-1\}.
\]
For each strictly increasing triple \(A<B<C\), test the exact condition
\(B_A\cap B_B\cap B_C=\varnothing\). The included standalone `verify.py` enumerates all such triples, using only integer arithmetic; it independently rebuilds every \(B_A\) from the direct image \(H_{A/(4N)}(N;p)\) with \(N=1\), and checks equality of the two constructions before counting. The asserted table contains **all** primes below 149, not a sample. Its nonzero entries give precisely the stated prime list.

**Step 4 (rigidity at the largest prime).** At \(p=73\), the exhaustive census returns exactly the 12 triples \(\{s,8s,64s\}\) with \(s\) a nonzero square; the checker independently forms that predicted orbit and asserts set equality against the complete census. Since \(8^3\equiv1\pmod{73}\) and \(8\not\equiv1\), each distinct triple has exactly three square representatives. Thus both the count and complete extremal classification follow. Together with Step 2 this proves the theorem. \(\square\)

## Verification
Execute `python3 verify.py` with Python 3 and no dependencies beyond the standard library. It computes all odd primes below 149 by trial division, checks every normalized coefficient's discriminant-complement mask against a direct inverse-input evaluation of its hyperbolic image, enumerates all unordered triples and their intersection masks, compares every count to the displayed table, and checks equality of the full extremal set at 73 to the 12 predicted triples. It prints `VERIFY_OK` only if every check succeeds. These are finite exhaustive checks for the finite region; the Hasse–Weil argument, not extrapolation from them, handles all larger primes.

## Relationship to prior work
Stănică, Mulder and Hittmeir (2026, arXiv:2606.13018) defined and analyzed these image sets and proved exact two-image formulas and a general \(k\)-target asymptotic bound (Theorem 5.1). That bound does not supply the exact triple-covering cutoff or the complete exceptional coefficient shape at 73. Stănică (2026, arXiv:2611.06580) studies primitive-root pair trace selection and factorization improvements, rather than triple-image covering.

A published classification of covering finite fields by three **translates of the square set** treats whether \(\mathbb F_p=\bigcup_i(A_i+Q_0)\). Our equivalent square-domain condition asks only whether \(Q_0\subseteq\bigcup_i(A_i+Q_0)\), with \(Q_0\) the squares including zero; these are different claims, and the classification of whole-field covers has no examples for \(p=73\). Another prior result about threefold sums of points on the split modular hyperbola concerns **three summands in a two-dimensional group**, not three one-dimensional projection images in a union. Neither directly yields the stated sharp 73 threshold.

## Limitations
The proof does not address extension fields, fixed primitive-root patterns, or algorithmic performance improvements. The finite count is certified by an exhaustive, independently cross-checked program, not by a closed symbolic formula for all exceptional primes. No claim of independent mathematical review or exhaustive historical novelty is made; unindexed prior arithmetic-combinatorial treatments of restricted square covers remain a possible overlap risk.

## References
1. P. Stănică, E. Mulder and M. Hittmeir, *Multi-target hyperbolic sieves and elliptic trace obstructions*, arXiv:2606.13018v1 (first public 11 June 2026), https://arxiv.org/abs/2606.13018. Sections 3–5, Theorem 5.1 and appendix compared.
2. P. Stănică, *Improved deterministic integer factorization by quadratic-image sieving*, arXiv:2611.06580v1 (first public 4 November 2026), https://arxiv.org/abs/2611.06580. Sections 1–2 compared.
3. *Complete affine-square orbit spectrum of three-shift quadratic-residue covers* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-complete-affine-square-orbit-spectrum-of-three-shift-quadratic-r--3e8343da37ce/RESULT.md. Full result and proof compared.
4. *Sharp three-sum covering of the split modular hyperbola over finite fields* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-sharp-three-sum-covering-of-the-split-modular-hyperbola-over-fin--02aca6c7a46d/RESULT.md. Full result and proof compared.
5. Hasse–Weil bound for smooth projective curves over finite fields, in the form \(|\#C(\mathbb F_p)-(p+1)|\le 2g\sqrt p\).
