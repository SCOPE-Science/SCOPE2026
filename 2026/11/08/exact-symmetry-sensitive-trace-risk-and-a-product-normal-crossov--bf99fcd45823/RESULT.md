# Exact symmetry-sensitive trace risk and a product-normal crossover for Gaussian diagonal recovery

## Finding
For every integer \(n\ge 2\), every real square matrix \(A\in\mathbb R^{n\times n}\), and every integer \(q\ge3\), apply the one-sided Gaussian rowwise least-squares algorithm to the prescribed diagonal row spaces. If \(\widehat A\) denotes its diagonal output, the trace error \(E_q=\operatorname{tr}\widehat A-\operatorname{tr}A\) is unbiased and obeys the exact identity
\[
\operatorname{Var}(E_q)=\frac{\|A_{\mathrm{off}}\|_F^2}{q-2}+\frac2q\sum_{1\le i<j\le n}A_{ij}A_{ji}
=\frac{2(q-1)}{q(q-2)}\|S_{\mathrm{off}}\|_F^2+\frac2{q(q-2)}\|K\|_F^2,
\]
where \(A_{\mathrm{off}}=A-\operatorname{diag}(A_{11},\ldots,A_{nn})\), \(S_{\mathrm{off}}=(A_{\mathrm{off}}+A_{\mathrm{off}}^T)/2\), and \(K=(A-A^T)/2\). In particular, a purely skew-symmetric matrix has mean-square trace error exactly \(2\|A\|_F^2/[q(q-2)]\), which is order \(q^{-2}\) rather than the generic \(q^{-1}\) rate.

There is a sharp non-Gaussian transition. For each \(q\), take
\[
A_q=\begin{pmatrix}0&a\\-a+\kappa/\sqrt q&0\end{pmatrix},\qquad a\ne0,\quad \kappa\in\mathbb R.
\]
With independent standard normal \(Z,W\), the trace error satisfies
\[
qE_q\ \xrightarrow{d}\ Z(\kappa+2aW).
\]
For \(\kappa=0\) this is the product-normal law \(2aZW\), not a Gaussian. Its characteristic function is \((1+4a^2t^2)^{-1/2}\); for general \(\kappa\), it is
\[
\frac{\exp\!\left[-\kappa^2t^2/(2(1+4a^2t^2))\right]}{\sqrt{1+4a^2t^2}}.
\]

## Assumptions and scope
Choose \(q\) independent standard Gaussian column queries \(g^{(1)},\ldots,g^{(q)}\in\mathbb R^n\), form \(G\in\mathbb R^{n\times q}\), and observe \(AG\). The same \(G\) is shared by all rows. Each row \(i\) is restricted to \(\operatorname{span}(e_i)\), and its scalar coefficient is the exact least-squares solution using the corresponding query row. Put \(g_i=G_{i,:}\in\mathbb R^q\), \(U_i=\|g_i\|_2^2\), and \(X_{ij}=g_i\cdot g_j\). All denominators are positive almost surely. All expectations refer to these Gaussian queries alone, with \(A\) fixed and deterministic. The matrix dimension is arbitrary but finite. The Gaussian query count satisfies \(q>2\), as used in finite second moments. The limiting statement uses dimension exactly two, with \(a,\kappa\) fixed as \(q\to\infty\).

## Proof
The rowwise least-squares normal equation gives
\[
\widehat A_{ii}=\frac{g_i\cdot(AG)_{i,:}}{U_i}
=A_{ii}+\sum_{j\ne i}A_{ij}\frac{X_{ij}}{U_i}.
\]
Define \(\delta_i=\widehat A_{ii}-A_{ii}\). Conditioning on \(g_i\) shows \(\mathbb E[\delta_i\mid g_i]=0\) and
\[
\mathbb E[\delta_i^2\mid g_i]=\frac{\sum_{j\ne i}A_{ij}^2}{U_i}.
\]
Since \(U_i\sim\chi_q^2\), \(\mathbb E[U_i^{-1}]=1/(q-2)\), yielding \(\operatorname{Var}(\delta_i)=\sum_{j\ne i}A_{ij}^2/(q-2)\).

For distinct \(i,j\), expand \(\mathbb E[\delta_i\delta_j]\). Terms in which the two off-diagonal sums have different unpaired Gaussian row indices vanish by centering or odd symmetry. The sole surviving term pairs \(X_{ij}/U_i\) with \(X_{ji}/U_j\), and hence
\[
\operatorname{Cov}(\delta_i,\delta_j)
=A_{ij}A_{ji}\,\mathbb E\frac{(g_i\cdot g_j)^2}{U_iU_j}
=\frac{A_{ij}A_{ji}}q.
\]
Indeed, \(g_i/\|g_i\|\) and \(g_j/\|g_j\|\) are independent uniformly spherical vectors in \(\mathbb R^q\), and their squared inner product has mean \(1/q\). Summing diagonal variances and twice the cross covariances proves the first formula. The Frobenius orthogonality of symmetric and skew-symmetric parts, together with \(2\sum_{i<j}A_{ij}A_{ji}=\|S_{\mathrm{off}}\|_F^2-\|K\|_F^2\), gives the second exact formula.

For the two-dimensional crossover write \(g=g_1\), \(h=g_2\), \(U=\|g\|^2\), \(V=\|h\|^2\), \(X=g\cdot h\). Exactly,
\[
E_q=X\left[\frac aU+\frac{-a+\kappa/\sqrt q}{V}\right]
=X\left[a\frac{V-U}{UV}+\frac\kappa{\sqrt q\,V}\right].
\]
The multivariate central limit theorem applies to the iid query-coordinate pairs \((g_rh_r,h_r^2-g_r^2)\), which have mean zero, variances \(1\) and \(4\), and zero cross covariance. Therefore
\[
\left(\frac X{\sqrt q},\frac{V-U}{\sqrt q}\right)\xrightarrow{d}(Z,2W),
\]
with independent standard Gaussians \(Z,W\). The law of large numbers gives \(U/q,V/q\to1\) in probability, and Slutsky's theorem yields \(qE_q\xrightarrow d Z(\kappa+2aW)\). Conditioning on \(W\) evaluates its characteristic function as claimed. For fixed off-diagonal coefficients \(a,b\) instead, \(\sqrt q E_q\xrightarrow d(a+b)Z\), so the faster scale occurs exactly on the antisymmetry line \(a+b=0\).

## Verification
The accompanying `verify.py` reconstructs the diagonal least-squares coefficients directly from \(AG\), independently evaluates the error formula and its symmetric–skew decomposition on random matrices, checks exact two-by-two rational identities, and runs seeded supplementary Monte Carlo sample-moment tests. It passes \(2021\) assertions/groups in a standard Python environment with NumPy. The mathematical identities and the central-limit result are proved above; finite numerical checks do not certify the asymptotic law. Run `python verify.py` from the folder containing the script.

## Relationship to prior work
Gallmeier and Otto (arXiv:2610.07513v1, §2, Algorithm 1, Theorem 1) study common Gaussian forward queries followed by rowwise least-squares reconstruction and bound Frobenius error using the individual row errors. Amsel and coauthors (arXiv:2402.09379v3, §2, Remark 3) identify the diagonal case with the normalized Gaussian Hutchinson diagonal estimator. Hallman, Ipsen and Saibaba (arXiv:2202.02887v2, §5.3, Lemma 5.7) identify the single-coordinate Student distribution, for symmetric input matrices. Bekas, Kokiopoulou and Saad (2005 preprint of the 2007 article, §2.1–2.2, Eq. 3) provide the original diagonal estimator and its rowwise expansion, but not the cross-row covariance or the near-skew scaling. Those statements establish the algorithm and marginal noise behavior; the present claim concerns the full cross-row covariance, its exact trace contraction into symmetric/skew components for non-self-adjoint inputs, and the critical two-dimensional product-normal limit. The classical direct Hutchinson trace estimator has a different formula and annihilates skew-symmetric matrices identically, rather than merely at order \(q^{-2}\). This finding does not claim superiority over direct trace estimation, nor does it claim to introduce the diagonal estimator itself.

## Limitations
Only real independent standard Gaussian forward queries, a single shared sketch, prescribed *coordinate-diagonal* row spaces, exact rowwise least squares, and exact arithmetic are treated. The finite risk is meaningful for \(q>2\). The product-normal limit concerns a two-dimensional near-skew family, not arbitrary growing matrices or nonlinear operators. A different subspace family, separate per-row sketches, non-Gaussian query distribution, or numerical conditioning may change these conclusions. Unindexed equivalent covariance computations remain possible; this is a self-reviewed mathematical finding, not an independent audit.

## References
1. Esther Gallmeier and Samuel E. Otto, *Efficient Approximation of Structured Linear Operators using Randomized One-Sided Queries*, arXiv:2610.07513v1, 5 October 2026, https://arxiv.org/html/2610.07513v1 (full primary text, §2 and Appendix).
2. Noah Amsel, Tyler Chen, Feyza Duman Keles, Diana Halikias, Cameron Musco and Christopher Musco, *Fixed-sparsity matrix approximation from matrix-vector products*, arXiv:2402.09379v3, https://arxiv.org/html/2402.09379v3 (full primary text, §1.3, §2, Remark 3).
3. Eric Hallman, Ilse C. F. Ipsen and Arvind K. Saibaba, *Monte Carlo Methods for Estimating the Diagonal of a Real Symmetric Matrix*, arXiv:2202.02887v2, https://arxiv.org/pdf/2202.02887 (full primary text, §5.3, Lemma 5.7).
4. C. Bekas, E. Kokiopoulou and Y. Saad, *An estimator for the diagonal of a matrix*, 7 April 2005 open preprint, https://infoscience.epfl.ch/record/87297/files/Bekas2005_1358.pdf, published in Applied Numerical Mathematics 57 (2007), 1214–1229, https://doi.org/10.1016/j.apnum.2007.01.003 (primary preprint, §2.1–2.2, Eq. 3 examined; no assertion that final journal version was inspected).
