# A sharp third-order dependence law for arbitrary-length needles on a triangular grid

## Finding

Fix a planar equilateral triangular line grid and a directed line segment whose displacement, expressed in positively oriented unit lattice coordinates, is \(a e_1+b e_2\), with \(a,b\geq0\). Translate the segment uniformly modulo the lattice, with its direction held fixed. Write \(a=m+\alpha\), \(b=n+\beta\), \(a+b=r+\gamma\), with \(m,n,r\) integers and \(0\leq\alpha,\beta,\gamma<1\). Let \(N_1,N_2,N_3\) be the respective numbers of grid lines of the three directional families intersected, counting only transverse interior crossings.

The three counts are **pairwise independent**, for arbitrarily large \(a\) and \(b\), but in general are not jointly independent. Their complete multivariate probability generating function is

\[
\mathbb E\left[\prod_{j=1}^{3}z_j^{N_j}\right]
=z_1^m z_2^n z_3^r
\left[\prod_{j=1}^{3}(1-p_j+p_jz_j)
+\tau(\alpha,\beta)\prod_{j=1}^{3}(z_j-1)\right],
\]

where \((p_1,p_2,p_3)=(\alpha,\beta,\gamma)\), \(\gamma=\{\alpha+\beta\}\), and

\[
\tau(\alpha,\beta)=
\begin{cases}
\alpha\beta(1-\alpha-\beta),&\alpha+\beta\leq1,\\
-(\alpha+\beta-1)(1-\alpha)(1-\beta),&\alpha+\beta\geq1.
\end{cases}
\]

The two expressions agree at the shared boundary. In particular the mixed centered third moment equals \(\tau\) and obeys the **sharp two-sided inequality** \(-1/27\leq\tau\leq1/27\). Equality holds precisely for \((\alpha,\beta)=(2/3,2/3)\) and \((1/3,1/3)\), respectively.

If \(S=N_1+N_2+N_3\), then its centered-at-the-integer-part generating function is

\[
\mathbb E[z^{S-m-n-r}]=
(1-\alpha+\alpha z)(1-\beta+\beta z)(1-\gamma+\gamma z)
+\tau(z-1)^3.
\]

Let \(S_{\mathrm{ind}}\) have the law of \(m+n+r\) plus a sum of three independent Bernoulli variables with success probabilities \(\alpha,\beta,\gamma\). The *exact* total-variation distance between the true total-count law and the independent comparison is

\[
\operatorname{TV}\bigl(\mathcal L(S),\mathcal L(S_{\mathrm{ind}})\bigr)
=4|\tau(\alpha,\beta)|\leq4/27.
\]

The constant \(4/27\) is attained. The same exact distance holds between the full vector \((N_1,N_2,N_3)\) and the product of its three marginals. The segment visits exactly \(S+1\) elementary triangles almost surely, so the result also gives a full fixed-direction tile-visitation distribution.

## Assumptions and scope

Choose unit vectors \(e_1=(1,0)\), \(e_2=(1/2,\sqrt3/2)\). Every point has unique affine coordinates \(x=u e_1+v e_2\). The grid consists of the lines \(u\in\mathbb Z\), \(v\in\mathbb Z\), and \(u+v\in\mathbb Z\). The initial endpoint has \((u,v)\) distributed uniformly over \([0,1)^2\), the image of a lattice fundamental parallelogram under these coordinates; the displacement \((a,b)\) is deterministic and nonnegative. The random translate is Haar-uniform, not uniformly oriented. For other directions, a dihedral symmetry of the triangular grid reduces to this positive cone, with the line-family labels permuted. Tangencies, initial endpoints on grid lines, and passages through vertices are probability-zero and may be disregarded.

For an integer displacement in a coordinate, the associated fractional crossing indicator is almost surely zero; all formulas include such boundary cases. This is an exact fixed-displacement law, not an asymptotic theorem or a statement about a Poisson line process.

## Proof

Set \(U=\{u\}\), \(V=\{v\}\), and \(W=\{U+V\}\). Because \((U,V)\) is uniform on the two-dimensional torus, each of \((U,V)\), \((U,W)\), and \((V,W)\) has independent uniform coordinates. For example, conditional on \(U\), adding \(U\) modulo one preserves the uniform law of \(V\).

For any \(a=m+\alpha\geq0\), the number of integer levels of \(u\) crossed by the segment is \(m+I_1\), where \(I_1=\mathbf 1_{\{U>1-\alpha\}}\). Similarly

\[
N_1=m+I_1,\quad N_2=n+I_2,\quad N_3=r+I_3,
\]

with \(I_2=\mathbf 1_{\{V>1-\beta\}}\) and \(I_3=\mathbf 1_{\{W>1-\gamma\}}\). Hence \(I_j\) are Bernoulli with means \(p_j\), and any two of them are independent. In particular \(\operatorname{Cov}(N_i,N_j)=0\) for \(i\neq j\).

It remains to compute the one higher-order interaction not fixed by the one- and two-variable marginals. When \(\alpha+\beta\leq1\), the rectangle \(U>1-\alpha,V>1-\beta\) lies above \(U+V=1\), and throughout that rectangle \(\{U+V\}>1-\alpha-\beta\). Consequently

\[
\Pr(I_1=I_2=I_3=1)=\alpha\beta.
\]

When \(\alpha+\beta\geq1\), write \(\gamma=\alpha+\beta-1\). In that rectangle the event \(I_3=1\) comprises two right triangles in the \((U,V)\)-square: the strip from \(U+V=1-\gamma\) up to \(U+V=1\), and the triangle above \(U+V=2-\gamma\). Each has area \(\gamma^2/2\), hence

\[
\Pr(I_1=I_2=I_3=1)=\gamma^2.
\]

Because the pairwise covariances vanish, the centered third product is the triple-success probability minus \(\alpha\beta\gamma\), yielding the claimed two-branch formula for \(\tau\). Expanding the multivariate generating function in \(z_j-1\), the coefficients of all linear and quadratic products are fixed by the marginal and pairwise expectations, while the cubic coefficient differs from the independent product by exactly \(\tau\). This proves the full multivariate generating-function identity, including all eight configurations, not merely a moment identity. Setting \(z_1=z_2=z_3=z\) yields the scalar generating function.

For \(\alpha+\beta\leq1\), the three nonnegative quantities \(\alpha,\beta,1-\alpha-\beta\) sum to one. The arithmetic–geometric mean inequality gives \(0\leq\tau\leq1/27\) with equality only when all three equal \(1/3\). For \(\alpha+\beta\geq1\), the three nonnegative quantities \(1-\alpha,1-\beta,\alpha+\beta-1\) also sum to one, giving \(-1/27\leq\tau\leq0\), with equality only at \(\alpha=\beta=2/3\).

The correction polynomial \(\tau(z-1)^3\) changes the masses at \(0,1,2,3\) successes by \((-\tau,3\tau,-3\tau,\tau)\). Therefore the total-variation distance is half the sum of their absolute values, namely \(4|\tau|\). In the full eight-cell table the correction in each cell also equals \(\pm\tau\), and exactly four cells have each sign; its total variation is the same. A transverse line crossing changes the containing triangular tile exactly once. With probability one the three line families are not crossed simultaneously, so the segment visits \(S+1\) tiles. This completes the proof.

## Verification

The standalone checker `checks/triangular_crossing_check.py` reconstructs the eight joint cell probabilities from an independent exact-rational polygon clipping procedure for eight rational pairs \((\alpha,\beta)\), including both branches, sharp equality points and degenerate boundaries. It verifies normalization, all three marginals, all pairwise independences, the third-centered product, every coefficient of the scalar generating function, and the total-variation identity. It runs with the Python standard library: `python3 checks/triangular_crossing_check.py`. Expected output: `TRIANGULAR_LINE_CROSSING_THIRD_ORDER_RATIONAL_CHECK_OK 8 cases`. The proof is analytic and applies beyond the finitely checked parameters.

## Relationship to prior work

Bäsel's *Hitting Probabilities for Random Convex Bodies and Lattices of Triangles* (first publicly posted 2013-12-18) studies angle-averaged counts of triangles hit, under a size hypothesis ensuring the convex body can fit into an elementary cell (Theorem 2.1). Its introduction cites earlier work of Markov, Santaló and Pettineo on classical needle hitting probabilities. Those quoted angle-averaged, short-body formulas are not the present all-length, fixed-displacement **three-family joint law** or its sharp total-variation comparison. Bäsel's main theorem is not asserted to be new here.

Pettineo's *A Buffon type problem for triangular lattices* (1997) is the closest named historical priority risk because its available description expressly says it studies dependence among the three line-family hit events. Full text could not be inspected. The exact relationship of its fixed-angle calculations, if any, to the sharp conditional third-order and all-length law must be checked independently before claiming historical priority. Siniksaran's 2009 review treats triple-grid hitting and estimator efficiency, not this conditional all-length joint distribution. The 1976 Diaconis long-needle problem concerns parallel lines rather than the three-family dependence.

## Limitations

The direction is deterministic; integrating over random orientations introduces additional dependence and is outside the asserted formula. This result is for a periodic triangular line lattice, not an independently randomized line process. The accessible historical literature comparison supports no verified equivalent coverage, but full-text access to Pettineo (1997) failed, leaving nontrivial residual historical-priority risk. Independently checking the proof and originality remains necessary. Exact finite rational checks cannot prove an all-parameter claim; the latter rests on the analytic argument.

## References

1. U. Bäsel, *Hitting probabilities for random convex bodies and lattices of triangles*, arXiv:1312.5131v1 (publicly submitted 2013-12-18); *Applied Mathematical Sciences* 8 (2014), 8295–8307, doi:10.12988/ams.2014.411917.
2. M. Pettineo, *A Buffon type problem for triangular lattices*, *Rendiconti del Circolo Matematico di Palermo*, Serie II, Supplement 50 (1997), 289–298 (original full text unavailable).
3. L. A. Santaló, *Sur quelques problèmes de probabilités géométriques*, *Tôhoku Mathematical Journal* 47 (1940), 159–171 (referenced in Bäsel, historical comparison not fully inspected).
4. E. Siniksaran, *Throwing Buffon's Needle with Mathematica*, *The Mathematica Journal* 11 (2009), online 2009-01-12, https://www.mathematica-journal.com/2009/01/12/throwing-buffons-needle-with-mathematica/.
