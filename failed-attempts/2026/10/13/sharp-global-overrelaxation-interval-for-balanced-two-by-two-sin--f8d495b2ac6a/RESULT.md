# Sharp global overrelaxation interval for balanced two-by-two Sinkhorn scaling

## Finding

**Theorem (exact global parameter frontier).** Let \(K=(K_{ij})_{i,j=1}^2\) be any real matrix with **all four entries strictly positive**, and prescribe both row and column sums as \(a=b=(1/2,1/2)\). Let \(u_0,v_0\) be **arbitrary strictly positive two-vectors**. For one fixed \(\omega\ge0\), consider the alternating updates

\[
u_{n+1}=u_n^{\,1-\omega}\odot\left(\frac{a}{Kv_n}\right)^\omega,\qquad
v_{n+1}=v_n^{\,1-\omega}\odot\left(\frac{b}{K^{\mathsf T}u_{n+1}}\right)^\omega.
\]

All powers and divisions are componentwise. Define the actual coupling \(P_n=\operatorname{diag}(u_n)K\operatorname{diag}(v_n)\) and its unit-mass normalization \(\widehat P_n=P_n/\sum_{ij}(P_n)_{ij}\). There is a **unique** matrix \(P_*\) diagonally equivalent to \(K\) with row and column sums equal to \(a,b\). The following are equivalent:

1. \(0<\omega<2\).
2. From **every** positive initialization, \(\widehat P_n\to P_*\).
3. From **every** positive initialization, the unnormalized couplings satisfy \(P_n\to P_*\).

When these assertions hold, convergence is eventually geometric (with constants depending on \(K,\omega,u_0,v_0\)). At \(\omega=2\), a nontrivial **exact first integral** prevents convergence to \(P_*\) from every initial projective pair distinct from the optimum. The same nonconvergence holds for all \(\omega>2\), and \(\omega=0\) is the identity. The threshold \(2\) is independent of the condition number and Birkhoff contraction factor of \(K\).

## Assumptions and scope

The kernel is a positive real \(2\times2\) matrix, both prescribed margins are exactly uniform and have total one, arithmetic is exact, and each complete iteration comprises a row scaling followed by a column scaling using a single fixed nonnegative \(\omega\). No rank or symmetry restriction is imposed on \(K\). Scaling vectors have the usual common scalar gauge freedom; the theorem asserts convergence of their coupling matrix and their two projective ratios, not uniqueness of the individual vector representatives.

Set \(s_1=1\), \(s_2=-1\), and use the logarithmic projective coordinates

\[
x=\log(u_1/u_2),\qquad y=\log(v_1/v_2).
\]

Define the positive partition function and potential

\[
Z(x,y)=\sum_{i,j=1}^{2}K_{ij}\exp\left(\frac{s_i x+s_j y}{2}\right),\qquad
\Phi(x,y)=\log Z(x,y).
\]

The uniquely determined unit-mass matrix represented by the ratios is

\[
\Pi_{ij}(x,y)=\frac{K_{ij}\exp((s_i x+s_j y)/2)}{Z(x,y)}.
\]

## Proof

**1. Strict convexity, compact sublevels, and the unique target.** The Hessian of \(\Phi\) is the covariance matrix of the four support vectors \((s_i/2,s_j/2)\) under the strictly positive probability law \(\Pi(x,y)\). Those support vectors affinely span \(\mathbb R^2\), so \(\nabla^2\Phi(x,y)\) is positive definite at every finite \((x,y)\). If \(k_{\min}=\min_{ij}K_{ij}>0\), then

\[
Z(x,y)\ge4k_{\min}\cosh(x/2)\cosh(y/2),
\]

hence \(\Phi\) is coercive. It has exactly one critical point \((x_*,y_*)\), its global minimum. Since

\[
\partial_x\Phi=\frac12\left(\sum_j\Pi_{1j}-\sum_j\Pi_{2j}\right),\qquad
\partial_y\Phi=\frac12\left(\sum_i\Pi_{i1}-\sum_i\Pi_{i2}\right),
\]

the corresponding \(\Pi(x_*,y_*)\) has both prescribed uniform margins, and uniqueness follows.

**2. Exact conditional symmetry.** For fixed \(y\), let

\[
A_1(y)=K_{11}e^{y/2}+K_{12}e^{-y/2},\quad
A_2(y)=K_{21}e^{y/2}+K_{22}e^{-y/2},\quad
X(y)=\log\frac{A_2(y)}{A_1(y)}.
\]

Then the entire nonquadratic conditional objective has the *exact* identity

\[
Z(x,y)=2\sqrt{A_1(y)A_2(y)}\cosh\left(\frac{x-X(y)}2\right).
\]

Thus \(X(y)\) is the unique minimizer of \(x\mapsto\Phi(x,y)\). Likewise define

\[
B_1(x)=K_{11}e^{x/2}+K_{21}e^{-x/2},\quad
B_2(x)=K_{12}e^{x/2}+K_{22}e^{-x/2},\quad
Y(x)=\log\frac{B_2(x)}{B_1(x)}.
\]

Directly taking ratios in the two multiplicative updates yields, with \(h=1-\omega\),

\[
x_{n+1}=h x_n+\omega X(y_n),\qquad
y_{n+1}=h y_n+\omega Y(x_{n+1}).
\]

In particular, with \(d=x-X(y)\), the row-coordinate update changes the potential by exactly

\[
\Phi(hx+\omega X(y),y)-\Phi(x,y)
=\log\cosh(hd/2)-\log\cosh(d/2).
\]

The identical formula holds for the column-coordinate update with \(d=y-Y(x)\). Because \(\cosh\) is even and strictly increasing on the nonnegative half-line, the change is strictly negative at a nonminimizing coordinate when \(|h|<1\), zero for every coordinate at \(|h|=1\), and strictly positive at a nonminimizing coordinate when \(|h|>1\). This conclusion uses no local approximation.

**3. Global projective convergence and sharp failure.** For \(0<\omega<2\), every full sweep weakly decreases \(\Phi\) and decreases it strictly unless both coordinates are already minimizing at their respective stages. A zero full-sweep decrement forces \(x=X(y)\) and \(y=Y(x)\), hence \((x,y)=(x_*,y_*)\). Coercivity confines all iterates to a compact sublevel set. Their potential values decrease to a limit; continuity implies every cluster point has zero full-sweep decrement, hence equals the unique minimum. Therefore \((x_n,y_n)\to(x_*,y_*)\) and \(\widehat P_n=\Pi(x_n,y_n)\to P_*\).

For \(\omega=2\), \(h=-1\), so **each half-step preserves \(\Phi\) exactly**. From an initial projective state different from \((x_*,y_*)\), its constant value exceeds the minimum and precludes convergence to the target. For \(\omega>2\), the potential is nondecreasing and likewise starts strictly above the minimum for every such initialization. For \(\omega=0\), the update is the identity. Thus the global interval is exactly \((0,2)\).

**4. Actual coupling normalization.** The preceding result does not silently identify projective convergence with unnormalized convergence. Write

\[
\log u_i=s+s_i x/2,\qquad \log v_j=t+s_j y/2,\qquad z=s+t,
\]

and set

\[
c(y)=\log2+\tfrac12\log(A_1(y)A_2(y)),\qquad
d(x)=\log2+\tfrac12\log(B_1(x)B_2(x)).
\]

Averaging the logarithms of both scaling updates and eliminating the intermediate average yields the **exact** scalar recurrence

\[
z_{n+1}=h^2z_n-\omega h\,c(y_n)-\omega\,d(x_{n+1}).
\]

At the unique balanced point, the two equal row contributions to the partition function and the two equal column contributions imply

\[
c(y_*)=d(x_*)=\log Z(x_*,y_*).
\]

Since \(h^2<1\) and \((x_n,y_n)\to(x_*,y_*)\), the stable affine recurrence forces

\[
z_n\longrightarrow-\log Z(x_*,y_*).
\]

But \((P_n)_{ij}=e^{z_n}K_{ij}e^{(s_i x_n+s_j y_n)/2}\), so \(P_n\to P_*\) **without an external renormalization**.

**5. Eventual geometric rate.** At the balanced optimum, write \(\rho=\sum_{ij}s_i s_j(P_*)_{ij}\). Strict positivity gives \(|\rho|<1\). Conditional implicit differentiation of the two stationary coordinate equations gives \(X'(y_*)=Y'(x_*)=-\rho\). The Jacobian of the complete two-coordinate update at the optimum is

\[
J=\begin{pmatrix}h&-\omega\rho\\-\omega h\rho&h+\omega^2\rho^2\end{pmatrix},\qquad
\det J=h^2,\qquad\operatorname{tr}J=2h+\omega^2\rho^2.
\]

Its three real quadratic Schur conditions are

\[
1-\det J=\omega(2-\omega)>0,\quad
1-\operatorname{tr}J+\det J=\omega^2(1-\rho^2)>0,\quad
1+\operatorname{tr}J+\det J=(2-\omega)^2+\omega^2\rho^2>0.
\]

For \(0<\omega<2\), both eigenvalues lie strictly inside the unit disk. Standard finite-dimensional differentiable fixed-point estimates give local geometric convergence and, since global convergence has already been proved, eventual geometric convergence from every start. The scalar recurrence in step 4 also contracts geometrically because its forcing terms do. This completes the proof.

## Verification

The standalone \(`verify.py`\) reconstructs the logarithmic ratio recurrence directly from multiplicative row and column scaling, checks the exact conditional potential identity, confirms descent/conservation/ascent for parameters on both sides of the sharp boundary, tests the normalization scalar recurrence, and exercises the fixed-point and Schur inequalities over reproducibly generated positive kernels. All such finite checks are diagnostics; the conclusions for every kernel, every positive initialization, and all iteration counts are established by the analytic arguments above.

Run the verifier with Python 3 using \(`python verify.py`\); no external dependencies are needed.

## Relationship to prior work

Thibault, Chizat, Dossal, and Papadakis [1] introduced the overrelaxed Sinkhorn approach and established convergence using **adaptive**, Lyapunov-controlled relaxation parameters. Their analysis explains why a fixed parameter need not be globally safe for general marginals and dimensions. The present result concerns the **unchanged fixed-parameter rule**, but exploits the exact even conditional log-cosh form special to two equal-mass rows and columns.

Lehmann, von Renesse, Sambale, and Uschmajew [2] established local convergence for every \(0<\omega<2\) and a general global sufficient range \(0<\omega<2/(1+\Lambda(K))\), where \(\Lambda(K)<1\) is the Birkhoff contraction factor. Their global theorem therefore does **not** imply the full \((0,2)\) interval when \(\Lambda(K)>0\). The present proof establishes this full range **globally and sharply** for the stated balanced \(2\times2\) class, as well as the conserved projective potential at the endpoint. The classical local-rate formula in [2] remains applicable; that rate is not claimed as new here.

## Limitations

Balanced marginals are essential to the exact even log-cosh coordinate identity; this theorem does not cover arbitrary marginal weights, rectangular kernels, or higher dimensions. The rate is eventual and does not provide a uniform globally valid contraction coefficient. The proof concerns exact arithmetic; extreme kernel conditioning may cause floating-point overflow or numerical underflow. It does not show an optimal choice of \(\omega\) inside the interval, and does not claim full convergence of individual scaling representatives, which have scalar gauge freedom. A mathematically equivalent result outside the inspected literature remains possible and would affect priority, not the proof.

## References

[1] A. Thibault, L. Chizat, C. Dossal, and N. Papadakis, *Overrelaxed Sinkhorn-Knopp Algorithm for Regularized Optimal Transport*, arXiv:1711.01851 (first public 2017-11-06). Full text: https://arxiv.org/html/1711.01851v2 .

[2] T. Lehmann, M.-K. von Renesse, A. Sambale, and A. Uschmajew, *A note on overrelaxation in the Sinkhorn algorithm*, arXiv:2012.12562 (first public 2020-12-23). Full text: https://arxiv.org/html/2012.12562v3 .
