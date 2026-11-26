# Universal two-mode instability and a sharp collinear threshold for dissipatively coupled Stuart–Landau polygons

## Finding
Fix an integer \(M\geq3\), a cubic saturation coefficient \(k>0\), a strictly positive real diffusive coupling \(c>0\), a common angular frequency \(\omega\in\mathbb R\), and growth rates \(\beta_1,\ldots,\beta_M>Mc\). Set \(a_j=\beta_j-Mc>0\). For the all-to-all Stuart–Landau system
\[
\dot z_j=(\beta_j+i\omega-k|z_j|^2)z_j+c\sum_{\ell\ne j}(z_\ell-z_j),\qquad j=1,\ldots,M,
\]
let \(w=(w_1,\ldots,w_M)\) satisfy
\[
|w_j|=\sqrt{a_j/k},\qquad \sum_{j=1}^M w_j=0.
\]
Then \(z_j(t)=e^{i\omega t}w_j\) is an exact rotating polygon solution. Let \(J(w)\) denote its \(2M\)-dimensional **real** Jacobian in the co-rotating frame, and let \((n_+,n_-,n_0)\) count its strictly positive, strictly negative, and zero eigenvalues, with multiplicity.

**Noncollinear case.** If the real span of \(w_1,\ldots,w_M\) is two-dimensional, then
\[
\boxed{(n_+,n_-,n_0)=(2,M,M-2).}
\]
Every such polygon is a saddle with **exactly two exponentially unstable normal directions**, irrespective of the number of oscillators, the polygon shape, and the unequal growth parameters. The \(M-2\) neutral directions are exactly tangent to the smooth local family of closed polygons; all eigenvalues are real and semisimple.

**Collinear case.** If all \(w_j\) lie on one line through the origin, define the dimensionless radial susceptibility
\[
R=c\sum_{j=1}^M\frac{1}{2a_j}.
\]
Its **complete** Jacobian inertia is
\[
\boxed{
(n_+,n_-,n_0)=
\begin{cases}
(1,M,M-1),& R<1,\\
(1,M-1,M),& R=1,\\
(2,M-1,M-1),& R>1.
\end{cases}}
\]
Thus all collinear zero-mean polygons are also linearly unstable; the threshold \(R=1\) is the unique point where the collinear radial block acquires one additional zero eigenvalue. This is a linear-stability result, not a classification of nonlinear motion at the threshold.

## Assumptions and scope
The coupling is real, reciprocal, unnormalized, complete-graph diffusive coupling. The coefficient of the nonlinear frequency shift is zero, and all natural frequencies are identical. All oscillators are active (\(a_j>0\)); the theorem applies to any closed polygon satisfying the stated side lengths and does **not** assert that those lengths always close. In particular, the noncollinear case exists exactly when the largest side is strictly smaller than the sum of the other side lengths; at a collinear configuration, a signing of the side lengths must sum to zero. If \(\omega\ne0\), the eigenvalues in the rotating frame are real Floquet exponents of the rotating solution; if \(\omega=0\), the solution is stationary. At no point is a gradient-flow statement alone taken as a proof of the exact inertia.

## Proof
**1. The equilibrium and its potential.** Write \(z_j=e^{i\omega t}u_j\), and let \(S(u)=\sum_\ell u_\ell\). The equations become
\[
\dot u_j=(a_j-k|u_j|^2)u_j+cS(u).
\]
Every specified closed polygon \(w\) is therefore an equilibrium. In the real Euclidean structure on \(\mathbb C^M\cong\mathbb R^{2M}\), the flow is \(-\nabla V\) for
\[
V(u)=\sum_j\left(-\frac{a_j}{2}|u_j|^2+\frac{k}{4}|u_j|^4\right)-\frac{c}{2}|S(u)|^2.
\]
The potential differs from the standard diffusive-coupling potential only by an algebraic regrouping using \(a_j=\beta_j-Mc\). At \(w\), the real symmetric Hessian \(H=\nabla^2V(w)=-J(w)\) has quadratic form
\[
\boxed{\langle v,Hv\rangle=\sum_{j=1}^M2a_j\bigl[\operatorname{Re}(\overline{e_j}v_j)\bigr]^2-c\left|\sum_{j=1}^M v_j\right|^2,\qquad e_j=w_j/|w_j|.}
\]
Here \(v_j\in\mathbb C\) is arbitrary. The first term is positive semidefinite of real rank \(M\); the second is negative semidefinite of rank at most two. The polarization of this identity gives the exact linear operator
\[
(Hv)_j=2a_j\operatorname{Re}(\overline{e_j}v_j)e_j-c\sum_\ell v_\ell.
\]

**2. Exact noncollinear kernel.** If \(Hv=0\), project its \(j\)-th component on the tangent line \(i\mathbb Re_j\). This implies \(\operatorname{Re}(\overline{i e_j}S(v))=0\) for every \(j\). For a noncollinear polygon, two of these tangents are linearly independent in \(\mathbb R^2\), so \(S(v)=0\). The radial equations then imply \(\operatorname{Re}(\overline{e_j}v_j)=0\) for all \(j\). Conversely any vector of the form \(v_j=i e_jt_j\) with \(t_j\in\mathbb R\) and \(\sum_ji e_jt_j=0\) belongs to \(\ker H\). The latter complex equation has exactly two independent real constraints, so
\[
\ker H=\{(i e_jt_j)_j:\ t_j\in\mathbb R,\ \sum_j i e_jt_j=0\},\quad\dim\ker H=M-2.
\]
The same closure-map differential \(\theta\mapsto\sum_j|w_j|e^{i\theta_j}\) has rank two, proving by the implicit-function theorem that this kernel equals the tangent space of the locally smooth \((M-2)\)-dimensional polygon manifold. The radial lengths affect this tangent parameterization only through nonzero scaling.

**3. Exact noncollinear inertia.** From Step 1, \(H\) is a rank-at-most-two negative perturbation of a nonnegative matrix with \(M\) strictly positive eigenvalues and \(M\) zero eigenvalues. Consequently its negative index is at most two and its positive index is at most \(M\). By Step 2 its nullity is exactly \(M-2\), hence its rank is \(M+2\). The only way this rank can be achieved under the two upper bounds is for \(H\) to have exactly \(M\) positive and two negative eigenvalues. Since \(J=-H\) and \(H\) is real symmetric, the asserted \((2,M,M-2)\) follows, with semisimplicity of every eigenvalue. Both unstable modes are transverse to the equilibrium manifold, as is every nonzero eigenmode.

**4. Exact collinear inertia.** Rotate coordinates so each \(e_j\) is \(+1\) or \(-1\). The Hessian splits into independent real- and imaginary-coordinate blocks
\[
H_\parallel=D-c\mathbf1\mathbf1^{\mathsf T},\qquad H_\perp=-c\mathbf1\mathbf1^{\mathsf T},\qquad D=\operatorname{diag}(2a_1,\ldots,2a_M)>0.
\]
The perpendicular block has one negative and \(M-1\) zero eigenvalues. Congruence by \(D^{-1/2}\) turns the parallel block into \(I-cvv^{\mathsf T}\), with \(v=D^{-1/2}\mathbf1\) and \(c\|v\|^2=R\). Sylvester's inertia theorem therefore gives \(M\) positive parallel eigenvalues if \(R<1\), \(M-1\) positive and one zero if \(R=1\), and \(M-1\) positive and one negative if \(R>1\). Negating the combined Hessian produces exactly the three tabulated inertias. The threshold and the change in unstable dimension are thus sharp for every eligible collinear polygon.

## Verification
The included `verify_inertia.py` symbolically differentiates the original polynomial vector field and computes exact eigenvalues for one equilateral three-oscillator polygon, one square four-oscillator polygon, and a collinear four-oscillator polygon on each side of and exactly at \(R=1\). It independently checks polygon closure, the rotating-frame equilibrium, real Jacobian symmetry, and the five predicted positive/negative/zero inertia triples. Run `python verify_inertia.py` with SymPy. These finite examples are checks, not a substitute for the universal rank and congruence proof in Steps 1–4.

## Relationship to prior work
Zhao and Uchida (2026) introduced the vanishing-mean-field polygon manifold, calculated its side lengths, identified the purely real-coupled gradient potential, and numerically sampled transverse stability for a **different, complex coupling regime**. Those ingredients and the existence/dimension statements are not new claims here. Their analysis does not state the complete all-population positive/negative/zero inertia for positive purely real coupling or the sharp collinear threshold. The present proof extracts these particular full-spectrum sign counts without computing eigenvalues numerically.

Two published studies of the **purely reactive** coupling regime prove normal attraction and finer spectral laws for noncollinear polygons. Their assumption of a nonzero imaginary coupling cannot be specialized to the purely real coupling of this theorem; in fact their normal stability conclusion is opposite to the positive two-mode index established here. A contemporary energy-landscape study of spatially structured and frustrated oscillator networks establishes gradient methods and analyzes saddle indices in a different interaction geometry; it does not give the present complete-graph, all-positive-active-radii formula. General rank-one inertia and implicit-function principles are classical tools, not themselves claimed as discoveries.

## Limitations
Positive real coupling, strictly positive active amplitudes, zero nonlinear frequency shift, and identical natural frequencies are essential hypotheses. The theorem is local and linear; at the collinear degeneracy \(R=1\) it does not determine nonlinear center-manifold dynamics, and no claim is made about basins of attraction, global convergence, or the arbitrary complex-coupling case. It does not show all polygon side lengths are realizable. Historical priority for the precise inertia law has not been independently certified.

## References
1. L. Zhao and N. Uchida, *Heterogeneity-induced chaos in globally coupled Stuart–Landau oscillators*, arXiv:2610.08239v1, first released 2026-10-06, https://arxiv.org/abs/2610.08239 ; especially Sections 3 and 5.
2. *Universal transverse attraction of noncollinear Stuart–Landau polygons under reactive coupling*, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-universal-transverse-attraction-of-noncollinear-stuart-landau-po--568cb1115538 .
3. *Exact finite-population spectrum and slow relaxation of reactive Stuart–Landau polygons*, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-finite-population-spectrum-and-slow-relaxation-of-reactive--a0832bb5dd4e .
4. *Energy landscapes and synergetic state transitions in frustrated Stuart–Landau oscillator networks: a homotopy continuation study*, *Frontiers in Network Physiology* (2026), https://doi.org/10.3389/fnetp.2026.1778380 .
