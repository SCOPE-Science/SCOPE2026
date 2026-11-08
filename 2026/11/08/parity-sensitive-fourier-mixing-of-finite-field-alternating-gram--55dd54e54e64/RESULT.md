# Parity-sensitive Fourier mixing of finite-field alternating Gram walks

## Finding
For every fixed finite field, a random walk on alternating matrices obtained by adding independent decomposable bivectors has an exact finite-time Fourier spectrum and chi-square divergence. It mixes in total variation in a bounded window about half the matrix dimension. Its fixed-offset chi-square profile depends on whether the dimension is even or odd.

Let \(q\) be a prime power, \(n\ge2\), and let \(P_{n,t}\) be the law after \(t\) independent updates. For all integer \(t\ge0\),
\[
\chi^2(P_{n,t}\Vert U_n)=\sum_{r=1}^{\lfloor n/2\rfloor}
{n\brack 2r}_q q^{r(r-1)}\Big(\prod_{j=1}^r(q^{2j-1}-1)\Big)q^{-4rt}.
\]
Here \({n\brack k}_q\) is the Gaussian binomial coefficient. The complete convolution eigenvalue of any character of rank \(2r\) is \(q^{-2r}\).

For each fixed \(q\) and integer \(s\), with \(m=\lfloor n/2\rfloor\) and \(t=m+s\), the even-dimensional and odd-dimensional chi-square limits respectively are
\[
F_q^{\mathrm{even}}(s)=\sum_{r=1}^{\infty}\frac{q^{-2r^2-r-4rs}}{\prod_{j=1}^r(1-q^{-2j})},\qquad
F_q^{\mathrm{odd}}(s)=\sum_{r=1}^{\infty}\frac{q^{-2r^2+r-4rs}}{\prod_{j=1}^r(1-q^{-2j})}.
\]
The sums converge absolutely and are positive; since every corresponding odd term is \(q^{2r}\) times the even term, the profiles differ strictly. For any integer \(a_n\to\infty\) such that \(0\le a_n\le\lfloor n/2\rfloor\),
\[
\lVert P_{n,\lfloor n/2\rfloor+a_n}-U_n\rVert_{\mathrm{TV}}\to0,
\qquad
\lVert P_{n,\lfloor n/2\rfloor-a_n}-U_n\rVert_{\mathrm{TV}}\to1.
\]

## Assumptions and scope
Let \(G_n=\operatorname{Alt}_n(\mathbb F_q)\) be the *additive* group of matrices with \(A^{\mathsf T}=-A\) and diagonal zero, including in characteristic two. Put \(N=\binom n2\), so \(\lvert G_n\rvert=q^N\). Choose each \(u_j,v_j\) independently and uniformly from \(\mathbb F_q^n\), and set
\[
A_{n,t}=\sum_{j=1}^t(u_jv_j^{\mathsf T}-v_ju_j^{\mathsf T}).
\]
The empty sum is zero. Let \(U_n\) be uniform on \(G_n\), and define \(\chi^2(P\Vert U)=\sum_{g\in G_n}(P(g)-U(g))^2/U(g)\). Characteristic two uses the same matrix expression, where subtraction equals addition. All asymptotics hold for fixed \(q\) while \(n\) grows. No simultaneous large-field limit or fixed-offset total-variation profile is claimed.

## Proof
**1. Fourier eigenvalues.** Fix a nontrivial additive character \(\psi\) of \(\mathbb F_q\). Each matrix \(B\in G_n\) labels a character
\[
\gamma_B(A)=\psi\Big(\sum_{1\le i<j\le n}B_{ij}A_{ij}\Big).
\]
The coordinate pairing is perfect, so these are all \(q^N\) characters. With \(E(u,v)=uv^{\mathsf T}-vu^{\mathsf T}\), one has
\[
\sum_{i<j}B_{ij}E(u,v)_{ij}=u^{\mathsf T}Bv.
\]
Average first over uniform \(v\): this character has expectation one if \(u\) lies in \(\ker B\) and zero otherwise. Thus
\[
\mathbb E\,\gamma_B(E(u,v))=\frac{\lvert\ker B\rvert}{q^n}=q^{-\operatorname{rank}B}.
\]
An alternating matrix has even rank \(2r\), including in characteristic two. Hence the Fourier convolution eigenvalues are exactly \(q^{-2r}\), \(0\le r\le\lfloor n/2\rfloor\). In particular, every nonprincipal eigenvalue is at most \(q^{-2}<1\), which also establishes convergence to uniform.

**2. Exact multiplicities.** An alternating matrix of rank \(2r\) has a radical of dimension \(n-2r\). Choosing this radical can be done in \({n\brack 2r}_q\) ways. On the quotient, the form must be nondegenerate, and the number of such alternating forms on a labeled \(2r\)-space is
\[
\frac{\lvert\operatorname{GL}_{2r}(\mathbb F_q)\rvert}{\lvert\operatorname{Sp}_{2r}(\mathbb F_q)\rvert}
=q^{r(r-1)}\prod_{j=1}^r(q^{2j-1}-1).
\]
Every form with a prescribed radical is uniquely induced from its quotient. Therefore, the multiplicity is
\[
N_{n,q}(2r)={n\brack 2r}_q q^{r(r-1)}\prod_{j=1}^r(q^{2j-1}-1).
\]
This includes \(N_{n,q}(0)=1\). Orthogonality of characters gives the stated chi-square formula by finite-group Plancherel, for **every** \(t\ge0\), including the point-mass initial state.

**3. Two limiting profiles.** The same multiplicity has the factorization
\[
N_{n,q}(2r)=q^{2rn-2r^2-r}
\frac{\prod_{i=0}^{2r-1}(1-q^{i-n})}{\prod_{j=1}^r(1-q^{-2j})}.
\]
For fixed \(r\), the numerator product tends to one as \(n\to\infty\). If \(n=2m\), substitution of \(t=m+s\) gives the exponent \(-2r^2-r-4rs\); if \(n=2m+1\), it gives \(-2r^2+r-4rs\). For all \(n\), the numerator product is between zero and one, and \(\prod_{j\ge1}(1-q^{-2j})>0\); a quadratic Gaussian majorant in \(r\) proves dominated convergence. This yields both series and their strict inequality.

**4. The upper total-variation bound.** For integer \(a_n\to\infty\) and \(t=\lfloor n/2\rfloor+a_n\), the same majorant with the extra factor \(q^{-4ra_n}\) gives \(\chi^2(P_{n,t}\Vert U_n)\to0\). The standard inequality \(\lVert P-U\rVert_{\mathrm{TV}}\le\frac12\sqrt{\chi^2(P\Vert U)}\) proves the upper cutoff bound.

**5. The lower total-variation bound.** Every update has matrix rank at most two, so \(\operatorname{rank}A_{n,t}\le2t\). At \(t=\lfloor n/2\rfloor-a_n\), the radical of \(A_{n,t}\) has dimension at least \(d_n=n-2t\ge2a_n\to\infty\). By contrast, if \(B\) is uniformly distributed on \(G_n\) and \(W\subset\mathbb F_q^n\) is a fixed \(d\)-dimensional subspace, the conditions \(W\subset\ker B\) impose exactly \(d(n-d)+d(d-1)/2\) independent linear constraints on the alternating-form coefficients. Therefore,
\[
\mathbb P_{U_n}(\dim\ker B\ge d)
\le {n\brack d}_q q^{-d(n-d)-d(d-1)/2}
\le C_q\,q^{-d(d-1)/2},
\]
where \(C_q=\prod_{i=1}^{\infty}(1-q^{-i})^{-1}<\infty\), independent of \(n,d\). Set \(d=d_n\). This event has probability one for the walk and probability tending to zero under \(U_n\), proving the lower cutoff bound.

## Verification
A standalone Python-standard-library checker (`check_alternating.py`) reconstructs alternating matrices over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), directly computes their ranks, and checks the rank multiplicities against the exact group-quotient formula. For the feasible pairs it enumerates every ordered vector pair \((u,v)\), forms the one-step distribution, verifies every Fourier eigenvalue directly, then computes two- and three-step convolution with exact rational arithmetic and compares the complete chi-square divergence to the theorem. It explicitly uses genuine \(\mathbb F_4\) extension-field arithmetic, not reduction modulo four. The execution reports `ALTERNATING_WEDGE_WALK_SPECTRAL_CHI2_CHECKS_PASS`. The infinite-dimensional cutoff, dominated convergence, and uniform radical estimate are established by proof, not by finite enumeration.

## Relationship to prior work
Delsarte and Goethals developed the rank-based association scheme of alternating bilinear forms, which underlies the harmonic decomposition; an explicit association-scheme eigenmatrix can provide the finite-dimensional spectral inputs, so those inputs are not claimed to be new by themselves. Fulman and Goldstein analyzed rank distributions of random *uniform* alternating matrices, rather than the time-indexed distribution of a sum of independent wedges. Schmidt developed association-scheme methods for symmetric bilinear forms. He proved cutoff for a transvection-generated walk on the **space of nondegenerate symplectic forms**, not for this additive walk on **all alternating matrices**. The specific cutoff at half-dimension, both exact limiting chi-square profiles, and the full bridge from wedge increments to total variation are not implied directly by the inspected statements. The full Delsarte–Goethals article was not available for comparison; this is a historical-priority risk, and no unconditional novelty claim is made.

## Limitations
This theorem uses independent uniform vector *pairs*, not uniform nonzero rank-two increments (which would rescale eigenvalues). It gives no fixed-offset total-variation limiting curve, no simultaneous \(q,n\) limit, and no assertion of a strongest possible separation constant. The exact Fourier and chi-square expressions follow from standard harmonic inputs, and a historical association-scheme argument might subsume portions of the statement. Independent audit has not been performed.

## References
1. P. Delsarte and J.-M. Goethals, *Alternating bilinear forms over GF(q)*, Journal of Combinatorial Theory, Series A 19 (1975), 26–50; DOI: 10.1016/0097-3165(75)90090-4.
2. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504 (original submission 2012-11-02), Annals of Probability 43 (2015), 1274–1314.
3. K.-U. Schmidt, *Symmetric bilinear forms over finite fields with applications to coding theory*, arXiv:1410.7184 (2014).
4. J. He, *Random walk on the symplectic forms over a finite field*, arXiv:1910.10823 (2019), Algebraic Combinatorics 3 (2020), 1165–1181.
