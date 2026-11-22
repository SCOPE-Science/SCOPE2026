# Exact position-invariant polarization in a two-hostile-link opinion path

## Finding

Let \(K\ge3\) individuals be joined by unit attractive links on the path \(1-2-\cdots-K\). Add unit repulsive links between the endpoints \(1,K\) and along exactly one path edge \(j,j+1\), for any \(j\in\{1,\ldots,K-1\}\). Under the nonlinear attraction–repulsion opinion equation of Boyce, Farina, McKerral, Shelyag and Zuparic, define
\[
\Lambda_K=\frac{K+\sqrt{(K-2)^2+4}}2,
\qquad \alpha_*(K)=\Lambda_K^{-1}.
\]
The critical repulsion strength \(\alpha_*\) is independent of \(j\) and is sharp. If \(0<\alpha\le\alpha_*\), consensus is the **only equilibrium** at any fixed population mean, and all trajectories converge to it. If \(\alpha>\alpha_*\), consensus is unstable and there are **exactly two global potential minimizers** at each fixed mean, interchanged by opinion reversal; both are locally exponentially attracting. This does not assert that all other stationary states are absent or unstable.

For each polarized minimizer, choose the orientation in which opinions decrease from the first node to the last. Every ordinary attractive path edge has the same positive opinion drop \(u\), and the one path edge which also repels has drop \(u+v\), where \((u,v)\in(0,1)^2\) is the unique strictly positive solution of
\[
u=\tanh\bigl(\alpha((K-1)u+v)\bigr),
\qquad v=\tanh\bigl(\alpha(u+v)\bigr).
\]
In particular, the range \(x_1-x_K=(K-1)u+v\), the global minimum energy and the onset threshold are exactly independent of the hostile edge position for every strength, not merely asymptotically near consensus. The edge position only determines which step is enlarged. The opposite minimizer has every drop negated.

## Assumptions and scope

For real opinions \(x_1,\ldots,x_K\), use the deterministic autonomous system
\[
\dot x_i=-\frac1K\left[\sum_{k:\{i,k\}\in E_A}(x_i-x_k)
-\sum_{k:\{i,k\}\in E_R}\tanh\bigl(\alpha(x_i-x_k)\bigr)\right],
\]
where \(E_A=\{\{i,i+1\}:1\le i<K\}\) and \(E_R=\{\{1,K\},\{j,j+1\}\}\), each undirected edge counted once in the potential, and \(\alpha>0\). Overlapping attraction and repulsion edges are intentional. The mean \(\bar x=K^{-1}\sum_i x_i\) is invariant. "Global minimizers" means minimizers of the model's potential restricted to a specified invariant mean hyperplane. "Stable" means local exponential stability on that hyperplane; the conserved mean gives a neutral direction in the unrestrained ambient space.

## Proof

**1. Exact path-gradient reduction.** Set \(m=K-1\) and \(y_i=x_i-x_{i+1}\) for \(1\le i\le m\). The fixed-mean map from \(x\) to \(y\in\mathbb R^m\) is bijective. Since \(x_1-x_K=S:=\sum_i y_i\), the original potential equals \(\Phi_j(y)/K\), with
\[
\Phi_j(y)=\frac12\sum_{i=1}^{m}y_i^2-\frac1\alpha\log\cosh(\alpha S)
-\frac1\alpha\log\cosh(\alpha y_j).
\]
The opinion flow is Euclidean gradient descent of this potential in \(x\). Under the change to \(y\), the metric need not be Euclidean, but stationary points, potential values and the inertia of Hessians are preserved. A permutation of the \(m\) path-difference coordinates taking coordinate \(j\) to \(\ell\) maps \(\Phi_j\) **exactly** to \(\Phi_\ell\). This proves placement invariance for energy and equilibrium differences (not equality of transient trajectories).

**2. Sharp consensus threshold.** Write \(e=(1,\ldots,1)^\top\) and \(e_j\) for a coordinate unit vector. At \(y=0\),
\[
D^2\Phi_j(0)=I_m-\alpha(ee^\top+e_je_j^\top).
\]
The two nonzero eigenvalues of \(ee^\top+e_je_j^\top\) equal the eigenvalues of \(M=\begin{pmatrix}m&1\\1&1\end{pmatrix}\), hence its spectral radius is
\(\Lambda_K=(m+1+\sqrt{(m-1)^2+4})/2\). Therefore the first negative Hessian direction appears exactly when \(\alpha>1/\Lambda_K\), regardless of \(j\).

For \(\alpha<\alpha_*\), use \(0\le\operatorname{sech}^2\le1\) to obtain
\[
D^2\Phi_j(y)=I_m-\alpha\operatorname{sech}^2(\alpha S)ee^\top
-\alpha\operatorname{sech}^2(\alpha y_j)e_je_j^\top\succ0.
\]
Thus \(\Phi_j\) is strictly convex. At equality \(\alpha=\alpha_*\), for every \(y\ne0\), strict inequality \(z\tanh(\alpha z)<\alpha z^2\) for nonzero \(z\) gives
\[
y\cdot\nabla\Phi_j(y)=\|y\|^2-S\tanh(\alpha S)-y_j\tanh(\alpha y_j)
>\|y\|^2-\alpha(S^2+y_j^2)\ge0;
\]
if \(S=y_j=0\), the displayed strictness follows instead directly from \(\|y\|^2>0\). Hence consensus is the unique critical point also at the endpoint. The potential is coercive since the log-cosh terms grow at most linearly in \(\|y\|\). Smooth gradient trajectories remain in compact sublevel sets, and every omega limit lies among critical points, so all trajectories at fixed mean converge to consensus for \(\alpha\le\alpha_*\).

**3. Existence and form of global polarized minima.** If \(\alpha>\alpha_*\), the origin is not a local minimizer, whereas coercivity ensures at least one nonzero global minimizer. For any \(y\), \(\Phi_j(|y_1|,\ldots,|y_m|)\le\Phi_j(y)\), with strict inequality whenever both positive and negative path drops occur: the quadratic and \(\log\cosh(\alpha y_j)\) terms are unchanged, but \(\log\cosh(\alpha |S|)\) increases strictly when \(|S|<\sum|y_i|\). Therefore each global minimum has a consistent sign; by sign reversal consider a nonnegative minimizer. Its stationarity equations are
\[
y_i=\tanh(\alpha S)\quad(i\ne j),\qquad
y_j=\tanh(\alpha S)+\tanh(\alpha y_j).
\]
A nonzero nonnegative critical vector necessarily has strictly positive components. Put \(u=\tanh(\alpha S)\), \(v=\tanh(\alpha y_j)\). Then \(y_i=u\) except \(y_j=u+v\), and \(S=mu+v\), producing the displayed two-equation system.

**4. Existence and uniqueness of the positive branch.** In vector form \(h=(u,v)^\top=\tanh(\alpha M h)\), with tanh applied componentwise and all entries of \(M\) positive. When \(\alpha\Lambda_K>1\), for a positive Perron eigenvector \(w\), a sufficiently small positive multiple \(\delta w\) is a strict subsolution, whereas \((1,1)^\top\) is a strict supersolution. Monotone iteration yields a positive fixed point. If \(h,k>0\) are two positive fixed points, let \(t=\max_i h_i/k_i\). If \(t>1\), positivity and \(\tanh(tz)<t\tanh(z)\) for \(z>0\) imply \(h_i\le \tanh(\alpha M(tk))_i<t\tanh(\alpha Mk)_i=tk_i\) for every coordinate, contradicting equality at a maximizing coordinate. Reverse the comparison if \(t\le1\); thus \(h=k\). Every global minimizer is therefore one of the two sign-related critical vectors, and they exist for all \(\alpha>\alpha_*\).

**5. Local strict attraction.** At a positive minimizer put \(d_1=\operatorname{sech}^2(\alpha S)\), \(d_2=\operatorname{sech}^2(\alpha(u+v))\) and \(D=\operatorname{diag}(d_1,d_2)\). Since \(z\operatorname{sech}^2 z<\tanh z\) for \(z>0\), the fixed-point equation gives \(\alpha D M h<h\). By the positive-matrix Perron criterion, \(\rho(\alpha D M)<1\). The nonzero eigenvalues of \(\alpha(d_1ee^\top+d_2e_je_j^\top)\) agree with those of \(\alpha D^{1/2}MD^{1/2}\); all are below one. Thus \(D^2\Phi_j\succ0\) at both global minimizers. Since the original fixed-mean flow is a genuine smooth gradient descent, both are locally exponentially attracting.

**6. Critical onset amplitude (optional refinement).** Let \(\varepsilon=\alpha/\alpha_*-1>0\), \(t=(\Lambda_K-1)^{-1}\), and \(\varepsilon\downarrow0\). Lyapunov–Schmidt reduction of \(h=\tanh(\alpha M h)\) along the normalized positive eigenvector proportional to \((1,t)\), using \(\tanh z=z-z^3/3+O(z^5)\), yields
\[
u=\sqrt{\frac{3(1+t^2)}{1+t^4}}\,\sqrt\varepsilon+O(\varepsilon^{3/2}),
\qquad v=tu+O(\varepsilon^{3/2}).
\]
The order and coefficients follow by taking the scalar product with the Perron eigenvector: \(\varepsilon a\|w\|^2=(a^3/3)\sum_i w_i^4+O(a^5+\varepsilon a^3)\). This coefficient is also independent of \(j\).

## Verification

The included standalone `CHECK.py` numerically evaluates the matrix threshold, critical Hessian, positive nonlinear fixed point, stationary Euler–Lagrange equations, local Hessian definiteness, equal potentials across all possible hostile-edge positions and the small-amplitude formula. It completed **750 finite assertions** for \(3\le K\le12\), all hostile-edge positions and several positive controversy strengths. These tests supplement, but do not prove, the all-\(K\) theorem. Reproduce with `python CHECK.py` using NumPy and SciPy.

## Relationship to prior work

Boyce et al. define the attraction–repulsion dynamical system, its gradient potential and a general consensus criterion. Their published Appendix C, arrangement B, explicitly considers an endpoint-hostile chord plus one hostile path edge at an end and gives only the interval \(1/K\le\alpha_*<1/(K-1)\). The exact algebraic onset, arbitrary hostile-edge placement invariance, exact nonlinear minimizing profiles, unique positive equilibrium profile and strict local stability proved here are not asserted by their Appendix C. The generalized signed-Laplacian spectral theory of Bronski and DeVille already supplies broad machinery for analyzing destabilizing negative links; this result does not claim to originate signed-Laplacian spectral analysis. Other opinion-placement studies concern different dynamics (e.g. fixed leaders or bounded-confidence updating), so the structural mathematical equivalence to this tanh-gradient model is absent in their described statements.

## Limitations

This is a deterministic finite-network theorem for a particular *overlapping* pair of repulsive edges and a unit attractive path, not a claim about arbitrary graphs or stochastic behavior. Global minimizer uniqueness means exactly two minimizing polarized equilibria; additional non-minimizing stationary points are not classified. The placement permutation acts on opinion *differences*, not by merely relabeling vertices, and therefore does not assert identical transients or basins. The sharp onset refers to a mean-constrained stability transition; the global mean always remains conserved. Historical priority beyond the inspected primary papers and indexed mathematical summaries remains open to independent scrutiny.

## References

1. J. Boyce, M. Farina, J. McKerral, S. Shelyag, M. Zuparic, *Opinion dynamics modelling: distinct attraction and repulsion topologies highlight quantitative effects of trolling*, arXiv:2512.05725 (first submitted 2025-12-05), https://arxiv.org/abs/2512.05725. Published in *Journal of Nonlinear Science* 36, 112 (2026), https://doi.org/10.1007/s00332-026-10333-0, especially Sect. 2 and Appendix C.
2. J. C. Bronski and L. DeVille, *Spectral Theory for Networks with Attractive and Repulsive Interactions*, arXiv:1303.0718 (2013), https://arxiv.org/abs/1303.0718.
