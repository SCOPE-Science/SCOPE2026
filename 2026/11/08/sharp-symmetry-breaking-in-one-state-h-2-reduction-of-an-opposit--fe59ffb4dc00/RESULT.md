# Sharp symmetry breaking in one-state \(H_2\) reduction of an opposite-pole system

## Finding

Let \(a>0\), \(0<p<1\), and consider the real, stable, two-state, strictly proper discrete-time transfer function with normalized delay-free factor
\[
G_p(z)=\frac{a}{1-pz}+\frac{a}{1+pz}=\frac{2a}{1-p^2z^2}.
\]
The physical transfer function is \(zG_p(z)\). Among **every** complex stable one-state transfer function \(zR_{\lambda,c}(z)\), with
\[
R_{\lambda,c}(z)=\frac{c}{1-\overline\lambda z},\qquad |\lambda|<1,\quad c\in\mathbb C,
\]
the global \(H_2\)-optimal reduced model is completely classified. Writing \(t=p^2\), its optimal pole and residue parameters are
\[
(\lambda,c)=
\begin{cases}
(0,2a),&0<t\le\tfrac12,\\
\bigl(\pm\sqrt{2-1/t},\,a/t\bigr),&\tfrac12<t<1.
\end{cases}
\]
The first branch has **one** global minimizer and the second has **exactly two**, even after allowing complex reduced poles and residues. The sharp transition is \(p=1/\sqrt2\). The minimal **squared** \(H_2\) error is
\[
\mathcal E_{\min}^2=
\begin{cases}
\dfrac{4a^2}{1-t^2}-4a^2,&0<t\le\tfrac12,\\
\dfrac{4a^2}{1-t^2}-\dfrac{a^2}{t(1-t)},&\tfrac12<t<1.
\end{cases}
\]
For \(t>1/2\), the symmetry-fixed parameter \(\lambda=0\) remains stationary but becomes a saddle of the two-real-dimensional complex-pole error landscape. Its excess **squared** error over the global minimum is exactly
\[
\Delta\mathcal E^2=\frac{a^2(2t-1)^2}{t(1-t)}.
\]
At the threshold, the loss along real poles is quartic; the two optimal poles emerge continuously with square-root scaling.

## Assumptions and scope

The model has equal positive residues \(a\), opposite real stable state eigenvalues \(\pm p\), no feedthrough, and the complete infinite impulse-response \(H_2\) objective in exact arithmetic. The coefficient convention is \(G(z)=\sum_{n\ge0}g_nz^n\) with \(\|G\|_{H_2}^2=\sum_{n\ge0}|g_n|^2\). The original strictly proper transfer function is \(zG\), and multiplication by the inner function \(z\) leaves this norm unchanged. The competitor has one state, potentially a complex state eigenvalue, and a freely chosen complex residue. Allowing complex competitors only strengthens the global claim; all optimizers turn out real. The state realization at \(\lambda=0\) is valid for the original strictly proper \(zR\), despite the normalized factor \(R\) being constant. Parameters \(p=0\), \(p=1\), and \(a=0\) are excluded.

## Proof

1. **Projection at a fixed pole.** The Szegő kernel \(k_\lambda(z)=(1-\overline\lambda z)^{-1}\) has \(\|k_\lambda\|_{H_2}^2=(1-|\lambda|^2)^{-1}\) and \(\langle G_p,k_\lambda\rangle=G_p(\lambda)\). Orthogonal projection onto its complex span gives the **unique** optimal coefficient
\[
c_\lambda=(1-|\lambda|^2)G_p(\lambda),
\]
and Pythagoras gives
\[
\min_c\|G_p-c k_\lambda\|_{H_2}^2
=\|G_p\|_{H_2}^2-\Phi(\lambda),\quad
\Phi(\lambda)=(1-|\lambda|^2)|G_p(\lambda)|^2.
\]
Since the even impulse coefficients are \(2ap^{2j}\) and all odd coefficients vanish, \(\|G_p\|_{H_2}^2=4a^2/(1-p^4)=4a^2/(1-t^2)\).

2. **No missing complex optimum.** For every \(|\lambda|=r<1\),
\[
\Phi(\lambda)=\frac{4a^2(1-r^2)}{|1-t\lambda^2|^2}
\le\frac{4a^2(1-r^2)}{(1-tr^2)^2}=\Phi(r),
\]
by the reverse triangle inequality. For \(0<r<1\) equality requires \(\lambda^2=r^2\), so \(\lambda\in\{-r,r\}\). At \(r=0\) there is only one pole. Furthermore \(\Phi(\lambda)\to0\) as \(|\lambda|\uparrow1\), whereas \(\Phi(0)=4a^2\), hence a maximum exists and none is omitted at the disk boundary.

3. **Complete real radial optimization.** With \(s=r^2\in[0,1)\), maximize
\[
f_t(s)=\frac{4a^2(1-s)}{(1-ts)^2},\qquad
f_t'(s)=\frac{4a^2(2t-1-ts)}{(1-ts)^3}.
\]
For \(0<t\le1/2\), the derivative is strictly negative for every \(s>0\), so the unique global maximum is \(s=0\). For \(1/2<t<1\), the derivative changes from positive to negative exactly at \(s_*=2-1/t\in(0,1)\). Consequently the only global parameters are \(\lambda=\pm\sqrt{s_*}\). In the first regime the optimum captured norm is \(4a^2\); in the second it is \(f_t(s_*)=a^2/[t(1-t)]\). Substitution into the projection coefficient yields \(c_0=2a\) and \(c_{\pm}=a/t\). This proves the global classification and the error formula.

4. **Symmetry-fixed stationary point and quantitative bifurcation.** Expanding near the origin with \(\lambda=x+iy\),
\[
\frac{\Phi(x+iy)}{4a^2}
=1+(2t-1)x^2-(2t+1)y^2+O(|\lambda|^4).
\]
Thus for \(t>1/2\), the origin is a stationary saddle of the captured-norm landscape and hence of squared error. For \(t=1/2\) and real \(x\), the exact identity is
\[
4a^2-\Phi(x)=\frac{a^2x^4}{(1-x^2/2)^2}.
\]
For \(t=1/2+\varepsilon\downarrow1/2\), \(|\lambda_\pm|=\sqrt{2-1/t}=2\sqrt\varepsilon+O(\varepsilon^{3/2})\). Subtracting \(4a^2\) from the supercritical captured norm gives the stated strict loss \(\Delta\mathcal E^2\).

## Verification

The bundled standalone \(\texttt{verify.py}\) checks all rational identities with exact fractions, evaluates each of six parameter cases by independent finite impulse-response reconstruction, and tests the global angular/radial bound at 58,500 deterministic complex samples. A symbolic derivative and critical expansion can also be verified directly from the displayed formulas. These numerical checks are supplementary: the proof covers every real \(a>0\), every \(0<p<1\), every complex stable \(\lambda\), and every complex \(c\) analytically.

For an exact example, set \(a=1\) and \(p^2=3/4\). Then the global pole pair is \(\pm\sqrt{2/3}\), each with residue \(4/3\), and
\[
\mathcal E_{\min}^2=\frac{80}{21},\qquad
\mathcal E_{\lambda=0}^2=\frac{36}{7},\qquad
\Delta\mathcal E^2=\frac43.
\]

## Relationship to prior work

Angino, Dózsa, and Voigt (2026) establish general necessary \(H_2\)-optimality equations and a stable Newton-type approach to the resulting root-finding problem; their discrete-time benchmarks have higher state and reduced orders. Their conditions motivate but do not state the present **global**, complex-admissible two-pole phase transition, exact optimizer multiplicity, and squared-error loss. Wang and Qian (2020) establish existence of best rational approximants in Hardy space but do not classify the global optimizer of this opposite-pole family. Van Dooren, Gallivan, and Absil (2008) present generic stationary conditions and numerical examples of nonconvex reduced-order fitting; their examples do not imply the exact disk threshold here. Varah (1982/1985) analyzes nonunique best exponential fits, notably for positive decays in continuous time, which is a related but different admissible family from a discrete-time system with one negative state eigenvalue. All generic projection formulas are acknowledged as established; the new content is the complete parametric global classification and its exact saddle/error boundary.

## Limitations

This theorem concerns a real two-mode family with *equal positive* residues and *opposite* poles, and the exact all-time \(H_2\) objective. It does not classify unequal-residue systems, systems of dimension above two, restricted-positive reduced eigenvalues, finite-sample least squares, numerical convergence of a particular root finder, or floating-point rounding. The sign of either optimal nonzero reduced pole does not represent a unique physical-model choice. The global classification is proved here; claims of independent external verification or historical uniqueness are not made.

## References

- A. Angino, T. Dózsa, and M. Voigt, “\(H_2\)-optimal model order reduction using hyperbolic geometry,” arXiv:2610.16249v1 (first public version 2026-10-12), https://arxiv.org/html/2610.16249v1 .
- Y.-B. Wang and T. Qian, “Pseudo-hyperbolic distance and n-best rational approximation in \(H^2\) space,” arXiv:2012.06184v1 (2020), https://arxiv.org/pdf/2012.06184 .
- P. Van Dooren, K. A. Gallivan, and P.-A. Absil, “\(H_2\)-Optimal Approximation of MIMO Linear Dynamical Systems,” SIAM Journal on Matrix Analysis and Applications (2008), https://sites.uclouvain.be/absil/Publi/H2-modred-mimo/SIMAX_08PA.pdf .
- J. M. Varah, “On Fitting Exponentials by Nonlinear Least Squares,” University of British Columbia report TR-82-02 (1982), https://www.cs.ubc.ca/sites/default/files/tr/1982/TR-82-02.pdf ; published in SIAM Journal on Scientific and Statistical Computing 6 (1985), 30–44.
