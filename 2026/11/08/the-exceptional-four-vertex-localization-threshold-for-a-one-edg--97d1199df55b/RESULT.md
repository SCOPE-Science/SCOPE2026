# The exceptional four-vertex localization threshold for a one-edge-deformed complete metric graph

## Finding
Let \(G_{n,h}\), for an integer \(n\ge4\) and a real \(h>0\), be the compact metric graph obtained from \(K_n\) by giving one distinguished edge \(ab\) length \(h\) and every other edge length \(1\). Integrate with **unnormalized arclength** \(ds\), and define
\[
\mathcal H_{n,h}=\left\{f\in C(G_{n,h}):f|_e\in H^1(e)\ \text{for every edge},\quad \int_{G_{n,h}}f\,ds=0\right\}.
\]
The sharp squared pointwise Sobolev embedding constant is
\[
\mathcal K_{n,h}=\sup_{0\ne f\in\mathcal H_{n,h}}\frac{\|f\|_\infty^2}{\int_{G_{n,h}}|f'|^2\,ds}.
\]
Call the two endpoints of the distinguished edge **special** and the other \(n-2\) vertices **ordinary**. There are three edge orbits: distinguished, mixed (special–ordinary), and ordinary–ordinary. Every maximizing evaluation point is an edge-interior point, and the complete classification is:

- If \(n\ge5\) and \(0<h<1\), precisely the midpoints of all ordinary–ordinary edges maximize.
- If \(n=4\), set \(h_\circ=\sqrt5-2\). For \(0<h<h_\circ\), only the midpoint of the unique ordinary–ordinary edge maximizes. At \(h=h_\circ\), that midpoint and one explicitly located interior point on **each** of the four mixed edges tie. For \(h_\circ<h<1\), precisely those four mixed-edge interior points maximize.
- If \(h=1\), precisely the midpoints of **every** edge maximize.
- If \(h>1\), precisely the midpoint of the distinguished edge maximizes, for every \(n\ge4\).

For a mixed edge parametrized from its special endpoint by \(z\in[0,1]\), the unique internal maximizing point is \(z=z_*\), with
\[
z_*=\frac{C_m+F_o-F_s}{2C_m},
\]
where the explicit rational quantities \(F_s,F_o,C_m\) are given below. One always has \(0<z_*<1\). The sharp constant, without any implicit optimization, is
\[
\boxed{\quad \mathcal K_{n,h}=\frac{F_{\max}}{L}-\frac{J}{2L^2}.\quad}
\]
The finite algebraic recipe for \(F_{\max}\) and \(J\) appears in the next section. Equality holds exactly for nonzero scalar multiples of the centered resistance Green representers at the classified maximizing points.

## Assumptions and scope
All edges are electrical resistors whose resistances equal their **arclengths**; electrical effective resistance is written \(r(x,y)\). Set
\[
L=\frac{n(n-1)}2-1+h,\qquad d=2+(n-2)h,\qquad D_s=n-2+h,\quad D_o=n-1,
\]
and define the three vertex-to-vertex resistances
\[
r_d=\frac{2h}{d},\qquad
r_m=\frac{2nh-3h+3}{nd},\qquad r_o=\frac2n.
\]
(The subscripts mean distinguished special–special, mixed special–ordinary, and ordinary–ordinary.) Define
\[
H=\frac{h(h-r_d)+2(n-2)(1-r_m)+\binom{n-2}{2}(1-r_o)}6,
\]
\[
F_s=H+\frac{D_s r_d+(n-2)D_o r_m}{2},\qquad
F_o=H+\frac{2D_s r_m+(n-3)D_o r_o}{2},
\]
\[
C_d=L(h-r_d)-h^2,\qquad
C_m=L(1-r_m)-1,\qquad
C_o=L(1-r_o)-1.
\]
For \(n\ge4,h>0\), all three \(C\)-coefficients are positive and \(C_m>|F_s-F_o|\). Define three orbit-peak quantities
\[
M_d=F_s+\frac{C_d}{4},\qquad
M_o=F_o+\frac{C_o}{4},\qquad
M_m=F_s+\frac{(C_m+F_o-F_s)^2}{4C_m}.
\]
The classification above selects \(F_{\max}\) as the relevant one of \(M_d,M_o,M_m\) (ties are stated explicitly). Finally let
\[
J=D_sF_s+\frac{(n-2)D_oF_o}{2}
  +\frac{hC_d+2(n-2)C_m+\binom{n-2}{2}C_o}{6}.
\]
Thus \(\mathcal K_{n,h}\) is an exact rational function of \(n,h\) within each region; the location threshold \(\sqrt5-2\) is the only nonunit boundary for \(n\ge4\).

## Proof
**1. Green diagonal and mean resistance.** Let \(r(x,y)\) be electrical effective resistance and put
\[
F(x)=\int_G r(x,y)\,ds_y,\qquad
J=\int_G\int_G r(y,z)\,ds_y\,ds_z.
\]
On the real Hilbert space of continuous edgewise \(H^1\) mean-zero functions with inner product \(\int f'g'\,ds\), evaluation at \(x\) has Green representer
\[
g_x(y)=\frac{F(x)+F(y)}{2L}-\frac{J}{2L^2}-\frac{r(x,y)}2.
\]
Indeed, differences of evaluations have squared dual norm \(r(x,y)\) (the Thomson energy principle); centering the resistance identity then gives \(\int_G g_x\,ds=0\), \(\int_G g_x'g'\,ds=g(x)\), and
\[
\|\delta_x\|^2=g_x(x)=\frac{F(x)}L-\frac{J}{2L^2}.
\]
Consequently \(\mathcal K_{n,h}\) is obtained by maximizing \(F\), and equality is exactly Cauchy–Schwarz equality for \(g_x\).

**2. Universal edge integral.** Let \(e=uv\) have length \(\ell\) and endpoint effective resistance \(r_e=r(u,v)\). With normalized edge coordinate \(z\in[0,1]\), series/parallel reduction gives, for \(y\) off the interior of \(e\),
\[
r(x_z,y)=(1-z)r(u,y)+zr(v,y)+(\ell-r_e)z(1-z).
\]
On the same edge, writing \(x=\ell z\) and the other point as \(y\in[0,\ell]\),
\[
r(x,y)=|x-y|-\frac{\ell-r_e}{\ell^2}(x-y)^2.
\]
Integrating the two cases over all edges yields the identity
\[
\boxed{F(x_z)=(1-z)F(u)+zF(v)+C_ez(1-z),\qquad C_e=L(\ell-r_e)-\ell^2.}
\]
It also gives, after integrating along an edge,
\[
J=\sum_{e=uv}\ell_e\frac{F(u)+F(v)}2+\frac16\sum_e\ell_e C_e.
\]
A second useful integral is
\[
F(v)=\frac12\sum_{u} D_u r(u,v)+\frac16\sum_{e=cd}\ell_e(\ell_e-r(c,d)),
\]
where \(D_u\) is the total arclength incident on vertex \(u\).

**3. Three resistance orbits.** The weighted vertex Laplacian is the unit-edge complete-graph Laplacian, perturbed by \((1/h-1)(e_a-e_b)(e_a-e_b)^{\mathsf T}\). On the zero-sum subspace its unperturbed inverse equals \(I/n\); applying the rank-one inversion formula gives
\[
r(a,b)=\frac{2h}{d},\quad r(a,v)=\frac{2nh-3h+3}{nd},\quad r(v,w)=\frac2n
\]
for distinct ordinary vertices \(v,w\). Substitution into the preceding integral formulas yields exactly \(F_s,F_o\) and \(J\) in the scope section. The three edge-orbit formulas are therefore
\[
F_{d}(z)=F_s+C_dz(1-z),\quad
F_{o}(z)=F_o+C_oz(1-z),\quad
F_m(z)=(1-z)F_s+zF_o+C_mz(1-z).
\]
Two direct simplifications show strict internal concavity and internal maximizers:
\[
C_d=\frac{n^2h^2(n-3)}{2d}>0,
\]
\[
C_m-(F_s-F_o)=\frac{(n-3)[n^2h-2nh+2n+2(h-1)^2]}{2d}>0,
\]
\[
C_m+(F_s-F_o)=\frac{(n-3)(n^2+2h-2)}{2n}>0.
\]
Also \(C_o=[n^3-3n^2+2nh-2n-4h+4]/(2n)>0\) for \(n\ge4,h>0\). The peak values are therefore precisely \(M_d,M_o,M_m\). Their maximizing locations are as stated.

**4. Global orbit comparison.** Write \(\Delta=F_s-F_o\) and
\[
T=n^3h-2n^2h+2n^2+2nh^2-3nh+n-2h^2+4h-2>0.
\]
In fact \(T=2ndC_m/(n-3)\), so positivity follows from the strict internal concavity established above.
Direct exact rational simplification gives
\[
M_d-M_o=\frac{(h-1)(n^3-n^2-4n-8)}{8n},
\]
\[
M_m-M_d=-\frac{n(n-3)(n+1)(h-1)[n^2h-nh+2n+2(h-1)^2]}{8T},
\]
and
\[
M_m-M_o=-\frac{(h-1)Q_n(h)}{8nT},
\]
where
\[
Q_n(h)=-n^4+n^3+12n^2-16
 +h(4n^3-12n^2-8n+32)+8(n-2)h^2.
\]
When \(h>1\), the first two comparisons show \(M_d\) strictly exceeds the other two. When \(0<h<1\), the distinguished edge is strictly below the ordinary–ordinary peak. For \(n\ge5\), the quadratic \(Q_n\) is strictly convex in \(h\), while
\[
Q_n(0)=-n^4+n^3+12n^2-16<0,\qquad Q_n(1)=n^3(5-n)\le0.
\]
Indeed, \(Q_5(0)=-216\) and \(\partial_n Q_n(0)=-n(4n^2-3n-24)<0\) for \(n\ge5\). Convexity then implies \(Q_n(h)<0\) for \(0<h<1\), hence \(M_m<M_o\). For \(n=4\),
\[
Q_4(h)=16(h^2+4h-1),\qquad
M_m-M_o=-\frac{(h-1)(h^2+4h-1)}{4(3h^2+12h+17)}.
\]
Its unique zero within \((0,1)\) is \(\sqrt5-2\), with the stated ordering. At \(h=1\), the graph is edge-transitive and all midpoints tie. This establishes the classification, sharp constant, and equality cases.

## Verification
The accompanying standalone `check_edge_defect.py` performs exact symbolic checks of the resistance formulas, edge-orbit coefficients, all three peak-difference identities, the \(n=4\) transition factor, and positive-factor reductions. It also reconstructs resistances of a subdivided finite network in exact rational arithmetic for representative dimensions and lengths, checking the edge-interpolation formula without relying on a floating-point fit. Finite checks are supplementary: the above algebraic identities and sign proof establish all integer \(n\ge4\) and real \(h>0\).

## Relationship to prior work
The effective-resistance, Dirichlet-energy, and Green-kernel framework is classical: Baker–Faber (first public preprint July 25, 2004, arXiv:math/0407428) develops the metric-graph electrical calculus, while Baker–Rumely (July 25, 2004, arXiv:math/0407427) develops general Green operators and the Dirichlet inner product. Cinkir (first public January 5, 2009, arXiv:0901.0407) studies the tau invariant under edge-length changes, including complete-graph calculations in the equilateral case. Those works provide general machinery and do **not** state the one-edge-defect sharp mean-zero arclength Sobolev maximizer classification or its exceptional \(\sqrt5-2\) threshold in the inspected sections. Takemura–Kametaka–Nagai studied sharp discrete Sobolev constants on weighted complete graphs, but their stated setting consists of vertex functions and finite Green matrices, not point evaluations along edges of a metrized graph equipped with arclength. Only the abstract and search-indexed exposition of that article were accessible here; potential concealed stronger coverage is an acknowledged literature risk. The comparison concerns theorem implications and assumptions, not title matching.

## Limitations
Only real continuous edgewise \(H^1\) functions with **unweighted mean-zero arclength** are treated. The result is not asserted for weighted mean measures, Robin conditions, spectral eigenvalue optimization, arbitrary multiple defective edges, or other graph families. Unindexed results or a derivation hidden in broader graph-theoretic formula collections could affect bibliographic priority; the classical resistance representation itself is not new. The proof is an ordinary analytic and algebraic argument, not an independent external certification.

## References
1. M. Baker and X. Faber, *Metrized graphs, electrical networks, and Fourier analysis*, arXiv:math/0407428 (first posted 2004-07-25), especially §§2–7. https://arxiv.org/abs/math/0407428
2. M. Baker and R. Rumely, *Harmonic analysis on metrized graphs*, arXiv:math/0407427 (first posted 2004-07-25), §§1–4 and examples. https://arxiv.org/abs/math/0407427
3. Z. Cinkir, *The tau constant of a metrized graph and its behavior under graph operations*, arXiv:0901.0407 (first posted 2009-01-05), especially §§2–3. https://arxiv.org/abs/0901.0407
4. K. Takemura, Y. Kametaka, and A. Nagai, *A Hierarchical Structure for the Sharp Constants of Discrete Sobolev Inequalities on a Weighted Complete Graph*, Symmetry 10 (2018), article 1; first online 2017-12-21, DOI:10.3390/sym10010001 (abstract inspected; full text unavailable).
