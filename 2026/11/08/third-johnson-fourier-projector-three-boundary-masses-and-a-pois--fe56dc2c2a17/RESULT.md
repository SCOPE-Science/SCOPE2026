# Third Johnson Fourier projector: three boundary masses and a Poisson–Charlier cusp
## Finding
For integers \(n\ge 2k\ge6\), let \(X_{n,k}\) be the set of all \(k\)-subsets of \([n]\) with uniform measure. Let \(P^{(3)}_{n,k}\) be the canonical orthogonal projection onto the third Johnson harmonic component (the irreducible \((n-3,3)\) component). Its rank is \(d_3=\binom n3-\binom n2\). The sharp endpoint norms \(\|P^{(3)}_{n,k}\|_{\ell^\infty\to\ell^\infty}=\|P^{(3)}_{n,k}\|_{\ell^1\to\ell^1}\) admit an exact **three-boundary-mass formula** below, using only three hypergeometric terms rather than a sum of \(k+1\) absolute values.

For every sequence with \(k/n\to\rho\in(0,1/2]\),
\[
\lim_{n\to\infty}n^{-3/2}\|P^{(3)}_{n,k}\|=\frac{\sqrt{2/\pi}}6(1+4e^{-3/2}).
\]
For every sequence with \(k\to\infty\) and \(k/\sqrt n\to c\in(0,\infty)\), instead
\[
\lim_{n\to\infty}n^{-3/2}\|P^{(3)}_{n,k}\|=\Phi(c):=\frac{\mathbb E|C_3(Z_{c^2};c^2)|}{6c^3},
\]
where \(Z_\lambda\sim\operatorname{Poisson}(\lambda)\) and
\[
C_3(j;\lambda)=j(j-1)(j-2)-3\lambda j(j-1)+3\lambda^2j-\lambda^3.
\]
The function \(\Phi\) has a genuine cusp at \(c=\sqrt3\), with exact one-sided derivative jump
\[
\Phi'_+(\sqrt3)-\Phi'_-(\sqrt3)=6e^{-3}.
\]
Further, \(\Phi(c)\sim 4c^3/3\) as \(c\downarrow0\), and \(\Phi(c)\to\sqrt{2/\pi}(1+4e^{-3/2})/6\) as \(c\to\infty\). No claim of uniqueness of this cusp is made.

## Assumptions and scope
Set \((x)_{\underline r}=x(x-1)\cdots(x-r+1)\), with \((x)_{\underline0}=1\). For a fixed \(S\in X_{n,k}\) and uniform \(T\in X_{n,k}\), put \(J=|S\cap T|\). Then \(\Pr(J=j)=w_j/W\), where \(W=\binom nk\) and \(w_j=\binom kj\binom{n-k}{k-j}\) for \(0\le j\le k\).

Write \(M_r=(k)_{\underline r}^2/(n)_{\underline r}\) for \(0\le r\le6\), and form the rational moments
\[
G_{ab}=\sum_{\ell=0}^{\min(a,b)}\binom a\ell\binom b\ell\ell!\,M_{a+b-\ell}\qquad(0\le a,b\le3).
\]
Let \(c_0,c_1,c_2\) be the unique solution to
\[
\sum_{b=0}^2G_{ab}c_b=-G_{a3}\qquad(a=0,1,2),
\]
and define the monic cubic
\[
h(j)=(j)_{\underline3}+c_2(j)_{\underline2}+c_1j+c_0.
\]
Let its three strictly ordered real roots be \(0<\alpha_1<\alpha_2<\alpha_3<k\), and put \(t_i=\lceil\alpha_i\rceil-1\). Define
\[
 b_2=\frac1{n-2},\qquad b_1=\frac{c_2-3+b_2(k^2-4k+2n-1)}{n-1},\qquad b_0=-\frac{c_0}{k^2},
\]
\[
F(j)=(k-j)^2(b_0+b_1j+b_2j^2)w_j\quad(0\le j\le k),\qquad F(-1)=0.
\]
All operations in the finite formula below use exact rational quantities except locating the three real zeros; the zeros may be isolated by rational intervals and compared with integers using signs.

The exact endpoint norm is
\[
\boxed{\|P^{(3)}_{n,k}\|=\frac{2d_3}{Wh(k)}\bigl(F(t_1)-F(t_2)+F(t_3)\bigr).}
\]
The equality extends to \(k>n/2\) by complementation after replacing \(k\) by \(n-k\). The result concerns only the *canonical third primitive idempotent*, not arbitrary equivariant linear maps or projections onto noncanonical copies.

## Proof
**Identification of the reproducing kernel.** The moment identity \(\mathbb E(J)_{\underline r}=M_r\) follows by counting ordered \(r\)-tuples in \(S\cap T\). The product rule for falling factorials gives the stated Gram matrix. Its leading \(3\times3\) block is strictly positive definite because \(J\) takes at least four values with positive probability. Hence the system uniquely defines a cubic \(h\) orthogonal to polynomials of degree at most two. The radial function \(T\mapsto h(|S\cap T|)\) lies in slice degree at most three and is orthogonal to every lower Johnson component by stabilizer averaging. Consequently it lies in the irreducible third component. The normalized kernel
\[
 K_{n,k}(S,T)=\frac{d_3}{h(k)}h(|S\cap T|)
\]
is symmetric, equivariant, has range in this component and diagonal value \(d_3\). Since the third component occurs with multiplicity one, Schur's lemma and the trace identify it as the reproducing kernel of \(P^{(3)}_{n,k}\) relative to normalized counting measure. In particular \(h(k)>0\), \(\mathbb E K_{n,k}(S,T)^2=d_3\), and transitivity gives
\[
 \|P^{(3)}_{n,k}\|=\frac{d_3}{Wh(k)}\sum_{j=0}^kw_j|h(j)|.
\]

**Reduction to three boundary masses.** The standard zero theorem for discrete orthogonal polynomials with strictly positive weights on \(0,1,\dots,k\) gives the three simple roots in \((0,k)\). For \(j\ge1\), the hypergeometric mass ratio is
\[
\frac{w_{j-1}}{w_j}=\frac{j(n-2k+j)}{(k-j+1)^2}.
\]
Expanding the displayed coefficients \(b_0,b_1,b_2\), using the three moment orthogonality identities where needed, yields for every \(0\le j\le k\):
\[
 h(j)w_j=F(j-1)-F(j).
\]
Equivalently the polynomial identity is \(h(j)=j(n-2k+j)B(j-1)-(k-j)^2B(j)\), with \(B(j)=b_0+b_1j+b_2j^2\). As \(\sum_jh(j)w_j=0\), its absolute sum is minus twice its sum over negative positions. The monic cubic is negative exactly for integer indices below \(\alpha_1\) and strictly between \(\alpha_2\) and \(\alpha_3\). Telescoping on these two intervals gives
\[
-\sum_{h(j)<0}h(j)w_j=F(t_1)-F(t_2)+F(t_3).
\]
This proves the finite exact formula, including integer-root cases since zero terms do not change the identity.

**Dense Gaussian limit.** Let \(\mu=k^2/n\) and \(\sigma^2=k^2(n-k)^2/[n^2(n-1)]\). In the bulk regime \(k/n\to\rho>0\), the standardized hypergeometric variable \(Y=(J-\mu)/\sigma\) tends to a standard Gaussian, with moments through order six converging. Orthogonalizing the monomials shows \(h(J)/\sigma^3\) tends in moments to \(H_3(Y)=Y^3-3Y\). The leading coefficient and \(k-\mu\sim\rho(1-\rho)n\) give \(h(k)\sim\rho^3(1-\rho)^3n^3\). Since \(d_3\sim n^3/6\), the normalized kernel \(n^{-3/2}K_{n,k}(J)\) converges to \(H_3(Z)/6\). Its second moments are \(d_3/n^3\to1/6\), ensuring uniform integrability of the absolute values. Finally \(\mathbb E|Z^3-3Z|=\sqrt{2/\pi}(1+4e^{-3/2})\), by integration across the zeros \(0,\pm\sqrt3\).

**Sparse Poisson limit and cusp.** If \(k/\sqrt n\to c>0\), then \(J\) converges with factorial moments through order six to a Poisson variable of mean \(\lambda=c^2\). The monic orthogonal cubic converges coefficientwise to \(C_3(j;\lambda)\), because its finite Gram matrix converges to the strictly positive Poisson Gram matrix. Now \(h(k)\sim k^3\sim c^3n^{3/2}\), yielding the claimed \(\Phi\). Exact projector second moments again bound the absolute tails uniformly. The Poisson sum for \(\Phi\) is locally uniformly differentiable away from integer roots of \(C_3(j;\lambda)\), using factorial tail bounds.

At \(\lambda=3\), \(C_3(j;3)=(j-1)(j^2-11j+27)\) has precisely one nonnegative integer root, \(j=1\). Its contribution to \(\Phi(\sqrt\lambda)\) equals \(e^{-\lambda}\lambda^{3/2}|3-\lambda|/6\); the remaining Poisson terms have continuous first derivatives at \(\lambda=3\). Taking the jump and converting \(d/d\lambda\) to \(d/dc\) gives \(6e^{-3}\). For \(\lambda\downarrow0\), contributions from \(j=0,1,2,3\) sum to \(8\lambda^3+o(\lambda^3)\), while larger \(j\) contribute smaller order; thus \(\Phi(c)\sim4c^3/3\). As \(\lambda\to\infty\), the standardized Charlier cubic converges in moments to \(H_3(Z)\), giving the Gaussian constant.

## Verification
The standalone `verify_johnson3.py` uses only Python's standard library. It checks all \(784\) parameter pairs \(6\le n\le60\), \(3\le k\le\lfloor n/2\rfloor\) with exact rational arithmetic: Gram orthogonality, kernel normalization, exact second moment, coefficient-wise telescoping, and agreement of direct and boundary absolute sums. It independently constructs complete projector matrices for \((n,k)=(6,3),(7,3),(8,3)\), proving their numerical instances of idempotence by rational arithmetic. The Poisson cusp and large-mean limit are additionally checked numerically; neither replaces the analytic arguments.

Run `python3 verify_johnson3.py` in a directory containing the file. Expected terminal result begins `JOHNSON_THIRD_ENDPOINT_CHECKS_PASS`.

## Relationship to prior work
Scarabotti–Tolli (arXiv:math/0701533) develop harmonic analysis on finite homogeneous spaces, including Johnson Gelfand-pair machinery. Filmus (arXiv:1406.0142) constructs slice harmonic bases, and Krebs–Shaheen (2008) analyze Johnson eigenpolynomials; these identify the third component and the Hahn/Eberlein polynomial framework, rather than evaluating this endpoint absolute-kernel norm. A closely related published degree-two Johnson endpoint calculation gives a two-boundary formula and bulk growth proportional to \(n\), but explicitly does not treat degree three. Sobrino–Dehesa (2022) survey \(L^q\)-norm problems for orthogonal polynomials and describe discrete-family questions as substantially open, but their reported results do not give this precise Johnson third-projection endpoint or its Poisson cusp. The present result does not claim originality of classical orthogonal polynomials, primitive idempotents, or their general spectral theory.

## Limitations
The theorem is restricted to canonical degree-three Johnson projection, \(k\ge3\), and the two specified growing-parameter regimes; a fixed-\(k\) limit, complete regularity classification of \(\Phi\), and arbitrary higher-degree analogues are not claimed. Although the finite formula is a complete evaluation of the natural endpoint invariant, literature priority for a stronger unlocated general identity remains uncertain. The cusp is a non-differentiability point of the explicitly normalized limiting profile, not an instability of any individual finite projection.

## References
1. F. Scarabotti and F. Tolli, *Harmonic analysis on a finite homogeneous space*, arXiv:math/0701533, first public 2007-01-19.
2. Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142, first public 2014-06-01.
3. M. Krebs and A. Shaheen, *On the spectra of Johnson graphs*, Electronic Journal of Linear Algebra **17** (2008), 154–167, DOI 10.13001/1081-3810.1256.
4. N. Sobrino and J. S. Dehesa, *Parameter and q asymptotics of Lq-norms of hypergeometric orthogonal polynomials*, International Journal of Quantum Chemistry **123** (2023), e27013, first public journal site 2022-09-14, DOI 10.1002/qua.27013.
5. *Exact endpoint norm of the second Johnson spherical projector*, published research record, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-endpoint-norm-of-the-second-johnson-spherical-projector--f9735429621e/RESULT.md.
