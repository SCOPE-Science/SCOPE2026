# Rank-two compression lenses and the singleton phase of two weighted Jordan blocks

## Finding
For a complex \(4\times4\) matrix formed by the direct sum of two nontrivial \(2\times2\) Jordan blocks, the rank-two numerical range has a complete geometric classification. Write
\[
J_a(\alpha)=\begin{pmatrix}\alpha&a\\0&\alpha\end{pmatrix},\qquad
T=J_a(\alpha)\oplus J_b(\beta),\qquad r=a/2,\quad s=b/2,\quad d=|\beta-\alpha|.
\]
For every \(a,b>0\) and \(\alpha,\beta\in\mathbb C\),
\[
\boxed{\Lambda_2(T)=
\begin{cases}
\overline{B}(\alpha,r)\cap\overline{B}(\beta,s),&d\le r+s,\\[3pt]
\left\{\dfrac{s\alpha+r\beta}{r+s}\right\},&d>r+s.
\end{cases}}
\]
At \(d\le|r-s|\), the intersection is the smaller closed disk; at \(|r-s|<d<r+s\), it is a lens; at \(d=r+s\), the disks are externally tangent at a singleton. Above this threshold the same weighted barycenter remains the unique rank-two compression value, *even though the two disks become disjoint*.

There is a strong stability distinction: for fixed \(\alpha\ne\beta\), as the two positive off-diagonal weights tend to zero along any path with \(r/(r+s)\to t\in[0,1]\), the rank-two ranges tend to the singleton \(\{(1-t)\alpha+t\beta\}\). At the limiting normal matrix \(T_0=\alpha I_2\oplus\beta I_2\), the rank-two range is the entire segment \([\alpha,\beta]\). Thus every point on that segment can appear as a Hausdorff limit of ranges of nonnormal perturbations.

## Assumptions and scope
\(\Lambda_2(T)\) means the set of all \(z\in\mathbb C\) for which an isometry \(V:\mathbb C^2\to\mathbb C^4\) satisfies \(V^*TV=zI_2\). Both Jordan off-diagonal magnitudes are strictly positive; arbitrary nonzero complex off-diagonal coefficients reduce to this setting by blockwise diagonal unitary conjugation. The discs \(\overline B(w,t)\) are closed Euclidean discs. There are no restrictions on the complex centers. This is a finite-dimensional operator-theoretic result, not a statement about ordinary numerical range \(\Lambda_1\) or higher-rank ranges for larger blocks.

## Proof
Translation and rotation reduce to \(\alpha=0\), \(\beta=D\ge0\), without changing the radii; write \(R=r+s\). The Li–Sze half-plane characterization gives
\[
\Lambda_2(T)=\bigcap_{\theta\in[0,2\pi)}\left\{z:\operatorname{Re}(e^{-i\theta}z)\le\lambda_2(H_\theta)\right\},\quad H_\theta=\operatorname{Re}(e^{-i\theta}T),
\]
with eigenvalues counted in decreasing order. The eigenvalues of \(H_\theta\) are \(r,-r,D\cos\theta+s,D\cos\theta-s\). Sorting these four real numbers, and putting \(u=D\cos\theta\), gives the *exact* second-largest value
\[
\lambda_2(H_\theta)=h(u)=\begin{cases}
-r,&u<-R,\\
\min(r,u+s),&-R\le u\le R,\\
u-s,&u>R.
\end{cases}
\]
If \(D\le R\), only the middle expression is encountered. Intersecting the inequalities \(\operatorname{Re}(e^{-i\theta}z)\le r\) over all angles yields \(\overline B(0,r)\). Intersecting \(\operatorname{Re}(e^{-i\theta}(z-D))\le s\) yields \(\overline B(D,s)\). Their intersection is exactly \(\Lambda_2(T)\), including the tangency case.

If \(D>R\), set \(q=\sqrt{1-R^2/D^2}>0\). Select the two angles with \(\cos\theta=R/D\) and the two with \(\cos\theta=-R/D\); their sines are respectively \(\pm q\). Writing \(z=x+iy\), the four half-plane constraints imply
\[
\frac{R}{D}x+q|y|\le r,\qquad -\frac{R}{D}x+q|y|\le-r.
\]
Adding forces \(y=0\), and then both constraints force \(x=Dr/R\). Thus \(\Lambda_2(T)\subseteq\{Dr/R\}\).

For the reverse inclusion, set \(Q=\operatorname{diag}(1,-1)\) and define the block-column isometry
\[
V=\begin{pmatrix}\sqrt{s/R}I_2\\\sqrt{r/R}Q\end{pmatrix},\qquad V^*V=I_2.
\]
Since \(Q^*J_b(0)Q=-J_b(0)\) and \(sa=rb\), the off-diagonal parts cancel exactly:
\[
V^*TV=\frac{s}{R}J_a(0)+\frac{r}{R}Q^*(DI_2+J_b(0))Q=\frac{rD}{R}I_2.
\]
This isometry works for every \(D\); it particularly proves attainment of the singleton when \(D>R\). Undoing the translation and rotation yields \((s\alpha+r\beta)/R\), completing the full classification.

For the limiting claim, take fixed distinct centers and positive \(r,s\to0\). Eventually \(d>r+s\), so the classification gives exactly one barycenter \((1-t_n)\alpha+t_n\beta\), where \(t_n=r/(r+s)\). If \(t_n\to t\), the singleton converges to \((1-t)\alpha+t\beta\). Every \(t\in[0,1]\) is achievable by choosing positive \(r,s\) with the required ratio limit. For the normal matrix \(\alpha I_2\oplus\beta I_2\), the classical normal-matrix rank-two range formula (the intersection of convex hulls of triples of eigenvalues) yields exactly \([\alpha,\beta]\). Its Hausdorff distance to any one-point subset is positive for \(\alpha\ne\beta\).

## Verification
The self-contained `verify.py` checks the formula for the sorted second Hermitian eigenvalue, verifies complex-valued isometry and compression algebra, tests half-plane inequalities on sampled angles, and tests the limiting barycenter numerically for a parameter grid. It supplements, but cannot establish, the all-parameter statements proved above. Run `python3 verify.py` from the extracted package. No external dependencies are required.

## Relationship to prior work
The Li–Sze higher-rank half-plane theorem is the essential established input; no claim of new convexity or half-plane theory is made. Argerami–Mustafa (2019) give a complete classification for one Jordan block plus a scalar block, which does **not** contain the two-active-block family here, while Mustafa's 2019 thesis analyzes selected direct sums of multiple Jordan blocks with unequal eigenvalues (including a larger two-block example). The present result provides an explicit all-parameter weighted, two-active-block formula and its normal-limit behavior. Jiang (2026) proves a rigidity theorem for constant-width *ordinary* numerical ranges, a contemporaneous motivation for comparing fine geometry under other ranks; its theorem is not used. Direct consequences of Li–Sze, such as the intersection-of-half-planes characterization and normal limiting segment, are acknowledged background.

## Limitations
The result concerns two \(2\times2\) blocks and rank exactly two. It does not classify larger multiblock systems or ordinary numerical ranges. An exact earlier equivalent two-block formula might exist under matrix-compression or quantum-error-correction terminology, and published bibliographic searches do not establish global priority. The numerical program only tests finite samples; the infinite family is handled by the proof.

## References
1. C.-K. Li and N.-S. Sze, *Canonical forms, higher rank numerical ranges, totally isotropic subspaces, and matrix equations*, Proceedings of the American Mathematical Society **136** (2008), 3013–3023; preprint https://arxiv.org/abs/0706.1536.
2. M. Argerami and S. Mustafa, *Higher Rank Numerical Ranges of Jordan-Like Matrices*, https://arxiv.org/abs/1908.05692 (first public 2019).
3. S. Mustafa, *Higher Rank Numerical Ranges for Certain Non-Normal Matrices*, thesis (2019), https://www.academia.edu/99973650/Higher_Rank_Numerical_Ranges_For_Certain_Non_Normal_Matrices.
4. M. Jiang, *A proof of the constant-width numerical range conjecture*, https://arxiv.org/abs/2611.13461 (first public 2026-11-10).
