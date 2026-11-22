# Exact Euclidean distance law and Gaussian fluctuations for zigzag unit-flow polytope vertices

## Finding
For every integer \(n\ge 1\), consider the standard edge-coordinate unit-flow polytope \(\mathcal F_n\) of the directed graph with vertices \(0,1,\ldots,n\), unit-step edges \(i\to i+1\), and double-step edges \(i\to i+2\) whenever those endpoints exist. Let \(X_n,Y_n\) be two independent uniformly chosen vertices, and put \(D_n=\|X_n-Y_n\|_2^2\). Write \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\). There are exactly \(F_{n+1}\) vertices.

The full finite-distance distribution is determined by the ordered-pair polynomial \(H_n(z)=F_{n+1}^2\mathbb E[z^{D_n}]\), whose bivariate generating function is
\[
\boxed{\sum_{n\ge1}H_n(z)t^n=\frac{t\bigl(1+t(1-z+2z^3)-t^2z\bigr)}{1-(1+z)t-(1-z+2z^3)t^2+zt^3}.}
\]
Consequently all coefficients are nonnegative integers and the finite-dimensional Euclidean squared-distance law is exactly \(\mathbb P(D_n=k)=[z^k]H_n(z)/F_{n+1}^2\).

The squared-distance and ordinary-distance fluctuation laws are
\[
\boxed{\frac{D_n-2n/\sqrt5}{\sqrt n}\ \xrightarrow{\mathrm d}\ N\!\left(0,\frac{18\sqrt5-20}{25}\right)}
\qquad\text{and}\qquad
\boxed{\|X_n-Y_n\|_2-\sqrt{\frac{2n}{\sqrt5}}\ \xrightarrow{\mathrm d}\ N\!\left(0,\frac{9-2\sqrt5}{20}\right).}
\]
The two normal variances are strictly positive. The second theorem has no additional fluctuation normalization: the ordinary Euclidean distances fluctuate on a constant scale.

## Assumptions and scope
The graph is the original, uncontracted zigzag directed graph with exactly \(n\) short edges and \(n-1\) long edges; edge-incidence coordinates in \(\mathbb R^{2n-1}\) are orthonormal. Flow is nonnegative with one unit sent from vertex \(0\) to vertex \(n\), with conservation at interior vertices. Sampling is independent and uniform over **vertices**, not over volume in the polytope or over objective directions. Equal path choices are allowed and contribute distance zero. Statements cover every integer \(n\ge1\), and the convergence is as \(n\to\infty\).

## Proof
**1. Vertex/path correspondence.** A nonnegative unit flow on an acyclic directed graph decomposes into a convex combination of source-to-sink directed path incidence vectors. Conversely, a path incidence vector is extreme: if it is a convex combination of other nonnegative path vectors, its zero coordinates force all component paths to avoid those edges, and its coordinates equal to one force every component path to use all its edges. Hence the vertices of \(\mathcal F_n\) are exactly the directed \(0\)-to-\(n\) paths. Their short/double-step word compositions obey the Fibonacci recurrence and are counted by \(F_{n+1}\). For two \(0\)-\(1\) incidence vectors the squared Euclidean distance equals the cardinality of the symmetric difference of their edge sets.

**2. Four-state exact transfer.** At each integer vertex index \(i\) before the sink, record whether the first and second path visit \(i\). The four states, in order, are \((0,0),(0,1),(1,0),(1,1)\). A path currently visiting \(i\) chooses a short or long outgoing edge, whereas one bypassing \(i\) is forced to visit \(i+1\). At \(i\le n-2\) the polynomial-weighted transition is
\[
T(z)=\begin{pmatrix}
0&0&0&1\\
0&0&z&z\\
0&z&0&z\\
1&z^2&z^2&1
\end{pmatrix}.
\]
Every selected outgoing edge contributes one to the exponent, except that a shared selected edge is counted zero in the symmetric difference. At the final pre-sink vertex \(n-1\), long jumps are forbidden, giving
\[
B(z)=\begin{pmatrix}
0&0&0&1\\
0&0&0&z\\
0&0&0&z\\
0&0&0&1
\end{pmatrix}.
\]
With \(e=(0,0,0,1)^{\mathsf T}\), both paths start present and finish at the sink, so the ordered-pair polynomial is **exactly** \(H_n(z)=e^{\mathsf T}T(z)^{n-1}B(z)e\). For example, \(H_1(z)=1\), \(H_2(z)=2+2z^3\), and \(H_3(z)=3+4z^3+2z^4\).

**3. Rational distribution function.** Formally summing the matrix geometric series gives
\[
\sum_{n\ge1}H_n(z)t^n=t\,e^{\mathsf T}(I-tT(z))^{-1}B(z)e.
\]
Taking the adjugate and determinant, and canceling the common linear factor, gives the stated cubic-denominator rational function. This is a formal power-series identity (no convergence hypothesis is needed). In particular, at \(z=1\), \(H_n(1)=F_{n+1}^2\); this also follows from the path enumeration.

**4. Fluctuations.** For \(z>0\) near one, \(T(z)\) is an irreducible primitive nonnegative matrix: the state \((1,1)\) has a self-loop and reaches all other states. Its Perron root \(\lambda(z)\) is analytic near one. Direct determinant expansion gives
\[
\det(\lambda I-T(z))=(\lambda+z)\left[\lambda^3-(1+z)\lambda^2-(1-z+2z^3)\lambda+z\right].
\]
The dominant root at one is \(\lambda(1)=(3+\sqrt5)/2\). Differentiating its cubic equation yields
\[
\lambda'(1)=1+\frac{3\sqrt5}{5},\qquad \lambda''(1)=\frac45+\frac{12\sqrt5}{25}.
\]
The positive starting/terminal vectors imply that, uniformly for complex \(s\) in a sufficiently small disc about zero,
\[
\mathbb E[e^{sD_n}]=c(s)\left(\frac{\lambda(e^s)}{\lambda(1)}\right)^{n-1}\bigl(1+O(\rho^n)\bigr),\qquad c(0)=1,
\]
for some analytic nonzero \(c\) and \(0<\rho<1\) (the harmless endpoint normalization is incorporated in \(c\)). Thus the first two derivatives at zero of \(\log\lambda(e^s)\) are
\[
\mu=\frac{\lambda'(1)}{\lambda(1)}=\frac{2}{\sqrt5},\qquad
\sigma^2=\mu+\frac{\lambda''(1)}{\lambda(1)}-\mu^2=\frac{18\sqrt5-20}{25}>0.
\]
Expanding the characteristic function at \(s=iu/\sqrt n\) proves \((D_n-\mu n)/\sqrt n\xrightarrow{\mathrm d}N(0,\sigma^2)\). By the continuous mapping and delta methods, \(D_n/n\to\mu\) in probability and
\[
\sqrt{D_n}-\sqrt{\mu n}\xrightarrow{\mathrm d}N\!\left(0,\frac{\sigma^2}{4\mu}\right),\qquad
\frac{\sigma^2}{4\mu}=\frac{9-2\sqrt5}{20}.
\]
All claims follow.

## Verification
The standalone `verify_zigzag_flow.py` enumerates every source-to-sink path and every ordered path pair for \(1\le n\le12\) and compares edge-symmetric-difference distances against the transfer matrix using exact integer counts. It also verifies the rational generating-function recurrence through \(n=40\), with no numerical tolerance and no third-party packages. Run `python3 verify_zigzag_flow.py`. These finite checks test the implementation and formulas; they are not a substitute for the all-dimensional transfer proof or Perron-root argument.

## Relationship to prior work
Brunner and Hanusa introduced and analyzed triangulations, groves and lattice statistics of the zigzag flow polytope. González D'León, Hanusa, Morales and Yip established spinal-graph/column-convex connections and Fibonacci vertex counts. These results do not supply the canonical *edge-coordinate Euclidean* distribution between independently and uniformly sampled vertices. Their integral equivalences to order polytopes do not preserve Euclidean distances. Klavžar and Mollard derived the Hosoya polynomial of Fibonacci cubes, which measures shortest-path/Hamming distances in their **binary-string coordinates**, a different metric: the two directed paths on \(0,1,2\) have squared edge-incidence separation three although their single long-step indicators differ in just one coordinate. Therefore that known distance polynomial does not imply this one.

## Limitations
The results concern the uncontracted unit-flow embedding, not a contracted integrally equivalent graph, a different scaling of edge coordinates, arbitrary zigzag order-polytope realizations, or uniform interior-volume sampling. The result makes no statement about Euclidean spectra for other distance graphs. Historical priority is not independently certified; an unindexed equivalent transfer calculation remains possible.

## References
1. R. Brunner and C. R. H. Hanusa, *A Triangulation of the Flow Polytope of the Zigzag Graph*, arXiv:2406.20048, first submitted 2024-06-28, https://arxiv.org/abs/2406.20048.
2. R. S. González D'León, C. R. H. Hanusa, A. H. Morales and M. Yip, *Column-Convex Matrices, G-Cyclic Orders, and Flow Polytopes*, arXiv:2107.07326, first submitted 2021-07-15, https://arxiv.org/abs/2107.07326.
3. S. Klavžar and M. Mollard, *Wiener Index and Hosoya Polynomial of Fibonacci and Lucas Cubes*, MATCH Commun. Math. Comput. Chem. 68 (2012), 311–324, https://users.fmf.uni-lj.si/klavzar/preprints/MATCH68%281%29_311-324.pdf.
4. OEIS A246173, the Fibonacci-cube shortest-path-distance triangle, https://oeis.org/A246173.
