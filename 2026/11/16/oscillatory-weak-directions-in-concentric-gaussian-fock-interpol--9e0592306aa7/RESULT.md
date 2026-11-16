# Oscillatory weak directions in concentric Gaussian Fock interpolation

## Finding

Fix an integer \(n\ge2\), a radius \(r>0\), and \(s>0\) with \(s\ne r\). At the two concentric regular \(n\)-gons \(r\omega^j,s\omega^j\), where \(\omega=e^{2\pi i/n}\) and \(0\le j<n\), form the Gram matrix \(G_n(r,s)\) of unit-norm evaluation kernels of the Gaussian Bargmann–Fock Hilbert space. It is strictly positive definite. Define

\[
\Lambda_\ell(t)=n e^{-t}\sum_{q=0}^{\infty}\frac{t^{\ell+nq}}{(\ell+nq)!},\qquad 0\le\ell<n,
\]

and let \(V_\ell(t)\) be the variance of a Poisson variable of mean \(t\), conditioned to lie in the congruence class \(\ell\pmod n\). Put

\[
c_\ell(r)=\frac{\Lambda_\ell(r^2)V_\ell(r^2)}{2r^2},\qquad
c_n(r)=\min_{0\le\ell<n}c_\ell(r).
\]

Then, with \(n,r\) held fixed and \(\varepsilon\to0\) through values with \(r+\varepsilon>0\),

\[
\lambda_{\min}(G_n(r,r+\varepsilon))
=c_n(r)\varepsilon^2+O_{n,r}(|\varepsilon|^3),\qquad
\lim_{\varepsilon\to0}\varepsilon^2\frac{\lambda_{\max}(G_n(r,r+\varepsilon))}{\lambda_{\min}(G_n(r,r+\varepsilon))}
=\frac{2\max_\ell\Lambda_\ell(r^2)}{c_n(r)}.
\]

The small- and large-radius laws are

\[
c_n(r)\sim\frac{n^3}{2(2n-1)!}\,r^{4n-4}\quad(r\downarrow0),\qquad
c_n(r)\longrightarrow\tfrac12\quad(r\to\infty).
\]

For all sufficiently small \(r>0\), the unique minimizing sector is \(\ell=n-1\). In marked contrast, **for every \(n\ge3\), each of the \(n\) sectors is the unique minimizer at infinitely many radii tending to infinity**. Thus the weak interpolation direction changes cyclically, without settling in any fixed Fourier sector, although every weak-direction coefficient tends to \(1/2\).

## Assumptions and scope

Use the Gaussian Fock space with scalar product normalized so that the reproducing kernel is \(K(z,w)=e^{z\bar w}\). Its normalized kernel at \(z\) is \(k_z(w)=e^{w\bar z-|z|^2/2}\). The Gram matrix is the Hermitian matrix of the \(2n\) vectors \(k_{r\omega^j}\) and \(k_{s\omega^j}\), with multiplicity and order determined by first listing one entire circle, then the other. The condition number is the ratio of largest to smallest *eigenvalue of the Gram matrix*, not the ratio of singular values of a synthesis operator. The two radii are positive and distinct; coincidence is the limiting singular configuration. The Poisson conditional law is defined for every \(t>0\) and has a positive variance since it assigns positive probability to infinitely many values in its congruence class. All limits keep the integer \(n\) fixed. The collision limit is taken with \(r\) fixed before any radius asymptotic.

## Proof

**1. Exact Fourier blocks.** The orthonormal monomial basis is \(e_k(w)=w^k/\sqrt{k!}\), for \(k\ge0\). A discrete angular Fourier transform of the kernels on a circle of radius \(r\) produces, in the \(\ell\)-th sector, the vector

\[
v_\ell(r)=\sqrt n\,e^{-r^2/2}\sum_{q\ge0}
\frac{r^{\ell+nq}}{\sqrt{(\ell+nq)!}}e_{\ell+nq}.
\]

The \(n\) sectors are mutually orthogonal and, for each \(\ell\), the two radii give the real symmetric block

\[
B_\ell(r,s)=n\begin{pmatrix}
 e^{-r^2}F_\ell(r^2)&e^{-(r^2+s^2)/2}F_\ell(rs)\\
 e^{-(r^2+s^2)/2}F_\ell(rs)&e^{-s^2}F_\ell(s^2)
\end{pmatrix},\qquad
F_\ell(x)=\sum_{q\ge0}\frac{x^{\ell+nq}}{(\ell+nq)!}.
\]

For positive distinct \(r,s\), the two sequences are not proportional: the quotient at consecutive support degrees changes by \((s/r)^n\ne1\). Strict Cauchy–Schwarz therefore makes every block positive definite and proves that the full Gram is positive definite.

**2. Collision coefficient.** Write \(v=v_\ell(r)\), \(u=v_\ell'(r)\), and let \(u_\perp=u-\langle u,v\rangle v/\|v\|^2\). Taylor expansion in the Fock norm gives \(v_\ell(r+\varepsilon)=v+\varepsilon u+O_{n,r}(\varepsilon^2)\). The determinant of the two-vector Gram block is \(\|v\|^2\|u_\perp\|^2\varepsilon^2+O_{n,r}(|\varepsilon|^3)\), while the trace approaches \(2\|v\|^2\). Therefore the small eigenvalue equals \(\|u_\perp\|^2\varepsilon^2/2+O_{n,r}(|\varepsilon|^3)\).

Under the probability distribution with mass proportional to \(e^{-r^2}r^{2k}/k!\) on \(k\equiv\ell\pmod n\), the logarithmic derivative of a component of \(v\) equals \(k/r-r\). Orthogonal projection removes its mean; the squared residual is exactly \(\|v\|^2\operatorname{Var}(k)/r^2=\Lambda_\ell(r^2)V_\ell(r^2)/r^2\). Hence the small-eigenvalue coefficient is \(c_\ell(r)\). The large eigenvalue of that block tends to \(2\Lambda_\ell(r^2)\). Since there are finitely many sectors, taking minima and maxima gives both spectral statements in the finding, including the condition-number formula.

**3. Radius zero.** The first two supported Poisson terms, with degrees \(\ell\) and \(\ell+n\), show for each \(0\le\ell<n\):

\[
\Lambda_\ell(r^2)\sim\frac{n r^{2\ell}}{\ell!},\qquad
V_\ell(r^2)\sim\frac{n^2\ell!}{(\ell+n)!}r^{2n},\qquad
c_\ell(r)\sim\frac{n^3}{2(\ell+n)!}r^{2\ell+2n-2}.
\]

Among finitely many positive functions, the uniquely highest exponent occurs at \(\ell=n-1\), hence this is the unique minimizer for sufficiently small positive \(r\), with the claimed constant.

**4. Explicit derivative identity and large-radius oscillation.** With \(t=r^2\), conditioning a Poisson law and differentiating its normalizing mass gives

\[
\operatorname{Var}(X_t\mid X_t\equiv\ell\pmod n)
=t+t\frac{\Lambda_\ell'(t)}{\Lambda_\ell(t)}
+t^2\left(\frac{\Lambda_\ell''(t)}{\Lambda_\ell(t)}
-\frac{\Lambda_\ell'(t)^2}{\Lambda_\ell(t)^2}\right).
\]

Therefore

\[
c_\ell(\sqrt t)=\tfrac12\left[\Lambda_\ell(t)+\Lambda_\ell'(t)
+t\Lambda_\ell''(t)-t\frac{\Lambda_\ell'(t)^2}{\Lambda_\ell(t)}\right].
\]

The roots-of-unity filter is the exact finite exponential sum

\[
\Lambda_\ell(t)=\sum_{j=0}^{n-1}\omega^{-j\ell}
\exp\bigl(t(\omega^j-1)\bigr).
\]

It follows immediately that \(\Lambda_\ell(t)\to1\), its first two derivatives tend to zero exponentially, and \(c_\ell(\sqrt t)\to1/2\); the convergence is uniform over the finite set of sectors.

Now suppose \(n\ge3\). Write \(\theta=2\pi/n\), \(\gamma=1-\cos\theta>0\), \(\beta=\sin\theta>0\), and \(\phi=\arg((\omega-1)^2)\). The indices \(j=1\) and \(j=n-1\) are the unique nontrivial Fourier frequencies with maximal real part \(\cos\theta\), and are conjugates. Expanding the displayed finite sum and its derivatives isolates their contribution:

\[
 c_\ell(\sqrt t)=\frac12+|\omega-1|^2\,t e^{-\gamma t}
 \cos(\beta t-\ell\theta+\phi)
 +o_n(t e^{-\gamma t})\quad(t\to\infty),
\]

uniformly for \(\ell=0,\ldots,n-1\). The lower-order terms \(\Lambda_\ell\) and \(\Lambda_\ell'\) contribute only \(O_n(e^{-\gamma t})\); all other roots contribute \(O_n(t e^{-\gamma' t})\) for some \(\gamma'>\gamma\), if present; and the nonlinear derivative-square term contributes \(O_n(t e^{-2\gamma t})\). This justifies the error estimate, including \(n=3\).

For each prescribed \(0\le\ell<n\), select the unbounded sequence of positive arguments

\[
t_{\ell,q}=\frac{\pi+\ell\theta-\phi+2\pi q}{\beta},\qquad q\to+\infty.
\]

At \(t_{\ell,q}\), the cosine for sector \(\ell\) equals \(-1\), while for every other sector \(h\ne\ell\) it equals \(-\cos((h-\ell)\theta)>-1\). Their gap is strictly positive for the fixed \(n\), so the uniform little-oh error cannot reverse the inequalities when \(q\) is large. Thus \(c_\ell(\sqrt{t_{\ell,q}})\) is the unique sector minimum for all sufficiently large \(q\). This proves infinitely recurring changes of the weak sector for each sector and completes the proof.

## Verification

The accompanying standalone `CHECK.py` uses two independent formulas for the collision coefficient: conditional Poisson moments and the exact finite roots-of-unity derivatives. It also compares eigenvalues of the full coherent-state Gram matrix with eigenvalues of the explicit \(2\times2\) Fourier blocks, checks the small-radius minimizing sector, and tests the predicted sequence of large-radius minimizers for several finite orders. Run `python CHECK.py` with Python, NumPy, and mpmath. These are finite consistency checks. Infinite recurrence, uniform asymptotic error estimates, and the limiting condition number are proved analytically above, not inferred from computation.

## Relationship to prior work

Fang and Tien (2026) establish density-level sampling and interpolation criteria for radial–angular Gaussian mixed-norm Fock spaces; they do not address the finite two-concentric-orbit Gram conditioning analyzed here. Horoshko, De Bièvre, Kolobov, and Patera (2016) describe Fourier-decomposed *single-circle* coherent-state spectra. The present two-circle block decomposition builds on that finite-cyclic framework, but its collision coefficient, conditioned-Poisson variance law, and recurrent weakest-sector phenomenon concern a different quantitative interpolation question. Kellay and Omari (2026) treat infinite complete interpolating sequences in differently weighted Fock-type spaces; their conclusions do not imply the present finite Gaussian two-ring assertions. The usual Hilbert-space two-vector Gram perturbation and roots-of-unity filter are standard methods, not claimed as new. Publication-priority verification remains subject to possible equivalent earlier formulations in circular coherent-state literature.

## Limitations

There is no claim about infinite sampling sequences, uniformity when \(n\to\infty\), simultaneous \(r\to\infty\) and \(s\to r\), displaced/rotated angular grids, or other weight functions. The periodic weak-sector switching describes the coefficient after the radial collision limit; it is not a statement that any fixed positive radial separation retains such switching at arbitrary large radii. No independent mathematical audit or exhaustive literature-priority certification has been performed.

## References

1. X. Fang and P. T. Tien, *Sampling and Interpolation in Gaussian Mixed-Norm Fock Spaces*, arXiv:2609.23572, first public 2026-09-20. https://arxiv.org/abs/2609.23572
2. D. B. Horoshko, S. De Bièvre, M. I. Kolobov, and G. Patera, *Entanglement of quantum circular states of light*, arXiv:1602.07852, first public 2016-02-25. https://arxiv.org/abs/1602.07852
3. K. Kellay and Y. Omari, *Complete interpolating sequences for Fock type spaces*, arXiv:2603.14679, first public 2026-03-16. https://arxiv.org/abs/2603.14679
