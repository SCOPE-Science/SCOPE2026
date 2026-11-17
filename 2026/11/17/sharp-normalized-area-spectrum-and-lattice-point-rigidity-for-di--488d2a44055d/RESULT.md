# Sharp normalized area spectrum and lattice-point rigidity for divisor-parabola polygons

## Finding
For each integer \(h\ge2\), let \(B_h\subset\mathbb R^2\) be the convex hull of \((0,-1)\) and all points \((a,a^2)\) for nonzero integral divisors \(a\mid h\). Write \(A_h\) for its Euclidean area, \(b_h\) for its number of boundary lattice points, and \(i_h\) for its number of interior lattice points. List its positive divisors as \(1=d_1<\cdots<d_k=h\). Then
\[
 b_h=4h,\qquad
 A_h=\frac{4h^3+2-\sum_{j=1}^{k-1}(d_{j+1}-d_j)^3}{3},\qquad
 i_h=A_h-2h+1.
\]
In particular \(A_h\ge h^3+h^2-h+1\), with equality **if and only if \(h\) is prime**.

The set of all subsequential limits of \(A_h/h^3\) as \(h\to\infty\) is exactly the following explicit divisor-spectrum. Let \(\nu=\prod_p p^{\alpha_p}\) range over all *supernatural integers*, with each exponent \(\alpha_p\in\{0,1,2,\ldots,\infty\}\). Set
\[
 D(\nu)=\{d\in\mathbb N:v_p(d)\le\alpha_p\text{ for every prime }p\},
 \qquad K_\nu=\{0\}\cup\{1/d:d\in D(\nu)\}.
\]
List the points of \(K_\nu\) in decreasing order, starting at \(1\) and ending at or converging to \(0\). Define the *cubic gap energy* \(\Phi(\nu)\) as the sum of the cubes of all consecutive gaps. (For finite \(D(\nu)\), include the last gap to \(0\).) The exact limit spectrum is
\[
 \left\{\lim_{j\to\infty}\frac{A_{h_j}}{h_j^3}:h_j\to\infty,\ \text{limit exists}\right\}
 =\left\{\frac43-\frac13\Phi(\nu):\nu\text{ supernatural}\right\}.
\]
Its two sharp endpoints and their **if-and-only-if rigidity criteria** are
\[
 1\le\liminf_{h\to\infty}\frac{A_h}{h^3}
 \le\limsup_{h\to\infty}\frac{A_h}{h^3}
 \le\frac{\pi^2-6}{3},
\]
\[
 \frac{A_{h_j}}{h_j^3}\longrightarrow\frac{\pi^2-6}{3}
 \quad\Longleftrightarrow\quad
 \text{every fixed positive integer eventually divides }h_j,
\]
\[
 \frac{A_{h_j}}{h_j^3}\longrightarrow1
 \quad\Longleftrightarrow\quad
 \text{the least prime divisor of }h_j\text{ tends to infinity}.
\]
Here \(h_j\to\infty\) is assumed in both equivalences. The upper endpoint is attained asymptotically by \(h_j=\operatorname{lcm}(1,\ldots,j)\); the lower by primes. The same asymptotic spectrum and endpoint rigidity hold for \(i_h/h^3\), by the exact lattice-point identity above. As an intermediate example, for any fixed prime \(p\),
\[
 \lim_{a\to\infty}\frac{A_{p^a}}{p^{3a}}
 =\frac43-\frac{(p-1)^3}{3(p^3-1)};
\]
for \(p=2\) this equals \(9/7\), strictly between the endpoints. The primorial parameters \(h_N=\prod_{p\le N}p\) used by the motivating facet construction have the strictly intermediate profile \(\nu=\prod_p p\), and hence the well-defined limit \(4/3-\Phi(\prod_p p)/3\).

## Assumptions and scope
All convex hulls use the standard lattice \(\mathbb Z^2\) and Euclidean planar area; \(h\) is a positive integer at least two, and both positive and negative divisors contribute vertices. The polygons are **exactly** those introduced in Hofscheier–Nill, *Reflexive polytopes can have doubly exponentially many vertices*, arXiv:2611.08819v1, Lemma 4.1. The source establishes their vertices, facet counts and facet lattice-distance divisibility, but not the above sharp area or lattice-point spectrum. The spectral parameter \(\nu\) is a formal collection of prime exponents, not necessarily a finite integer.

## Proof
**1. Exact area and lattice boundary.** By the cited vertex description the upper boundary of \(B_h\) is the horizontal segment from \((-h,h^2)\) to \((h,h^2)\); the lower boundary consists of the two edges from \((0,-1)\) to \((\pm1,1)\) and the straight chords between consecutive divisor points on each half-parabola. The integral of the linear function on \([0,1]\) joining \(-1\) to \(1\) vanishes. Computing the area between the horizontal top and two symmetrical lower chains gives
\[
 A_h=2h^3-\sum_{j=1}^{k-1}(d_{j+1}-d_j)(d_j^2+d_{j+1}^2).
\]
The exact algebraic identity
\[
 (e-d)(d^2+e^2)=\frac23(e^3-d^3)+\frac13(e-d)^3
\]
and telescoping yield the claimed cubic-gap formula.

For a lattice segment with displacement \((\Delta x,\Delta y)\), the number of lattice intervals on it is \(\gcd(|\Delta x|,|\Delta y|)\). The top edge contributes \(2h\). Each half of the lower boundary contributes \(1+\sum_j(d_{j+1}-d_j)=h\), since a consecutive-parabola edge has displacement \((e-d,(e-d)(e+d))\) and lattice length \(e-d\). Thus \(b_h=4h\), and Pick's theorem gives \(i_h=A_h-b_h/2+1\).

Since all positive gaps sum to \(h-1\), strict superadditivity of the cube yields \(\sum_j(d_{j+1}-d_j)^3\le(h-1)^3\), with equality precisely when there is only one gap. This is equivalent to \(h\) having exactly two positive divisors, i.e. to primality. Substitution proves the finite sharp lower area bound.

**2. Reciprocal mesh identity.** Let \(\mathcal D_h\) denote the positive divisors of \(h\). The set \(\{d/h:d\in\mathcal D_h\}\) equals \(\{1/d:d\in\mathcal D_h\}\) because \(d\mapsto h/d\) permutes divisors. Adjoin \(0\), and let \(E_h\) be the sum of cubes of gaps between consecutive points of the resulting finite closed set. Its gap from \(0\) to \(1/h\) contributes \(1/h^3\), so the area formula becomes
\[
 \frac{A_h}{h^3}=\frac43+\frac1{h^3}-\frac13E_h. \tag{1}
\]
If a point splits a positive gap of lengths \(a+b\) into gaps \(a,b>0\), then cubic energy strictly decreases by \(3ab(a+b)\). Every divisor reciprocal set is a subset of the universal reciprocal mesh \(K_\infty=\{0,1,1/2,1/3,\ldots\}\), so its energy is at least
\[
 E_\infty=\sum_{j=1}^\infty\left(\frac1j-\frac1{j+1}\right)^3
 =\sum_{j=1}^\infty\frac1{j^3(j+1)^3}=10-\pi^2. \tag{2}
\]
For the last equality, decompose the summand as
\[
 \frac6j-\frac6{j+1}-\frac3{j^2}-\frac3{(j+1)^2}
 +\frac1{j^3}-\frac1{(j+1)^3},
\]
then telescope the first and last differences and use \(\sum_{j\ge1}j^{-2}=\pi^2/6\). At the other extreme \(E_h\le1\), since all gaps partition \([0,1]\). This establishes the numerical endpoint bounds for all limiting subsequences.

**3. Compactness and realization of the entire limit spectrum.** Given any sequence \(h_j\to\infty\), successive subsequence extraction and a diagonal choice make the indicator of \(d\mid h_j\) eventually constant for each fixed positive integer \(d\). For each prime \(p\), let \(\alpha_p\) be the largest nonnegative exponent eventually dividing all selected \(h_j\), allowing \(\infty\). The stable set of divisors is exactly \(D(\nu)\): every fixed integer has finitely many prime factors, and divisibility by it is the conjunction of finitely many prime-power divisibilities.

To prove convergence of cubic gap energy, fix an integer \(M\). The point sets for \(h_j\) and \(\nu\) eventually agree on all reciprocal points at least \(1/M\). All remaining points lie in \([0,1/M)\). The gap from the smallest common point above the cutoff can change its cube by at most \(3/M\), while the sum of cubed gaps entirely below the cutoff is at most \(1/M^3\). Consequently their energies differ by at most \(3/M+2/M^3\) once these finitely many divisor decisions have stabilized. Letting \(M\to\infty\) proves \(E_{h_j}\to\Phi(\nu)\), then (1) proves the claimed limit.

Conversely, fix any supernatural \(\nu\). For each \(j\), let
\[
 b_j=\prod_{p\le j}p^{\min(\alpha_p,j)}
\]
(where \(\min(\infty,j)=j\)), and choose a prime \(q_j>j\). Put \(h_j=b_jq_j\). Then \(h_j\to\infty\), and for every fixed integer \(d\), eventually \(d\mid h_j\) if and only if \(d\in D(\nu)\). The preceding convergence argument realizes exactly the stated value. This proves both inclusions in the spectrum equality.

**4. Sharpness and endpoint rigidity.** Strict cubic-gap refinement shows that among the reciprocal sets \(K_\nu\), the unique energy minimum is the full mesh \(K_\infty\), and the unique maximum is \(\{0,1\}\). Indeed, omitting a fixed reciprocal \(1/m\) from the full mesh strictly merges neighboring positive gaps, whereas including any reciprocal strictly splits the gap of length one. Equations (1)–(2) therefore give sharp lower and upper normalized-area limits, with equality respectively for the trivial divisor set \(\{1\}\) and full set \(\mathbb N\).

The compactness argument has a stronger consequence. If normalized areas converge to the upper endpoint but some fixed \(m\) fails to divide infinitely many \(h_j\), an extracted divisor-profile subsequence omitting \(m\) would give a strictly smaller limit, contradiction. Conversely, if every \(m\) eventually divides the sequence, the divisor profiles converge to the full mesh, giving the upper limit. This is realized by least common multiples. For the lower endpoint, if the least prime divisor is unbounded then every fixed \(m>1\) eventually fails to divide \(h_j\), giving trivial divisor profile. Conversely, if the least prime divisor does not tend to infinity, some fixed prime divides infinitely many members, producing a nontrivial limiting divisor profile and a limit strictly above one. Primes realize the lower endpoint. Finally, \(i_h=A_h-2h+1\) transfers the spectrum and rigidity to interior lattice-point counts. For \(h=p^a\), the reciprocal gaps form a geometric progression; summing their cubes yields the stated prime-power limit.

## Verification
The standalone file `verify_divisor_area.py` performs an independent integer shoelace-area calculation and independent gcd boundary enumeration for every \(2\le h\le800\). For each it checks the cubic-gap formula, the prime equality criterion, Pick integrality and the full reciprocal-refinement inequalities. It also checks finite approximations to the series in (2), least-common-multiple examples, and prime-power examples: 5,616 checks passed when run from this package. The proof of the infinite spectrum, rigidity and endpoint constants is analytical; no finite experiment substitutes for it.

Reproduce with `python3 verify_divisor_area.py` (standard Python library only). The generated file contains no compiled dependencies or external data.

## Relationship to prior work
Hofscheier and Nill (arXiv:2611.08819v1, 2026-11-06) introduce \(B_h\), prove the full vertex set and \(2\tau(h)+1\) facets, and establish the facet lattice-distance property driving their reflexive-polytope construction. Those ingredients are credited. Their area, complete lattice-point counts, cubic divisor-gap energy, supernatural limit spectrum, and two endpoint rigidity equivalences are not claimed in the inspected relevant sections of that paper. Pick's theorem and ordinary shoelace identities are classical and not claimed as new.

The new geometric content is the **sharp asymptotic normalized-area spectrum**, including the specific \((\pi^2-6)/3\) extremum and both necessary-and-sufficient divisor-profile criteria, for the precise planar building blocks used in the recent doubly exponential facet constructions. A prior result about random convex lattice polygonal lines (Bogachev–Zarbaliev, 2023) concerns a different ensemble and does not imply a theorem for these divisor-selected deterministic polygons.

## Limitations
The classification concerns area and interior lattice-point counts of the **two-dimensional building blocks** \(B_h\). It does not determine the lattice-point count or Euclidean volume of the higher-dimensional reflexive polytopes constructed from them. The supernatural parametrization describes the entire limit set but does not assert that distinct supernatural integers yield distinct numerical values. The elementary exact area formula is not alone a deep theorem; the principal novelty/value rests on the sharp full asymptotic spectrum and rigidity. Historical priority against unindexed divisor-geometry notes or generic cubic mesh-energy results remains a residual literature risk. Independent external mathematical audit has not been performed.

## References
1. J. Hofscheier and B. Nill, *Reflexive polytopes can have doubly exponentially many vertices*, arXiv:2611.08819v1, 2026-11-06, especially Lemma 4.1, Figure 1, and Section 4. https://arxiv.org/abs/2611.08819
2. G. Pick, *Geometrisches zur Zahlenlehre*, Sitzungsberichte des Deutschen Naturwissenschaftlich-Medicinischen Vereines für Böhmen “Lotos” (1899). Used only for the classical lattice-point area identity.
3. L. V. Bogachev and S. M. Zarbaliev, *Inverse Limit Shape Problem for Multiplicative Ensembles of Convex Lattice Polygonal Lines*, Mathematics 11 (2023), 385. https://doi.org/10.3390/math11020385 (background on different polygonal-line limit-shape settings, not a result for \(B_h\)).
