# Three-edge motifs determine the cubic projection-width moment of graphical zonotopes

## Finding
Let \(G=(V,E)\) be any finite, connected, simple graph with \(N=|V|\ge3\), \(m=|E|\), and degrees \(d_v\). In the Euclidean zero-sum hyperplane \(H=\{x\in\mathbb R^N:\sum_v x_v=0\}\), consider the centered graphical zonotope
\[
Z_G=\sum_{\{i,j\}\in E}[-(e_i-e_j)/2,(e_i-e_j)/2].
\]
Let \(U\) be Haar-uniform on the unit sphere in \(H\), and let \(W_G\) be the length of the orthogonal projection of \(Z_G\) onto the line spanned by \(U\). Define the edge-motif counts
\[
q=\sum_v\binom{d_v}{2},\quad s=\sum_v\binom{d_v}{3},\quad t=\#\{\text{triangles in }G\},\quad p=\sum_{\{i,j\}\in E}(d_i-1)(d_j-1)-3t.
\]
Here \(s\) counts edge-subsets forming three-stars and \(p\) counts edge-subsets forming simple three-edge paths, even if extra edges connect vertices of the path. Put
\[
\mu=\frac2{\sqrt\pi},\quad \eta=\frac13+\frac{2\sqrt3}{\pi},\quad \theta=\arcsin\frac13,
\]
and introduce five universal coefficients
\[
\begin{aligned}
 k_0&=\frac8{\sqrt\pi}-6\mu+2\mu^3,\\
 k_1&=\frac5{\sqrt\pi}-\mu(2+2\eta)+2\mu^3,\\
 k_s&=\frac{4\sqrt2+18\theta}{\pi^{3/2}}-3\mu\eta+2\mu^3,\\
 k_p&=\frac{4\sqrt2+2\pi-6\theta}{\pi^{3/2}}-\mu(2\eta+\mu^2)+2\mu^3,\\
 k_t&=\frac3{\sqrt\pi}-3\mu\eta+2\mu^3.
\end{aligned}
\]
Define the Gaussian edge-difference total \(T_G=\sum_{\{i,j\}\in E}|G_i-G_j|\) for independent standard normal \(G_i\). Then the **exact third centered moment** of \(T_G\) is
\[
\boxed{K_3(G)=\mathbb E[(T_G-\mathbb ET_G)^3]=m k_0+6q k_1+6s k_s+6p k_p+6t k_t.}
\tag{1}
\]
This is an exact, finite motif formula, not an asymptotic expansion. To obtain the corresponding genuine spherical projection-width moment, put \(d=N-1\) and
\[
 r_j=2^{j/2}\frac{\Gamma((d+j)/2)}{\Gamma(d/2)},\quad M_1=m\mu,\quad M_2=2m+m(m-1)\mu^2+2q(\eta-\mu^2),\quad M_3=K_3(G)+3M_1M_2-2M_1^3.
\]
Then
\[
\boxed{\mathbb E[(W_G-\mathbb EW_G)^3]=\frac{M_3}{r_3}-3\frac{M_1M_2}{r_1r_2}+2\left(\frac{M_1}{r_1}\right)^3.}
\tag{2}
\]

In particular, let \(G_\triangle\) be the triangular prism graph and \(G_\square=K_{3,3}\). Both have six vertices, nine edges, every degree equal to three, and **identical mean and variance of spherical projection width**. Nevertheless,
\[
\boxed{\mathbb E[(W_{G_\triangle}-\mathbb EW_{G_\triangle})^3]-\mathbb E[(W_{G_\square}-\mathbb EW_{G_\square})^3]=\frac{12}{r_3}(k_t-3k_p)<0,\qquad d=5,}
\tag{3}
\]
with numerical value approximately \(-0.204340519081\). This explicitly distinguishes their random projection-width laws at the first moment beyond variance.

## Assumptions and scope
All graphs are finite, simple, unweighted and connected, with at least three vertices. The metric is the inherited Euclidean metric of \(H\). The width convention is the full length of the one-dimensional projection, without a factor of one half. The coefficients and motif counts refer to **edge subsets**, not induced subgraphs. No assumptions about triangles, regularity, planarity, or graph size beyond those stated are needed.

A graph with at least two vertices would also satisfy the formulas, but the restriction \(N\ge3\) keeps the unit sphere of \(H\) nonempty and of its usual positive-dimensional type. The Gaussian random variables used in the derivation are auxiliary; the final observable in (2) is the width in an actual uniformly random unit direction.

## Proof
**Step 1: exact Gaussian and spherical normalization.** The support function of a line segment \([-v/2,v/2]\) is \(|\langle v,u\rangle|/2\). Support functions add under Minkowski addition, so the full width of \(Z_G\) at \(u\in H\) is
\[
 w(Z_G,u)=\sum_{\{i,j\}\in E}|u_i-u_j|.
\]
Let \(g\) be an independent standard Gaussian vector in \(\mathbb R^N\), and \(g_H=g-(\sum_i g_i)\mathbf1/N\). Then \(g_H=RU\), where \(U\) is Haar-uniform on the unit sphere of \(H\), \(R\sim\chi_d\), and \(R,U\) are independent. The equality of all edge differences between \(g\) and \(g_H\) yields \(T_G=RW_G\). Consequently \(\mathbb ET_G^j=r_j\mathbb EW_G^j\) for \(j=1,2,3\), which proves (2) from (1) and the raw moments.

**Step 2: one- and two-edge kernels.** Let \(X_{ij}=|g_i-g_j|\). Every such variable has mean \(\mu=2/\sqrt\pi\), second moment \(2\), and third moment \(8/\sqrt\pi\). Distinct disjoint edges give independent variables. Distinct incident edges have absolute correlation \(1/2\) between their centered signed Gaussian differences. Bivariate normal polar integration gives
\[
 \mathbb E X_{ij}X_{ik}=\eta=\frac13+\frac{2\sqrt3}{\pi}.
\]
Conditioning on \(g_i-g_k\), the other incident signed difference has conditional mean equal to one half of this difference and conditional variance \(3/2\). Therefore
\[
\mathbb E(X_{ij}^2X_{ik})=\frac32\,\frac2{\sqrt\pi}+\frac14\,\frac8{\sqrt\pi}=\frac5{\sqrt\pi}.
\]
These identities give the single-variable third cumulant \(k_0\), the joint third cumulant of a repeated edge and an incident edge \(k_1\), and the formula for \(M_1,M_2\).

**Step 3: the three-star kernel.** Write \(\phi(z)=(2\pi)^{-1/2}e^{-z^2/2}\), \(h(z)=\mathbb E|z-g|=2\phi(z)+z\operatorname{erf}(z/\sqrt2)\), with \(g\) standard Gaussian independent of \(z\). For three edges sharing a center, conditional independence of their leaves gives \(\mathbb E(X_1X_2X_3)=\mathbb Eh(g)^3\). Put \(u(z)=h'(z)=\operatorname{erf}(z/\sqrt2)\). Three elementary Gaussian integration-by-parts identities, using \(\mathbb E[g f(g)]=\mathbb Ef'(g)\) and \(u'=2\phi\), give
\[
 \mathbb Eh(g)^3=32\mathbb E\phi(g)^3+18\mathbb E[\phi(g)u(g)^2].
\]
Here \(\mathbb E\phi(g)^3=1/(4\sqrt2\pi^{3/2})\). For the second term, the density \(\phi(z)^2\) is a constant multiple of a centered normal with variance \(1/2\). Writing each error function as a conditional Gaussian sign expectation, the elementary bivariate sign-correlation identity \(\mathbb E\operatorname{sgn}(A)\operatorname{sgn}(B)=(2/\pi)\arcsin\operatorname{Corr}(A,B)\) at correlation \(1/3\) yields
\[
 \mathbb E[\phi(g)u(g)^2]=\frac{\theta}{\pi^{3/2}}.
\]
Thus the star product moment is \((4\sqrt2+18\theta)/\pi^{3/2}\). Since all three edge pairs share a vertex, subtracting \(3\mu\eta\) and adding \(2\mu^3\) gives \(k_s\).

**Step 4: the three-edge path kernel.** For independent standard normals \(A,B,C,D\), conditioning on the middle variables gives
\[
 \mathbb E|A-B||B-C||C-D|=\mathbb E[h(B)\,|B-C|\,h(C)].
\]
Since \(h\) is even, splitting the integral by signs and by the larger absolute middle variable reduces it to
\[
 8\int_0^\infty x Q(x)Q'(x)\,dx
 =4\int_0^\infty\left(\frac1\pi-Q(x)^2\right)dx,
\quad Q(x)=\int_0^x\phi(z)h(z)dz=\frac{\operatorname{erf}(x)}{\sqrt\pi}-\phi(x)\operatorname{erf}(x/\sqrt2).
\]
The integration by parts is justified because \(Q(x)\) approaches \(1/\sqrt\pi\) at Gaussian-tail speed. Expanding the square uses only the exact elementary normal integrals
\[
 \begin{aligned}
 \int_0^\infty (1-\operatorname{erf}(x)^2)dx&=\sqrt{2/\pi},\\
 \int_0^\infty\operatorname{erf}(x)\phi(x)\operatorname{erf}(x/\sqrt2)dx&=\pi^{-1}\arcsin(1/\sqrt3),\\
 \int_0^\infty\phi(x)^2\operatorname{erf}(x/\sqrt2)^2dx&=\theta/(2\pi^{3/2}).
 \end{aligned}
\]
The first follows from integration by parts and a one-dimensional Gaussian integral. The others follow by writing products of error functions as expected signs of correlated centered Gaussians (and splitting an even integrand at zero). Since \(2\arcsin(1/\sqrt3)=\pi/2-\theta\), the path product moment equals \((4\sqrt2+2\pi-6\theta)/\pi^{3/2}\). Its adjacent edge pairs contribute \(2\mu\eta\) and its disjoint outer pair contributes \(\mu^3\) to the third cumulant subtraction, giving \(k_p\).

**Step 5: the triangle kernel.** For three independent standard Gaussians, make the orthogonal change of variables \(x=(g_1-g_2)/\sqrt2\), \(y=(g_1+g_2-2g_3)/\sqrt6\). The variables \(x,y\) are independent standard normals and
\[
 |g_1-g_2|\,|g_2-g_3|\,|g_3-g_1|=\frac{|x|\,|x^2-3y^2|}{\sqrt2}.
\]
Polar integration \((x,y)=r(\cos\varphi,\sin\varphi)\) gives \(\mathbb Er^3=3\sqrt{2\pi}/2\) and angular average
\[
 \frac{2}{\pi}\int_0^1|1-4z^2|\,dz=\frac2\pi.
\]
The triangle product moment is therefore \(3/\sqrt\pi\), and all three edge pairs are incident, giving \(k_t\).

**Step 6: cumulant expansion and motif enumeration.** Multilinearity of the joint third cumulant gives \(\kappa_3(T_G)=\sum_{e,f,h}\kappa(X_e,X_f,X_h)\) over *ordered* triples of edges. If all three edges are distinct and their three-edge graph is disconnected, at least one edge variable is independent of the other two, and the joint cumulant vanishes. Connected distinct-edge triples of a simple graph are precisely three-stars, three-edge paths, and triangles, with coefficients \(k_s,k_p,k_t\). Each unordered triple admits six orders. Single-edge triples contribute \(m k_0\); triples with exactly two equal edges and a third incident edge contribute \(6q k_1\). A three-edge path has a unique central edge, hence its number is \(\sum_{\{i,j\}\in E}(d_i-1)(d_j-1)-3t\): every triangle creates three spurious pair-of-neighbor choices in this sum. This proves (1) and the moment conversion (2).

**Step 7: the six-vertex separation.** Both the triangular prism and \(K_{3,3}\) have \((N,m,q,s)=(6,9,18,6)\). Their \((p,t)\) are respectively \((30,2)\) and \((36,0)\). Their first two Gaussian moments, hence their first two spherical moments, coincide, so their centered third spherical-moment difference equals the third Gaussian-cumulant difference divided by \(r_3\): this is (3). Explicitly,
\[
 k_t-3k_p=\frac{18\arcsin(1/3)-\pi-8+12\sqrt3-12\sqrt2}{\pi^{3/2}}<0.
\]
For a rigorous sign check, \(\arcsin(1/3)<0.34\), because \(\sin(0.34)\ge0.34-0.34^3/6>1/3\). The elementary bounds \(\pi>3.14\), \(\sqrt3<1.733\), and \(\sqrt2>1.414\) make the numerator strictly less than \(6.12-3.14-8+20.796-16.968<0\). Thus the width laws differ, completing the proof.

## Verification
All formulas are exact for every graph in the stated scope. The included standard-library Python program `verify.py` independently classifies edge-triples for all simple graphs on three through five vertices, integrates the nontrivial one-dimensional star and path Gaussian kernels numerically, and verifies the graph motif counts, first two moment equalities, and signed third-moment difference for the triangular-prism and complete-bipartite example. Run `python3 verify.py`; its successful marker is `GRAPHICAL_ZONOTOPE_THIRD_WIDTH_MOMENT_CHECKS_PASSED`. The finite enumerations and quadratures check arithmetic and implementation; the preceding analytical argument establishes the universal result.

## Relationship to prior work
Padrol, Pilaud, and Poullot (*Deformed Graphical Zonotopes*, arXiv:2111.12422, first publicly posted 2021-11-24) give the standard graphical-zonotope construction and analyze their deformation cones, linear equations, and facet inequalities. Their full available text does not establish projection-width moments.

The published research result *Sharp width-variance extremizers among tree graphical zonotopes* determines the first two spherical width moments for all simple connected graphs, and compares tree variances. The exact first and second moment formula used here agrees with that result; its full accessible theorem and proof stop at order two and do not give the star/path/triangle cubic law or the cubic-graph separation. Kabluchko, Litvak, and Zaporozhets (*Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479) calculate higher width moments for regular cubes, simplices, and crosspolytopes, not general graphical zonotopes with motif-dependent third cumulants.

At fixed \(N,m,q\), the two lower spherical width moments coincide, whereas the cubic invariant probes three-edge subgraphs. Neither first/second-moment formulas nor cubic *circumradius* formulas for complete multipartite zonotopes imply the presented third **projection-width** moment. Different generating sets and Gaussian dependencies govern those quantities.

## Limitations
The claim concerns unweighted graphical zonotopes in their canonical root-coordinate Euclidean embedding. Arbitrary affine changes, weighted edges, and higher-dimensional random projections are outside the formula. Numerical signs reported in decimals are approximations; the strict inequality has an analytical proof. Priority remains provisional: a logically equivalent formula could exist in unindexed stochastic graph-variation or Gaussian absolute-moment literature, even though targeted searches and inspected closest full texts revealed none.

## References
1. Arnau Padrol, Vincent Pilaud, Germain Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422, first public version 2021-11-24, https://arxiv.org/abs/2111.12422 ; full HTML https://arxiv.org/html/2111.12422v2 .
2. *Sharp width-variance extremizers among tree graphical zonotopes*, research result and full proof available at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-width-variance-extremizers-among-tree-graphical-zonotopes--482983ab9269 .
3. Zakhar Kabluchko, Alexander E. Litvak, Dmitry Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479, first version 2015-11-26, https://arxiv.org/abs/1511.08479 .
