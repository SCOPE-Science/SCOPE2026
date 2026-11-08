# Exact dyadic-block collision clocks and rare staircases in the necktie symplectic billiard

## Finding

The polygonal *necktie* symplectic billiard has a return section on which the induced transformation is a dyadic adding machine. The already-established geometric return time is four times the relevant staircase level. Under normalized arclength on one such section fiber, this roof has an exceptionally rigid joint law, not the law of independent excursions.

Fix an integer \(k\geq0\). The total number \(C_{2^k}\) of **original symplectic-billiard iterations** needed for \(2^k\) successive returns to the same fiber obeys the **exact**, nonasymptotic distribution
\[
\Pr\{C_{2^k}=8\cdot2^k-4+4j\}=2^{-(j+1)},\qquad j=0,1,2,\ldots.
\]
In particular, \(\mathbb E C_{2^k}=8\cdot2^k\) and \(\operatorname{Var}(C_{2^k})=32\) for **every** \(k\geq0\). The variance remains bounded even as the number of nonperiodic returns grows without bound.

More generally, let \(\ell_j\) be the staircase level of the \(j\)-th return and let \(\tau_j=4\ell_j\) be its number of original billiard-map iterations. For integers \(n,m\geq1\), write \(n=q2^{m-1}+r\), where \(0\leq r<2^{m-1}\), and let
\[
N_{n,m}=\#\{0\leq j<n:\ell_j\geq m\}.
\]
Then
\[
N_{n,m}\ \stackrel{d}{=}\ q+\operatorname{Bernoulli}(r/2^{m-1}).
\]
This means that every orbit has exactly one depth-at-least-\(m\) excursion in every block of \(2^{m-1}\) consecutive returns, up to the null set of undefined boundary trajectories. In particular, such events **cannot** have Poisson count fluctuations at complete dyadic blocks.

For the maximum depth \(M_n=\max_{0\leq j<n}\ell_j\), its exact finite-horizon law is
\[
\Pr(M_n\leq m)=\max\{0,1-n/2^m\},\qquad m=0,1,2,\ldots.
\]
The one-step moment and two-time covariance laws are
\[
\mathbb E\tau_0=8,\quad \operatorname{Var}(\tau_0)=32,\quad
\operatorname{Cov}(\tau_0,\tau_h)=16\left(2-3\cdot2^{-\nu_2(h)}\right)\quad(h\geq1),
\]
where \(\nu_2(h)\) is the exponent of two dividing a positive integer \(h\). Thus the nondecaying long-lag covariance along powers of two coexists with exact cancellation in the full-block collision clock.

## Assumptions and scope

Use the explicit necktie of Albers, Lander and Westermann: the square has cyclic vertices \((2,2),(2,0),(0,0),(0,2)\); the kite has cyclic vertices \((5,2),(4,2),(3,0),(5,1)\). Fix any interior point \(x\) on the upper kite side joining \((5,2)\) and \((4,2)\). Consider the first-return section with initial first coordinate \(x\) and second coordinate on the right square side, affinely normalized to \(s\in(0,1)\). Sample \(s\) with normalized one-dimensional Lebesgue measure. Exclude the countable dyadic exceptional set where the billiard map encounters a vertex or the return coding is not defined.

The geometric input from Section 5 of *Symplectic billiards for pairs of polygons* is that the induced return \(T\) on this fiber is the von Neumann–Kakutani map and that for every \(\ell\geq1\), points in
\[
I_\ell=(1-2^{1-\ell},1-2^{-\ell})
\]
first return after exactly \(4\ell\) iterations of the original billiard map. In particular this theorem concerns the **induced clock** on a specified one-dimensional fiber with its normalized arclength law. It makes no assertion about sampling from full two-dimensional billiard phase-space area, or about metric path length in place of iteration count.

## Proof

**1. Coding the geometry into a valuation observable.** A nondyadic coordinate \(s\) has a unique infinite binary expansion \(s=\sum_{i\geq1}b_i2^{-i}\). Its digit sequence is a Haar-distributed \(2\)-adic integer \(K=\sum_{i\geq1}b_i2^{i-1}\). The cited return-map conjugacy sends \(T\) to \(K\mapsto K+1\). The cylinder \(I_\ell\) comprises the binary sequences beginning with \(\ell-1\) ones followed by a zero. Equivalently, \(\nu_2(K+1)=\ell-1\). Therefore, simultaneously for every forward return index \(j\geq0\),
\[
\ell_j=1+\nu_2(K+j+1),\qquad \tau_j=4\bigl(1+\nu_2(K+j+1)\bigr).
\]
The equality holds outside the Haar-null set on which one of the arguments of \(\nu_2\) vanishes in the \(2\)-adic integers. Haar invariance under addition means every \(K+j\) is Haar distributed. For \(a\geq0\), divisibility by \(2^a\) has probability \(2^{-a}\). Hence \(\Pr(\ell_j=t)=2^{-t}\) for every positive integer \(t\), giving the quoted one-step moments.

**2. Exact counts and maximum.** The event \(\ell_j\geq m\) means that \(K+j+1\) occupies the unique residue zero modulo \(p=2^{m-1}\). Every interval of \(n=qp+r\) consecutive integers contains either \(q\) or \(q+1\) members of a prescribed residue class modulo \(p\). As the starting residue \(K+1\pmod p\) is uniform, exactly \(r\) of its \(p\) choices yield the additional member. This proves the stated Bernoulli law and its deterministic complete-block consequence. Similarly, \(M_n\leq m\) means avoiding the residue zero modulo \(2^m\) during \(n\) consecutive integers. For \(n\leq2^m\), exactly \(n\) of the \(2^m\) starting residues hit zero; for \(n>2^m\), all do. This proves the maximum law, including the boundary \(m=0\).

**3. Exact dyadic clock.** Put \(n=2^k\) and let \(\nu_j=\nu_2(K+j+1)\). For each valuation level \(1\leq a\leq k\), exactly \(2^{k-a}\) among these \(2^k\) consecutive integers are divisible by \(2^a\). Their total contribution to \(\sum_j\nu_j\) is therefore \(\sum_{a=1}^k2^{k-a}=2^k-1\). Precisely one summand is divisible by \(2^k\). Conditioned on its residue modulo \(2^k\), its quotient by \(2^k\) is Haar distributed, and its **additional** valuation \(G_k\) satisfies
\[
\Pr(G_k=j)=2^{-(j+1)},\qquad j\geq0.
\]
All other summands have valuation below \(k\), so
\[
\sum_{j=0}^{2^k-1}\nu_j=2^k-1+G_k,
\quad C_{2^k}=4\sum_{j=0}^{2^k-1}(1+\nu_j)=8\cdot2^k-4+4G_k.
\]
The geometric variable has mean one and variance two, yielding the exact clock law, expectation and variance. This is a statement of distributions for each block length; it does **not** claim that \(G_k\) is one common random variable for all \(k\).

**4. Lagged correlations.** Put \(h\geq1\), \(z=\nu_2(h)\), and \(A=\nu_2(K+1)\), \(B=\nu_2(K+h+1)\). If \(A<z\), then \(B=A\). If \(A>z\), then \(B=z\). If \(A=z\), then \(B>z\), with its excess valuation geometric conditional on the corresponding residue. By symmetry between \(A\) and \(B\), with \(\Pr(A=t)=2^{-(t+1)}\),
\[
\mathbb E[(A+1)(B+1)]
=\sum_{t=0}^{z-1}\frac{(t+1)^2}{2^{t+1}}
 +2(z+1)\sum_{t=z+1}^{\infty}\frac{t+1}{2^{t+1}}
=6-3\cdot2^{-z}.
\]
Both one-step means are two. Subtract their product four and multiply by sixteen, because \(\tau=4\ell\), to get \(\operatorname{Cov}(\tau_0,\tau_h)=16(2-3\cdot2^{-z})\). For \(h=0\), \(\operatorname{Var}(\tau_0)=32\), as proved already.

All claims follow by residue combinatorics and full-measure measurable coding, with no infinite-horizon conclusion inferred from enumeration.

## Verification

Run `python3 verify_clock.py` from the package directory. The code tests \(7{,}729\) exact finite modular assertions on dyadic return counts, dyadic-block collision clocks, maximum-level distributions, and joint divisibility for distinct lags. All tested assertions passed. The proof above, not the finite calculations, establishes the unbounded-level and all-horizon identities.

A direct consistency check is that at \(n=1\), the total return time equals four times a geometric-level variable with mean eight and variance thirty-two, agreeing with the dyadic-block formula for \(k=0\). The longer-block formula makes the strong dependence operationally visible: the same variance persists when \(n\) is arbitrarily large but a power of two.

## Relationship to prior work

Albers, Lander and Westermann, *Symplectic billiards for pairs of polygons*, Section 5, provide the exact necktie geometry, conjugacy to the dyadic odometer, and the return time \(4\ell\) for each branch. These foundational statements are **not** new here. The present contribution takes the original billiard-iteration clock as a dynamical observable and computes its **multi-return distribution**, its exact lattice block fluctuations, the complete rare-staircase count and maximum laws, and the two-time covariance. None of these joint statistical statements is asserted in the inspected Section 5.

Bruin and Lukina, *Rotated odometers*, study measurable conjugacies and ergodic structure of odometer-derived interval exchanges. Bruin and Lukina, *Skew-product systems over infinite interval exchange transformations*, analyze discrepancy and diffusion for different, mostly bounded-symbol skew observables of rotated odometers. Both inform the present comparison, but neither inspected result gives this geometric billiard roof's valuation law or its constant-variance physical collision clock. The underlying residue argument is elementary and related to classical divisibility counting; independent novelty in the broad arithmetic literature is not certified.

## Limitations

The statement is specific to the stated necktie geometry and the indicated one-dimensional return fibers with normalized Lebesgue initial law. The count variable measures original-map iterations, not Euclidean flight lengths. It does not imply analogous statistics for arbitrary polygon pairs, general rotated odometers, or phase-space area measures. The original geometric return-time fact is invoked from the cited full-text source; the new statistics are proved conditionally on that established geometric identification. Existing number-theoretic treatments of sums of consecutive \(2\)-adic valuations could imply some arithmetic components in other language. Publication priority beyond the inspected sources and research-record searches needs human literature review. No independent mathematical audit is reported.

## References

1. P. Albers, F. Lander, J. M. Westermann, *Symplectic billiards for pairs of polygons*, arXiv:2402.12244, first submitted 2024-02-19, especially Section 5; https://arxiv.org/abs/2402.12244.
2. H. Bruin and O. Lukina, *Rotated odometers*, Journal of the London Mathematical Society **107** (2023), 1983–2024, DOI: 10.1112/jlms.12731; https://doi.org/10.1112/jlms.12731.
3. H. Bruin and O. Lukina, *Skew-product systems over infinite interval exchange transformations*, arXiv:2408.14079, first submitted 2024-08-26, especially Sections 1 and 4; https://arxiv.org/abs/2408.14079.
