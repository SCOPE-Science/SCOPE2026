# Exponential versus quadratic covariance conditioning in pyramids over repeated polytope products

## Finding

Let \(B\subset\mathbb R^r\) be any full-dimensional compact convex polytope, with \(r\ge1\), having \(v\ge r+1\) distinct vertices. For each integer \(m\ge1\), form its product pyramid
\[
 P_m=\operatorname{conv}\left((B^m\times\{0\})\cup\{(0,\ldots,0,1)\}\right)\subset\mathbb R^{mr+1}.
\]
All product factors are placed in mutually orthogonal coordinate blocks, and the last coordinate is height. Let \(C_m^{\mathrm{vert}}\) be the covariance of the **uniform distribution on the distinct vertices** of \(P_m\), and let \(C_m^{\mathrm{vol}}\) be the covariance of normalized full-dimensional Lebesgue volume on \(P_m\). Both are positive definite. For a positive-definite matrix \(C\), write \(\kappa(C)=\lambda_{\max}(C)/\lambda_{\min}(C)\).

Let \(\Sigma_{\mathrm{vert}}\) and \(\Sigma_{\mathrm{vol}}\) be the corresponding vertex-uniform and volume-uniform covariance matrices of \(B\). Then
\[
 \boxed{\lim_{m\to\infty}\frac{\kappa(C_m^{\mathrm{vert}})}{v^m}=\lambda_{\max}(\Sigma_{\mathrm{vert}})},
 \qquad
 \boxed{\lim_{m\to\infty}\frac{\kappa(C_m^{\mathrm{vol}})}{(mr)^2}=\lambda_{\max}(\Sigma_{\mathrm{vol}})}.
\]
Consequently, the ratio has the **sharp universal separation law**
\[
 \boxed{\lim_{m\to\infty}\frac{(mr)^2}{v^m}\frac{\kappa(C_m^{\mathrm{vert}})}{\kappa(C_m^{\mathrm{vol}})}
 =\frac{\lambda_{\max}(\Sigma_{\mathrm{vert}})}{\lambda_{\max}(\Sigma_{\mathrm{vol}})}>0.}
\]
These constants do not depend on the locations of the two centroids relative to the pyramid apex.

The formulas are constructive for arbitrary \(B\). With \(\nu\) and \(\mu\) respectively the means of the vertex and volume measures on \(B\), \(I_m\) the identity on the product-factor index, and \(\mathbf1_m\) the all-ones vector, set
\[
 \mathcal C(c,a,\Sigma,z)=
 \begin{pmatrix}0&0\\0&c(I_m\otimes\Sigma)\end{pmatrix}
 +a\begin{pmatrix}1\\-\mathbf1_m\otimes z\end{pmatrix}
 \begin{pmatrix}1&-(\mathbf1_m\otimes z)^\mathsf T\end{pmatrix}.
\]
Here the upper-left block is one-dimensional. If \(t=v^m\) and \(d=mr\), **the exact finite-dimensional covariance identities** are
\[
 \boxed{C_m^{\mathrm{vert}}=\mathcal C\!\left(\frac{t}{t+1},\frac{t}{(t+1)^2},\Sigma_{\mathrm{vert}},\nu\right),}
\]
\[
 \boxed{C_m^{\mathrm{vol}}=\mathcal C\!\left(\frac{d+1}{d+3},\frac{d+1}{(d+2)^2(d+3)},\Sigma_{\mathrm{vol}},\mu\right).}
\]
In particular, for each fixed integer \(q\ge2\), the stable-set polytope of the clique windmill \(K_1\vee(mK_q)\) is exactly \(P_m\) with \(B=\Delta_q=\operatorname{conv}(0,e_1,\ldots,e_q)\). In this canonical realization,
\[
 \lim_{m\to\infty}\frac{\kappa(C_m^{\mathrm{vert}})}{(q+1)^m}=\frac1{q+1},\qquad
 \lim_{m\to\infty}\frac{\kappa(C_m^{\mathrm{vol}})}{(mq)^2}=\frac1{(q+1)(q+2)},
\]
so the sharp separation constant is \(q+2\).

## Assumptions and scope

The polytope \(B\) is fixed as \(m\) tends to infinity and has nonempty interior in its \(r\)-dimensional ambient Euclidean space. Its position is arbitrary; the pyramid apex is at the origin of the product coordinates and height one. No central symmetry, rationality, integrality, or isotropy assumption is required. All covariance matrices use the specified Euclidean coordinate metric, not a separately chosen affine whitening. The two sampling rules are genuinely different; vertex sampling gives each **distinct vertex** equal mass, whereas volume sampling uses ordinary normalized Lebesgue measure. The theorem does not assert uniform bounds when \(B\), its dimension, or its shape varies with \(m\).

## Proof

**1. Positive definiteness and the vertex law.** Write \(V(B)\) for the vertices of \(B\). The base of \(P_m\) has exactly \(t=v^m\) vertices, the \(m\)-tuples from \(V(B)\), and the apex is one additional vertex; every base vertex is exposed by a supporting functional extended with a sufficiently negative height coefficient. The apex is likewise exposed. Thus a vertex-uniform sample has height zero with probability \(t/(t+1)\). Conditional on this event, its product coordinates are \(m\) independent samples from the vertex-uniform distribution of \(B\); otherwise its coordinates are zero and its height is one. The law of total covariance immediately yields the first displayed \(\mathcal C\) identity. Full dimensionality makes \(\Sigma_{\mathrm{vert}}\) positive definite and the rank-one term has nonzero height component, so the full matrix is positive definite.

**2. Volume law and normalization.** Put \(d=mr\). The slice at height \(h\in[0,1]\) is \((1-h)B^m\), so its \(d\)-dimensional volume is \((1-h)^d\operatorname{vol}_d(B^m)\). Therefore a volume-uniform point has independent representation \((H,(1-H)Y_1,\ldots,(1-H)Y_m)\), where \(Y_i\) are independent volume-uniform points of \(B\) and \(H\sim\operatorname{Beta}(1,d+1)\). The beta moments are
\[
 \operatorname{Var}(H)=\frac{d+1}{(d+2)^2(d+3)},\qquad
 \mathbb E(1-H)^2=\frac{d+1}{d+3}.
\]
Since \(\operatorname{Cov}(H,1-H)=-\operatorname{Var}(H)\), applying total covariance produces the second \(\mathcal C\) identity. The same argument proves positive definiteness.

**3. Spectral perturbation lemma.** Let \(\Sigma\) be any fixed positive-definite \(r\times r\) matrix and \(z\in\mathbb R^r\) be fixed. Suppose \(c_m\to1\), \(a_m>0\), and \(ma_m\to0\). For
\[
 C_m=\operatorname{diag}(0,c_m I_m\otimes\Sigma)+a_m ww^\mathsf T,
 \qquad w=(1,-\mathbf1_m\otimes z),
\]
one has
\[
 \lambda_{\max}(C_m)\longrightarrow\lambda_{\max}(\Sigma),
 \qquad \frac{\lambda_{\min}(C_m)}{a_m}\longrightarrow1.
\]
For the maximum, the perturbation has operator norm \(a_m\|w\|^2=a_m(1+m\|z\|^2)\to0\); the first matrix has maximum eigenvalue \(c_m\lambda_{\max}(\Sigma)\). For the minimum, denote \(\sigma=\lambda_{\min}(\Sigma)>0\). The unit height vector gives \(\lambda_{\min}(C_m)\le a_m\). For sufficiently large \(m\), \(a_m<c_m\sigma\). With \(u=\mathbf1_m\otimes z\), the Schur complement at \(\lambda=\lambda_{\min}(C_m)\) gives
\[
 a_m-\lambda=a_m^2 u^\mathsf T
 (c_m I_m\otimes\Sigma+a_m uu^\mathsf T-\lambda I)^{-1}u.
\]
The inverse exists because its matrix is bounded below by \((c_m\sigma-a_m)I\). Since \(\|u\|^2=m\|z\|^2\),
\[
 1-\frac{a_m m\|z\|^2}{c_m\sigma-a_m}
 \le\frac{\lambda_{\min}(C_m)}{a_m}\le1.
\]
The lower bound tends to one. If \(z=0\), this argument remains valid with equality at the lower eigenvalue.

**4. Sharp asymptotics.** In the vertex case \(a_m=t/(t+1)^2\), so \(a_m\sim v^{-m}\) and \(ma_m\to0\). In the volume case \(a_m=(d+1)/((d+2)^2(d+3))\), so \(a_m\sim d^{-2}\) and \(ma_m\to0\), since \(d=mr\). In both cases the relevant \(c_m\) tends to one. Applying the lemma proves the two limits and their ratio. All limiting constants are strictly positive because both covariances of \(B\) are positive definite.

**5. Clique-windmill application.** The stable sets of \(K_1\vee(mK_q)\) either consist solely of the hub or omit the hub and select independently at most one vertex from each outer clique. Their incidence polytope is the stated pyramid with \(B=\Delta_q\). The covariance of the \(q+1\) equally weighted vertices \(0,e_1,\ldots,e_q\) is
\[
 \Sigma_{\mathrm{vert}}=\frac{I_q}{q+1}-\frac{\mathbf1_q\mathbf1_q^\mathsf T}{(q+1)^2}.
\]
The uniform volume covariance of that simplex is
\[
 \Sigma_{\mathrm{vol}}=\frac{I_q}{(q+1)(q+2)}-\frac{\mathbf1_q\mathbf1_q^\mathsf T}{(q+1)^2(q+2)}.
\]
For \(q\ge2\) their largest eigenvalues are respectively \(1/(q+1)\) and \(1/((q+1)(q+2))\), completing the corollary.

## Verification

An accompanying standalone Python checker reconstructs each vertex covariance independently by explicit enumeration for simplex, square, and translated-simplex bases through four product factors. It checks all covariance entries using exact rational arithmetic. A separate beta-integral implementation reconstructs the volume covariance entries from raw moments and independently matches the rank-one formulas. The exact spectral asymptotic lemma above, not finite enumeration, proves the limits. The code requires only the Python standard library and prints a fixed success marker.

## Relationship to prior work

Aliniaeifard, Benedetti, Bergeron, Li, and Saliola (arXiv:1804.00360, first posted April 2, 2018) study stable-set polytopes and their one-skeleta; that paper supplies the motivating incidence-polytope setting but not the dual covariance-conditioning result. Hibi, Ohsugi, and Tsuchiya (arXiv:1807.05989, first posted July 16, 2018) study Cayley sums of order and stable-set polytopes and their lattice properties; they do not analyze the present product-pyramid covariance laws.

Known product-moment and beta-integral identities, including exact volume moments for special cograph stable-set families, form part of the background and are not claimed as new. The result proved here is the **universal comparison of vertex and volume covariance spectra with sharp asymptotic constants for every fixed full-dimensional base polytope**. The searchable mathematical research record contains related results on covariances of other particular polytope families and product geometry, but the examined matches do not assert or imply this universal ratio. This is a best-knowledge priority assessment, not a claim that no earlier equivalent theorem exists.

## Limitations

The result concerns covariance condition numbers in the given ambient Euclidean coordinates; arbitrary affine changes of metric need not preserve the constants. The asymptotics hold with a fixed base polytope, and no quantitative remainder uniform over all bases is asserted. The argument uses classical beta moments and elementary block-matrix perturbation; the originality claim is about their sharpened combination, not the component identities. Broader earlier work on pyramid second moments could potentially contain an equivalent formulation; no independent mathematical audit or historical-priority certification has been performed.

## References

1. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li, and F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360, first public version 2018-04-02. https://arxiv.org/abs/1804.00360
2. T. Hibi, H. Ohsugi, and A. Tsuchiya, *Integer decomposition property for Cayley sums of order and stable set polytopes*, arXiv:1807.05989, first public version 2018-07-16. https://arxiv.org/abs/1807.05989
