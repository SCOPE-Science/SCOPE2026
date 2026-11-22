# Sharp cusp-diameter laws and parity-dependent sample extremes of hypocycloids

## Finding

Fix an integer \(n\ge3\), a generating-circle radius \(r>0\), and the ordinary \(n\)-cusped planar hypocycloid
\[
\Gamma_{n,r}=\{\gamma_{n,r}(t):0\le t<2\pi\},\qquad
\gamma_{n,r}(t)=r\bigl((n-1)e^{it}+e^{-i(n-1)t}\bigr).
\]
The full arclength and Euclidean diameter are, respectively,
\[
L_n=8r(n-1),\qquad D_n=2nr a_n,\qquad
a_n=\begin{cases}1,&n\text{ even},\\ \cos(\pi/(2n)),&n\text{ odd}.\end{cases}
\]
For independent arclength-uniform points \(X,Y\in\Gamma_{n,r}\), the sharp upper chord tail is
\[
\boxed{\Pr\bigl(\lVert X-Y\rVert>D_n-\varepsilon\bigr)
\sim C_n(\varepsilon/r)^2,\qquad
C_n=\begin{cases}
\dfrac{n}{32(n-1)^2},&n\text{ even},\\[5pt]
\dfrac{n}{16(n-1)^2\cos^2(\pi/(2n))},&n\text{ odd}.
\end{cases}}
\]
Thus the deltoid has coefficient \(C_3=1/16\), and the astroid has \(C_4=1/72\). Conditioned on a nearly maximal ordered chord, its ordered diametral cusp pair and two cusp-approach sides are asymptotically independent uniform labels. Let \(s_1,s_2\) be inward arclength distances from those cusps. The conditional law of
\[
\left(\frac{a_n s_1}{\varepsilon},\frac{a_n s_2}{\varepsilon},
1-\frac{a_n(s_1+s_2)}{\varepsilon}\right)
\]
converges in total variation to \(\operatorname{Dirichlet}(1,1,1)\), jointly with the uniform labels.

The same cusp mechanism yields the **full large-sample diameter limit**. If \(Z_1,\ldots,Z_N\) are independent arclength-uniform hypocycloid points and \(M_N=\max_{i<j}\lVert Z_i-Z_j\rVert\), then
\[
\boxed{\frac{2N}{a_n L_n}(D_n-M_N)
\xrightarrow{\mathrm d}W_n:=\min_{\{j,k\}\in E_n}(E_j+E_k),}
\]
where \(E_0,\ldots,E_{n-1}\) are independent unit-rate exponential variables, and \(E_n\) is the set of unordered pairs of maximally separated cusps. For even \(n\), the graph \(E_n\) is a perfect matching; hence
\[
\Pr(W_n>t)=\bigl(e^{-t}(1+t)\bigr)^{n/2}\quad(t\ge0).
\]
For odd \(n\), it is a single cycle of length \(n\), and consecutive diameter-pair sums share a cusp variable; for example
\[
\Pr(W_3>t)=4e^{-3t/2}-3e^{-2t}.
\]
For every odd \(n\), the exact finite-dimensional description is
\[
\Pr(W_n>t)=\int_{[0,\infty)^n}e^{-\sum_j x_j}
\prod_{\{j,k\}\in E_n}\mathbf1\{x_j+x_k>t\}\,dx_0\cdots dx_{n-1}.
\]
This parity distinction is not obtained by treating the pair deficits as independent.

## Assumptions and scope

The parameter \(n\) is a fixed integer at least three, \(r\) is fixed and positive, and sampling uses **normalized Euclidean arclength on the complete curve**, including both one-sided branches at each cusp. The random points are independent. All asymptotics are for \(\varepsilon\downarrow0\) at fixed \(n,r\) or \(N\to\infty\) at fixed \(n,r\), respectively; no joint uniformity in the cusp count is asserted. The ordered chord-cusp mark labels refer to the two ordered closest cusps under the near-diameter event, which are unambiguous for sufficiently small deficits. The graph of diametral cusps has \(n/2\) edges for even \(n\) and \(n\) edges for odd \(n\). Equality at a cusp has zero sampling probability.

## Proof

**1. Exact arclength and cusps.** Complex differentiation gives
\[
\gamma'_{n,r}(t)=ir(n-1)\bigl(e^{it}-e^{-i(n-1)t}\bigr),\qquad
\lvert\gamma'_{n,r}(t)\rvert=2r(n-1)\lvert\sin(nt/2)\rvert.
\]
Thus exactly the parameters \(t_j=2\pi j/n\), \(j=0,\ldots,n-1\), are cusps, with values \(v_j=nr e^{2\pi ij/n}\). Integration gives \(L_n=8r(n-1)\).

**2. Convex hull and exact diameter.** Each open cusp-to-cusp arc lies strictly inside the regular \(n\)-gon of vertices \(v_j\). Here is a direct verification. Divide by \(r\), rotate to the first arc \(0<t<2\pi/n\), and set \(\alpha=\pi/n\). The polar angle of \(\gamma_{n,1}(t)\) is nondecreasing, with derivative
\[
\frac{(n-1)(n-2)(1-\cos nt)}{(n-1)^2+1+2(n-1)\cos nt}>0
\quad(0<t<2\pi/n).
\]
It therefore lies in the angular wedge spanned by its endpoints. Its projection onto the outward normal of their joining side is
\[
F(t)=(n-1)\cos(t-\alpha)+\cos((n-1)t+\alpha).
\]
Since
\[
F'(t)=-2(n-1)\sin(nt/2)
\cos\bigl((n-2)t/2+\alpha\bigr),
\]
\(F\) strictly decreases and then increases on this arc, with \(F(0)=F(2\pi/n)=n\cos\alpha\). Consequently the arc lies strictly within the triangle with vertices \(0,v_0,v_1\), except at its cusps. Rotational symmetry completes the convex-hull description. The diameter of a regular \(n\)-gon of circumradius \(nr\) is \(D_n=2nr a_n\). By strict convexity of the Euclidean norm away from collinear coincidences and the strict interior placement of every noncusp arc point in the polygon, its only diametral pairs on the curve are the farthest cusp pairs. These are exactly the edges \(E_n\): opposite vertices when \(n\) is even, and \(\{j,j+(n-1)/2\}\) modulo \(n\) for each \(j\) when \(n\) is odd.

**3. Universal inward cusp loss.** For small signed \(u\), Taylor expansion at any \(t_j\) gives
\[
\gamma_{n,r}(t_j+u)=e^{it_j}\left(nr-\frac{rn(n-1)}2u^2
+i\frac{rn(n-1)(n-2)}6u^3+O_{n,r}(u^4)\right).
\]
The positive arclength distance from the cusp on either adjacent branch is
\[
s=r\frac{n(n-1)}2u^2+O_{n,r}(u^4).
\]
Thus the point is \(v_j-s e^{it_j}+O_{n,r}(s^{3/2})\), uniformly for both branch signs. For any ordered diametral pair \((j,k)\), the unit chord vector has projections \(a_n\) and \(-a_n\) along the outward radial unit vectors at the two cusps. Expanding the Euclidean distance therefore yields
\[
D_n-\lVert P_j(s_1)-P_k(s_2)\rVert
=a_n(s_1+s_2)+O_{n,r}\bigl((s_1+s_2)^{3/2}\bigr)
\]
uniformly in the four one-sided branch combinations. Since there are only finitely many maximizers and \(a_n>0\), compactness and this positive linear loss show that near-diametral pairs lie entirely within such small cusp-branch charts. In particular their inward arclengths are \(O_{n,r}(\varepsilon)\).

**4. Sharp pair probability and marks.** At a cusp each of the two incident branch intervals of length \(ds\) has probability \(ds/L_n\). For one ordered diametral cusp pair, the four branch combinations each contribute the area of the simplex \(a_n(s_1+s_2)<\varepsilon\), namely \(\varepsilon^2/(2a_n^2)\). The total is therefore \(2\varepsilon^2/(a_n^2L_n^2)+o(\varepsilon^2)\) per ordered cusp pair. There are \(n\) such ordered pairs for even \(n\), and \(2n\) for odd \(n\). Substituting \(L_n\) proves \(C_n\). The uniform \(O(\varepsilon^{3/2})\) remainder after dividing the loss by \(\varepsilon\) and rescaling \(s_i\) by \(\varepsilon/a_n\) makes the rescaled event indicators converge in \(L^1\) on a fixed bounded quadrant to the simplex indicator. Normalization converts this convergence to total variation of the conditional densities. Equal local leading arclength densities and symmetry give uniform independent labels and the Dirichlet law.

**5. Rare-sample cusp point processes.** Let \(S_{j,N}\) denote the smallest arclength distance from sampled points to cusp \(v_j\), counting both adjacent arcs. For any fixed nonnegative \(x_j\), the disjoint \(2x_jL_n/(2N)\)-length cusp neighborhoods imply
\[
\Pr\left(\frac{2NS_{j,N}}{L_n}>x_j\ \forall j\right)
=\left(1-\frac{\sum_jx_j}{N}\right)^N
\longrightarrow e^{-\sum_jx_j}.
\]
Hence the vector \((2NS_{j,N}/L_n)_j\) converges jointly to independent unit exponentials. Compactness and the strictly positive linear loss in step 3 imply that, with probability tending to one, any pair attaining sample diameter has both endpoints within \(O_p(N^{-1})\) arclength of diametral cusps. The nearest sample to each cusp furnishes the optimal first-order loss for each corresponding edge, and the remainder is uniformly \(o_p(N^{-1})\) because there are finitely many cusp neighborhoods. Consequently
\[
D_n-M_N=a_n\min_{\{j,k\}\in E_n}
(S_{j,N}+S_{k,N})+o_p(N^{-1}).
\]
Apply the continuous mapping theorem. The graph structure is immediate: even \(n\) produces disjoint opposite pairs, whereas for odd \(n\), the step \((n-1)/2\) is coprime with \(n\), giving one cycle. For an even matching, independent \(E_j+E_k\) have \(\operatorname{Gamma}(2,1)\) survival \(e^{-t}(1+t)\). For \(n=3\), the minimum edge sum is the sum of the two smallest of three exponentials; independence of exponential spacings gives \(2\operatorname{Exp}(3)+\operatorname{Exp}(2)\), yielding the displayed survival. For other odd sizes the stated integral follows directly from the joint exponential density. \(\square\)

## Verification

Run \`python3 verify_hypocycloid.py\` (standard library only). The checker re-evaluates the exact curve, cusp positions and arclength inversion, tests side containment and global diameter bounds at over twenty thousand deterministic coordinates, and independently integrates six positive-threshold pair-tail coefficients by midpoint quadrature using exact complex point separations and all four cusp branches. For the fixed test threshold \(\varepsilon=0.025r\), each numerical coefficient agrees with its theoretical limiting value to within \(0.4\%\) relative error. The script also checks finite-sample cusp distances and the tricuspoid exponential-cycle formula. Expected success marker: \`VERIFY_OK 21658 deterministic checks\`. These are finite confirmations; the proof above establishes all stated infinite limits and constants.

## Relationship to prior work

Classical geometry of hypocycloids and their arclength features is developed by Apostol and Mnatsakanian (2009), and the full family with arbitrary integer cusp count is addressed by Mani and Rubinstein-Salzedo (2015) in the different context of straightedge-and-compass arc division. Baez (2013) explicitly identifies the hypocycloid parametrization used here and its relationship to matrix traces. The new theorem concerns the exact geometric diameter, a probabilistic near-diameter chord law, its conditional cusp marks and the coupled extreme-sample limit; the cited results about cycloidal areas, roulettes, and constructibility do not imply those probability laws.

The older foundational geometric-extreme-value analysis by Wei Lao (2010), Chapter 5, proves the analogous sample-diameter weak limits for points sampled on regular **polygon edges**. Its even- and odd-polygon theorems involve independent nearest-to-vertex gaps along distinct straight side rays with different first-order projections. It is credited as the predecessor of the point-process method; simply substituting the convex hull of the hypocycloid would alter the sampling measure and its two cusp-branch projections. The single radial exponential per hypocycloid cusp, the resulting coefficients and its odd-cycle reduction require the local curve calculation given here. A related endpoint-cusp arc asymptotic for transverse cusp tangencies has a \(4/3\) power of the deficit; that hypothesis is not met here, because inward cusp arclength has a strictly positive longitudinal projection along a diametral chord.

Two particularly close published comparisons are *A coupled Poisson diameter law for odd regular polygons* (area-uniform points inside a fixed regular polygon) and *Parity-split polygon-to-circle crossover for almost-diametral boundary chords* (arclength points on regular polygon **edges** while the number of edges grows). Their full statements and proofs were compared. The present sampling is on **curved, inward-facing hypocycloid cusp arcs**, at fixed cusp count; its one-sided inward loss is linear in **arclength**, and the \(N\)-sample exponent and limiting corner processes differ from the area-uniform polygon law. Nor does a polygon-to-circle refinement determine fixed-cusp hypo­cycloid coefficients or the exponential vertex-cycle law. These are mathematical distinctions, not a certification of historical priority.

## Limitations

Only ordinary integer-cusp hypocycloids with \(n\ge3\), independent normalized Euclidean-arclength sampling, and fixed \(n,r\) are covered. The sample-limit graph law is not claimed for interior-area points, equiangular parameter sampling, rational noninteger rolling ratios, or all cusp-like plane curves. The comparison with classical 2009 cycloidal-area work was based on publicly accessible metadata and abstract, not the inaccessible full article; older unindexed treatments of stochastic chords could exist. Historical originality is provisional and independent mathematical audit remains unperformed.

## References

1. T. M. Apostol and M. A. Mnatsakanian, *New Insight into Cycloidal Areas*, American Mathematical Monthly 116(7) (2009), 598–611, DOI 10.4169/193009709X458573; public Caltech record dated 2009-12-04: https://authors.library.caltech.edu/records/7wxkh-b1h64 .
2. N. Mani and S. Rubinstein-Salzedo, *N-Division Points of Hypocycloids*, arXiv:1503.00566v1, first posted 2015-02-27; openly readable author text at https://paperzz.com/doc/9072457/%24-n-%24-division-points-of-hypocycloids .
3. W. Lao, *Some Weak Limit Laws for the Diameter of Random Point Sets in Bounded Regions*, KIT Scientific Publishing (2010), Chapter 5, Theorems 5.1 and 5.3, https://publikationen.bibliothek.kit.edu/1000019800/105664897 .
4. J. Baez, *Deltoid Rolling Inside Astroid*, American Mathematical Society, Visual Insight (2013-12-01), https://blogs.ams.org/visualinsight/2013/12/01/deltoid-rolling-inside-astroid/ .
5. *A coupled Poisson diameter law for odd regular polygons*, mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-coupled-poisson-diameter-law-for-odd-regular-polygons--5e3a52b5d3db .
6. *Parity-split polygon-to-circle crossover for almost-diametral boundary chords*, mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-parity-split-polygon-to-circle-crossover-for-almost-diametral-bo--f64acf954997 .
