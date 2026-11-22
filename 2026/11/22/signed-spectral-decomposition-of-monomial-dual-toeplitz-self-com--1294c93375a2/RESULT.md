# Signed spectral decomposition of monomial dual Toeplitz self-commutators on weighted harmonic Bergman complements

## Finding
For every real \(\alpha>-1\) and integer \(m\ge1\), the dual Toeplitz operator \(S_m=P_\alpha M_{z^m}|_{\mathcal K_\alpha}\), where \(\mathcal K_\alpha\) is the orthogonal complement of the beta-weighted harmonic Bergman space, has a compact, trace-class self-commutator \(K_{\alpha,m}=S_m^*S_m-S_mS_m^*\). Its **complete nonzero spectrum** consists of explicitly determined signed pairs: one opposite-sign pair for every angular degree \(k\ge m\), plus two opposite-sign pairs for every \(1\le k<m\). The zero eigenvalue has infinite multiplicity, and the positive and negative eigenvalue multisets coincide, including multiplicities.

Define normalized radial moments
\[
h_j=\frac{\Gamma(j+1)\Gamma(\alpha+2)}{\Gamma(j+\alpha+2)},\qquad j=0,1,2,\ldots.
\]
For \(k\ge m\), set
\[
b_k=\frac{h_{k+2m}}{h_{k+m}}-\frac{h_{k+m}}{h_k}>0.
\]
For \(1\le k<m\), put
\[
A_k=\frac{h_{2m-k}-h_m^2/h_k}{h_{m-k}},\quad
B_k=\frac{h_{k+2m}-h_{k+m}^2/h_k}{h_{k+m}},\quad
G_k=\frac{h_{2m}-h_m h_{k+m}/h_k}{\sqrt{h_{m-k}h_{k+m}}},
\]
\[
\lambda_{\pm,k}=\frac{A_k-B_k\pm\sqrt{(A_k+B_k)^2-4G_k^2}}2.
\]
For these central degrees, \(\lambda_{+,k}>0>\lambda_{-,k}\). The nonzero eigenvalue multiset of \(K_{\alpha,m}\) is exactly
\[
\left\{+b_k,-b_k:k\ge m\right\}
\ \cup\
\left\{\lambda_{+,k},\lambda_{-,k},-\lambda_{+,k},-\lambda_{-,k}:1\le k<m\right\}.
\]
The sign symmetry is exact, not merely asymptotic. If \(N_\pm(t)\) counts eigenvalues greater than \(t\) of the positive and negative parts respectively, then
\[
\lim_{t\downarrow0}\sqrt t\,N_\pm(t)=m\sqrt{\alpha+1},\qquad
s_n(K_{\alpha,m})\sim\frac{4m^2(\alpha+1)}{n^2}.
\]
Consequently \(K_{\alpha,m}\in\mathcal S_p\) exactly for \(p>1/2\), including \(0<p<1\) quasi-Schatten classes, and its trace is zero. Its **exact trace norm** is a finite moment formula:
\[
\boxed{
\|K_{\alpha,m}\|_{\mathcal S_1}
=2\left[m-\sum_{k=m}^{2m-1}\frac{h_{k+m}}{h_k}
+\sum_{k=1}^{m-1}\sqrt{(A_k+B_k)^2-4G_k^2}\right].}
\]
The central angular blocks can control the operator norm, rather than the infinite tail. For instance, for \(\alpha=0,m=2\) the central eigenvalues in angular degree one are \(-1/18\pm\sqrt7/45\); the precise norm is
\[
\boxed{\|K_{0,2}\|=\frac1{18}+\frac{\sqrt7}{45}>\frac4{35}=b_2.}
\]

## Assumptions and scope
Let \(\mathbb D\) be the disk and let
\[
d\mu_\alpha(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha\,dx\,dy,\quad\alpha>-1.
\]
Let \(\mathcal H_\alpha\subset L^2(\mathbb D,d\mu_\alpha)\) be its closed complex harmonic subspace and let \(Q_\alpha\) be its orthogonal projection. Set \(P_\alpha=I-Q_\alpha\), \(\mathcal K_\alpha=P_\alpha L^2\). Since \(z^m\) is bounded on the disk, \(S_m=P_\alpha M_{z^m}|_{\mathcal K_\alpha}\) is a bounded operator. Our self-commutator convention is \(K_{\alpha,m}=S_m^*S_m-S_mS_m^*\). The spectral theorem includes multiplicities, including coincident eigenvalues from different angular sectors; \(\mathcal S_p\) denotes the usual Schatten or quasi-Schatten ideal. The integer \(m\) is fixed for the large-index asymptotics, and \(\alpha\) is fixed with \(\alpha>-1\). No conclusion is asserted for general symbols or non-beta radial measures.

## Proof
**1. Normal ambient multiplication and angular ranks.** Write \(M=M_{z^m}\) on ambient \(L^2\). Multiplication operators are normal, so \(M^*M=MM^*\). Compressing to \(\mathcal K_\alpha\), inserting \(P_\alpha+Q_\alpha=I\), and cancelling the normal ambient terms gives the exact operator identity
\[
K_{\alpha,m}=P_\alpha M Q_\alpha M^*P_\alpha-P_\alpha M^*Q_\alpha MP_\alpha\quad\text{on }\mathcal K_\alpha.
\]
For every integer angular frequency \(k\), the harmonic subspace in that frequency is one-dimensional, spanned by
\[
u_k(re^{i\theta})=\frac{r^{|k|}e^{ik\theta}}{\sqrt{h_{|k|}}}.
\]
Let \(P_k\) be the projection onto the orthogonal complement of \(u_k\) in the angular sector \(k\). The angular sector of \(K\) is a signed difference of rank-one operators:
\[
K_k=|v_{k,-}\rangle\langle v_{k,-}|-|v_{k,+}\rangle\langle v_{k,+}|,\quad
v_{k,-}=P_k Mu_{k-m},\quad v_{k,+}=P_k M^*u_{k+m}.
\]
Thus \(\operatorname{rank}K_k\le2\). Complex conjugation preserves the radial measure, interchanges the two generators for \(k\) and \(-k\), and sends \(K_k\) antiunitarily to \(-K_{-k}\). The sector \(k=0\) vanishes: both generators are exactly \(r^{2m}/\sqrt{h_m}\) after the same radial projection. These identities prove exact sign pairing.

**2. Infinite tails and positivity.** For \(k\ge m\), multiplication of \(u_{k-m}\) by \(z^m\) is a scalar multiple of \(u_k\), so \(v_{k,-}=0\). Direct moments give
\[
\|v_{k,+}\|^2=\frac{h_{k+2m}}{h_{k+m}}-\frac{h_{k+m}}{h_k}=b_k.
\]
The ratio \(r_m(k)=h_{k+m}/h_k\) is strictly increasing: its product expression and the strictly increasing consecutive ratios \(h_{j+1}/h_j=(j+1)/(j+\alpha+2)\) prove this for \(\alpha>-1\). Therefore \(b_k=r_m(k+m)-r_m(k)>0\). Each positive-frequency tail sector supplies exactly one eigenvalue \(-b_k\), and its negative counterpart supplies \(+b_k\).

**3. Central signed pairs.** Fix \(1\le k<m\). Apart from normalization, the two generators in the positive angular sector are the radial powers \(r^{2m-k}\) and \(r^{k+2m}\), each projected perpendicular to \(r^k\). Taking normalized radial moments gives the two squared norms \(A_k,B_k\) and their real mutual inner product \(G_k\). The powers \(r^k,r^{2m-k},r^{2m+k}\) are linearly independent on \((0,1)\), so the projected generators are linearly independent. Hence \(A_kB_k>G_k^2\) and \(A_k,B_k>0\). A difference of two rank-one forms on their two-dimensional span has trace \(A_k-B_k\) and determinant \(-(A_kB_k-G_k^2)\), giving the two displayed simple real eigenvalues of opposite sign. The negative-frequency sector supplies their negatives. All other radial directions lie in the kernel, and each angular sector has infinite-dimensional radial orthogonal complement to these at most two generators; thus \(\dim\ker K=\infty\).

**4. Spectral tails and ideal threshold.** The moment ratio has the exact gamma-product representation
\[
r_m(k)=\prod_{j=1}^{m}\frac{k+j}{k+\alpha+1+j}
=1-\frac{m(\alpha+1)}k+O_{\alpha,m}(k^{-2}).
\]
Expanding one further term and subtracting the shifted ratio yields
\[
b_k=r_m(k+m)-r_m(k)=m^2(\alpha+1)k^{-2}+O_{\alpha,m}(k^{-3}).
\]
The finitely many central eigenvalues do not affect asymptotic counts. For each sign, exactly one tail eigenvalue of magnitude \(b_k\) occurs for each \(k\ge m\), so \(N_\pm(t)\sim m\sqrt{(\alpha+1)/t}\) as \(t\downarrow0\). Twice as many singular values give \(s_n\sim4m^2(\alpha+1)/n^2\), without assuming that every low-index tail term is ordered. Summing \(b_k^p\) proves the strict \(p>1/2\) Schatten threshold, as well as trace class and compactness. Pairing yields trace zero.

**5. Exact nuclear norm and a norm-dominating central example.** The trace norm of the central positive angular block is \(\lambda_{+,k}-\lambda_{-,k}=\sqrt{(A_k+B_k)^2-4G_k^2}\); the negative block contributes the same. For the infinite tail, the identity \(b_k=r_m(k+m)-r_m(k)\) telescopes:
\[
\sum_{k=m}^{N}b_k
=\sum_{k=N+1}^{N+m}r_m(k)-\sum_{k=m}^{2m-1}r_m(k)
\longrightarrow m-\sum_{k=m}^{2m-1}\frac{h_{k+m}}{h_k}.
\]
Doubling for the negative frequencies proves the claimed finite trace-norm expression. With \(\alpha=0,m=2,k=1\), exact rational moments yield \(A_1=1/18\), \(B_1=1/6\), \(G_1^2=2/225\). Therefore \(\lambda_{\pm,1}=-1/18\pm\sqrt7/45\). Every tail magnitude is \(b_k=4/((k+3)(k+5))\), strictly decreasing in \(k\ge2\), and its maximum is \(4/35\). Both central sectors have maximum absolute eigenvalue \(1/18+\sqrt7/45\), which is strictly greater than \(4/35\). This proves the exact operator-norm example.

## Verification
The accompanying standalone file `checker.py` uses only the Python standard library. Run `python3 checker.py` after extracting it beside this file. It checks the beta-moment log-convexity, direct quadratic forms of compressed multipliers against an independently expressed rank-two angular model, strict central Gram determinants, tail signs, exact telescoping, and the rational/radical example for a range of weights and degrees. The observed run returned `VERIFICATION_OK 177256`. These finitely many assertions are supporting consistency checks, not proofs of the infinite spectral and asymptotic statements; the full proof is given above.

## Relationship to prior work
Wang and Zhao (arXiv:2101.00552; first public 2021-01-03) establish that hyponormal dual Toeplitz operators on the orthogonal complement of the harmonic Bergman space are normal, including a qualitative monomial characterization. The present result quantifies the indefinite self-commutator by giving every nonzero eigenvalue, an exact nuclear norm and sharp ideal membership across beta weights; those conclusions are not stated in their analyzed article. Yang and Lu (2015) characterize commuting dual Toeplitz operators with harmonic symbols, while Liu (2024) studies zero products and commutativity. Their hypotheses and conclusions do not imply this signed spectral list.

The related result *Paired self-commutator spectra of monomial Toeplitz operators on weighted harmonic Bergman spaces* studies compression **to the harmonic subspace**, not the dual compression to its complement. Its one-dimensional angular blocks and the present two-dimensional central blocks are mathematically different. Already at \(\alpha=0,m=1\), the former has operator norm \(1/6\) whereas the complement self-commutator has norm \(1/12\). Likewise, *A three-regime signed Schatten law for mixed-monomial dual Toeplitz self-commutators* concerns a different complement, that of the **analytic** Bergman space, with different symbols; it does not imply the present formulas. These sources inform the comparison but do not establish uniqueness or historical priority.

## Limitations
The exact theorem is restricted to a single analytic monomial and beta-weighted disk area measures. It does not cover arbitrary polynomial symbols or other radial weights. For general \(m,\alpha\), the theorem provides a complete eigenvalue formula and hence a variational way to calculate the operator norm, but does not claim a simplified closed norm formula; the explicit norm formula is for \(m=2,\alpha=0\). The mathematical proof has not undergone independent external validation. An earlier Peng–Zhao paper (2021) on the same ambient complement reports spectral structure of the *dual Toeplitz operator itself*; its full text was inaccessible during comparison, leaving a genuine historical-priority risk. Finite code checks do not resolve this risk.

## References
1. C. Wang and X. Zhao, *Hyponormal dual Toeplitz operators on the orthogonal complement of the harmonic Bergman space*, arXiv:2101.00552 (first public 2021-01-03), https://arxiv.org/abs/2101.00552.
2. J. Yang and Y. Lu, *Commuting dual Toeplitz operators on the harmonic Bergman space*, Science China Mathematics 58 (2015), 1461–1472, https://doi.org/10.1007/s11425-014-4940-x.
3. L. Liu, *Dual Toeplitz operators on the orthogonal complement of the harmonic Bergman space*, AIMS Mathematics 9 (2024), 25413–25437, https://doi.org/10.3934/math.20241241.
4. Y. Peng and X. Zhao, *Dual Toeplitz operators on the orthogonal complement of the harmonic Bergman space*, Acta Mathematica Sinica, English Series 37 (2021), 1143–1155, https://doi.org/10.1007/s10114-021-0315-8 (full text not inspected).
5. *Paired self-commutator spectra of monomial Toeplitz operators on weighted harmonic Bergman spaces*, published mathematical result (2026), distinct harmonic-subspace compression.
6. *A three-regime signed Schatten law for mixed-monomial dual Toeplitz self-commutators*, published mathematical result (2026), distinct analytic-Bergman complement.
