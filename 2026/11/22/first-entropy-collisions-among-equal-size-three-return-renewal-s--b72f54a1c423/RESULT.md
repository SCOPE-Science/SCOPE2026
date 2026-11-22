# First entropy collisions among equal-size three-return renewal shifts

## Finding
For three-return bouquet edge shifts of a fixed vertex size, topological entropy first ceases to distinguish the length multiset at **nine vertices**: the unique collision is \((1,4,6)\) versus \((2,2,7)\). Both have entropy \(\log\alpha\), where \(\alpha\) is the unique root greater than one of \(x^3-x^2-1=0\). When directed self-loops are excluded, the first collision instead occurs at **eleven vertices**, uniquely between \((2,5,6)\) and \((3,3,7)\), both of entropy \(\log\beta\) with \(\beta^3-\beta-1=0\). Every displayed shift is mixing, yet the members of either pair have different periodic-point counts and are not topologically conjugate.

## Assumptions and scope
For integers \(1\le a\le b\le c\), at most one of which equals one, form a finite directed graph \(R(a,b,c)\) by identifying exactly one base vertex of three otherwise disjoint, consistently oriented directed cycles of lengths \(a,b,c\). The cycles of equal length, if any, have distinct internal vertices and edges. There are no parallel directed edges, and the resulting graph has exactly \(N=a+b+c-2\) vertices and \(N+2\) edges. Write \(X_{a,b,c}\) for its **two-sided edge shift** and \(\sigma\) for the left shift. The loopless subfamily imposes \(a\ge2\). The first-collision statements compare different unordered triples only **at equal vertex order** within these classes, not arbitrary strongly connected graphs or systems of different orders. Standard definitions of topological entropy and the Artin–Mazur zeta function apply.

## Proof
**Entropy and zeta formula.** Remove the common base vertex. Every first-return path to that vertex is one of the three prescribed oriented petals. Thus its first-return series is \(z^a+z^b+z^c\). A decomposition of closed walks into first returns, or equivalently a Schur-complement evaluation of the graph's adjacency determinant, gives
\[
\det(I-zA_{a,b,c})=1-z^a-z^b-z^c,\qquad
\zeta_{X_{a,b,c}}(z)=\frac1{1-z^a-z^b-z^c}.
\]
The adjacency matrix is irreducible because the graph is strongly connected. Consequently its Perron root \(\lambda_{a,b,c}>1\) is the unique solution greater than one of
\[
\lambda^{-a}+\lambda^{-b}+\lambda^{-c}=1,
\qquad h_{\mathrm{top}}(X_{a,b,c})=\log\lambda_{a,b,c}.
\]
Strict decrease of the left side for positive \(\lambda\) proves uniqueness; its value at one is three and its limit at infinity zero. The edge shift is mixing exactly when \(\gcd(a,b,c)=1\), by the period criterion for irreducible edge shifts.

**Two exact equalities.** With \(P_{a,b,c}(x)=x^c-x^{c-a}-x^{c-b}-1\), direct factorization gives
\[
\begin{aligned}
P_{1,4,6}(x)&=(x+1)(x^2-x+1)(x^3-x^2-1),\\
P_{2,2,7}(x)&=(x+1)(x^3-x+1)(x^3-x^2-1),\\
P_{2,5,6}(x)&=(x+1)(x^2-x+1)(x^3-x-1),\\
P_{3,3,7}(x)&=(x^3-x-1)(x^4+x^2-x+1).
\end{aligned}
\]
Each pair therefore has the same unique Perron root and the entropies claimed. The two first-pair graphs have \(N=9\), the two second-pair graphs have \(N=11\), and every displayed triple has gcd one.

**Sharp uniqueness at smaller orders.** To make the finite classification an exact proof, enumerate all nondecreasing integer triples with \(a+b+c=N+2\), admitting at most one \(1\). In the loopless case impose \(a\ge2\). For any two candidates, each polynomial \(P_{a,b,c}\) has exactly one real zero greater than one; their entropies coincide if and only if their monic greatest common divisor over \(\mathbb Q[x]\) has a real zero in \((1,\infty)\). The attached standalone `check_renewal.py` computes these gcds using exact rational polynomial long division and counts their real zeros in \((1,\infty)\) by a rational Sturm chain, with sign variations at one and positive infinity. It tests **every pair**, including those sharing non-Perron roots. For the loop-allowed class through \(N=9\), it checks 82 same-order pairs, finding only \((1,4,6),(2,2,7)\) at \(N=9\). In the loopless class through \(N=11\), it checks 69 pairs, finding only \((2,5,6),(3,3,7)\) at \(N=11\). The explicit finite loops and exact algebra in the included script constitute a fully reproducible finite exhaustion—not an extrapolation from sampling. In particular there is no earlier entropy collision in either family, and each boundary collision is unique.

**Nonconjugacy.** The equal-entropy shifts have different rational zeta functions by their displayed first-return polynomials. In the first pair, one shift has a fixed point from its length-one loop while the other has none. In the loopless pair, \(X_{2,5,6}\) has a period-two orbit but \(X_{3,3,7}\) has none. Counts of shift-periodic points are conjugacy invariants; hence neither pair is conjugate.

## Verification
Run `python3 check_renewal.py` in the extracted package. It uses only Python's standard library, exact rational numbers, Euclidean polynomial gcds, and Sturm sign variations, with no external data or network access. Its asserted output includes 82 loop-allowed pair comparisons through nine vertices, 69 loopless comparisons through eleven vertices, both unique boundary pairs, and exact common cubic divisibility. The four factorizations above can also be expanded and checked by hand. All roots are selected by the explicit \(\lambda>1\) condition; no near-equality of floating-point approximations is used to certify the coincidences.

## Relationship to prior work
Klech, *Generating Functions and the Entropy Hierarchy of Strongly Connected Digraphs* (arXiv:2609.17334v1), develops the first-return entropy equation and establishes that entropy is a complete isomorphism invariant for its specific class of strongly connected directed graphs with \(N+1\) edges. The present class has exactly \(N+2\) edges, and the new result is a sharp **failure** of entropy rigidity, not a purported new proof of the first-return identity. Wu and Zhang, *Generating Forbidden Words and Measures of Maximal Entropy for Subshifts* (arXiv:2611.03758v1), study forbidden-word and maximal-entropy-measure structure in general subshifts, not the first equal-entropy nonconjugate three-return pairs. Known general examples of equal-entropy nonconjugate shifts are not claimed as new; the assertion is restricted to these smallest equal-order renewal bouquets.

## Limitations
The sharp thresholds are restricted to bouquets formed by **three** internally disjoint directed cycles sharing one hub, with nondecreasing lengths and no duplicated length-one loop. The theorem does not classify four-or-more return petals, arbitrary irreducible shifts of finite type, unequal graph orders, or all entropy collisions above the two cutoffs. The result has undergone self-review only; an independent audit has not been performed. Historical priority of the precise small-size equal-entropy census remains subject to external expert review.

## References
1. Rostislav Klech, *Generating Functions and the Entropy Hierarchy of Strongly Connected Digraphs*, arXiv:2609.17334v1 (first public 2026-09-15), https://arxiv.org/abs/2609.17334 .
2. Xinxing Wu and Xu Zhang, *Generating Forbidden Words and Measures of Maximal Entropy for Subshifts*, arXiv:2611.03758v1 (first public 2026-11-02), https://arxiv.org/abs/2611.03758 .
3. Douglas Lind and Brian Marcus, *An Introduction to Symbolic Dynamics and Coding*, Cambridge University Press, second edition (standard edge-shift zeta, entropy and mixing facts).
