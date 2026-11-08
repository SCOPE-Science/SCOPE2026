# Unique optimal resetting and a universal strong-outward-drift law for a partially reactive point target

## Finding
For an outward-drifting one-dimensional Brownian searcher with a partially absorbing point target, the mean killing time has exactly one positive optimum in resetting rate whenever the outward Péclet number \(b=uL/(2D)\ge1\). At fixed reactivity-to-drift ratio \(\eta=k/u>0\), as \(b\to\infty\), the unique optimum and optimal mean time satisfy
\[
r_* =\frac{u}{L}+\frac{2D}{L^2}\frac{\eta}{1+\eta}+O\!\left(\frac{D}{bL^2}\right),\qquad
T_* =\frac{L}{u}\left(1+\frac1\eta\right)\exp\!\left(1+\frac{uL}{D}\right)\left[1+O(b^{-1})\right].
\]
The correction to the dimensionless optimal spectral displacement \(\sqrt{b^2+r_*L^2/D}-b\) changes sign at \(\eta=1\), though the correction to \(r_*\) is strictly positive.

## Assumptions and scope
Fix \(D,u,k,L>0\). The searcher evolves on \(\mathbb R\) by \(dX_t=u\,dt+\sqrt{2D}\,dW_t\), starts at \(X_0=L\), and is reset instantaneously to \(L\) at independent Poisson rate \(r>0\). Killing is implemented by the point sink \(-k\delta_0 p\) in the forward diffusion equation, equivalently an exponential local-time hazard with this normalization. The drift \(u>0\) points **away** from the target at zero. The asymptotics require \(b=uL/(2D)\to\infty\) with \(\eta=k/u\in(0,\infty)\) fixed, so both the drift and sink strength scale together at fixed \(D,L\), or equivalently compatible parameter families. The uniqueness statement needs only \(b\ge1\), not this asymptotic scaling.

## Proof
Write \(q=\sqrt{b^2+rL^2/D}>b\) and \(a=kL/(2D)>0\), so \(a=\eta b\) in the strong-drift regime. The free resolvent of generator \(D\partial_{xx}+u\partial_x\) at the target gives \(G_r(0,L)=e^{-(b+q)}/[(2D/L)q]\) and \(G_r(0,0)=1/[(2D/L)q]\). The rank-one sink resolvent therefore gives the absorption-before-reset probability
\[
p_r=\frac{kG_r(0,L)}{1+kG_r(0,0)}=\frac{a}{a+q}e^{-(b+q)}.
\]
The renewal identity for independent resets gives the exact mean killing time
\[
T(r)=\frac{1-p_r}{rp_r}=\frac{L^2}{D}\frac{(1+q/a)e^{b+q}-1}{q^2-b^2}.
\]
This is the known mean-time resolvent relation, not the novel assertion.

Set \(y=q-b>0\), \(C=a+b+y\). Up to a positive constant the function to minimize is \(F(y)=[e^{2b+y}C-a]/[y(2b+y)]\). Differentiation gives the sign of \(F'(y)\) as the sign of
\[
K(y)=H(y)+2a(b+y)e^{-2b-y},\quad
H(y)=y^3+(a+3b-1)y^2+2(a+b)(b-1)y-2b(a+b).
\]
For \(b\ge1\), \(K(0)=-2b(a+b)+2ab e^{-2b}<0\), and \(K(y)\to\infty\). Moreover,
\[
K''(y)=6y+2(a+3b-1)+2a e^{-2b-y}(b+y-2)>0.
\]
Indeed, if \(b+y\ge2\) the final summand is nonnegative; otherwise it is bounded below by \(-2a\), while the first two terms are at least \(2a+4\). Thus \(K\) is strictly convex, starts negative and eventually becomes positive. A strictly convex function with these properties has exactly one positive zero; \(F\) decreases then increases, with \(F(y)\to\infty\) at both endpoints. This proves global uniqueness.

For fixed \(\eta>0\), set \(a=\eta b\). On each fixed bounded \(y\)-interval, \(K(y)/[2(1+\eta)b^2]=y-1+O(b^{-1})\), uniformly. The root is therefore trapped between \(1/2\) and \(2\) for sufficiently large \(b\), and tends to one. Using the exact stationary equation \(F'(y)=0\), divide by \(F\) to obtain
\[
1+\frac{1}{a+b+y}-\frac1y-\frac1{2b+y}+O(e^{-2b})=0
\]
uniformly on \([1/2,2]\). Taylor expansion with \(y=1+c/b+O(b^{-2})\) yields \(c=\tfrac12-(1+\eta)^{-1}\). The implicit-function argument is valid because the leading derivative with respect to \(y\) is one at \(y=1\); the exponentially small term does not affect either coefficient. Consequently
\[
\frac{r_*L^2}{D}=q_*^2-b^2=2b+\frac{2\eta}{1+\eta}+O(b^{-1}).
\]
Substituting \(y_*=1+O(b^{-1})\) into the exact \(T(r)\), and using \(2b=uL/D\), yields the stated optimal-time equivalent with relative error \(O(b^{-1})\).

## Verification
The included `verify.py` checks the exact derivative polynomial and second-derivative identities in symbolic algebra, then computes positive roots for 28 combinations of outward Péclet number and reactivity ratio. The proof of uniqueness and the asymptotic equivalents is analytic; finite checks do not establish the universal statements.

## Relationship to prior work
Mazzolo (2026) supplies the drifted delta-killing resolvent and survival analysis from which the mean-time representation follows. Whitehouse, Evans, and Majumdar (2013) treat imperfect resetting capture without outward drift. Related gated drift–diffusion studies discuss optimal resetting with a switchable target, rather than the fixed finite delta-sink asymptotic here. The additional claimed result is the uniqueness threshold \(b\ge1\), the universal leading law \(r_*\sim u/L\), and the finite-reactivity correction in the joint large-drift/large-reactivity limit. This is not a claim to a new resolvent or to discovering reset optimization in drifted diffusion.

## Limitations
The uniqueness theorem is stated only for \(b\ge1\); no claim is made about \(0<b<1\). The expansion assumes \(\eta\) fixed strictly positive and does not cover simultaneous weak-reactivity limits. The full Mazzolo preprint and journal PDF could not be independently inspected at this stage, so publication-priority comparison with sections beyond indexed abstracts remains open. No external independent audit has been performed.

## References
1. Alain Mazzolo, *Diffusion with stochastic resetting in the presence of a delta killing trap: Drift-controlled survival regimes*, arXiv:2609.22527, first submitted 2026-09-18; Phys. Rev. E **114**, 044105 (2026). https://arxiv.org/abs/2609.22527
2. J. Whitehouse, M. R. Evans, and S. N. Majumdar, *Effect of Partial Absorption on Diffusion with Resetting*, Phys. Rev. E **87**, 022118 (2013). https://doi.org/10.1103/PhysRevE.87.022118
3. *Rate enhancement of gated drift-diffusion process by optimal resetting*, J. Chem. Phys. **159**, 054111 (2023). https://doi.org/10.1063/5.0154210
