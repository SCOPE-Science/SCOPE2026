# A sharp heterogeneity ordering for the torus-Kuramoto synchronization onset

## Finding

Consider the reduced, factorized Lorentzian torus-Kuramoto mean-field system
\[
\dot x_i=-d_i x_i+K(1-x_i)\prod_{j=1}^{D}x_j,
\qquad i=1,\ldots,D,
\]
with integer \(D\ge3\), positive dispersion rates \(d_i=2\Delta_i>0\), coupling \(K>0\), and \(x_i\in[0,1]\). Let \(K_c(d)\) be the least coupling admitting a strictly positive equilibrium, and let \(X_c(d)=\prod_i x_{i,c}\) be the product coherence at its saddle-node onset. Both quantities are **strictly Schur-concave** in \(d\): for positive vectors of the same sum, if \(d\) majorizes \(e\) and they are not permutations, then
\[
K_c(d)<K_c(e),\qquad X_c(d)<X_c(e).
\]
Writing \(S=\sum_i d_i\), their sharp fixed-budget ranges are
\[
S<K_c(d)\le S\Bigl(\frac D{D-1}\Bigr)^{D-1},
\qquad
0<X_c(d)\le\Bigl(\frac{D-1}{D}\Bigr)^D.
\]
The two upper bounds are attained only at equal rates; both lower bounds are limiting infima, approached as one rate tends to \(S\) and the others tend to zero. The upper threshold-to-budget ratio increases to \(e\) with dimension.

For a fixed rate scale \(m>0\) and \(d_i=m(1+\varepsilon_i)\), where \(\sum_i\varepsilon_i=0\) and \(\|\varepsilon\|_\infty\) is small, the shared sharp quadratic heterogeneity penalty is
\[
\frac{K_c(d)}{mD^D/(D-1)^{D-1}}
=1-\frac{1}{2D^2}\sum_i\varepsilon_i^2+O_D(\|\varepsilon\|_\infty^3),
\]
\[
\frac{X_c(d)}{((D-1)/D)^D}
=1-\frac{1}{2D^2}\sum_i\varepsilon_i^2+O_D(\|\varepsilon\|_\infty^3).
\]
Thus unequal frequency-width allocation lowers the coupling needed for an attracting partially synchronized equilibrium, but also lowers the coherence jump at onset. The result concerns the stated reduced system, not arbitrary finite-oscillator initial distributions.

## Assumptions and scope

The stated ODE is the order-parameter system arising from independent Cauchy frequency distributions and the factorized multidimensional Ott--Antonsen reduction of Novaes [1]. The mathematical theorem here is **conditional on that exact reduced ODE**. All rates are positive, the dimension is an integer at least three, and all equilibrium statements concern the cube \([0,1]^D\). Majorization means: after sorting decreasingly, every initial partial sum of \(d\) is at least the corresponding sum of \(e\), and the total sums coincide. The minimum coupling \(K_c\) and saddle-node product \(X_c\) are defined from the strictly positive branch. The origin remains an attracting equilibrium independently of \(K\).

## Proof

**1. Exact scalar reduction and onset.** A nonzero stationary state on the boundary has some \(x_i=0\), which makes the product zero; its other coordinates then satisfy \(-d_jx_j=0\). Thus the origin is the only boundary equilibrium. For any positive stationary state set \(t=K\prod_i x_i>0\). Stationarity gives
\[
x_i=\frac{t}{t+d_i},\qquad
K=\Phi_d(t):=\frac{\prod_i(t+d_i)}{t^{D-1}}
=t\prod_i\left(1+\frac{d_i}{t}\right).
\]
Differentiating yields
\[
\frac{d\log\Phi_d}{d\log t}=1-\sum_i\frac{d_i}{t+d_i}.
\]
The right-hand side is strictly increasing from \(1-D\) to \(1\), and hence vanishes at one and only one \(t=t_c(d)>0\). The function \(\Phi_d\) diverges at zero and infinity, so \(K_c(d)=\Phi_d(t_c)\) is its unique strict minimum. The onset condition and product read
\[
\sum_i\frac{d_i}{t_c+d_i}=1,
\qquad \sum_i x_{i,c}=D-1,
\qquad X_c(d)=\prod_i\frac{t_c}{t_c+d_i}.
\]
Consequently there are zero, one (at equality), or two strictly positive equilibria as \(K\) passes through \(K_c\).

**2. Dynamical nature of the threshold.** At a positive equilibrium, the Jacobian is similar, by \(P=\operatorname{diag}(x_i\sqrt{d_i})\), to the symmetric rank-one update
\[
P^{-1}JP=-\operatorname{diag}(t+d_i)+vv^{\mathsf T},
\qquad v_i=\sqrt{d_i}.
\]
By the rank-one inertia test, this matrix is negative definite when \(\sum_i d_i/(t+d_i)<1\), has exactly one simple zero and all other eigenvalues negative at equality, and has exactly one positive eigenvalue when that sum exceeds one. Since this sum decreases with \(t\), the upper positive branch is attracting and the lower one is an index-one saddle. The strict minimum of \(\Phi_d\) is nondegenerate because the derivative of \(1-\sum_i d_i/(t+d_i)\) is strictly positive. This is a genuine one-parameter saddle-node, not merely an algebraic repeated root.

**3. Strict majorization for coupling.** Smooth dependence of \(t_c\) on positive \(d\) follows from the implicit-function theorem and the preceding strict derivative. By the envelope identity at the minimizer,
\[
\frac{\partial\log K_c}{\partial d_i}=\frac1{t_c+d_i}=:q_i.
\]
For \(d_i>d_j\), \(q_i<q_j\). The differential Schur--Ostrowski criterion therefore shows that \(\log K_c\) is strictly Schur-concave on each positive fixed-sum simplex. Equivalently, any nontrivial equalizing transfer strictly raises \(K_c\); finite sequences of transfers give the stated majorization comparison.

**4. Strict majorization for onset coherence.** Write \(t=t_c(d)\), \(x_i=t/(t+d_i)\), and \(R=\sum_k d_k/(t+d_k)^2>0\). Implicit differentiation of \(\sum_k d_k/(t+d_k)=1\) yields \(\partial t/\partial d_i=tq_i^2/R\). Because \(\sum_k q_k=(D-1)/t\), differentiating \(\log X_c=D\log t-\sum_k\log(t+d_k)\) gives
\[
\frac{\partial\log X_c}{\partial d_i}=\frac{q_i^2}{R}-q_i.
\]
The difference of two such partial derivatives equals \((q_i-q_j)((q_i+q_j)/R-1)\). The onset sum rule implies
\[
tR=\sum_k x_k(1-x_k)<\sum_k(1-x_k)=1,
\qquad t(q_i+q_j)=x_i+x_j\ge1.
\]
Hence the parenthesis is strictly positive. Therefore \((d_i-d_j)(\partial_i\log X_c-\partial_j\log X_c)<0\) whenever \(d_i\ne d_j\). The same strict Schur criterion proves the second majorization assertion.

**5. Sharp extrema.** With \(S=\sum_i d_i\), the product expansion \(\Phi_d(t)=t+S+\sum_{i<j}d_id_j/t+\cdots\) gives \(K_c>S\). By strict Schur concavity, \(K_c\) is uniquely maximized at \(d_i=S/D\), where \(t_c=S(D-1)/D\), yielding \(K_c=S(D/(D-1))^{D-1}\). The onset sum rule \(\sum_i x_i=D-1\) and arithmetic--geometric mean give \(X_c\le((D-1)/D)^D\), with equality only at equal rates. As \(d\to(S,0,\ldots,0)\) through positive vectors, the unique onset root tends to zero. It follows that \(K_c\to S\) and \(X_c\to0\), proving both lower bounds sharp without claiming a positive-rate endpoint is attained.

**6. Local quadratic penalty.** Let \(d_i=m(1+\varepsilon_i)\) and \(\sum_i\varepsilon_i=0\). At the equal-rate point \(t_0=(D-1)m\), the first variation of \(t_c\) vanishes along fixed-sum perturbations. The envelope Hessian of \(\log K_c\) on this tangent space is \(-\sum_i\varepsilon_i^2/D^2\) at second directional derivative order, because \(\sum_i\log(t_0+d_i)\) contributes \(-\sum_i\varepsilon_i^2/(2D^2)\) and the minimizing \(t\) has no first variation. Therefore
\[
\log\frac{K_c(d)}{K_c(m\mathbf 1)}
=-\frac{\sum_i\varepsilon_i^2}{2D^2}+O_D(\|\varepsilon\|_\infty^3).
\]
For the coherence product, the critical coordinates obey \(\sum_i x_i=D-1\) exactly, and their first variations are \(\delta x_i=-(D-1)\varepsilon_i/D^2\). Expanding \(\sum_i\log x_i\) about the constant vector, with the exact zero sum of all coordinate variations, yields the identical quadratic coefficient. Exponentiating proves both displayed expansions.

## Verification

Run `python checker.py` from the extracted package, with Python, NumPy and SciPy installed. The checker recomputes unique scalar roots, the stationary identities, the simple neutral Jacobian eigenvalue, 1,400 mean-preserving equalization tests across dimensions \(3\) through \(16\), the strict sharp bounds, and the quadratic expansions in both observables. These finite numerical tests support the analytic steps but are **not** proofs of the universal parameter claims or all majorization relations; the arguments above are the proof.

## Relationship to prior work

Novaes [1], particularly equations (28), (30), and (32)--(34), already gives the reduced ODE, the stationary scalar formulation, the unique saddle-node condition, and selected equal- or partly equal-dispersion formulas. Those premises and the known saddle-node existence are not claimed as discoveries here. The new statement is the **global strict majorization order in arbitrary positive dimension-rate vectors**, simultaneously for the critical coupling and the critical product coherence, with sharp fixed-budget extremizers and a common local quadratic loss. None of these comparisons is stated in the inspected source. The standard Schur--Ostrowski differential criterion [2] is used as a classical tool, not presented as new.

## Limitations

The theorem applies to the reduced mean-field equations and all strictly positive dispersion rates, not to the finite-oscillator microscopic equations without the factorization assumptions or to arbitrary frequency distributions. It makes no claim that the incoherent state loses stability; indeed it stays attracting. The lower extremizers occur only on the boundary of the positive-rate parameter domain. A prior equivalent formulation not found by targeted searches remains a residual priority risk. Independent mathematical validation has not been performed.

## References

[1] Marcel Novaes, *Kuramoto model on the \(D\)-dimensional torus*, arXiv:2605.01021 (first publicly posted 2026-05-01), https://arxiv.org/abs/2605.01021.

[2] Marshall, Olkin and Arnold, *Inequalities: Theory of Majorization and Its Applications*, second edition, Springer, 2011. Classical Schur--Ostrowski criterion.
