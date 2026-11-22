# Exact gcd spectra of rationally coupled polynomial floors

## Finding

**Theorem.** Let \(b\ge1\) be an integer and let \(f\in\mathbb R[X]\) have at least one irrational coefficient of positive degree. For positive integers \(n\), define
\[
G_{b,f}(n)=\gcd\left(n,\lfloor f(n)\rfloor,\left\lfloor f(n)+\frac nb\right\rfloor\right),
\]
using the nonnegative greatest common divisor. For every integer \(d\ge1\), the natural density of \(G_{b,f}(n)=d\) exists and is independent of \(f\). Put
\[
H_c(d)=\begin{cases}
\displaystyle \frac{1}{d^2}\prod_{p\mid c/d}(1-p^{-2}),&d\mid c,\\
0,&d\nmid c,
\end{cases}\qquad c\ge1,
\]
where the product is over distinct prime factors (and is \(1\) for an empty product). Then the density is
\[
\boxed{\pi_b(d)=\frac{1}{b\zeta(2)d^2}
+\frac{2}{b^2}\sum_{c=1}^{b-1}(b-c)H_c(d).}
\tag{1}
\]
These masses sum to one. In particular, for **every** \(d\ge b\),
\[
\boxed{\pi_b(d)=\frac{1}{b\zeta(2)d^2};}
\tag{2}
\]
the correlated triple retains an exact two-variable zeta tail at all such gcd values. At \(b=2\), \(\pi_2(1)=\tfrac12+\tfrac1{2\zeta(2)}\).

As \(b\to\infty\), the entire distribution converges in total variation to the standard three-integer gcd law, with the uniform quantitative bound
\[
\boxed{\frac12\sum_{d\ge1}\left|\pi_b(d)-\frac{1}{\zeta(3)d^3}\right|
\ll\frac{(\log(2b))^2}{b^2}.}
\tag{3}
\]
In particular, for each fixed \(d\),
\[
\pi_b(d)=\frac{1}{\zeta(3)d^3}
+O_d\left(\frac{1+\log b}{b^2}\right).
\]
The limit in \(n\) is taken **first** for fixed \(b,f\); then \(b\to\infty\). No simultaneous growth regime is claimed.

## Assumptions and scope

The parameter \(b\) is any fixed positive integer; \(f\) may have arbitrary real coefficients and any positive degree, provided that one nonconstant coefficient is irrational. Its constant term and the other coefficients are unrestricted. Negative floor values are allowed. The gcd is always positive because \(n\ge1\). \(\zeta\) denotes the Riemann zeta function. Formula (1) gives the complete mass function, including \(b=1\), which specializes to the published two-variable gcd law. The new phenomena concern coupled pairs of floors at \(b\ge2\).

## Proof

**1. Residue/phase reduction.** Write \(n=bm+r\), where \(0\le r<b\), let \(T=\lfloor f(n)\rfloor\), and let \(U=\{f(n)\}\in[0,1)\). Define \(e=0\) when \(r=0\), and for \(1\le r<b\) put \(e=\mathbf1_{\{U\ge1-r/b\}}\). The exact floor identity is
\[
\left\lfloor f(n)+\frac nb\right\rfloor=T+m+e.
\]
Integer column operations on the gcd yield the exact pointwise equality
\[
G_{b,f}(n)=\gcd(bm+r,T,m+e)=\gcd(r-be,T,m+e).
\tag{4}
\]
In the class \(r=0\), (4) equals \(\gcd(m,\lfloor f(bm)\rfloor)\). In a class \(1\le r<b\), it equals \(\gcd(r,T,m)\) on the phase interval \(U<1-r/b\), of relative length \((b-r)/b\), and \(\gcd(b-r,T,m+1)\) on its complement, of relative length \(r/b\).

**2. Exact local distributions for nonzero residues.** For every fixed \(r\), the polynomial \(m\mapsto f(bm+r)\) retains an irrational nonconstant coefficient: take the *highest-degree* irrational coefficient of \(f\), whose contribution to the corresponding coefficient after affine substitution is an irrational nonzero integer multiple, while all higher-degree contributions there are rational. Weyl's theorem therefore gives equidistribution of \(f(bm+r)/D\) modulo one on every subprogression \(m\equiv u\pmod D\), for each positive integer \(D\). In particular, for a fixed integer \(c\ge1\), the joint limiting distribution of
\[
(m\bmod c,\quad T\bmod c,\quad U)
\]
is uniform on the two residue coordinates and Lebesgue-uniform on \([0,1)\). (The floor residue and phase condition correspond to an interval for \(f(bm+r)/c\); its endpoints have zero frequency.) Thus the two phase intervals in step 1 are independent of the two residue coordinates and have the stated lengths.

If \(X,Y\) are independent uniform residues modulo \(c\), then the exact probability that \(\gcd(c,X,Y)=d\) equals \(H_c(d)\). Indeed, for a prime power \(p^a\parallel c\), when \(p^j\parallel d\) with \(j<a\), its local probability is \(p^{-2j}(1-p^{-2})\); when \(j=a\), it is \(p^{-2a}\). The Chinese remainder theorem gives the product in the definition of \(H_c\). Therefore the conditional mass at \(d\), on the class \(r\), is
\[
\frac{b-r}{b}H_r(d)+\frac r b H_{b-r}(d).
\tag{5}
\]

**3. The divisible-by-\(b\) class and large prime tail.** On \(r=0\), we must obtain the complete, rather than only coprime, gcd distribution of \(m\) and \(\lfloor f(bm)\rfloor\). For each fixed modulus \(D\), Weyl equidistribution makes the pair of residues \((m,\lfloor f(bm)\rfloor)\pmod D\) uniformly distributed. Hence the finite-prime valuation truncations agree with those for two independent uniformly sampled integers; high powers of any fixed prime are negligible because the probability of simultaneous divisibility by \(p^A\) is exactly \(p^{-2A}\) in the limit as \(M	o\infty\). Holdridge's large-prime theorem (Theorem 1.3 of the cited work, degree at least two; the linear case follows from Champagne's theorem cited there) shows
\[
\lim_{R\to\infty}\limsup_{M\to\infty}\frac1M
\#\{m\le M:\exists p>R\text{ prime},\ p\mid m,\ p\mid\lfloor f(bm)\rfloor\}=0.
\]
The polynomial \(f(bm)\) satisfies the same irrational-coefficient hypothesis, so this theorem applies without any Diophantine-type restriction. The finite-prime distributions therefore converge to the full gcd masses \(1/(\zeta(2)d^2)\). For example, the probability of the event \(\gcd(m,\lfloor f(bm)\rfloor)=d\) is the limit of finite-prime restrictions after the large-prime tail is removed; the standard Euler product gives the stated mass. This handles all \(d\ge1\), not only \(d=1\).

**4. Assemble the exact law.** Each class \(r\pmod b\) has density \(1/b\). The class \(r=0\) contributes \(1/(b\zeta(2)d^2)\). Summing (5) over \(r=1,\ldots,b-1\), and replacing \(r\) by \(b-r\) in its second term, yields exactly (1). For each \(c\), \(\sum_{d\ge1}H_c(d)=1\) because it is a genuine gcd distribution. Also \(\sum_{d\ge1}1/(\zeta(2)d^2)=1\); the weights in (5) sum to one in each residue class. Thus \(\sum_d\pi_b(d)=1\). As \(d\ge b\) divides none of \(1,\ldots,b-1\), (2) follows.

**5. Quantitative approach to the three-integer law.** For \(d<b\), let \(\mu\) be the Möbius function and write \(A(j)=\prod_{p\mid j}(1-p^{-2})=\sum_{\ell\mid j}\mu(\ell)/\ell^2\). Substituting \(c=dj\) in (1) gives
\[
\pi_b(d)=\frac1{b\zeta(2)d^2}
+\frac{2}{b^2d^2}\sum_{1\le j<b/d}(b-dj)A(j).
\tag{6}
\]
For each integer \(\ell<b/d\), put \(x_\ell=b/(d\ell)\), \(k_\ell=\lfloor(b-1)/(d\ell)\rfloor\), and \(\theta_\ell=x_\ell-k_\ell\in(0,1]\). The finite arithmetic-progression identity
\[
\sum_{1\le h<x_\ell}(b-d\ell h)
=\frac{d\ell}{2}\bigl(x_\ell^2-x_\ell+\theta_\ell(1-\theta_\ell)\bigr)
\]
turns (6) **exactly** into
\[
\pi_b(d)=\frac1{d^3}\sum_{\ell<b/d}\frac{\mu(\ell)}{\ell^3}
+\frac1{bd^2}\left(\frac1{\zeta(2)}-\sum_{\ell<b/d}\frac{\mu(\ell)}{\ell^2}\right)
+\frac1{b^2d}\sum_{\ell<b/d}\frac{\mu(\ell)\theta_\ell(1-\theta_\ell)}{\ell}.
\tag{7}
\]
Since \(0\le\theta(1-\theta)\le1/4\), the tails of the absolutely convergent series for \(1/\zeta(2)\) and \(1/\zeta(3)\) give, uniformly for \(1\le d<b\),
\[
\left|\pi_b(d)-\frac1{\zeta(3)d^3}\right|
\ll \frac{1+\log(b/d)}{b^2d}.
\]
Summing over \(d<b\) costs at most \(O((\log(2b))^2/b^2)\). For \(d\ge b\), (2) and \(\sum_{d\ge b}d^{-2}\ll b^{-1}\), \(\sum_{d\ge b}d^{-3}\ll b^{-2}\), give an additional \(O(b^{-2})\). This establishes (3) and its fixed-\(d\) consequence.

## Verification

The standalone standard-library script `verify.py` independently enumerates 496 exact finite CRT gcd frequencies for \(1\le c\le31\) and checks them against \(H_c\), verifies 3500 exact Möbius-expansion equalities at rational test values for the zeta parameter, and computes finite-sample gcds for \(f(n)=\sqrt2\,n^2\) using integer square roots only. The output begins `DEPENDENT_FLOOR_GCD_CHECK_OK`. These checks test the arithmetic and symbolic finite reductions, **not** the unbounded Weyl theorem, the published large-prime theorem, or infinite-limit convergence.

## Relationship to prior work

Holdridge's arXiv:2611.02223v1 (November 1, 2026) proves the coprimality density \(1/\zeta(s)\) under *total homogeneous equidistribution* of the floor-coordinate vector, and proves the essential large-prime estimate for one irrational polynomial floor and the integer index. In the present triple the two polynomial arguments differ by \(n/b\), so their vector fails that equidistribution hypothesis. Its \(b=1\) two-coordinate consequence is not new. The present exact full histogram (1), finite-denominator tail (2), and quantitative approach (3) are not statements of that paper.

A prior result on split integer polynomials and equidistributed floor coordinates gives Euler factors for \(\gcd(P(n),\lfloor f_i(n)\rfloor)=1\) but also requires total homogeneous equidistribution of those coordinates. Another result on rational floor dilations determines \(\gcd(n,\lfloor pn/q\rfloor)\) for rational slopes; that polynomial pair has no irrational equidistribution hypothesis and lacks the coupled third coordinate considered here. Banks and Shparlinski's earlier polynomial-floor asymptotics likewise require independent-type polynomial coordinates and do not state this dependent full histogram. The proof explicitly imports the published large-prime ingredient; novelty is confined to the dependent-triple exact spectrum and the quantitative parameter transition.

## Limitations

The fixed-\(b\), fixed-\(f\) density limit need not have an effective rate; (3) compares limiting mass functions as \(b\to\infty\), **not** the finite-\(n\) distributions with growing \(b\). The hypothesis cannot simply be dropped for rational-coefficient polynomials, since equidistribution and large-prime control fail in general. An unindexed equivalent formulation may exist; no assertion of exhaustive historical uniqueness or independent audit is made. The infinite result depends on the cited existing large-prime theorem for polynomial floors.

## References

1. Philippa Holdridge, *On the probability that the integer parts of polynomials are coprime*, arXiv:2611.02223v1, first public 2026-11-01, https://arxiv.org/html/2611.02223v1 (Introduction, Theorems 1.2–1.3 and Section 6).
2. William Banks and Igor E. Shparlinski, *On the greatest common divisor of integer parts of polynomials*, arXiv:2205.00253v3, https://arxiv.org/html/2205.00253v3.
3. Jérémy Champagne, *On the greatest common divisor of* \(n\) *and polynomial integer parts*, arXiv:2607.27533 (2026); cited in Holdridge, reference [3].
4. *Coprimality densities for split integer polynomials and equidistributed integer parts*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-coprimality-densities-for-split-integer-polynomials-and-equidist--bcbc904e31ef.
5. *Numerator-independent gcd histograms for rational floor dilations*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-numerator-independent-gcd-histograms-for-rational-floor-dilation--86c702b63d42.
