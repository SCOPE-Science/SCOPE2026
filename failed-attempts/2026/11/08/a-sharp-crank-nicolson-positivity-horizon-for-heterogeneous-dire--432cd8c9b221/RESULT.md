# A sharp Crank–Nicolson positivity horizon for heterogeneous directed cycles

## Finding
For every integer \(n\ge3\) and strictly positive rates \(r_0,\ldots,r_{n-1}\), let \(Q\) be the row Markov generator on a one-way directed cycle, with \(Q_{ii}=-r_i\) and \(Q_{i,i+1\bmod n}=r_i\), all other entries zero. Put
\[
C(h)=\bigl(I-\tfrac h2 Q\bigr)^{-1}\bigl(I+\tfrac h2 Q\bigr),\qquad h\ge0.
\]
Choose an index \(p\) for which \(r_p=M:=\max_i r_i\). For \(0\le k\le n-1\), let \(a_k\) be the elementary symmetric polynomial of degree \(k\) in the \(n-1\) rates other than \(r_p\), with \(a_0=1\) and \(a_{-1}=0\). Set
\[
H_p(s)=\sum_{k=0}^{n-1}(a_k-Ma_{k-1})s^k.
\]
**Theorem.** The polynomial \(H_p\) has exactly one positive zero \(s_*>0\), that zero is simple, and
\[
\boxed{C(h)\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad0\le h\le h_*:=2s_*.}
\]
All off-diagonal entries of \(C(h)\) are strictly positive for every \(h>0\). Loss of positivity is caused by a diagonal entry at a state of maximum exit rate; it never recovers at larger timesteps. The threshold depends only on the **multiset** of rates, not on their cyclic ordering.

The sharp envelope at fixed maximum rate \(M\) is
\[
\boxed{\frac2M<h_*\le\frac{2\sigma_n}{M},}
\]
where \(\sigma_n>1\) is the unique solution of
\[
(\sigma_n-1)(1+\sigma_n)^{n-1}=\sigma_n^n.
\]
Equality on the right holds exactly when every rate equals \(M\). The left bound is the sharp infimum, approached as one of the remaining rates tends to zero while the other rates and \(M\) remain fixed. For \(n=3\), the upper threshold is \((1+\sqrt5)/M\).

More generally, define the stationary weights
\[
\pi_i=\frac{1/r_i}{\sum_{j=0}^{n-1}1/r_j}.
\]
For each state \(i\), its diagonal Crank–Nicolson entry has exactly one positive zero if \(\pi_i<1/2\), and has no finite positive zero if \(\pi_i\ge1/2\). When a zero exists, the diagonal changes sign from positive to negative exactly once. In particular, states of largest rate have the smallest diagonal entries at every positive step.

## Assumptions and scope
The cycle contains at least three distinct vertices, its transition rates are arbitrary strictly positive real numbers, and row probability vectors evolve by right multiplication with \(C(h)\). The generator is irreducible but generally not reversible. The claim concerns entrywise nonnegativity of the **end-step** rational update, not internal Runge–Kutta stages or nonlinear invariant-region preservation.

The elementary symmetric coefficients are finite polynomial expressions in the rates. The threshold can be computed by locating the unique positive real root of the explicitly stated degree-at-most-\(n-1\) polynomial. Rate vectors may have equal entries; there are no genericity assumptions. The endpoint \(h=0\) is included.

## Proof
Write \(s=h/2\) and \(R_s=(I-sQ)^{-1}\). Since \(I-sQ\) is a nonsingular irreducible \(M\)-matrix, its inverse is nonnegative, and strictly positive for \(s>0\). The Cayley identity gives
\[
C(h)=2R_s-I.
\]
Thus every off-diagonal entry is positive at positive steps; entrywise positivity is equivalent to \((R_s)_{ii}\ge1/2\) for every \(i\).

Set \(t_i=(1+sr_i)^{-1}\) and \(q_i=sr_i/(1+sr_i)\). From the cyclic recurrence for a resolvent column, or from the Neumann series of the weighted cyclic shift, the probability of returning to \(i\) after \(k\) complete tours yields
\[
(R_s)_{ii}=t_i\sum_{k=0}^{\infty}\left(\prod_{j=0}^{n-1}q_j\right)^k
=\frac{1}{(1+sr_i)(1-\Pi(s))},
\quad
\Pi(s)=\prod_{j=0}^{n-1}\frac{sr_j}{1+sr_j}.
\]
The formula is valid for every \(s>0\), since \(0<\Pi(s)<1\); it extends continuously to \(s=0\). In particular, at fixed \(s>0\) the denominator factor \(1-\Pi(s)\) is common to all states, so the smallest diagonal resolvent entry is exactly at any state with maximum rate. Consequently only such states constrain the full matrix, and permuting the rates leaves the threshold unchanged.

The positive common denominator can be written
\[
D(s)=\prod_j(1+sr_j)-s^n\prod_jr_j
=\sum_{k=0}^{n-1}e_k(r_0,\ldots,r_{n-1})s^k>0,
\]
where \(e_k\) is the elementary symmetric polynomial of degree \(k\). For an arbitrary state \(i\), write \(a^{(i)}_k=e_k((r_j)_{j\ne i})\), and put \(a^{(i)}_{-1}=0\). Then
\[
(R_s)_{ii}=\frac{\prod_{j\ne i}(1+sr_j)}{D(s)},\qquad
2(R_s)_{ii}-1
=\frac{\sum_{k=0}^{n-1}\bigl(a^{(i)}_k-r_i a^{(i)}_{k-1}\bigr)s^k}{D(s)}.
\]
For positive \(n-1\) variables, Newton's inequalities imply that the ratios \(a^{(i)}_k/a^{(i)}_{k-1}\) strictly decrease with \(k\) for \(1\le k\le n-1\). Therefore the coefficient sequence \(a^{(i)}_k-r_i a^{(i)}_{k-1}\), read from constant to leading coefficient and ignoring zeros, has **at most one** sign change, from positive to negative. Its constant term is one. Its leading coefficient is
\[
a^{(i)}_{n-1}-r_i a^{(i)}_{n-2}
=\left(\prod_{j\ne i}r_j\right)
\left(1-r_i\sum_{j\ne i}\frac1{r_j}\right).
\]
The latter is negative precisely when \(\pi_i<1/2\). In that case, the polynomial is positive at zero and tends to negative infinity, and Descartes' rule of signs proves that it has exactly one positive root, counted with multiplicity. In particular the root is simple, and the entry is negative thereafter. If \(\pi_i\ge1/2\), the leading coefficient is nonnegative; the monotonicity of the ratios forces **all** coefficients to be nonnegative, so there is no positive root and the diagonal stays positive at finite steps.

At a maximum-rate state \(p\),
\[
M\sum_{j\ne p}\frac1{r_j}\ge n-1>1,
\]
so a unique finite positive root \(s_*\) exists. Its state has the smallest resolvent diagonal, proving the claimed exact full-matrix positivity interval and no-recovery law.

For the sharp bounds, evaluate the resolvent formula at \(s=1/M\):
\[
(R_{1/M})_{pp}=\frac{1}{2(1-\Pi(1/M))}>\frac12.
\]
Thus \(s_*>1/M\). Fix \(M\). The product \(\Pi(s)\) is strictly increasing in each other rate at every fixed \(s>0\), so \((R_s)_{pp}\), and hence its unique crossing time, strictly increases when any rate other than \(r_p\) increases while \(M\) is unchanged. The largest possible threshold is therefore attained precisely when all rates equal \(M\). With \(x=sM\), the uniform-rate crossing equation is
\[
\frac{1}{(1+x)\bigl(1-(x/(1+x))^n\bigr)}=\frac12
\quad\Longleftrightarrow\quad
(x-1)(x+1)^{n-1}=x^n.
\]
Uniqueness follows from the already-proved one-crossing property. If any one of the other positive rates tends to zero, \(\Pi(s)\to0\) for fixed \(s>0\) and the crossing tends to \(s=1/M\), proving sharpness of the strict lower bound. When \(n=3\), the uniform equation becomes \(x^2-x-1=0\), so \(x=(1+\sqrt5)/2\), completing the proof.

## Verification
`verify_cn_cycle.py` uses Python's exact rational type to assemble each cyclic generator, invert \(I-sQ\) by independent rational Gaussian elimination, and test the return formula, the sign-polynomial numerator and stochastic row sums. It checks a seeded collection of rational rate vectors for all cycle sizes from three through eight and multiple rational steps per vector. It also checks the ordering-of-rates identity, coefficient-ratio monotonicity, the three-state uniform critical equation and near-zero-rate limiting brackets. Run it with `python3 verify_cn_cycle.py` in the extracted directory. The verifier must print its four `PASS` lines without exceptions. These finite calculations are consistency tests; the proof above establishes the result for every allowed length and positive real rate vector.

## Relationship to prior work
The Cayley/resolvent identity and the fact that off-diagonal entries are nonnegative for Markov generators are **prior work**. Fallat and Tsatsomeros (2002) treat Cayley transforms of matrix positivity classes; a published published-finding corpus result (*A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*) gives the exact diagonal-resolvent test for **all** finite generators and proves the single-crossing property using reversibility. That source explicitly leaves nonreversible uniqueness of positivity windows open. The present theorem does not claim those general identities or their reversible consequences as new: it proves a **nonreversible directed-cycle** single-crossing law, a closed elementary-symmetric root formula, cyclic-order independence, and sharp extrema over heterogeneous rates.

Horváth, Song and Terlaky (2014) develop general step-size bounds for invariance of discretization methods, but the inspected rational-method positivity analysis does not determine the fixed-generator, heterogeneous directed-cycle threshold. Hadjimichael, Ketcheson and Lóczi (2021) discuss one-way periodic upwind advection as a positive baseline, but principally analyze non-Metzler centered-difference operators, not variable-rate directed-cycle Crank–Nicolson thresholds. Higueras and Roldán (2023) classify positivity thresholds for symmetric tridiagonal heat discretizations rather than one-way nonreversible cycles. These comparisons concern the exact claims and hypotheses, not merely matching terminology.

## Limitations
The result concerns directed one-way cycles with strictly positive rates. It does not classify general nonreversible generators, multiway transport, trees or graphs with additional jumps. It gives a degree-at-most-\(n-1\) root specification, not radicals for arbitrary cycle size. Independent literature-priority verification has not been performed; obscure specialist sources could contain an equivalent cyclic-resolvent formula or its implications. The exact threshold is an end-step condition, and floating-point computations near a zero diagonal need care.

## References
1. Zoltán Horváth, Yue Song and Tamás Terlaky, *Steplength Thresholds for Invariance Preserving of Discretization Methods of Dynamical Systems on a Polyhedron*, first publicly posted 26 June 2014, arXiv:1406.6755v1. https://arxiv.org/abs/1406.6755
2. Shaun M. Fallat and Michael J. Tsatsomeros, *On the Cayley Transform of Positivity Classes of Matrices*, Electronic Journal of Linear Algebra 9 (2002), 190–196, DOI:10.13001/1081-3810.1086. https://journals.uwyo.edu/index.php/ela/article/download/173/173
3. A. Hadjimichael, D. I. Ketcheson and L. Lóczi, *Positivity preservation of implicit discretizations of the advection equation*, arXiv:2105.07403 (2021). https://arxiv.org/abs/2105.07403
4. I. Higueras and T. Roldán, *A new insight on positivity and contractivity of the Crank–Nicolson scheme for the heat equation*, arXiv:2301.01066 (2023). https://arxiv.org/abs/2301.01066
5. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, published-finding corpus, 2026, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a.
