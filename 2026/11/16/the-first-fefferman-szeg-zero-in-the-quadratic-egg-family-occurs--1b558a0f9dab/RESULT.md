# The first Fefferman–Szegő zero in the quadratic egg family occurs in dimension eleven

## Finding
For every integer \(2\le n\le 11\), put
\[
 E_{n,2}=\{(z,w)\in\mathbb C^{n-1}\times\mathbb C:\|z\|^2+|w|^4<1\}.
\]
Equip its boundary with Fefferman surface measure and let \(S_n\) be the reproducing kernel of the closure of holomorphic polynomials in the resulting boundary \(L^2\) space (a positive overall normalization of the measure is immaterial). Then **\(S_n\) is everywhere nonzero on \(E_{n,2}\times E_{n,2}\) for \(2\le n\le10\), whereas \(S_{11}\) has zeros.** More precisely, after the scalar reduction below, the numerator for \(n=11\) has exactly two simple, nonreal conjugate roots inside the unit disk; for every \(2\le n\le10\) its numerator has no roots in the closed unit disk. The two roots for \(n=11\) are approximately \(0.539048877687875\pm0.817441544338130i\), of modulus approximately \(0.979175352502\).

This is the first dimension exhibiting a kernel zero **within the fixed quadratic-egg family**; no assertion is made for larger dimensions or other egg exponents.

## Assumptions and scope
Write \(k=n-1\), \(\mu_n=(n+2)/(2(n+1))\), \(u=\langle z,\zeta\rangle\), and
\[
 X=\frac{w\overline\eta}{(1-u)^{1/2}},
\]
where the analytic square-root branch is chosen by its value \(1\) at \(u=0\). For any \((z,w),(\zeta,\eta)\in E_{n,2}\), one has \(|X|<1\), since
\[
 |w\eta|^2 < \sqrt{(1-\|z\|^2)(1-\|\zeta\|^2)}\le |1-u|.
\]
Conversely, each \(X\) in the unit disk occurs with \(z=\zeta=0\) and suitably chosen \(w,\eta\) of modulus \(\sqrt{|X|}\). Thus scalar roots in \(|X|<1\) correspond exactly to kernel-zero fibres.

Set \((v)_k=v(v+1)\cdots(v+k-1)\), with \((v)_0=1\). Define
\[
 f_n(b)=(\mu_n+b/2)_{n-1},\qquad
 P_n(X)=\sum_{j=0}^{n-1}\Delta^j f_n(0)X^j(1-X)^{n-1-j},
\]
where \(\Delta f(b)=f(b+1)-f(b)\) and
\(\Delta^j f(0)=\sum_{i=0}^j(-1)^{j-i}\binom ji f(i)\).
All coefficients of \(P_n\) are rational and \(P_n(0)>0\).

## Proof
**1. Fefferman measure and monomial moments.** With defining function \(\rho(z,w)=\|z\|^2+|w|^4-1\), the Fefferman determinant is a positive constant times \(|w|^2\) on the boundary. Consequently, modulo a global positive factor, the boundary measure equals \(|w|^{2/(n+1)}d\sigma/|\nabla\rho|\). Integrating the squared modulus of \(z^\alpha w^b\) first over the \(2n-3\)-sphere in the \(z\) variables and then over \(r=|w|\) gives, with \(\alpha\in\mathbb N^{n-1}\),
\[
 \|z^\alpha w^b\|^2=C_n\,\alpha!\,
 \frac{\Gamma(\mu_n+b/2)}{\Gamma(\mu_n+b/2+n-1+|\alpha|)},
 \qquad C_n>0.
\]
Indeed, the radial integral is proportional to
\(\int_0^1 r^{2b+1+2/(n+1)}(1-r^4)^{n-2+|\alpha|}\,dr\), whose substitution \(s=r^4\) is a beta integral. Torus invariance makes the monomials orthogonal; their span is dense by the definition of the Hardy space.

**2. Exact kernel reduction.** Invert the monomial norms, sum over multiindices using the multinomial identity, and then sum over \(b\). This gives
\[
 S_n((z,w),(\zeta,\eta))=C'_n (1-u)^{-n+1-\mu_n}
 \sum_{b=0}^{\infty}(\mu_n+b/2)_{n-1}X^b,
 \qquad C'_n>0.
\]
The finite-difference identity for a polynomial sequence of degree \(n-1\) yields
\[
 \sum_{b\ge0}f_n(b)X^b=\frac{P_n(X)}{(1-X)^n},\qquad |X|<1.
\]
Both prefactors are nonzero there. Thus the asserted kernel-zero question is exactly the root question for \(P_n\).

**3. Rational Cohn/Rouché root-count certificate.** For any real polynomial \(p(X)=\sum_{j=0}^d c_jX^j\) with \(c_0=1\), \(c_d\ne0\), set \(q=c_d\), \(p^*(X)=X^dp(1/X)\). Whenever \(|q|\ne1\), its Cohn reduction is
\[
 R(p)(X)=\frac{p(X)-q p^*(X)}{1-q^2}.
\]
This has constant coefficient \(1\) and degree at most \(d-1\). Provided \(p\) has no unit-circle root, Rouché's theorem gives
\[
 N(p)=\begin{cases}N(R(p)),&|q|<1,\\d-N(R(p)),&|q|>1,\end{cases}
\]
where \(N\) counts zeros in the open unit disk with multiplicity. The second case follows because the reciprocal polynomial has \(d-N(p)\) such zeros. A unit-circle root of \(p\) would be common to \(p\) and \(p^*\), so their polynomial gcd being constant is a sufficient exact check excluding this case.

Starting from the exact rational coefficients of \(P_n/P_n(0)\), apply these reductions successively. The complete degree-by-degree sign certificates are as follows, where each \(<\) means \(|q|<1\), each \(>\) means \(|q|>1\), and the symbols run from original degree \(n-1\) down to degree \(1\):

| Dimension | Exact inequality pattern | Interior zero count |
| --- | --- | ---: |
| \(2\) | `<` | 0 |
| \(3\) | `<<` | 0 |
| \(4\) | `<<<` | 0 |
| \(5\) | `<<<<` | 0 |
| \(6\) | `<<<<<` | 0 |
| \(7\) | `<<<<<<` | 0 |
| \(8\) | `<<<<<<<` | 0 |
| \(9\) | `<<<<<<<<` | 0 |
| \(10\) | `<<<<<<<<<` | 0 |
| \(11\) | `<<<<<<><><` | 2 |

These are exact rational inequalities, not floating-point comparisons. For \(n=11\) the strict \(>\) steps occur at degrees \(4\) and \(2\). Backward counting gives \(N(P_{11})=2\). Polynomial Euclidean division gives \(\gcd(P_n,P_n^*)=1\) and \(\gcd(P_n,P_n')=1\) for all \(2\le n\le11\); hence the counted roots are not on the unit circle and are simple. The numerator \(P_{11}\) has strictly alternating coefficient signs; therefore \(P_{11}(x)>0\) for \(-1<x\le0\). For \(0<x<1\) its defining positive-coefficient series is strictly positive. Accordingly its two interior roots are nonreal and, by real coefficients, form a conjugate pair. The explicit root approximations above are only descriptive and are not used in the proof.

## Verification
The standalone file `CHECK.py` uses Python's exact rational arithmetic and implements the finite-difference polynomial and the Cohn reduction directly. Executing `python3 CHECK.py` checks 22 initial generating-series coefficients independently for every \(n\), computes each exact reflection coefficient, checks the polynomial gcds using rational Euclidean division, verifies the entire inequality pattern, and reconstructs the interior root counts. It prints `EXACT_CERTIFICATE_OK` if all tests pass. The scientific proof relies on the elementary exact identities and Rouché's theorem; no floating-point experiment is used to infer a general statement.

## Relationship to prior work
Pendyala, *Fefferman–Szegő kernels and finite-type rigidity on egg domains* (arXiv:2607.04100, publicly submitted July 5, 2026) derives Fefferman–Szegő kernels and curvature rigidity for the egg family. The present result takes that natural kernel family as its starting point but concerns the **first dimension with an interior off-diagonal kernel zero at the smallest nonlinear exponent**. The relevant published abstract and accessible mathematical synopsis describe a closed kernel numerator and geometric rigidity, not an exact disk-root cutoff or Cohn count. The complete primary text was not available for comparison, so equivalent treatment in that text remains a publication-priority risk rather than a verified absence.

Bhatnagar and Fan, *The invariant Szegő metric on Egg domains* (arXiv:2606.24452, June 23, 2026), treats the two-complex-dimensional egg family; that dimension lies on the zero-free side of the present statement. Szegő-kernel zeros on planar annuli (Gafai–Murid–Naqos–Wahid, 2023) concern a different domain and boundary measure. Lu Qi-Keng results for Bergman kernels or derivative-jet kernels do not imply the root counts for this Fefferman boundary Szegő kernel.

## Limitations
Only the fixed exponent \(m=2\) and dimensions \(2\le n\le11\) are classified. No result for \(n\ge12\) or for other exponents follows from the finite certificate. The location estimates are numerical approximations, not proof certificates. The root counts and simplicity are proven by exact rational calculations; independent scientific audit and historical publication-priority verification have not been performed. Full-text access to the most directly relevant general-egg preprint remained unavailable; it could contain unrecognized related results.

## References
1. V. S. Pendyala, *Fefferman–Szegő kernels and finite-type rigidity on egg domains*, arXiv:2607.04100, first posted 2026-07-05, https://arxiv.org/abs/2607.04100.
2. A. Bhatnagar and J. Fan, *The invariant Szegő metric on Egg domains*, arXiv:2606.24452, first posted 2026-06-23, https://arxiv.org/abs/2606.24452.
3. N. S. Gafai, A. H. M. Murid, S. Naqos and N. H. A. A. Wahid, *Computing the zeros of the Szegö kernel for doubly connected regions using conformal mapping*, AIMS Mathematics 8 (2023), 12040–12061, https://doi.org/10.3934/math.2023607.
4. A. Cohn, *Über die Anzahl der Wurzeln einer algebraischen Gleichung in einem Kreise*, Mathematische Zeitschrift 14 (1922), 110–148 (root-count reduction; an elementary derivation using Rouché is given above).
