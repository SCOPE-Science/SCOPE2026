# Sharp second-Specht endpoint projection norms from short-cycle avoidance

## Finding

For every integer \(n\ge4\), let \(G=S_n\) and let \(E_n\subset C(G;\mathbb R)\) be the span of all real matrix coefficients of the irreducible Specht representation indexed by \((n-2,2)\). Let \(d_n=n(n-3)/2\). For \(m\ge0\), let \(q_m\) be the proportion of permutations of \(m\) letters with no cycles of length one or two, with \(q_0=1\). The **minimum norm among all bounded linear projections** from \(C(G;\mathbb R)\), in the supremum norm, onto \(E_n\) is
\[
\boxed{\lambda(E_n)=n(n-3)\left(q_{n-1}+\frac12q_{n-2}\right).}
\]
The unique projection commuting with both left and right translations is the central Fourier projection \(P_n\); it attains this minimum. Its norming inputs are classified explicitly below. The same minimum holds over complex scalars.

The forbidden-short-cycle probabilities have the exact finite formula
\[
\boxed{q_m=\sum_{a,b\ge0:\,a+2b\le m}\frac{(-1)^{a+b}}{a!\,2^b b!}.}
\]
Consequently
\[
\boxed{\lim_{n\to\infty}\frac{\lambda(E_n)}{n(n-3)}=\frac{3}{2e^{3/2}}.}
\]
The normalized error converges more rapidly than any fixed geometric rate, as quantified in the proof. Thus the sharp constant has quadratic growth, unlike the linear-growth standard Specht block.

## Assumptions and scope

The finite set \(G\) has the uniform/counting supremum norm; changing counting to normalized measure does not change that norm. A bounded projection onto \(E_n\) means a linear map \(T:C(G;\mathbb R)\to E_n\) whose restriction to \(E_n\) is the identity. This is an **absolute** (not relative) projection constant of the stated concrete function subspace. The real Specht module of shape \((n-2,2)\) exists and is irreducible for every \(n\ge4\). Its coefficient space has dimension \(d_n^2\). A cycle of length one is a fixed letter; a cycle of length two is a transposition in the disjoint-cycle decomposition, not an arbitrary transposition appearing in a factorization.

Write \(F(g)\) for the number of fixed letters of \(g\), and \(T_2(g)\) for the number of disjoint two-cycles. The character of the displayed Specht module, denoted \(\chi_n\), is real and invariant under inversion.

## Proof

**1. The exact second-Specht character.** The permutation representation on unordered pairs of distinct letters decomposes as the sum of the trivial, the standard \((n-1,1)\), and the \((n-2,2)\) Specht modules, each once. One way to see the last irreducible summand directly is through the multiplicity-free Young permutation module \(M^{(n-2,2)}\); this decomposition holds also for \(n=4\). Its permutation character is the number of invariant unordered pairs,
\[
\rho_2(g)=\binom{F(g)}2+T_2(g).
\]
Subtracting the trivial character \(1\) and the standard character \(F(g)-1\) gives
\[
\boxed{\chi_n(g)=\frac{F(g)(F(g)-3)}2+T_2(g).}
\]
At the identity this equals \(\binom n2-n=d_n\), confirming the degree. Character orthogonality gives \(\sum_{g\in G}\chi_n(g)=0\), since the Specht module is nontrivial.

**2. The sign-support collapse.** For nonnegative integer \(F\), the polynomial \(F(F-3)/2\) is \(-1\) precisely for \(F=1,2\), is \(0\) for \(F=0,3\), and is positive for \(F\ge4\). Since \(T_2(g)\) is a nonnegative integer, it follows that
\[
\chi_n(g)<0\quad\Longleftrightarrow\quad F(g)\in\{1,2\},\quad T_2(g)=0,
\]
and there \(\chi_n(g)=-1\). Hence the zero total character mass forces
\[
\frac1{n!}\sum_{g\in G}|\chi_n(g)|=2\Pr(F\in\{1,2\},T_2=0).
\]
There are exactly \(n\,a_{n-1}\) permutations with one fixed letter and no two-cycle, and \(\binom n2 a_{n-2}\) with two fixed letters and no two-cycle, where \(a_m=m!q_m\). (For the first case choose the fixed letter; the remaining permutation must have no cycles of length one or two. The second is analogous.) Therefore
\[
\boxed{\mathbb E_G|\chi_n|=2q_{n-1}+q_{n-2}.}
\]

**3. Sharpness and minimality among all projections.** On \(C(G)\) the canonical central isotypic projection is
\[
(P_nf)(x)=\frac{d_n}{n!}\sum_{g\in G}\chi_n(g^{-1})f(xg).
\]
Its kernel is a translate of \(d_n\chi_n/n!\), so the triangle inequality gives the upper bound \(\|P_n\|\le d_n\mathbb E_G|\chi_n|\). Taking \(f(g)=\operatorname{sgn}(\chi_n(g))\) for nonzero character values, and arbitrary values in \([-1,1]\) at zero character values, yields equality at the identity. Thus
\[
\|P_n\|=d_n(2q_{n-1}+q_{n-2})=n(n-3)\left(q_{n-1}+\frac12q_{n-2}\right).
\]

Now let \(Q\) be any projection onto \(E_n\). Average its conjugates under the isometric left and right regular actions of \(G\). The average \(\overline Q\) still takes values in \(E_n\), restricts to the identity there, and has \(\|\overline Q\|\le\|Q\|\). It commutes with all left and right translations. Such an operator is convolution with a central function and acts by scalars on the irreducible Fourier blocks of \(C(G)\). Since it must equal the identity on the \((n-2,2)\) block and zero on all other blocks, it is necessarily \(P_n\). Therefore \(\|Q\|\ge\|P_n\|\), proving the minimum. This averaging proof works over both \(\mathbb R\) and \(\mathbb C\) because the relevant central idempotent has a real kernel.

For real inputs \(f\) satisfying \(\|f\|_\infty=1\), equality \(\|P_nf\|_\infty=\|P_n\|\) holds **if and only if** there exist \(x\in G\) and \(\varepsilon\in\{-1,1\}\) such that
\[
 f(xg)=\varepsilon\,\operatorname{sgn}\chi_n(g)
 \quad\text{whenever }\chi_n(g)\ne0.
\]
There is no further restriction at the zero-character positions beyond \(|f|\le1\). This is exactly the equality condition in the finite triangle inequality at a maximizing kernel row. For complex inputs replace \(\varepsilon\) by an arbitrary unimodular phase.

**4. Exact coefficient formula, limit, and error.** The exponential formula for labelled permutations shows that permutations with no cycles of lengths one and two have exponential generating function
\[
\sum_{m\ge0}\frac{a_m}{m!}z^m
=\exp\left(\sum_{j\ge3}\frac{z^j}{j}\right)
=\frac{e^{-z-z^2/2}}{1-z}.
\]
Expanding the numerator proves the asserted finite double sum for \(q_m\). Writing \(h(z)=e^{-z-z^2/2}=\sum_{j\ge0}h_jz^j\), we have \(q_m=\sum_{j=0}^m h_j\), whereas \(\sum_{j\ge0}h_j=h(1)=e^{-3/2}\). Absolute convergence gives the limit. More quantitatively, for every real \(R>1\), the Cauchy coefficient bound \(|h_j|\le e^{R+R^2/2}R^{-j}\) implies
\[
 |q_m-e^{-3/2}|\le\frac{e^{R+R^2/2}}{R-1}R^{-m}.
\]
Substitution gives the explicit all-\(n\) inequality
\[
\left|\frac{\lambda(E_n)}{n(n-3)}-\frac3{2e^{3/2}}\right|
\le \frac{e^{R+R^2/2}}{R-1}
\left(R^{-(n-1)}+\frac12R^{-(n-2)}\right),\quad R>1.
\]
Since \(R\) can be fixed arbitrarily large, the normalized error decreases faster than any prescribed geometric rate.

## Verification

Run the standalone Python-standard-library program `python3 verify.py`. It enumerates all permutations in \(S_n\) for \(4\le n\le8\), counts their fixed points and disjoint two-cycles independently, and checks the character's mean zero, squared-character mean one, negative-sign support, exact absolute mass and sharp formula by rational arithmetic. It also checks the forbidden-cycle recurrence against the alternating double sum for \(0\le m\le14\). The terminal diagnostic is `ALL_SECOND_SPECHT_PROJECTION_CHECKS_PASSED`. These finite tests corroborate the calculation; the assertions for all \(n\ge4\) are proved above by representation decomposition, group averaging, and labelled-cycle enumeration.

## Relationship to prior work

Wildon's *Labelling the character tables of symmetric and alternating groups* provides concrete low-row character information and two-row Specht representations. Diaconis, Fulman and Guralnick's *On fixed points of permutations*, especially its section on the symmetric group's action on subsets, treats the pair-action fixed-point statistic and its Poisson-cycle limit. These are antecedents for the character and asymptotic setup; neither of their inspected full texts computes the sharp \(C(S_n)\) projection constant of the full \((n-2,2)\) matrix-coefficient block by its absolute character mass.

Scarabotti and Tolli's *Harmonic analysis on a finite homogeneous space* supplies the general finite homogeneous-space Fourier idempotent machinery (including its Corollary 2.15). General idempotent orthogonality and Haar/character inversion are standard, not claimed as new. Other related sharp calculations concern the **standard** Specht Fourier block in \(C(S_n)\) and the **same Specht shape in a different space**, the Johnson scheme on fixed-size subsets. Neither value determines the norm of this full regular-representation block: its convolution kernel is the character on all permutations, not a Johnson spherical function on subset intersections. The present evaluated absolute-character norm, cycle-avoidance reduction and complete norming-input classification were not found in the primary material inspected.

## Limitations

This is an exact theorem only for the full coefficient block of \((n-2,2)\) in the finite regular representation, not the Johnson spherical projector or projections onto individual copies of the module. It concerns supremum endpoint projections; no sharp intermediate-\(L^p\) formula is asserted. The old character identity and general central-projection method are classical. A matching evaluation could conceivably occur in unindexed character-\(L^1\) tables, symmetric-group Lebesgue-constant literature, or representation-theory books; absence from the examined texts does not constitute a universal priority certificate. The numerical checks are finite and do not independently certify the universal proof.

## References

1. Mark Wildon, *Labelling the character tables of symmetric and alternating groups*, arXiv:math/0612292v1, first posted 11 December 2006, especially section 2.2. https://arxiv.org/abs/math/0612292.
2. Persi Diaconis, Jason Fulman, Robert Guralnick, *On fixed points of permutations*, arXiv:0708.2643v1, first posted 20 August 2007, especially section 4. https://arxiv.org/html/0708.2643v1.
3. Fabio Scarabotti, Filippo Tolli, *Harmonic analysis on a finite homogeneous space*, arXiv:math/0701533v1, first posted 19 January 2007, especially Corollary 2.15. https://arxiv.org/html/math/0701533v1.
4. Mahya Alaghmandan, Nico Spronk, *Amenability properties of the central Fourier algebra of a compact group*, arXiv:1407.6783, first posted 25 July 2014. https://arxiv.org/abs/1407.6783.
