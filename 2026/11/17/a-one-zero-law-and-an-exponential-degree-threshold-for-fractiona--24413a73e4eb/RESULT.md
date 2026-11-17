# A one-zero law and an exponential degree threshold for fractional Bergman Blaschke multipliers

## Finding
Equip the weighted disk Bergman space \(A^2_{\epsilon-1}(\mathbb D)\), \(0<\epsilon<1\), with its usual normalized area norm. For each integer \(k\ge1\), let
\[
\mathcal E_k=\overline{\operatorname{span}}\{z^{kn}:n\ge0\},\quad
F_{\epsilon,k}(u)=\sum_{n=0}^{\infty}\frac{\Gamma(kn+1+\epsilon)}{\Gamma(1+\epsilon)\Gamma(kn+1)}u^n,
\]
and define the positive one-dimensional integral
\[
J_{\epsilon,k}=\frac{\sin(\pi\epsilon)}{\pi}
\int_0^1\frac{t^\epsilon(1-t^k)}{(1-t)^{1+\epsilon}(1+t^k)}\,dt.
\]
There is a unique real \(\kappa(\epsilon)>1\) at which the same integral, with real \(k\), equals one. For every positive integer \(k\), the function \(F_{\epsilon,k}\) is zero-free in \(|u|<1\) **if and only if** \(J_{\epsilon,k}\le1\), equivalently \(k\le\kappa(\epsilon)\). If \(J_{\epsilon,k}>1\), it has **exactly one zero**, a simple negative real number \(-r_{\epsilon,k}\in(-1,0)\), and no others in the disk. At equality its sole boundary zero is at \(u=-1\).

This is also an exact phase diagram for a natural *specified cyclic invariant subspace*, rather than an assertion about all invariant subspaces. For \(0\le a<1\), put
\[
B_{k,a}(z)=\frac{z^k-a}{1-a z^k}.
\]
The space \(\mathcal E_k\) is invariant and cyclic under multiplication by \(B_{k,a}\), and its one-dimensional wandering space is spanned by \(g(z)=F_{\epsilon,k}(a z^k)\). If \(J_{\epsilon,k}\le1\), this vector generates \(\mathcal E_k\) for **every** \(0\le a<1\). If \(J_{\epsilon,k}>1\), it generates \(\mathcal E_k\) **exactly when** \(a\le r_{\epsilon,k}\). For \(r_{\epsilon,k}<a<1\), its generated subspace is proper, furnishing an explicit degree-\(k\) Blaschke multiplier with a cyclic invariant subspace lacking wandering generation.

The least degree where this *canonical kernel-zero mechanism* can fail is
\[
k_{\mathrm{crit}}(\epsilon)=\min\{k\in\mathbb Z_{\ge1}:J_{\epsilon,k}>1\}
=\lfloor\kappa(\epsilon)\rfloor+1.
\]
It grows at the sharp exponential scale
\[
\boxed{\quad k_{\mathrm{crit}}(\epsilon)\sim
\frac{\pi e^{-\gamma}}2\,2^{1/\epsilon}\quad(\epsilon\downarrow0),\quad}
\]
where \(\gamma\) is the Euler--Mascheroni constant. In particular, the fraction of the exponent is not merely a lower or upper estimate: the explicit universal prefactor is attained asymptotically. No claim is made that this is the least degree among *all* possible Blaschke products or invariant subspaces.

## Assumptions and scope
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), \(dA=dx\,dy/\pi\), and
\[
\|f\|^2_{\epsilon-1}=\epsilon\int_{\mathbb D}|f(z)|^2(1-|z|^2)^{\epsilon-1}\,dA(z).
\]
The usual beta integral gives \(\|z^j\|^2=\Gamma(1+\epsilon)\Gamma(j+1)/\Gamma(j+1+\epsilon)\). All closures and orthogonal complements use this original norm. The real parameter \(a\) lies in \([0,1)\). The threshold \(\kappa(\epsilon)\) uses the continuous real extension of \(J_{\epsilon,k}\), but a Blaschke degree is always an integer. The analytic assertions concern the open disk; boundary equality is handled separately. The operator is studied only on \(\mathcal E_k\).

## Proof
**1. A Hausdorff-moment identity.** Write \(b_j=\Gamma(j+1+\epsilon)/[\Gamma(1+\epsilon)\Gamma(j+1)]\). For integers \(j\ge0\), beta integration and the reflection identity yield
\[
b_{j+1}-b_j=\frac{\sin(\pi\epsilon)}\pi
\int_0^1 t^{j+\epsilon}(1-t)^{-\epsilon}\,dt.
\]
Thus \(c_n=b_{kn}-b_{k(n-1)}\), \(n\ge1\), is a sequence of positive Hausdorff moments:
\[
c_n=\int_0^1(t^k)^{n-1}\,d\mu_{\epsilon,k}(t),\qquad
d\mu_{\epsilon,k}(t)=\frac{\sin(\pi\epsilon)}\pi
\frac{t^\epsilon(1-t^k)}{(1-t)^{1+\epsilon}}dt.
\]
This is a finite positive measure because \(0<\epsilon<1\); hence \(c_n\) decreases strictly to zero. On \(|u|<1\), multiplication of the series by \(1-u\) gives
\[
D_{\epsilon,k}(u):=(1-u)F_{\epsilon,k}(u)
=1+\int_0^1\frac{u}{1-t^k u}\,d\mu_{\epsilon,k}(t).
\]
The integral extends holomorphically through every point of the unit circle except possibly \(u=1\). In particular, \(D_{\epsilon,k}(-1)=1-J_{\epsilon,k}\) and \(F_{\epsilon,k}(-1)=(1-J_{\epsilon,k})/2\) by analytic continuation.

**2. The exhaustive zero classification.** For nonreal \(u\) in the disk,
\[
\operatorname{Im}D_{\epsilon,k}(u)
=\operatorname{Im}(u)\int_0^1|1-t^k u|^{-2}d\mu_{\epsilon,k}(t),
\]
so it cannot vanish. For \(0\le u<1\), \(D(u)>0\). On \((-1,0)\), \(D'(u)=\int(1-t^k u)^{-2}d\mu>0\); hence there is exactly one simple negative real zero when \(D(-1)<0\), and none when \(D(-1)\ge0\). The zero of \(D\) is also a simple zero of \(F\), since \(1-u\ne0\). For \(J\le1\), the stronger estimate \(\operatorname{Re}[u/(1-tu)]>-1/(1+t)\) for \(|u|<1\), \(0<t<1\), also gives \(\operatorname{Re}D(u)>0\). At \(J=1\) the continuation has the simple zero \(u=-1\), but no open-disk zero.

**3. A unique degree threshold.** The integrand in \(J_{\epsilon,k}\) is strictly increasing with real \(k>0\), because \((1-t^k)/(1+t^k)\) increases for every \(0<t<1\). Its integral is continuous in \(k\) on compact parameter intervals. For \(k=1\), \(F_{\epsilon,1}(u)=(1-u)^{-1-\epsilon}\), whence \(J_{\epsilon,1}=1-2^{-\epsilon}<1\). Monotone convergence as \(k\to\infty\) gives \(J_{\epsilon,k}\to\infty\), since the limiting integrand diverges nonintegrably at \(t=1\). This proves existence and uniqueness of \(\kappa(\epsilon)>1\), the strict integer cutoff, and the boundary convention.

**4. Wandering generation, including the zero-on-boundary case.** Under the isometric coefficient identification \(G(w)\mapsto G(z^k)\), the space \(\mathcal E_k\) becomes an analytic Hilbert space \(\mathcal H_k\) with squared monomial norms \(\|w^n\|^2_{\mathcal H_k}=\|z^{kn}\|^2_{\epsilon-1}\). Gamma-ratio asymptotics show that these norms are equivalent to the usual \(A^2_{\epsilon-1}\) norms; in particular all functions analytic beyond the closed disk are multipliers. As in the standard Bergman division lemma, for \(b_a(w)=(w-a)/(1-aw)\),
\[
b_a\mathcal H_k=\{G\in\mathcal H_k:G(a)=0\},\qquad
\mathcal H_k\ominus b_a\mathcal H_k=\mathbb C F_{\epsilon,k}(a\,\cdot).
\]
Division by \(w-a\) is bounded on the vanishing-at-\(a\) subspace, first in ordinary Bergman space by an automorphism and the bounded backward shift on functions vanishing at zero, and then in \(\mathcal H_k\) by norm equivalence. Both \(w=(b_a+a)/(1+a b_a)\) and \(b_a=(w-a)/(1-aw)\) are operator-norm limits of polynomials in the other multiplier: \(\|M_w\|\le1\), \(\|M_{b_a}\|\le1\) in the inherited area norm, so the geometric expansions converge. Consequently, \(1\) is cyclic for \(b_a\), and cyclicity of \(F_{\epsilon,k}(aw)\) for \(b_a\) is equivalent to its cyclicity for \(w\).

If \(F_{\epsilon,k}\) has no interior zero, \(F_{\epsilon,k}(aw)\) and its reciprocal extend analytically to a neighborhood of \(|w|\le1\), so it is an invertible multiplier and cyclic. The same holds when it has its only zero at \(-r\) and \(a<r\). At \(a=r<1\), factor \(F_{\epsilon,k}(rw)=(1+w)h(w)\), where \(h\) and \(1/h\) are analytic on a neighborhood of the closed disk, using the simple boundary zero. The factor \(1+w\) is cyclic, since
\[
(1+w)\sum_{j=0}^N(-w)^j=1-(-w)^{N+1},\qquad
\|w^{N+1}\|_{\mathcal H_k}\longrightarrow0.
\]
Thus the threshold equality is on the generating side. When \(a>r\), the wandering vector vanishes at every \(z\) satisfying \(z^k=-r/a\) inside \(\mathbb D\); its multiplier orbit vanishes there, whereas \(1\in\mathcal E_k\) does not. This proves the exact generation phase diagram.

**5. The sharp exponential constant.** The alternating-moment sum has the convergent representation
\[
J_{\epsilon,k}=\sum_{n=1}^\infty(-1)^{n-1}(b_{kn}-b_{k(n-1)}).
\]
For \(0<\epsilon\le1/2\), the uniform differentiated gamma-ratio expansion
\[
\frac{\Gamma(x+1+\epsilon)}{\Gamma(x+1)}
=x^\epsilon\left[1+\frac{\epsilon(1+\epsilon)}{2x}+O(x^{-2})\right]
\]
(with its differentiated remainder) implies, by summing the variation of the errors over \(n\ge1\),
\[
J_{\epsilon,k}=
\frac{2k^\epsilon}{\Gamma(1+\epsilon)}\eta(-\epsilon)-1
+O(k^{\epsilon-1}),\qquad k\ge2,
\]
where \(\eta(s)=(1-2^{1-s})\zeta(s)\) is Dirichlet's eta function; the implicit constant is uniform in \(\epsilon\in(0,1/2]\). To see the factor \(2\eta(-\epsilon)\), take Abel limits of the alternating differences \(n^\epsilon-(n-1)^\epsilon\), which form a decreasing sequence tending to zero. Set
\[
K_\epsilon=\left(\frac{\Gamma(1+\epsilon)}{\eta(-\epsilon)}\right)^{1/\epsilon}.
\]
At \(k=e^{\pm\delta}K_\epsilon\) the displayed main term is \(2e^{\pm\epsilon\delta}-1\), strictly below or above one; its error is exponentially smaller than \(\epsilon\) as \(\epsilon\downarrow0\). Strict monotonicity of \(J\) therefore gives \(\kappa(\epsilon)/K_\epsilon\to1\). Finally,
\[
\Gamma(1+\epsilon)=1-\gamma\epsilon+O(\epsilon^2),\qquad
\eta(-\epsilon)=\frac12-\frac\epsilon2\log\frac\pi2+O(\epsilon^2),
\]
so \(K_\epsilon=2^{1/\epsilon}(\pi/2)e^{-\gamma}(1+o(1))\). Taking the first integer strictly above \(\kappa\) does not affect the ratio because \(\kappa\to\infty\).

## Verification
Run `python CHECK.py` with SciPy and mpmath. The standalone script passes 73 finite numerical assertions covering monotonicity, the alternating-sum brackets, finite critical-degree brackets, a high-precision interior kernel zero, and the prefactor limit's numerical approach. These computations support, but do not replace, the infinite-dimensional and asymptotic proofs above. All analytic identities are derived with the stated gamma/beta normalization.

## Relationship to prior work
Xu and Yu, arXiv:2610.37035 (first public October 27, 2026), Theorem 12, prove existence of a nonwandering canonical Blaschke multiplier for all sufficiently large degrees at every Bergman weight, and Example 13 gives degree three at the unweighted weight. The present result treats the **negative weight interval** \(-1<\alpha<0\), supplies the exact one-zero/zero-free dichotomy at each degree, the full multiplier-parameter transition on \(\mathcal E_k\), and an exponential *least-witness-degree* asymptotic with explicit prefactor; these are not stated or implied quantitatively by their eventual-existence estimate. Related published calculations give an exact degree-two canonical threshold for arbitrary Bergman weight and a degree-two minimum over a positive-weight range; neither determines the degree transition for general \(k\) as \(\alpha\downarrow-1\). Gallardo-Gutiérrez, Partington, and Seco (2019/2020) treat monomial multipliers and equivalent Hilbert norms; their sufficient logarithmic condition is not a classification of the Möbius-transformed canonical multiplier in the original norm. General root-of-unity multisection identities are known, but alone do not supply the positive-measure zero-classification and the degree threshold established here.

## Limitations
The threshold classifies kernel zeros and wandering generation on the fixed invariant subspace \(\mathcal E_k\) only; it does not identify the minimum degree for arbitrary Blaschke products or prove the full Beurling-type theorem. It is restricted to \(0<\epsilon<1\) and real \(a\in[0,1)\); no extension outside those parameters is asserted. The prefactor is an \(\epsilon\downarrow0\) asymptotic, not an exact finite-degree formula. The finite checker cannot certify infinite claims. Equivalent older zero-distribution formulations not found in the inspected sources remain a bibliographic risk.

## References
1. S. Xu and T. Yu, *The Beurling-type theorem for powers of weighted Bergman shifts*, arXiv:2610.37035v1, first public October 27, 2026, https://arxiv.org/html/2610.37035v2, Sections 3--4, especially Lemma 11, Theorem 12, and Example 13.
2. E. Gallardo-Gutiérrez, J. R. Partington and D. Seco, *On the wandering property in Dirichlet spaces*, arXiv:1904.02974v1, April 5, 2019, https://arxiv.org/html/1904.02974v1.
3. Published finding, *A sharp degree-two Bergman kernel and wandering threshold*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-degree-two-bergman-kernel-and-wandering-threshold--fe3b5433aca8.
4. Published finding, *Degree-two Blaschke failure of wandering generation at the sharp positive Bergman-weight threshold*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-degree-two-blaschke-failure-of-wandering-generation-at-the-sharp--6667f5fce44a.
5. T. Simpson's classical series multisection identity (1757), as summarized in https://en.wikipedia.org/wiki/Series_multisection; background identity only, not a zero theorem.
