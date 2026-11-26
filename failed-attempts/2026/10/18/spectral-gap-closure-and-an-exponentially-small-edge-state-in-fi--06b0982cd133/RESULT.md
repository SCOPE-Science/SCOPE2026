# Spectral gap closure and an exponentially small edge state in finite-rank Laguerre Hankel operators

## Finding
For each integer \(n\geq0\), each fixed real \(\tau\geq0\), and \(m=n+1\), consider the self-adjoint Hankel operator on \(L^2(0,\infty)\)
\[
(H_{n,\tau}f)(x)=\int_0^\infty e^{-(x+y)}\bigl[L_n^{(1)}(2x+2y)-\tau L_{n-1}^{(1)}(2x+2y)\bigr]f(y)\,dy,
\]
where \(L_j^{(1)}\) is the associated Laguerre polynomial and \(L_{-1}^{(1)}=0\). The operator has exactly \(m\) nonzero real eigenvalues, with \(\lceil m/2\rceil\) positive and \(\lfloor m/2\rfloor\) negative, and zero of infinite multiplicity. The inertia is a known feature of finite-rank polynomial-exponential Hankel operators, not the novelty claimed here.

The new quantitative claim is a **three-regime smallest-nonzero-singular-value law** as \(m\to\infty\), with \(\tau\) held fixed:
\[
\begin{aligned}
\lim_{m\to\infty}s_m(H_{m-1,\tau})&=\frac{1-\tau}{2} &&(0\leq\tau<1),\\
s_m(H_{m-1,1})&=\sin\frac{\pi}{4m+2}\sim\frac{\pi}{4m+2},\\
s_m(H_{m-1,\tau})&\sim\frac{\tau^2-1}{2\tau^{m+1}} &&(\tau>1).
\end{aligned}
\]
Here \(s_m\) means the smallest of the \(m\) nonzero singular values (not the \(m\)-th approximation number of the infinite null extension beyond rank). Subcritical separation, critical algebraic closure, and a supercritical exponentially small boundary mode thus coexist in one family.

For each fixed \(\tau\), the signed empirical measure of the \(m\) nonzero eigenvalues converges weakly to
\[
\nu_\tau=\frac1{2\pi}\int_0^\pi\!\left(\delta_{\sqrt{1+\tau^2-2\tau\cos\theta}/2}+\delta_{-\sqrt{1+\tau^2-2\tau\cos\theta}/2}\right)d\theta.
\]
The limiting bulk has a gap about zero of half-width \(|1-\tau|/2\) whenever \(\tau\ne1\). For each fixed \(\tau>1\), nevertheless, **exactly one** of the \(m\) singular values lies below \((\tau-1)/2\) for all sufficiently large \(m\); that exceptional singular value is the exponentially small one above. At \(\tau=1\) the bulk gap closes, and \(\nu_1\) is the arcsine probability measure on \([-1,1]\).

At the critical parameter, **every signed eigenvalue** and a corresponding normalized eigenfunction is explicit. For \(1\leq k\leq m\), put
\[
\theta_{m,k}=\frac{(2k-1)\pi}{2m+1},\quad
\lambda_{m,k}=(-1)^{k-1}\sin\!\frac{\theta_{m,k}}2,\quad
\phi_j(x)=\sqrt2e^{-x}L_j(2x),
\]
\[
\psi_{m,k}(x)=\frac{2}{\sqrt{2m+1}}\sum_{j=0}^{m-1}\sin((j+1)\theta_{m,k})\phi_j(x).
\]
Then \(H_{m-1,1}\psi_{m,k}=\lambda_{m,k}\psi_{m,k}\) and the \(\psi_{m,k}\) form an orthonormal basis of its range. In particular,
\[
\|H_{m-1,1}\|=\cos\frac{\pi}{2m+1},\qquad
\prod_{k=1}^{m}|\lambda_{m,k}|=2^{-m}.
\]

## Assumptions and scope
The Hilbert space is complex \(L^2(0,\infty)\), the kernel is real and symmetric, \(n\) is any nonnegative integer, and the scalar \(\tau\geq0\) is independent of \(n\). The Laguerre polynomials are normalized by
\[
L_j(z)=\sum_{r=0}^j(-1)^r{\binom jr}\frac{z^r}{r!},\qquad
L_j^{(1)}(z)=\sum_{r=0}^j(-1)^r{\binom{j+1}{r+1}}\frac{z^r}{r!}.
\]
The limiting statements concern nonzero singular or eigenvalues of the finite-dimensional range; the ambient operator has an infinite-dimensional nullspace. All estimates are for fixed \(\tau\); they are not claimed uniform as \(\tau\to1\) with \(m\).

## Proof
**1. Exact Laguerre matrix model.** The classical Laguerre generating function and its associated counterpart imply
\[
L_n^{(1)}(u+v)=\sum_{j+k=n}L_j(u)L_k(v),\qquad
L_{n-1}^{(1)}(u+v)=\sum_{j+k=n-1}L_j(u)L_k(v).
\]
The functions \(\phi_j(x)=\sqrt2e^{-x}L_j(2x)\) are an orthonormal basis of \(L^2(0,\infty)\). Thus, in \(\operatorname{span}\{\phi_0,\ldots,\phi_{m-1}\}\), the operator is precisely
\[
M_m(\tau)=\tfrac12R_m(I-\tau S_m),
\]
where \(R_m e_j=e_{m-1-j}\) is reversal and \(S_m e_j=e_{j+1}\) for \(j<m-1\), with \(S_me_{m-1}=0\). All other matrix entries vanish. The reversal identity \(R_mS_m=S_m^*R_m\) makes the matrix real symmetric. It has determinant \((-1)^{m(m-1)/2}2^{-m}\), so its rank is \(m\) for all parameters. Inertia stays constant as \(\tau\) varies continuously, and at \(\tau=0\) it is the inertia of reversal.

**2. Tridiagonal singular-value reduction.** By unitary invariance,
\[
4M_m(\tau)^2=(I-\tau S_m^*)(I-\tau S_m)=J_m(\tau),
\]
where \(J_m(\tau)\) has diagonal \(1+\tau^2\) in the first \(m-1\) positions, last diagonal entry \(1\), and off-diagonals \(-\tau\). For \(\tau=0\), this is the identity. For \(\tau>0\), it is the usual Toeplitz tridiagonal matrix with constant diagonal \(1+\tau^2\), corrected by \(-\tau^2 e_{m-1}e_{m-1}^*\). Its Toeplitz comparator has eigenvalues
\[
1+\tau^2-2\tau\cos\frac{k\pi}{m+1},\quad 1\le k\le m.
\]
The correction changes normalized eigenvalue counting by at most one eigenvalue per interval. Taking square roots and both signs gives the claimed limiting even moments. The signed limit follows directly because odd normalized traces vanish: for fixed \(p\), the matrix \(M_m(\tau)(M_m(\tau)^2)^p\) is supported in finitely many diagonals adjacent to the reverse diagonal, hence has at most \(O(p+1)\) potentially nonzero diagonal entries, each uniformly bounded. Thus the odd normalized traces tend to zero. All spectra are uniformly bounded by \((1+\tau)/2\), and polynomial approximation gives weak convergence to the unique symmetric measure with these moments. At \(\tau=1\), the change of variables from \(\sin(\theta/2)\) gives the arcsine law.

**3. Subcritical limit.** For \(0\le\tau<1\), the reverse triangle inequality gives \(\|(I-\tau S_m)v\|\ge(1-\tau)\|v\|\). The normalized constant vector \(v=m^{-1/2}(1,\ldots,1)\) yields \(\|(I-\tau S_m)v\|^2=m^{-1}(1+(m-1)(1-\tau)^2)\). These lower and upper bounds imply the stated limit.

**4. Supercritical exponentially small mode.** For \(\tau>1\), the exact inverse is
\[
(I-\tau S_m)^{-1}=\sum_{j=0}^{m-1}\tau^j S_m^j.
\]
After reversal of its rows, multiplication by \(\tau^{-m}\), and zero extension to \(\ell^2(\mathbb N_0)\), its entry in row \(r\), column \(s\) equals \(\tau^{-1-r-s}\) if \(r+s\le m-1\) and vanishes otherwise. These matrices converge in Hilbert–Schmidt norm to the rank-one operator with kernel \(\tau^{-1-r-s}\), whose norm is \(\tau/(\tau^2-1)\). Therefore \(\tau^{-m}\|(I-\tau S_m)^{-1}\|\to\tau/(\tau^2-1)\), so the claimed supercritical asymptotic follows from the reciprocal operator norm. Since the rank-one boundary perturbation in step 2 lowers at most one eigenvalue below the Toeplitz lower edge \((\tau-1)^2\), and the derived smallest eigenvalue tends to zero, exactly one singular value falls below \((\tau-1)/2\) for all large \(m\). Every other singular value remains in or above the bulk gap edge.

**5. Critical exact diagonalization.** When \(\tau=1\), the tridiagonal eigenproblem admits the normalized sine vectors with components \(v_j=2\sin((j+1)\theta_{m,k})/\sqrt{2m+1}\) and eigenvalues \(4\sin^2(\theta_{m,k}/2)\). The terminal boundary condition is \(v_m=v_{m-1}\), equivalent to \(\cos((m+\tfrac12)\theta_{m,k})=0\). Direct reversal of the difference vector gives \(R_m(I-S_m)v=2(-1)^{k-1}\sin(\theta_{m,k}/2)v\), proving each signed eigenvalue above. Sine orthogonality yields the normalized eigenfunctions. Their products agree with the determinant from step 1. The smallest and largest magnitudes are the displayed sine and cosine expressions.

## Verification
The standalone Python 3 file `checker.py` uses only the standard library and completes 103624 assertions. It independently checks associated Laguerre addition identities with exact rational coefficients, exact determinants and Jacobi squares for several rational parameters, orthonormal critical eigenvectors through size 80, and illustrative subcritical and supercritical finite spectral estimates. It prints `PASS 103624 checks; exact Laguerre identities, Jacobi square, determinant and finite spectral checks` when executed as `python3 checker.py`. The finite checks are diagnostic; the full infinite-parameter and limiting proofs are analytical steps 1–5, including an infinite-dimensional Hilbert–Schmidt convergence argument.

## Relationship to prior work
Yafaev's 2013 finite-rank self-adjoint Hankel theory provides sign-counting results and the polynomial-exponential finite-rank framework; this work does not claim the general inertia result as new. Da Silva's 2016 anti-pentadiagonal and 2019 anti-tridiagonal Hankel studies provide general structured finite-matrix spectral representations, including eigenvalues as zeros of rational functions. The quantitative novelty asserted here is the fixed-parameter, all-order trichotomy for the **least** nonzero singular value, the coexistence of a two-sided limiting bulk gap and exactly one exponentially small supercritical state, and a complete elementary critical signed eigenbasis for this Laguerre-integral subfamily. These are claims about implications, not merely unmatched terminology. A full-text comparison with the 2016 paper remains unresolved; see limitations.

## Limitations
The 2016 anti-pentadiagonal primary paper was available only in bibliographic abstract form; complete coverage of that family could reduce or eliminate historical priority for some finite-dimensional formulas. A later 2019 anti-tridiagonal treatment also gives general implicit eigenvalue equations, and no universal priority claim is made. The all-order edge asymptotics are proved only for each fixed parameter, not in a critical window with parameter depending on dimension. Singular values away from the extreme edge are described by a limiting empirical distribution, not a finite-size exact formula for every noncritical parameter. No independent mathematical audit has been performed.

## References
1. D. R. Yafaev, *On finite rank Hankel operators*, arXiv:1304.2677v1 (first publicly posted 2013-04-09), https://arxiv.org/abs/1304.2677.
2. J. Lita da Silva, *On anti-pentadiagonal persymmetric Hankel matrices with perturbed corners*, Computers & Mathematics with Applications 72 (2016), 415–426, doi:10.1016/j.camwa.2016.04.023 (bibliographic abstract reviewed; complete text not accessed).
3. J. Lita da Silva, *On the spectral properties of real anti-tridiagonal Hankel matrices*, arXiv:1902.06998v1 (2019-02-19), https://arxiv.org/abs/1902.06998.
