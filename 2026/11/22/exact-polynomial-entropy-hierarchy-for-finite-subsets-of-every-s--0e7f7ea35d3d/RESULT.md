# Exact polynomial-entropy hierarchy for finite subsets of every Sturmian shift

## Finding
Fix any irrational \(\alpha\in(0,1)\) and let \((X_\alpha,\sigma)\) be the bilateral Sturmian subshift of slope \(\alpha\). For every integer \(k\ge1\), the induced shift on finite nonempty subsets of cardinality at most \(k\) has polynomial entropy
\[
h_{\mathrm{pol}}(F_k(\sigma))=k.
\]
For every integer \(k\ge2\), the singleton-collapsed symmetric-product suspension also has
\[
h_{\mathrm{pol}}(SF_k(\sigma))=k, \qquad SF_k(X_\alpha)=F_k(X_\alpha)/F_1(X_\alpha).
\]
Consequently the induced map on the full hyperspace \(2^{X_\alpha}\) of nonempty compact subsets has infinite polynomial entropy. All finite-subset layers and their singleton-collapsed suspensions nevertheless have zero ordinary topological entropy.

This is an exact hierarchy for a **minimal, aperiodic, zero-topological-entropy** system in which every point belongs to the infinite chain-recurrent set. The lower bound survives both forgetting the ordering of the points and collapsing every singleton to one fixed point.

## Assumptions and scope
Let \(\mathbb T=\mathbb R/\mathbb Z\) have circle distance \(d_{\mathbb T}\). For irrational \(\alpha\in(0,1)\) define mechanical words at nonsingular intercepts \(t\in\mathbb T\) by
\[
c_t(j)=\lfloor t+(j+1)\alpha\rfloor-\lfloor t+j\alpha\rfloor\quad(j\in\mathbb Z).
\]
The Sturmian system \(X_\alpha\subset\{0,1\}^{\mathbb Z}\) is the closure of these words, including both boundary codings. The shift is \(\sigma(x)_j=x_{j+1}\). Equip \(X_\alpha\) with a compatible symbolic metric, normalized so that symbols differing at coordinate zero have distance \(1\). The Hausdorff metric \(d_H\) gives \(F_k(X_\alpha)=\{A\subset X_\alpha:1\le|A|\le k\}\) its compact topology. The induced map is \(F_k(\sigma)(A)=\sigma(A)\). For \(k\ge2\), collapse the closed invariant singleton stratum \(F_1(X_\alpha)\) to one point, obtaining \(SF_k(X_\alpha)\) with its induced homeomorphism. The full hyperspace \(2^{X_\alpha}\) consists of all nonempty compact subsets with the Hausdorff metric.

For a continuous map \(T\) on a compact metric space, write \(d_N^T(x,y)=\max_{0\le j<N}d(T^j x,T^j y)\), and let \(\mathrm{sep}(T,N,\varepsilon)\) be the maximum cardinality of a pairwise \(\varepsilon\)-separated set in this Bowen metric. Polynomial entropy means
\[
h_{\mathrm{pol}}(T)=\lim_{\varepsilon\downarrow0}\limsup_{N\to\infty}\frac{\log\mathrm{sep}(T,N,\varepsilon)}{\log N}.
\]
The convention for strict versus non-strict separation does not alter this value. All conclusions concern fixed irrational slopes; no claim about a rational slope, an arbitrary zero-entropy subshift, or a uniform finite-length constant across all slopes is made.

## Proof
**1. The continuous phase factor and its uniform separation.** The standard Sturmian phase map \(\pi:X_\alpha\to\mathbb T\) satisfies \(\pi(\sigma x)=\pi(x)+\alpha\). For completeness, take the closure in \(\mathbb T\times\{0,1\}^{\mathbb Z}\) of the graph of nonsingular mechanical codings. This closed graph projects onto \(X_\alpha\). Its projection to the symbolic coordinate is injective: two different intercepts \(t,s\) have different translated circle-interval indicator functions on a nonempty open arc, so density of irrational rotation produces an index at which any boundary codings differ. A compact-to-Hausdorff continuous bijection is a homeomorphism, yielding the claimed continuous map \(\pi\). At a singular intercept the two possible boundary codings have the same phase, which is harmless here. Compactness and continuity give, for each \(\delta>0\), some \(\eta(\delta)>0\) with
\[
d_{\mathbb T}(\pi x,\pi y)\ge\delta\quad\Longrightarrow\quad d(x,y)\ge\eta(\delta).
\]
The same implication holds after every common iterate because phase differences are rotation-invariant.

**2. An \(O(N)\) base bound.** The classical Sturmian block-complexity identity is \(p_{X_\alpha}(N)=N+1\): the \(N\)-symbol coding partition of the intercept circle has exactly the \(N+1\) distinct cut points \(-j\alpha\), \(0\le j\le N\), and these determine the distinct words. Given any fixed symbolic precision \(\varepsilon>0\), matching all coordinates in a fixed window \([-R,R]\) implies distance below \(\varepsilon\). Matching a word on \([-R,N+R]\) suffices throughout the \(N\)-step Bowen window and requires at most \(N+2R+2\) word classes. Thus the base \(N\)-step spanning number is \(O_\varepsilon(N)\). The ordered product \(X_\alpha^k\), with maximum product metric, has spanning number \(O_{\varepsilon,k}(N^k)\). The equivariant map from ordered tuples to their underlying unordered subset is 1-Lipschitz into \(F_k(X_\alpha)\). Hence \(h_{\mathrm{pol}}(F_k(\sigma))\le k\), and the singleton-collapse factor gives \(h_{\mathrm{pol}}(SF_k(\sigma))\le k\) for \(k\ge2\).

**3. Phase-labeled separated families of size \(\Omega(N^k)\).** Fix \(k\) pairwise disjoint closed nondegenerate circle arcs \(J_1,\ldots,J_k\) having mutual circular distance at least \(\delta>0\). For each \(N\), each arc \(J_i\) contains \(|J_i|N+o(N)\) cut points from the irrational-rotation orbit \(\{-j\alpha:0\le j\le N\}\), by Weyl equidistribution. Consequently the arc meets at least \(c_iN\) different length-\(N\) Sturmian coding cylinders for all sufficiently large \(N\), with some constants \(c_i>0\). For each such distinct word in each arc, select one nonsingular intercept there and its associated symbolic sequence. For every choice of one of these points in each \(J_i\), form the unordered \(k\)-element set \(A=\{x_1,\ldots,x_k\}\). There are at least \((\prod_i c_i)N^k\) such sets, and all their phases are separated across different indices by \(\delta\).

Consider two distinct selected sets \(A=\{x_i\}\) and \(B=\{y_i\}\), labeled uniquely by their arcs. There is an index \(i\) for which the selected length-\(N\) symbolic words differ, so for some \(0\le j<N\) the zeroth symbols of \(\sigma^j x_i\) and \(\sigma^j y_i\) differ. Hence \(d(\sigma^j x_i,\sigma^j y_i)=1\). For every \(\ell\ne i\), phase separation and Step 1 give \(d(\sigma^j x_i,\sigma^j y_\ell)\ge\eta(\delta)\). It follows that
\[
d_H(\sigma^j A,\sigma^j B)\ge \varepsilon_0:=\min\{1,\eta(\delta)\}>0.
\]
Thus these \(\Omega(N^k)\) sets are \(\varepsilon_0\)-separated for the length-\(N\) Bowen metric. This proves \(h_{\mathrm{pol}}(F_k(\sigma))\ge k\), completing the first equality without assuming that the quotient preserves the whole ordered-product complexity.

**4. Singleton collapse does not erase the lower bound.** For \(k\ge2\), consider the compact invariant subspace \(K_\delta\subset F_k(X_\alpha)\) comprising those exactly \(k\)-point subsets whose distinct phase coordinates have mutual circular distance at least \(\delta\). It is compact: such points cannot collide in a convergent sequence, because their phases remain separated. It is invariant because the common phase rotation preserves all phase differences, and it is disjoint from the singleton stratum. The quotient map \(q:F_k(X_\alpha)\to SF_k(X_\alpha)\) restricts to a homeomorphism of \(K_\delta\) onto its compact image. Uniform continuity of its inverse gives a scale \(\varepsilon_1>0\) for which \(d_H(A,B)\ge\varepsilon_0\) for \(A,B\in K_\delta\) implies their quotient images are at least \(\varepsilon_1\) apart. The selected sets of Step 3 and all their iterates belong to \(K_\delta\); their separation therefore persists in the quotient. This proves \(h_{\mathrm{pol}}(SF_k(\sigma))\ge k\).

**5. Full hyperspace and ordinary entropy.** The invariant finite-subset layers \(F_k(X_\alpha)\) embed in \(2^{X_\alpha}\). Polynomial entropy is monotone under invariant-subsystem restriction, so its value on the full hyperspace is at least \(k\) for each \(k\), hence infinite. Finally, the Sturmian shift has zero topological entropy because its word count is \(N+1\). Every ordered product \(X_\alpha^k\) has zero topological entropy; so do its unordered finite-subset factor and the singleton-collapsed factor. The theorem follows.

## Verification
The proof is analytical for all irrational slopes and all finite \(k\). The accompanying dependency-free `checker.py` uses exact rational arithmetic for a large-denominator coprime approximation and enumerates coding-partition components through length 60. It checks the \(N+1\) distinct word count, that three fixed separated phase arcs each carry linearly many different blocks, and that changing an arc-label changes a word in some time at which it is distinguished from every other label by phase. Run `python3 checker.py` to reproduce `checker_output.txt`. These finite checks are consistency tests; they are not substituted for Weyl equidistribution, uniform phase separation, or the quotient compactness argument.

## Relationship to prior work
Đorić’s preprint (arXiv:2507.10126v1, first public 2025-07-14) states a symmetric-product formula with a finiteness condition on the nonwandering set; its accepted 2026 manuscript gives the multiplicative expression for symmetric products and singleton-collapsed suspensions under **finite chain recurrence**, and a separate lower-bound result with **wandering points**. Neither hypothesis holds for a minimal infinite Sturmian subshift; the general product upper bound alone does not imply the lower bound through an unordered, then singleton-collapsed, quotient. Đorić, Katić and Lasković (2023) proved wandering-point-based lower bounds, likewise inapplicable here. This statement supplies the phase-marker lower bound for a natural minimal aperiodic system.

Published related work on parity of two equal-slope Sturmian sequences identifies a zero-entropy parity factor with the symmetric square after collapsing its diagonal; that topological identification does not compute polynomial entropy of this quotient, nor the all-\(k\) finite-subset hierarchy. The different rotating-disk example of a pointwise-periodic continuum has an exact fractional finite-hyperspace hierarchy but is not Sturmian or minimal: its proof relies on independent radial markers and on a different height-packing exponent. A general exact **ordinary topological entropy** theorem for finite-atomic measure strata involves a different space and invariant, and cannot determine the present polynomial entropy. The source searches find no statement dominating this theorem; historical priority is evidence-limited rather than independently certified.

## Limitations
The system is precisely a two-sided Sturmian subshift of known irrational slope. This theorem does not assert a comparable product equality for arbitrary minimal subshifts or for any general finite-to-one factor, where phase labels may be absent. Polynomial entropy of the full hyperspace is infinite, but its ordinary topological entropy is not asserted. The multiplicative statements are exact exponents, not sharp leading coefficients of finite-time covering numbers. Results do not assert quantitative constants uniform as \(\alpha\) approaches rational slopes, and finite checker runs do not prove the infinite claims. Independent validation and comprehensive historical-priority certification have not been performed.

## References
- M. Đorić, *Polynomial entropy on the \(n\)-fold symmetric product and its suspension*, arXiv:2507.10126v1 (first public 2025-07-14), https://arxiv.org/abs/2507.10126; Glasnik Matematicki 61 (2026), 59–76, https://doi.org/10.3336/gm.61.1.03.
- M. Đorić, J. Katić and B. Lasković, *On polynomial entropy of induced maps on symmetric products*, Acta Math. Hungar. 171 (2023), 334–347, https://doi.org/10.1007/s10474-023-01386-8.
- J. Berstel and L. Vuillon, *Coding rotations on intervals*, arXiv:math/0106217v1 (2001), https://arxiv.org/abs/math/0106217. Standard Sturmian intercept coding and cut-point complexity are used.
- *Exact two-to-one parity reconstruction and ergodic joining spectrum for a resonant Sturmian product*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-two-to-one-parity-reconstruction-and-ergodic-joining-spect--605183582075 (distinct parity-factor and symmetric-square description).
- *Fractional polynomial-entropy hierarchy in the finite hyperspaces of a pointwise periodic continuum*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-fractional-polynomial-entropy-hierarchy-in-the-finite-hyperspace--66fed2d3c218 (distinct rotating-disk system).
