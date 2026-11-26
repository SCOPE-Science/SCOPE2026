# Sharp near-bipartite stability ceiling for heterogeneous two-agent gradient tracking

## Finding

Fix \(0<\eta<1\). For \(-1<\nu<1\), let
\[
 W_\nu=\tfrac12\begin{pmatrix}1+\nu&1-\nu\\1-\nu&1+\nu\end{pmatrix},
 \qquad H=\operatorname{diag}(1+\eta,1-\eta).
\]
For two centered scalar quadratic costs with curvatures given by \(H\), use a common normalized constant step \(\beta>0\) and exactly the update
\[
 x^+=W_\nu(x-\beta y),\qquad y^+=W_\nu y+H(x^+-x),\qquad y_0=Hx_0.
\]
Let \(B_-(\sigma,\eta)\) be the supremum of the strictly Schur-stable steps on the consistent invariant subspace at \(\nu=-\sigma\), where \(0<\sigma<1\). Then
\[
 \lim_{\sigma\uparrow1}\frac{B_-(\sigma,\eta)}{1-\sigma}=2.
\]
In particular, the upper bound controls **all** stable steps, not just steps in a shrinking interval near zero. By comparison the previously known positive-eigenvalue frontier \(B_+(\sigma,\eta)\) at \(\nu=+\sigma\) tends to \(2/(1+\eta)\), so
\[
 \frac{B_+(\sigma,\eta)}{B_-(\sigma,\eta)}\sim\frac{1}{(1+\eta)(1-\sigma)}.
\]
The networks have the same essential spectral radius \(\sigma\) and the same curvature dispersion \(\eta\). A rule that sees only these descriptors and must stabilize both networks is therefore subject to the smaller, vanishing ceiling. The positive frontier is used for comparison, not claimed as new. No interval property is presumed for the negative-network stability set. All statements hold with \(\eta\) fixed in the open interval specified above.

## Proof

**Consistent subspace and cubic.** In orthonormal consensus and disagreement coordinates, use subscripts \(c,d\) for the two components. The initialization implies \(y_c=x_c+\eta x_d\), which is preserved by the tracker update. On coordinates \((\beta y_c,x_d,\beta y_d)\) the restricted matrix is
\[
A=\begin{pmatrix}
1-\beta&\beta\eta(\nu-1)&-\beta\eta\nu\\
0&\nu&-\nu\\
-\beta\eta&\beta(\nu-1)&\nu(1-\beta)
\end{pmatrix}.
\]
In particular, the initialization does not leave an unstable mode untested for all possible positions. In these coordinates the initial states span the plane \(K=\ker \ell\), where \(\ell=(-\eta,-\beta(1-\eta^2),1)\). Direct multiplication gives \(\ell A=(-\eta,-\beta(1-\eta^2),\nu)\), so \(K\) is not invariant and \(K+AK=\mathbb R^3\). If every initial state in \(K\) converges to zero, so does every state in this span. For \(\nu\ne0\) convergence of positions implies that of trackers, because \(\beta y_j=x_j-W_\nu^{-1}x_{j+1}\). Thus strict Schur stability is also necessary for convergence from every consistently initialized position for either signed network.

Let \(Q(z)=\det(zI-A)=z^3+a z^2+b z+c\). A determinant expansion gives
\[
 Q(z)=(z-1+\beta)[(z-\nu)^2+\beta\nu(z-1)]-\beta^2\eta^2\nu(z-1),
\]
or equivalently, with \(h=1-\eta^2\),
\[
 a=\beta(1+\nu)-1-2\nu,\quad
 b=\nu^2+2\nu-4\beta\nu+\beta^2\nu h,\quad
 c=-\nu^2+\beta\nu(1+\nu)-\beta^2\nu h.
\]
The real cubic Schur conditions are \(|c|<1\), \(Q(1)>0\), \(-Q(-1)>0\), and \(D=1-b+ac-c^2>0\). For example, with \(|c|<1\), the Schur reduction \([Q(z)-c z^3Q(1/z)]/z\) has leading coefficient \(1-c^2\) and constant term \(b-ac\). Its strict quadratic conditions are positivity at \(1,-1\) and constant term less than leading coefficient (the lower bound follows from summing the two endpoint inequalities). This gives the stated conditions. Here \(Q(1)=\beta(1-\nu)^2\).

**Near-bipartite lower bound.** Put \(\delta=1-\sigma\) and \(\nu=-1+\delta\). For a fixed \(k>0\), substitute \(\beta=k\delta\). The coefficients above give
\[
 1+c=2\delta+O(\delta^2),\quad 1-c=2+O(\delta),\quad
 -Q(-1)=4k\delta+O(\delta^2),\quad D=(8-4k)\delta+O(\delta^2).
\]
Thus all four tests are strict for sufficiently small \(\delta>0\) whenever \(0<k<2\). This gives \(\liminf B_-/\delta\ge2\).

**Upper bound for all stable steps.** The constant coefficient is
\[
c=-(1-\delta)^2-\beta\delta(1-\delta)+h(1-\delta)\beta^2.
\]
Since \(h>0\) is fixed, \(c<1\) uniformly bounds stable \(\beta\) near \(\delta=0\). At the limiting value \(\nu=-1\) the fourth Schur expression is
\[
D=-\beta\bigl(h^2\beta^3-4h\beta+4\bigr).
\]
For \(\beta>0\), the bracket is \(4+\sqrt h(u^3-4u)\) with \(u=\sqrt h\,\beta>0\); its minimum is positive since \(u^3-4u\ge-16/(3\sqrt3)>-4\) and \(0<h<1\). Thus a sequence of stable steps cannot have a positive accumulation point as \(\delta\downarrow0\). All stable steps tend uniformly to zero in that limit, by the preceding boundedness. The two-variable Taylor expansion is
\[
D=8\delta-4\beta+O((\delta+\beta)^2).
\]
For an arbitrarily small fixed \(e>0\), eventually the absolute remainder is at most \(e(\delta+\beta)\) for every stable step. Positivity of \(D\) then forces \((4-e)\beta<(8+e)\delta\). Taking the supremum and letting \(e\downarrow0\) gives the matching upper bound.

**Comparison and a finite witness.** The earlier positive-spectrum two-agent frontier is
\[
 B_+(\sigma,\eta)=\frac{4(1+\sigma)^2}{L+\sqrt{L^2-16\sigma h(1+\sigma)^2}},\qquad L=\sigma^2+6\sigma+1.
\]
Substitution of \(\sigma\uparrow1\) gives \(2/(1+\eta)\), and the ceiling ratio follows. For a finite witness, take \(\eta=\sigma=1/2\), \(\beta=6/5\). At \(\nu=+1/2\) the cubic is \(z^3-z^2/5-61z/100+11/100\); all strict Schur conditions hold, with \(D=15759/10000\). At \(\nu=-1/2\) it is \(z^3+3z^2/5+111z/100-1/100\), with \(D=-1161/10000\). Its derivative is everywhere positive and its sole real root \(r\) is in \((0,1/100)\). The conjugate pair has squared modulus \(1/(100r)>1\). The integer polynomial obtained by multiplying by 100 has degree three and no root modulo seven, so \(r\) is irrational. The valid initialization \(x_0=(1,-1)^\mathsf T\), \(y_0=Hx_0\) gives a nonzero reduced vector rational up to a common factor. It cannot be an eigenvector for \(r\) of the rational matrix, hence it has a component in the unstable two-dimensional real subspace. The relation between positions and trackers from invertibility of \(W_\nu\) implies \(\limsup_j\|x_j\|^{1/j}>1\).

## Verification and scope

The accompanying `verify_dgt.py` in the source package is an optional exact SymPy checker for the characteristic polynomial, Schur expansions and finite witness. Its finite checks are not used to infer the upper bound on all stable steps. The theorem concerns only the stated constant-step two-agent quadratic recurrence and fixed disparity; it does not claim an exact finite negative-eigenvalue frontier, time-varying convergence, or higher-dimensional optimality. In particular, mixing the gradient correction as part of \(W_\nu[y+H(x^+-x)]\) changes the method.

## Relationship to prior work

- [*Sharp heterogeneous two-agent gradient-tracking stability frontier*](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-sharp-heterogeneous-two-agent-gradient-tracking-stability-fronti--da4f13406cac) gives the exact positive-spectrum formula used above, for the same reduced matrix and cubic. Neither the positive limit nor that cubic or the general Jury test is claimed as new here.
- [*A sharp curvature-mixing stability frontier for two-agent gradient tracking*](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-a-sharp-curvature-mixing-stability-frontier-for-two-agent-gradie--4a839f6da62a) studies signed spectra and curvature dispersion at the single normalized step \(\beta=1\); it does not determine the supremum as a function of the negative spectral gap. [*Exact sign-aware graph-specific tuning for homogeneous distributed gradient tracking*](https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-sign-aware-graph-specific-tuning-for-homogeneous-distribut--4bef30512fd6) gives sign-aware rate tuning at zero disparity, not the present fixed heterogeneous scaling.
- Wang et al., [*Adaptive Stepsizes With Certified Convergence in Distributed Gradient Tracking With Quadratic Costs*](https://arxiv.org/abs/2608.03548), supply the general reduced dynamics and a sufficient certificate; a sufficient certificate does not give the necessary bound over every stable step. Tian, Chai and Xu, [*Exact Worst-case Convergence Rates of Distributed Gradient Tracking Methods*](https://arxiv.org/abs/2607.23601), use the alternate gradient-difference placement in their AugDGM recurrence, which in general does not coincide with this one when \(H\) and \(W_\nu\) do not commute.

The distinct contribution is the sharp negative-endpoint ceiling for fixed heterogeneous curvatures and its resulting unbounded separation from the known positive frontier. The literature comparison does not establish exhaustive historical priority.
