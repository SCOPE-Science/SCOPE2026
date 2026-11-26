# A sharp singular-value Weyl law for the geometrically weighted Cesàro operator

## Finding

For every real \(0<r<1\), equip complex sequences \(x=(x_n)_{n\ge1}\) with the Hilbert norm
\[
\|x\|_{r}^{2}=\sum_{n=1}^{\infty}r^{n-1}|x_n|^2.
\]
Let \(C_r\) denote the bounded extension of the Cesàro averaging rule \((C_rx)_n=n^{-1}\sum_{k=1}^n x_k\) to this Hilbert space. If \(s_n(C_r)\) are its singular values in decreasing order with multiplicities, then
\[
\boxed{\lim_{n\to\infty}n s_n(C_r)
=\mathfrak c(r):=\frac{1}{2\pi}\int_0^{2\pi}
\frac{d\theta}{\sqrt{1+r-2\sqrt r\cos\theta}}.}
\]
In particular, \(C_r\) belongs to the Schatten class \(\mathcal S_p\) exactly for \(p>1\), among real \(p>0\), and is measurable in weak trace class in the sense that
\[
\lim_{N\to\infty}\frac{1}{\log N}\sum_{n=1}^{N}s_n(C_r)=\mathfrak c(r).
\]
Consequently every ordinary Dixmier trace of \(|C_r|\) equals \(\mathfrak c(r)\). For every \(0<r<1\), \(\mathfrak c(r)>1\), although the nonzero eigenvalues of the same operator are \(1,1/2,1/3,\ldots\), each simple, as already known for the generalized Cesàro matrices.

## Assumptions and scope

The Hilbert space is complex, the weight is exactly \(w_n=r^{n-1}\), and the Cesàro average has the conventional normalization \(1/n\). All limits are taken with the weight parameter \(r\) fixed strictly between zero and one. The positive numbers \(s_n\) are singular values, not eigenvalue moduli. The asserted weak-trace-class measurability follows from convergence of the ordinary logarithmic mean; it does not assert that \(C_r\) itself is a positive operator.

## Proof

**1. Unitary representation.** Define \(U:\ell^2(r^{n-1})\to\ell^2\) by \((Ux)_n=r^{(n-1)/2}x_n\). Put \(t=\sqrt r\), \(D=\operatorname{diag}(1,1/2,1/3,\ldots)\), and let \(S\) be the unilateral forward shift \((Sx)_1=0\), \((Sx)_n=x_{n-1}\) for \(n\ge2\). Directly from the matrix entries,
\[
UC_rU^{-1}=A_t=D(I-tS)^{-1}.
\]
The inverse is the norm-convergent Neumann series \(T_t=\sum_{k\ge0}t^kS^k\). Hence \(A_t\) is compact, and the singular values of \(A_t\) and \(C_r\) coincide.

**2. The finite-band counting lemma.** Let \(P(z)=\sum_{j=0}^{B}a_jz^j\) be any complex polynomial. For the compact operator \(A_P=DP(S)\), set \(N_P(\lambda)=\#\{n:s_n(A_P)>\lambda\}\). We establish
\[
\lim_{\lambda\downarrow0}\lambda N_P(\lambda)
=\frac{1}{2\pi}\int_0^{2\pi}|P(e^{i\theta})|\,d\theta.\tag{1}
\]
The identically zero polynomial gives the trivial case. For nonzero \(P\), write \(m_P(u)=(2\pi)^{-1}|\{\theta:|P(e^{i\theta})|>u\}|\); the layer-cake identity gives \(\int_0^\infty m_P(u)\,du=(2\pi)^{-1}\int|P|\).

Here are details of the counting limit. Fix cutoffs \(0<\delta<M\), a geometric mesh ratio \(1+\eta>1\), and \(\lambda>0\). Discard output coordinates \(n\le\delta/\lambda\), a perturbation of rank at most \(\lfloor\delta/\lambda\rfloor\). The operator supported on output coordinates \(n>M/\lambda\) has norm at most \(\lambda\|P(S)\|/M\). Partition the intervening coordinates into finitely many consecutive blocks \(I_j\), with endpoints approximately \(u_j/\lambda\) and \(u_{j+1}/\lambda\), where \(u_{j+1}=(1+\eta)u_j\) except possibly at the final endpoint. Since \(P(S)\) has bandwidth \(B\), suppressing matrix entries connecting distinct blocks has rank at most \(B\) times the number of block boundaries, independent of \(\lambda\).

On a block with endpoint indices \(a_j\le n\le b_j\), the singular values of \(D_{I_j}P(S)_{I_j}\) lie, index by index, between \(b_j^{-1}\) and \(a_j^{-1}\) times those of \(P(S)_{I_j}\). The latter finite Toeplitz matrix differs by rank at most \(B\) from the corresponding circulant. That circulant has singular values \(|P(e^{2\pi ik/|I_j|})|\), so its empirical singular-value distribution converges to the distribution of \(|P(e^{i\theta})|\) as \(|I_j|\to\infty\). Thus, at continuity points of \(m_P\),
\[
|I_j|\,m_P(\lambda b_j)+o(|I_j|)
\ \le\ N(\lambda;D_{I_j}P(S)_{I_j})\ \le\
|I_j|\,m_P(\lambda a_j)+o(|I_j|).
\]
The bounds remain sufficient at any isolated exceptional levels by one-sided approximation. Multiplying by \(\lambda\), summing the finitely many blocks, and then shrinking \(\eta\) gives the integral of \(m_P\) over \([\delta,M]\) by upper and lower Darboux sums. Finite-rank changes in the block comparisons disappear after multiplication by \(\lambda\). The discarded head contributes at most \(\delta\) to the normalized count. The discarded tail, with norm \(\le\lambda\|P(S)\|/M\), changes the counting threshold from \(\lambda\) to \((1\pm\|P(S)\|/M)\lambda\) by the singular-number perturbation inequality. Finally send \(\delta\downarrow0\), \(M\uparrow\infty\), and \(\eta\downarrow0\). The layer-cake identity proves (1).

**3. Passage to the analytic symbol.** For each integer \(B\ge0\), let \(P_B(z)=\sum_{k=0}^{B}t^kz^k\). Then \(A_t=A_{P_B}+E_B\), where
\[
\|T_t-P_B(S)\|\le\epsilon_B:=\frac{t^{B+1}}{1-t},
\qquad s_n(E_B)\le\frac{\epsilon_B}{n}.
\]
The singular-number counting inequality for sums therefore gives, for \(0<\gamma<1\),
\[
N_{P_B}((1+\gamma)\lambda)-\frac{\epsilon_B}{\gamma\lambda}
\le N(\lambda;A_t)
\le N_{P_B}((1-\gamma)\lambda)+\frac{\epsilon_B}{\gamma\lambda}.
\]
By (1), after taking \(\lambda\downarrow0\), the normalized upper and lower counts lie within \(\epsilon_B/\gamma\) of \(c_B/(1\mp\gamma)\), where \(c_B=(2\pi)^{-1}\int|P_B(e^{i\theta})|d\theta\). Since \(\epsilon_B\to0\), choose \(\gamma=\sqrt{\epsilon_B}\) for sufficiently large \(B\), and let \(B\to\infty\). Uniform convergence \(P_B(e^{i\theta})\to(1-te^{i\theta})^{-1}\) yields
\[
\lim_{\lambda\downarrow0}\lambda N(\lambda;A_t)
=\frac{1}{2\pi}\int_0^{2\pi}\frac{d\theta}{|1-te^{i\theta}|}
=\mathfrak c(r).\tag{2}
\]
For decreasing positive singular values, (2) is equivalent to \(n s_n(A_t)\to\mathfrak c(r)\). The Schatten and logarithmic assertions follow by comparison with the harmonic sequence and the ordinary Cesàro summation of \(s_n=\mathfrak c(r)/n+o(1/n)\). Lastly \((2\pi)^{-1}\int(1-te^{i\theta})^{-1}\,d\theta=1\), while the integrand has nonconstant phase for \(t>0\). The strict triangle inequality for integrals therefore gives \(\mathfrak c(r)>1\).

## Verification

The included `verify.py` constructs finite sections \(A_t^{(N)}\) with entries \(t^{i-j}/(i+1)\) for \(i\ge j\), computes their singular values, and compares selected interior indices with numerical quadrature of the asserted constant. For \(t=0.4\), quadrature gives approximately \(1.04405634128953\); for \(t=0.7\), it gives approximately \(1.17500529310553\). At section dimension \(N=320\), the values of \(100s_{100}\) are approximately \(1.04405517839\) and \(1.17499977622\), respectively. Finite-section evidence corroborates but does not replace the counting argument above.

Run `python verify.py` with Python 3 and NumPy installed. No unpublished input, network access, or additional file is needed.

## Relationship to prior work

Rhaly introduced and studied the same generalized Cesàro matrices in 1982, establishing compactness and the point spectrum \(\{1/n:n\ge1\}\) for a nonzero geometric parameter, and in 1984 established a Hilbert–Schmidt norm formula. Albanese, Bonet, and Ricker studied compactness and spectra of ordinary Cesàro averaging in weighted \(\ell_p\) spaces; their 2015 paper includes geometric weights as an example. These results provide the operator and qualitative compactness, but the inspected statements do not determine the sharp asymptotic of **singular values** or its logarithmic trace coefficient. The classical Toeplitz singular-value-distribution theorem (for finite Toeplitz sections) underlies the elementary finite-band counting lemma, but a finite Toeplitz distribution alone does not supply the infinite compact diagonal-times-Toeplitz counting limit. General pseudodifferential Weyl laws may furnish alternative derivations; see limitations.

## Limitations

The asymptotic is for fixed \(0<r<1\), not uniform as \(r\uparrow1\), and does not give exact finite-index singular values or a second-order remainder. The 2015 weighted-space article could be inspected in substantial author-provided extracted text, but full mathematical formatting was imperfect; a completely legible archival version could not be secured through the available authorized routes. Bibliographic equivalence to a general singular-value Weyl theorem for one-sided discrete pseudodifferential operators remains a specific originality risk. The result has not undergone independent mathematical audit.

## References

1. H. C. Rhaly Jr., *Discrete generalized Cesàro operators*, Proceedings of the American Mathematical Society 86 (1982), 405–409, DOI: 10.1090/S0002-9939-1982-0671204-7; publicly readable archival PDF: https://scispace.com/pdf/discrete-generalized-cesaro-operators-96dbouzxs4.pdf.
2. H. C. Rhaly Jr., *Generalized Cesàro Matrices*, Canadian Mathematical Bulletin 27 (1984), 417–422, DOI: 10.4153/CMB-1984-064-5; archival PDF: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/967DB4D41F4A7EB149E5E3CBFC548BDE/S0008439500068879a.pdf/div-class-title-generalized-cesaro-matrices-div.pdf.
3. A. A. Albanese, J. Bonet, and W. J. Ricker, *Spectrum and compactness of the Cesàro operator on weighted \(\ell_p\) spaces*, Journal of the Australian Mathematical Society 99 (2015), 287–314, DOI: 10.1017/S1446788715000221, online 19 August 2015.
4. H. Widom, *On the singular values of Toeplitz matrices*, Zeitschrift für Analysis und ihre Anwendungen 8 (1989), 221–229, DOI: 10.4171/ZAA/350.
