# A Robin spectral crossover for polynomial Gram matrices in de Branges–Rovnyak spaces

## Finding
For \(0<c\le1\), let \(b_c(z)=c(1+z)/2\), and let \(G_n(c)=(\langle z^j,z^k\rangle_{\mathcal H(b_c)})_{0\le j,k\le n}\) be the monomial Gram matrix of the de Branges–Rovnyak space with kernel \((1-b_c(z)\overline{b_c(w)})/(1-z\bar w)\). Put
\[
q=q(c)=\frac{1-\sqrt{1-c^2}}{1+\sqrt{1-c^2}}\in(0,1],
\qquad \Delta_n(c)=\frac{\lambda_{\max}(G_n(c))}{\lambda_{\min}(G_n(c))}.
\]
Every entry and determinant are explicit:
\[
\boxed{G_n(c)_{jk}=\frac{1+q}{1-q}\left(q^{|j-k|}-q^{j+k+1}\right),\qquad \det G_n(c)=(1+q)^{2n+1}.}
\]
The displayed entry formula is interpreted continuously at \(q=1\), where it is \(2+4\min(j,k)\).

The smallest eigenvalue tends to \(1\) **uniformly** in \(0<c\le1\) as \(n\to\infty\). More precisely, for \(n\ge3\),
\[
1\le \lambda_{\min}(G_n(c))\le \left(1-\frac1{2(n-1)}\right)^{-1}.
\]
For any sequence \(c_n\in(0,1]\), set \(q_n=q(c_n)\). There is a sharp three-regime description of the upper Gram spectrum.

* **Finite crossover.** If \(n(1-q_n)\to\tau\in[0,\infty)\), then for every fixed positive integer \(j\),
\[
\boxed{\frac{\lambda_j^{\downarrow}(G_n(c_n))}{n^2}\longrightarrow
\frac4{\tau^2+\omega_j(\tau)^2},}
\]
where \(\lambda_j^{\downarrow}\) is the \(j\)-th largest eigenvalue and \(\omega_j(\tau)\) is the unique root of \(\omega\cos\omega+\tau\sin\omega=0\) in \(((j-\tfrac12)\pi,j\pi)\) when \(\tau>0\), and \(\omega_j(0)=(j-\tfrac12)\pi\). In particular,
\[
\boxed{\frac{\Delta_n(c_n)}{n^2}\to \frac4{\tau^2+\omega_1(\tau)^2}.}
\]
At the boundary symbol \(c_n=1\), this gives the exact leading conditioning constant \(\Delta_n(1)\sim16n^2/\pi^2\).

* **Separated regime.** If \(n(1-q_n)\to\infty\), then
\[
\boxed{\lambda_{\max}(G_n(c_n))\sim\Delta_n(c_n)\sim
\left(\frac{1+q_n}{1-q_n}\right)^2=\frac1{1-c_n^2}.}
\]
This includes every fixed \(0<c<1\). These statements quantify the sharp scale \(1-c_n^2\asymp n^{-2}\) at which the bounded finite-section Gram norm changes to quadratic growth.

## Assumptions and scope
The Hilbert norm is the canonical range norm of \(\mathcal H(b)\), not an arbitrarily equivalent local-Dirichlet norm. The monomial cutoff is \(\{1,z,\ldots,z^n\}\); matrices have size \(n+1\). Eigenvalues are positive and ordered decreasingly. The transition holds for arbitrary real sequences \(c_n\in(0,1]\), including the endpoint \(c_n=1\). The parameter \(\tau\) is measured using \(n(1-q_n)\), not \(n(1-c_n)\). Equivalently, \(1-q_n\sim2\sqrt{1-c_n^2}\) in the critical regime.

## Proof
**Pythagorean factor and Gram identity.** Let \(\delta=\sqrt{1-c^2}\). The outer Pythagorean mate of \(b_c\) is \(a_c(z)=(1+\delta)(1-qz)/2\), where \(q=(1-\delta)/(1+\delta)\). Indeed on the circle \(|a_c|^2+|b_c|^2=1\); \(a_c(0)>0\) and its single zero lies outside the open disk (on the boundary if \(c=1\)). Thus
\[
\phi_c=b_c/a_c=\sqrt q\frac{1+z}{1-qz},\quad
\phi_{c,0}=\sqrt q,\quad \phi_{c,k}=\sqrt q(1+q)q^{k-1}\ (k\ge1).
\]
The standard non-extreme de Branges–Rovnyak norm identity is \(\|f\|_{\mathcal H(b)}^2=\|f\|_{H^2}^2+\|T_{\overline\phi}f\|_{H^2}^2\) on polynomials. Inserting the coefficients into \(\langle z^j,z^k\rangle=\mathbf1_{j=k}+\sum_{s=0}^{\min(j,k)}\overline{\phi_s}\phi_{|j-k|+s}\) gives, by a finite geometric sum, the boxed formula for \(q<1\), and its \(q=1\) limit \(2+4\min(j,k)\).

**Exact factorization.** For \(n\ge1\), let \(D_{n,q}\) be the lower bidiagonal matrix with main diagonal \(1\) and first subdiagonal \(-q\). The Gram entries imply
\[
D_{n,q}G_nD_{n,q}^{*}=\operatorname{diag}(1+q,(1+q)^2,\ldots,(1+q)^2).
\]
This gives the determinant and shows that \(G_n^{-1}\), after multiplication by \((1+q)^2\), is tridiagonal with first diagonal entry \(1+q+q^2\), interior diagonal entries \(1+q^2\), last entry \(1\), and off-diagonals \(-q\). For \(n\ge3\), the alternating vector supported in coordinates \(1,\ldots,n-1\), with endpoint coordinates zero, has inverse-Gram Rayleigh quotient at least \(1-1/[2(n-1)]\). Meanwhile the norm identity gives \(G_n\ge I\). Hence the uniform bound on \(\lambda_{\min}\).

**Finite crossover.** For \(n(1-q_n)\to\tau<\infty\) and \(u=j/n,v=k/n\), the geometric-sum representation
\[
G_n(j,k)=(1+q_n)q_n^{|j-k|}\sum_{s=0}^{2\min(j,k)}q_n^s
\]
shows uniformly in all indices that \(G_n(j,k)/n\to \mathcal K_\tau(u,v)\), where
\[
\mathcal K_\tau(u,v)=\begin{cases}
\dfrac2\tau(e^{-\tau|u-v|}-e^{-\tau(u+v)}),&\tau>0,\\
4\min(u,v),&\tau=0.
\end{cases}
\]
Uniform convergence of the embedded step kernels on \([0,1]^2\) implies operator-norm convergence of the corresponding finite-rank integral operators. Using \(n+1\) equal cells, their nonzero eigenvalues are those of \(G_n/[n(n+1)]\), which have the same fixed-index limit as \(G_n/n^2\). Thus every fixed ordered eigenvalue converges. The kernel \(\mathcal K_\tau\) is four times the Green kernel of \(-d^2/du^2+\tau^2\), with \(h(0)=0\) and \(h'(1)+\tau h(1)=0\); at \(\tau=0\), the second condition is \(h'(1)=0\). A positive eigenfunction solves \(h(u)=\sin(\omega u)\), and the boundary condition gives \(\omega\cos\omega+\tau\sin\omega=0\). Sturm–Liouville theory yields the listed simple eigenvalues \(4/(\tau^2+\omega_j^2)\).

**Separated regime.** For \(0<q<1\), the norm identity gives \(G_n\le (1+\|\phi_c\|_\infty^2)I\). Since \(\|\phi_c\|_\infty=2\sqrt q/(1-q)\), this upper bound equals \(((1+q)/(1-q))^2\). For the matching lower bound, use the vector constant on the last \(\lfloor n/2\rfloor\) coordinates and zero elsewhere. Its Rayleigh quotient for the Toeplitz term of the exact formula has relative defect \(O([n(1-q)]^{-1})\); the reflected term \(q^{j+k+1}\) contributes a relative \(o(1)\) uniformly when \(n(1-q)\to\infty\). Thus the upper bound is asymptotically attained. Combine with the uniform smallest-eigenvalue limit to obtain the condition-number asymptotic.

## Verification
The accompanying standalone `CHECK.py` checks the exact Gram identity independently against the Toeplitz coefficient sum, the factorization, determinant, inverse, positivity, and numerical finite-crossover and separated-regime behavior at multiple parameters and dimensions. It is a finite consistency test, not a proof of any infinite assertion; the proof above supplies the required infinite-dimensional argument.

## Relationship to prior work
Dellepiane and Seco (arXiv:2603.03093, first posted March 3, 2026) provide the non-extreme monomial norm identity, and orthogonal polynomial bases for symbols including \((1+z)/2\). Those identities are expressly acknowledged as the starting point, not claimed as new. The present quantitative finding is the **full finite-section spectrum at the joint boundary/degree scale**, including the Robin crossover, an exact determinant and matching separated-regime conditioning. The nearest classic matrix analogue is the Kac–Murdock–Szegő / AR(1) covariance matrix. Unlike the stationary Toeplitz covariance, this Gram matrix has a reflected term encoding the hard boundary at index zero, and consequently has a Dirichlet–Robin spectral law. Standard stationary KMS formulas do not directly give this boundary law. The classical Green-kernel and Jacobi-matrix techniques are likewise not claimed as new.

## Limitations
The exact family is \(b_c(z)=c(1+z)/2\), with real \(0<c\le1\); it is not a theorem for arbitrary Schur symbols or other polynomial bases. The finite-crossover conclusions concern each fixed-index eigenvalue, not a uniform asymptotic for all indices. The new application is a statement about canonical monomial Gram matrices; the underlying AR(1) covariance and Sturm–Liouville calculations are classical. Priority outside the inspected literature is not independently established.

## References
1. E. Dellepiane and D. Seco, *Orthogonal polynomials in de Branges–Rovnyak spaces*, arXiv:2603.03093 (2026), Sections 2–4, https://arxiv.org/html/2603.03093v1.
2. B. Łanucha and M. T. Nowak, *Examples of de Branges-Rovnyak spaces generated by nonextreme functions*, arXiv:1807.04347 (2018), https://arxiv.org/abs/1807.04347.
3. A. Bourget, A. Alvarez Loya and T. McMillen, *Spectral asymptotics for Kac–Murdock–Szegő matrices*, arXiv:1610.00084 (2016), https://arxiv.org/html/1610.00084v1.
4. N. J. Higham, *What Is the Kac–Murdock–Szegő Matrix?* (2021), https://nhigham.com/2021/07/06/what-is-the-kac-murdock-szego-matrix/.
