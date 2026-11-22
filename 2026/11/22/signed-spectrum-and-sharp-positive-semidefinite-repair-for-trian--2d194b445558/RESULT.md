# Signed spectrum and sharp positive-semidefinite repair for triangular Gram split products

## Finding

Let \(d\ge2\) and let \(v_1,\ldots,v_d\in\mathbb R^n\). The triangularly retained product of a split Gram matrix is
\[
T_d=\sum_{\substack{1\le r,s\le d\\r+s\le d+1}}v_rv_s^\mathsf T=BH_dB^\mathsf T,
\qquad B=[v_1\ \cdots\ v_d],\qquad (H_d)_{rs}=\mathbf1_{\{r+s\le d+1\}}.
\]
The full split Gram matrix \(G=(\sum_{r=1}^{d}v_r)(\sum_{r=1}^{d}v_r)^\mathsf T\) is positive semidefinite. In contrast, the entire ordered spectrum of the symmetric coefficient matrix is
\[
\lambda_k(H_d)=\frac{(-1)^{k-1}}{2\sin((2k-1)\pi/(4d+2))},\qquad k=1,\ldots,d.
\]
Consequently, whenever \(B\) has column rank \(d\), the inertia of \(T_d\), with zero eigenvalues included, is exactly
\[
\big(\lceil d/2\rceil,\lfloor d/2\rfloor,n-d\big).
\]
In particular, every such \(T_d\) is indefinite, even when all entries of the split vectors are strictly positive.

The exact least **nonnegative** coefficient-diagonal repair \(\eta\sum_{r=1}^d v_rv_r^\mathsf T\), guaranteeing positive semidefiniteness for **every** split matrix \(B\), is
\[
\eta_*(d)=\frac{1}{2\sin(3\pi/(4d+2))} \quad(d\ge2),
\qquad \eta_*(d)\sim\frac{2d+1}{3\pi}.
\]
Furthermore, if one may only add previously omitted split products, keeping symmetric binary coefficients, **every** omitted product must be restored to guarantee positive semidefiniteness for all possible split vectors: the complete all-pairs Gram coefficient is the unique safe supermask of the triangular one.

## Assumptions and scope

All statements are in real, exact arithmetic and refer to the explicitly defined ideal split-product surrogate. The ordering of the \(d\) arbitrary vectors determines the triangular retention rule. The inertia formula requires \(n\ge d\) and rank \(B=d\); the universal repair and unique-completion statements allow arbitrary \(B\) and take the quantifier over all \(n\ge d\). Neither theorem asserts that an arbitrary chosen split family is produced by a particular finite-precision Ozaki splitting routine. The full Gram comparator contains exactly these \(d\) vectors, with no further split tail. The diagonal-repair statement allows \(\eta\ge0\), and does not assert good approximation accuracy after repair.

## Proof

**1. Signed spectrum.** For \(k=1,\ldots,d\), set
\[
\theta_k=\frac{(2k-1)\pi}{2d+1},\qquad u^{(k)}_i=\sin((d+1-i)\theta_k),\quad i=1,\ldots,d.
\]
The \(i\)-th entry of \(H_du^{(k)}\) is \(\sum_{j=1}^{d+1-i}\sin((d+1-j)\theta_k)=\sum_{m=i}^{d}\sin(m\theta_k)\). Using the finite sine-sum identity, this is
\[
\frac{\cos((i-\tfrac12)\theta_k)-\cos((d+\tfrac12)\theta_k)}{2\sin(\theta_k/2)}
=\frac{\cos((i-\tfrac12)\theta_k)}{2\sin(\theta_k/2)}.
\]
Since \(\cos((d+\tfrac12)\theta_k)=0\) and
\(u^{(k)}_i=(-1)^{k-1}\cos((i-\tfrac12)\theta_k)\), the displayed eigenvalue formula follows. The \(d\) eigenvalues have distinct absolute values, since \(0<\theta_1<\cdots<\theta_d<\pi\) and sine is strictly increasing on \((0,\pi/2)\). Hence they exhaust the real symmetric matrix spectrum, with exactly alternating signs and the stated positive/negative counts.

**2. Split-vector inertia.** The congruence \(T_d=BH_dB^\mathsf T\), for full-column-rank \(B\), has precisely the same nonzero inertia as \(H_d\) by Sylvester's law of inertia; the remaining \(n-d\) eigenvalues are zero. This is not a claim about arbitrary rank-deficient \(B\).

**3. Optimal coefficient repair.** The most negative eigenvalue is the second one, namely \(-1/[2\sin(3\pi/(4d+2))]\). Thus \(H_d+\eta I_d\succeq0\) precisely when \(\eta\ge\eta_*(d)\). Such a coefficient PSD matrix stays PSD after congruence by any \(B\). Conversely \(B=I_d\) witnesses failure for any smaller \(\eta\), giving necessity under the universal quantifier. The large-depth asymptotic follows by \(\sin t\sim t\).

**4. No partial binary completion.** Let \(M\) be a symmetric \(d\)-by-\(d\) binary matrix with \(M_{rs}=1\) wherever \((H_d)_{rs}=1\). Assume \(BMB^\mathsf T\succeq0\) for every \(B\); taking \(B=I_d\) gives \(M\succeq0\). Because the first row and column of \(H_d\) consist entirely of ones, \(M_{11}=M_{1j}=1\). Every two-by-two principal PSD minor implies \(M_{jj}\ge1\). Since diagonal entries are binary, \(M_{jj}=1\). Now \((e_1-e_j)^\mathsf T M(e_1-e_j)=0\), and for a PSD matrix zero quadratic form entails \(M(e_1-e_j)=0\). Consequently every column equals the first and \(M\) is the all-ones matrix. The number of additional ordered split products required is exactly \(d(d-1)/2\).

**5. Arbitrarily small relative truncation error with negative spectrum.** Let \(0<q<1\), \(n=d\), and
\[
v_r=q^{r-1}(\mathbf1+e_r),\qquad r=1,\ldots,d.
\]
Every entry of every vector is strictly positive and \(B=(I+\mathbf1\mathbf1^\mathsf T)\operatorname{diag}(1,q,\ldots,q^{d-1})\) is invertible. Hence \(T_d\) has \(\lfloor d/2\rfloor\) negative eigenvalues for every \(q>0\). Each omitted ordered pair has \(r+s\ge d+2\), and \(\|v_rv_s^\mathsf T\|_2=(d+3)q^{r+s-2}\le(d+3)q^d\). There are exactly \(d(d-1)/2\) such pairs, so
\[
\|G-T_d\|_2\le\frac{d(d-1)(d+3)}{2}q^d,
\quad \|G\|_2\ge\|v_1\|_2^2=d+3,
\quad \frac{\|G-T_d\|_2}{\|G\|_2}\le\frac{d(d-1)}2q^d\longrightarrow0.
\]
The comparison norm is nonzero. For \(d=2\), choosing \(q=1/10\) gives \(T_2=\begin{pmatrix}22/5&5/2\\5/2&7/5\end{pmatrix}\) with determinant \(-9/100\), whereas \(G\) is an outer product and PSD.

## Verification

The standalone file `verify_splitmask.py` runs directly with Python and NumPy and prints `VERIFY_OK 1870` in the delivered test environment. It checks the full coefficient eigenvalue spectrum, trigonometric eigenpairs, inertia and squared matrix identity for depths one through forty; compares finite Gram examples with their explicit bound; checks an exact-rational two-dimensional determinant family; and enumerates small binary retention supermasks. The formulas for unbounded depth, arbitrary real split vectors, and all masks follow from the analytical proof above, not these finite experiments.

## Relationship to prior work

Carson and Ma, *Adaptive accuracy-driven splitting in Ozaki matrix multiplication and application to block LU factorization* (arXiv:2611.03158v1, 2026), equation (5), specifies precisely the triangular product schedule used here, in the context of normwise/componentwise accuracy of matrix products and block LU. That paper does not claim that this split-product schedule preserves the PSD cone for Gram inputs. The present theorem is a special *Gram specialization* of that schedule, not a general modification or correctness criticism of its algorithm.

The sine spectrum is closely related to **classical discrete-integration and Brownian covariance spectral theory**, not wholly independent of it: indeed \((H_d^2)_{ij}=\min(d+1-i,d+1-j)\), the reversal of the discrete Brownian kernel in Sra (2014, Proposition 3.2). That result already gives the eigenvalue magnitudes after squaring. The signed eigenvectors, full-rank Gram inertia, sharp coefficient-diagonal PSD repair, and rigidity of product-retention completion are combined here as a numerical linear-algebra consequence of the triangular product schedule. Ochiai et al. (2014) treat different anti-triangular matrices with a special diagonal-eigenvalue property; they do not characterize the specified triangular Gram coefficient mask and its admissible PSD completions.

## Limitations

The ideal split vectors are not required to satisfy the discrete-bit extraction constraints of a specific Ozaki implementation. The result does not measure floating-point roundoff, input-dependent cancellation, or application-level performance, and it makes no claim that an actual computed matrix always has the ideal surrogate's inertia. A nonnegative coefficient-diagonal repair can worsen approximation error, so it is not proposed as an optimal accuracy-preserving implementation. Historical priority relative to unindexed earlier matrix-mask or structured Hankel results requires independent literature assessment. The analysis does not classify rank-deficient split families.

## References

1. Erin Carson and Yuxin Ma, *Adaptive accuracy-driven splitting in Ozaki matrix multiplication and application to block LU factorization*, arXiv:2611.03158v1 (2026-11-02). https://arxiv.org/html/2611.03158v1 .
2. Suvrit Sra, *Explicit diagonalization of an anti-triangular Cesàro matrix*, arXiv:1411.4107 (2014), particularly Section 3.2 on the finite Brownian kernel. https://arxiv.org/abs/1411.4107 .
3. Hiroyuki Ochiai, Makiko Sasada, Tomoyuki Shirai, Takashi Tsuboi, *Eigenvalue problem for some special class of anti-triangular matrices*, arXiv:1403.6797v1 (2014). https://arxiv.org/html/1403.6797v1 .
