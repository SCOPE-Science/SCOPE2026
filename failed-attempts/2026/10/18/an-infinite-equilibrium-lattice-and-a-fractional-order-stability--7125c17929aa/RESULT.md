# An infinite equilibrium lattice and a fractional-order stability staircase in a sinusoidal map

## Finding

Consider the commensurate Caputo-like fractional discrete system described below with real state variables, positive parameter \(c\), and common order \(0<\nu\le1\). Its stationary solutions on the entire real plane admit a complete enumeration. When \(c>1\), besides the origin there are countably infinitely many equilibria, not merely the principal symmetry pair. Their positive Jacobian determinants, **each with multiplicity two**, are exactly

\[
d_j(c)=2\pi\sqrt{c-1}\bigl(j+\tau(c)\bigr),\quad j=0,1,\ldots,
\qquad\tau(c)=\pi^{-1}\arcsin\sqrt{1-c^{-1}}.
\]

For every \(0<\nu\le1\), define \(D_\nu>1/4\) as the unique solution of

\[
\sqrt{D_\nu}=
\left[2\cos\!\left(\frac{\arccos[-1/(2\sqrt{D_\nu})]-\pi}{2-\nu}\right)\right]^\nu.
\]

A nonzero equilibrium is **linearly asymptotically stable for the fractional variational equation if and only if** its Jacobian determinant lies strictly between \(0\) and \(D_\nu\). This statement includes every boundary case: determinant \(D_\nu\) is not asymptotically stable, and all equilibria with negative determinant are linearly unstable. Therefore the **exact number** of linearly asymptotically stable nonzero equilibria is

\[
\boxed{N_\nu(c)=2\max\!\left\{0,\left\lceil
\frac{D_\nu}{2\pi\sqrt{c-1}}-\tau(c)
\right\rceil\right\},\qquad c>1.}
\]

In particular, for fixed \(\nu\),

\[
N_\nu(c)=\frac{D_\nu}{\pi\sqrt{c-1}}+O_\nu(1)
\quad(c\downarrow1).
\]

The integer-order threshold equals \(D_1=1\). Every genuinely fractional order \(0<\nu<1\) has \(D_\nu>1\), so fractional memory strictly enlarges the range of positive determinants having linearly stable equilibria. For each \(j\ge0\), the equation \(d_j(c)=D_\nu\) defines exactly one threshold \(c_{\nu,j}>1\). These thresholds accumulate at \(1\), with \(c_{\nu,j}=1+D_\nu^2/(4\pi^2j^2)+O_\nu(j^{-4})\) as \(j\to\infty\).

## Assumptions and scope

Put \(G_c(x,y)=(\sin(\pi y)-x,\,[c(1-x^2)-1]y)\). The system is the Caputo-like delta recurrence with initial \((x_0,y_0)\in\mathbb R^2\), equivalently

\[
Z_n=Z_0+\sum_{m=1}^{n}\frac{\Gamma(n-m+\nu)}{\Gamma(\nu)\Gamma(n-m+1)}G_c(Z_{m-1}),\qquad n\ge1.
\]

Here \(0<\nu\le1\), \(c>0\), and *equilibrium* means a constant sequence \(Z_n=Z_*\), or equivalently \(G_c(Z_*)=0\). *Linearly asymptotically stable* means that every initial perturbation of the constant-coefficient fractional variational recurrence \(G_c(Z_*+u)=DG_c(Z_*)u+O(\|u\|^2)\) has its linear solution tending to zero. It does **not** by itself assert nonlinear local attraction of the fractional recurrence. At \(\nu=1\), the original memoryless map is \(Z_{n+1}=Z_n+G_c(Z_n)\), and the linearly stable equilibria are hyperbolic attracting fixed points of this map.

For \(0<c<1\), the origin is the only equilibrium and is linearly asymptotically stable. At \(c=1\), all points \((0,k)\), \(k\in\mathbb Z\), are equilibria, each with a zero Jacobian eigenvalue and therefore not linearly asymptotically stable. For \(c>1\), the origin has a positive Jacobian eigenvalue and is linearly unstable.

## Proof

**All equilibria.** From \(G_c(x,y)=0\), either \(y=0\), hence \(x=0\), or \(c(1-x^2)=1\). The second possibility is real only for \(c\ge1\). At \(c=1\), \(x=0\) and \(\sin(\pi y)=0\), yielding \(y\in\mathbb Z\). For \(c>1\) write \(s=\sqrt{1-c^{-1}}\), \(\tau=\arcsin(s)/\pi\). The complete nonzero list consists of the two families of ordinates \(y=2k+\tau\) and \(y=2k+1-\tau\) at \(x=s\), and \(y=2k-\tau\) and \(y=2k+1+\tau\) at \(x=-s\), for every \(k\in\mathbb Z\). Substituting directly checks every member; periodicity of sine makes the list exhaustive.

**Determinants and their multiplicity.** On every nonzero equilibrium the Jacobian is

\[
M(x,y)=\begin{pmatrix}-1&\pi\cos(\pi y)\\-2cxy&0\end{pmatrix},\qquad
\operatorname{tr}M=-1,\qquad d=\det M=2\pi cxy\cos(\pi y).
\]

Because \(cs\cos(\pi\tau)=\sqrt{c-1}\), direct substitution into the four complete ordinate branches shows that exactly two equilibria have determinant \(d_j(c)>0\) for each integer \(j\ge0\), and all other nonzero equilibria have negative determinant. In particular no nonzero determinant vanishes. The characteristic polynomial is \(\lambda^2+\lambda+d\).

**Sharp spectral criterion.** For scalar eigenvalue \(\lambda\), the linear variational recurrence has generating function

\[
\sum_{n\ge0}u_nz^n
=u_0\frac{(1-z)^{\nu-1}}{(1-z)^\nu-z\lambda}.
\]

The standard fractional-difference stability region is described by \(|\arg\lambda|>\nu\pi/2\) and
\[
|\lambda|<\left[2\cos\!\left(\frac{|\arg\lambda|-\pi}{2-\nu}\right)\right]^\nu.
\]

For clarity, necessity as well as sufficiency follows here by the generating-function denominator. Its unit-circle spectral boundary is parametrized by \(\lambda=(1-e^{it})^\nu e^{-it}\), \(0<t<2\pi\). This curve has argument \(-\nu\pi/2-(1-\nu/2)t\) and modulus \([2\sin(t/2)]^\nu\). Each non-boundary radial direction intersects it once in the relevant sector; moving a spectral eigenvalue outward across it places a zero of the denominator strictly inside the unit disk, causing a nondecaying solution. On the boundary a noncancelled unit-circle pole precludes asymptotic decay. The stable side is fixed by small negative eigenvalues, which have decaying scalar solutions. The result also follows from the established sharp linear fractional-difference spectral criterion cited below. Double negative eigenvalues do not alter decay, since the associated matrix resolvent has the same algebraically decaying singularity at \(z=1\).

For \(d<0\), the polynomial \(\lambda^2+\lambda+d\) has a positive real root, so the equilibrium is unstable. For \(0<d\le1/4\), both eigenvalues are negative and lie strictly between \(-1\) and \(0\), so they are stable for all allowed orders. For \(d>1/4\), the roots are \(-1/2\pm i\sqrt{d-1/4}\), with modulus \(\sqrt d\) and absolute argument \(\theta(d)=\arccos[-1/(2\sqrt d)]\). The modulus \(\sqrt d\) increases strictly, whereas \([2\cos((\theta(d)-\pi)/(2-\nu))]^\nu\) decreases strictly on \(d>1/4\). Their comparison starts strictly in the stable region at \(d=1/4\) and eventually fails as \(d\to\infty\), so the unique crossing defines \(D_\nu\) and gives stability exactly for \(0<d<D_\nu\). At \(\nu=1\), substitution gives \(D_1=1\). At \(d=1\), \(\theta=2\pi/3\) and, for \(0<\nu<1\), the right side is \([2\cos(\pi/[3(2-\nu)])]^\nu>1\), proving \(D_\nu>1\).

**Counting and critical accumulation.** The integer indices satisfying \(d_j(c)<D_\nu\) are precisely \(0\le j<D_\nu/(2\pi\sqrt{c-1})-\tau(c)\). Counting these, including strict integer boundary cases, yields the stated ceiling formula and the factor two. The expansion \(\tau(c)=\pi^{-1}\sqrt{c-1}+O((c-1)^{3/2})\) establishes the stated divergent counting law. For fixed \(j\), \(d_j(c)\) is strictly increasing from zero to infinity as \(c\) ranges from \(1\) to infinity. Thus each level crosses \(D_\nu\) once. The level equation gives \(\sqrt{c_{\nu,j}-1}=D_\nu/[2\pi(j+\tau(c_{\nu,j}))]\); substituting \(\tau(c)=O(\sqrt{c-1})\) gives the quoted \(j^{-2}\) law and \(O(j^{-4})\) remainder.

## Verification

The standalone standard-library program `CHECK.py` enumerates all branches in large finite ordinate windows, checks the equilibrium identities, computes Jacobian determinants and their paired level indices, independently applies the quoted spectral inequality to each computed eigenvalue, and compares the observed finite count with the ceiling formula for multiple values of \(c\) and \(\nu\). It also checks the determinant-level formula at high indices. The finite test is **not** a proof of the infinite classifications, threshold uniqueness, or asymptotic formulas; those assertions are proved above.

## Relationship to prior work

Liu, Tang, and Hong (2022), especially Sections 2–3.2 and equations (7)–(14), introduce this fractional recurrence and analyze the principal symmetry pair of equilibria. Their spectral stability condition is established general linear theory, not claimed new here. The present result addresses the *whole unbounded real phase plane*, gives the complete branch lattice, a sharp and order-dependent global **linearized** equilibrium count, and a near-threshold staircase. The earlier integer-order paper by Chuang and collaborators (2013) introduces the underlying sine map; its full paper could not be materially inspected here, so precedence for any integer-order substatement remains uncertain. Other linear fractional stability theorems furnish the generic spectral criterion but do not, by themselves, enumerate this model's real equilibria or evaluate their determinant levels.

## Limitations

The count refers to linearly asymptotically stable equilibria of the fractional **variational equation**, not a theorem that every counted equilibrium attracts nearby nonlinear fractional trajectories. The result says nothing about sizes of nonlinear basins, global boundedness, chaos, or how frequently trajectories visit high-index equilibria. The real plane is essential: a phase-space restriction such as \(|y|\le1\) would remove most of the counted equilibria. Existing general fractional stability theory supplies the scalar criterion; the contribution is the exhaustive model-specific lattice, exact determinant reduction, counting formula and its infinite staircase. Priority uncertainty remains for equivalent calculations in literature not accessible in full.

## References

1. Xiaojun Liu, Dafeng Tang, Ling Hong, *A Fractional-Order Sinusoidal Discrete Map*, Entropy **24** (2022), 320; first online publication 23 February 2022. https://doi.org/10.3390/e24030320 (full open-access article inspected, including Sections 2, 3 and Discussion).
2. Bi Chuang, Zhang Qian, Xiang Yong, Wang Jing-Mei, *Bifurcation and attractor of two-dimensional sinusoidal discrete map*, Acta Physica Sinica **62** (2013), 240503. https://doi.org/10.7498/aps.62.240503 (bibliographic record and abstract inspected; full article not accessible in this examination).
3. Jan Čermák, István Győri, Luděk Nechvátal, *On explicit stability conditions for a linear fractional difference system*, Fractional Calculus and Applied Analysis **18** (2015); https://doi.org/10.1515/fca-2015-0040 (general linear stability result, also quoted as Theorem 1 in reference 1).
