# Sharp local noise amplification and optimal mesh balancing for nonuniform PCHIP

## Finding
Let four consecutive knots have positive spacings \(a,b,c\), and interpolate nondecreasing four-point data with the standard weighted-harmonic-mean interior slopes of the shape-preserving piecewise cubic Hermite interpolant (PCHIP). Define the pointwise two-input perturbation coefficient \(K_{a,b,c}(t)\) at relative position \(t\in[0,1]\) in the middle cell by taking the supremum of absolute output differences divided by the maximum absolute nodal-data difference, over every pair of distinct nondecreasing data vectors.

Set
\[
q(a,b)=\frac{3b(a+b)}{a(a+2b)}=\frac{3b}{2}\left(\frac1a+\frac1{a+2b}\right).
\]
**The exact sharp local perturbation profile is**
\[
\boxed{K_{a,b,c}(t)=1+2t(1-t)\bigl[q(a,b)(1-t)+q(c,b)t\bigr].}
\]
The full-cell coefficient \(L(a,b,c)=\max_{0\le t\le1}K_{a,b,c}(t)\) has a unique interior maximizer. For fixed middle spacing \(b>0\) and fixed sum of neighboring spacings \(a+c=T>0\), **the unique minimizing mesh is** \(a=c=T/2\), at which
\[
\boxed{L(T/2,b,T/2)=1+\tfrac12q(T/2,b).}
\]
Equal spacings give \(L(b,b,b)=2\), whereas \((a,b,c)=(1,2,1)\) gives \(L=14/5\). If \(b,c>0\) remain fixed as \(a\downarrow0\), then
\[
\boxed{L(a,b,c)\sim\frac{4b}{9a}.}
\]
Thus preserving the range and monotonicity of *each* data vector does not prevent arbitrarily large amplification of the difference between two monotone data vectors on strongly graded meshes.

## Assumptions and scope
Fix four distinct real knots \(x_{-1}<x_0<x_1<x_2\) with \(a=x_0-x_{-1}\), \(b=x_1-x_0\), \(c=x_2-x_1\). Data belong to the closed convex cone \(\mathcal C=\{y\in\mathbb R^4:y_{-1}\le y_0\le y_1\le y_2\}\). The local PCHIP polynomial \(P_y\) on \([x_0,x_1]\) uses its standard *interior* Brodlie/Fritsch--Butland weighted harmonic-mean derivatives at \(x_0,x_1\), with zero slope if either adjacent secant is zero. It needs no assumption on the outer endpoint derivatives and is unchanged by additional knots outside the four-point stencil.

For \(t\in[0,1]\), precisely
\[
K_{a,b,c}(t)=\sup_{y,z\in\mathcal C,\ y\ne z}
\frac{|P_y(x_0+bt)-P_z(x_0+bt)|}{\max_{-1\le j\le2}|y_j-z_j|}.
\]
The analogous full-cell coefficient is the supremum of the numerator over the entire middle interval before division; the pointwise supremum and interval supremum commute. These are **two-input nonlinear Lipschitz** constants, not single-input Lebesgue constants, floating-point roundoff bounds, or errors relative to an unknown underlying function. The supremum for interior positions can require limiting pairs approaching a flat neighboring secant; finite distinct pairs need not attain it.

## Proof
**1. The local interpolation map.** Put \(A=(y_0-y_{-1})/a\), \(B=(y_1-y_0)/b\), \(C=(y_2-y_1)/c\), all nonnegative. Let
\[
\alpha=\frac{a+2b}{3(a+b)},\quad\beta=1-\alpha=\frac{2a+b}{3(a+b)},\quad
\alpha'=\frac{b+2c}{3(b+c)},\quad\beta'=1-\alpha'=\frac{2b+c}{3(b+c)}.
\]
In particular, \(1/3<\alpha,\beta,\alpha',\beta'<2/3\). Define \(H_{r,s}(u,v)=uv/(rv+su)\) for positive inputs, extended continuously by zero when either input is zero. The PCHIP slopes are \(d_0=H_{\alpha,\beta}(A,B)\) and \(d_1=H_{\alpha',\beta'}(B,C)\). With \(S=3t^2-2t^3\), \(U=t(1-t)^2\), \(V=t^2(1-t)\), standard Hermite interpolation gives
\[
P_y(x_0+bt)=y_0+S(y_1-y_0)+bUd_0-bVd_1.
\]

**2. Gradient-sign identity.** At strictly positive secants, the four partial derivatives of this expression with respect to \((y_{-1},y_0,y_1,y_2)\) are
\[
\begin{aligned}
p_{-1}&=-\frac ba U (d_0)_A,\\
p_0&=1-S+\frac baU(d_0)_A-U(d_0)_B+V(d_1)_B,\\
p_1&=S+U(d_0)_B-V(d_1)_B+\frac bcV(d_1)_C,\\
p_2&=-\frac bcV(d_1)_C.
\end{aligned}
\]
For \(u,v>0\), the elementary exact identities are
\[
\partial_uH_{r,s}(u,v)=\frac{rv^2}{(rv+su)^2},\qquad
\partial_vH_{r,s}(u,v)=\frac{su^2}{(rv+su)^2}.
\]
Thus \(0\le(d_0)_B\le1/\beta<3\) and \(0\le(d_1)_B\le1/\alpha'<3\). Consequently
\[
p_0\ge1-S-3U=(1-t)^3\ge0,
\qquad p_1\ge S-3V=t^3\ge0,
\]
while \(p_{-1},p_2\le0\). Translation-equivariance gives \(\sum_jp_j=1\), whence
\[
\sum_j|p_j|=1+2\left[\frac baU(d_0)_A+\frac bcV(d_1)_C\right].
\]

**3. Sharp pointwise upper bound and limiting witness.** The derivative formulas yield \((d_0)_A\le1/\alpha\) and \((d_1)_C\le1/\beta'\). They approach these bounds simultaneously when \(A,C\downarrow0\) with \(B>0\) fixed. Therefore the supremum of the gradient's \(\ell^1\) norm is
\[
1+2U\frac{b}{a\alpha}+2V\frac{b}{c\beta'}=1+2Uq(a,b)+2Vq(c,b).
\]
Because \(\mathcal C\) is convex and the extended harmonic mean is locally Lipschitz on the closed positive quadrant, integration along each segment from \(y\) to \(z\), with almost-everywhere differentiation, proves this is a global Lipschitz upper bound. To prove sharpness, start from strictly increasing data with positive central secant and arbitrarily small *positive* outer secants. Perturb the four nodal values in the signed direction \((-1,+1,+1,-1)\), taking the amplitude smaller than half the smallest outer nodal increment. Both vectors remain in \(\mathcal C\), and their finite-difference quotient approaches the sum of the four absolute partial derivatives. Let the outer secants tend to zero. This proves the displayed pointwise equality, including the endpoints by interpolation.

**4. Unique location and balanced neighboring mesh.** Write \(u=q(a,b)>0\), \(v=q(c,b)>0\), so the added factor is \(2f(t)\) with \(f(t)=t(1-t)[u(1-t)+vt]\). Differentiation gives
\[
f'(t)=u+2(v-2u)t-3(v-u)t^2.
\]
Since \(f'(0)=u>0\) and \(f'(1)=-v<0\), and the product of its two roots is \(-u/[3(v-u)]\) when \(u\ne v\), there is exactly one root in \((0,1)\) (the other lies outside). Equivalently its explicit location is
\[
t_*=\begin{cases}\displaystyle\frac{v-2u+\sqrt{u^2-uv+v^2}}{3(v-u)},&u\ne v,\\[4pt]\frac12,&u=v.\end{cases}
\]
The identity \(q(a,b)=\tfrac{3b}{2}(a^{-1}+(a+2b)^{-1})\) makes \(q(\cdot,b)\) strictly convex for positive arguments. For fixed \(a+c=T\), evaluating the profile at \(t=1/2\) and applying strict Jensen gives
\[
L(a,b,c)\ge1+\frac{q(a,b)+q(c,b)}4
\ge1+\frac{q(T/2,b)}2,
\]
with equality in the second inequality only if \(a=c\). For \(a=c=T/2\), the profile reduces to \(1+2q(T/2,b)t(1-t)\), attaining exactly the lower bound at \(t=1/2\). This proves unique optimal balancing. If \(a\downarrow0\), then \(q(a,b)\sim3b/(2a)\), whereas \(q(c,b)\) is fixed. Since \(\max_{0\le t\le1}t(1-t)^2=4/27\), the stated \(4b/(9a)\) asymptotic follows.

## Verification
Run `python3 pchip_sensitivity_verify.py` using the Python standard library. The checker reproduces the exact-rational gradient-sign and translation identities for 1,000 seeded parameter combinations, tests 1,200 exact-rational two-input inequalities and monotonicity/range cases, verifies three limiting signed-perturbation witnesses, checks 300 random neighbor-balancing comparisons, and verifies the exact coefficients \(2\) and \(14/5\). The analytic all-mesh and all-data theorem depends on Steps 1–4, **not** on finite randomized checks. Every numerical check uses the identical four-node interior map and stated mesh parameters.

## Relationship to prior work
The weighted harmonic interior derivative is standard: Fritsch and Butland (1984) introduced the monotonicity-preserving local cubic rule, and SciPy's documented PCHIP algorithm gives exactly these nonuniform weights. Aràndiga, Baeza and Yáñez (2021) inspect Brodlie's derivative and the approximation order on nonuniform meshes, including nonuniform tests; their Sections 3–4 do not state the two-input maximum-norm coefficient or balancing law. Baeza, Donat and Martínez-Gavara (published online 11 January 2024) use PCHIP in multilevel balance-law numerics and emphasize shape-preservation, without giving this exact worst-case perturbation profile. The earlier PCHIP subdivision analysis of Aràndiga, Donat and Santágueda (2016) proves convergence and stability of the iterated uniform-grid nonlinear subdivision process via generalized Jacobians; this does not state the sharp *single nonuniform-cell*, pointwise two-input maximum-norm coefficient or fixed-neighbor-length minimax balance. Published adjacent findings address sharp **total variation** sensitivity for the uniform-grid harmonic rule and a **different Steffen** rule on nonuniform grids. Neither statement implies the exact four-point maximum-norm coefficient for nonuniform PCHIP without a separate argument. There is no claim that ordinary PCHIP interpolation or its monotonicity was invented here.

## Limitations
The result requires two real nondecreasing data vectors, fixed real knots, and unmodified interior PCHIP harmonic slopes. It gives no global estimate for finite-grid *endpoint* cells, where different derivative rules apply; it does not cover decreasing/oscillatory pairs (though reflection can handle decreasing pairs separately), movement/noise in the knot coordinates, other monotone slope rules, or errors with respect to an unknown true function. The sharp Lipschitz bound is an adversarial deterministic sensitivity measure, not a typical-noise distributional prediction. A historical priority judgment remains provisional pending further literature review; independently validated novelty is not claimed.

## References
1. F. N. Fritsch and J. Butland, *A Method for Constructing Local Monotone Piecewise Cubic Interpolants*, SIAM J. Sci. Stat. Comput. 5 (1984), 300–304, https://doi.org/10.1137/0905021.
2. F. Aràndiga, A. Baeza and D. F. Yáñez, *Monotone cubic spline interpolation for functions with a strong gradient*, arXiv:2102.11564, first submitted 23 February 2021, https://arxiv.org/html/2102.11564v1.
3. A. Baeza, R. Donat and A. Martínez-Gavara, *On the Use of Monotonicity-Preserving Interpolatory Techniques in Multilevel Schemes for Balance Laws*, Commun. Appl. Math. Comput. 6 (2024), 1319–1341, publicly online 11 January 2024, https://doi.org/10.1007/s42967-023-00332-3.
4. F. Aràndiga, R. Donat and M. Santágueda, *The PCHIP subdivision scheme*, Applied Mathematics and Computation 272 (2016), 28–40, https://doi.org/10.1016/j.amc.2015.07.071.
5. SciPy documentation, *PchipInterpolator*, interior nonuniform weighted harmonic means, https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.PchipInterpolator.html.
6. *Sharp two-input bounded-variation stability of harmonic-mean cubic Hermite interpolation*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-two-input-bounded-variation-stability-of-harmonic-mean-cub--479993d5519d.
7. *Sharp mesh-ratio control of two-input variation for nonuniform Steffen cubic Hermite interpolation*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-mesh-ratio-control-of-two-input-variation-for-nonuniform-s--c024605d3664.
