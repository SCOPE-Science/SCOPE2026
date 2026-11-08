# Sharp endpoint unconditionality on biased binary filtrations

## Finding

Let \(d\ge0\) and let \(\Omega=\{0,1\}^d\) carry a strictly positive product probability measure. Write \(\theta_j\in(0,1)\) for the probability of a zero in coordinate \(j\), and put \(r_j=\min\{\theta_j,1-\theta_j\}\in(0,1/2]\). Denote by \(\mathbb E_j\) conditional expectation onto the first \(j\) coordinates, with \(\mathbb E_0 f=\int f\,d\mu\). For each prefix \(u\) of length \(j-1\), let \(D_{j,u}f=\mathbf1_{C_u}(\mathbb E_j-\mathbb E_{j-1})f\). For independently chosen signs \(\varepsilon_0,\varepsilon_{j,u}\in\{-1,1\}\), set
\[
T_\varepsilon=\varepsilon_0\mathbb E_0+\sum_{j=1}^d\sum_{|u|=j-1}\varepsilon_{j,u}D_{j,u}.
\]
These are the signed diagonal transforms of the complete finite real Haar system, including the constant vector. Define their sharp endpoint unconditionality constant by
\[
U(\theta_1,\ldots,\theta_d)=\max_\varepsilon\|T_\varepsilon\|_{L^\infty(\mu)\to L^\infty(\mu)}.
\]
The following **exact nonstationary formula** holds. Starting with \(A_{d+1}=0\) and \(B_{d+1}=1\), compute, for \(j=d,d-1,\ldots,1\),
\[
\boxed{\quad A_j=A_{j+1}+(1-r_j)(1+B_{j+1}),\qquad B_j=(1-r_j)-r_jB_{j+1}.\quad}
\]
Then
\[
\boxed{U(\theta_1,\ldots,\theta_d)=A_1+B_1,}
\]
with the empty-depth convention \(U=1\).

If every \(\theta_j\ne1/2\), there is exactly **one evaluation atom** on which a maximally normed transform can realize the global bound: the leaf choosing the *less likely* child at every level. On that leaf, all maximizing transforms have the constant coefficient sign \(\varepsilon_0=s\in\{-1,1\}\) and the successive ancestral Haar signs \(\varepsilon_{j,u_j}=(-1)^j s\). Signs at all nonancestral nodes may be chosen arbitrarily. For any such transform, a norming real input with unit supremum norm is obtained by taking the sign of its kernel row at this leaf; on zero kernel entries arbitrary values in \([-1,1]\) are allowed. These conditions characterize all norm-attaining unit inputs for a maximizing transform, up to the common output sign.

For identical biases with \(r=\min\{\theta,1-\theta\}\), the recurrence reduces to the **closed form**
\[
\boxed{U_d(r)=1+\frac{2(1-r)}{1+r}d-\frac{4r^2}{(1+r)^2}\bigl(1-(-r)^d\bigr).}
\]
In particular, for every fixed \(0<r<1/2\),
\[
U_d(r)=\frac{2(1-r)}{1+r}d+1-\frac{4r^2}{(1+r)^2}+\frac{4r^2}{(1+r)^2}(-r)^d.
\]
Thus the exact linear endpoint-growth slope is \(2(1-r)/(1+r)\), strictly greater than the fair-splitting slope \(2/3\). The alternating exponentially decaying term is exact, not only asymptotic. The fair case \(r=1/2\) is included as a consistency boundary, not claimed as new.

## Assumptions and scope

All functions, signs and norms are real. Every coordinate probability lies strictly between zero and one. The filtration is **coordinate-product**, with one binary split per level and identical split probabilities across nodes of a given depth, but probabilities may differ arbitrarily between depths. The signs are independently assigned to the constant and every one-dimensional martingale difference space indexed by a prefix. The entire finite Haar system is retained; this is a signed unconditionality problem, not a suppression-only problem or a best projection onto a proper subspace. The \(L^\infty\) space is finite-dimensional, so all suprema are attained.

## Proof

**1. Signed kernel and active mass.** Fix a terminal atom \(x\) and a sign assignment. The row kernel with respect to \(\mu\) is
\[
K_\varepsilon(x,y)=\varepsilon_0+\sum_{j=1}^d\varepsilon_{j,u_j}\left(\frac{\mathbf1_{\{y_{1:j}=x_{1:j}\}}}{\mu(C_{x_{1:j}})}-\frac{\mathbf1_{\{y_{1:j-1}=x_{1:j-1}\}}}{\mu(C_{x_{1:j-1}})}\right),
\]
where \(u_j=x_{1:j-1}\). The \(L^\infty\)-norm of the operator is the largest absolute row integral \(\max_x\sum_y\mu(y)|K_\varepsilon(x,y)|\). Off-path signs never occur in this row.

Accumulate the signed row measure \(K_\varepsilon(x,y)\mu(y)\) down the path of \(x\). Immediately before a split, its restriction to the active node has constant density and total signed mass \(z\in[-1,1]\). Let \(q\) be the conditional probability of the selected child, and \(e\in\{-1,1\}\) the sign of this node's martingale difference. The sibling receives signed mass \((1-q)(z-e)\); the selected child retains signed mass \(qz+e(1-q)\). The latter remains in \([-1,1]\) since it is a convex combination of \(z\) and \(e\). The siblings have disjoint supports, so the endpoint row variation satisfies an exact one-dimensional Bellman recursion.

**2. Affine Bellman envelope.** For the subfiltration beginning at level \(j\), let \(F_j(z)\) be the maximum absolute mass of the completed signed row when the active signed mass is \(z\). The base case is \(F_{d+1}(z)=|z|\). For the two possible child weights \(q\in\{r_j,1-r_j\}\),
\[
F_j(z)=\max_{q,e}\left\{(1-q)|z-e|+F_{j+1}(qz+e(1-q))\right\},\quad |z|\le1.
\]
We prove inductively that \(F_j(z)=A_j+B_j|z|\), with \(0\le B_j\le1\). By symmetry take \(z\in[0,1]\), abbreviate \(r=r_j\), \(a=A_{j+1}\), \(b=B_{j+1}\). Choosing the rarer child \(q=r\) and opposite sign \(e=-1\) yields
\[
L(z)=a+(1-r)(1+b)+\bigl((1-r)-rb\bigr)z,
\]
because \(rz-(1-r)\le0\). The other sign with \(q=r\) yields the same intercept with the negative slope, so cannot improve on \(L\) because \((1-r)-rb\ge0\).

For \(q=1-r\), either sign gives a convex function of \(z\). To compare it with the affine \(L(z)\), it suffices to check \(z=0\) and \(z=1\): the difference \(L\) minus a convex function is concave and cannot lie below the minimum of its endpoint values. At \(z=0\) the difference is \((1-2r)(1+b)\). At \(z=1\) it is respectively \(2(1-2r)\) for \(e=-1\) and \(2(1-r(1+b))\) for \(e=+1\). All are nonnegative for \(r\le1/2\), \(0\le b\le1\). Thus \(L\) is the exact maximum. This proves the displayed recurrences, including \(0\le B_j=(1-r_j)-r_jB_{j+1}\le1\). Starting with \(z=\varepsilon_0=\pm1\) gives \(U=A_1+B_1\).

**3. Strict extremizers.** If \(r_j<1/2\), all three competing endpoint gaps above are strictly positive for the more likely child. Also \((1-r_j)-r_jB_{j+1}>0\), forcing opposite sign whenever \(z\ne0\). Along the optimal path the updated signed mass has the opposite sign, since \((1-r_j)>r_j|z|\) and hence it never vanishes. Consequently every maximizing row chooses the rare child at each level, with strictly alternating ancestral signs. Conversely this choice attains the affine Bellman value. A real input realizes the absolute row sum exactly when it matches the signs of the nonzero kernel coefficients (or their common negative), as stated.

**4. Homogeneous simplification.** With \(r_j=r\), write \(b_m\) for the affine slope after \(m\) remaining steps. Then \(b_0=1\), \(b_{m+1}=1-r-rb_m\), so
\[
b_m=\frac{1-r}{1+r}+\frac{2r}{1+r}(-r)^m.
\]
The intercept increases by \((1-r)(1+b_m)\) per step. Summing this finite geometric series gives the boxed formula for \(U_d(r)\). Both the linear term and exact alternating correction follow without taking an infinite-depth limit.

## Verification

The companion `check_biased_haar.py` constructs each probability-weighted kernel row directly from the conditional-expectation formula, enumerates all row-ancestral sign choices, and compares the resulting exact rational maxima against the separate Bellman recurrence. It checks 16 heterogeneous and homogeneous configurations and 10,586 row/sign combinations, including norming-path and sign rigidity when all biases are strict. A second rational test verifies 120 homogeneous closed-form instances. It uses standard-library exact fractions, does not rely on floating-point tolerances, and ends with `ALL_NONHOMOGENEOUS_HAAR_ENDPOINT_CHECKS_PASSED`. Tests are finite diagnostics, not substitutes for the proof above.

## Relationship to prior work

Classical martingale-transform and Haar unconditionality theory motivates this endpoint problem. Osękowski (2013) establishes sharp *restricted weak-type* inequalities for the Haar system and martingale transforms; its result concerns different norms and does not determine finite weighted \(L^\infty\) row constants. Thiele, Treil and Volberg (2014) treat general nonhomogeneous martingale differences and prove weighted \(L^2\) multiplier bounds under \(A_2\) conditions, but do not give this finite-depth \(L^\infty\) exact recurrence or rare-leaf rigidity. The known exact fair-binary finite-depth signed formula is recovered upon setting all \(r_j=1/2\) and is not included in the claimed novelty. The new contribution is the exact nonstationary-bias formula, strict rare-leaf/alternating-sign classification, and the full continuum of sharp homogeneous slopes.

## Limitations

The result does not cover non-product node-dependent biases, nonbinary splits, weighted target norms, \(L^p\) norms for finite \(p\), or suppression-only constants. Norming real inputs are classified by kernel-row sign rather than by an explicit listing of their values on all \(2^d\) atoms. Bibliographic searches and inspected source texts do not prove universal priority: equivalent formulas may occur implicitly in older martingale-transform literature. No independent mathematical audit has been performed.

## References

1. A. Osękowski, *Sharp Inequalities for the Haar System and Fourier Multipliers*, Journal of Function Spaces and Applications (2013), article 646012. First published: 2013-12-05. https://doi.org/10.1155/2013/646012
2. C. Thiele, S. Treil and A. Volberg, *Weighted martingale multipliers in non-homogeneous setting and outer measure spaces*, arXiv:1411.5345 (first posted 2014-11-19). https://arxiv.org/abs/1411.5345
