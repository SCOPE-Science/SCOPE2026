# Exact Lipschitz-budget projections for symmetric signed-density hyperplanes

## Finding

Let \(a>0\), let \(w\in L^1(0,a)\) be strictly positive almost everywhere, and assume \(2\int_0^a w(t)\,dt=1\). On the real Banach space \(X=C([-a,a])\) with the supremum norm, define the norm-one functional
\[
\mu_w(f)=\int_0^a w(t)\bigl(f(t)-f(-t)\bigr)\,dt,
\qquad Y_w=\ker\mu_w.
\]
For \(L\ge0\), define the regularized projection constant
\[
\Lambda_w(L)=\inf\left\{\|P_g\|:\ P_g f=f-\mu_w(f)g,\ \mu_w(g)=1,\ \operatorname{Lip}(g)\le L\right\},
\]
where an empty infimum is \(+\infty\). The Lipschitz seminorm is taken over the whole interval. Put
\[
L_c=\left(2\int_0^a t w(t)\,dt\right)^{-1},\qquad
F_L(M)=2\int_0^a w(t)\min\{M,Lt\}\,dt.
\]
**Exact budget and unique optimizer.** If \(L<L_c\), then \(\Lambda_w(L)=+\infty\). For every finite \(L\ge L_c\) there is exactly one \(M_L\in(0,La]\) satisfying \(F_L(M_L)=1\), and
\[
\boxed{\Lambda_w(L)=1+M_L.}
\]
The **unique** correction function attaining this minimum is the clipped ramp
\[
\boxed{g_L(x)=\max\{-M_L,\min\{Lx,M_L\}\}\quad(-a\le x\le a).}
\]
In particular, \(M_{L_c}=aL_c\), \(M_L>1\) for each finite admissible \(L\), and \(M_L\downarrow1\) as \(L\to\infty\). Thus the unrestricted projection constant is \(2\), never attained.

**Sharp local-density law.** If, for some \(\beta>-1\) and \(c>0\),
\[
w(t)=c t^\beta(1+o(1))\qquad(t\downarrow0),
\]
then the exact leading regularity penalty is
\[
\boxed{\Lambda_w(L)-2\sim\frac{2c}{(\beta+1)(\beta+2)}L^{-(\beta+1)}.}
\]
Every positive decay exponent occurs for a natural one-parameter family of absolutely continuous signed functionals, without changing their unregularized projection constant.

For explicit formulas take \(a=1/2\) and \(w_\beta(t)=(\beta+1)2^\beta t^\beta\), where \(\beta>-1\). Then
\[
L_c=\frac{2(\beta+2)}{\beta+1},\qquad
\boxed{M_L-\frac{2^{\beta+1}}{\beta+2}\frac{M_L^{\beta+2}}{L^{\beta+1}}=1},
\qquad 1<M_L\le L/2.
\]
Writing \(q_\beta=2^{\beta+1}/(\beta+2)\), the two-term expansion is
\[
\boxed{\Lambda_\beta(L)=2+q_\beta L^{-(\beta+1)}
+(\beta+2)q_\beta^2 L^{-2(\beta+1)}+O_\beta(L^{-3(\beta+1)}).}
\]
Equivalently, the least feasible regularity budget for projection norm at most \(2+\varepsilon\) is
\[
\boxed{L_{\min}(\varepsilon)=
\begin{cases}
\bigl(q_\beta(1+\varepsilon)^{\beta+2}/\varepsilon\bigr)^{1/(\beta+1)},&0<\varepsilon<1/(\beta+1),\\[2pt]
2(\beta+2)/(\beta+1),&\varepsilon\ge1/(\beta+1).
\end{cases}}
\]
At \(\beta=0\), \(L_c=4\) and \(M_L=\frac L2(1-\sqrt{1-4/L})\) for \(L\ge4\).

## Assumptions and scope

All functions, measures, and projections are **real**. The assumptions include strict positivity of \(w\) almost everywhere on the *entire* positive half-interval, not only near zero; that hypothesis is used in uniqueness of the minimizer. The density may diverge integrably at zero when \(-1<\beta<0\). The normalized functional is the difference between a positive and a negative absolutely continuous measure, each of mass \(1/2\); the two supports touch at zero. The projection norm is computed on \(C([-a,a])\), not on the Lipschitz function space. Requiring a Lipschitz correction is a restriction on the coefficient of a rank-one correction, not a requirement that the projection preserve a fixed Lipschitz norm. The unregularized infimum ranges over **all bounded projections** onto \(Y_w\). The finite-budget infimum is over the subset with Lipschitz correction and is attained there.

## Proof

**1. Rank-one parametrization and norm.** The Jordan decomposition of \(\mu_w\) is positive on \((0,a]\), negative on \([-a,0)\), and has total variation \(2\int_0^a w=1\). It is not norm-attaining on \(C([-a,a])\): equality in \(|\mu_w(f)|\le\|f\|_\infty\) would force \(f=1\) almost everywhere on the positive half and \(f=-1\) almost everywhere on the negative half, up to a common global sign, contradicting continuity at zero. Every projection \(P\) onto the codimension-one space \(Y_w\) uniquely has \(P=P_g=I-\mu_w\otimes g\) with \(\mu_w(g)=1\). Indeed, \(I-P\) vanishes on \(Y_w\), hence factors through \(X/Y_w\cong\mathbb R\), and idempotence gives the displayed normalization. The rank-one Daugavet identity for \(C(K)\) on a compact interval without isolated points gives
\[
\|P_g\|=\|I-\mu_w\otimes g\|=1+\|\mu_w\|\,\|g\|_\infty=1+\|g\|_\infty.
\]
This identity, and the unconditional hyperplane projection constant \(2\), are classical input, not new statements.

**2. Sharp constrained moment bound.** If \(\|g\|_\infty\le M\) and \(\operatorname{Lip}(g)\le L\), then for every \(0<t<a\),
\[
g(t)-g(-t)\le2M,\qquad g(t)-g(-t)\le2Lt.
\]
Consequently \(\mu_w(g)\le F_L(M)\). This bound is attained simultaneously at every \(t\) by the clipped ramp \(g_{M,L}(x)=\max\{-M,\min\{Lx,M\}\}\), because \(g_{M,L}(t)-g_{M,L}(-t)=2\min\{M,Lt\}\). Thus \(F_L(M)\) is the **exact** maximum attainable value of the functional under both bounds, not merely an upper estimate.

For fixed \(L>0\), \(F_L\) is continuous and strictly increasing on \([0,La]\), since \(w>0\) almost everywhere; it is constant at \(2L\int_0^a tw\) for \(M\ge La\). Therefore a function satisfying \(\mu_w(g)=1\) and \(\operatorname{Lip}(g)\le L\) exists precisely when \(L\ge L_c\). At and above that threshold the equation \(F_L(M)=1\) has exactly one root \(M_L\in(0,La]\). The clipped ramp of this amplitude satisfies \(\mu_w(g_L)=1\) and has \(\|g_L\|_\infty=M_L\). The sharp moment inequality excludes any smaller correction norm, and the rank-one norm identity gives \(\Lambda_w(L)=1+M_L\).

**3. Uniqueness.** Let \(g\) be another minimizing correction. Equality \(\mu_w(g)=F_L(M_L)\) and strict positivity of \(w\) imply
\[
g(t)-g(-t)=2\min\{M_L,Lt\}\quad\text{for almost every }t\in(0,a).
\]
By continuity this holds for all positive \(t\). When \(0<t<M_L/L\), equality in the Lipschitz bound across \([-t,t]\) forces \(g\) to be affine with slope \(L\) on that segment. By nestedness of these segments, \(g(x)=Lx+b\) on \([-M_L/L,M_L/L]\). If \(M_L/L<a\), then the equality for all \(t>M_L/L\) forces \(g(t)=M_L\) and \(g(-t)=-M_L\); continuity at the clipping points gives \(b=0\). If \(M_L/L=a\), the full affine segment is \([-a,a]\), and \(\|g\|_\infty=M_L=La\) forces \(b=0\). Hence the unique minimizer is \(g_L\).

**4. Unattained unregularized limit.** For each fixed finite \(L\), the strict inequality \(F_L(1)<1\) follows by integrating over the positive-measure set \((0,\min\{a,1/L\})\), so \(M_L>1\). For any fixed \(M>1\), dominated convergence gives \(F_L(M)\to M>1\) as \(L\to\infty\); thus eventually \(M_L<M\). It follows that \(M_L\downarrow1\). The unconstrained projection constant is therefore \(2\); attainment is excluded by nonattainment of \(\mu_w\) as in Step 1.

**5. Boundary-layer identity and asymptotics.** Since \(2\int w=1\) and \(M_L/L\le a\), subtracting the moment equation from \(M_L\) gives the exact identity
\[
M_L-1=2\int_0^{M_L/L}w(t)(M_L-Lt)\,dt.
\]
If \(w(t)\sim ct^\beta\), substitute \(t=M_Ls/L\) to obtain
\[
M_L-1=\frac{2cM_L^{\beta+2}}{L^{\beta+1}}
\left(\int_0^1s^\beta(1-s)\,ds+o(1)\right).
\]
The error follows from dominated convergence after using the local positive bound \(w(t)\le2ct^\beta\) for sufficiently small \(t\); \(s^\beta(1-s)\) is integrable precisely when \(\beta>-1\). The integral equals \(1/((\beta+1)(\beta+2))\). Since \(M_L\to1\), this proves the local-density law.

**6. Closed power family and inverse tradeoff.** Direct integration for \(w_\beta(t)=(\beta+1)2^\beta t^\beta\), \(a=1/2\), gives \(L_c=2(\beta+2)/(\beta+1)\) and the displayed scalar equation. Write \(z=L^{-(\beta+1)}\) and \(\delta=M_L-1\); then
\[
\delta=q_\beta z(1+\delta)^{\beta+2}.
\]
The implicit-function theorem at \((\delta,z)=(0,0)\), or direct successive substitution, gives \(\delta=q_\beta z+(\beta+2)q_\beta^2z^2+O(z^3)\). Solving the same exact equation for \(L\) at \(M_L=1+\varepsilon\), and remembering the absolute feasibility threshold \(L_c\), yields the inverse budget formula. At \(\varepsilon=1/(\beta+1)\) the two branches agree. This proves the formulas and the realization of every positive exponent \(\beta+1\).

## Verification

The standalone standard-library script `check.py` numerically checks the feasibility boundary, exact truncated integral, unique-amplitude root, sample strict lower amplitudes, the power-law limiting constant, and the special closed formula at \(\beta=0\). It passed **288** assertions across seven sample exponents, including integrable singular densities and a nonpower positive density. These finite tests are supplementary; they do not prove any universally quantified statement. The proof above supplies the exact inequalities and the limit. The script uses floating-point arithmetic, so very small asymptotic defects below numerical resolution are excluded from its asymptotic spot checks.

## Relationship to prior work

Kania and Lewicki (2026), Theorem 3.1 and their hyperplane classification, establish the unconditional value \(2\), its norm-attainment criterion, and the Daugavet duality that gives the rank-one norm formula used here. The present exact **Lipschitz-constrained** profile, unique clipped minimizer, and local-density exponent law are different assertions, not asserted in their inspected manuscript. The classical bounded-Lipschitz dual formulation for signed measures supplies general background for the moment maximization; no new transport duality is claimed.

Two related published mathematical findings were checked in their full public statements and proofs: *Sharp Lipschitz budgets and lattice-phase convergence for nonattaining hyperplane projections* treats a different **countably atomic** signed measure with a geometric-lattice asymptotic; *Sharp inverse-square regularization penalty for two-moment annihilator projections* treats a different **codimension-two** projection with a nontrivial polar optimizer. Neither establishes the signed-density hyperplane formula or arbitrary positive polynomial decay exponents by statement or direct specialization. A related codimension-two result on pairwise singular positive probabilities has a qualitative \(1/\varepsilon\) blow-up estimate for Lebesgue measure versus a single atom but not this class's exact norm curve. These comparisons do not prove that no unindexed equivalent exists.

## Limitations

The theorem is restricted to real interval spaces and a symmetric, almost-everywhere positive signed density with a single sign change. For general asymmetric measures, atoms, multiple sign changes, complex scalars, or other regularity constraints, the clipped ramp and the rate law need not remain valid. The asymptotic assumes a genuine power-law density ratio near zero; no uniformity over varying densities or exponents is asserted. The proof gives an exact scalar-integral characterization for general densities, but a closed algebraic equation only for the power family. Bibliographic searches cannot exclude a differently formulated earlier bounded-Lipschitz dual formula that could imply this result; independent literature review is still desirable.

## References

1. T. Kania and G. Lewicki, *Finite-codimensional subspaces of Daugavet spaces: projection constants and minimal projections*, arXiv:2604.10771v1, first public 12 April 2026, Theorem 3.1 and Sections 3, 5–6. https://arxiv.org/html/2604.10771v1
2. S. C. Hille and E. S. Theewis, *Norming and dense sets of extreme points of the unit ball in spaces of bounded Lipschitz functions*, arXiv:2305.08500, 15 May 2023. https://arxiv.org/abs/2305.08500
3. *Sharp Lipschitz budgets and lattice-phase convergence for nonattaining hyperplane projections*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-lipschitz-budgets-and-lattice-phase-convergence-for-nonatt--06943e74246c
4. *Sharp inverse-square regularization penalty for two-moment annihilator projections*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-inverse-square-regularization-penalty-for-two-moment-annih--383ef76f1656
5. *Generic nonattainment at the least finite-codimensional projection constant*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-generic-nonattainment-at-the-least-finite-codimensional-projecti--f43f3271bce8
