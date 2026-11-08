# Exact face-vector mixtures and nonconcentrated near-vertex sections of cross-polytopes

## Finding
For every integer \(d\ge3\), set
\[
C_d=\operatorname{conv}\{\pm e_1,\ldots,\pm e_d\}\subset\mathbb R^d.
\]
Let \(0<h<1\) and intersect \(C_d\) with the uniformly oriented affine hyperplane \(H=h e_d+L\), where \(L\) is Haar-uniform among linear hyperplanes. This is an interior, noncentral section.

Let \(G_1,\ldots,G_d\) be independent standard normal variables and define
\[
K=\#\{i\in\{1,\ldots,d-1\}:|G_i|>h|G_d|\},\qquad p=K+1.
\]
The entire face vector is a deterministic function of this one integer: almost surely, for each \(0\le j\le d-2\),
\[
f_j(C_d\cap H)=2^{j+2}\binom{d}{j+2}-\binom{p}{j+2}-[z^{j+2}](1+z)^p(1+2z)^{d-p}.
\tag{1}
\]
The bracket extracts a coefficient, with binomial coefficients outside their natural range interpreted as zero. In particular the vertex count is
\[
V_{d,h}=p(2d-1-p)=(K+1)(2d-2-K).
\tag{2}
\]
The exact finite-dimensional mixing law is
\[
\Pr(K=k)=\binom{d-1}{k}\sqrt{\frac2\pi}\int_0^\infty e^{-t^2/2}\operatorname{erfc}\!\left(\frac{ht}{\sqrt2}\right)^k
\operatorname{erf}\!\left(\frac{ht}{\sqrt2}\right)^{d-1-k}\,dt,\qquad 0\le k\le d-1.
\tag{3}
\]
The values in (2) are strictly increasing for \(0\le K\le d-2\), with a final tie between \(K=d-2\) and \(K=d-1\); hence (3) gives the exact vertex-count distribution and (1) gives the complete joint face-vector distribution.

At fixed \(d\), as \(h\uparrow1\) **from below**, \(K\) tends to the discrete uniform distribution on \(\{0,\ldots,d-1\}\). Consequently the limiting maximum-vertex probability is exactly \(2/d\), while each of the \(d-2\) lower possible vertex counts has probability \(1/d\). The limiting moments are
\[
\lim_{h\uparrow1}\mathbb E V_{d,h}=\frac{2(d^2-1)}3,\qquad
\lim_{h\uparrow1}\operatorname{Var}(V_{d,h})=\frac{(d-2)(d-1)(d+1)(4d-7)}{45}.
\tag{4}
\]
For any sequence \(h_d\in(0,1)\) such that \(h_d\to h_*\in(0,1]\),
\[
\frac{V_{d,h_d}}{d^2}\ \Longrightarrow\ Y_{h_*}=Q(2-Q),\qquad
Q=\operatorname{erfc}\!\left(\frac{h_*|G|}{\sqrt2}\right),\quad G\sim N(0,1).
\tag{5}
\]
All positive integer moments converge as well. For \(0<y<1\), the limiting CDF is
\[
\Pr(Y_{h_*}\le y)=\operatorname{erfc}\!\left(\frac{\operatorname{erfc}^{-1}(1-\sqrt{1-y})}{h_*}\right).
\tag{6}
\]
In particular, when \(h_d\uparrow1\),
\[
\Pr(Y_1\le y)=1-\sqrt{1-y},\quad 0\le y\le1,\qquad
\mathbb E Y_1=\frac23,\quad\operatorname{Var}(Y_1)=\frac4{45}.
\tag{7}
\]
Thus these section vertex counts have fluctuations of order \(d^2\), not a concentrating normalized limit, whenever the shift fraction stays positive.

## Assumptions and scope
The ambient Euclidean metric is standard; orientations are sampled with the invariant probability measure on hyperplanes through the origin. The affine section is always taken through \(h e_d\), with the strict condition \(0<h<1\). The section has dimension \(d-1\) and contains the shift point in its relative interior. Almost-sure claims exclude the measure-zero set of orientations at which a section passes through any original vertex or meets a proper face nongenerically. For every valid \(h\), almost surely these degeneracies do not occur. The one-sided limit \(h\uparrow1\) is **not** an assertion about the geometrically different hyperplane section at \(h=1\).

## Proof
**Step 1: signs and the parameter.** Write a Haar-random normal vector as \(U=G/\|G\|_2\), with independent Gaussian components. Replacing \(U\) by \(-U\) leaves the affine hyperplane unchanged, so orient the normal to make its last component positive. Its equation is \(\langle U,x-h e_d\rangle=0\). Of the vertices \(\pm e_d\), one lies strictly on each side because \(0<h<1\). For each \(i<d\), the pair \(\pm e_i\) is separated by the hyperplane if and only if \(|G_i|>h|G_d|\). Otherwise both vertices lie on the negative side. Thus there are exactly \(p=K+1\) coordinate pairs with one positive and one negative vertex and \(d-p\) coordinate pairs with both vertices negative; no pair has two positive vertices.

**Step 2: every face count.** A \((j+1)\)-face of the regular cross-polytope is a simplex with \(r=j+2\) vertices obtained by selecting \(r\) distinct coordinate axes and one sign on each axis. For a generic hyperplane, such a face meets the hyperplane in a \(j\)-face if and only if its chosen vertices occur on both sides. All such section faces are distinct, and every \(j\)-face arises this way: the section is transverse to each intersected original face. There are \(2^r\binom dr\) original \((j+1)\)-faces. The number entirely on the positive side is \(\binom pr\). For those entirely on the negative side, each of the \(p\) split coordinate pairs offers one negative option and each remaining pair offers two. Their generating polynomial is \((1+z)^p(1+2z)^{d-p}\); extraction of the \(z^r\) coefficient proves (1). For \(j=0\), equivalently count crossing original edges: there are \(p(2d-p)\) positive-negative vertex pairs and exactly \(p\) nonedges joining antipodes, proving (2). Its successive difference in \(K\) is \(2(d-2-K)\), yielding the final two-parameter tie.

**Step 3: exact mixing distribution.** Given \(T=|G_d|=t\), the indicators \(\mathbf1\{|G_i|>ht\}\), \(i<d\), are independent Bernoulli variables with success probability \(q_h(t)=\operatorname{erfc}(ht/\sqrt2)\). Since \(T\) has the half-normal density \(\sqrt{2/\pi}e^{-t^2/2}\) for \(t>0\), integrating the conditional binomial law yields (3).

**Step 4: the finite-dimensional vertex boundary.** As \(h\uparrow1\), the random integer \(K\) converges almost surely under a Gaussian coupling to the number of the first \(d-1\) absolute Gaussian samples larger than the last. The rank of the last sample among the \(d\) continuous, independent and identically distributed samples is uniform. The resulting exact face-vector law follows from (1). Summing \(r(2d-1-r)\) and its square over uniform integers \(r\in\{1,\ldots,d\}\), using the elementary sums of the first four powers, gives (4). The maximum \(d(d-1)\) occurs at \(r=d-1,d\) and nowhere else.

**Step 5: the growing-dimensional limit.** For every \(d\), couple the conditional binomial variable \(K\), given \(T\), with its conditional success probability \(q_{h_d}(T)\). Then
\[
\mathbb E\left[\left(\frac{K}{d-1}-q_{h_d}(T)\right)^2\right]
\le\frac{1}{4(d-1)}.
\]
By continuity, \(q_{h_d}(T)\to Q=q_{h_*}(T)\). Therefore \(K/d\) converges in distribution to \(Q\), and (2) with the continuous mapping theorem yields (5). Because \(0\le V_{d,h}/d^2\le1\), convergence of every positive integer moment follows from boundedness. For \(0<y<1\), the inequality \(Q(2-Q)\le y\) is equivalent to \(Q\le 1-\sqrt{1-y}\). Since \(T\) is half normal and \(Q=\operatorname{erfc}(h_*T/\sqrt2)\), inversion gives (6). At \(h_*=1\), the probability-integral transform makes \(Q\) exactly uniform on \([0,1]\); integration of \(Q(2-Q)\) and its square proves (7).

## Verification
The included `verify.py` is standalone Python using only the standard library. Run `python3 verify.py`. It enumerates signed-coordinate faces independently and compares their direct intersection conditions against (1) for dimensions \(3\) through \(8\), four shifts, and 21 normal vectors each. It also checks the crossing-edge vertex formula, exhaustively enumerates all small-sample Gaussian rank permutations, verifies the two highest parameter values share an entire face vector, and numerically compares the binomial mixture integral with direct Gaussian samples. On the reviewed copy it printed `PASS 2389 supplementary tests`. The enumeration and simulation are finite checks only; the dimension-uniform results are proved by the arguments above.

## Relationship to prior work
Schange, *Solid-angle formulas for simplicial cones and random shifted sections of polytopes* (arXiv:2610.28084v1, October 20, 2026), Theorem 4.7(b), computes **expected face counts** of shifted crosspolytope sections using conic intrinsic volumes. The proof and discussion in its Section 4.3 and appendix were inspected. They do not state the joint distribution, the rank-mixture law, or the macroscopic high-dimensional nonconcentration and one-sided near-vertex law above. Knowledge of expectations does not directly specify their full joint distribution; the explicit sign-rank reduction supplies additional structure. This remains the most relevant originality comparison: a different algebraic reconstruction of the distribution from all of the published expected face numbers could potentially make portions of the finite formula an implicit consequence.

Kabluchko and Seidel, *Convex cones spanned by regular polytopes* (arXiv:2006.09492v2, 2020; Advances in Geometry 22, 2022), Theorem 4.5, treats expected face counts of **central** sections. It does not cover affine shifts along a vertex axis or a nondegenerate limit for vertex counts. Accessible published research-record comparisons concerning the face-vector fluctuations of central simplex and cube sections describe different polytopes and sampling regimes. A survey of accessible previous claims found no overlapping shifted crosspolytope joint law.

## Limitations
The results concern codimension-one sections of a Euclidean regular cross-polytope and shifts lying strictly between its center and one vertex. No claim is made for arbitrary affine translations, asymmetric crosspolytopes, higher-codimension sections, or the **actual** vertex-passing section at \(h=1\). The limit approaching the vertex is explicitly one-sided. The result has received self-review only, not independent mathematical validation. Historical priority cannot be established by searching alone; independent literature review is appropriate before publication.

## References
- Philipp Schange, *Solid-angle formulas for simplicial cones and random shifted sections of polytopes*, arXiv:2610.28084v1 (first public October 20, 2026), especially Section 4.3, Theorem 4.7, and Appendix A. https://arxiv.org/abs/2610.28084
- Zakhar Kabluchko and Hauke Seidel, *Convex cones spanned by regular polytopes*, arXiv:2006.09492v2 (2020), published in *Advances in Geometry* 22 (2022), 245–267, especially Section 4 and Theorem 4.5. https://arxiv.org/abs/2006.09492
