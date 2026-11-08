# Exact dispersion and extreme-value limit for nearest-vertex quantization of a regular simplex

## Finding
Let \(m\ge2\), and let \(v_1,\ldots,v_m\) be the vertices of a regular Euclidean \((m-1)\)-simplex of circumradius \(R>0\). If \(X\) is uniformly distributed in its volume, define the normalized squared nearest-vertex error
\[
Q_m=R^{-2}\min_{1\le i\le m}\lVert X-v_i\rVert^2.
\]
Set \(H_m=\sum_{j=1}^m1/j\) and \(H_m^{(2)}=\sum_{j=1}^m1/j^2\). Then, in every finite dimension,
\[
\mathbb E Q_m=\frac{m}{m-1}\left(1+\frac2{m+1}-\frac{2H_m}{m}\right),
\]
\[
\boxed{\operatorname{Var}(Q_m)=\left(\frac{m}{m-1}\right)^2\left[\frac{4(m-1)}{(m+1)^2(m+2)(m+3)}+\frac{4\bigl(mH_m^{(2)}-H_m^2\bigr)}{m^2(m+1)}-\frac{4\bigl(H_m^2+H_m^{(2)}-2H_m\bigr)}{m(m+1)(m+2)}\right].}
\]
The nonstandard ingredient is an exact positive covariance: for the uniform barycentric coordinates \((\lambda_1,\ldots,\lambda_m)\), set \(M_m=\max_i\lambda_i\) and \(S_m=\sum_i\lambda_i^2\). Then
\[
\boxed{\operatorname{Cov}(M_m,S_m)=\frac{H_m^2+H_m^{(2)}-2H_m}{m(m+1)(m+2)}>0.}
\]
Despite positivity in every finite dimension, this covariance corresponds to asymptotic decorrelation:
\[
\operatorname{Corr}(M_m,S_m)\sim\frac{\sqrt6}{2\pi}\frac{(\log m)^2}{\sqrt m}.
\]
Finally, if \(G\) is standard Gumbel, with \(\Pr(G\le x)=\exp(-e^{-x})\), then
\[
\boxed{m(1-Q_m)-2\log m\ \Longrightarrow\ 2G-3,\qquad m^2\operatorname{Var}(Q_m)\longrightarrow\frac{2\pi^2}{3}.}
\]
These are statements about a fixed regular vertex code on the simplex itself, not about optimal quantizer design over arbitrary codebooks.

## Assumptions and scope
The simplex is nondegenerate, \(m\ge2\) is an integer, and its circumcenter is translated to the origin. All vertices satisfy \(\|v_i\|=R\) and \(v_i\cdot v_j=-R^2/(m-1)\) for \(i\ne j\). The probability measure is normalized \((m-1)\)-dimensional Euclidean volume on the simplex. Nearest-vertex ties have probability zero; any deterministic tie convention gives the same law. The variance formula uses the variance of the *squared* Euclidean error, divided by \(R^4\), not that of the unsquared distance.

## Proof
**1. Barycentric reduction.** Write \(X=\sum_i\lambda_i v_i\) with \(\lambda_i\ge0\), \(\sum_i\lambda_i=1\). Volume-uniform sampling makes \(\lambda\sim\mathrm{Dirichlet}(1,\ldots,1)\). The regular-simplex inner products give
\[
\frac{\|X\|^2}{R^2}=\frac{mS_m-1}{m-1},\qquad
\frac{2X\cdot v_i}{R^2}=\frac{2(m\lambda_i-1)}{m-1}.
\]
Thus the closest vertex has the largest barycentric coordinate and
\[
Q_m=\frac{m}{m-1}(1+S_m-2M_m). \tag{1}
\]

**2. Standard and maximum-coordinate moments.** Uniform-simplex integration gives
\[
\mathbb ES_m=\frac2{m+1},\quad
\mathbb ES_m^2=\frac{4(m+5)}{(m+1)(m+2)(m+3)}. \tag{2}
\]
To verify the second identity, use \(\mathbb E\lambda_i^4=24/[m(m+1)(m+2)(m+3)]\) and \(\mathbb E\lambda_i^2\lambda_j^2=4/[m(m+1)(m+2)(m+3)]\) for distinct indices, and expand \(S_m^2\). The usual inclusion-exclusion formula for the largest uniform spacing is
\[
\Pr(M_m>t)=\sum_{k=1}^m(-1)^{k+1}{m\choose k}(1-kt)_+^{m-1}.
\]
Integrating against \(1\) and \(2t\) respectively yields
\[
\mathbb EM_m=\frac{H_m}{m},\qquad
\mathbb EM_m^2=\frac{H_m^2+H_m^{(2)}}{m(m+1)}. \tag{3}
\]
Here one uses \(\sum_{k=1}^m(-1)^{k+1}{m\choose k}/k=H_m\) and \(\sum_{k=1}^m(-1)^{k+1}{m\choose k}/k^2=(H_m^2+H_m^{(2)})/2\). They follow by integrating \([1-(1-u)^m]/u\) and then its logarithmically weighted integral over \((0,1)\).

**3. The joint mixed moment.** For any specified set \(I\) of \(k\) coordinate indices, the event \(\lambda_i>t\) for all \(i\in I\) has probability \((1-kt)^{m-1}\) on \(0\le t\le1/k\). Translating those \(k\) coordinates by \(t\) leaves a uniformly distributed simplex of total mass \(1-kt\). Hence
\[
\mathbb E\left[S_m;\ \lambda_i>t\text{ for every }i\in I\right]
=(1-kt)^{m-1}\left[\frac{2(1-kt)^2}{m+1}+\frac{2kt(1-kt)}{m}+kt^2\right]. \tag{4}
\]
The integral of the right-hand side over \(0\le t\le1/k\) equals
\[
\frac{2}{km(m+2)}+\frac{2}{k^2m(m+1)(m+2)}.
\]
Since \(M_m=\int_0^1\mathbf1_{\{M_m>t\}}\,dt\), inclusion-exclusion in (4), followed by the two binomial identities, gives
\[
\mathbb E[M_mS_m]=\frac{2H_m}{m(m+2)}+
\frac{H_m^2+H_m^{(2)}}{m(m+1)(m+2)}. \tag{5}
\]
Subtract \(\mathbb EM_m\mathbb ES_m\) to obtain the boxed covariance. Its numerator is \((H_m-1)^2+(H_m^{(2)}-1)>0\) for every \(m\ge2\).

**4. Exact dispersion.** From (2)--(5),
\[
\operatorname{Var}(S_m)=\frac{4(m-1)}{(m+1)^2(m+2)(m+3)},\quad
\operatorname{Var}(M_m)=\frac{mH_m^{(2)}-H_m^2}{m^2(m+1)}.
\]
Substituting these and the mixed covariance into (1) proves the mean and variance identities. For example, \(m=2\) gives \(\mathbb EQ_2=1/3\), \(\operatorname{Var}(Q_2)=4/45\), while \(m=3\) gives \(\mathbb EQ_3=5/12\), \(\operatorname{Var}(Q_3)=43/720\). The limits of the exact formulas use \(H_m=\log m+\gamma+o(1)\) and \(H_m^{(2)}\to\pi^2/6\). The same formulas imply the stated correlation asymptotic.

**5. Non-Gaussian high-dimensional limit.** Represent \(\lambda_i=Y_i/T_m\), where \(Y_i\) are independent mean-one exponential variables and \(T_m=\sum_iY_i\). The laws of large numbers give \(T_m/m\to1\) and \(\sum_iY_i^2/m\to2\) in probability. The maximum \(Y_{(m)}\) obeys \(\Pr(Y_{(m)}-\log m\le x)=(1-e^{-x}/m)^m\to\exp(-e^{-x})\). Since \(Y_{(m)}=O_{\Pr}(\log m)\) and \(T_m/m=1+O_{\Pr}(m^{-1/2})\), we have \(mM_m-\log m\Longrightarrow G\); also \(mS_m\to2\) in probability. Rearranging (1),
\[
m(1-Q_m)-2\log m
=\frac{2m^2M_m-m^2S_m-m}{m-1}-2\log m
\Longrightarrow 2G-3.
\]
This proves every asserted limit. The variance limit follows independently from the exact finite formula and does not rely on an unproved uniform-integrability inference from weak convergence.

## Verification
Run `python3 verify.py` with Python 3.10 or newer. The standalone program uses only standard-library exact rational arithmetic and explicitly integrates the mixed cubic moment over an *ordered* barycentric simplex (a distinct calculation from the inclusion-exclusion derivation). It checks dimensions with \(2\le m\le16\), verifies two closed-form endpoint cases, and makes illustrative direct simulations with 210,000 sampled points. Successful execution reports:

`VERIFY_OK ordered_simplex_exact_cases=15 exact_dim1=1 exact_dim2=1 sampled_points=210000 strict_positive_covariance_cases=15`

The infinite-dimensional limit and all-dimension formulas are established by the proof, not by finite tests.

## Relationship to prior work
Conway and Sloane (1982) calculate second moments of regular polytopes about their centroids and formulate lattice quantization, but not the variance of distance to the nearest vertex of the simplex itself. Onn and Weissman (first published online May 19, 2009) identify uniform-simplex coordinates with uniform spacings and give the first and second moments of the maximum coordinate. These known marginal formulas are used and credited. The mixed moment in (5), its positive covariance, the exact finite-dimensional nearest-vertex distortion variance, and the corresponding geometric limit law are distinct from their stated results. Pyke's survey explains classical spacing models. Kabluchko, Litvak and Zaporozhets (2015) obtain Gumbel limits for random *projection widths* of regular polytopes; those variables differ from nearest-vertex distortion of uniform interior points. No claim of novelty is made for Gumbel extreme-value theory itself.

## Limitations
This addresses the circumradius-normalized, unweighted squared-error distribution for a fixed regular-simplex vertex set only. It neither asserts the codebook is optimal nor gives concentration inequalities uniform in dimension or finite-sample error guarantees. The exact covariance and fluctuation theorem are proven; exhaustive historical priority beyond the inspected sources remains unverified. An exact expression for the *full finite-dimensional law* of \(Q_m\) is not asserted.

## References
1. S. Onn and I. Weissman, *Generating uniform random vectors over a simplex with implications to the volume of a certain polytope and to multivariate extremes*, Annals of Operations Research 189 (2011), 331–342. First published online May 19, 2009. DOI: https://doi.org/10.1007/s10479-009-0567-7. Full author-uploaded text: https://www.researchgate.net/publication/220461324_Generating_uniform_random_vectors_over_a_simplex_with_implications_to_the_volume_of_a_certain_polytope_and_to_multivariate_extremes.
2. J. H. Conway and N. J. A. Sloane, *Voronoi Regions of Lattices, Second Moments of Polytopes, and Quantization*, IEEE Transactions on Information Theory 28 (1982), 211–226. https://neilsloane.com/doc/Me82.pdf.
3. R. Pyke, *Spacings Revisited*, Proceedings of the Sixth Berkeley Symposium on Mathematical Statistics and Probability, volume 1 (1972), 417–427. https://digicoll.lib.berkeley.edu/record/113194/files/math_s6_v1_article-22.pdf.
4. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, first posted November 26, 2015. https://arxiv.org/abs/1511.08479.
