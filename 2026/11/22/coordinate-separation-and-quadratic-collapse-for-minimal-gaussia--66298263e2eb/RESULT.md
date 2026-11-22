# Coordinate separation and quadratic collapse for minimal Gaussian multiwindow Gabor frames

## Finding
Fix an integer \(d\geq1\) and positive widths \(\beta_1,\ldots,\beta_d\). Put \(g_\beta(t)=\exp(-\sum_{i=1}^{d}\beta_i t_i^2)\), and, for \(d+1\) translation vectors \(a_0,\ldots,a_d\in\mathbb R^d\), form the multiwindow Gabor system
\[
\mathcal G_\beta(a)=\{e^{2\pi i n\cdot t}g_\beta(t-m-a_j):m,n\in\mathbb Z^d,\ 0\leq j\leq d\}.
\]
It is a frame for \(L^2(\mathbb R^d)\) **if and only if**, for each coordinate \(1\leq i\leq d\), the \(d+1\) residues \(a_{0,i},\ldots,a_{d,i}\pmod1\) are pairwise distinct. This gives explicit Schwartz-window frames with the sharp minimum \(d+1\) windows, for example \(a_j=(j/(d+1),\ldots,j/(d+1))\).

For positive coordinate separations
\[
\rho_i=\min_{j<k}\operatorname{dist}_{\mathbb R/\mathbb Z}(a_{j,i},a_{k,i}),\quad q_i=e^{-\beta_i},
\]
define
\[
P(q)=\prod_{n=1}^{\infty}(1-q^{2n})(1-q^{2n-1})^2,\quad
L_i=q_iP(q_i)(1-q_i^{\rho_i}),\quad
U_i=2+2\sum_{n=1}^{\infty}q_i^{n^2}.
\]
The Gabor frame has valid completely explicit bounds
\[
\boxed{\prod_{i=1}^{d}L_i^2\ \leq\ A_\mathrm{opt}\leq B_\mathrm{opt}\ \leq(d+1)\prod_{i=1}^{d}U_i^2.}
\]
Here \(A_\mathrm{opt}\) and \(B_\mathrm{opt}\) denote the optimal lower and upper frame bounds for the **unnormalized** Gaussian windows as displayed.

The frame boundary also has a sharp quantitative law. In dimension two, take \(\beta_1=\beta_2=\beta>0\), and the three centers
\[
a_0=(0,0),\quad a_1=(\varepsilon,1/3),\quad a_2=(1/3,2/3),\qquad0<\varepsilon<1/3.
\]
Let \(A_\beta(\varepsilon)\) be their optimal lower frame bound. Define
\[
z_\beta(x,\omega)=\sum_{k\in\mathbb Z}e^{-\beta(x+k)^2}e^{-2\pi i k\omega},\qquad
\ell_\beta=z_\beta(1/6,1/2),\qquad D_\beta=\partial_xz_\beta(1/2,1/2).
\]
Then \(\ell_\beta>0\), \(D_\beta<0\), and
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{A_\beta(\varepsilon)}{\varepsilon^2}
=\frac12\ell_\beta^2D_\beta^2>0.}
\]
The derivative has the explicit, convergent product
\[
D_\beta=-2\beta e^{-\beta/4}\prod_{n=1}^{\infty}(1-e^{-2\beta n})^3.
\]
Thus the best lower frame bound collapses quadratically, with a sharp shape-dependent coefficient, at a precisely classified collision of two coordinate residues.

## Assumptions and scope
All coordinates, translations, frequencies and displacements are real. There are exactly \(d+1\) windows, each a **single** translate of the same positive coordinate-product Gaussian, all modulated and translated by the full integer lattice \(\mathbb Z^d\times\mathbb Z^d\). The \(d=2\) collision statement uses only the displayed one-parameter family and a fixed \(\beta>0\); no claim is made about other kinds of lattice or window perturbation. \(\operatorname{dist}_{\mathbb R/\mathbb Z}\) is the shortest circular distance modulo integers. The bounds are nonoptimal except that the collision coefficient is optimal.

## Proof
**1. Zak reduction and a unique one-dimensional zero.** The (unitary-normalized) integer Zak transform is
\[
Zf(x,\omega)=\sum_{k\in\mathbb Z^d}f(x+k)e^{-2\pi i k\cdot\omega}.
\]
On \([0,1]^{2d}\), the integer-lattice Gabor frame operator is multiplication by
\[
M_a(x,\omega)=\sum_{j=0}^{d}\left|Zg_\beta(x-a_j,\omega)\right|^2.
\]
This follows by Parseval in the two integer indices, first for Schwartz functions and then by density; therefore \(A_\mathrm{opt}=\min M_a\) and \(B_\mathrm{opt}=\max M_a\). Continuity and quasi-periodicity make these extrema attainable. Tensor factorization gives \(Zg_\beta(x,\omega)=\prod_i z_{\beta_i}(x_i,\omega_i)\).

For \(q=e^{-\beta}\), \(0\leq x<1\), and \(v=q^{2x}e^{-2\pi i\omega}\), Jacobi's absolutely convergent triple product gives
\[
z_\beta(x,\omega)=e^{-\beta x^2}\prod_{n=1}^{\infty}
(1-q^{2n})(1+q^{2n-1}v)(1+q^{2n-1}/v).
\]
The second factor of each parenthesis is never zero since \(|q^{2n-1}v|<1\). The third vanishes only when \(q^{2n-1-2x}=1\) and \(e^{2\pi i\omega}=-1\); inside the fundamental cell this means \(n=1\), \(x=1/2\), \(\omega=1/2\). Consequently \(z_\beta\) has precisely one zero modulo its quasi-periods, and it is simple in both independent real directions. Differentiating the vanishing factor gives
\[
\partial_x z_\beta(1/2,1/2)=-2\beta e^{-\beta/4}\prod_{n\geq1}(1-q^{2n})^3\in\mathbb R_{<0},
\quad\partial_\omega z_\beta(1/2,1/2)=\frac{\pi i}{\beta}\partial_x z_\beta(1/2,1/2)\in i\mathbb R_{<0}.
\]
At \((1/6,1/2)\) every product factor is strictly positive, establishing \(\ell_\beta>0\).

**2. Exact coordinate-cover criterion.** For a given \(j\), its Zak product vanishes precisely when some coordinate \(i\) obeys both \(\omega_i=1/2\pmod1\) and \(x_i=a_{j,i}+1/2\pmod1\). If every coordinate has pairwise distinct residues among the \(d+1\) centers, any fixed coordinate can kill at most one window. Since there are only \(d\) coordinates, no \((x,\omega)\) can kill all \(d+1\) products; compactness then gives a positive lower bound.

Conversely, suppose \(a_{j,i}=a_{k,i}\pmod1\) for distinct windows \(j,k\) in coordinate \(i\). Choose \(\omega_i=1/2\) and \(x_i=a_{j,i}+1/2\); this kills both windows. Assign the remaining \(d-1\) windows bijectively to the remaining \(d-1\) coordinates and set each corresponding \((x_h,\omega_h)=(a_{j(h),h}+1/2,1/2)\pmod1\). Every window has a zero factor, so \(M_a=0\) and the system is not a frame. For \(r\leq d\) windows, assigning one window per distinct coordinate similarly proves nonexistence for *any* translations of the same Gaussian; this establishes sharpness of the minimal window count within this family.

**3. Quantitative bounds.** When \(\operatorname{dist}_{\mathbb R/\mathbb Z}(x- a_{j,i},1/2)\geq\rho_i/2\), the preceding product, with the \(n=1\) factor \(1+q_i^{1-2x}e^{2\pi i\omega}\) isolated, yields
\[
|z_{\beta_i}(x-a_{j,i},\omega_i)|\geq q_iP(q_i)(1-q_i^{\rho_i})=L_i.
\]
Indeed, the isolated factor has modulus at least \(1-q_i^{\rho_i}\) on either side of the zero, all other factors are bounded below by the factors defining \(P(q_i)\), and \(e^{-\beta_i x^2}\geq q_i\). By coordinate separation, fewer than two windows can lie in the *open* danger arc of radius \(\rho_i/2\) in any one coordinate. The union of these \(d\) danger sets excludes at most \(d\) windows, hence there is a window whose every factor is at least \(L_i\). This proves \(M_a\geq\prod_i L_i^2\). Finally \(|z_\beta(x,\omega)|\leq\sum_{k\in\mathbb Z}e^{-\beta(x+k)^2}\leq 2+2\sum_{n\geq1}e^{-\beta n^2}\), giving the upper bound.

**4. Sharp quadratic collision.** Put \(\varepsilon=0\) for the special planar family. By the coordinate-cover characterization, its unique common Zak zero modulo the unit four-torus is
\[
p=(x_1,x_2,\omega_1,\omega_2)=(1/2,1/6,1/2,1/2).
\]
Uniqueness follows because the two coincident first-coordinate residues can kill only windows 0 and 1, while the second-coordinate residue for window 2 is the only remaining possibility. Let local real coordinates near \(p\) be \((u,s,v,t)\), in the order \((x_1-1/2,x_2-1/6,\omega_1-1/2,\omega_2-1/2)\). Write \(D=D_\beta\), \(H=\partial_\omega z_\beta(1/2,1/2)=\pi iD/\beta\) and \(\ell=\ell_\beta\). Quasiperiodicity, evenness of the Gaussian and the preceding derivatives give the first-order expansion
\[
M_\varepsilon(p+(u,s,v,t))=\ell^2\bigl(|Du+Hv|^2+|D(u-\varepsilon)+Hv|^2+|Ds+Ht|^2\bigr)
+o\bigl((|u|+|s|+|v|+|t|+\varepsilon)^2\bigr).
\]
The displayed quadratic form is coercive in the four local variables: \(D\) is nonzero real and \(H\) nonzero purely imaginary. Its minimum is exactly \(\ell^2D^2\varepsilon^2/2\), attained at \(u=\varepsilon/2\) and \(s=v=t=0\). For small \(\varepsilon\), the global minimizers of \(M_\varepsilon\) must lie near \(p\): otherwise a compactness subsequence would give a different zero of \(M_0\). The coercive Taylor expansion and the displayed trial point then force their distances from \(p\) to be \(O(\varepsilon)\), and division by \(\varepsilon^2\) gives the asserted sharp limit.

## Verification
The attached standard-library script `verify_gaussian.py` evaluates the rapidly convergent Zak series and its exact derivative series for several widths and small collision parameters; it checks the predicted quadratic coefficient numerically and exercises the coordinate-residue classification on finite examples. These diagnostics do not establish the infinite-product zero lemma, the all-dimensional classification, or the global minimization; those are proven above. To reproduce: `python3 verify_gaussian.py` from a directory containing the script. No external packages, data or network access are needed.

## Relationship to prior work
De Dios Pont–Liehr–Taylor (2026) establish the general \(rN>d\) existence obstruction and construct Schwartz Parseval multiwindow frames for suitable rational lattices. Caragea–Pfander (2026) provide a broader minimal-window existence classification and describe constructions using finite combinations of shifted Gaussians. Neither of these implications classifies when a **prescribed set of exactly \(d+1\) single Gaussian translates** works on the integer lattice; the present criterion identifies every bad coordinate coincidence and provides explicit computable bounds and a sharp degeneracy coefficient. Luef–Testorf–Wang (2024) study Gaussian and Hermite Gabor frame criteria for different geometric and lattice configurations. Classical Gaussian Zak-zero and Zak-fiber facts are used as context; the Gaussian-zero claim is reconstructed directly here from the triple product. This work makes no priority claim beyond the inspected literature; equivalent older designs may exist.

## Limitations
Only integer critical-lattice shifts, pure time-translated tensor Gaussians, and the stated planar one-parameter collision are covered. The explicit general lower bound is conservative and not an optimizer formula. The quadratic coefficient is asymptotic as \(\varepsilon\to0^+\), not an exact finite-\(\varepsilon\) expression. The literature comparison is limited to the sources stated and the accessible indexed evidence; an unknown earlier Gaussian multiwindow construction could affect originality. There has been no independent mathematical audit.

## References
- J. de Dios Pont, L. Liehr and M. A. Taylor, *On the existence problem of regular Gabor frames*, arXiv:2606.26052, first posted 2026-06-24, https://arxiv.org/abs/2606.26052 .
- A. Caragea and G. Pfander, *Schwartz-Class Gabor Windows and the Balian-Low Classification*, arXiv:2609.06255, first posted 2026-09-05, https://arxiv.org/abs/2609.06255 .
- F. Luef, J. Testorf and X. Wang, *On the transcendentality condition for Gaussian Gabor frames and Hermite super/multiwindow frames*, arXiv:2405.08415, first posted 2024-05-14, https://arxiv.org/abs/2405.08415 .
- A. J. E. M. Janssen, *On generating tight Gabor frames at critical density*, work documenting the single Gaussian Zak zero, https://research.tue.nl/en/publications/on-generating-tight-gabor-frames-at-critical-density/ .
