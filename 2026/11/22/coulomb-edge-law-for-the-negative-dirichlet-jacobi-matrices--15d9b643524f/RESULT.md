# Coulomb edge law for the negative Dirichlet Jacobi matrices

## Finding
For each fixed real \(s>0\), let \(J_s\) be the bounded self-adjoint operator on \(\ell^2(\mathbb N_0)\) with diagonal entries zero and consecutive off-diagonal entries
\[
a_n=\left(\frac{n+2}{n+1}\right)^{s/2},\qquad n=0,1,2,\ldots.
\]
For \(\varepsilon>0\), let \(N_s(\varepsilon)\) count, with multiplicity, the eigenvalues of \(J_s\) in \((2+\varepsilon,\infty)\). Then
\[
\boxed{\lim_{\varepsilon\downarrow0}\sqrt\varepsilon\,N_s(\varepsilon)=\frac{s}{2}.}
\]
Consequently there are infinitely many simple eigenvalues \(\lambda_1(s)>\lambda_2(s)>\cdots>2\), and
\[
\boxed{\lambda_j(s)=2+\frac{s^2}{4j^2}(1+o(1))\qquad(j\to\infty).}
\]
The eigenvalues below \(-2\) are exactly the negatives of these, with the same asymptotic distances from \(-2\).

These are the Jacobi matrices associated with the negative Dirichlet-type coefficient weights \(\omega_n=(n+1)^{-s}\). The eigenvalue distribution supplies a quantitative spectral edge law for the family whose *largest* eigenvalue controls the extremal zero-modulus problem for optimal polynomial approximants. It does not evaluate that largest eigenvalue.

## Assumptions and scope
Here \(s\) is fixed and strictly positive; the limits are in the spectral threshold \(\varepsilon\downarrow0\) and eigenvalue index \(j\to\infty\), respectively, with no simultaneous parameter-uniform assertion. The operator acts on the half-line, not the full integer lattice. The strict spectral threshold excludes an eigenvalue exactly at \(2+\varepsilon\). All statements concern exact infinite-dimensional spectra. Finite-dimensional numerical calculations are illustrative and are not used to infer infinitude.

## Proof
**1. Spectral preliminaries.** Since \(a_n\to1\), the difference between \(J_s\) and the free half-line Jacobi matrix \(J_0\) (unit consecutive hoppings) is compact: truncating the off-diagonal differences beyond index \(M\) leaves operator-norm error at most \(2\sup_{n\ge M}|a_n-1|\). The free essential spectrum is \([-2,2]\), so this is also the essential spectrum of \(J_s\). Each exterior eigenvalue is simple, because the recurrence \(a_{n-1}u_{n-1}+a_nu_{n+1}=\lambda u_n\), with \(u_{-1}=0\), is determined by \(u_0\). The unitary \((Uu)_n=(-1)^nu_n\) satisfies \(UJ_sU^{-1}=-J_s\), giving spectral symmetry.

**2. A constant-hopping block.** Let \(B_{L,b}\) be the \(L\)-by-\(L\) tridiagonal matrix with zero diagonal and constant positive hopping \(b\). Its eigenvalues are exactly \(2b\cos(\pi k/(L+1))\) for \(k=1,\ldots,L\). If \(2b>2+\varepsilon\), its number of eigenvalues strictly above \(2+\varepsilon\) differs by at most one from
\[
\frac{L+1}{\pi}\arccos\!\left(\frac{2+\varepsilon}{2b}\right).
\]
Otherwise that number is zero. If all hoppings of a finite block differ from \(b\) by at most \(\Delta\), its operator norm difference from \(B_{L,b}\) is at most \(2\Delta\), and Weyl's variational inequalities sandwich its threshold count between those of \(B_{L,b}\) at thresholds \(2+\varepsilon\pm2\Delta\).

**3. Finite-rank bracketing.** Cut the half-line into successive blocks by setting selected interblock hoppings to zero. Each cut is an operator of rank at most two, so the original count above any fixed threshold and the sum of counts for the resulting blocks differ by no more than twice the number of cuts (min-max interlacing). This remains valid when one last block is an infinite tail, because the threshold lies strictly above essential spectrum.

**4. Negligible initial and terminal portions.** Put \(m_\varepsilon=\lceil\varepsilon^{-1/3}\rceil\). The first \(m_\varepsilon\) coordinates contribute at most \(m_\varepsilon=o(\varepsilon^{-1/2})\) eigenvalues. Fix \(\eta>0\) and decompose indices from \(m_\varepsilon\) up to about \(\eta/\varepsilon\) into dyadic blocks with left endpoints \(m\), lengths at most \(m\). On each block \(\|J_s-J_0\|\le C_s/m\), so the constant-hopping formula bounds the count above \(2+\varepsilon\) by \(C_s\sqrt m+1\). Geometric summation and the rank costs from \(O(\log(1/\varepsilon))\) cuts yield a total at most
\[
C_s\sqrt{\eta/\varepsilon}+O_s(\log(1/\varepsilon)+\varepsilon^{-1/3}).
\]
In particular, its rescaled contribution has upper limit at most \(C_s\sqrt\eta\), which vanishes as \(\eta\downarrow0\).

For indices \(n\ge(s+\eta)/\varepsilon\), Taylor expansion gives \(2a_n=2+s/(n+1)+O_s((n+1)^{-2})<2+\varepsilon\), uniformly for sufficiently small \(\varepsilon\). The operator norm of the corresponding half-line tail is at most twice its largest hopping, hence the tail has no eigenvalue above the threshold. The single edge cut adds only a bounded rank cost.

**5. Interior Riemann sum.** Fix \(0<\eta<s\), and partition the scaled interval \([\eta,s+\eta]\) into finitely many subintervals of mesh at most \(\delta>0\). A subinterval with left endpoint \(x>0\) corresponds to a Jacobi block of length \(L=(\delta_x+o(1))/\varepsilon\), where \(\delta_x\) is its actual scaled width. Uniformly within it,
\[
a_n=1+\frac{s\varepsilon}{2x}+O_{s,\eta}(\varepsilon\delta+\varepsilon^2).
\]
The constant-hopping formula and the elementary expansion \(\arccos(1-u)=\sqrt{2u}+O(u^{3/2})\) show that, after multiplying counts by \(\sqrt\varepsilon\), the block contributes the Riemann-sum term
\[
\frac{\delta_x}{\pi}\sqrt{(s/x-1)_+},
\]
up to a discrepancy tending to zero when first \(\varepsilon\downarrow0\) and then \(\delta\downarrow0\). For rigor at the turning point, use the norm-error bracketing in Step 2, with the relative threshold variation \(O_{s,\eta}(\delta)\), before letting \(\delta\) tend to zero. There are only finitely many interior cuts for each fixed \(\eta,\delta\), and their contributions vanish after multiplication by \(\sqrt\varepsilon\).

Combining the three regions gives, with upper/lower errors tending to zero as \(\eta\downarrow0\),
\[
\lim_{\varepsilon\downarrow0}\sqrt\varepsilon\,N_s(\varepsilon)
=\frac1\pi\int_0^s\sqrt{\frac{s}{x}-1}\,dx
=\frac{s}{2},
\]
where the last equality follows from \(x=s\sin^2u\). The integral's singularity at zero is integrable, justifying removal of the initial cutoff.

**6. Eigenvalue inversion.** The count diverges as \(\varepsilon\downarrow0\), proving infinitely many simple exterior eigenvalues. For any \(\gamma>0\), the asymptotic count eventually lies between \((s/2-\gamma)\varepsilon^{-1/2}\) and \((s/2+\gamma)\varepsilon^{-1/2}\). Monotonic inversion gives \(j\sqrt{\lambda_j(s)-2}\to s/2\), hence the asserted \(j^{-2}\) law. The unitary symmetry from Step 1 treats the negative side.

## Verification
The accompanying `check.py` constructs finite Jacobi truncations, computes selected positive exterior eigenvalues, checks the exact constant-hopping spectrum against direct diagonalization, checks the scaled count at four small thresholds for three distinct exponents, and evaluates the limiting phase integral independently. It reports observed finite-size discrepancies and checks that the counts approach the predicted coefficient. These experiments do not certify the limit: the proof is the finite-rank bracketing argument above. No numerical root is used in the theorem.

## Relationship to prior work
Bénéteau, Khavinson, Liaw, Seco and Simanek (2016) identify these Jacobi operators in the optimal-polynomial-approximant extremal problem and relate the top eigenvalue to minimum zero modulus. The 2021 survey by Bénéteau and Centner explicitly highlights the unresolved norm for negative Dirichlet exponents other than the Bergman case, which motivates a study of the same spectral family. The present result describes the entire accumulation *tail*, not the largest eigenvalue, and does not claim to resolve that norm question. Zlatoš (2002) studies Szegő conditions for Coulomb-perturbed Jacobi matrices; those conditions and associated eigenvalue comparisons do not provide the displayed coefficient \(s/2\) for this sequence in the inspected text. Webb and Olver (2021) establish computational spectral tools for compact perturbations; their statements do not specify this edge-count limit. The special-function Jacobi families treated by Štampach and Šťovíček (2013) have a different discrete-spectrum setting. These implication comparisons are best-knowledge and do not establish historical uniqueness.

## Limitations
The new statement is about the high-index tail for fixed \(s>0\), not the exact finite eigenvalues, a second-order correction, or the spectral norm. It does not claim an all-parameter-uniform rate. General semiclassical methods may subsume this particular counting law; no exhaustive historical priority claim is made. The proof is analytic, while the included finite-dimensional tests are auxiliary. An independent mathematical audit has not been carried out.

## References
- C. Bénéteau and R. Centner, *A survey of optimal polynomial approximants, applications to digital filter design, and related open problems*, arXiv:2102.01725v1, first public 2021-02-02, https://arxiv.org/abs/2102.01725.
- C. Bénéteau, D. Khavinson, C. Liaw, D. Seco, and B. Simanek, *Zeros of optimal polynomial approximants: Jacobi matrices and Jentzsch-type theorems*, arXiv:1606.08615v1, 2016-06-28, https://arxiv.org/abs/1606.08615.
- A. Zlatoš, *The Szegő condition for Coulomb Jacobi matrices*, public manuscript dated 2002-07-24, https://mathweb.ucsd.edu/~zlatos/Papers/szego.pdf.
- M. Webb and S. Olver, *Spectra of Jacobi operators via connection coefficient matrices*, Communications in Mathematical Physics (2021), https://doi.org/10.1007/s00220-021-03939-w.
- F. Štampach and P. Šťovíček, *Special functions and spectrum of Jacobi matrices*, arXiv:1301.2125v1, 2013-01-10, https://arxiv.org/abs/1301.2125.
