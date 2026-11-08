# Three-regime face-vector fluctuations of vertex-shifted regular-simplex sections

## Finding

Let \(n\ge2\), put \(N=n+1\), and consider the regular \(n\)-simplex
\[
S_n=\operatorname{conv}\{e_i-\mathbf{1}/N:0\le i\le n\}
\subset H_n=\{x\in\mathbb R^{N}:\sum_{i=0}^n x_i=0\}.
\]
For \(0\le h_n<1\), choose a Haar-uniform, unoriented hyperplane normal in \(H_n\), independently for each dimension, and intersect the simplex with the hyperplane through \(h_n(e_0-\mathbf{1}/N)\). Write \(f_{n,j}\) for the number of \(j\)-faces of the section, \(0\le j\le n-2\), and \(V_n=f_{n,0}\). Binomial coefficients with upper argument less than lower argument are zero.

**Exact finite-dimensional law.** Let \(G_0,\ldots,G_n\) be independent standard Gaussians, \(\bar G=N^{-1}\sum_{i=0}^nG_i\), and define
\[
K_n=\#\{0\le i\le n:G_i-\bar G>h_n(G_0-\bar G)\}.
\]
The entire face vector is equal in distribution to
\[
\boxed{f_{n,j}=\binom N{j+2}-\binom{K_n}{j+2}-\binom{N-K_n}{j+2},\quad 0\le j\le n-2.}\tag{1}
\]
In particular, \(V_n=K_n(N-K_n)\) and
\[
\boxed{N^2/4-V_n=(K_n-N/2)^2.}\tag{2}
\]

**Critical displacement.** Suppose \(\sqrt n\,h_n\to c\in[0,\infty)\). Put \(\sigma_c^2=1/4+(c^2-1)/(2\pi)\). For any fixed finite set of ranks \(j\ge0\), define
\[
B_{n,j}=\binom N{j+2}-\binom{\lfloor N/2\rfloor}{j+2}
-\binom{\lceil N/2\rceil}{j+2}.
\]
Then, jointly across these ranks,
\[
\boxed{\left(\frac{B_{n,j}-f_{n,j}}{n^{j+1}}\right)_j
\Longrightarrow\left(\frac{\sigma_c^2}{2^j j!}Z^2\right)_j,\quad Z\sim N(0,1).}\tag{3}
\]
For vertices, equivalently, \((N^2/4-V_n)/n\Rightarrow\sigma_c^2 Z^2\). The case \(c=0\) is the previously known central regime; the nonzero \(c\) law gives a continuous displacement crossover.

**Mesoscopic displacement.** If \(h_n\to0\) and \(\sqrt n\,h_n\to\infty\), then, jointly for all fixed finite collections of ranks,
\[
\boxed{\left(\frac{B_{n,j}-f_{n,j}}{n^{j+2}h_n^2}\right)_j
\Longrightarrow\left(\frac{Z^2}{2\pi\,2^j j!}\right)_j.}\tag{4}
\]
In particular \((N^2/4-V_n)/(n^2h_n^2)\Rightarrow Z^2/(2\pi)\).

**Macroscopic displacement.** If \(h_n\to h\in(0,1]\), while \(h_n<1\) in every finite dimension, let \(p=\Phi(hZ)\), where \(Z\sim N(0,1)\) and \(\Phi\) is the standard Gaussian distribution function. Then, jointly for every finite collection of ranks,
\[
\boxed{\left(\frac{f_{n,j}}{n^{j+2}}\right)_j
\Longrightarrow\left(\frac{1-p^{j+2}-(1-p)^{j+2}}{(j+2)!}\right)_j.}\tag{5}
\]
All joint moments of the quantities in (5), of fixed nonnegative integer orders, also converge. Specifically
\[
\frac{V_n}{n^2}\Longrightarrow W_h=\Phi(hZ)\Phi(-hZ),
\quad \mathbb EW_h=\frac14-\frac1{2\pi}\arcsin\frac{h^2}{1+h^2}.
\]
For \(0<w<1/4\), its complete distribution is
\[
\boxed{\Pr(W_h\le w)=2\Phi\left(-\frac{\Phi^{-1}(1/2+\sqrt{1/4-w})}{h}\right).}\tag{6}
\]
At the endpoint \(h=1\) the law simplifies to \(\Pr(W_1\le w)=1-\sqrt{1-4w}\) on \([0,1/4]\), with \(\mathbb EW_1=1/6\), \(\operatorname{Var}(W_1)=1/180\).

**Supplementary exact expectation.** For every finite \(n\ge2\) and \(0\le h<1\), set
\[
D_n(h)=n(1+h^2)+2h,\quad
\rho_0=-\frac{1+nh}{\sqrt{nD_n(h)}},\quad
\rho_1=\frac{nh^2+2h-1}{D_n(h)}.
\]
Then
\[
\boxed{\mathbb E V_n=\frac n\pi\arccos(\rho_0)+\frac{n(n-1)}{2\pi}\arccos(\rho_1).}\tag{7}
\]
The exact expectation is supplied to check normalization and is not claimed as a new consequence independent of previously established expected-face-number formulas for shifted sections.

## Assumptions and scope

The affine space of the simplex is \(H_n\); the hyperplane is perpendicular to a rotationally invariant unit normal in \(H_n\). Its shift follows the centroid-to-vertex segment, parameterized by \(h_n\in[0,1)\). Every hyperplane contains the interior point \(h_n(e_0-\mathbf{1}/N)\), so its section is nonempty, of dimension \(n-1\), and generic with probability one. A changing normal is independently resampled in each dimension; the limit theorem describes its marginal distribution. The endpoint \(h=1\) is permitted only as a limit of strictly interior shifts, not as a hyperplane through a simplex vertex in finite dimension. The conclusions (3) and (4) concern each **fixed** face rank, not ranks growing with dimension. Formula (5) covers fixed ranks jointly and includes convergence of their moments. The limit statements do not assert finite-dimensional Gaussian independence of the face counts.

## Proof

**1. Faces and Gaussian heights.** For a generic hyperplane section of a simplex containing an interior point, a \(j\)-face of the section is exactly the transversal intersection of the hyperplane with a \((j+1)\)-face of the simplex whose vertices appear on both sides. A simplex \((j+1)\)-face corresponds to a subset of \(j+2\) vertices. Thus if \(K\) vertex heights are positive and \(N-K\) negative, the number of crossed faces is the right-hand side of (1). This is a bijection, because the smallest simplex face containing a generic intersection-face is unique, and its face dimension exceeds that of the intersection by one. For \(j=0\), this is the familiar edge-crossing identity \(V=K(N-K)\), giving (2).

The normal distribution is realized by projecting the vector of independent standard normals \((G_0,\ldots,G_n)\) orthogonally onto \(H_n\); its projected coordinates are \(G_i-\bar G\), and dividing by their Euclidean norm produces a Haar direction without changing signs. The signed height of \(e_i-\mathbf{1}/N\) relative to the shifted hyperplane is \(G_i-\bar G-h_n(G_0-\bar G)\) times a common positive scalar. This proves the exact law (1). Opposite choices of oriented normal merely exchange \(K\) with \(N-K\) and leave the face counts unchanged.

**2. A movable empirical threshold.** Put \(T_n=h_nG_0+(1-h_n)\bar G\), and let \(F_n\) be the empirical CDF of \(G_1,\ldots,G_n\), excluding the distinguished \(G_0\). Up to an error of at most one from that distinguished observation,
\[
K_n=n(1-F_n(T_n))+O(1).
\tag{8}
\]
The \(O(1)\) is deterministic. For \(T_n=O_p(n^{-1/2})\), the local empirical increment satisfies
\[
\sqrt n\{F_n(T_n)-F_n(0)-[\Phi(T_n)-\Phi(0)]\}=o_p(1).
\tag{9}
\]
One direct proof: restrict \(|T_n|\le Cn^{-1/2}\), whose probability is arbitrarily high for sufficiently large fixed \(C\); cover that interval by a deterministic grid with spacing at most \(n^{-3/4}\), containing \(O_C(n^{1/4})\) points. At any grid point the centered empirical increment has variance \(O(n^{-3/2})\), because its underlying Bernoulli event has probability \(O(n^{-1/2})\). Bernstein's inequality (or bounded-increment fourth moments) and a union bound show that its supremum over the grid, multiplied by \(\sqrt n\), converges in probability to zero. Monotonicity of \(F_n\) and boundedness of the normal density extend the conclusion to points between grid nodes; the largest centered binomial count over a grid interval is also \(o_p(\sqrt n)\) by the same Bernstein bound. The possibility that \(T_n\) depends on the observations is immaterial to this uniform estimate.

**3. Critical regime.** If \(\sqrt n h_n\to c\), then
\[
\sqrt n T_n=cG_0+\frac1{\sqrt n}\sum_{i=1}^nG_i+o_p(1),
\qquad
\Phi(T_n)=\frac12+\varphi(0)T_n+o_p(n^{-1/2}),
\]
where \(\varphi(0)=1/\sqrt{2\pi}\). Combining these identities with (8)–(9) yields
\[
\frac{K_n-N/2}{\sqrt n}
=\frac1{\sqrt n}\sum_{i=1}^n
\bigl({\mathbf{1}}_{\{G_i>0\}}-\tfrac12-\varphi(0)G_i\bigr)
-c\varphi(0)G_0+o_p(1).
\tag{10}
\]
The summands are i.i.d. with mean zero, variance \(1/4-1/(2\pi)\) (use \(\mathbb E[G{\mathbf{1}}_{\{G>0\}}]=\varphi(0)\)), and independent of \(G_0\). The CLT and Slutsky's theorem therefore give a centered normal limit of variance \(\sigma_c^2=1/4-1/(2\pi)+c^2/(2\pi)\). Squaring proves the vertex case of (3).

The discrete second difference of \(k\mapsto\binom{k}{r}\) is nonnegative (a shifted \(\binom{k}{r-2}\)), so \(q_r(k)\) is a symmetric discrete-convex function and is minimized at the two balanced integers; this proves that \(B_{n,j}\) is the maximum possible face count. For every fixed \(r=j+2\ge2\), the polynomial \(q_r(k)=\binom{k}{r}+\binom{N-k}{r}\) is symmetric about \(N/2\) and satisfies, uniformly for \(|k-N/2|=o(N)\),
\[
q_r(k)-q_r(N/2)
=\frac{N^{r-2}}{2^{r-2}(r-2)!}(k-N/2)^2
+O_r\bigl(N^{r-3}(k-N/2)^2+N^{r-4}(k-N/2)^4\bigr).
\tag{11}
\]
The expansion is interpreted by the polynomial extension of binomial coefficients and with inapplicable high-order terms omitted when \(r<4\). Moving from the continuous midpoint to the balanced integers changes the baseline by \(O_r(N^{r-2})\), negligible compared with \(n^{r-1}\). Since \((K_n-N/2)/\sqrt n=O_p(1)\), (11) proves (3) jointly for every fixed finite set of ranks; all share the same squared-normal factor.

**4. Intermediate regime.** If \(h_n\to0\) and \(\sqrt n h_n\to\infty\), then \(T_n/h_n\to G_0\) in probability. The uniform empirical error is \(\sup_x|F_n(x)-\Phi(x)|=O_p(n^{-1/2})=o_p(h_n)\). Taylor expansion at zero gives
\[
\frac{K_n/N-1/2}{h_n}\ \longrightarrow_p\ -\varphi(0)G_0.
\tag{12}
\]
The normalized binomial expansions (11), with \(|K_n-N/2|=O_p(nh_n)=o_p(n)\), yield (4).

**5. Macroscopic regime and its exact density.** On a common infinite Gaussian sequence, the strong law gives \(\bar G\to0\), while the Glivenko–Cantelli theorem gives uniform convergence of the empirical CDF of \(G_1,G_2,\ldots\). Thus \(T_n\to hG_0\) almost surely and
\[
K_n/N\longrightarrow \Phi(-hG_0)\quad\text{almost surely}.
\]
Dividing the exact binomial polynomials in (1) by \(n^{j+2}\) proves (5); replacing \(-G_0\) by \(Z\) gives the displayed form. All these variables are uniformly bounded for each fixed rank, hence all fixed joint moments converge by bounded convergence.

For \(p=\Phi(hZ)\), the event \(p(1-p)\le w\) is equivalent to \(|Z|\ge h^{-1}\Phi^{-1}(1/2+\sqrt{1/4-w})\). Symmetry yields (6). To compute the mean, for independent standard Gaussians \(X,Y,Z\), \(\mathbb E[\Phi(hZ)\Phi(-hZ)]=\Pr(X\le hZ,Y\le-hZ)\). The standardized pair \((hZ-X,-hZ-Y)\) has correlation \(-h^2/(1+h^2)\); the classical Gaussian quadrant identity gives \(1/4-\arcsin(h^2/(1+h^2))/(2\pi)\). If \(h=1\), \(\Phi(Z)\) is uniform on \((0,1)\), so \(W_1=U(1-U)\), with CDF \(1-\sqrt{1-4w}\), mean \(1/6\) and variance \(1/180\).

**6. Finite expected vertices.** For \(0\le i\le n\), let \(Y_i=G_i-\bar G-h(G_0-\bar G)\). Their covariance is
\[
\operatorname{Cov}(Y_i,Y_j)=\delta_{ij}-1/N-h[(\delta_{i0}-1/N)+(\delta_{j0}-1/N)]+h^2(1-1/N).
\]
The correlation for a pair with one index zero is \(\rho_0\) and between two nonzero indices is \(\rho_1\), as in (7). A centered bivariate Gaussian pair of correlation \(\rho\) has opposite signs with probability \(\arccos(\rho)/\pi\). There are \(n\) edges incident to vertex zero and \(\binom n2\) edges among the others. Summing their crossing probabilities establishes (7), including \(h=0\) and its previously established central expected-count formula.

## Verification

The included `verify.py` requires Python 3 and only standard-library modules. Execute `python verify.py` from the containing directory. It checks 2,250 face-count identities against independent enumeration of crossed vertex subsets for dimensions \(2\) through \(11\), 30 independent symbolic covariance comparisons in floating point, seven Monte Carlo checks of (7), and 660 coupled large-dimensional comparisons for the macroscopic limit. It also checks exact scalar endpoint mean and variance identities and the positivity of \(\sigma_c^2\). These numerical/finite checks **do not certify the infinite-dimensional weak limits**: those follow from steps 2–5 and the cited probability theorems.

## Relationship to prior work

Schange [1] derives solid-angle/integral expressions for **expected face numbers** of random shifted sections of polytopes, including simplices (Theorem 4.7). His theorem includes the context of (7), so the finite expected count is explicitly not claimed as independently new. The present claim is instead the exact *joint distributional reduction* for the vertex-directed noncentral section and its **three distinct dimension-dependent fluctuation laws**, including the critical \(n^{-1/2}\) displacement crossover, the mesoscopic quadratic regime and the macroscopic random limiting face vector.

Two independently published research notes [2, 3] establish the Gaussian sign count, complete face-vector reduction, and rank-one chi-square fluctuations **for central hyperplanes**. In their statements the plane passes through the centroid, so their conclusions cover \(c=0\), not the positive critical parameter, mesoscopic growth, or fixed-positive-displacement limits. The central results are used as close comparisons, not repackaged. Kabluchko–Seidel [4] treats angles and expected face numbers for central sections of regular polytopes; De Loera–Lopez-Campos–Torres [5] studies deterministic section-vertex bounds and realizable configurations, not random displacement phase laws. The new formulas require tracking a Gaussian threshold tied to one distinguished vertex and its interaction with the empirical sample mean.

## Limitations

Only regular simplices, Haar directions, and shifts along a centroid-to-vertex line are covered. No affine-uniform distribution on all displaced hyperplanes is asserted. The intermediate/critical limits concern fixed face ranks and distributional convergence, with no quantitative error rate or claim of an exact elementary probability mass function for finite-dimensional sign counts. The endpoint \(h=1\) describes limits of interior sections, not degenerate sections through a vertex. General empirical-process methods and normal quadrant probabilities are classical. Historical priority for the combined phase diagram could be affected by older work using alternative statistical terminology; absence of a matching indexed result is not proof of global novelty. The scientific review is not an independent audit.

## References

[1] Philipp Schange, *Solid-angle formulas for simplicial cones and random shifted sections of polytopes*, arXiv:2610.28084, first submitted October 20, 2026; https://arxiv.org/abs/2610.28084 .

[2] *Exact mean and chi-square fluctuations of Haar central simplex-section vertex counts*, publicly available research note, October 2026; https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-mean-and-chi-square-fluctuations-of-haar-central-simplex-s--d3f9b0447a8e .

[3] *Joint chi-square face-vector fluctuations of random central regular-simplex sections*, publicly available research note, October 2026; https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-joint-chi-square-face-vector-fluctuations-of-random-central-regu--aa90c887fe90 .

[4] Zakhar Kabluchko and Hans Seidel, *Convex cones spanned by regular polytopes*, arXiv:2006.09492, first submitted June 16, 2020; https://arxiv.org/abs/2006.09492 .

[5] Jesus A. De Loera, Georgina Lopez-Campos, Antonio J. Torres, *On the number of vertices in hyperplane cross-sections of convex polytopes*, arXiv:2412.12419, first submitted December 17, 2024; https://arxiv.org/abs/2412.12419 .
