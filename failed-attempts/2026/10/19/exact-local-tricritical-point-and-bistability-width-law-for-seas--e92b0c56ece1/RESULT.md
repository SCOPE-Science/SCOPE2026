# Exact local tricritical point and bistability-width law for seasonal plant–pollinator viability

## Finding

The shifted-Poisson seasonal plant–pollinator cavity model has an **exact, unique local tricritical point** at
\[
\tau_*=1+m_*=1.420049608669704\ldots,\qquad
z_*=\sqrt{(1+m_*)e^{m_*}}=1.470159219746206\ldots,
\]
where \(m_*>1/4\) is the unique root of
\[
(4m_*-1)\sqrt{(1+m_*)e^{m_*}}=1.
\]
The local nonzero cavity-state branch enters from the linearly unstable side for \(\tau<\tau_*\) and from the linearly stable side for \(\tau>\tau_*\). At \(\tau=\tau_*\) its onset has an exact square-root law. Just above \(\tau_*\), a bistability window opens **quadratically** in the excess mean lifespan, with a specified leading constant. The assertion is a classification of small fixed points and their stability under cavity-map iteration, not a global classification of all viability states or of ecological dynamics in physical time.

## Assumptions and scope

Take \(z>0\) as the mean plant and pollinator degree per seasonal step. A pollinator is active for \(T=1+\operatorname{Pois}(m)\) steps, where \(m\ge0\) and its mean active lifespan is \(\tau=1+m\). Under independent, locally tree-like Poisson contacts, a plant requires at least one viable pollinator neighbour, while a pollinator requires a viable plant in every active step. The size-biased distribution of **remaining** active steps is described by
\[
L(s)=s e^{m(s-1)},\qquad
K(s)=\frac{L'(s)}{L'(1)}=\frac{(1+ms)e^{m(s-1)}}{1+m}.
\]
In particular, \(K(1)=1\); this is the probability-generating function for the remaining active steps as sampled along a random interaction. The plant-neighbour cavity viability \(q\in[0,1]\) is a fixed point of the map
\[
s(q)=1-e^{-zq},\qquad
b(q)=s(q)K(s(q)),\qquad
G_{z,m}(q)=1-e^{-zb(q)}.
\]
We use the scalar iteration \(q_{n+1}=G_{z,m}(q_n)\) solely as a fixed-point stability diagnostic. In this Poisson specialization, a typical plant's viable fraction is \(p=q\), while a typical pollinator's fraction is \(a=L(s(q))\).

Define
\[
c(m)=\frac{e^{-m}}{1+m},\quad
z_c(m)=\sqrt{(1+m)e^m},\quad
D_* = \frac{23m_*^2-4m_*+1}{6(4m_*-1)^2}>0,
\]
\[
b_1=2z_*+\frac{m_*+2}{4(1+m_*)}>0,\qquad
W_* = \frac{z_*b_1^2}{8D_*}>0.
\]
All asymptotic statements are in a sufficiently small neighbourhood of \((q,z,m)=(0,z_*,m_*)\); limits in \(m\) are taken from above where specified.

## Proof

**1. Exact loss of zero-state stability.** The function \(G_{z,m}\) is analytic near zero and increasing on \([0,1]\). Substituting the generating functions and expanding gives
\[
\begin{aligned}
G_{z,m}(q)-q
={}&(cz^2-1)q
-\frac{cz^3}{2}(cz-4m+1)q^2\\
&+\frac{cz^4}{6}\big(c^2z^2-12cmz+3cz+9m^2-12m+1\big)q^3
+O(q^4),
\end{aligned}
\]
where \(c=c(m)\). Hence \(G_{z,m}'(0)=cz^2\). The zero state attracts nearby nonnegative iterates if \(z<z_c(m)\), and repels them if \(z>z_c(m)\).

**2. Unique change in the local branch direction.** At \(z=z_c(m)\) the coefficient of \(q^2\) is
\[
B(m)=\frac{z_c(m)(4m-1)-1}{2}.
\]
It is negative for \(m\le1/4\). For \(m>1/4\), the function \(z_c(m)(4m-1)\) is strictly increasing from zero to infinity, so \(B\) vanishes precisely once, at \(m=m_*\). At any fixed \(m\ne m_*\), the analytic function \((G(q)-q)/q\) has a nonzero derivative with respect to \(q\) at \((q,z)=(0,z_c(m))\). The implicit-function theorem therefore gives the unique local nonzero branch. For \(m<m_*\) it exists for \(z>z_c(m)\) and is locally attracting; for \(m>m_*\) it exists for \(z<z_c(m)\) and is locally repelling. This follows also from the sign of the derivative of \(G(q)-q\) at the branch.

**3. Degenerate cubic and square-root onset.** In the displayed cubic coefficient, substitute \(cz^2=1\) and then \(z(4m-1)=1\). The coefficient becomes exactly \(-D_*\), where \(D_*>0\), since the numerator \(23m^2-4m+1\) has negative discriminant and positive leading coefficient. Thus
\[
G_{z_*,m_*}(q)-q=-D_*q^3+O(q^4).
\]
Write \(\varepsilon=z-z_*\). Dividing by positive \(q\) and using \(cz_*^2=1\) gives
\[
0=\frac{2}{z_*}\varepsilon-D_*q^2
+O\big(\varepsilon^2+|\varepsilon|q+q^3\big).
\]
A standard square-root rescaling followed by the implicit-function theorem yields exactly one small positive nonzero fixed point for \(\varepsilon>0\):
\[
q_+(z,m_*)=\sqrt{\frac{2}{z_*D_*}}\sqrt{z-z_*}+O(z-z_*),
\qquad \sqrt{\frac{2}{z_*D_*}}=1.057345229126056\ldots.
\]
There is no small positive nonzero branch for \(\varepsilon<0\). The positive branch is attracting for cavity-map iteration since \(G'(q_+)-1<0\) and \(G'(q_+)>0\).

**4. Fold and quadratic bistability window.** Extend \(h(q,z,m)=(G_{z,m}(q)-q)/q\) analytically to \(q=0\). Put \(\eta=m-m_*\) and \(y=z-z_c(m)\). At the tricritical point,
\[
h(q,z,m)=\frac{2}{z_*}y+b_1\eta q-D_*q^2
+O\big(y^2+|y\eta|+|yq|+\eta^2q+|\eta|q^2+q^3\big).
\]
The coefficient \(b_1=B'(m_*)\) is the positive number defined above. The Jacobian of the two equations \(h=0\), \(\partial_q h=0\), viewed as equations for \((z,q)\), is nonsingular at the tricritical point because \(\partial_z h=2/z_*\) and \(\partial_q^2h=-2D_*\). The analytic implicit-function theorem therefore gives a unique nearby fold curve. With the rescaling \(q=\eta u\), \(y=\eta^2v\), the leading equations are
\[
\frac{2v}{z_*}+b_1u-D_*u^2=0,
\qquad b_1-2D_*u=0.
\]
Their unique solution is \(u=b_1/(2D_*)\), \(v=-W_*\). Consequently the unique local fold satisfies
\[
q_f(m)=\frac{b_1}{2D_*}(m-m_*)+O((m-m_*)^2),
\]
\[
z_f(m)=z_c(m)-W_*(m-m_*)^2+O((m-m_*)^3),
\qquad W_*=1.711455938024846\ldots.
\]
For sufficiently small \(\eta>0\), and \(z_f(m)<z<z_c(m)\), the strict local maximum of \(h\) is positive while \(h(0,z,m)<0\). There are exactly two **small positive** fixed points, \(q_-<q_+\), in the chosen neighbourhood. At a positive fixed point,
\[
G'(q)-1=q\,\partial_qh(q,z,m).
\]
Thus \(q_-\) is repelling and \(q_+\) attracting under cavity iteration; the zero fixed point also attracts since \(G'(0)<1\). This is a genuine local bistable interval. At its lower endpoint the two positive local roots coalesce in a fold, and at the upper endpoint the lower branch reaches zero. The proof does not rule out remote roots beyond the stated neighbourhood.

## Verification

The accompanying standalone script `verify_cusp.py` reconstructs the first three Taylor coefficients using exact symbolic algebra, checks the exact cubic simplification and uniqueness-domain signs, and numerically stress-tests the square-root branch and quadratic fold law at multiple decreasing perturbation sizes. It independently solves the finite-parameter fold conditions and tests the signs of the derivatives at both positive roots and at zero. Run `python verify_cusp.py` with SymPy and mpmath installed. Numerical checks verify the formulas in tested regimes; the arbitrary-parameter and limiting statements rely on the preceding analytic proof, not the finite tests.

## Relationship to prior work

Clegg and Gross (2026, arXiv:2604.07347, first publicly posted 2026-04-08) formulate the seasonal plant–pollinator mutualistic viability rules, derive a generating-function system, and identify qualitative continuous versus discontinuous collapse and bistability regimes. Their full model and corresponding Poisson/shifted-Poisson specialization motivate this analysis. The present contribution is the **explicit unique local tricritical lifetime/degree pair, the square-root onset coefficient, and the leading constant of the quadratically narrow bistability wedge**. These exact local invariants are not asserted to be independent of the established cavity equations.

Bianconi and Dorogovtsev (2023, arXiv:2307.15346) establish general hypergraph core-percolation bifurcation techniques, including degeneracy conditions for tricriticality, but for different connectivity and dependence constraints. Clegg and Gross (2024, arXiv:2412.05212) analyse microbial cross-feeding viability in another network model; its bistability is not the same stepwise plant-resource requirement. General generating-function and saddle-node methods are pre-existing mathematics. No claim is made that those generic methods are new.

## Limitations

This is a local mathematical theorem about the self-consistency map for the specified infinite, locally tree-like Poisson model. It does not establish a globally unique nonzero state, a global continuous/discontinuous phase diagram, biological stability in physical time, finite-network thresholds, environmental noise robustness, or universal behaviour for other degree or lifespan distributions. The local fixed-point stability adjectives refer to iteration of \(G\), not to observed population dynamics. The possibility that broader percolation literature already implies the exact coefficients is a residual originality risk.

## References

1. T. Clegg and T. Gross, “Temporal Structure Mediates the Robustness and Collapse of Plant-Pollinator Networks,” arXiv:2604.07347, submitted 2026-04-08. https://arxiv.org/abs/2604.07347 and https://arxiv.org/pdf/2604.07347.
2. G. Bianconi and S. N. Dorogovtsev, “The nature of hypergraph k-core percolation problems,” arXiv:2307.15346, 2023. https://arxiv.org/abs/2307.15346.
3. T. Clegg and T. Gross, “Cross-feeding Creates Tipping Points in Microbiome Diversity,” arXiv:2412.05212, submitted 2024-12-06. https://arxiv.org/abs/2412.05212.
