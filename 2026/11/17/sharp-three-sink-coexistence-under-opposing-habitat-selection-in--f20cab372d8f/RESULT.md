# Sharp three-sink coexistence under opposing habitat selection in a two-patch replicator

## Finding

For the two-patch, two-strategy selection–migration flow
\[
\begin{aligned}
\dot x&=d(y-x)+x(1-x)[b(x-1/2)+c],\\
\dot y&=d(x-y)+y(1-y)[b(y-1/2)-c],
\end{aligned}
\qquad (x,y)\in[0,1]^2,
\]
with \(b,d,c>0\), define
\[
C_0=\sqrt{\frac{b^2}{4}+bd},\qquad
C_1=\frac{\sqrt{bd}}2\left(4-\sqrt{4+b/d}\right).
\]
There is exactly one equilibrium on the open anti-diagonal \(\{(x,1-x):0<x<1\}\), denoted \(E\). Both pure-strategy equilibria \((0,0)\) and \((1,1)\), together with \(E\), are **simultaneously hyperbolic attracting equilibria** if and only if
\[
\boxed{\max\{0,C_1\}<c<C_0.}
\]
If one also requires **strictly opposing local dominance**—strategy 1 is selected for at every interior frequency in uncoupled patch 1, while strategy 0 is selected for at every interior frequency in uncoupled patch 2—the sharp condition is
\[
\boxed{\max\{b/2,C_1\}<c<C_0.}
\]
This interval is nonempty for **all** \(b,d>0\). The additional mixed-state bound is active inside the local-dominance regime exactly when \(b/d<9/4\); for \(b/d\ge9/4\), the strict local-dominance and pure-state stability inequalities already guarantee stability of \(E\). The claims concern these three specified equilibria: they do not classify additional equilibria or their basins.

## Assumptions and scope

The two coordinates are local frequencies of strategy 1, migration has equal positive rate \(d\), local selection has positive frequency dependence \(b\), and habitat preference is exactly antisymmetric with magnitude \(c\). The four boundary faces of \([0,1]^2\) point inward or tangent, so the square is forward invariant. The algebraic thresholds apply to this finite-dimensional symmetric model; they are not asserted for general heterogeneous networks or continuous-space diffusion equations.

An *attractor* here means a locally asymptotically stable hyperbolic equilibrium of the full two-dimensional flow, including stability relative to the ambient real plane. At \(c=C_0\) or \(c=C_1\) the corresponding Jacobian has a zero eigenvalue and the strict attracting-hyperbolic conclusion does not hold. In particular, endpoint equalities are excluded, rather than assigned a hyperbolic status.

## Proof

**1. Pure-state eigenvalues.** The two corners \((0,0)\) and \((1,1)\) are equilibria. Their Jacobians have the same trace and determinant, because their diagonal entries are \(-b/2-d+c\) and \(-b/2-d-c\) in reversed order and the off-diagonal entries are \(d\). Their eigenvalues are
\[
\lambda_{\pm}=-\frac b2-d\pm\sqrt{d^2+c^2}.
\]
Both are negative exactly when \(c^2<b^2/4+bd\), equivalently \(0<c<C_0\).

**2. Unique interior anti-diagonal equilibrium.** The line \(x+y=1\) is invariant, since the two local selection contributions cancel under \(y=1-x\). Parametrize \(x=(1+m)/2\), \(y=(1-m)/2\), with \(-1<m<1\). The equilibrium equation becomes
\[
H(m):=(1-m^2)(bm+2c)-8dm=0.
\]
It has precisely one root \(m\in(0,1)\): \(H(0)=2c>0\), \(H(1)=-8d<0\), and its descending polynomial coefficient signs are those of \((-b,-2c,b-8d,2c)\), which have exactly one sign change. Descartes's rule thus gives exactly one positive root counted with multiplicity, and sign change establishes its existence in \((0,1)\). This root \(m(c)\) is simple and increasing with \(c\), since \(H\) crosses from positive to negative and \(\partial H/\partial c=2(1-m^2)>0\).

**3. Full two-dimensional stability of the mixed state.** At \(E=((1+m)/2,(1-m)/2)\), both diagonal entries of the Jacobian equal \(\alpha-d\), with off-diagonal entries \(d\), where elimination of \(c\) using \(H(m)=0\) gives
\[
\alpha=\frac{b(1-m^2)}4-\frac{4dm^2}{1-m^2}.
\]
Thus its **two** real eigenvalues, including the transverse one, are \(\alpha\) and \(\alpha-2d\). The function \(\alpha(m)\) strictly decreases on \((0,1)\), from \(b/4\) to \(-\infty\). Its unique zero is at
\[
m_*=\frac{\sqrt{4+b/d}-2}{\sqrt{b/d}},\qquad
b(1-m_*^2)^2=16dm_*^2.
\]
Solving the equilibrium equation for habitat bias gives
\[
c=\frac{4dm}{1-m^2}-\frac{bm}2.
\]
At \(m=m_*\) this equals \(C_1\) above. Since \(m(c)\) increases strictly with \(c>0\), \(E\) is a hyperbolic sink exactly when \(c>C_1\), including automatically when \(C_1\le0\). Combining with the corner criterion yields \(\max\{0,C_1\}<c<C_0\). The condition is necessary as well, because failure of either strict inequality leaves one of the three Jacobians with a nonnegative eigenvalue.

**4. Nonempty sharp local-dominance wedge.** With \(d=0\) *only for the meaning of isolated-patch selection*, the local payoff differences are \(b(x-1/2)+c\) and \(b(y-1/2)-c\). They have opposite strict fixed signs across \((0,1)\) precisely when \(c\ge b/2\), and for strict uniform margins on the closed frequency interval precisely when \(c>b/2\). We use the latter robust formulation. Since \(C_0^2=b^2/4+bd>b^2/4\), one has \(C_0>b/2\). To compare \(C_0\) with \(C_1\), substitute \(m_*\) into
\[
b=\frac{16dm_*^2}{(1-m_*^2)^2},\qquad
C_1=\frac{4dm_*(1-3m_*^2)}{(1-m_*^2)^2},
\]
which yields the strictly positive identity
\[
C_0^2-C_1^2=\frac{128d^2m_*^4}{(1-m_*^2)^3}>0.
\]
If \(C_1>0\), this implies \(C_1<C_0\); if \(C_1\le0\), the desired strict upper bound is immediate. Hence the local-dominance three-sink wedge is nonempty. Finally \(C_1>b/2\) is equivalent to
\[
\sqrt{4+b/d}+\sqrt{b/d}<4,
\]
and the left side is strictly increasing with \(b/d>0\), attaining four exactly at \(b/d=9/4\). This proves the two boundary regimes.

**5. Exact witness.** At \(b=3\), \(d=1\), \(c=23/12\), one has \(m=1/2\), hence \(E=(3/4,1/4)\). Both vector-field components vanish exactly at \(E\). The corner eigenvalues are
\[
-\frac52\pm\frac{\sqrt{673}}{12}<0,
\]
while the mixed eigenvalues are \(-37/48\) and \(-133/48\). Further, \(c>3/2\) and \(c^2<3^2/4+3\). This exhibits three strict hyperbolic sinks while each isolated patch has strict single-strategy dominance in opposite directions.

## Verification

Run `python3 verify.py` using the accompanying standalone Python 3 checker. It verifies exact rational equilibrium and Jacobian identities, the witness inequalities, the symbolic threshold relation on representative parameter choices, and numerical root bracketing throughout both threshold regimes. Its finite tests complement but do not replace the analytic proof above. All dependencies are in the Python standard library.

## Relationship to prior work

Freire, Gjini and Madec [1] establish backward bifurcations and stable coexistence against unfavorable invasion criteria for spatially heterogeneous replicator partial differential equations, including numerical multistability. The qualitative possibility of coexistence alongside pure-strategy attractors is therefore **prior art**, not claimed new here. The precise contribution here is a necessary-and-sufficient **closed-form stability wedge for three designated equilibria** in an exactly specified symmetric, finite two-patch frequency system, including a second sharp \(b/d=9/4\) boundary for when the mixed-state stability condition is additional. This does not follow directly from their continuous-space local bifurcation condition without an explicit reduction and a comparison of both transverse eigenmodes.

Li, Zhang, Zhang, Cressman and Tao [2] study a two-phenotype, two-patch evolutionary system with additional evolving patch population sizes and frequency-dependent effective migration, and describe complex multistability. The present two-state frequency-only system is not their full four-dimensional model. Related heterogeneous two-patch systems and lattice bistable reaction–diffusion models may give analogous pinning; this does not establish literature-wide uniqueness of the formula. The published exact three-site Nagumo-ring stationary census [3] concerns a different (unbiased, three-node) system; it does not imply these two-site opposing-selection inequalities.

## Limitations

The theorem classifies hyperbolic stability only of the two pure corners and the unique interior equilibrium on the anti-diagonal; further equilibria may exist and are not enumerated. There is no assertion of global attraction, basin size, stochastic robustness, heterogeneous migration, or extension to continuum spatial domains. The non-hyperbolic equality cases are deliberately excluded. Independent validation and exhaustive historical-priority review have not been performed. The qualitative multistability mechanism predates this calculation.

## References

1. T. Freire, E. Gjini, S. Madec, *Backward bifurcations in spatial replicator models: when invasion criteria fail to predict coexistence*, arXiv:2608.05914, v1 publicly submitted 2026-08-06. https://arxiv.org/abs/2608.05914
2. Q. Li, J. Zhang, B. Zhang, R. Cressman, Y. Tao, *Effect of Spatial Dispersion on Evolutionary Stability: A Two-Phenotype and Two-Patch Model*, PLOS ONE **10** (2015), e0142929. https://doi.org/10.1371/journal.pone.0142929
3. *Exact equilibrium census and sharp pinning fold on a three-site cubic Nagumo ring*, published published-finding corpus research record (2026-11-02). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-equilibrium-census-and-sharp-pinning-fold-on-a-three-site--90178de4c9e1
