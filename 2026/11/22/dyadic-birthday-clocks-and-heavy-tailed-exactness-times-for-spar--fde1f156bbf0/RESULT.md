# Dyadic birthday clocks and heavy-tailed exactness times for sparse cylinders of binary Rule 102

## Finding

For the additive cellular automaton \(F:\mathbb F_2^{\mathbb Z}\to\mathbb F_2^{\mathbb Z}\), \((Fx)_i=x_i+x_{i+1}\pmod{2}\), let \(S\subset\mathbb Z\) be nonempty and finite, \(u:S\to\mathbb F_2\), and
\[
C(S,u)=\{x:x_s=u(s)\text{ for all }s\in S\},\qquad
T(S)=\min\{t\ge 0:F^t C(S,u)=\mathbb F_2^{\mathbb Z}\}.
\]
The time \(T(S)\) is finite and independent of the prescribed pattern \(u\). For **every** integer \(m\ge0\), the following exact equivalence holds:
\[
\boxed{T(S)\le 2^m\quad\Longleftrightarrow\quad
s\longmapsto s\bmod 2^m\text{ is injective on }S.}
\tag{1}
\]
In particular, fix integers \(R\ge1\), \(1\le k\le N=2^R\), sample \(S\) uniformly from the \(k\)-subsets of \(\{0,\ldots,N-1\}\), and define the dyadically rounded exactness clock \(H(S)=\min\{2^m:T(S)\le2^m\}\). Its **complete finite-size distribution** is
\[
\boxed{\Pr(H(S)\le2^m)=
\frac{\binom{2^m}{k}(N/2^m)^k}{\binom Nk},\quad 0\le m\le R.}
\tag{2}
\]
The binomial coefficient is zero if \(2^m<k\). As \(k\to\infty\), \(N=2^R\to\infty\), and \(k^2/N\to0\), for dyadic \(b=2^m\) with \(b/k^2\to\alpha\in(0,\infty)\),
\[
\boxed{\Pr(H(S)\le b)\longrightarrow e^{-1/(2\alpha)}.}
\tag{3}
\]
Thus the natural onset of full-image cylinder exactness occurs at the **birthday-collision scale** \(k^2\), with dyadic phase dependence rather than a single smoothly rescaled continuous hitting-time law.

A further exact evaluation of the **unrounded** clock is possible for three sites. For any three distinct integers \(a,b,c\), set \(\nu_2(d)\) to be the exponent of two in a nonzero integer \(d\). Then
\[
\boxed{T(\{a,b,c\})=1+\max\{2^{\nu_2(b-a)},2^{\nu_2(c-a)},2^{\nu_2(c-b)}\}.}
\tag{4}
\]
For uniform three-subsets of \(\{0,\ldots,2^R-1\}\), \(R\ge2\), write \(T_R=T(S)\), \(Z_R=T_R-1\), \(N=2^R\), and \(\Delta_N=(1-N^{-1})(1-2N^{-1})\). The exact mean and second moment are
\[
\mathbb E[T_R]
=2+\frac{\tfrac32R-4+6/N-2/N^2}{\Delta_N},
\tag{5}
\]
\[
\mathbb E[Z_R^2]=1+\frac{3}{4\Delta_N}
\left(2N-2R-\frac{10}{3}+\frac4N-\frac{8}{3N^2}\right).
\tag{6}
\]
Consequently,
\[
\boxed{\mathbb E[T_R]=\frac32\log_2 N-2+O((\log N)/N),\qquad
\operatorname{Var}(T_R)=\frac32N+O((\log N)^2).}
\tag{7}
\]
Yet the distribution of \(T_R\) is tight: for each fixed \(m\ge1\),
\[
\lim_{R\to\infty}\Pr(T_R\le1+2^{m-1})
=(1-2^{-m})(1-2^{1-m}).
\tag{8}
\]
In particular, its limiting median is five updates. The logarithmically divergent mean and linearly divergent variance come from increasingly rare near-collisions of the three sampling sites modulo high powers of two, not from typical growth of the clock.

## Assumptions and scope

All configurations are **bilateral**, indexed by every integer, with values in \(\mathbb F_2\). Dynamics is synchronous. A cylinder fixes exactly the coordinates indexed by \(S\) and leaves all other coordinates free. The equality \(F^t C(S,u)=\mathbb F_2^{\mathbb Z}\) means *every bilateral target configuration*, not merely a finite output block or periodic-ring target. The randomized statements sample unordered position sets uniformly without replacement; there is no randomness in the cellular-automaton update. The dyadic law (1) holds for every nonempty finite position set; the exact unrounded mean (5) and variance (7) are claimed only for three-site masks in a dyadic interval.

## Proof

**1. Entire image and kernel.** Put \(E x\) for the left shift \((Ex)_i=x_{i+1}\). Then \(F=I+E\), and the extreme coefficients of \(F^t\) equal one. The bilateral recurrence therefore solves \(F^t x=y\) in both directions for any target \(y\): \(F^t\) is onto for every \(t\ge1\). The homogeneous solution space \(K_t=\ker(F^t)\) has dimension \(t\) over \(\mathbb F_2\), determined by any \(t\) consecutive coordinates. A prescribed cylinder maps onto the whole target space precisely if the evaluation map \(K_t\to\mathbb F_2^S\), \(z\mapsto z|_S\), is onto. This follows because each nonempty fibre of \(F^t\) is a translate of \(K_t\); if evaluation were not onto, some target would exclude the prescribed pattern by linearity.

**2. Exact dyadic criterion.** In characteristic two the Frobenius identity gives \(F^{2^m}=I+E^{2^m}\). Thus \(K_{2^m}\) consists **exactly** of arbitrary binary sequences periodic with period dividing \(2^m\). Prescribing values at sites \(S\) can be extended to all of \(K_{2^m}\) exactly when no two sites represent the same residue class modulo \(2^m\). Combined with step 1 this proves (1), including \(m=0\), and also implies that \(T(S)\) is finite. Once an image becomes full, it remains full under subsequent iterates since \(F\) is onto.

**3. Complete dyadic population.** Let \(b=2^m\) divide \(N=2^R\). There are \(b\) residue classes, each containing \(N/b\) eligible sites. Exactly \(\binom bk(N/b)^k\) unordered \(k\)-sets select pairwise different classes, out of \(\binom Nk\) equally likely sets. This proves (2). Using falling factorials, its probability is \(\prod_{j=0}^{k-1}(1-j/b)/(1-j/N)\). Under the stated sparse birthday scaling, the denominator product tends to one because \(k^2/N\to0\); Taylor expansion of the numerator gives
\[
\sum_{j=0}^{k-1}\log(1-j/b)
=-\frac{k(k-1)}{2b}+O(k^3/b^2)
\longrightarrow-\frac{1}{2\alpha},
\]
which proves (3). The limit is asserted only along sequences for which the displayed dyadic ratio converges; different dyadic phases need not merge.

**4. The exact unrounded triple clock.** Use the standard identification of the dual of \(K_t\) with \(\mathbb F_2[z,z^{-1}]/((1+z)^t)\): an evaluation relation \(\sum_{s\in S}\epsilon_s z^s\) vanishes on all \(K_t\) exactly if it is divisible by \((1+z)^t\). Consequently, for every nonempty finite \(S\),
\[
T(S)=1+\max_{\substack{\epsilon\in\mathbb F_2^S\\\epsilon\ne0}}
\operatorname{ord}_{z=1}\sum_{s\in S}\epsilon_s z^s.
\tag{9}
\]
The zero polynomial is excluded; Laurent monomials have order zero. For three distinct sites, every odd-cardinality subset polynomial has value one at \(z=1\) and hence order zero. Every nonempty even-cardinality subset has two sites \(a,b\), for which
\[
\operatorname{ord}_{z=1}(z^a+z^b)=2^{\nu_2(b-a)};
\]
this follows from \(1+z^d=(1+z^{d/2^{\nu_2(d)}})^{2^{\nu_2(d)}}\) in characteristic two, with the inner factor having a simple root at one. Equation (9) now proves (4).

**5. Three-probe moments and tightness.** By (4), for \(1\le m\le R\), the event \(T_R\le1+2^{m-1}\) is exactly the event that all three sampled sites have distinct residues modulo \(2^m\). Hence
\[
\Pr(T_R\le1+2^{m-1})
=\frac{\binom{2^m}{3}(N/2^m)^3}{\binom N3}
=\frac{(1-2^{-m})(1-2^{1-m})}{\Delta_N}.
\tag{10}
\]
The random variable \(Z_R\) takes values among \(1,2,4,\ldots,2^{R-1}\). For \(j\in\{1,2\}\), its moments follow by the finite telescoping identity
\[
\mathbb E[Z_R^j]
=1+\sum_{m=1}^{R-1}(2^{jm}-2^{j(m-1)})
\left[1-\Pr(T_R\le1+2^{m-1})\right].
\tag{11}
\]
Substituting (10) and evaluating the elementary geometric sums yields (5) and (6); subtracting \((\mathbb E[Z_R])^2\) proves (7). Taking \(R\to\infty\) in (10) proves (8). Since the limiting cumulative probability at three updates is \(3/8\), and at five updates is \(21/32\), the limiting median is five.

## Verification

Run `python3 verify_threepoint.py` from this package. The checker compares an independently constructed mod-two Pascal/Hasse evaluation matrix with (4) for all \(560\) triples on sixteen sites; exhaustively tests (10), (5), and (6) for every triple on intervals of lengths \(4,8,16,32,64\); tests (1) against independent matrix rank over \(43,255\) finite mask-time cases; and checks the exact occupancy census (2) for sizes up to \(32\) and masks up to five sites. This is a finite check of the algebra and finite counts; the general all-size and asymptotic statements rest on the proofs above.

## Relationship to prior work

Haugland, Larsen, Omland and Rustad establish a qualitative locally-eventually-onto framework and discuss the known locally-eventually-onto property of bipermutive cellular automata; the inspected full text does not evaluate sparse-site cylinder exactness-time distributions or birthday scaling. Sutner's de Bruijn graph treatment establishes CA surjectivity and reversibility criteria but not this distribution. Existing special-mask exactness results for arithmetic-progression probes and two separated blocks imply certain exceptional cases of (1) and (4), but do not state the arbitrary-mask residue criterion, finite-size \(k\)-probe distribution, sparse-birthday transition or three-probe mean/variance disparity. The algebraic ingredients (Frobenius, finite-field linear algebra and elementary occupancy counting) are classical; the claimed contribution is their complete, explicitly evaluated **quantitative dynamical distribution** for sparse cylinders, not a new theorem about those classical ingredients.

## Limitations

The finite-size occupancy law concerns **dyadic iterates** and the rounded clock \(H(S)\), not a complete distribution of the unrounded clock \(T(S)\) for arbitrary \(k\ge4\). The exact unrounded clock and moment formulas are restricted to three-point sets; for four or more points, non-pairwise polynomial relations can affect \(T(S)\) between dyadic instants. The birthday scaling assumes \(k^2/N\to0\), and the dyadic phase \(2^m/k^2\) must converge. These statements concern the bilateral full shift and do not assert corresponding cyclic-ring behavior. Historical originality outside the searched literature is provisional; no independent audit has occurred.

## References

- J. K. Haugland, N. S. Larsen, T. Omland and H. G. Rustad, *Locally eventually onto cellular automata*, arXiv:2610.33131, first public 23 October 2026, https://arxiv.org/abs/2610.33131, especially Section 5 and Appendix B of version 2.
- K. Sutner, *De Bruijn Graphs and Linear Cellular Automata*, Complex Systems **5** (1991), 19–30, https://content.wolfram.com/sites/13/2018/02/05-1-3.pdf, Sections 1–2.
