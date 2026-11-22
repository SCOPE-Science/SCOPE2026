# Exact false-nearest-neighbour spectra and an optimal frequency for three-delay circle observations

## Finding
Let \(T_\alpha(u)=u+2\pi\alpha\pmod{2\pi}\) be an irrational circle rotation and let \(h(u)=\cos u\). For each \(n\ge2\), construct the \(n\) three-delay vectors \(Y_i=(h(T_\alpha^i u_0),h(T_\alpha^{i+1}u_0),h(T_\alpha^{i+2}u_0))\), for \(0\le i<n\). Choose an arbitrary nearest other vector \(Y_{j(i)}\) in Euclidean distance. Declare \(i\) false if either
\[
\frac{|h(T_\alpha^{i+3}u_0)-h(T_\alpha^{j(i)+3}u_0)|}{\|Y_i-Y_{j(i)}\|}>R
\quad\text{or}\quad
\frac{|h(T_\alpha^{i+3}u_0)-h(T_\alpha^{j(i)+3}u_0)|}{\sigma_n}>A_{\mathrm{tol}},
\]
where \(R,A_{\mathrm{tol}}>0\) and \(\sigma_n\) is the empirical standard deviation of the \(n+3\) observed scalar samples. Write \(p_n\) for the fraction declared false.

Set \(\theta=2\pi\alpha\), \(z=\cos^2\theta\), \(\lambda=R^2\), and
\[
E(z)=\frac{8z^2-2z+1}{2z+1},\qquad
\tau=1-3\lambda,\qquad
\Delta=2\lambda(1-z)(1+2z)(\lambda-E(z)).
\]
Then for **every** initial phase, every tie-breaking choice, and all positive tolerances, the limit exists and is
\[
\boxed{\lim_{n\to\infty}p_n=
\begin{cases}
0,&\lambda\ge E(z),\\[3pt]
\displaystyle\frac2\pi\arctan\sqrt{\frac{\tau+\sqrt{\tau^2-4\Delta}}{\sqrt{\tau^2-4\Delta}-\tau}},&0<\lambda<E(z).
\end{cases}}
\]
Thus the limiting false-neighbour fraction is independent of initial phase and of the absolute-distance tolerance, and it is strictly positive exactly when \(R<\sqrt{E(z)}\), even though the three-delay map is a smooth embedding of the circle.

Furthermore, among all irrational rotation angles, the smallest exact uniform relative-tolerance threshold for zero false neighbours is
\[
\boxed{R_{\mathrm{crit,min}}=\sqrt{4\sqrt2-5}},
\]
attained precisely when \(\cos^2(2\pi\alpha)=(\sqrt2-1)/2\). These optimizing rotation numbers are irrational.

## Assumptions and scope
The phase space is \(\mathbb R/(2\pi\mathbb Z)\), with its usual circle dynamics. The rotation number \(\alpha\) is irrational, \(h(u)=\cos u\), three consecutive delay coordinates and one consecutive appended coordinate are used, and there is no observational noise. Only the one-nearest-neighbour (excluding self) criterion is studied. The \(n+3\) scalar observations used for \(\sigma_n\) have indices \(0\) through \(n+2\). The ratio thresholds \(R>0\) and \(A_{\mathrm{tol}}>0\) are fixed independently of \(n\). The formula is not asserted for rational rotations, general observables, larger temporal exclusion windows, or noisy data. Norms on delay space are Euclidean.

## Proof
**1. Exact chord identity and uniform neighbour convergence.** Let \(V_j=(\cos(j\theta),\sin(j\theta))\) for \(j=0,1,2,3\), and let \(A_3=\sum_{j=0}^2V_jV_j^\top\). Because \(\sin\theta\ne0\), the first two linear measurements of the unit-circle coordinate already constitute an invertible affine-linear image; therefore the three-delay map is a smooth embedding. Every irrational rotation orbit is dense. Moreover, the maximum distance from any circle point to its nearest *distinct* phase among the first \(n\) orbit points tends to zero uniformly. To see this, fix an arc length \(\varepsilon>0\). Compactness and minimality furnish a finite orbit segment meeting each of finitely many arcs of diameter below \(\varepsilon\) at least twice; any sufficiently long initial orbit segment contains these points. Its delay image is correspondingly a uniform twofold net. Inverting the embedded circle map shows that the phase separation of every selected nearest neighbour tends uniformly to zero.

The exact cosine chord formula
\[
\cos(u+j\theta)-\cos(v+j\theta)=-2\sin\frac{u-v}{2}\,\sin\left(\frac{u+v}{2}+j\theta\right)
\]
shows that the appended-coordinate difference divided by the three-delay distance is **exactly**
\[
r_\theta(w)=\frac{|\sin(w+3\theta)|}{\sqrt{\sin^2w+\sin^2(w+\theta)+\sin^2(w+2\theta)}},
\qquad w=\frac{u+v}{2},
\]
for any distinct orbit phases (all denominators are nonzero). This quantity is continuous modulo \(\pi\), and the uniform phase closeness implies that each empirical ratio is uniformly approximated by \(r_\theta(u_0+i\theta)\). Unique ergodicity gives \(\sigma_n\to1/\sqrt2\); moreover, the future coordinate of every nearest pair differs by \(o(1)\) uniformly. Hence the absolute-distance condition is eventually false at every index.

**2. Limiting angular law.** Put \(b=V_3\) and \(v(w)=(\sin w,\cos w)\). Then \(r_\theta(w)^2=(v(w)^\top bb^\top v(w))/(v(w)^\top A_3v(w))\). The positive matrix \(A_3\) has trace \(3\) and
\[
\det A_3=2\sin^2\theta+\sin^2(2\theta)=2(1-z)(1+2z)>0.
\]
Direct multiplication, or the adjugate identity, yields
\[
b^\top A_3^{-1}b=E(z)=\frac{8z^2-2z+1}{2z+1}.
\]
Cauchy–Schwarz in the \(A_3\) inner product makes \(E(z)\) the maximum squared ratio. For \(\lambda<E(z)\), the matrix \(B=bb^\top-\lambda A_3\) has eigenvalues of opposite signs because
\[
\operatorname{tr}B=1-3\lambda=\tau,
\qquad\det B=\lambda\det A_3(\lambda-E(z))=\Delta<0.
\]
With \(D=\sqrt{\tau^2-4\Delta}\), the positive and negative eigenvalues are \((\tau+D)/2\) and \((\tau-D)/2\). Uniform angle measure satisfies \(v^\top Bv>0\) on a fraction \(\frac2\pi\arctan\sqrt{(\tau+D)/(D-\tau)}\) of the circle. The boundary consists of finitely many angles and has zero measure. Irrational rotation equidistribution and the uniform nearest-ratio approximation show that the same fraction is \(\lim p_n\). If \(\lambda\ge E(z)\), the ratio is never strictly greater than \(R\), even for a finite chord, and the absolute-distance condition eventually vanishes, so \(p_n\to0\).

**3. Sharp global frequency optimum.** Differentiating the explicit function of \(z\) gives
\[
E'(z)=\frac{4(4z^2+4z-1)}{(2z+1)^2}.
\]
On \(0\le z<1\) this changes sign exactly once at \(z_*=(\sqrt2-1)/2\), yielding the unique global minimum \(E(z_*)=4\sqrt2-5\). It is attained within irrational rotations. Indeed if \(t=2|\cos\theta|\) at the minimum, then \(t^2=2\sqrt2-2\), and \(t\) has irreducible polynomial \(t^4+4t^2-4=0\) over \(\mathbb Q\). Its other conjugates include nonreal numbers. If \(\alpha\) were rational, \(2\cos(2\pi\alpha)\) would be a sum of two roots of unity, all of whose algebraic conjugates are real, a contradiction. The irreducibility follows because \(t^2\) has degree two while \(t\notin\mathbb Q(\sqrt2)\): the rational part of the square of \(a+b\sqrt2\), for rational \(a,b\), cannot equal \(-2\).

## Verification
Run `python CHECK.py` from this directory (requires SymPy, NumPy and SciPy). It symbolically verifies the Gram determinant, exact squared maximum, derivative, and algebraic minimum. It independently reconstructs nearest neighbours from actual finite rotation orbits and compares six empirical fractions against the analytic limiting formula. All six deviations are below \(0.015\). The finite samples are checks of the derivation, not proof of the infinite limits; the preceding exact chord argument and irrational equidistribution are the proof.

## Relationship to prior work
Śpiewak, *On the convergence of the False Nearest Neighbours algorithm*, arXiv:2611.18087v1, develops general typical-observable convergence statements and the precise two-tolerance FNN definition. Its Theorems 1.2 and 1.3 provide neither the exact fixed-cosine irrational-rotation threshold distribution nor the sharp frequency optimization. The classical Kennel–Brown–Abarbanel method supplies the algorithm, not the present limit law. Analyses of harmonic delay embeddings give useful linear-algebra context but do not automatically imply the nearest-neighbour empirical distribution or the sharp uniform threshold. The statement here concerns one explicit nonmixing family and one nongeneric smooth observable, not prevalence.

## Limitations
The formulas are specific to three consecutive delay coordinates, the fourth appended observation, Euclidean nearest neighbours and the cosine observable. They do not imply that a positive FNN fraction proves a failure of injectivity: the three-delay map here is already embedded, and a too-small tolerance produces a nonzero fraction because of nonzero tangent expansion. The optimal parameter is an optimization of the worst relative coordinate ratio within this family, not of all embedding designs. The exact limit does not supply a universal convergence rate in \(n\), especially for Liouville rotations. Literature priority beyond the inspected publications remains open to independent scrutiny.

## References
- Adam Śpiewak, *On the convergence of the False Nearest Neighbours algorithm*, arXiv:2611.18087v1, posted 13 November 2026, https://arxiv.org/html/2611.18087v1.
- M. B. Kennel, R. Brown, H. D. I. Abarbanel, *Determining embedding dimension for phase-space reconstruction using a geometrical construction*, Physical Review A 45 (1992), 3403–3411, https://doi.org/10.1103/PhysRevA.45.3403.
- H. D. I. Abarbanel and M. B. Kennel, *Local false nearest neighbors and dynamical dimensions from observed chaotic data*, Physical Review E 47 (1993), 3057, https://doi.org/10.1103/PhysRevE.47.3057.
- *Use of False Nearest Neighbours for Selecting Variables and Embedding Parameters for State Space Reconstruction* (2015), https://doi.org/10.1155/2015/932750.
