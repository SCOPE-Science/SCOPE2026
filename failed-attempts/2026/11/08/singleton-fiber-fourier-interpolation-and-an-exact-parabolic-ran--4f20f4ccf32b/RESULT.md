# Singleton-fiber Fourier interpolation and an exact parabolic rank transition

## Finding

Let \(p\ge3\) be an odd prime, let \(\zeta=\exp(2\pi i/p)\), and let \(h:\mathbb F_p\to\mathbb F_p\) satisfy \(h(0)=0\). Define the multiplicative-Hankel phase matrix
\[
M_h=(\zeta^{h(st)})_{s,t\in\mathbb F_p}.
\]
**Singleton-fiber interpolation theorem.** If some \(y\in\mathbb F_p\) has exactly one preimage in \(\mathbb F_p^\times\), then \(M_h\) is invertible over \(\mathbb C\). This hypothesis is sufficient, not necessary.

For the geometric parabola \(\Gamma=\{(t,t^2):t\in\mathbb F_p\}\) consider the bilinear pairing \(\langle(x_1,x_2),(y_1,y_2)\rangle_{a,b}=a x_1y_1+b x_2y_2\), with arbitrary \(a,b\in\mathbb F_p\). Its unnormalized self-restriction Fourier matrix is
\[
M_{p;a,b}(s,t)=\zeta^{a st+b s^2t^2}.
\]
The **complete rank trichotomy** is
\[
\boxed{\operatorname{rank}_{\mathbb C}M_{p;a,b}=
\begin{cases}
p,&a\ne0,\\
(p+1)/2,&a=0,\ b\ne0,\\
1,&a=b=0.
\end{cases}}
\]
In the middle case, the nullspace is precisely the space of functions \(f:\mathbb F_p\to\mathbb C\) satisfying \(f(0)=0\) and \(f(-t)=-f(t)\) for every \(t\ne0\). Thus every nonzero linear-coordinate Fourier coupling gives full sampling rank \(p\), while its removal leaves rank \((p+1)/2\), without changing the parabola or its number of samples.

**Complete singular-value description.** For every multiplicative character \(\chi\) of \(\mathbb F_p^\times\), put
\[
K_\chi=\sum_{u\in\mathbb F_p^\times}\chi(u)\zeta^{a u+b u^2},\qquad S=K_1,
\]
and define \(T=2p-1+|S|^2\), \(\Delta=|S-(p-1)|^2\). The squared singular-value multiset is
\[
\left\{\frac{T+\sqrt{T^2-4\Delta}}2,\ \frac{T-\sqrt{T^2-4\Delta}}2\right\}
\ \cup\ \bigl\{|K_\chi|^2:\chi\ne1\bigr\},
\]
with each nontrivial character counted once. This formula applies in all three rank regimes, including the zero singular values. The normalization is the unnormalized Fourier convention; no factor of \(p^{-1/2}\) is included.

## Assumptions and scope

All parameters, products, and polynomial evaluations inside an exponent are taken in the prime field \(\mathbb F_p\), then represented by residues \(0,\ldots,p-1\). The complex rank is evaluated in characteristic zero, not modulo \(p\). The interpolation theorem applies to any function \(h\) with \(h(0)=0\) and a singleton nonzero-domain fiber; the exact trichotomy and singular-value formula apply to the quadratic function \(h(u)=a u+b u^2\). Nothing is asserted here for extension fields \(\mathbb F_{p^r}\) with \(r>1\), or for even characteristic.

## Proof

**1. Multiplicative-character decomposition.** Write \(U=\mathbb F_p^\times\). Split \(\mathbb C^{\mathbb F_p}\) orthogonally into the two-dimensional subspace spanned by the point mass at zero and the constant vector on \(U\), plus the one-dimensional spaces spanned by each nontrivial multiplicative character on \(U\), extended by zero at zero. For a character \(\chi\ne1\) and \(s\in U\), substitution \(u=st\) gives
\[
(M_h\chi)(s)=\chi(s)^{-1}K_\chi(h),\quad K_\chi(h)=\sum_{u\in U}\chi(u)\zeta^{h(u)},\quad (M_h\chi)(0)=0.
\]
The characters have common norm \(\sqrt{p-1}\). On the two-dimensional orthonormal constant block, \(M_h\) is exactly
\[
\begin{pmatrix}1&\sqrt{p-1}\\\sqrt{p-1}&K_1(h)\end{pmatrix}.
\]
Thus the nontrivial-character singular values are \(|K_\chi(h)|\), and the constant-block determinant equals \(K_1(h)-(p-1)\). Its squared singular values are the two roots of \(z^2-Tz+\Delta\), where \(T=2p-1+|K_1(h)|^2\) and \(\Delta=|K_1(h)-(p-1)|^2\).

**2. The singleton-fiber nonvanishing lemma.** Let \(\chi\ne1\) and put \(E=\mathbb Q(\zeta_{p-1})\), a field containing the values of \(\chi\). Because \(\gcd(p,p-1)=1\), the minimal polynomial of \(\zeta\) over \(E\) remains \(\Phi_p(X)=1+X+\cdots+X^{p-1}\). For every \(y\in\mathbb F_p\), let \(c_y=\sum_{u\in U,\ h(u)=y}\chi(u)\). The equation \(K_\chi(h)=\sum_y c_y\zeta^y=0\) implies that all \(c_y\) are equal. Yet \(\sum_y c_y=\sum_{u\in U}\chi(u)=0\), so they must all vanish. At a singleton fiber \(h^{-1}(y_0)\cap U=\{u_0\}\), however, \(c_{y_0}=\chi(u_0)\ne0\), contradiction. Hence each nontrivial \(K_\chi(h)\ne0\).

The same singleton-fiber hypothesis implies that \(h\) is not identically zero on \(U\): if its unique singleton image is zero, at least one other element of \(U\) maps to a nonzero value, since \(|U|=p-1\ge2\). Therefore \(K_1(h)=\sum_{u\in U}\zeta^{h(u)}\ne p-1\), because equality in the triangle inequality with this positive real value would require every phase to be \(1\). The constant block and all other blocks are invertible. This proves the interpolation theorem.

**3. The quadratic trichotomy.** If \(a\ne0\) and \(b\ne0\), the equation \(a u+b u^2=0\) has exactly one nonzero solution \(u=-a/b\), so Step 2 applies. If \(a\ne0,b=0\), the matrix is simply a row-permuted prime Fourier matrix, hence invertible (and all singular values are \(\sqrt p\)).

If \(a=0,b\ne0\), both rows and columns are unchanged under \(s\mapsto-s\) and \(t\mapsto-t\), so the rank is at most \((p+1)/2\). After identifying \(t\) and \(-t\), the resulting square matrix is \((\zeta^{buv})_{u,v\in Q}\), where \(Q=\{0\}\cup\{t^2:t\in U\}\) has \((p+1)/2\) elements. This is a square minor of the prime \(p\)-point Fourier matrix. Chebotarev's nonvanishing theorem for prime Fourier minors shows it is invertible. Thus the rank is exactly \((p+1)/2\), with the claimed odd-function nullspace. Alternatively, Step 2's cyclotomic reasoning on nontrivial *even* multiplicative characters and the pairing cancellation on odd characters give the same rank. Finally if \(a=b=0\), every entry is \(1\), so the rank is \(1\).

**4. The singular-value formula.** The first step gives all \(p-2\) nonconstant squared singular values \(|K_\chi|^2\). The exceptional two-dimensional block \(B\) has \(\operatorname{tr}(B^*B)=2p-1+|S|^2\) and \(\det(B^*B)=|S-(p-1)|^2\). Its squared singular values are the two roots displayed in the Finding. This accounts for exactly \(p\) values and proves the complete formula for every \(a,b\).

## Verification

A standalone checker `check_parabola.py` builds the actual phase matrices at exact finite-field roots of unity modulo auxiliary primes \(\ell\equiv1\pmod p\), performs modular Gaussian elimination, and confirms rank **lower bounds** agreeing with the proved upper bounds. A nonzero modular minor proves that the corresponding complex cyclotomic minor is nonzero; the checker never interprets a singular reduction at one auxiliary prime as a complex singularity, and tries other auxiliary primes. It checks all \(a,b\) for \(p=3,5,7,11\) and selected pairs for \(p=13,17,19,23,29\), totaling 239 rank cases. It separately checks the multiplicative-character action, nonvanishing and zero patterns, and the exceptional-block squared-singular-value identities numerically in 24 cases through \(p=17\). Execute `python3 check_parabola.py` in this directory. These finite checks corroborate, rather than replace, the proof for every odd prime.

## Relationship to prior work

Mockenhaupt–Tao initiated Fourier restriction to finite-field paraboloids, while Iosevich–Koh studied restriction/extension estimates for quadratic surfaces. Neither inspected analysis provides this square on-curve Fourier interpolation rank trichotomy or multiplicative-Hankel character spectrum. Tao's prime-order uncertainty principle proves every square minor of the ordinary one-dimensional prime Fourier matrix is nonzero; that theorem supplies the pure-quadratic branch after identifying opposite points, but does not imply the full-rank mixed quadratic branch of the two-dimensional Fourier restriction. The published complete description of orthogonal exponential spectra of the parabola over odd prime-power rings concerns *unitary orthogonal bases*, rather than the generally nonorthogonal self-restriction matrix here. A published exact Fourier-frame spectrum on a three-dimensional finite-field paraboloid concerns a different frequency family and ambient geometric object. A recent full-surface sparse parabolic uncertainty theorem constrains zero sets of sparse coefficient vectors, not the invertibility of the complete \(p\)-column self-restriction matrix or the rank trichotomy. The key distinct mechanisms are singleton-fiber cyclotomic nonvanishing and sharp loss of half the modes when the linear-coordinate coupling disappears.

## Limitations

No uniform numerical lower bound on the smallest nonzero singular value is claimed; finite examples exhibit poor conditioning despite exact invertibility. Character sums in the singular-value formula are finite exact expressions but are not evaluated by elementary radicals for every character and prime. The singleton-fiber condition is sufficient but not necessary for arbitrary nonlinear \(h\). The argument does not extend automatically to prime-power fields, where the additive character sees the trace of a polynomial and singleton fibers may be lost. A general older theorem on multiplicative character twists of quadratic exponential sums could imply this specialization; that historical-priority risk remains.

## References

- Gerd Mockenhaupt and Terence Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1, first posted 2002-04-18, https://arxiv.org/abs/math/0204234.
- Terence Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286v1, first posted 2003-08-29, https://arxiv.org/abs/math/0308286.
- Alex Iosevich and Doowon Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, first posted 2008-04-28, https://arxiv.org/abs/0804.4505.
- *Complete exponential spectra of the parabola over odd prime-power rings*, publicly indexed result, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-exponential-spectra-of-the-parabola-over-odd-prime-powe--2cf08dd7e325.
- *Exact seven-level Fourier-frame spectrum on the finite-field paraboloid*, publicly indexed result, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-seven-level-fourier-frame-spectrum-on-the-finite-field-par--b205e1a359db.
- Dongwei Li, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola*, arXiv:2609.16030v1, first posted 2026-09-11, https://arxiv.org/abs/2609.16030.
