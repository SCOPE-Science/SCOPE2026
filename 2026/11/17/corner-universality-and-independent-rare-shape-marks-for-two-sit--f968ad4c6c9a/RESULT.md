# Corner universality and independent rare-shape marks for two-site rectangle Voronoi cells

## Finding
Let \(K\) be any fixed Euclidean rectangle of positive side lengths \(L_1,L_2\) and area \(S=L_1L_2\). Sample independent area-uniform sites \(X,Y\) in \(K\), and let \(T\) be the smaller area of the two ordinary Euclidean nearest-site Voronoi cells clipped to \(K\). Then
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-2}\Pr(T/S<\varepsilon)=\frac83.
\]
The coefficient is independent of the rectangle's aspect ratio. More strongly, the complete conditional rare-cap coordinates defined below converge jointly in total variation to a product of four explicit laws and two independent discrete labels.

## Assumptions and scope
The rectangle is fixed with \(0<L_1,L_2<\infty\). Points have independent normalized Lebesgue area distribution; ties and coordinate degeneracies have probability zero. Each cell consists of points of \(K\) closer in Euclidean distance to one of the two sites. The minimum cell has area \(T\).

For a sufficiently small-area cell, choose its corner \(c\) (the unique corner of \(K\) inside that cap, apart from a negligible face-truncation event). Reflect the coordinate axes so that the corner has coordinates \((0,0)\) and the rectangle is \([0,L_1]\times[0,L_2]\). Let the two ordered site coordinates, from the smaller-cell site to the other, be \((a-p,b-q)\) and \((a+p,b+q)\); on the triangular-cap event \(0<p<a<L_1-p\), \(0<q<b<L_2-q\). Put \(t=\varepsilon S\) and define
\[
\eta=T/t,\qquad \xi=\frac{ap}{ap+bq},\qquad
\ell=\frac12\log\frac{bp}{aq},\qquad
j=\left(\max\left\{\frac pa,\frac qb\right\}\right)^2.
\]
For the exceptional nontriangular event, set these marks by any fixed measurable convention; its conditional probability tends to zero. The limiting joint law of \((\eta,\xi,\ell,j,c,\text{smaller-site label})\), given \(T<t\), is the independent product
\[
\operatorname{Beta}(2,1)\otimes\operatorname{Beta}(2,2)
\otimes\operatorname{Laplace}(0,\tfrac12)
\otimes\operatorname{Unif}(0,1)
\otimes\operatorname{Unif}(\{1,2,3,4\})
\otimes\operatorname{Unif}(\{1,2\}).
\]
Here \(\operatorname{Laplace}(0,1/2)\) denotes density \(u\mapsto e^{-2|u|}\) on the real line. In particular the first four continuous limiting marks are independent.

## Proof
Use one corner, orient its inward directions positively, and one choice of smaller-cell site label. Define \(r=p/q>0\) and the corner-facing bisector
\[
pu+qv=pa+qb.
\]
Its axis intercepts are \(U=a+b/r\) and \(V=b+ra\). When \(U<L_1\) and \(V<L_2\), the smaller cap is precisely a corner triangle, of area
\[
T=UV/2=\tfrac12(a\sqrt r+b/\sqrt r)^2.
\]
The two sites are inside the rectangle exactly when \(p<a<L_1-p\) and \(q<b<L_2-q\).

The configurations with a cap of area below \(t<S/2\) that reaches either nonadjacent side contribute \(O(t^4)\) in four-dimensional site-pair Lebesgue measure (with a constant depending on the fixed rectangle). To verify this, if \(U\ge L_1\), a cap of area below \(S/2\) requires \(V<L_2\), and the cap contains the triangle with base \(L_1\) and altitude \(V\). Thus \(V\le2t/L_1\). Consequently \(b\le V=O(t)\), \(q\le b=O(t)\), and \(r=V/U=O(t)\), so \(p=rq=O(t^2)\), while \(a\le L_1\). Integration over these four coordinates is \(O(t^4)\). The case \(V\ge L_2\) is symmetric. The event \(U\ge L_1, V\ge L_2\) would contain a triangle of area \(S/2\) and cannot occur when the cap is smaller than \(t<S/2\). There are eight corner/label classes and no further classes for sufficiently small caps.

It suffices to integrate the unbounded homogeneous positive wedge in coordinates \((a,b,p,q)\), subject to \(p<a\), \(q<b\), and \((a\sqrt r+b/\sqrt r)^2<2t\), and then impose the fixed-rectangle upper bounds. Set
\[
A=a\sqrt r,\quad B=b/\sqrt r,\quad p=rq,\quad c=\sqrt{2t}.
\]
The Jacobian has absolute value \(q\):
\[
da\,db\,dp\,dq=q\,dA\,dB\,dr\,dq.
\]
The wedge conditions are \(A,B>0\), \(A+B<c\), and \(0<q<Q\) where \(Q=\min(A/r^{3/2},B\sqrt r)\). Write \(r=\sqrt{A/B}\,\lambda\). Direct substitution yields
\[
Q^2\,dr=AB\min(\lambda,\lambda^{-3})\,d\lambda,
\qquad \int_0^\infty\min(\lambda,\lambda^{-3})\,d\lambda=1.
\]
Thus the wedge measure for one corner/label class is
\[
\frac12\int_{A+B<c}AB\,dA\,dB
=\frac{c^4}{48}=\frac{t^2}{12}.
\]
The linear transformation from two site positions to the coordinate means and half-differences has Jacobian \(4\). There are four corners and two equally weighted site labels, hence eight disjoint classes. Dividing by the sampling density's normalization \(S^2\), the total leading probability is \(8\cdot4\cdot t^2/(12S^2)=8t^2/(3S^2)\).

For the marked law put \(Z=A/c\), \(W=B/c\), \(R_0=1-Z-W\), and \(j=(q/Q)^2\). The normalized joint measure splits into the factors
\[
24ZW\,dZ\,dW\quad(Z,W>0,\ Z+W<1),\qquad
\min(\lambda,\lambda^{-3})\,d\lambda,\qquad dj.
\]
Therefore \((Z,W,R_0)\sim\operatorname{Dirichlet}(2,2,1)\), \(j\sim\operatorname{Unif}(0,1)\), and \(\lambda\) is independent with density \(\min(\lambda,\lambda^{-3})\). The standard beta factorization of the Dirichlet law gives \((Z+W)^2=\eta\sim\operatorname{Beta}(2,1)\) and \(Z/(Z+W)=\xi\sim\operatorname{Beta}(2,2)\) independently. Since \(\ell=\log\lambda\), its density is \(e^{-2|\ell|}\). The eight corner/label classes have the same measure by rectangular reflection and exchange of site labels.

Finally, the finite-rectangle constraints converge pointwise to no restriction under the scale \(A,B=O(\sqrt t)\), except on a set of limiting measure zero, and their indicators are bounded by the integrable homogeneous density just computed. Dominated convergence gives convergence of the normalized marked densities in \(L^1\); the face-truncated cases have vanishing conditional probability. This proves the stated total-variation limit.

## Verification
The accompanying standalone `check.py` uses a separate polygon-clipping algorithm and an algebraic clipped-cap formula to compare 300 randomly generated two-site rectangles. It checks the rational prefactor, runs 2,000,000 independent simulated site pairs for both a square and a \(4:1\) rectangle, and tests the conditional means and symmetry predicted by the four continuous limit distributions. Execute with `python check.py` after installing `numpy` from `requirements.txt`. These are finite numerical checks and do not replace the preceding proof.

## Relationship to prior work
Devroye, Györfi, Lugosi, and Walk (2015) analyze measures of Voronoi cells in the many-site regime; their results do not directly imply this fixed-two-site rectangle small-minimum law or its conditional geometric marks. Beermann, Redenbach, and Thäle (2012) study the shapes of small Poisson line-tessellation cells, a different stochastic geometry. Koufos and Dettmann (2016) consider cells in bounded Poisson Voronoi tessellations, principally pinned typical-cell areas and moments rather than two random sites. Le Caër's random-ball circumcenter formulas address a related two-site midpoint/separation transformation in balls, not the corner-defined rectangle event. A public discussion asking for average smallest Voronoi cell areas reflects interest but provides no prior theorem. No searched source identified a result covering the entire displayed statement; historical priority remains provisional.

## Limitations
The rectangle is fixed and nondegenerate; no uniformity is asserted as its aspect ratio changes with \(t\). No quantitative rate for convergence of the marked law is established. No result for three or more sites or other polygon angles is asserted. Total variation refers to the six displayed marks and labels, not to the unscaled original site-pair distribution. Literature search is not a proof of novelty; more obscure exact finite-site formulae remain a risk. Independent mathematical validation has not been performed.

## References
1. Devroye, Györfi, Lugosi, and Walk, *On the measure of Voronoi cells* (first posted 2015-12-14), https://arxiv.org/abs/1512.04267.
2. Beermann, Redenbach, and Thäle, *Asymptotic shape of small cells* (2012), https://arxiv.org/abs/1211.5488.
3. Koufos and Dettmann, *Distribution of Cell Area in Bounded Poisson Voronoi Tessellations with Application to Secure Local Connectivity* (first posted 2016-12-07), https://arxiv.org/abs/1612.02375.
4. Le Caër, *Circumspheres of sets of \(n+1\) random points in the \(d\)-dimensional Euclidean unit ball* (2018 preprint), https://arxiv.org/abs/1803.08484.
5. *What is the average area of the smallest region in a Voronoi diagram?* (2025 public discussion), https://math.stackexchange.com/questions/5033119/what-is-the-average-area-of-the-smallest-region-in-a-voronoi-diagram.
