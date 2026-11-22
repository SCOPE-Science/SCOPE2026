# Exact dyadic residue fibers and three-square obstruction density for two-colored binary partitions

## Finding
Let \(b_2(n)\) count partitions of \(n\) into powers of two, with two distinguishable colors for each part. For \(L\ge 11\) and \(0\le j\le7\), put
\[
H_L(j)=\#\{0\le n<2^L:b_2(n)\equiv16j\pmod{128}\}.
\]
Then, simultaneously for all eight residues,
\[
(H_L(0),\ldots,H_L(7))
=2^{L-5}(1,1,1,1,1,1,1,1)+(2,-2,1,3,-1,0,-2,-2).
\]
In particular, for every \(L\ge11\), exactly \(2^{L-5}-2\) indices in the initial dyadic interval satisfy \(b_2(n)\equiv112\pmod{128}\). Moreover, for every real \(X\ge2\),
\[
\#\{0\le n<X:b_2(n)\equiv112\pmod{128}\}
=\frac X{32}+O(1+\log X),
\]
where the implicit constant is absolute. Therefore that residue fiber has **ordinary natural density** \(1/32\). Since \(112\equiv 16\cdot7\pmod{128}\), Legendre's three-square theorem implies
\[
\liminf_{X\to\infty}\frac1X\#\{0\le n<X:b_2(n)\text{ is not a sum of three integer squares}\}\ \ge\ \frac1{32}.
\]
This is a lower bound for the full obstruction set, not a determination of its density.

## Assumptions and scope
All calculations use formal series over \(\mathbb Z\) and exact arithmetic modulo \(128\). Put
\[
B(x)=\prod_{i\ge0}(1-x^{2^i})^{-2}=\sum_{n\ge0}b_2(n)x^n.
\]
The eight residue formulas concern only the targets divisible by \(16\), not all \(128\) residues. They hold at every integer depth \(L\ge11\). We count indices from zero and allow zero coordinates in sums of three squares. The proof of the natural density is separate from, and stronger than, convergence only at dyadic endpoints.

## Proof
**1. Exact binary sections.** The defining product gives
\[
B(x)=(1-x)^{-2}B(x^2).
\]
For \(\varepsilon\in\{0,1\}\), define \(\mathcal C_\varepsilon\sum_{n\ge0}a_nx^n=\sum_{n\ge0}a_{2n+\varepsilon}x^n\). Consequently, for every series \(g\),
\[
\mathcal C_\varepsilon(g(x)B(x))
=\mathcal C_\varepsilon(g(x)/(1-x)^2)B(x).
\]
Represent \(g(x)=\sum_{n\ge0}Q(n)x^n\) using an integer-valued polynomial \(Q(n)=\sum_{j=0}^d a_j\binom nj\), with coefficients modulo \(128\). Vandermonde convolution yields the exact section transform
\[
Q\longmapsto Q_\varepsilon(n)
=\sum_{j=0}^d a_j\binom{2n+\varepsilon+2}{j+2}\pmod{128}.
\]
For the initial multiplier \(g(x)=1\), the two transforms are \(2n+1\) and \(2n+2\), with binomial-basis coefficient tuples \((1,2)\) and \((2,2)\). Reduce subsequent polynomial coefficients modulo \(128\) and delete trailing zero Newton differences. This gives an exact finite-state system.

**2. A reproducible finite closure.** The standalone file `verify.py` performs breadth-first closure from the initial multiplier under both section transforms. It finds exactly \(100\) distinct states, including the initial root; all non-root states have degree at most four. Thus every possible input digit string is accounted for, rather than sampled. Each state emits the constant coefficient of its multiplier. Since section by zero preserves constant coefficients, leading zero digits do not affect the value. Reading the binary expansion of \(n\) from least to most significant digit emits exactly \(b_2(n)\pmod{128}\).

Let \(T\) be the integer \(100\times100\) transition matrix, with one edge for input zero and one for input one, counted with multiplicity. Let \(e\) be the initial-state row and \(u_r\) the zero-one column selecting state outputs \(r\). The resulting exact count is
\[
H_L(r/16)=eT^Lu_r\qquad(r\in\{0,16,\ldots,112\}).
\]
For every such \(r\), the certificate evaluates the integers
\[
eT^{11+k}(T^2-3T+2I)u_r
\quad(0\le k<100)
\]
and finds every one equal to zero. The Cayley–Hamilton theorem for the displayed \(100\)-state matrix then forces zero for **all** \(k\ge0\). Hence \(H_{L+2}(j)=3H_{L+1}(j)-2H_L(j)\) for every \(L\ge11\). The checker also gives the eight exact initial counts at depths \(11\) and \(12\), namely \(64+\delta_j\) and \(128+\delta_j\), for
\[
(\delta_0,\ldots,\delta_7)=(2,-2,1,3,-1,0,-2,-2).
\]
The recurrence proves the asserted formulas at every depth.

**3. Uniform control of shifted dyadic blocks.** For residue \(112\), label a state *stable* if every finite continuation of binary digits produces the same truth value for “output equals \(112\)”. Taking the union of reachable output labels under the two transitions stabilizes after finitely many steps; the finite checker identifies exactly \(37\) unstable states. Let \(v\) be their indicator column. The certificate establishes
\[
eT^7v=10,\qquad eT^{7+k}(T-I)v=0\quad(0\le k<100).
\]
By Cayley–Hamilton, \(eT^Lv=10\) for **every** \(L\ge7\). Consequently among the \(2^L\) choices of the lowest \(L\) bits, only ten can have their target-residue decision changed by *any* choice of more significant bits.

For every integer \(q\ge0\), compare the interval \(q2^L\le n<(q+1)2^L\) with \(0\le n<2^L\). Their low \(L\) bits are identical, and only the ten unstable suffixes can change the target decision. Therefore, uniformly in \(q\) and \(L\ge11\),
\[
\left|\#\{q2^L\le n<(q+1)2^L:b_2(n)\equiv112\pmod{128}\}-\frac{2^L}{32}\right|\le12.
\]
Write every integer interval \([0,N)\) as disjoint, aligned dyadic intervals corresponding to its binary digits. There is at most one block of each length, so the total discrepancy is at most \(2047+12\max(0,\lfloor\log_2 N\rfloor-10)\). This proves the ordinary natural density and logarithmic discrepancy for integer cutoffs; replacing \(N\) by a nearby integer handles real \(X\).

**4. Three squares.** Every positive integer congruent to \(112\pmod{128}\) equals \(16(8m+7)\) for some nonnegative \(m\), hence is excluded by Legendre's three-square theorem. Since all \(b_2(n)\) are positive, the preceding density of the residue fiber yields the lower-density bound.

## Verification
Run `python3 verify.py` in a standard Python 3 environment. The program reconstructs all states from the two stated transforms; verifies all transitions and preservation under leading zeros; independently calculates the first \(16,384\) coefficients using the truncated Euler product; checks all eight histogram initial values and \(800\) Cayley–Hamilton zero evaluations; and verifies the \(100\) further annihilation values for the ten-unstable-suffix invariant. It prints `VERIFY_OK states=100 independent_coefficients=16384 Cayley_Hamilton_probes=900 residue_classes=8 unstable_suffixes=10_from_depth=7 from_depth=11`. Its finite certificates, together with the explicit Cayley–Hamilton reasoning, prove statements for infinitely many indices; brute-force coefficient checks alone do not.

## Relationship to prior work
Sobolewski and Ulas (first posted 29 November 2022) investigate three-square representability of colored binary partitions, establish automaticity of fixed-modulus coefficient residues (Proposition 7.3), and pose their general-color Problem 7.2 and modular Problem 7.4. Their main exact-density results treat color counts \(2^k-1\), excluding two colors. An earlier Gawron–Miska–Ulas study gives valuation properties for two colors, not these exact eight modulo-\(128\) frequencies.

The closest inspected published result, *A positive-density three-square obstruction for two-colored binary partitions*, establishes two constant-residue progressions \(n\equiv36,62\pmod{128}\), and consequently a lower density of \(1/64\); it expressly does **not** claim full residue density. The present result establishes the exact ordinary density \(1/32\) of one obstruction residue, the uniform logarithmic discrepancy, and a complete eight-cell dyadic histogram. The two fixed progressions are compatible with, but do not imply, these stronger claims. Priority outside inspected literature is not certified.

## Limitations
The natural density established here concerns precisely the residue \(112\pmod{128}\), not the union of every three-square-obstructing value, and the eight exact histogram formulas do not cover the remaining \(120\) residues modulo \(128\). The automaton is specified algorithmically rather than by a printed \(100\times100\) matrix; the fully deterministic source code produces that matrix from exact binomial identities and checks all finite certificates. This is a self-review, not independent mathematical validation. An unlocated equivalent in automatic-sequence or partition literature remains possible.

## References
- B. Sobolewski and M. Ulas, *Values of Binary Partition Function Represented by a Sum of Three Squares*, arXiv:2211.16622, first posted 29 November 2022; Results in Mathematics 78 (2023), article 188, DOI: 10.1007/s00025-023-01966-8. https://arxiv.org/abs/2211.16622
- M. Gawron, P. Miska and M. Ulas, *Arithmetic properties of coefficients of power series expansion ...*, Monatshefte für Mathematik 185 (2018), 307–360, DOI: 10.1007/s00605-017-1041-2.
- *A positive-density three-square obstruction for two-colored binary partitions*, published result, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-positive-density-three-square-obstruction-for-two-colored-bina--48027f9dc065/RESULT.md.
- A.-M. Legendre, classical three-square theorem.
