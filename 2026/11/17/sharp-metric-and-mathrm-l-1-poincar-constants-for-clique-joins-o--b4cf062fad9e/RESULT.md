# Sharp metric and \(\mathrm L^1\) Poincaré constants for clique joins of balanced bicliques

## Finding
For integers \(m\ge3\) and \(c\ge1\), let \(G_{m,c}=K_{m,m}\vee K_c\), the graph obtained by adjoining a \(c\)-vertex clique to every vertex of the balanced complete bipartite graph. Its two independent shores are \(A,B\), each of cardinality \(m\), and its universal clique is \(C\), of cardinality \(c\). Put
\[
N=2m+c,\qquad E_0=m^2+2mc+\binom c2,\qquad \rho=\frac{E_0}{\binom N2}.
\]
For a nonconstant map \(f\) of the vertices into any metric space, write
\[
R_G(f)=\frac{\binom N2^{-1}\sum_{\{u,v\}\subset V(G)}d(f(u),f(v))}{E_0^{-1}\sum_{\{u,v\}\in E(G)}d(f(u),f(v))}.
\]
(The denominator is positive because \(G\) is connected.) The sharp constant over **all metric targets** is
\[
\boxed{\gamma_{\mathrm{met}}(G_{m,c})=\rho\,\frac{3m+2c-2}{m+2c}.}
\]
The sharp constant over **all real \(\mathrm L^1\) targets** is
\[
\boxed{\gamma_{\mathrm L^1}(G_{m,c})=\rho\,\frac{2m+c-2}{m+c-1}.}
\]
Their ratio is strictly greater than one, with exact difference
\[
\boxed{\frac{\gamma_{\mathrm{met}}}{\gamma_{\mathrm L^1}}-1
=\frac{(m-1)(m-2)}{(m+2c)(2m+c-2)}.}
\]
For every optimal nonconstant real \(\mathrm L^1\) map, almost every nontrivial scalar level-set cut selects **one vertex of each shore and no clique vertex**, or its complement; conversely, this condition characterizes all optimal \(\mathrm L^1\) maps. In particular, adding even one universal vertex changes the optimal balanced cuts from the multiscale family permitted when \(c=0\) to singleton pairs and complements. The unrestricted metric case has the exact equality characterization in the proof below.

## Assumptions and scope
All graphs are finite, undirected, unweighted, and simple. The average in the numerator is over **distinct unordered pairs**, not all ordered pairs; the edge average is over unordered edges. A metric target may assign the same image to distinct graph vertices. A real \(\mathrm L^1\) target means \(\mathrm L^1(\Omega,\mu;\mathbb R)\) for an arbitrary measure space (finite-valued maps suffice for sharpness). The exponent on target distances is exactly one. The statement concerns \(m\ge3,c\ge1\), and claims no extension to general complete multipartite graphs or other exponents.

## Proof
**1. Metric bound.** For a map \(f\) write \(U_A\) and \(U_B\) for the sums of distances over all unordered pairs within shores \(A\) and \(B\), and \(D_{AB},D_{AC},D_{BC},D_{CC}\) for the sums over the indicated edges. Put \(U=U_A+U_B\), \(u=D_{AB}\), \(v=D_{AC}+D_{BC}\), \(w=D_{CC}\). The total numerator before normalization is \(U+u+v+w\), and the edge sum is \(u+v+w\).

Apply the triangle inequality to every pair of points of \(A\), with each vertex of \(B\) as intermediary. Summing counts every cross edge exactly \(m-1\) times, so \(mU_A\le(m-1)u\). The corresponding inequality with shores exchanged yields \(mU_B\le(m-1)u\); hence
\[
U\le \frac{2(m-1)}m u.
\]
Using each of the \(c\) clique vertices instead gives \(cU_A\le(m-1)D_{AC}\) and \(cU_B\le(m-1)D_{BC}\), whence
\[
U\le\frac{m-1}{c}v.
\]
For \(a=2(m-1)/m\) and \(b=(m-1)/c\), the elementary positive-cone bound \(\min(au,bv)\le ab(u+v)/(a+b)\) gives
\[
U\le\frac{2(m-1)}{m+2c}(u+v)
\le\frac{2(m-1)}{m+2c}(u+v+w).
\]
This yields the claimed upper bound after multiplying by \(\rho\). Sharpness: take a finite metric target consisting of \(2m+1\) distinct points \(a_1,\ldots,a_m,b_1,\ldots,b_m,o\); put all mutual distances within the \(a\)-family and within the \(b\)-family equal to two, and every remaining distance between distinct target points equal to one. This is a metric (the only nontrivial triangle inequalities are \(2\le1+1\)). Map shore vertices to their distinct named points and all clique vertices to \(o\). Then \(U=2m(m-1)\), \(u=m^2\), \(v=2mc\), \(w=0\), so equality holds.

**Metric equality.** For any nonconstant map, the displayed metric upper bound is equality if and only if (i) all clique vertices share an image, (ii) for every unordered pair in \(A\) and every vertex of \(B\cup C\), that intermediate image lies metrically between the two shore images, and (iii) the analogous condition holds for every pair in \(B\) and every vertex of \(A\cup C\). Necessity follows because all contributing triangle defects and the edge term \(w\) are nonnegative and each must vanish. Sufficiency follows by saturation of both triangle-sum inequalities, which imposes the balancing ratio \(au=bv=U\) and hence saturates their harmonic-mean bound.

**2. Real \(\mathrm L^1\) bound.** Every real \(\mathrm L^1\) metric on a finite vertex set is a nonnegative integral of scalar threshold-cut metrics, by \(|s-t|=\int_{\mathbb R}|\mathbf1_{s>h}-\mathbf1_{t>h}|\,dh\). It therefore suffices to determine the sharp ratio for nontrivial cuts. Let a cut select \(x\) points of \(A\), \(y\) points of \(B\), and \(z\) points of \(C\), with \(0\le x,y\le m\), \(0\le z\le c\). The number of crossing pairs that are nonedges is
\[
H=x(m-x)+y(m-y).
\]
If \(s=x+y+z\), the crossing-edge count is \(e=s(N-s)-H>0\). For fixed \(x,y\), \(e\) is strictly concave in \(z\); its minimum on \([0,c]\) lies at an endpoint, and a nontrivial cut with \(0<z<c\) cannot be optimal. Complementing a cut with \(z=c\) reduces it to \(z=0\). Thus take \(z=0\), when
\[
e=(m+c)(x+y)-2xy.
\]
Set \(\lambda=(m-1)/(m+c-1)\in(0,1)\), and let \(F(x,y)=H-\lambda e\). Direct expansion yields
\[
F(x+1,y+1)-F(x,y)=-2(1-\lambda)(x+y)
\]
whenever both increments are admissible. Also
\[
F(d,0)=d\bigl(m-d-\lambda(m+c)\bigr)<0
\quad\text{for every integer }1\le d\le m,
\]
since \(\lambda(m+c)>m-1\). The same holds for \(F(0,d)\). From any integer \((x,y)\), repeatedly remove matched pairs of selected vertices until reaching an axis. The increment identity then proves \(F(x,y)\le0\), with equality only at \((0,0)\) and \((1,1)\). The former is a trivial cut and is excluded. Therefore the largest nonedge-to-edge cut ratio is exactly \(\lambda\); its only nontrivial maximizing cardinalities are \((x,y,z)=(1,1,0)\) and the complementary \((m-1,m-1,c)\). Threshold integration gives the sharp \(\mathrm L^1\) constant and the claimed complete equality characterization. A scalar indicator of one vertex in each shore attains equality.

**3. Separation.** Cancelling \(\rho\) and expanding the two rational factors gives
\[
\frac{\gamma_{\mathrm{met}}}{\gamma_{\mathrm L^1}}-1=
\frac{(3m+2c-2)(m+c-1)-(m+2c)(2m+c-2)}{(m+2c)(2m+c-2)}
=\frac{(m-1)(m-2)}{(m+2c)(2m+c-2)}.
\]
This is positive for every \(m\ge3,c\ge1\). For fixed \(c\), the ratio tends to \(3/2\) as \(m\) tends to infinity; for fixed \(m\), it tends to one quadratically fast as \(c\) increases.

## Verification
An accompanying dependency-free Python checker performs exact-rational enumeration of all nontrivial cut cardinality triples for \(3\le m\le12\) and \(1\le c\le9\), confirming both the sharp bound and the unique optimal cardinalities. It also checks each triangle inequality for the stated metric witness and confirms the rational constants. Its output is `JOINED_BICLIQUE_EXACT_OK 90 parameter pairs; 43290 exact cuts; 409545 triangle inequalities`. This finite diagnostic is **not** the proof for all parameters; the preceding triangle-sum and cut-peeling arguments are the proof.

## Relationship to prior work
Polavarapu (arXiv:2611.05649, submitted 3 November 2026) gives target-space estimates for nonlinear Poincaré constants on regular expanders. The graphs here are not regular: shore degrees are \(m+c\), clique degrees are \(2m+c-1\). Consequently the stated regular-graph hypotheses do not directly supply the formulas above. For \(c=0\), the displayed formulas reduce algebraically to the balanced complete-bipartite boundary constants. The nonzero-clique equality classification, strict gap law, and quadratic vanishing under clique growth require separate proof. Standard cut decomposition is used only to reduce the real \(\mathrm L^1\) problem to exact finite-graph cuts, not to assert novelty. Related literature on complete multipartite negative type, Lipschitz variance, and cut-space projections addresses different invariants.

## Limitations
The exponent is one, the independent shore sizes are equal and at least three, and the extra vertices form a universal clique. The motivating paper was assessed using publicly available abstract and metadata; its full text was unavailable. Therefore no claim is made that its appendices or every earlier study of cut ratios have been exhaustively eliminated as priority risks. Results for higher exponents, arbitrary multipartite sizes, and independent external validation are not established.

## References
- Achintya Raya Polavarapu, *Linear Cotype Bounds for Nonlinear Spectral Gaps of Scalar Expanders*, arXiv:2611.05649 (initial submission 3 November 2026), https://arxiv.org/abs/2611.05649.
- Anupam Gupta, Ilan Newman, Yuri Rabinovich and Alistair Sinclair, *Cuts, trees and \(\ell_1\)-embeddings of graphs*, Combinatorica **24** (2004), 233–269, https://doi.org/10.1007/s00493-004-0015-x (background on cut metrics and graph embeddings; not asserted to state the theorem).
