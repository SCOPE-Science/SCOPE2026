# An arithmetic correction-order transition for mixed perfect-power gap shifts

## Finding

Fix coprime integers \(2\le r<s\). Let \(X_{r,s}\subseteq\{0,1\}^{\mathbb Z}\) be the binary subshift obtained by closing all bi-infinite concatenations of blocks \(10^{m^r}\) and \(10^{m^s}\), for integers \(m\ge1\). Set
\[
\mathcal E_{r,s}(\rho)=\sup\{h_\mu(\sigma):\mu\text{ is shift-invariant on }X_{r,s},\ \mu([1])=\rho\},\quad 0<\rho<\tfrac12.
\]
Entropies use natural logarithms. Write
\[
q=\frac1r,\quad \alpha=\frac1r-\frac1s,\quad
\beta=\frac1r-\frac1{rs},\quad a=\frac{\Gamma(1/r)}r,\quad
B=\frac{\Gamma(1/s)/s}{a},\quad C=\frac{\Gamma(1/(rs))/(rs)}a,\quad
Q=\frac{B^2}{2}\left(1+\frac{\alpha^2}{q}\right).
\]
**Theorem.** The unique entropy-maximizing invariant probability at every \(0<\rho<1/2\) is the stationary renewal process with a unique exponentially tilted return-length distribution. As \(\rho\downarrow0\), its entropy obeys the **three-regime expansion**
\[
\frac{\mathcal E_{r,s}(\rho)}\rho
=q\log\frac1\rho+\log a-q\log q+q+B(q\rho)^\alpha-
\begin{cases}
Q(q\rho)^{2\alpha}+o(\rho^{2\alpha}),&s<2r-1,\\
(Q+C)(q\rho)^{2\alpha}+o(\rho^{2\alpha}),&s=2r-1,\\
C(q\rho)^\beta+o(\rho^\beta),&s>2r-1.
\end{cases}
\]
Thus the second sparse-marker correction has a sharp **arithmetic resonance** at \(s=2r-1\). Below it the second correction comes from entropy-optimization feedback, above it from duplicate integer powers, and at equality both terms contribute at the same order. The equality regime is achievable, e.g. \((r,s)=(2,3)\) and \((3,5)\).

For the smallest example \((r,s)=(2,3)\), the normalized entropy has the explicit form
\[
\frac{\mathcal E_{2,3}(\rho)}\rho
=\frac12\log\frac1\rho+\frac12\log\frac\pi2+\frac12
+0.897686900876\ldots\rho^{1/6}
-1.256166304699\ldots\rho^{1/3}+o(\rho^{1/3}).
\]

## Assumptions and scope

A permitted gap is the **number of zero symbols** between consecutive markers, not the return length. Hence a gap \(k\) gives a marker-to-marker return length \(R=k+1\). The allowed gap set is the **union**, not a multiset: a number that is both an \(r\)-th and an \(s\)-th power is permitted only once. The coprimality assumption is essential for the displayed intersection exponent \(rs\); for noncoprime exponents one must use their least common multiple instead. The proof is for fixed integers \(r,s\) as density \(\rho\) tends to zero, not uniform as those exponents grow. The shift includes its all-zero closure point and other limiting configurations with infinite zero tails.

## Proof

**1. Exact return partition and optimization.** Since \(\gcd(r,s)=1\), unique prime factorization gives
\[
\{m^r:m\ge1\}\cap\{m^s:m\ge1\}=\{m^{rs}:m\ge1\}.
\]
For \(p>0\), define \(D_k(p)=\sum_{m\ge1}e^{-p m^k}\). The return partition is exactly
\[
Z(p)=\sum_{k\text{ permitted}}e^{-p(k+1)}
=e^{-p}\bigl(D_r(p)+D_s(p)-D_{rs}(p)\bigr).
\]
Its tilted return distribution is \(\nu_p(R)=e^{-pR}/Z(p)\). Because distinct return lengths occur, \(m(p)=-(\log Z)'(p)\) is strictly decreasing, with \(m(0+)=\infty\) and \(m(+\infty)=2\). There is therefore exactly one \(p=p(\rho)>0\) with \(m(p)=1/\rho\) for every \(0<\rho<1/2\).

Condition a stationary measure with marker density \(\rho>0\) on a marker at the origin and induce to the next marker. Its return-length marginal \(\nu\) satisfies \(\mathbb E_\nu R\le1/\rho\), with equality precisely if no invariant mass is on the all-zero fixed point. (Any extra infinite-zero tails carry zero mass under a stationary measure with positive marker density.) By Abramov's entropy formula and the entropy-rate bound, \(h_\mu(\sigma)\le \rho H(\nu)\). The relative-entropy inequality against \(\nu_p\) gives \(H(\nu)\le\log Z(p)+p\mathbb E_\nu R\), hence
\[
h_\mu(\sigma)\le\rho\log Z(p)+p.
\]
At \(p=p(\rho)\), equality is attained by the shift-stationary, i.i.d.-return renewal measure with Palm gap law \(\nu_p\). Equality requires (i) no zero atom, (ii) independent induced returns, and (iii) the exact tilted marginal; this proves uniqueness. In particular,
\[
\frac{\mathcal E_{r,s}(\rho)}\rho
=\inf_{p>0}\left(\frac p\rho+\log Z(p)\right).
\tag{1}
\]
The infimum has a unique minimizer because \((\log Z)''=\operatorname{Var}_{\nu_p}(R)>0\).

**2. Controlled power sums, including derivatives.** For any fixed integer \(k\ge2\), put \(a_k=\Gamma(1/k)/k\). Euler summation, with one further integration by parts in its Bernoulli remainder, gives
\[
D_k(p)=a_k p^{-1/k}-\tfrac12+O(p^{1/k})\quad(p\downarrow0),
\tag{2}
\]
with the same asymptotic after applying \((p\,d/dp)^j\) for \(j=1,2\) (the constant contributes zero to those derivatives). To see the error bound directly, apply the second-order Euler summation identity to the smooth function \(f_p(x)=e^{-p x^k}\). Its integral is \(a_kp^{-1/k}\), its value at zero is one, its first derivative at zero vanishes, and the integral of the absolute second derivative is \(O(p^{1/k})\). For the derivative statements replace \(f_p\) by \((p\,\partial_p)^j f_p\), whose second derivative still has integrable absolute value \(O(p^{1/k})\); the endpoint terms have the required values. All constants may depend on the fixed exponents.

Substituting (2) and \(q=1/r\) in the inclusion-exclusion identity yields, with two logarithmic derivatives uniformly controlled,
\[
D_r(p)+D_s(p)-D_{rs}(p)
=a p^{-q}\left(1+B p^\alpha-Cp^\beta+O(p^q)\right).
\tag{3}
\]
Note \(0<\alpha<\beta<q<1\). Expanding its logarithm and writing \(\kappa=\min\{2\alpha,\beta\}\),
\[
\log Z(p)= -p+\log a-q\log p+B p^\alpha
-\tfrac12 B^2p^{2\alpha}-Cp^\beta+o(p^\kappa),
\tag{4}
\]
where terms of order higher than \(p^\kappa\) are harmless and the differentiated remainder has the same relative order. This follows because \(3\alpha>2\alpha\), \(\alpha+\beta>\beta\), and \(q>\beta\).

**3. Perturbing the unique saddle.** The unperturbed objective in (1) is \(p/\rho-q\log p+\log a\), whose unique saddle is \(p_0=q\rho\). The derivative expansion from (3)-(4), together with strict convexity, gives
\[
p(\rho)=p_0\left(1-\frac{B\alpha}{q}p_0^\alpha+o(p_0^\alpha)\right).
\tag{5}
\]
The term \(-p\) in (4) contributes only \(O(\rho)\), negligible because \(\kappa<1\). Evaluating the objective at (5), the first perturbation contributes \(Bp_0^\alpha\); optimization of the saddle supplies the additional \(-B^2\alpha^2 p_0^{2\alpha}/(2q)\). Thus
\[
\frac{\mathcal E_{r,s}(\rho)}\rho
=q\log\frac1\rho+\log a-q\log q+q+Bp_0^\alpha
-Qp_0^{2\alpha}-Cp_0^\beta+o(p_0^\kappa).
\tag{6}
\]
Only those displayed terms at or below the \(p_0^\kappa\) scale are retained; terms of higher order are absorbed into the remainder.

Finally,
\[
\beta-2\alpha=\frac{2r-s-1}{rs}.
\]
For \(s<2r-1\) the \(2\alpha\) term dominates the overlap term; for \(s>2r-1\) the \(\beta\) term dominates the quadratic term; at equality both have exactly the same exponent. This proves all three assertions. Substitution of \((r,s)=(2,3)\) in the constants gives the displayed numerical example.

## Verification

The standalone `verify.py` uses only the Python standard library. It implements the exact three-power partition (rather than counting duplicate perfect powers twice), numerically solves the strict-variance saddle equation, and compares the entropy against the first- and second-order expansions on eight coprime exponent pairs at three small densities. It also checks finite perfect-power intersections and the sign of the critical exponent difference. Run `python verify.py`. The checker passed **24 saddle/entropy comparisons, 8 intersection comparisons, and 8 order comparisons**. All computations are supporting finite checks; the asymptotic statement is proved analytically above. Truncation of each positive sum is at a dimensionless exponential cutoff, and can be bounded by an elementary decreasing-tail integral beyond that cutoff.

## Relationship to prior work

General \(S\)-gap shift renewal coding and entropy variational principles are established in the prior literature. Haydarov–Kadyrov–Makhmudov–Mamayusupov (2026) develop a general renewal-potential theory for \(S\)-gap shifts, including induced return laws; their results are used as motivating context, not represented here as newly discovered. Climenhaga–Thompson and Baker–Ghenciu address intrinsic ergodicity, coding and topological entropy. A published calculation titled *A theta-cubic law for sparse-marker entropy in the square-gap shift* obtains the single-power \(r=2\) density-constrained entropy expansion, exploiting a Gaussian theta identity. That calculation is an important closest analogue, but it does not include the union of distinct exponent families, the explicit duplicate-power subtraction, or the three-way arithmetic correction-order transition. General power-sum asymptotics and relative-entropy optimization are classical ingredients; the asserted new result is their nontrivial combined, explicit classification for all fixed coprime exponent pairs.

## Limitations

The asymptotic little-o constants depend on fixed \(r,s\), and no quantitative density threshold or uniformity in growing exponents is asserted. The result is about density-constrained invariant entropy, not all equilibrium states of arbitrary potentials or the unconstrained topological entropy. The coprimality assumption matters; no extension to noncoprime exponents is claimed. Published and indexed results were searched, but earlier equivalent calculations in unindexed renewal or arithmetic thermodynamic literature cannot be categorically excluded. The numerical checker is not an independent proof or an independent mathematical audit.

## References

1. B. Haydarov, S. Kadyrov, J. Makhmudov, M. Mamayusupov, *Effective Intrinsic Ergodicity for renewal-type potentials on S-gap shifts*, first publicly posted 2026-06-15, arXiv:2606.17031, https://arxiv.org/abs/2606.17031.
2. V. Climenhaga and D. J. Thompson, *Intrinsic ergodicity beyond specification: beta-shifts, S-gap shifts, and their factors*, arXiv:1011.2780, https://arxiv.org/abs/1011.2780.
3. S. Baker and A. E. Ghenciu, *Dynamical properties of S-gap shifts and other shift spaces*, arXiv:1411.7167, https://arxiv.org/abs/1411.7167.
4. V. Climenhaga, *Entropy of S-gap shifts*, 2014-09-08, https://vaughnclimenhaga.wordpress.com/2014/09/08/entropy-of-s-gap-shifts/.
5. *A theta-cubic law for sparse-marker entropy in the square-gap shift*, public research record dated 2026-10-25, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-a-theta-cubic-law-for-sparse-marker-entropy-in-the-square-gap-sh--1db74ef026b2/RESULT.md.
6. Classical Euler summation and the Gibbs variational/relative-entropy inequality (standard analytical identities invoked with proofs of the needed bounds above).
