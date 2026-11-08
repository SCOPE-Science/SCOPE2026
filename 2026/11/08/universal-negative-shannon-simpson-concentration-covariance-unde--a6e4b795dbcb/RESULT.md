# Universal negative Shannon–Simpson concentration covariance under heterogeneous Dirichlet laws

## Finding

For any integer \(m\ge2\) and any strictly positive, not necessarily equal, real numbers \(\alpha_1,\ldots,\alpha_m\), consider \(P=(P_1,\ldots,P_m)\sim\operatorname{Dirichlet}(\alpha_1,\ldots,\alpha_m)\). Define Shannon entropy \(H=-\sum_iP_i\log P_i\) and Simpson concentration \(C=\sum_i P_i^2\). The Gini–Simpson diversity is \(D=1-C\).

Write \(A=\sum_i\alpha_i\), \(B=\sum_i\alpha_i^2\), \(w_i=\alpha_i/A\), and let \(\psi(z)=\Gamma'(z)/\Gamma(z)\) denote the digamma function. Weighted covariance for deterministic arrays means
\[\operatorname{Cov}_w(u_i,v_i)=\sum_iw_iu_iv_i-\left(\sum_iw_iu_i\right)\left(\sum_iw_iv_i\right).\]
The exact result is
\[
\boxed{\operatorname{Cov}(C,H)
=-\frac{A^2-B}{A(A+1)^2(A+2)}-\frac{2}{(A+1)(A+2)}\operatorname{Cov}_w\bigl(\alpha_i,\psi(\alpha_i+1)\bigr).}
\]
Equivalently, as a sum over unordered pairs,
\[
\boxed{\operatorname{Cov}(C,H)=
-\frac{2}{A(A+1)^2(A+2)}\sum_{i<j}\alpha_i\alpha_j
\left[1+\frac{A+1}{A}(\alpha_i-\alpha_j)(\psi(\alpha_i+1)-\psi(\alpha_j+1))\right].}
\]
Consequently \(\operatorname{Cov}(C,H)<0\) and \(\operatorname{Cov}(H,D)>0\) for every such law, with the sharp, parameter-specific envelope
\[
\operatorname{Cov}(C,H)\le-\frac{A^2-B}{A(A+1)^2(A+2)}<0.
\]
The first inequality becomes an equality **if and only if** \(\alpha_1=\cdots=\alpha_m\). In that symmetric case, with all \(\alpha_i=a>0\), the exact value simplifies to
\[\operatorname{Cov}(C,H)=-\frac{a(m-1)}{(ma+1)^2(ma+2)}.\]

## Assumptions and scope

The Dirichlet distribution has density proportional to \(\prod_i p_i^{\alpha_i-1}\) on the open probability simplex. All logarithms are natural. There is no integer, symmetry, or concentration restriction on the strictly positive parameters. The formulas hold for every finite \(m\ge2\), including any finite-dimensional multinomial–Dirichlet posterior obtained from positive prior parameters by adding nonnegative counts. The one-category case is degenerate and excluded.

## Proof

Put \(M=A+B\) and \(Q=A(A+1)(A+2)\). The standard beta-gamma moment identity, valid when all exponents keep parameters positive, is
\[
\mathbb E\prod_iP_i^{r_i}=\frac{\Gamma(A)}{\Gamma(A+\sum_ir_i)}\prod_i\frac{\Gamma(\alpha_i+r_i)}{\Gamma(\alpha_i)}.
\]
Differentiation with respect to one exponent yields moments containing \(\log P_j\). Because all \(\alpha_i>0\), the derivatives in the following finite neighborhood are integrable. The elementary expectations are
\[
\mathbb EC=\frac{M}{A(A+1)},\qquad
\mathbb EH=\psi(A+1)-\frac1A\sum_j\alpha_j\psi(\alpha_j+1).
\]
For every \(j\), separate the term whose squared coordinate equals \(j\) from the terms with distinct squared coordinate, and differentiate the Dirichlet mixed-moment formula at exponent one in coordinate \(j\). This gives
\[
\mathbb E[CP_j\log P_j]
=\frac{\alpha_j(M+2\alpha_j+2)}{Q}
[\psi(\alpha_j+1)-\psi(A+3)]
+\frac{\alpha_j(2\alpha_j+3)}{Q}.
\]
Since \(CH=-\sum_j CP_j\log P_j\), subtract \(\mathbb EC\,\mathbb EH\) and use \(\psi(A+3)-\psi(A+1)=(A+1)^{-1}+(A+2)^{-1}\). Writing \(T=\sum_j\alpha_j\psi(\alpha_j+1)\) and \(U=\sum_j\alpha_j^2\psi(\alpha_j+1)\), the numerator simplifies exactly to
\[
\operatorname{Cov}(C,H)=\frac{B-A^2}{A(A+1)^2(A+2)}
-\frac{2}{A(A+1)(A+2)}\left(U-\frac{BT}{A}\right).
\]
By the definition of the weights, \(U-BT/A=A\operatorname{Cov}_w(\alpha_i,\psi(\alpha_i+1))\). This proves the first boxed formula, with the raw-moment algebra also independently checked by the provided program.

For any normalized positive weights, the deterministic polarization identity gives
\[
\operatorname{Cov}_w(u_i,v_i)=\sum_{i<j}w_iw_j(u_i-u_j)(v_i-v_j).
\]
Apply this to \(u_i=\alpha_i\), \(v_i=\psi(\alpha_i+1)\); use \(A^2-B=2\sum_{i<j}\alpha_i\alpha_j\) to obtain the second boxed formula. Finally, \(\psi\) is strictly increasing on the positive real axis because \(\psi'(x)=\sum_{r\ge0}(x+r)^{-2}>0\). Therefore every pairwise bracket is at least one, while every pair weight is positive. The inequality is strict since \(m\ge2\). The bracket is exactly one for every pair if and only if all positive parameters coincide, proving the claimed equality condition. Replacing \(C\) by \(D=1-C\) reverses covariance's sign.

## Verification

`check_covariance.py` is standalone checker source, using only Python's standard library and `mpmath` for its independently evaluated beta-integral tests. It compares the differentiated raw-moment expression with both final formulas using exact rational arithmetic for all ordered integer parameter vectors of lengths two through five with coordinates in \(\{1,2,3,4}\), totaling 1,360 vectors. Each vector checks two formula equalities and strict negativity; symmetric vectors additionally check the closed special case. Four two-category real-parameter configurations use independent direct beta quadratures to high precision, with errors below \(10^{-45}\). These are checks of the proof algebra, not a replacement for the all-parameter analytic argument.

To reproduce, run `python check_covariance.py` from the directory containing the supplied checker. In the verified environment `mpmath` was available; `python` 3.11+ supports the syntax used here.

## Relationship to prior work

Cerquetti (2014), arXiv:1404.3441, Theorem 1 and Theorem 2, presents separate first through third moments for generalized Tsallis indices and Shannon entropy under Gnedin–Pitman models; those separate marginal moments do not determine a cross-moment. The present assertion is specifically a *cross-index* covariance with a universal strict sign for arbitrary heterogeneous, finite Dirichlet parameters. It neither claims to originate Dirichlet mixed moments nor to improve the marginal index formulas. Wolpert and Wolf (1994) supply general beta-integral and Bayesian entropy-moment methods; such an integration method allows the mixed moment to be computed, but does not itself state the pairwise positive decomposition or global sign. Related research on sample richness and unbiased Gini–Simpson diversity measures a different random pair of statistics under iid sampling and does not imply this Dirichlet latent-probability result. Generic multivariate moment formulas are antecedents rather than a novelty claim.

## Limitations

No assertion is made for non-Dirichlet priors, infinite-dimensional random discrete laws, Rényi entropy at orders other than Shannon, or a sign for every pair of monotone diversity functionals. The theorem is an exact first-order covariance statement, not stochastic association or a full joint-law ordering. Older or generalized functional integration formulas could implicitly cover the displayed expression; this historical-priority possibility is not eliminated by a finite literature search. The checks use exact finite cases and high-precision beta integrals, while validity for all real positive parameters follows from the analytic proof. Independent scientific validation has not been performed.

## References

- A. Cerquetti, *Bayesian nonparametric estimation of Tsallis diversity indices under Gnedin–Pitman priors*, arXiv:1404.3441, first public April 14, 2014. https://arxiv.org/abs/1404.3441
- D. H. Wolpert and D. R. Wolf, *Estimating Functions of Probability Distributions from a Finite Set of Samples, Part I: Bayes Estimators and the Shannon Entropy*, arXiv:comp-gas/9403001, first public March 8, 1994. https://arxiv.org/abs/comp-gas/9403001
- A. Cerquetti, *Bayesian nonparametric estimation of Simpson's evenness index under \(\alpha\)-Gibbs priors*, arXiv:1203.1666, first public March 8, 2012. https://arxiv.org/abs/1203.1666
