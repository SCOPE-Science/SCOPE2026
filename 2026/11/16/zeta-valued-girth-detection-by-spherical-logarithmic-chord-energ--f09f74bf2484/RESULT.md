# Zeta-valued girth detection by spherical logarithmic chord energies

## Finding

Let \(G=(V,E)\) be a finite simple graph and let \((P_v)_{v\in V}\) be independent points uniformly distributed in normalized area measure on the unit sphere \(\mathbb S^2\). For \(e=\{u,v\}\), put
\[
X_e=\log\frac{|P_u-P_v|}{2}+\frac12.
\]
Each \(X_e\) has the same centered law. The complete family \((X_e)_{e\in E}\) is jointly independent **if and only if** \(G\) is a forest.

For every integer \(k\ge3\), a simple \(k\)-cycle has the nonzero connected edge moment
\[
\tau_k=\operatorname{cum}(X_{e_1},\ldots,X_{e_k})
=\sum_{\ell=1}^\infty(2\ell+1)\left(-\frac1{2\ell(\ell+1)}\right)^k.
\]
In particular, \(\tau_3=(1-\zeta(3))/4\), \(\tau_4=5/16-\zeta(3)/4\), and \(\tau_5=(7-5\zeta(3)-\zeta(5))/16\), and
\[
\tau_k=3(-1/4)^k+O((1/12)^k)\quad(k\to\infty).
\]
The fourth-cycle value was previously obtained for the logarithmic cross ratio; it is not a new special-case claim.

Let \(S_G=\sum_{e\in E}X_e\), let \(m=|E|\), and if \(G\) is cyclic let \(g\) denote its girth and \(c_g\) its number of unoriented shortest simple cycles. Then the defect of the cumulant-generating functions has the *exact first nonzero order*
\[
\log\mathbb E e^{tS_G}-m\left(\frac t2-\log(1+t/2)\right)
=c_g\tau_g t^g+O_G(t^{g+1})\quad(t\to0).
\]
For a forest it vanishes identically wherever the moment generating functions exist. Thus the scalar law of \(S_G\) determines \(m=4\operatorname{Var}(S_G)\), whether \(G\) is a forest, and, when cyclic, both \(g\) and \(c_g\) exactly. The coefficient alternates in sign with \(g\), unlike the positive overlap coefficients for linear spherical spin interactions.

More generally, for any strictly positive edge weights \(w_e\), the same assertion holds after replacing \(S_G\) by \(\sum_e w_eX_e\), the independent-edge comparison by the corresponding weighted sum, and \(c_g\) by \(\sum_{C\in\mathcal C_g(G)}\prod_{e\in C}w_e\).

## Assumptions and scope

The graph is finite, simple, loop-free and undirected; isolated vertices are allowed. Chord lengths are Euclidean lengths in \(\mathbb R^3\). All measures on the sphere are normalized to probability one. Every cycle is unoriented and counted once up to cyclic rotation and reversal. Girth is the length of the shortest simple cycle; a forest has infinite girth. The logarithm is the real natural logarithm; coinciding independent sphere points have probability zero. Weighted graphs use deterministic real weights, with positive weights required to prevent cancellation in the first nonzero cycle coefficient. All assertions concern exact population distributions; nothing is claimed about noisy finite-sample reconstruction or graph isomorphism.

## Proof

**1. One-edge law and forests.** For fixed \(P_u\), rotational invariance makes \(U=(1-P_u\cdot P_v)/2\) uniform on \((0,1)\). Since \(|P_u-P_v|/2=\sqrt U\), the edge variable is \(X=(1+\log U)/2\). Thus for real \(t>-2\),
\[
\mathbb E e^{tX}=\frac{e^{t/2}}{1+t/2},\qquad
\kappa_1(X)=0,\qquad \kappa_j(X)=\frac{(-1)^j(j-1)!}{2^j}\quad(j\ge2).
\]
At a leaf vertex of a forest, condition on all other sphere points. Its unique incident edge variable then has this universal law independent of the conditioning; remove the leaf and iterate. Hence forest edge variables are jointly independent, including any fixed powers and repetitions of individual edge variables.

**2. The spherical logarithmic potential spectrum.** The self-adjoint integral operator
\[
(Tf)(x)=\int_{\mathbb S^2}K(x,y)f(y)\,d\sigma(y),\qquad
K(x,y)=\log\frac{|x-y|}{2}+\frac12,
\]
has \(T1=0\). Funk--Hecke's formula assigns to every degree-\(\ell\) spherical harmonic the eigenvalue
\[
\lambda_\ell=\frac12\int_{-1}^1
\left[\frac12\log\frac{1-u}{2}+\frac12\right]P_\ell(u)\,du.
\]
For \(\ell\ge1\), the Legendre equation \(((1-u^2)P_\ell'(u))'=-\ell(\ell+1)P_\ell(u)\), orthogonality to constants, and integration by parts show
\[
\int_{-1}^1\log\frac{1-u}{2}P_\ell(u)\,du
=-\frac2{\ell(\ell+1)}.
\]
The boundary term vanishes because \((1-u)\log(1-u)\to0\). Hence \(\lambda_0=0\) and \(\lambda_\ell=-1/[2\ell(\ell+1)]\) with multiplicity \(2\ell+1\). The kernel is square-integrable and \(T\) is Hilbert--Schmidt.

**3. Every simple cycle moment.** For distinct vertices \(v_1,\ldots,v_k\) ordered cyclically, \(k\ge3\),
\[
\mathbb E\prod_{i=1}^k K(P_{v_i},P_{v_{i+1}})
=\operatorname{Tr}(T^k)=\sum_{\ell\ge1}(2\ell+1)\lambda_\ell^k,
\qquad v_{k+1}=v_1.
\]
This is an absolutely convergent identity. Indeed \(K\in L^q(\mathbb S^2\!\times\mathbb S^2)\) for every finite \(q\), so the absolute cycle integral is finite by Hölder. The equality follows for bounded truncations of \(K\), then by their convergence in \(L^k\) on the cycle space and in Hilbert--Schmidt norm (therefore in trace norm for the \(k\)-th powers). Every proper subset of the cycle edges is a forest of centered independent variables, making every nontrivial moment-partition term vanish. The joint cumulant consequently equals this cycle moment. Since all \(\lambda_\ell<0\), the sum is nonzero with sign \((-1)^k\). The first eigenvalue gives the displayed large-\(k\) estimate; the rest are bounded by a constant multiple of \((1/12)^k\).

**4. Girth in the scalar law.** For a cyclic graph, expand the order-\(j\) cumulant of the weighted sum by multilinearity. If \(j<g\), all distinct edges appearing in any such term form a forest. A mixed cumulant involving more than one distinct edge is zero by Step 1, even if an edge is repeated. At \(j=g\), the only additional terms arise from all \(g\) edges of a shortest simple cycle, each occurring once. Every cycle contributes \(g!\tau_g\prod_{e\in C}w_e\) to the order-\(g\) cumulant; no other edge-supported terms survive. Therefore, with \(S_w=\sum_e w_eX_e\),
\[
\kappa_g(S_w)-\kappa_g(X)\sum_e w_e^g
=g!\tau_g\sum_{C\in\mathcal C_g(G)}\prod_{e\in C}w_e,
\]
and all analogous differences at lower positive orders vanish. Moment generating functions are analytic in a neighborhood of zero: a generalized Hölder bound reduces their finiteness to that of a single edge variable for sufficiently small \(|t|\). Division by \(g!\) proves the claimed Taylor expansion. For positive weights there is no cancellation because \(\tau_g\) has a strict common sign. For a forest, Step 1 gives equality of all moment generating functions throughout their common domains. Since \(\operatorname{Var}(X)=1/4\) and distinct edges are pairwise independent, \(\operatorname{Var}(S_G)=m/4\); the asserted inverse recovery follows.

**5. Exact zeta constants.** Partial fractions of the absolutely convergent rational sums
\[
\tau_k=\frac{(-1)^k}{2^k}\sum_{\ell\ge1}\frac{2\ell+1}{\ell^k(\ell+1)^k}
\]
give the stated values for orders three, four and five. They may also be verified by direct symbolic summation as described below.

## Verification

Run `python3 CHECK.py` with SymPy and mpmath available. The checker reconstructs Legendre coefficients by exact polynomial integration against logarithmic moments for degrees one through sixteen, compares cycle traces with exact zeta expressions for orders three through five, checks trace tails and signs for multiple orders, independently tests the one-edge moment generating function. Its finite numerical and symbolic tests supplement, but do not replace, the all-graph spectral and cumulant proof above. The scalar cumulant reconstruction requires the full population law, not finite samples.

## Relationship to prior work

Marshall and Martin (2026) derive the density and geometric applications of the cross ratio of four uniform spherical points. The earlier four-point logarithmic cross-ratio moment calculation gives the \(k=4\) constant above; this work does not claim that constant again. A separate published 2026 note, *Girth from the first cumulant defect of random spherical overlap sums*, treats **linear inner-product** edges and obtains graph-girth cumulant coefficients proportional to powers of the sphere dimension; it does not establish the zeta-valued logarithmic-potential cycle spectrum or the present scalar-law formula. Classical spin high-temperature expansions provide the general cycle/graph method. The distinction is between the linear spin kernel and the singular Green-type logarithmic chord kernel, whose spectrum contributes genuinely different constants. This result claims no discovery of forest independence as a general probabilistic technique or of the spherical harmonic eigenvalues in isolation.

## Limitations

The mathematical scope is finite graphs and random points on the ordinary two-sphere. The cycle coefficients are exact for logarithmic chord energies, not universal for arbitrary isotropic functions. The graph itself need not be recoverable from the scalar distribution. The special four-cycle trace and the generic graph-cumulant method are antecedents, and closely related older graphon or potential-theoretic formulations may exist under other terminology. The research review is not an independent mathematical audit. No numerical experiment can independently establish the all-graph theorem.

## References

1. T. Marshall and G. Martin, *Random complex cross ratios*, arXiv:2611.07670v1, publicly posted 5 November 2026, https://arxiv.org/abs/2611.07670.
2. *Girth from the first cumulant defect of random spherical overlap sums*, publicly archived mathematical finding (2026), on classical spherical inner-product edge statistics.
3. R. Peled and Y. Spinka, *Lectures on the Spin and Loop \(O(n)\) Models*, arXiv:1708.00058, especially Section 2.4, https://arxiv.org/abs/1708.00058.
4. N. N. Lebedev, *Special Functions and Their Applications*, classical Legendre polynomial identities and Funk--Hecke normalization.
