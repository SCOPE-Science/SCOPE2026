# Coordinatewise Euclidean inertia dominance for every order–chain polytope pair

## Finding

Let \(P\) be an arbitrary nonempty finite poset and let \(X\) and \(Y\) be uniform by full-dimensional Lebesgue volume on its standard-coordinate order and chain polytopes, respectively. For each \(v\in P\), put
\[
L_v(x)=\max\bigl(\{x_u:u<_P v\}\cup\{0\}\bigr),\qquad
U_v(x)=\min\bigl(\{x_w:v<_P w\}\cup\{1\}\bigr).
\]
Then the following **coordinatewise variance identity and strict sign classification** hold:
\[
\boxed{\operatorname{Var}(X_v)-\operatorname{Var}(Y_v)
=\operatorname{Cov}\bigl(L_v(X),U_v(X)\bigr)\geq 0.}
\]
The inequality is **strict if and only if** there exist \(u,w\in P\) with \(u<_P v<_P w\); otherwise the difference is exactly zero. Consequently, writing \(J(K)=\operatorname{tr}(\operatorname{Cov}(Z))\) for uniform \(Z\) in \(K\),
\[
\boxed{J(\mathcal O(P))\ge J(\mathcal C(P)),\quad
J(\mathcal O(P))=J(\mathcal C(P))\iff \operatorname{height}(P)\le 2.}
\]
For the three-element chain, the strict gap is \(1/80\).

There is also an exact rational linear-extension formula. Put \(n=|P|\); choose a linear extension \(\sigma\) uniformly and write \(r_\sigma(u)\) for the position of \(u\). Set
\[
a_v(\sigma)=\max\bigl(\{r_\sigma(u):u<_P v\}\cup\{0\}\bigr),\qquad
b_v(\sigma)=\min\bigl(\{r_\sigma(w):v<_P w\}\cup\{n+1\}\bigr).
\]
With expectation \(\mathbb E_\sigma\) over linear extensions, the common difference above equals
\[
\boxed{\frac{\mathbb E_\sigma[a_v(b_v+1)]}{(n+1)(n+2)}-
\frac{(\mathbb E_\sigma a_v)(\mathbb E_\sigma b_v)}{(n+1)^2}.}
\]

## Assumptions and scope

The order polytope is
\[
\mathcal O(P)=\{x\in[0,1]^P:x_u\le x_v\text{ whenever }u<_P v\}.
\]
The chain polytope is
\[
\mathcal C(P)=\{y\in\mathbb R_{\ge0}^P:\sum_{v\in C}y_v\le1\text{ for every chain }C\subseteq P\}.
\]
Both polytopes are full-dimensional in the same canonical coordinate Euclidean space. All variances use the *uniform interior-volume* distributions, not uniform vertices or random independent generator coefficients. A chain of length three means three distinct, strictly comparable elements. The height is the maximum number of elements in a chain, not the number of cover edges.

## Proof

**1. Uniform transfer and conditional variances.** Stanley's triangular transfer map sends \(x\in\mathcal O(P)\) to \(y\in\mathcal C(P)\) via \(y_v=x_v-L_v(x)\). In a linear extension order of the coordinates this is a triangular map with diagonal entries one almost everywhere. Its inverse is constructed inductively using \(x_v=y_v+\max_{u<_P v}x_u\) (with the empty maximum zero). Thus it sends uniform volume to uniform volume. We may couple the distributions by setting \(Y_v=X_v-L_v(X)\).

Fix a vertex \(v\) and condition on the other coordinates \(X_{P\setminus\{v\}}\). By the defining order inequalities, \(X_v\) is uniform on \([L_v,U_v]\). Hence \(Y_v\) is conditionally uniform on \([0,U_v-L_v]\). Their conditional variances coincide, equal to \((U_v-L_v)^2/12\), while their conditional means are \((U_v+L_v)/2\) and \((U_v-L_v)/2\). The law of total variance therefore yields the exact identity
\[
\operatorname{Var}(X_v)-\operatorname{Var}(Y_v)
=\operatorname{Var}\!\left(\frac{U_v+L_v}{2}\right)
-\operatorname{Var}\!\left(\frac{U_v-L_v}{2}\right)
=\operatorname{Cov}(L_v,U_v).
\]

**2. Nonnegative covariance.** The order polytope is closed under coordinatewise minimum and maximum: if \(x,z\in\mathcal O(P)\), then \(x\wedge z,x\vee z\in\mathcal O(P)\). Consequently its indicator density is log-supermodular (MTP2): \(f(x)f(z)\le f(x\wedge z)f(x\vee z)\) for every \(x,z\). The continuous FKG association inequality applies to its normalized uniform measure. Since \(L_v\) and \(U_v\) are coordinatewise nondecreasing, \(\operatorname{Cov}(L_v,U_v)\ge0\).

**3. Exact strictness.** If \(v\) is minimal then \(L_v=0\) identically; if \(v\) is maximal then \(U_v=1\) identically. Either way the covariance is zero.

Suppose now \(v\) has at least one strict predecessor and at least one strict successor. Set \(T=X_v\). For every \(0<t<1\), the conditional law of the other coordinates given \(T=t\) is uniform on a nonempty full-dimensional slice, and its density is MTP2. Thus \(\operatorname{Cov}(L_v,U_v\mid T=t)\ge0\). Furthermore, when \(0<s<t<1\), the two slice densities satisfy Holley's cross-lattice inequality: for any possible other-coordinate vectors \(z,z'\), the indicator at \((s,z)\) times that at \((t,z')\) is at most the product of the indicators at \((s,z\wedge z')\) and \((t,z\vee z')\). Indeed, coordinatewise minimum and maximum preserve all order inequalities. Holley's stochastic-order criterion therefore implies that the conditional distributions of the other coordinates are stochastically nondecreasing as \(t\) increases. As \(L_v,U_v\) are increasing, the two functions
\[
\ell(t)=\mathbb E[L_v\mid T=t],\qquad
\nu(t)=\mathbb E[U_v\mid T=t]
\]
are nondecreasing.

They are both nonconstant. Since \(0\le L_v\le T\), \(\ell(t)\to0\) as \(t\downarrow0\), while \(\ell(t)>0\) for all \(0<t<1\) because a strict predecessor has a strictly positive coordinate almost surely on every interior slice. Similarly \(T\le U_v\le1\) yields \(\nu(t)\to1\) as \(t\uparrow1\), but \(\nu(t)<1\) for all \(0<t<1\) because a strict successor has coordinate less than one almost surely. The density of \(T\) is positive throughout \((0,1)\), so the strict one-variable Chebyshev association inequality for two nonconstant nondecreasing functions gives \(\operatorname{Cov}(\ell(T),\nu(T))>0\). Explicitly, using an independent copy \(T'\), this covariance is one half of \(\mathbb E[(\ell(T)-\ell(T'))(\nu(T)-\nu(T'))]\), and the integrand is positive on a set of positive probability. The law of total covariance now implies
\[
\operatorname{Cov}(L_v,U_v)=\mathbb E[\operatorname{Cov}(L_v,U_v\mid T)]+\operatorname{Cov}(\ell(T),\nu(T))>0.
\]
A vertex has both a predecessor and successor exactly when it is internal to a three-element chain; summing the nonnegative coordinate gaps proves the inertia statement and its exact equality classification.

**4. Exact finite rank expression.** The order polytope is partitioned, up to measure-zero boundaries, into the simplices indexed by linear extensions. All such simplices have equal volume. Conditional on a uniform extension, the coordinates are the increasing order statistics \(U_{(1)}<\dots<U_{(n)}\) of \(n\) iid uniform \([0,1]\) observations. With \(U_{(0)}=0\), \(U_{(n+1)}=1\), and positions \(a_v<b_v\), the Dirichlet spacing identities give
\[
\mathbb E[U_{(a_v)}\mid\sigma]=\frac{a_v}{n+1},\quad
\mathbb E[U_{(b_v)}\mid\sigma]=\frac{b_v}{n+1},\quad
\mathbb E[U_{(a_v)}U_{(b_v)}\mid\sigma]=\frac{a_v(b_v+1)}{(n+1)(n+2)}.
\]
Averaging over extensions gives the displayed exact rational covariance formula. The empty boundary conventions also satisfy these three identities, including \(b_v=n+1\).

## Verification

The standalone Python 3 checker `check_order_chain_inertia.py` uses only standard-library exact rational arithmetic. Independently of FKG or Holley's theorem, it enumerates all 5230 naturally labeled finite posets of sizes two through six, exhausts their linear extensions, calculates both polytope coordinate variances via order-statistic/Dirichlet moments, verifies the covariance identity term by term and the claimed strictness/equality criterion, and checks 250 additional reproducible seven-element posets. It also verifies the three-chain gap \(1/80\). It prints `ORDER_CHAIN_INERTIA_FKG_CHECKS_PASSED 5230 3708 1522 250` on success. This is finite corroboration, not a replacement for the proof for arbitrary posets.

## Relationship to prior work

Stanley's original transfer map gives volume preservation and the order/chain-polytope definitions; it does not supply the present variance comparison. Ahmad–Fourier–Joswig (2023) and Freij-Hollanti–Lundström (2023) study face-vector comparisons of order and chain polytopes, not uniform-volume covariance. Hibi–Li (2012 preprint) characterize unimodular equivalence, which is not Euclidean-isometric equivalence. Lee (2026) proves a different inequality on edge lengths, with the same three-chain threshold, but edge-length dominance does not determine second moments of uniform interior volume. A previously obtained exact inertia-gap expression for ordinal sums of antichains is a strict special case, not a general-poset formula, and is not claimed anew. The FKG/Holley principles are established probabilistic ingredients, not claimed as new.

## Limitations

Only standard-coordinate Euclidean volume and the coordinatewise variances, not the full covariance-matrix positive-semidefinite order, are compared. No affine-invariant isotropic-constant comparison is proved; volume-preserving but nonorthogonal transformations generally change Euclidean inertia. While the specified searches and inspected literature did not identify an equivalent general-poset inequality, historical priority needs independent verification, including possible earlier statements phrased as stochastic association or order-statistic inequalities.

## References

- R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23, DOI: 10.1007/BF02187680. Definitions and transfer map.
- I. Ahmad, G. Fourier, M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626v1, posted 2023-09-04, https://arxiv.org/abs/2309.01626. Relevant lead literature on comparisons.
- R. Freij-Hollanti, T. Lundström, *\(f\)-vector inequalities for order and chain polytopes*, arXiv:2312.13890v1, posted 2023-12-21, https://arxiv.org/abs/2312.13890.
- T. Hibi, N. Li, *Unimodular equivalence of order and chain polytopes*, arXiv:1208.4029, posted 2012-08-20, https://arxiv.org/abs/1208.4029.
- J. Lee, *A refinement of the edge theorem for order and chain polytopes*, arXiv:2610.07413v1, posted 2026-10-05, https://arxiv.org/abs/2610.07413.
- C. M. Fortuin, P. W. Kasteleyn, J. Ginibre, *Correlation inequalities on some partially ordered sets*, Communications in Mathematical Physics 22 (1971), 89–103; and R. Holley, *Remarks on the FKG inequalities*, Communications in Mathematical Physics 36 (1974), 227–231. Standard association and monotone-measure principles used above.
