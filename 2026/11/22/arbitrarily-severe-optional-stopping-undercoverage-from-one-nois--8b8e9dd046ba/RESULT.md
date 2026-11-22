# Arbitrarily severe optional-stopping undercoverage from one noisy Landweber dataset

## Finding

**Theorem (multiscale marginal-coverage collapse).** For any integer \(r\ge 2\) and confidence level \(0<\alpha<1\), there exists an explicit sequence of finite-dimensional symmetric positive-definite linear inverse problems, with one Gaussian observation of dimension \(r\), and \(r\) deterministic Landweber iteration indices, such that each fixed-index, first-coordinate confidence interval has coverage at least \(1-\alpha\) under the standard source condition, but choosing the first interval that excludes the null value zero yields
\[
\lim_{q\to\infty}\Pr_{x^\dagger=0}\{0\in I_{k_{\widehat j}}(Y)\}=(1-\alpha)^r.
\]
Consequently no positive lower coverage bound independent of \(r\) survives this data-dependent first-exclusion rule, even though the *same* observation and *same* coordinate are used throughout. This is not the observation-independent stopping rule in the motivating paper.

## Assumptions and scope

Fix \(r\ge2\), an integer \(q\ge2\), and \(0<\alpha<1\). Write
\[
C_q=\left(\sum_{i=1}^r q^{-2i}\right)^{1/2},\qquad c_i=q^{-i}/C_q.
\]
Choose a real orthogonal \(r\)-by-\(r\) matrix \(V\) whose first row is \((c_1,\dots,c_r)\); for instance the Householder reflection \(V=I-2vv^\top\) with \(v=(e_1-c)/\|e_1-c\|_2\). Set
\[
A_q=V\operatorname{diag}(q^{-2},q^{-4},\ldots,q^{-2r})V^\top,\qquad B_q=A_q^\top A_q,
\]
and let \(Y=A_qx^\dagger+\epsilon\), where \(\epsilon\sim N(0,I_r)\). The admissible source class is \(x^\dagger=B_qw\) with \(\|w\|_2\le1\), and the claimed coverage-collapse calculation takes \(x^\dagger=0\). Start with \(x^{(0)}=0\) and apply
\[
x^{(k+1)}=x^{(k)}+\omega A_q^\top(Y-A_qx^{(k)}),\qquad \omega=q^4/2.
\]
The fixed-index marginal interval for coordinate one is
\[
I_k(Y)=\left[x^{(k)}_1-z_\alpha\sqrt{v_k}-b_k,\ x^{(k)}_1+z_\alpha\sqrt{v_k}+b_k\right],
\]
where \(z_\alpha=\Phi^{-1}(1-\alpha/2)\), \(v_k=\operatorname{Var}(x^{(k)}_1)\) under the unit Gaussian noise, and
\[
b_k=2q^{-4}\frac{k^k}{(k+1)^{k+1}}.
\]
The latter is the standard global bias upper bound for source exponent and radius \(\nu=M=1\), not an estimated or tuned bias. At candidate indices \(k_j=2q^{4(j-1)}\) for \(j=1,\ldots,r\), let \(\widehat j\) be the smallest index \(j\) for which \(0\notin I_{k_j}(Y)\); if no such index exists, set \(\widehat j=r\).

## Proof

**1. Marginal validity.** The singular values of \(A_q\) are \(s_i=q^{-2i}\), so \(\omega=1/(2s_{\max}^2)\). For any fixed \(k\) and \(x^\dagger=B_qw\) in the source class, the reconstruction bias is \(-(I-\omega B_q)^kx^\dagger\), with Euclidean norm at most \(b_k\) since
\[
\max_{0\le t\le1/2}2q^{-4}t(1-t)^k\le 2q^{-4}\frac{k^k}{(k+1)^{k+1}}.
\]
The random part of the first coordinate is centered Gaussian with variance \(v_k>0\). The Gaussian quantile event and the bias bound imply \(\Pr_{x^\dagger}(x^\dagger_1\in I_k)\ge1-\alpha\) for each *fixed* \(k\).

**2. Exact modal formula.** With \(\xi=V^\top\epsilon\sim N(0,I_r)\), define
\[
u_{ij}(q)=1-\left(1-\tfrac12q^{-4(i-1)}\right)^{k_j}.
\]
At the zero source, direct solution of the Landweber recursion yields
\[
x^{(k_j)}_1=\frac1{C_q}\sum_{i=1}^r q^i u_{ij}(q)\xi_i,\qquad
v_{k_j}=\frac1{C_q^2}\sum_{i=1}^r q^{2i}u_{ij}(q)^2.
\]
The diagonal filter satisfies \(u_{11}=3/4\) and \(u_{jj}\to1-e^{-1}\) for each fixed \(j\ge2\), as \(q\to\infty\); in particular \(u_{jj}\ge1-e^{-1}\).

**3. Separation of standardized noise directions.** For \(i<j\), use \(u_{ij}\le1\) to get
\[
\frac{q^iu_{ij}}{q^ju_{jj}}\le\frac{q^{-(j-i)}}{1-e^{-1}}.
\]
For \(i>j\), Bernoulli's inequality implies \(u_{ij}\le k_jq^{-4(i-1)}/2=q^{-4(i-j)}\), and therefore
\[
\frac{q^iu_{ij}}{q^ju_{jj}}\le\frac{q^{-3(i-j)}}{1-e^{-1}}.
\]
For each fixed \(r\), the coefficient matrix of the standardized Gaussian vector \(Z_j=x_1^{(k_j)}/\sqrt{v_{k_j}}\) converges to the identity matrix. Hence \((Z_1,\ldots,Z_r)\) converges jointly in distribution to \(r\) independent standard normals.

**4. Bias padding disappears after standardization.** Since \(k^k/(k+1)^{k+1}\le1/(k+1)\) and \(\sqrt{v_{k_j}}\ge q^ju_{jj}/C_q\),
\[
0\le\frac{b_{k_j}}{\sqrt{v_{k_j}}}\le
\frac{2C_qq^{-4-j}}{(k_j+1)(1-e^{-1})}\longrightarrow0.
\]
Thus each fixed-index null coverage converges to \(1-\alpha\). Crucially, the selection rule returns a covering interval **if and only if every candidate interval covers zero**. The simultaneous event is
\[
\bigcap_{j=1}^r\left\{|Z_j|\le z_\alpha+b_{k_j}/\sqrt{v_{k_j}}\right\}.
\]
Continuity of the limiting multivariate normal law and the preceding bounds give probability \((1-\alpha)^r\). Letting \(r\) grow proves arbitrarily poor selected coverage, while keeping every individual fixed-index guarantee intact. \(\square\)

## Verification

The bundled `check_landweber.py` constructs the Householder matrix and covariance-standardized spectral filters directly, compares closed-form iterates with matrix Landweber recursions, checks convergence of the correlation matrix toward the identity, and tests a Gaussian Monte Carlo instance. It is executed with `python check_landweber.py` (NumPy required). Exact asymptotic and all-parameter assertions follow from the proof, not the finite computation. At \(r=3\), \(\alpha=0.05\), the limiting adaptive null coverage is \(0.95^3=0.857375\), below nominal \(0.95\).

## Relationship to prior work

Abhishek and Holman, arXiv:2610.00882v1, give the source-condition bias envelope (Lemma 3.4, equation 3.18) and the fixed-index pixelwise interval (equation 3.20). Their actual stopping index in equation 3.21 and the randomized counterpart are computed independently of the observed data. The construction here instead studies an explicitly *data-dependent, adversarial first-exclusion rule*. It does not refute their prescribed procedure. Blanchard, Hoffmann and Reiß (arXiv:1606.07702) develop adaptive stopping risk theory, not this joint marginal coverage law. Batlle and collaborators (arXiv:2510.11708) give simultaneous confidence calibration for multiple inverse-problem functionals; this reinforces the general need for simultaneous rather than separate calibration but does not supply the stated temporal, single-coordinate multiscale example. The broad danger of selecting among marginal intervals is well known; the specific constructive asymptotic separation of Landweber iterates on one reused dataset is the substantive assertion.

## Limitations

This is a family of deliberately ill-conditioned finite-dimensional positive-definite operators, with dimension increasing when arbitrarily small coverage is sought. The failure is for a deliberately adversarial data-dependent first-exclusion stopping rule, **not** for ordinary noise-level-based offline stopping or the observed-data-independent rules of the motivating study. The experiment assumes exact covariance and known Gaussian noise variance; it excludes complications from randomized covariance approximation. It establishes neither failure of all adaptive stopping rules nor priority over every unindexed related construction. Independent mathematical audit has not been performed.

## References

1. A. Abhishek and S. Holman, *Uncertainty Quantification for Landweber Iteration with Randomized Normal-Operator Approximation*, arXiv:2610.00882v1 (first public 2026-10-01), https://arxiv.org/html/2610.00882v1.
2. G. Blanchard, M. Hoffmann and M. Reiß, *Optimal adaptation for early stopping in statistical inverse problems*, arXiv:1606.07702, https://arxiv.org/pdf/1606.07702.
3. P. Batlle and collaborators, *Simultaneous Frequentist Calibration of Confidence Regions for Multiple Functionals in Constrained Inverse Problems*, arXiv:2510.11708v1, https://arxiv.org/html/2510.11708v1.
