# A sharp pendant-edge localization threshold for Sobolev evaluation on parallel-path graphs

## Finding
For each integer \(r\ge3\), join two vertices \(u,v\) by \(r\) internally disjoint unit-length edges, and attach a single pendant edge of length \(h>0\) to \(u\). Denote the resulting compact metric multigraph by \(G_{r,h}\). Define the real Hilbert space
\[
\mathcal H_{r,h}=\{f\in C(G_{r,h}): f|_e\in H^1(e)\text{ for every edge},\quad \int_{G_{r,h}}f\,ds=0\},
\qquad \|f\|_{\mathcal H}^2=\int_{G_{r,h}}|f'|^2\,ds.
\]
Here \(ds\) is **unnormalized arclength**, and continuity is imposed at every vertex. Set
\[
L=r+h,\quad k=r-2+\frac{r-1}{r}h,\quad
F_0=\frac{r+2}{6}+\frac{h^2}{2},\quad
J=\frac{r^2+(r+2)h+3rh^2+h^3}{3}.
\]
Then the exact squared norm of the embedding \(\mathcal H_{r,h}\hookrightarrow C(G_{r,h})\) is
\[
\boxed{\ C_{r,h}^2=\frac{F_0+\max\!\left\{rh,\frac{(r-2+h)^2}{4k}\right\}}{L}-\frac{J}{2L^2}.\ }
\]
There is exactly one positive transition length,
\[
\boxed{\ h_r=\frac{(r-2)\bigl(2\sqrt{r^2-1}-2r+1\bigr)}{4r-5}.\ }
\]
For \(0<h<h_r\), the **only norm-maximizing evaluation points** are the \(r\) points, one on each unit edge, at distance
\[
\boxed{\ x_r(h)=\frac{r-2+h}{2\left(r-2+(r-1)h/r\right)}\ }
\]
from \(u\). For \(h>h_r\), the pendant endpoint is the **only** maximizing evaluation point. At \(h=h_r\), precisely those \(r+1\) points maximize. Thus growing a pendant edge produces a discontinuous switch from interior cyclic locations to the leaf tip, although \(C_{r,h}\) itself remains continuous. The transition lengths satisfy \(0<h_r<1\) and \(h_r\to1/4\) as \(r\to\infty\).

For every maximizing point \(x\), the complete nonzero equality class in the sharp Sobolev inequality \(\|f\|_\infty\le C_{r,h}\|f'\|_2\) consists of scalar multiples of its centered resistance Green representer \(G_x\), with either sign. At the transition there are \(r+1\) such one-dimensional families.

## Assumptions and scope
The parameters are an integer \(r\ge3\) and a real \(h>0\). All parallel edges have length exactly \(1\), with distinct interiors and common endpoints. The attached edge has length \(h\), with its other endpoint of degree one. Functions are real, continuous across vertices, edgewise Sobolev \(H^1\), and have zero **arclength** mean. The energy is the unnormalized derivative integral. The norm of the embedding is from this energy Hilbert space to the supremum norm on the entire continuum of graph points, not merely its vertex set. It is attained because the graph is compact and point evaluations are continuous.

## Proof
**1. Resistance formula for point evaluations.** Write \(R(x,y)\) for effective electrical resistance when each edge has resistance equal to its arclength. Define
\[
F(x)=\int_G R(x,y)\,dy,\qquad J=\int_G\int_G R(y,z)\,dy\,dz.
\]
The centered resistance kernel
\[
G_x(y)=-\tfrac12R(x,y)+\frac{F(x)+F(y)}{2L}-\frac{J}{2L^2}
\]
satisfies \(\int G_x=0\) and \(\int f'G_x'=f(x)\) for every \(f\in\mathcal H\). This follows from the unit-current characterisation of resistance, integration by parts, and polarization. In particular,
\[
\|\delta_x\|_{\mathcal H^*}^2=G_x(x)=\frac{F(x)}L-\frac{J}{2L^2}.
\]
The sharp supremum problem therefore reduces exactly to maximizing \(F\), and equality in Cauchy--Schwarz forces \(f\) to be proportional to \(G_x\).

**2. The resistance average is quadratic on each edge.** For a metrized graph of length \(L\), if an edge has length \(\ell\) and its complement connects its endpoints with effective resistance \(R_e\), the resistance-Laplacian identity gives the second derivative of \(F\) on the edge as
\[
F''(t)=2-\frac{2L}{\ell+R_e}.
\]
On bridges take \(R_e=\infty\), so \(F''=2\). This identity also follows directly from series--parallel reduction and integration of resistance over the graph. The required canonical-measure and resistance identities are in Baker--Faber (2004), Theorems 10--12, but the optimization below is specific to this graph.

For a unit parallel edge, the other \(r-1\) unit edges have effective resistance \(1/(r-1)\) between \(u,v\), and the pendant is electrically irrelevant to that two-terminal resistance. Thus the curvature is \(F''=-2k\), where
\[
k=\frac{L(r-1)}r-1=r-2+\frac{r-1}{r}h>0.
\]
For the pendant, the complement is disconnected and \(F''=2\).

**3. Determine all endpoint values and profiles.** For a point at distance \(t\in[0,1]\) from \(u\) along any unit parallel edge,
\[
R(u,t)=t-\frac{r-1}{r}t^2.
\]
Integrating over the \(r\) unit edges and the pendant gives
\[
F(u)=r\int_0^1\left(t-\frac{r-1}{r}t^2\right)dt+\int_0^h t\,dt
=\frac{r+2}{6}+\frac{h^2}{2}=F_0.
\]
The involution reversing the bare parallel-path bundle shows its contribution to \(F(v)-F(u)\) vanishes. For a point at pendant distance \(z\), \(R(v,z)-R(u,z)=R(u,v)=1/r\). The pendant contributes \(h/r\), so \(F(v)-F(u)=h/r\). By the curvature formula, on each unit edge
\[
F_{\rm path}(t)=F_0+\frac hr t+k t(1-t).
\]
On the pendant, at distance \(z\in[0,h]\) from \(u\), the bridge formula and series resistance give
\[
F_{\rm leaf}(z)=F_0+z^2+(r-h)z.
\]
This is convex. The tip has \(F_{\rm leaf}(h)=F_0+rh>F_0\), so no other pendant point can globally maximize.

For a unit edge, \(F_{\rm path}\) is strictly concave. Its unique maximum is at
\[
t=x_r(h)=\frac{k+h/r}{2k}=\frac{r-2+h}{2k};
\]
it lies strictly between \(1/2\) and \(1\), because \(r-2>0\) implies \(h/r<k\). The maximum value is \(F_0+(r-2+h)^2/(4k)\). This proves the stated complete list of candidate points and the formula for their larger \(F\)-value.

**4. Exactly one localization transition.** Compare the path profile with the pendant tip:
\[
D_h(t)=F_{\rm path}(t)-F_{\rm leaf}(h)
=kt(1-t)+\frac hr t-rh.
\]
For every \(0\le t\le1\),
\[
\partial_hD_h(t)=\frac{r-1}{r}t(1-t)+\frac tr-r
\le\frac{r-1}{4r}+\frac1r-r<0.
\]
Thus \(\max_{t\in[0,1]}D_h(t)\) is strictly decreasing in \(h\). At \(h=0\) it equals \((r-2)/4>0\); it becomes negative for large \(h\). At its unique zero the maximizing path point is interior, and the equality is
\[
4rhk=(r-2+h)^2,
\]
which reduces to
\[
(4r-5)h^2+2(r-2)(2r-1)h-(r-2)^2=0.
\]
Its unique positive root is exactly \(h_r\) as displayed above. Since the polynomial is negative at zero and positive at one, \(0<h_r<1\). Direct division of the radical expression by \(r\) yields \(h_r\to1/4\).

**5. Compute the constant \(J\).** With no pendant, \(F(u)=(r+2)/6\), and the unit-edge profile is \(F(u)+(r-2)t(1-t)\); integrating over all \(r\) edges gives \(J_{\rm bundle}=r^2/3\). The self-interaction of the pendant is \(\int_0^h\int_0^h|z-w|\,dz\,dw=h^3/3\). For two points on the pendant and on the bundle, resistance equals their pendant distance \(z\) plus \(R(u,t)\). Integrating both orientations gives \(rh^2+(r+2)h/3\). Therefore
\[
J=\frac{r^2}{3}+rh^2+\frac{(r+2)h}{3}+\frac{h^3}{3}.
\]
Substituting into Step 1 gives the exact constant. The representer characterization completes all equality statements.

## Verification
The standalone `checker.py` independently computes effective resistances of explicitly subdivided finite resistor networks using rational Laplacian inverses; exact Simpson integration on each polynomial segment then reconstructs \(F\). It checks multiple rational pendant lengths, three numbers of parallel edges, all edge classes, exact double integrals, and the critical radical identity for integer values \(3\le r<70\). The completed run printed `ALL_TWIGGED_BANANA_SOBOLEV_CHECKS_PASSED 103`. This finite checker tests the algebra and normalization; it is not used as an infinite-dimensional proof. The proof above handles all real \(h>0\) and all integers \(r\ge3\).

## Relationship to prior work
The resistance representation and the canonical-measure edge density are classical (Baker--Faber, arXiv:math/0407428, originally posted July 25, 2004; Baker--Rumely, arXiv:math/0407427). They are used as exact inputs, not claimed as new. The ungrafted parallel-path case and separately joined loop bouquets have different network structures and do not supply the pendant-grafted sharp localization threshold. Here the graft breaks the pole-reversal symmetry but retains the parallel-path degeneracy. The claim here is only the complete **grafted** norm, threshold, and equality-location classification, not a new general resistance formula.

## Limitations
The parallel edges must all have length one; a single pendant edge is grafted at one shared endpoint. The theorem does not classify unequal parallel lengths, multiple grafts, nonuniform arclength weights, higher-order Sobolev norms, or other graph topologies. The manuscript establishes a same-source mathematical derivation and finite exact diagnostics; independent review has not been performed.

## References
1. Matthew Baker and Xander Faber, *Metrized graphs, electrical networks, and Fourier analysis*, arXiv:math/0407428 (first public version July 25, 2004). In particular, Theorems 10--12 on effective resistance and canonical measure. https://arxiv.org/abs/math/0407428
2. Matthew Baker and Robert Rumely, *Harmonic analysis on metrized graphs*, arXiv:math/0407427 (first public version July 25, 2004). Its Green-kernel and electrical-network foundations are used for normalization. https://arxiv.org/abs/math/0407427
3. Michael Solomyak, *On approximation of functions from Sobolev spaces on metric graphs*, Journal of Approximation Theory 121 (2003), 199--219. Background on graph Sobolev embeddings; no sharp pendant-multipath localization formula is asserted here. https://doi.org/10.1016/S0021-9045(03)00033-9
