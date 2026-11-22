# Exact volume and exponential overlap cost of the cube's Thales-ball covering

## Finding

Let \(d\ge 1\) be an integer, let \(Q_d=[-1,1]^d\), and for each vertex \(v\in\{-1,1\}^d\) let \(D_v\) be the closed Euclidean ball having \([0,v]\) as diameter. Put \(T_d=\bigcup_vD_v\), and let \(U_d=\operatorname{vol}_d(T_d)\). Then

\[
T_d=\{x\in\mathbb R^d:\|x\|_2^2\le\|x\|_1\},\qquad Q_d\subseteq T_d.
\]

For the entire function \(F(t)=e^{t^2/2}\bigl(1+\operatorname{erf}(t/\sqrt2)\bigr)\), its volume has the **exact, all-dimensional coefficient formula**

\[
\boxed{U_d=2(\pi/2)^{d/2}\,[t^d]F(t)^d.}
\]

The coefficient is a finite explicit sum: if \(c_k=2^{k/2}\Gamma((k+1)/2)/(\sqrt\pi\,k!)\), then \([t^d]F(t)^d=\sum_{k_1+\dots+k_d=d}\prod_{j=1}^dc_{k_j}\). In particular \(U_1=2\), \(U_2=2+\pi\), \(U_3=2+4\pi\), and \(U_4=2+10\pi+\pi^2\).

Let \(\varphi\) and \(\Phi\) be the standard normal density and distribution function. There is a unique \(\tau>0\) satisfying

\[
\tau^2+\tau\frac{\varphi(\tau)}{\Phi(\tau)}=1.
\]

Put \(r=\varphi(\tau)/\Phi(\tau)\),
\[
\beta=\tau\bigl(2\tau+r-\tau r(\tau+r)\bigr)>0,\qquad
\Lambda=\sqrt{\pi/8}\,\frac{F(\tau)}{\tau}>1.
\]

Then the **sharp dimension-asymptotic covering-volume overhead** is

\[
\boxed{
\frac{U_d}{\operatorname{vol}_d(Q_d)}
=\frac{2\Lambda^d}{\sqrt{2\pi\beta d}}\left(1+O(d^{-1})\right)
\quad(d\to\infty).
}
\]

Numerically \(\tau=0.839923675692331\ldots\), \(\beta=1.41094356197705\ldots\), and \(\Lambda=1.69763020222053\ldots\). Hence this canonical full-covering by \(2^d\) equal balls incurs an **exponentially growing extra ambient volume**, despite containing the cube exactly as a subset. The constant \(\Lambda\) is the limiting \(d\)-th root of that overhead, not a bound over all possible ball coverings.

## Assumptions and scope

All distances and volumes are Euclidean. Every ball \(D_v\) has center \(v/2\) and radius \(\sqrt d/2\). The ball union is considered in all of \(\mathbb R^d\), **not clipped to the cube**. Both the ball count and radius are fixed by the cube-vertex diameter construction. The result makes no assertion that this is an optimal-ball-number, optimal-radius, or minimum-union-volume covering among arbitrary arrangements. The coefficient notation means the coefficient in the Maclaurin expansion of the given entire function; no formal-analytic continuation is needed. The \(O(d^{-1})\) constant is absolute.

## Proof

**1. Exact union and covering.** For arbitrary \(x\in\mathbb R^d\), the diameter-ball condition is
\[
\|x-v/2\|_2^2\le d/4\quad\Longleftrightarrow\quad\|x\|_2^2\le x\cdot v.
\]
Taking the union over all signs \(v\in\{-1,1\}^d\) replaces \(x\cdot v\) by \(\max_v x\cdot v=\sum_{i=1}^d|x_i|\), proving the asserted set identity. If \(x\in[-1,1]^d\), coordinatewise \(x_i^2\le|x_i|\), so \(Q_d\subseteq T_d\). The boundary is radial from the origin: for a unit vector \(u\), the largest \(s\ge0\) with \(su\in T_d\) is \(\rho_d(u)=\|u\|_1\).

**2. Radial integral.** Spherical polar integration gives
\[
U_d=\frac1d\int_{S^{d-1}}\|u\|_1^d\,dS(u)
=\kappa_d\,\mathbb E\|\Theta\|_1^d,
\]
where \(\Theta\) is uniform on the Euclidean unit sphere and \(\kappa_d=\pi^{d/2}/\Gamma(d/2+1)\). This remains valid for \(d=1\) with counting measure on its two-point sphere.

**3. Exact coefficient.** Let \(G=(G_1,\ldots,G_d)\) have independent standard normal coordinates and write \(G=R\Theta\). Its direction \(\Theta\) is uniform on the unit sphere and independent of \(R\). Direct gamma integration gives
\[
\mathbb E R^d=2^{d/2}\frac{\Gamma(d)}{\Gamma(d/2)}.
\]
Thus
\[
U_d=\frac{2(\pi/2)^{d/2}}{\Gamma(d+1)}
\,\mathbb E\bigl(\sum_{j=1}^d|G_j|\bigr)^d.
\]
A half-normal variable \(H=|G_1|\) has moment-generating function
\[
F(t)=\mathbb E e^{tH}=2e^{t^2/2}\Phi(t)
=e^{t^2/2}(1+\operatorname{erf}(t/\sqrt2)),
\]
which is entire. Independence and coefficient extraction yield
\(\mathbb E(\sum_j|G_j|)^d=d!\,[t^d]F(t)^d\). Substituting \(\Gamma(d+1)=d!\) proves the exact formula. Expansion into the positive half-normal moments yields the stated finite sum. For low dimensions the coefficients simplify to the four displayed exact values.

**4. Unique saddle and its variance.** Write \(F(t)=\sum_{k\ge0}c_kt^k\) with \(c_k=\mathbb E H^k/k!>0\). For every \(t>0\), define an integer-valued variable \(N_t\) by \(\mathbb P(N_t=k)=c_kt^k/F(t)\). Then
\[
\mu(t)=\mathbb EN_t=tF'(t)/F(t),\qquad
\operatorname{Var}(N_t)=t\mu'(t)>0.
\]
The strict positivity holds because \(N_t\) assigns positive mass to at least two integers. Thus \(\mu\) is strictly increasing. It tends to zero as \(t\downarrow0\), and, using \(F'/F=t+\varphi(t)/\Phi(t)\), it tends to infinity as \(t\to\infty\). Consequently there is exactly one \(\tau>0\) with \(\mu(\tau)=1\), equivalent to the stated normal-function equation. Differentiating \(\varphi/\Phi\), whose derivative is \(-r(t)(t+r(t))\), gives \(\operatorname{Var}(N_\tau)=\beta\) with the displayed expression, so \(\beta>0\) intrinsically.

**5. Coefficient asymptotic (including prefactor).** Let \(N_1,\ldots,N_d\) be independent copies of \(N_\tau\). They have mean \(1\), variance \(\beta>0\), exponential moments of all orders, and lattice span one since their probabilities are positive at every nonnegative integer. Exact convolution therefore gives
\[
\mathbb P\{N_1+\cdots+N_d=d\}
=\frac{\tau^d}{F(\tau)^d}[t^d]F(t)^d.
\]
The standard lattice local central limit theorem, with its first local Edgeworth correction at the mean (the order-\(d^{-1/2}\) skewness term vanishes at centered argument zero), gives
\[
\mathbb P\{\textstyle\sum N_j=d\}
=\frac{1}{\sqrt{2\pi\beta d}}(1+O(d^{-1})).
\]
For completeness, Fourier inversion supplies the needed error: on any arc away from angle zero, the characteristic function has absolute value strictly below one, uniformly on compact arcs, by span one. On a small arc its logarithm has a convergent cumulant expansion; rescale the angle by \(d^{-1/2}\). The cubic term is odd and its integral on the symmetric arc vanishes; the first surviving correction is of relative order \(d^{-1}\), and the remaining terms and tails are controlled by the exponential moment. Substitution into the exact coefficient formula gives
\[
U_d=\frac{2(\pi/2)^{d/2}}{\sqrt{2\pi\beta d}}
\left(\frac{F(\tau)}{\tau}\right)^d(1+O(d^{-1})).
\]
Because \(\operatorname{vol}_d Q_d=2^d\), division produces the claimed \(\Lambda=\sqrt{\pi/8}F(\tau)/\tau\). Numerical evaluation by monotone bisection on \(\mu(t)=1\) gives the quoted values, in particular \(\Lambda>1\). This completes the proof.

## Verification

Run the bundled `verify_thales_volume.py` with Python 3. The script independently computes coefficients from exact half-normal moments for selected dimensions up to \(64\), checks the low-dimensional closed forms, solves the monotone saddle equation numerically, checks finite-dimensional approach to its leading asymptotic, and cross-checks the geometric radial volume by deterministic numerical quadrature in dimension two and seeded Monte Carlo on the Euclidean two-sphere. The program is a corroborating finite experiment, **not** a proof of the coefficient or asymptotic theorem. The proof above is analytic and does not depend on its output.

## Relationship to prior work

Pavlík's November 2026 Thales covering theorem guarantees that all vertex-to-point diameter balls cover any polytope, and his power-diagram refinement gives a tiling within that polytope. Our Step 1 specializes his construction to the cube, but the exact **ambient union volume** and the sharp exponential high-dimensional excess are different numerical and asymptotic invariants not supplied by that covering theorem. Work of Zhigljavsky and Noonan studies the **fraction of a high-dimensional cube covered** by balls with other placement strategies, whereas the present union already covers the entire cube and asks for the total volume of the union *outside as well as inside* the cube. Planar overlap/multiplicity studies for regular polygons and finite regular simplices do not imply this all-dimensional cubical volume law. The Gaussian moment and lattice-coefficient techniques used here are classical; their application to this specific high-dimensional Thales covering is the assessed contribution. No assertion of independently certified historical priority is made.

## Limitations

The ambient union volume is not a measure of optimality among all equal-ball coverings; it is only an exact sharp formula for this natural fixed construction. The asymptotic concerns dimensions tending to infinity, with one specific ball family per dimension; it does not describe fixed-dimensional perturbations of ball centers. Numerical constants are rounded, but all defining equations are exact. The search for prior equivalents is necessarily non-exhaustive, and an older exact union-of-cube-corner-balls theorem could supersede the claimed novelty. Independent external validation has not been performed.

## References

1. J. Pavlík, *Thales's theorem in higher dimensions*, arXiv:2611.14277v1, publicly submitted 10 November 2026, https://arxiv.org/abs/2611.14277. Relevant primary material: Section 5, Theorem 5.1 and Corollary 5.3 (covering and power diagram).
2. A. Zhigljavsky and J. Noonan, *Covering of High-Dimensional Cubes and Quantization*, Operations Research Forum **1**, article 18 (2020), https://doi.org/10.1007/s43069-020-0015-8. Relevant primary material: Sections 1–3 (intersection-volume fraction and covering schemes).
3. Standard Gaussian polar decomposition, half-normal moments, and lattice local central limit/Edgeworth expansions (used in the proof with explicit hypotheses).
