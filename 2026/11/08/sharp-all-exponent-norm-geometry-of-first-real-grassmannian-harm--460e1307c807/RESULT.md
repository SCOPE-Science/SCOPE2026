# Sharp all-exponent norm geometry of first real Grassmannian harmonics

## Finding

Let \(\mathcal G=\operatorname{Gr}(2,4)\) be the real Grassmannian of unoriented two-planes in \(\mathbb R^4\), represented by rank-two orthogonal projectors and equipped with invariant probability measure \(\mu\). Its nine-dimensional first nonconstant polynomial space consists of
\[
 f_A(P)=\operatorname{tr}(AP),\qquad A\in\operatorname{Sym}_0(4,\mathbb R),
\]
where \(A\) is real symmetric and trace-free. For every nonzero \(A\),
\[
 \|f_A\|_{L^2(\mu)}=\frac{\sqrt{\operatorname{tr}(A^2)}}{3}.
\]
For each real \(1\le p<\infty\), put
\[
 R_{\mathrm{pair}}(p)=\frac{3}{(p+1)^{2/p}},\qquad
 R_{\mathrm{outlier}}(p)=\frac{\sqrt3}{(p+1)^{1/p}}.
\]
The following **two-sided inequalities are sharp**, with all nonzero equality cases specified:
\[
\begin{array}{ll}
 R_{\mathrm{pair}}(p)\le \|f_A\|_p/\|f_A\|_2\le R_{\mathrm{outlier}}(p),&1\le p<2,\\[3pt]
 \|f_A\|_p/\|f_A\|_2=1,&p=2,\\[3pt]
 R_{\mathrm{outlier}}(p)\le \|f_A\|_p/\|f_A\|_2\le R_{\mathrm{pair}}(p),&2<p<\infty.
\end{array}
\]
The pair bound is attained **only** when the eigenvalues of \(A\), including multiplicity and up to a nonzero common factor, are \((1,1,-1,-1)\). The outlier bound is attained **only** when they are \((3,-1,-1,-1)\). Orthogonal conjugation and nonzero scalar multiples give every equality case. At \(p=2\), all nonzero \(A\) are equality cases. At the endpoint,
\[
\sqrt3\le\frac{\|f_A\|_\infty}{\|f_A\|_2}\le 3,
\]
with the same respective outlier and pair equality classes. In particular,
\[
 \frac95\le\frac{\|f_A\|_4^4}{\|f_A\|_2^4}\le\frac{81}{25},
\]
again with complete equality cases as above. The sharp norm ratio switches its extremal spectral family at the Hilbert exponent \(p=2\).

## Assumptions and scope

All matrices, functions and vector spaces here are **real**. For \(A\in\operatorname{Sym}_0(4,\mathbb R)\) the function \(P\mapsto\operatorname{tr}(AP)\) is defined on rank-two real orthogonal projectors. The \(L^p\)-norms use Haar probability measure, not unnormalized Riemannian volume. At \(p=\infty\), use the supremum over the compact Grassmannian (equivalently the essential supremum). The exact statement includes all real \(p\ge1\), not just even integers.

## Proof

**1. Oriented two-planes and two spheres.** Fix an orientation of \(\mathbb R^4\). A plane with an oriented orthonormal basis \(x,y\) has Plücker coordinates \(p_{ij}=x_i y_j-x_j y_i\), \(1\le i<j\le4\). They satisfy
\[
 \sum_{i<j}p_{ij}^2=1,\qquad
 p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}=0.
\]
Introduce
\[
\begin{aligned}
 u&=(p_{12}+p_{34},\ p_{13}-p_{24},\ p_{14}+p_{23}),\\
 v&=(p_{12}-p_{34},\ p_{13}+p_{24},\ p_{14}-p_{23}).
\end{aligned}
\]
The two displayed Plücker identities imply \(\|u\|_2=\|v\|_2=1\). Conversely, the inverse linear formulas for the six \(p_{ij}\) produce a unit decomposable bivector from every \((u,v)\in\mathbb S^2\times\mathbb S^2\). Hence the oriented Grassmannian is \(\mathbb S^2\times\mathbb S^2\) in these coordinates. The two commuting self-dual and anti-self-dual actions of \(\operatorname{SO}(4)\) act by the full product \(\operatorname{SO}(3)\times\operatorname{SO}(3)\). Thus invariant probability measure becomes the product of the uniform sphere laws. Orientation reversal changes \((u,v)\) to \((-u,-v)\); the bilinear expressions below are invariant under that simultaneous sign change and therefore descend to the unoriented Grassmannian.

**2. Matrix coefficients become bilinear forms.** By orthogonal invariance diagonalize \(A=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3,\lambda_4)\) with \(\sum_i\lambda_i=0\). The identity
\[
 P_{ii}=x_i^2+y_i^2=\sum_{j\ne i}p_{\min(i,j),\max(i,j)}^2
\]
and the Plücker relation give, after collecting opposite index pairs,
\[
 f_A(P)=m_1u_1v_1+m_2u_2v_2+m_3u_3v_3,
\qquad m_j=\lambda_1+\lambda_{j+1}\quad(j=1,2,3).
\]
Direct expansion using \(\sum_i\lambda_i=0\) shows
\[
 m_1^2+m_2^2+m_3^2=\sum_{i=1}^4\lambda_i^2
 =:T=\operatorname{tr}(A^2)>0.
\]
Conversely, any real triple \((m_1,m_2,m_3)\) arises from one trace-free diagonal: \(\lambda_1=(m_1+m_2+m_3)/2\), \(\lambda_{j+1}=m_j-\lambda_1\). Thus optimizing over all nonzero \(A\) is equivalent to optimizing over nonnegative triples \(q_j=m_j^2\) of fixed sum \(T\).

**3. Sphere averaging gives an exact one-dimensional moment functional.** Let \(U,V\) be independent and uniform on \(\mathbb S^2\). For every deterministic \(w\in\mathbb R^3\), the dot product \(w\cdot V\) is uniform on \([-\|w\|_2,\|w\|_2]\), so
\[
 \mathbb E|w\cdot V|^p=\frac{\|w\|_2^p}{p+1},\qquad p>-1.
\]
Consequently, for each \(1\le p<\infty\),
\[
 \|f_A\|_p^p=\frac1{p+1}\,
 \mathbb E_U\left(\sum_{j=1}^3q_j U_j^2\right)^{p/2}.
 \tag{1}
\]
In particular, \(\|f_A\|_2^2=\tfrac13\mathbb E_U\sum_jq_jU_j^2=T/9\).

**4. Strict convexity/concavity and all equality cases.** On the closed simplex \(q_j\ge0\), \(\sum q_j=T\), the right side of (1) is invariant under coordinate permutations. It is **strictly concave** in \(q\) for \(1\le p<2\), and **strictly convex** for \(p>2\). Indeed, \(t\mapsto t^{p/2}\) is strictly concave or convex on nonnegative reals, and if distinct triples \(q,r\) are chosen, then \(\sum_j(q_j-r_j)U_j^2\) is not almost surely zero: the law of \((U_1^2,U_2^2,U_3^2)\) has support with nonempty relative interior in the simplex. Integrating strict scalar Jensen proves strictness, including boundary points.

For \(p>2\), convexity writes any \(q\) as a convex combination of the three vertices \(Te_j\), making the vertices the **only** maximizers; permutation averaging (strict Jensen) makes \((T/3,T/3,T/3)\) the **only** minimizer. When \(p<2\), the conclusions reverse. At \(p=2\), (1) depends only on \(T\). When \(q=(T,0,0)\), the random variable is \(\sqrt T U_1V_1\), a product of two independent uniform \([-1,1]\) variables, giving
\[
\frac{\|f_A\|_p}{\|f_A\|_2}=\frac{3}{(p+1)^{2/p}}=R_{\mathrm{pair}}(p).
\]
When \(q=(T/3,T/3,T/3)\), the random variable is distributed as \(\sqrt{T/3}\,U\cdot V\), which is uniform on \([-\sqrt{T/3},\sqrt{T/3}]\); its ratio is
\[
\frac{\|f_A\|_p}{\|f_A\|_2}=\frac{\sqrt3}{(p+1)^{1/p}}=R_{\mathrm{outlier}}(p).
\]
If only one \(q_j\) is nonzero, the inverse eigenvalue formula gives the multiset proportional to \((1,1,-1,-1)\). If all \(q_j\) are equal, each \(m_j\) equals either \(\sqrt{T/3}\) or its negative; the inverse formula always gives the multiset proportional to \((3,-1,-1,-1)\). There are no other nonzero equality classes by strictness.

**5. The endpoint and a fourth-moment identity.** Since
\[
 \sup_{u,v\in\mathbb S^2}\left|\sum_jm_ju_jv_j\right|=\max_j|m_j|,
\]
the fixed-sum relation \(\sum_jm_j^2=T\) gives \(\sqrt{T/3}\le\|f_A\|_\infty\le\sqrt T\). Dividing by \(\|f_A\|_2=\sqrt T/3\) proves the endpoint, with precisely the corresponding equality cases. As an independent even-moment consequence, integrating (1) at \(p=4\) and using \(\mathbb E U_i^4=1/5\), \(\mathbb E U_i^2U_j^2=1/15\) gives
\[
\mathbb E f_A^4=\frac4{75}\left[(\operatorname{tr}A^2)^2-\operatorname{tr}A^4\right],
\]
which agrees with the stated sharp fourth-moment range. This completes the proof for every exponent and every equality case.

## Verification

The standalone file `verify_grassmannian.py` uses exact Python rational arithmetic and requires no nonstandard packages. Running `python verify_grassmannian.py` prints the following markers:

```text
EXACT_PLUCKER_AND_BILINEAR_IDENTITY_OK 20
EXACT_MOMENTS_AND_SHARP_ENVELOPES_OK 1710
SHARP_EIGENVALUE_MULTIPLICITIES_OK 16
ALL_GRASSMANNIAN_LP_CHECKS_OK
```

The checker independently constructs rational orthogonal four-dimensional rotations and Plücker coordinates; verifies the bilinear identity; computes exact even moments through the Dirichlet \((1/2,1/2,1/2)\) moment formula; checks sharp bounds in 1,710 cases; and checks both eigenvalue equality families. Finite computations test identities but do not prove the strict convexity assertion for every real exponent; the analytic argument above does so.

## Relationship to prior work

Ehler and Gräf [1] develop the polynomial harmonic decomposition and reproducing kernels for real Grassmannians, including first-degree spaces; these facts provide the setting but do not specify the sharp real \(L^2\)-to-\(L^p\) envelope or the two equality spectra. Bodmann, Ehler and Gräf [2] develop exact trace-moment techniques and cubature for Grassmannian projections using invariant theory and zonal polynomials; their polynomial moment formulas are background, but do not furnish the noninteger-exponent inequalities and strict all-exponent equality classification derived here. The classical Grassmannian spherical-function treatment [3] and differential-geometric harmonic analysis [4] likewise provide structural context; the new assertion is specifically the sharp all-real-exponent first-harmonic norm geometry of the real four-dimensional rank-two Grassmannian. A historical theorem not found in the indexed literature could still imply this result indirectly.

## Limitations

The claim is specific to the real \(\operatorname{Gr}(2,4)\), its trace-free first nonconstant polynomial space, and Haar probability measure. It neither determines sharp embeddings for higher harmonic degrees or different Grassmannians nor treats complex matrix coefficients. The derivation gives exact normalized norms, not the sharp operator norm of an unrelated polynomial projection. The literature comparison cannot exclude inaccessible or unindexed equivalent earlier assertions. Independent mathematical audit has not been carried out.

## References

1. M. Ehler and M. Gräf, *Harmonic decompositions on unions of Grassmannians* (first public preprint 2014-11-21; later *Reproducing kernels for the irreducible components of polynomial spaces on unions of Grassmannians*), arXiv:1411.5865v1, https://arxiv.org/abs/1411.5865.
2. B. G. Bodmann, M. Ehler and M. Gräf, *From low to high-dimensional moments without magic* (first public preprint 2016-01-27), arXiv:1601.07401v1, https://arxiv.org/abs/1601.07401.
3. A. T. James and A. G. Constantine, *Generalized Jacobi Polynomials as Spherical Functions of the Grassmann Manifold*, Proceedings of the London Mathematical Society (1974); referenced for classical invariant harmonics.
4. R. Howe and S. T. Lee, *Spherical harmonics on Grassmannians*, 2010, as background on representation-theoretic harmonic decompositions.
