# Only the unperturbed constant yields a subnormal integro-multiplication operator

## Finding
For every \(a\in\mathbb C\), let \(\mathcal H_a\) be the reproducing-kernel Hilbert space on the open unit disk whose orthonormal basis is
\[
f_n(z)=(n+1+az)z^n,\qquad n=0,1,2,\ldots.
\]
The coordinate multiplier \(M_z\) is bounded, and
\[
\boxed{\;M_z\text{ is subnormal}\quad\Longleftrightarrow\quad a=0.\;}
\]
Thus no nonzero constant parameter yields a subnormal operator in this family. The proof uses a pointwise incompatibility between the unique radial moment measure and a required first angular moment, rather than finite tests of hyponormality.

## Assumptions and scope
All parameters \(a\) are finite complex numbers, with no smallness, reality, or sign restriction. The Hilbert-space inner product is linear in its first argument. Subnormality means existence of a normal extension of the bounded multiplier, equivalently a positive representing measure for all mixed monomial Gram moments of the cyclic vector \(1\). The result concerns this particular tridiagonal basis and not arbitrary symbols \(\varphi\) in the larger integro-multiplication class.

A convenient boundedness check uses the unilateral shift \(S\) on \(\ell^2(\mathbb N_0)\) and \(D=\operatorname{diag}(1,2,3,\ldots)\). The Taylor-coefficient map on the basis is \(B=D+aS=(I+aSD^{-1})D\). For every integer \(k\ge0\), \(\|(SD^{-1})^k\|\le1/k!\), so \((I+aSD^{-1})^{-1}\) exists and \(B^{-1}=D^{-1}(I+aSD^{-1})^{-1}\) is bounded. On finitely supported coefficients, \(BS-SB=S\), hence the multiplier has the bounded matrix \(B^{-1}SB=S-B^{-1}S\). Moreover, each monomial has a convergent coefficient expansion in the displayed orthonormal basis.

## Proof
**1. Exact monomial Gram data.** Solving the triangular coefficient system gives, in Hilbert-space norm,
\[
z^n=\sum_{j=0}^{\infty}\frac{(-a)^j n!}{(n+j+1)!}\,f_{n+j}.
\]
Thus, for every integer \(n\ge0\),
\[
m_n:=\|z^n\|^2=\sum_{j=0}^{\infty}|a|^{2j}\left(\frac{n!}{(n+j+1)!}\right)^2,
\qquad
\langle z^n,z^{n+1}\rangle=-\frac{a}{n+1}m_{n+1}.
\tag{1}
\]
Both identities follow by orthonormality and absolute convergence. In particular \(m_n\le C_a/(n+1)^2\), where \(C_a=\sum_{j\ge0}|a|^{2j}/(j!)^2<\infty\). Hence \(m_n\to0\).

**2. The unique radial measure.** Define the entire nonnegative series
\[
I_0(2u)=\sum_{j=0}^{\infty}\frac{u^{2j}}{(j!)^2},\qquad u\ge0,
\]
and, for \(0<q<1\), the density
\[
\rho_a(q)=\int_q^1\frac1t I_0\!\left(2|a|\sqrt{(1-t)(1-q/t)}\right)dt.
\tag{2}
\]
The elementary beta identity
\[
\int_0^1t^n(1-t)^jdt=\frac{n!\,j!}{(n+j+1)!}
\]
and the substitution \(q=tu\) in a product of two such integrals imply, by Tonelli,
\[
\int_0^1q^n\rho_a(q)\,dq=m_n\quad(n\ge0).
\tag{3}
\]
Because \(I_0\) is increasing on nonnegative real arguments,
\[
0<\rho_a(q)\le I_0(2|a|)\log(1/q),
\qquad \lim_{q\downarrow0}\sqrt q\rho_a(q)=0.
\tag{4}
\]
Also \(\int_0^1\rho_a(q)\,dq=m_0>0\).

**3. Any normal extension would contradict the angular moment.** Suppose \(M_z\) is subnormal. Since polynomials are dense and \(1\) is cyclic, a finite positive Borel measure \(\mu\) exists on the complex plane with
\[
\langle z^n,z^m\rangle=\int_{\mathbb C}z^n\overline z^{\,m}\,d\mu(z)
\qquad(n,m\ge0).
\tag{5}
\]
The bounds \(m_n\to0\) rule out mass at \(|z|>1\) and at \(|z|=1\), so \(\mu\) is supported in the closed unit disk. The pushforward \(\nu=(|z|^2)_*\mu\) has moments \(m_n\). Uniqueness of finite Borel measures on \([0,1]\) from their polynomial moments, together with (3), forces
\[
 d\nu(q)=\rho_a(q)\,dq.
\tag{6}
\]
Define the complex measure on \([0,1]\)
\[
\eta(E)=\int_{\{|z|^2\in E\}}\overline z\,d\mu(z).
\]
For every Borel set \(E\), its variation is bounded by \(|\eta|(E)\le\int_E\sqrt q\,d\nu(q)\). Equation (1) shows that
\[
\int_0^1q^n\,d\eta(q)=-\frac a{n+1}m_{n+1}.
\]
Let \(F_a(q)=\int_q^1\rho_a(t)\,dt\). Fubini and (3) yield
\[
\int_0^1q^nF_a(q)\,dq
=\frac1{n+1}\int_0^1t^{n+1}\rho_a(t)\,dt
=\frac{m_{n+1}}{n+1}.
\]
Uniqueness of finite complex measures on \([0,1]\) now forces \(d\eta(q)=-aF_a(q)\,dq\). From (6) and the variation bound we obtain
\[
|a|F_a(q)\le\sqrt q\rho_a(q)\quad\text{for almost every }q\in(0,1).
\tag{7}
\]
As \(q\downarrow0\), the left side tends to \(|a|m_0\), whereas the right side tends to zero by (4). For every \(a\ne0\), this contradicts (7), proving necessity.

**4. The zero parameter.** If \(a=0\), the basis consists of \((n+1)z^n\) and \(m_n=(n+1)^{-2}\), with all off-diagonal monomial moments zero. The positive rotationally invariant measure
\[
\int_{\overline{\mathbb D}}h(z)\,d\mu_0(z)
=\int_0^1\int_0^{2\pi}h(\sqrt q e^{i\theta})\frac{d\theta}{2\pi}(-\log q)\,dq
\]
has exactly those mixed moments, so multiplication by \(z\) on \(\mathcal H_0\) is the restriction of normal multiplication on \(L^2(\mu_0)\). This proves sufficiency.

## Verification
The proof covers all integers \(n\ge0\) and all complex parameters. The only nonstandard integral calculation is (2)–(3), which is obtained from a positive termwise beta expansion; no truncated series is used to infer a global property. The accompanying `CHECK.py` independently recomputes finite truncations of the norm, mixed moment, density-moment and primitive-moment identities using exact rational arithmetic. It is supplementary; the contradiction (7) is analytic and is not inferred from a numerical experiment. Reproduce with `python CHECK.py`.

## Relationship to prior work
Adams, Feldman and McGuire (2022) investigate precisely the kernels with \(f_n(z)=(n+1+\varphi(z)z)z^n\). Their Proposition 11 proves non-subnormality for the single parameter \(a=1\), using a Lambert criterion. Their final discussion explicitly leaves open whether any nonzero constant choice could be subnormal. The theorem above gives a complete complex-parameter answer. Their exact \(a=1\) Gram data and single-parameter obstruction are acknowledged as prior results, not asserted as new here.

Adams, Feldman and McGuire (2013), Section 4, already ask about the particular \(a=1\) tridiagonal basis and provide monomial Gram identities; this older question was addressed for \(a=1\) by the 2022 paper. Adams and Wagner (first posted 28 August 2019) study a distinct but relevant class of finite-bandwidth RKHS and provide dated contemporary context for multiplication-operator methods. Neither inspected source proves the nonzero-complex-parameter classification through the radial-angular incompatibility above. The 2019 manuscript is the earliest source used here with an independently verified exact public day; the 2022 article's publisher establishes its September 2022 issue but not an exact original online day. The 2013 paper is older historical background for a previously settled special parameter, not the all-parameter question.

## Limitations
The conclusion is confined to the constant-parameter family. No claim is made about general nonconstant \(\varphi\), stronger polynomial-hyponormality thresholds, or priority against inaccessible or unindexed subsequent research. The proof supplies no finite-degree obstruction uniform in \(a\); its obstruction uses unique infinite Hausdorff moments. The 2022 source's exact day of first public posting is unverified. Independent mathematical validation has not been performed.

## References
1. G. T. Adams, N. S. Feldman, P. J. McGuire, *A Class of Integro-Multiplication Operators*, Operators and Matrices **16** (2022), 581–610, DOI: 10.7153/oam-2022-16-44, https://files.ele-math.com/articles/oam-16-44.pdf; especially Proposition 11 and the last discussion on p. 609.
2. G. T. Adams, N. S. Feldman, P. J. McGuire, *Tridiagonal Reproducing Kernels and Subnormality*, Journal of Operator Theory **70** (2013), 477–494, DOI: 10.7900/jot.2011sep12.1942, https://jot.theta.ro/jot/archive/2013-070-002/2013-070-002-007.pdf; Section 4.
3. G. T. Adams, N. A. Wagner, *A Functional Decomposition of Finite Bandwidth Reproducing Kernel Hilbert Spaces*, arXiv:1908.10822, first posted 28 August 2019, https://arxiv.org/abs/1908.10822.
