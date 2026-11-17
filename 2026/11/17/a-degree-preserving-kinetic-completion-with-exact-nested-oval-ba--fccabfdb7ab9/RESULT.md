# A degree-preserving kinetic completion with exact nested-oval basins and Floquet data

## Finding

A polynomial modification of the nested algebraic-oval chemical oscillator of Craciun and Erban preserves **each original periodic orbit pointwise as a parametrized trajectory**, including its original-time period and transverse Floquet multiplier, yet makes the complete positive-quadrant basin structure explicit. It realizes **exactly** any prescribed positive integer number of algebraic limit cycles, rather than only a guaranteed lower bound, without increasing polynomial degree or sacrificing mass-action realizability.

Fix any integer \(N\ge1\), distinct real numbers \(0<\delta_1<\cdots<\delta_N\), and \(\varepsilon>0\). Define
\[
L(x,y)=(x+1+x^{-1})(y+1+y^{-1})-9,
\quad P(z)=\prod_{j=1}^{N}(z-\delta_j),
\]
\[
h_{\delta}(x,y)=x^2y^2+x^2y+xy^2+x^2+y^2+x+y+1-(8+\delta)xy,
\quad H(x,y)=\prod_{j=1}^{N}h_{\delta_j}(x,y).
\]
Write \(F_0(x,y)=((1-x)(1+y),(1-y)(1+x))\) and \(J(a,b)=(-b,a)\). Consider the **polynomial** vector field on the strictly positive quadrant
\[
\boxed{\;\dot{\mathbf x}=H F_0+\varepsilon xy J\nabla H
             +\varepsilon N H(x,-y),\qquad \mathbf x=(x,y).\;}
\tag{1}
\]
The last summand is the completion term. It vanishes on every prescribed oval. The originating field is the same expression with that last summand omitted.

**Complete classification.** The flow (1) is globally forward complete in the strictly positive quadrant; its unique equilibrium is \((1,1)\), and its only nonconstant periodic orbits are precisely the \(N\) ovals
\[
\mathcal C_i=\{(x,y)>0:L(x,y)=\delta_i\}=\{h_{\delta_i}=0\},\qquad 1\le i\le N.
\]
They are all hyperbolic. The oval \(\mathcal C_i\) is attracting if \(N-i\) is even and repelling if \(N-i\) is odd. The equilibrium is a hyperbolic attracting focus for even \(N\), and a hyperbolic repelling focus for odd \(N\).

The basins have an exact level-set description. Put \(\delta_0=0\) and \(\delta_{N+1}=+\infty\). An initial point on \(L=\delta_i\) remains on \(\mathcal C_i\), and \((1,1)\) is stationary. For \(k\in\{0,\ldots,N\}\), if
\(\delta_k<L(x(0),y(0))<\delta_{k+1}\), then its forward orbit approaches the set \(L=\delta_k\) when \(N-k\) is even, or the set \(L=\delta_{k+1}\) when \(N-k\) is odd. In the first alternative with \(k=0\), the limiting set is the equilibrium. The parity-incompatible infinite endpoint never arises, since \(N-k=0\) for \(k=N\).

**Unchanged physical clocks and transverse spectra.** On \(\mathcal C_i\), the completed and originating fields coincide as vectors; therefore both have the same minimal physical-time period \(T_i\). Let \(ds\) denote Euclidean arclength and let \(\Omega_i=\{L<\delta_i\}\) be the bounded interior of \(\mathcal C_i\). Then, for **both** systems,
\[
\boxed{\quad
T_i=\frac1{\varepsilon |P'(\delta_i)|}\oint_{\mathcal C_i}
\frac{ds}{(xy)^{N+1}|\nabla L|},\quad
\mu_i=\exp\!\left[-\frac{\operatorname{sgn}P'(\delta_i)}{\varepsilon}\,
\mathcal A(\delta_i)\right],\quad}
\tag{2}
\]
where \(\mu_i\) is the nontrivial Poincaré multiplier and
\[
\boxed{\quad\mathcal A(\delta)
=\iint_{\Omega_\delta}\left(
\frac{1+y^{-1}}{x^2}+\frac{1+x^{-1}}{y^2}
\right)\,dx\,dy>0.\quad}
\tag{3}
\]
In particular, the magnitude of the logarithmic transverse multiplier of each oval depends on its **own** level \(\delta_i\) and on \(\varepsilon\), but not on the number, positions or spacings of the other ovals. Their influence on stability is only the parity sign of \(P'(\delta_i)\); their influence on period appears through \(|P'(\delta_i)|\) and the common factor \((xy)^{N+1}\) in the time integral.

## Assumptions and scope

All parameters \(N,\delta_i,\varepsilon\) are as stated and held fixed. Statements concern classical solutions with \(x(0),y(0)>0\), the Euclidean original-time flow, and hyperbolicity in the planar Poincaré sense. The chemical-realization assertion is **mass-action realizability**, not weak reversibility or a minimal reaction count. No statement is made about arbitrary perturbations of (1), stochastic chemical kinetics, or global basins of the unmodified originating field.

The polynomial field (1) has exact total degree \(4N+2\), the same as the originating construction. Its boundary coordinate polynomials satisfy
\[
\dot x\big|_{x=0}=(1+y)(y^2+y+1)^N,
\quad\dot y\big|_{y=0}=(1+x)(x^2+x+1)^N.
\]
All coefficients of both expressions are nonnegative. Thus every negative coefficient in the \(\dot x\) polynomial occurs in a monomial containing \(x\), and analogously every negative coefficient in \(\dot y\) occurs in a monomial containing \(y\). Splitting terms into elementary nonnegative-rate production and consumption reactions realizes (1) by a finite two-species mass-action network of maximum reaction order \(4N+2\). The construction does not establish a reversible or weakly reversible realization.

## Proof

**1. A compact radial-like coordinate.** Direct multiplication gives
\[
 h_\delta(x,y)=xy\,[L(x,y)-\delta],\qquad
 H(x,y)=(xy)^N P(L(x,y)).
\tag{4}
\]
In logarithmic coordinates \(u=\log x,v=\log y\),
\[
L=(1+2\cosh u)(1+2\cosh v)-9.
\]
The function \(\log(9+L)=\log(1+2\cosh u)+\log(1+2\cosh v)\) is strictly convex and proper; its unique minimum is at \((u,v)=(0,0)\). Every \(L=\delta>0\) is therefore a regular smooth simple closed curve enclosing \((1,1)\), and each positive-quadrant sublevel \(L\le R<\infty\) is compact. Moreover \(\nabla L=0\) only at \((1,1)\).

**2. Polynomial identity and the strict Lyapunov law.** Differentiating (4),
\[
\nabla H=(xy)^N P'(L)\nabla L+N H\nabla\log(xy).
\]
Because \(xy J\nabla\log(xy)=(-x,y)\), the last two terms of (1) simplify exactly:
\[
\boxed{\quad \dot{\mathbf x}=(xy)^N P(L)F_0
       +\varepsilon(xy)^{N+1}P'(L)J\nabla L.\quad}
\tag{5}
\]
Although its representation uses reciprocal coordinates, (5) is polynomial by the equivalent expression (1). Taking a scalar product with \(\nabla L\) yields the exact identity
\[
\dot L=- (xy)^N P(L)D(x,y),
\]
\[
D=(y+1+y^{-1})\frac{(x-1)^2(x+1)(y+1)}{x^2}
 +(x+1+x^{-1})\frac{(y-1)^2(y+1)(x+1)}{y^2}.
\tag{6}
\]
Here \(D>0\) away from \((1,1)\) and \(D(1,1)=0\). Consequently \(L\) is strictly decreasing or increasing between consecutive zero levels of \(P\), with the direction determined by \(-\operatorname{sgn}P\). No trajectory crosses a level \(L=\delta_i\), because the vector field is tangent there. Thus any interior positive trajectory is trapped in a finite compact sublevel \(L\le R\), proving forward completeness and precluding axis contact and escape.

Within any open interval between consecutive roots, \(L(t)\) is strictly monotone and bounded. Its limit must be the appropriate endpoint: otherwise \(D(x,y)\) and \(|P(L)|\) are uniformly separated from zero on the compact strip away from the unique center, giving a contradiction to convergence. The only zero level at the origin of the level scale is \((1,1)\). This proves the stated basin classification. Since any nonconstant periodic trajectory would make \(L(t)\) periodic, (6) forces it to lie on one of the \(N\) prescribed levels. On such a level, (5) reduces to a nonvanishing tangent field because \(P'(\delta_i)\neq0\) and \(\nabla L\neq0\). Each is therefore a single periodic orbit, not a set of equilibria. Equation (6) rules out every other equilibrium, and (5) vanishes at \((1,1)\).

**3. Stability and the center.** Near \(\mathcal C_i\), set \(s=L-\delta_i\). Then
\[
\dot s=-(xy)^N D\,P'(\delta_i)s+O(s^2).
\]
Because the sign is fixed along the compact oval, \(P'(\delta_i)=\prod_{j\neq i}(\delta_i-\delta_j)\) determines hyperbolicity and the alternating stability. At \((1,1)\) the linearization of (5) has eigenvalues
\[
-2P(0)\pm6i\varepsilon P'(0),
\]
whose real parts are negative exactly when \(N\) is even. This also excludes degenerate center behavior.

**4. Period and Floquet integral.** Along \(\mathcal C_i\), equation (5) has speed \(\varepsilon(xy)^{N+1}|P'(\delta_i)|\,|\nabla L|\), giving the period in (2). The transverse variational logarithm of (6) over one orbit equals
\[
\log\mu_i
=-\int_0^{T_i}(xy)^N P'(\delta_i)D\,dt
=-\frac{\operatorname{sgn}P'(\delta_i)}{\varepsilon}
\oint_{\mathcal C_i}\frac{D}{xy|\nabla L|}\,ds.
\]
The outward unit normal of the oval is \(\nabla L/|\nabla L|\), and \(F_0\cdot\nabla L=-D\). The divergence theorem applied to the smooth vector field \(F_0/(xy)\) on the strictly positive compact domain \(\Omega_i\) yields
\[
\oint_{\mathcal C_i}\frac{D}{xy|\nabla L|}\,ds
=-\iint_{\Omega_i}\operatorname{div}\!\left(\frac{F_0}{xy}\right)dx\,dy
=\mathcal A(\delta_i),
\]
with the positive integrand (3).

**5. Why the original cycles retain their physical-time and transverse data.** Define the originating field \(F_{\mathrm{old}}=HF_0+\varepsilon xyJ\nabla H\). The difference from (1) is exactly \(\varepsilon N H(x,-y)\), zero on all the ovals, so their parametrized trajectories and periods agree. The function \(H\) is a local transverse defining coordinate at each oval. For the originating flow,
\[
\dot H=H\,\nabla H\cdot F_0.
\]
For (1) there is the additional cofactor \(\varepsilon N(xH_x-yH_y)\). On each oval, where \(F_{\mathrm{old}}=\varepsilon xyJ\nabla H\), this added cofactor is the total physical-time derivative
\[
\varepsilon N(xH_x-yH_y)
=\frac{d}{dt}\big[N\log(xy)\big].
\]
Its integral over any complete orbit is zero. Therefore the cofactor integrals, hence the nontrivial Floquet multipliers, coincide exactly for both fields, proving the preservation assertion. The modified field's explicit global basins do **not** imply any unproved global classification for the originating field.

## Verification

The standalone script `check_kinetic_completion.py` evaluates the defining polynomial identity and exact Lyapunov derivative symbolically for \(N=1,2,3\) and rational sample levels, checks the correction and divergence identities, verifies polynomial coordinate fields and positive-axis boundary terms, and numerically tests the Lyapunov derivative at nonstationary sample points. It completed with `KINETIC_COMPLETION_CHECK_OK`. The general theorem follows from the analytic proof above, not from finite case checks. All integrals in (2)–(3) are proper: the oval is smooth and stays strictly inside the positive quadrant, with \(|\nabla L|>0\).

## Relationship to prior work

Craciun and Erban [1] constructed the nested quartic levels \(h_{\delta_i}=0\), the originating polynomial field and mass-action realizations; their Theorem 1 asserts at least \(N\) algebraic cycles. Their Theorem 2 provides a local transversality criterion. **Those ingredients and the existence of the oval family are not new.** Here, by contrast, the explicit correction preserves each originating orbit's original-time period and Floquet multiplier while supplying a single globally monotone scalar on the entire positive quadrant. This yields exact cycle count, all attraction/repulsion parities, all positive basins and a universal per-oval integral for the transverse multiplier. Gasull and Giacomini [2] provide general invariant-algebraic-curve and nonexistence techniques, not this completed nested-oval field or these explicit global basins. Existing constructions with prescribed circular cycles are not automatically the same vector field, nor do they imply preservation of these quartic oval clocks and Floquet spectra.

## Limitations

The corrected mass-action realization is not claimed to be reversible or weakly reversible, and no minimal molecularity or reaction-channel count is proved. The source's unmodified field is **not** claimed to have the same global basins: only the stated cycles and their on-orbit linear data are conserved. No robustness statement for generic parameter perturbations, stochastic kinetics, or the entire real plane is asserted. Although targeted literature and mathematical-record searches did not identify a stronger result already implying this precise completion, a general unindexed theorem about Lyapunov-complete planar polynomial fields remains a priority risk.

## References

[1] G. Craciun and R. Erban, *Planar chemical reaction systems with algebraic and non-algebraic limit cycles*, arXiv:2406.05057 (first public version 7 June 2024); *Journal of Mathematical Biology* 90, 64 (2025), DOI:10.1007/s00285-025-02221-0. The construction and local criterion are in Sections 4.1 and 5, especially equations (4.27)–(4.30) and Theorems 1–2.

[2] A. Gasull and H. Giacomini, *Number of limit cycles for planar systems with invariant algebraic curves*, arXiv:2210.15803 (27 October 2022); *Qualitative Theory of Dynamical Systems* 22, 44 (2023), DOI:10.1007/s12346-023-00746-7. General invariant-curve/cofactor methodology and results principally for quadratic systems.
