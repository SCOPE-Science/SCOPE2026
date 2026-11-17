# A sharp length-conditioned alignment phase diagram for random closed planar polygons

## Finding
For each integer \(n\ge4\), take a Haar-uniform real \(n\)-by-\(2\) orthonormal frame. Square its complexified rows to obtain a closed planar polygon of perimeter \(2\). The conditional direction law of any two distinct labelled edges at their fixed positive lengths is explicit. Remarkably, its alignment depends qualitatively on the edge count: pentagons have uniformly distributed relative directions whenever the two lengths sum to less than one, quadrilaterals favor parallel directions in that regime, and all polygons with at least six edges favor antiparallel directions. For two longer edges in a quadrilateral the alignment preference reverses exactly once, at a universal elliptic-integral threshold.

Let \(s,t\in(0,1)\) be the two edge lengths and let \(\psi\in[0,2\pi)\) be their oriented relative direction. Put
\[
D_{s,t}(\psi)=1-s-t+\frac{st}{2}(1-\cos\psi),\qquad p_n=\frac{n-5}{2}.
\]
For \(s+t\ne1\), the regular conditional density is
\[
f_n(\psi\mid s,t)=\frac{{\bf1}_{\{D_{s,t}(\psi)>0\}}D_{s,t}(\psi)^{p_n}}{\int_0^{2\pi}{\bf1}_{\{D_{s,t}(\phi)>0\}}D_{s,t}(\phi)^{p_n}\,d\phi}.
\]
This holds for every \(n\ge4\); the integrable singularities for \(n=4\) are part of the density. For fixed lengths, \(\cos\psi\) decreases strictly in likelihood-ratio order as \(n\) increases.

When \(s+t<1\), the sign of \(\mathbb E[\cos\psi\mid s,t]\) is positive, zero, negative for \(n=4\), \(n=5\), \(n\ge6\), respectively. When \(s+t>1\), it is negative for all \(n\ge5\). For \(n=4\), define \(q=(s+t-1)/(st)\in(0,1)\) and the complete elliptic integrals
\[
K(m)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{1-m\sin^2\theta}},\qquad E(m)=\int_0^{\pi/2}\sqrt{1-m\sin^2\theta}\,d\theta.
\]
Then the exact conditional mean is
\[
\mathbb E[\cos\psi\mid s,t,n=4]=1-2q\,\frac{E(1-1/q)}{K(1-1/q)}.
\]
It changes sign exactly once: positive for \(q<q_*\), zero at \(q=q_*\), and negative for \(q>q_*\), where
\[
2q_* E(1-1/q_*)=K(1-1/q_*),\qquad q_*\approx0.173885234015.
\]
The numerical value is illustrative; the exact integral equation and the uniqueness assertion define the constant.

## Assumptions and scope
The frame \(Q=(a_j,b_j)_{j=1}^n\) satisfies \(Q^{\mathsf T}Q=I_2\) and is uniformly distributed on \(V_2(\mathbb R^n)\). Define \(e_j=(a_j^2-b_j^2,2a_jb_j)\in\mathbb R^2\). Orthogonality gives \(\sum_j e_j=0\), while \(\sum_j\|e_j\|=\sum_j(a_j^2+b_j^2)=2\). All two distinct labelled edges have the same distribution by row-permutation symmetry, regardless of adjacency in a chosen polygon order. Statements about lengths refer to a regular conditional distribution, not a positive-probability point conditioning. The exceptional hypersurface \(s+t=1\) is omitted (it has zero probability). Positive lengths \(s,t<1\) are the interior feasible range.

## Proof
**1. The two-row marginal.** Let \(R\) be the first two rows of \(Q\), and write its remaining \(n-2\) rows as \(B\). In the constrained Euclidean volume measure on \(B\), the identity \(B^{\mathsf T}B=I_2-R^{\mathsf T}R\) contributes the matrix polar-coordinate Jacobian \(\det(I_2-R^{\mathsf T}R)^{((n-2)-3)/2}\). This is the standard real truncated-Stiefel (matrix beta) density. Thus, for every \(n\ge4\), the density of \(R\), with respect to its four Euclidean entries, is proportional to
\[
{\bf1}_{\{I_2-R^{\mathsf T}R>0\}}\det(I_2-R^{\mathsf T}R)^{(n-5)/2}.
\]
The exponent is valid even at \(n=4\); its boundary singularity is integrable by the Stiefel polar-coordinate formula.

**2. Edge coordinates and exact normalization.** Write the two rows as \(\sqrt{s}(\cos\alpha,\sin\alpha)\) and \(\sqrt{t}(\cos\beta,\sin\beta)\). Their Euclidean row-coordinate Jacobian is constant times \(ds\,dt\,d\alpha\,d\beta\); the polygon edge angles are twice the row angles, so \(\psi=2(\beta-\alpha)\pmod{2\pi}\). Direct determinant expansion gives
\[
\det(I_2-R^{\mathsf T}R)=1-s-t+st\sin^2(\beta-\alpha)=D_{s,t}(\psi).
\]
Integrating the free simultaneous rotation and summing the equal two-to-one angular preimages yields the displayed density after division by its explicit one-dimensional normalization integral. Since \(D_{s,t}(\pi)=(1-s)(1-t)>0\), every interior pair \(s,t\in(0,1)\) is feasible. For \(s+t>1\), the support is exactly \(\cos\psi<1-2(s+t-1)/(st)\). Squaring the closing-chain bound \(\|e_1+e_2\|\le2-s-t\) gives the identical angular cutoff; equality is of conditional measure zero.

**3. Ordered alignment and the pentagon transition.** For two edge counts \(m>n\ge4\), their conditional densities have ratio proportional to \(D_{s,t}(\psi)^{(m-n)/2}\), which is strictly decreasing as a function of \(z=\cos\psi\) because \(st>0\). This proves strict monotone likelihood-ratio, and hence stochastic, decrease of \(\cos\psi\). When \(s+t<1\), the support is the full circle and the \(n=5\) exponent vanishes, giving exact uniformity and zero cosine mean. Pairing angles with opposite cosines proves the quadrilateral mean positive and all \(n\ge6\) means negative. When \(s+t>1\), the \(n=5\) law is uniform on a proper arc centered at \(\pi\), with strictly negative cosine mean, and likelihood-ratio ordering gives negativity for larger \(n\).

**4. The unique quadrilateral threshold.** For \(n=4\) and \(s+t>1\), let \(q=(s+t-1)/(st)\), and substitute \(x=\sin^2(\psi/2)\). The conditional density of \(x\) is proportional to \([x(1-x)(x-q)]^{-1/2}\) on \(q<x<1\). Setting \(x=q+(1-q)v\), its density in \(v\in(0,1)\) is proportional to \([v(1-v)(q+(1-q)v)]^{-1/2}\). Writing \(v=\sin^2\theta\), the normalizing integral is \(2K(1-1/q)/\sqrt q\), while its \(x\)-weighted integral is \(2\sqrt q E(1-1/q)\). Therefore the conditional cosine mean \(1-2\mathbb E[x]\) equals the displayed elliptic expression.

For \(0<q_1<q_2<1\), the ratio of the \(v\) densities at \(q_2\) and \(q_1\) is, up to a constant, \(\sqrt{(q_1+(1-q_1)v)/(q_2+(1-q_2)v)}\), a strictly increasing function of \(v\). Hence \(v\) strictly increases in likelihood-ratio order as \(q\) increases. The map \(x=q+(1-q)v\) is strictly increasing in both \(v\) and \(q\) on their open domains, so \(\mathbb E[x]\) increases strictly. As \(q\downarrow0\), the normalizer diverges logarithmically at \(v=0\), forcing \(x\to0\) in probability. As \(q\uparrow1\), \(x\to1\) uniformly. The mean cosine therefore decreases continuously from \(+1\) to \(-1\), crossing zero exactly once. This proves existence, uniqueness and the sign classification, without relying on a numerical root finder.

## Verification
The standalone `checker.py` reconstructs independent Haar-real-Stiefel frames by Gaussian QR, verifies the determinant/edge-angle identity to machine accuracy, compares conditional cosine integrals against independent sampled frames for three edge counts, checks strict monotonicity and the \(n=5\) uniform law, and independently computes the elliptic threshold and its sign on both sides. It prints `STIEFEL_EDGE_ANGLE_CHECKS_OK` on success. Numerical work checks formulas and does not replace the proofs of the two-row marginal, stochastic order or threshold uniqueness.

## Relationship to prior work
The frame-to-polygon construction and single-edge beta marginals are due to Cantarella, Deguchi and Shonkwiler (arXiv:1206.3161, first public June 14, 2012). Their discussion explicitly calls for improved understanding of joint edge-length and dot-product correlations. General matrix-beta/truncated-Stiefel calculus supplies the two-row marginal used here; no originality is claimed for that general density. Cantarella, Grosberg, Kusner and Shonkwiler (arXiv:1210.6537, October 24, 2012), Proposition 22, derive a two-edge density and turning-angle expectation for the **spatial** symmetric measure, not this real-Stiefel planar conditional sign classification. Cantarella, Needham, Shonkwiler and Stewart (arXiv:1702.01027, February 1, 2017) analyze the planar Grassmann model and quadrilateral types, but do not report the all-edge-count conditional angular family or the universal elliptic alignment boundary. The contribution is the full **planar conditioned directional law and its sign/ordering phase diagram**, not the model definition, the general matrix-beta marginal, nor spatial curvature results.

## Limitations
The probability model is the symmetric Haar-Stiefel measure, not independently sampled edge directions or uniformly sampled polygon vertices, and requires \(n\ge4\). There is no assertion about conditioning on the probability-zero hypersurface \(s+t=1\). Relative directions are labelled edge-vector directions; internal turning angles have the conventional supplementary-angle adjustment when traversing polygon vertices. The numerical approximation of \(q_*\) is not an independently validated certified interval. The work has undergone only self-review, not independent mathematical validation. Priority against all classical literature remains provisional.

## References
- J. Cantarella, T. Deguchi and C. Shonkwiler, *Probability Theory of Random Polygons from the Quaternionic Viewpoint*, arXiv:1206.3161, first submitted June 14, 2012. https://arxiv.org/abs/1206.3161
- J. Cantarella, A. Grosberg, R. Kusner and C. Shonkwiler, *The Expected Total Curvature of Random Polygons*, arXiv:1210.6537, first submitted October 24, 2012. https://arxiv.org/abs/1210.6537
- J. Cantarella, T. Needham, C. Shonkwiler and G. Stewart, *Random Triangles and Polygons in the Plane*, arXiv:1702.01027, first submitted February 1, 2017. https://arxiv.org/abs/1702.01027
