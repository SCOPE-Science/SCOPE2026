# Cubic singular-value Weyl law for cross-parameter generalized Cesàro commutators

## Finding
For real parameters \(0\le s,t<1\), define the generalized Cesàro operators on complex \(\ell^2(\mathbb N_0)\) by
\[
(C_t x)_n=\frac1{n+1}\sum_{j=0}^n t^{n-j}x_j.
\]
Set \(K_{t,s}=C_tC_s-C_sC_t\). They commute if and only if \(t=s\). For \(t\ne s\), the compact operator \(K_{t,s}\) is injective, quasinilpotent, and trace class, with \(\operatorname{Tr}K_{t,s}=0\). Its nonincreasing singular values, indexed from one, satisfy the **exact** Weyl law
\[
\boxed{\lim_{n\to\infty}n^3s_n(K_{t,s})=|t-s|J(t,s)^3,}\qquad
J(t,s)=\frac1{2\pi}\int_0^{2\pi}
\big[(1-2t\cos\theta+t^2)(1-2s\cos\theta+s^2)\big]^{-1/3}\,d\theta.
\]
In particular \(K_{t,s}\in\mathcal S_p\) exactly for \(p>1/3\), for all real \(p>0\); at the endpoint it lies in weak \(\mathcal S_{1/3}\) but not strong \(\mathcal S_{1/3}\). The positive operator \(|K_{t,s}|^{1/3}\) has the ordinary logarithmic singular-trace limit
\[
\boxed{\lim_{N\to\infty}\frac1{\log N}\sum_{n=1}^{N}s_n(|K_{t,s}|^{1/3})=|t-s|^{1/3}J(t,s).}
\]
For the natural diagonal endpoint \(t=0\), the integral reduces to \(J(0,s)={}_2F_1(1/3,1/3;1;s^2)\). The exponential off-diagonal localization makes the cross-parameter commutator three orders compact, despite each separate \(C_t\) having singular values of order \(n^{-1}\).

## Assumptions and scope
Work on the complex Hilbert space \(\ell^2(\mathbb N_0)\), with \(Se_k=e_{k+1}\) and \(Be_k=(k+1)^{-1}e_k\). Parameters \(s,t\) are fixed within \([0,1)\); no uniform assertion as either parameter approaches \(1\) is made. Singular values are numbered \(s_1\ge s_2\ge\cdots\), with multiplicity. For real \(p>0\), \(\mathcal S_p\) denotes the compact operators whose singular values have summable \(p\)-th powers, and the weak endpoint means \(\sup_{n\ge1}n^3s_n(K_{t,s})<\infty\). For \(t=s\), the zero commutator is excluded from the positive-coefficient Weyl and nonmembership assertions.

## Proof
### 1. Exact resolvent-commutator factorization
Put \(A_t=(I-tS)^{-1}=\sum_{j\ge0}t^jS^j\); each is bounded and boundedly invertible because \(0\le t<1\). The definition gives \(C_t=BA_t\). The resolvent commutator identity gives
\[
[A_t,B]=t A_t(SB-BS)A_t.
\]
Using the commutativity of \(A_t,A_s\), and the scalar resolvent identity \(tA_t-sA_s=(t-s)A_tA_s\), obtains the exact operator identity
\[
\boxed{K_{t,s}=(t-s)B R(SB-BS)R,\quad R=A_tA_s.}\tag{1}
\]
Here \(Q=SB-BS\) is the injective weighted shift
\[
Qe_k=\frac1{(k+1)(k+2)}e_{k+1}.
\]
The diagonal and each resolvent \(R\) are injective. Hence \(K_{t,s}\) is injective if \(t\ne s\). Formula (1) also gives the first subdiagonal
\[
(K_{t,s})_{k+1,k}=\frac{t-s}{(k+1)(k+2)^2}\ne0,
\]
and every entry on or above the diagonal vanishes. Thus \(C_t,C_s\) commute precisely at \(t=s\), and the nonzero commutator has infinite rank. Formula (1), with a compact factor \(B\), gives compactness. Each \(C_t=BA_t\) has singular values comparable to \(n^{-1}\), because \(A_t\) is boundedly invertible. Independently of the exact coefficient below, the factorization \(K_{t,s}=(t-s)(BRB^{-1})(BQ)R\) shows its singular values are comparable to \(n^{-3}\): the conjugate \(BRB^{-1}\) and its inverse are bounded, as their lower-triangular entries are finite or exponentially decaying shift sums multiplied by \((k+1)/(n+1)\le1\), and \(BQ\) is a weighted shift with weights \(1/[(k+1)(k+2)^2]\). A compact strictly lower-triangular operator has no nonzero eigenvalue: the eigen-equation can be read successively from coordinate zero. Therefore its spectrum is \(\{0\}\), proving quasinilpotence. It is trace class by step 4, and its trace is the sum of its vanishing diagonal entries.

### 2. Exact leading weighted-Toeplitz symbol and a strictly smaller remainder
Let \(r_h\) be the Taylor coefficients of \(R(z)=[(1-tz)(1-sz)]^{-1}\). For some \(\rho\in(\max\{s,t\},1)\) and a constant \(M\), \(|r_h|\le M\rho^h\). Equation (1) gives, for \(n>k\),
\[
(K_{t,s})_{n,k}=\frac{t-s}{n+1}
\sum_{j=k}^{n-1}\frac{r_{n-j-1}r_{j-k}}{(j+1)(j+2)}.
\tag{2}
\]
Define \(\phi(z)=zR(z)^2=z/[(1-tz)^2(1-sz)^2]\), with coefficients \(\phi_h\). Let \(D_3e_n=(n+1)^{-3}e_n\). The identity \(\phi_h=\sum_{j=k}^{n-1}r_{n-j-1}r_{j-k}\) for \(h=n-k\) shows from (2) that
\[
K_{t,s}=(t-s)D_3\phi(S)+E_{t,s}.
\tag{3}
\]
For completeness, the \((n,k)\)-entry of the remainder is exactly \((t-s)/(n+1)\) times the above convolution with the bracket
\[
\big[(j+1)^{-1}(j+2)^{-1}-(n+1)^{-2}\big].
\]
This bracket is at most \(C(n-j+1)(n+1)^{-3}\) in absolute value for \(j\ge n/2\). For \(j<n/2\), one has \(h=n-k\ge n/2\), and the geometric product bound \(|r_{n-j-1}r_{j-k}|\le M^2\rho^{h-1}\) absorbs all polynomial powers of \(n\). Summation gives a uniform estimate, for some fixed \(0<\rho_1<1\),
\[
|(E_{t,s})_{n,k}|\le C_{s,t}(n+1)^{-4}(1+n-k)^3\rho_1^{n-k}\quad(n>k).
\tag{4}
\]
All other entries vanish. Thus \(E_{t,s}=D_4F_{t,s}\), where \(D_4e_n=(n+1)^{-4}e_n\) and \(F_{t,s}\) is bounded by the row/column Schur test, because the convolution majorant in (4) is summable. The singular-value product inequality therefore gives
\[
s_n(E_{t,s})\le\|F_{t,s}\|s_n(D_4)=O_{s,t}(n^{-4}).
\tag{5}
\]

### 3. Weighted analytic Toeplitz counting lemma
We prove the needed general fact rather than assuming a spectral-asymptotic formula. If \(\gamma>0\) and \(\psi\) is analytic on a neighborhood of the closed unit disk, then
\[
N_{D_\gamma\psi(S)}(\lambda)
\sim\lambda^{-1/\gamma}\frac1{2\pi}
\int_0^{2\pi}|\psi(e^{i\theta})|^{1/\gamma}d\theta,
\qquad\lambda\downarrow0,
\tag{6}
\]
provided \(\psi\not\equiv0\). Here \(D_\gamma e_n=(n+1)^{-\gamma}e_n\) and \(N_T(\lambda)=\#\{j:s_j(T)>\lambda\}\). Equivalently,
\[
s_n(D_\gamma\psi(S))\sim
\left[\frac1{2\pi}\int_0^{2\pi}|\psi(e^{i\theta})|^{1/\gamma}d\theta\right]^\gamma n^{-\gamma}.
\tag{7}
\]
**Proof of (6).** First suppose \(\psi\) is a polynomial of degree \(d\). Write \(L=\lambda^{-1/\gamma}\). Rows below \(\delta L\) have rank at most \(\delta L+1\); rows beyond \(ML\) have norm at most \(\|\psi(S)\|M^{-\gamma}\lambda\). Fix \(0<\delta<M\), take \(M\) large, and partition the intermediate indices into consecutive blocks of length \(\lfloor L^{1/2}\rfloor\). Removing matrix entries crossing a block boundary changes the operator by rank at most \(d(ML/\lfloor L^{1/2}\rfloor+2)=o(L)\). On each block \((n+1)^{-\gamma}/\lambda\) differs uniformly by \(o(1)\) from the value at the block's rescaled coordinate \(x=n/L\). Finite Toeplitz sections of \(\psi(S)\) have asymptotic singular-value distribution given by \(|\psi(e^{i\theta})|\): for each fixed polynomial, the squared singular-value matrix differs from the corresponding finite Toeplitz section of \(|\psi|^2\) by rank at most \(2d\), and normalized traces of every fixed polynomial of these self-adjoint sections converge to the circle integral by expanding Fourier coefficients. Polynomial approximation of continuous test functions then yields the asserted distribution. Using singular-value counting inequalities at thresholds \((1\pm\eta)\lambda\), letting \(L\to\infty\) and then \(\eta\downarrow0\), the count per \(L\) tends to
\[
\int_\delta^M\frac1{2\pi}
\big|\{\theta:x^{-\gamma}|\psi(e^{i\theta})|>1\}\big|\,dx.
\]
Finally \(\delta\downarrow0\), \(M\to\infty\) gives the right side of (6), by Tonelli's theorem. For general \(\psi\) analytic beyond the circle, approximate it in the operator norm of \(\psi(S)\) by Taylor polynomials \(\psi_m(S)\). The residual obeys \(s_n(D_\gamma(\psi-\psi_m)(S))\le\|\psi-\psi_m\|_\infty s_n(D_\gamma)\), so its singular-value count above \(\eta\lambda\) is at most \(O((\|\psi-\psi_m\|_\infty/(\eta\lambda))^{1/\gamma})\). Apply the counting inequalities, first send \(\lambda\downarrow0\), then \(m\to\infty\), and finally \(\eta\downarrow0\). This proves (6), and monotone inversion proves (7). All discarded ranks and tails are controlled on the \(\lambda^{-1/\gamma}\) scale. \(\square\)

### 4. Exact coefficient, Schatten transition and logarithmic residue
Apply (7) at \(\gamma=3\) to \(\psi=\phi\). Since \(|\phi(e^{i\theta})|^{1/3}=[(1-2t\cos\theta+t^2)(1-2s\cos\theta+s^2)]^{-1/3}\), it gives
\[
s_n((t-s)D_3\phi(S))\sim |t-s|J(t,s)^3 n^{-3}.
\]
The error estimate (5) does not change this equivalent: choose \(k=\lfloor n^{9/10}\rfloor\) in the singular-value inequality \(s_{j+k-1}(A+B)\le s_j(A)+s_k(B)\), and use the reverse inequality with \(A=(A+B)-B\). Then \(s_k(E)=O(n^{-18/5})=o(n^{-3})\) while \(n-k\sim n\). This proves the displayed Weyl limit. The coefficient is strictly positive for distinct parameters. Hence \(\sum_ns_n(K)^p\) converges exactly if \(3p>1\), and the weak endpoint bound follows. Moreover \(s_n(|K|^{1/3})\sim |t-s|^{1/3}J(t,s)/n\); ordinary harmonic-sum comparison proves the logarithmic limit, without invoking any independent trace evaluation. At \(t=0\), expansion of \((1-se^{i\theta})^{-1/3}(1-se^{-i\theta})^{-1/3}\) and integration of the constant Fourier mode give
\(J(0,s)=\sum_{k\ge0}( (1/3)_k/k!)^2s^{2k}={}_2F_1(1/3,1/3;1;s^2)\).

## Verification
The included \(check.py\) verifies equation (1) on rational finite sections using only exact rational arithmetic, including the first subdiagonal identity and the commuting diagonal case. Supplementary finite singular-value computations at three parameter pairs compare the scaled singular values with the circle integral. These checks are finite diagnostics, **not** a proof of the infinite Weyl law; that law follows from the localization and perturbation arguments above. Reproduction: run \(\texttt{OPENBLAS_NUM_THREADS=1 python check.py}\) from the extracted package directory (Python 3 and NumPy). No external data or earlier packages are needed.

## Relationship to prior work
Curbera–Ricker (arXiv:2302.08750, first public 2023-02-17), and Albanese–Bonet–Ricker (arXiv:2305.04805, first public 2023-05-08) establish compactness, single-operator spectrum and sequence-space mapping properties of \(C_t\), and document the resolvent factorization. Their inspected full texts do not treat the cross-parameter commutator's singular-value distribution. Gallardo-Gutiérrez–Partington (arXiv:2408.03182, first public 2024-08-06) investigates Rhaly spectral and invariant-subspace structure rather than this two-parameter commutator. Bellavita–Dellepiane–Stylogiannis (arXiv:2503.21930, 2025) classify Schatten membership for row-constant Rhaly matrices in the range \(p>1\); the matrix \(K_{t,s}\) is neither of that row-constant form nor in that exponent regime. The published diagonal-commutator result *A Hilbert–Schmidt cusp trichotomy for power-diagonal commutators of generalized Cesàro operators* treats \([D_\alpha,C_t]\); at \(\alpha=1\), \(D_1=C_0\), its square-summable-norm and endpoint-cusp conclusions do not imply the present exact singular-value coefficient or the positive-parameter cross-commutators. Published Cesàro–shift and classical self-commutator Weyl results concern \([C_1,S]\) and \([C_1^*,C_1]\), respectively; neither is a statement about \([C_t,C_s]\) for fixed \(t,s<1\). General weighted Toeplitz asymptotic methods are background tools, not claimed as new.

## Limitations
The theorem is confined to fixed \(0\le s,t<1\) on Hilbert sequence space. It does not cover the classical \(t=1\) boundary, a uniform simultaneous approach to that boundary, arbitrary complex parameters, or a closed elementary form of \(J(t,s)\) at general parameter pairs. The Weyl law determines the leading ordered singular values, not a complete exact finite-index singular spectrum. The originality search does not establish absolute priority over all historically published operator-ideal literature; broader symbolic-calculus formulations may yield the same asymptotic as a less explicit corollary. No external independent mathematical validation has been performed.

## References
1. G. P. Curbera and W. J. Ricker, *Fine spectra and compactness of generalized Cesàro operators in Banach lattices in \(\mathbb C^{\mathbb N_0}\)*, arXiv:2302.08750 (first public 2023-02-17), https://arxiv.org/abs/2302.08750.
2. A. A. Albanese, J. Bonet and W. J. Ricker, *Spectral properties of generalized Cesàro operators in sequence spaces*, arXiv:2305.04805 (first public 2023-05-08), https://arxiv.org/abs/2305.04805; journal DOI 10.1007/s13398-023-01470-2.
3. E. A. Gallardo-Gutiérrez and J. R. Partington, *Rhaly operators: more on generalized Cesàro operators*, arXiv:2408.03182 (2024), https://arxiv.org/abs/2408.03182; journal DOI 10.1007/s10231-025-01560-5.
4. *A Hilbert–Schmidt cusp trichotomy for power-diagonal commutators of generalized Cesàro operators*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-hilbert-schmidt-cusp-trichotomy-for-power-diagonal-commutators--3c84886d6b6e.
5. C. Bellavita, E. Dellepiane and G. Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, arXiv:2503.21930 (2025), https://arxiv.org/html/2503.21930v3.
6. *An exact singular-value coefficient and noncommutative residue for the Cesàro–shift commutator*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-an-exact-singular-value-coefficient-and-noncommutative-residue-f--0f4f9caba4ce.
