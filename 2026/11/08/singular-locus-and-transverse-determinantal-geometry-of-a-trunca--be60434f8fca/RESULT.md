# Singular locus and transverse determinantal geometry of a truncated Grassmannian

## Finding

Let \(E\) and \(F\) be three-dimensional complex vector spaces, let \(V=E\oplus F\), and let
\[
G=\operatorname{Gr}(3,V)\subset\mathbb P(\bigwedge^3V)\cong\mathbb P^{19}.
\]
Set \(p=[\bigwedge^3F]\in G\), and let \(X\subset\mathbb P^{18}\) be the reduced closure of the linear projection of \(G\) away from \(p\). Equivalently, \(X\) is the truncated Grassmannian \(\operatorname{Gr}^{2}_{3}(\mathbb C^6)\), defined by retaining the Plücker coordinates involving at most two vectors of \(F\).

**Theorem.** The nine-dimensional variety \(X\) has reduced singular locus exactly
\[
S=\operatorname{Segre}(\mathbb P(E)\times\operatorname{Gr}(2,F))
\cong\mathbb P^2\times\mathbb P^2
\subset\mathbb P(E\otimes\bigwedge^2F)\cong\mathbb P^8.
\]
At every point of \(S\), a Zariski-open neighborhood of \(X\) is isomorphic to a Zariski-open neighborhood of the origin section of
\[
\mathbb A^4\times\{A\in\operatorname{Mat}_{2\times4}(\mathbb C):\operatorname{rank}A\leq1\}.
\]
In particular, the transverse singularity is the five-dimensional affine cone over \(\mathbb P^1\times\mathbb P^3\), with Hilbert series \((1+3t)/(1-t)^5\) and Hilbert–Samuel multiplicity \(4\). The variety \(X\) is normal and Cohen–Macaulay, and its projective degree is
\[
\deg X=41.
\]

## Assumptions and scope

All schemes and varieties are over \(\mathbb C\). The singular locus is asserted with its reduced structure. The local product is a statement about algebraic Zariski neighborhoods, not merely tangent cones or formal completions. The transverse multiplicity is the Hilbert–Samuel multiplicity of the local ring at the generic point of \(S\), equivalently the multiplicity of the rank-one determinantal cone at its vertex; the same transverse model holds at every point of \(S\).

## Proof

**1. Projection and the distinguished fourfold.** Choose bases \(e_1,e_2,e_3\) of \(E\) and \(e_4,e_5,e_6\) of \(F\). Write \(p_{ijk}\) for the usual Plücker coordinates of \(G\). Projection from \(p=[e_4\wedge e_5\wedge e_6]\) deletes precisely \(p_{456}\). Since the dense big cell consists of graphs \(E\to F\), its projected closure is the stated truncated Grassmannian.

For \(U\in G\), the Plücker line joining \(p\) to \([\bigwedge^3U]\) lies in \(G\) exactly when \(\dim(U\cap F)\geq2\). This is the standard classification of Plücker lines (two three-planes form such a line if and only if their intersection has dimension at least two). After deleting the pure \(F\)-coordinate, such a line projects to the point represented by \(u\wedge v\wedge w\), with \(0\ne u\in E\) and linearly independent \(v,w\in F\). Varying these data gives precisely \(S\), and \(S\) is homogeneous under \(GL(E)\times GL(F)\).

**2. An explicit chart at one point of \(S\).** Work in the target affine chart \(p_{156}=1\). The source Grassmannian chart has unique matrix representatives
\[
M=\begin{pmatrix}
1&0&0\\
a&d&g\\b&e&h\\c&f&i\\0&1&0\\0&0&1
\end{pmatrix}.
\]
The four affine target coordinates \(a=p_{256}\), \(b=p_{356}\), \(f=p_{146}\), and \(i=-p_{145}\) are free. Apply the invertible block-preserving shears \(e_1\mapsto e_1-ae_2-be_3\), \(e_5\mapsto e_5-fe_4\), and \(e_6\mapsto e_6-ie_4\). Because \(a,b,f,i\) are regular functions in this target chart, these shears and their inverses give an algebraic change of its coordinates over \(\mathbb A^4\). The source representative becomes
\[
M_0=\begin{pmatrix}
1&0&0\\0&d&g\\0&e&h\\c&0&0\\0&1&0\\0&0&1
\end{pmatrix}.
\]
Apart from the normalized coordinate \(p_{156}=1\), its only nonzero Plücker coordinates are
\[
\begin{aligned}
p_{123}&=dh-eg,&p_{125}&=-g,&p_{126}&=d,&p_{135}&=-h,&p_{136}&=e,\\
p_{234}&=c(dh-eg),&p_{245}&=cg,&p_{246}&=-cd,&p_{345}&=ch,&p_{346}&=-ce,
\end{aligned}
\]
plus the deleted \(p_{456}=c\). Set
\[
(x_1,x_2,x_3,x_4)=(d,e,g,h),\qquad
(y_1,y_2,y_3,y_4)=(cd,ce,cg,ch).
\]
All remaining retained coordinates are polynomials in \(x_j,y_j\): in particular \(p_{123}=x_1x_4-x_2x_3\) and \(p_{234}=x_1y_4-x_2y_3\). Thus the affine coordinate ring of the projected image, after adjoining the four free variables, is the closure of \(\{(x,cx):x\in\mathbb A^4,c\in\mathbb A^1\}\) times \(\mathbb A^4\).

The closure of \(\{(x,cx)\}\) is the full rank-at-most-one determinantal locus: the equations \(x_jy_k-x_ky_j=0\) cut out an irreducible reduced variety, and the parameterized subset with \(x\ne0\) is dense in it. Therefore the **exact** target affine ring is
\[
\mathbb C[a,b,f,i,x_1,\ldots,x_4,y_1,\ldots,y_4]
\big/\bigl(x_jy_k-x_ky_j:1\leq j<k\leq4\bigr).
\]
There is no appeal to a tangent-cone approximation. This equality also proves that the chart is normal and Cohen–Macaulay: rank-one generic determinantal rings have both properties, as can also be seen for normality from their realization as the invariants of the polynomial algebra on a pair of dimensions \(2\) and \(4\) under scalar \(\mathbb G_m\).

**3. The complete singular locus.** The rank-one \(2\times4\) matrix cone is smooth at its nonzero matrices: on a chart where an entry is invertible, the other row is uniquely proportional to the first. Its vertex is singular, since all the defining minors have zero differential at the origin. The singular locus in the above target chart is therefore exactly \(\{x=y=0\}\times\mathbb A^4\), which agrees with \(S\cap\{p_{156}\ne0\}\). The group \(GL(E)\times GL(F)\) acts transitively on \(S\), so this local model holds at **every** point of \(S\).

It remains to exclude singularities outside these charts. Let \(Y=\operatorname{Bl}_pG\). Projection extends to a proper birational morphism \(Y\to X\). The exceptional divisor maps isomorphically to the projectivized tangent space \(\mathbb P(T_pG)\cong\mathbb P^8\), which is the linear space containing \(S\). Every point of this space has a nonzero degree-two Plücker coordinate and hence lies in a chart of the kind just analyzed (by the block-group action). On its complement in \(X\), there is a preimage \(q\in G\setminus\{p\}\) such that the line \(pq\) is not contained in \(G\). Since the Grassmannian ideal is generated by Plücker quadrics, some Plücker quadric \(Q\) is nonzero on that line. As \(Q(p)=Q(q)=0\), the coefficient of the omitted coordinate in \(Q\) is nonzero at \(q\). One therefore solves the equation \(Q=0\) algebraically for that omitted coordinate near the image of \(q\), constructing a regular inverse to projection there. Thus the complement is smooth. This proves \(\operatorname{Sing}(X)_{\mathrm{red}}=S\).

**4. Multiplicity and degree.** The transverse rank-one cone has homogeneous coordinate ring of \(\mathbb P^1\times\mathbb P^3\), whose graded dimension in degree \(m\geq0\) is \((m+1)\binom{m+3}{3}\). Its Hilbert series is \((1+3t)/(1-t)^5\), so its Hilbert–Samuel multiplicity is \(1+3=4\).

Let \(H\) denote the Plücker hyperplane class on \(G\) and its pullback to \(Y\), and let \(D\) be the exceptional divisor of the blow-up at \(p\). The projected hyperplane class pulls back to \(H-D\). The projection is birational because it is an isomorphism off the above exceptional locus. On the ninefold \(Y\), all mixed products \(H^{9-j}D^j\) with \(0<j<9\) vanish, and \(\int_YD^9=(-1)^8=1\). The Plücker degree \(\int_GH^9=42\) follows from the \(3\times3\) rectangular hook-length formula. Hence
\[
\deg X=\int_Y(H-D)^9=42-1=41.
\]

## Verification

The included `verify.py` reconstructs all twenty Plücker minors from the original nine-variable matrix, applies the explicit block shears, tests every minor against the displayed normal form, and verifies all six rank-one determinantal equations identically over \(\mathbb Z\). It also checks the Hilbert-function identity in thirty-six degrees and the hook-length and blow-up degree arithmetic. Running `python verify.py` with SymPy installed produces `VERIFY_OK`. The symbolic checks substantiate the coordinate calculations; the infinite-dimensional geometric conclusions use the density, smoothness, and blow-up arguments in the proof, not finite enumeration.

## Relationship to prior work

Feigin and Makhlin (arXiv:2610.40891v1, October 29, 2026) define these truncated Grassmannians and study their representation-theoretic homogeneous coordinate rings. Feigin (arXiv:2604.00751v2) supplies general blow-up and collineation constructions. Their inspected full texts do not state this complete singular-locus, Zariski-local determinantal-type, uniform multiplicity, and degree classification for \(\operatorname{Gr}^{2}_{3}(\mathbb C^6)\).

The local rank-one determinantal model uses classical results concerning Segre varieties and determinantal rings; its normality and Cohen–Macaulay property are not claimed as novel abstract facts. Huang–Petroulakis–Sottile–Zelenko study Grassmannian projections with centers **disjoint** from the Grassmannian, inapplicable to the center \(p\in G\). Faulstich–Sturmfels–Sverrisdóttir compute degree \(41\) for a *different*, ten-dimensional truncation variety \(V_{\{1,3\}}\subset\mathbb P^{19}\); that number alone must not be taken as evidence of priority or novelty for this nine-dimensional projected variety. The present contribution is the identification of the complete singular geometry of the concrete projected Grassmannian.

## Limitations

The theorem addresses only the indicated first nontrivial truncation, not arbitrary \(d,n,r\). It identifies the reduced singular locus and Zariski local types, not the full projective defining ideal, all syzygies, the global intersection cohomology, or a classification of resolutions. The interpretation of the theorem as a historically new contribution remains subject to specialist checking, including possible implicit results in older projection and collineation literature. No independent mathematical audit has been performed.

## References

1. E. Feigin and I. Makhlin, *Truncated Grassmannians: polytopes, representations, and Cauchy formulas*, arXiv:2610.40891v1 (first public October 29, 2026), https://arxiv.org/html/2610.40891v1 .
2. E. Feigin, *Truncated Grassmannians, blow-ups along Schubert varieties and collineations*, arXiv:2604.00751v2 (first public April 1, 2026), https://arxiv.org/html/2604.00751v2 .
3. F. Faulstich, B. Sturmfels, and S. Sverrisdóttir, *Algebraic Varieties in Quantum Chemistry*, Foundations of Computational Mathematics 25 (2025), 1167–1198, https://doi.org/10.1007/s10208-024-09657-8 .
4. Y. Huang, G. Petroulakis, F. Sottile, and I. Zelenko, *Nontrivial linear projections of the Grassmannian \(\operatorname{Gr}_3(\mathbb C^6)\)*, arXiv:2004.10070, https://arxiv.org/abs/2004.10070 .
5. C. De Concini, D. Eisenbud, and C. Procesi, *Young diagrams and determinantal varieties*, Inventiones Mathematicae 56 (1980), 129–165.
