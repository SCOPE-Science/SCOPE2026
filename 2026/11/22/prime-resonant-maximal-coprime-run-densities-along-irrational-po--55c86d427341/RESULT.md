# Prime-resonant maximal coprime-run densities along irrational polynomial floors

## Finding

**Theorem (universal maximal-run law and two-scale prime resonance).** Let \(f\in\mathbb R[X]\) have degree at least two and at least one irrational nonconstant coefficient. For integers \(n\ge1\), put \(t_n=\lfloor f(n)\rfloor\). For each fixed integer \(r\ge1\), let \(E_r\) be the set of positive integers \(n\) for which
\[
\gcd(n,t_n-1)>1,\qquad
\gcd(n,t_n+j)=1\quad(0\le j<r),\qquad
\gcd(n,t_n+r)>1.
\]
Thus the consecutive integers \(t_n,t_n+1,\ldots,t_n+r-1\) form a maximal run of integers coprime to \(n\), with both adjacent integers noncoprime. The natural density \(\delta_r=\operatorname{dens}(E_r)\) exists, is strictly positive, is independent of \(f\), and is given *exactly* by
\[
\boxed{\delta_r=C_r-2C_{r+1}+C_{r+2},\qquad
C_r=\prod_{p\ \mathrm{prime}}
\left(1-\frac{\min\{p,r\}}{p^2}\right).}
\tag{1}
\]
In particular the complete maximal-run length distribution is explicit for every finite \(r\). Its large-length behavior has two distinct asymptotic scales:
\[
\boxed{\begin{aligned}
\delta_{p-1}&\sim\frac{e^{-\gamma}}{p^2\log p}
&&\text{as primes }p\to\infty,\\
\delta_r&\sim\frac{e^{-\gamma}}{r^2(\log r)^3}
&&\text{as }r\to\infty\text{ through integers with }r+1\text{ composite}.
\end{aligned}}
\tag{2}
\]
Here \(\gamma\) is the Euler–Mascheroni constant, and the limits in \(n\) defining each density precede the large-\(r\) limits. Hence lengths one less than a prime are asymptotically enhanced by two powers of \(\log r\) relative to their composite-successor neighbors.

## Assumptions and scope

Every \(r\) is fixed while taking the natural-density limit over \(n\); formula (2) concerns the resulting real sequence \((\delta_r)\). No uniform error estimate in the two parameters \(n,r\) is claimed. Integer parts may be negative, and \(\gcd(n,z)\) denotes the nonnegative greatest common divisor; the finitely many small indices and the exceptional modulus \(n=1\) have no effect on natural density. Formula (1) uses ordinary rational primes. The theorem is stated for degree at least two to invoke the large-prime estimate of Holdridge directly; a separate, previously available linear estimate could be used for an analogous extension to degree one, but that extension is not part of the claim.

## Proof

**1. Every fixed coprime block has the Euler-product density.** For integers \(k\ge1\), set
\[
B_k=\{n\ge1:\gcd(n,t_n+j)=1\text{ for all }0\le j<k\}.
\]
Fix a squarefree modulus \(D\). Because \(f\) has an irrational nonconstant coefficient, for every residue \(u\pmod D\) the polynomial \(f(Dm+u)/D\) has an irrational nonconstant coefficient. By Weyl equidistribution, its fractional parts are uniform in \([0,1)\). Consequently the pair
\[
(n\bmod D,\,\lfloor f(n)\rfloor\bmod D)
\]
occupies each of the \(D^2\) pairs of residues with natural density \(1/D^2\). The exact floor-residue criterion is \(\lfloor f(n)\rfloor\equiv v\pmod D\) if and only if \(\{f(n)/D\}\in[v/D,(v+1)/D)\).

For a prime \(p\), an inner block of length \(k\) fails the prime-\(p\) condition precisely when \(p\mid n\) and \(t_n\equiv-j\pmod p\) for some \(0\le j<k\). Exactly \(\min\{p,k\}\) distinct residues occur among these \(-j\pmod p\). Therefore the proportion of good residue pairs modulo \(p\) is
\[
1-\frac{\min\{p,k\}}{p^2}.
\]
The Chinese remainder theorem gives the product of these factors for any fixed finite set of primes. To pass to all primes, the error is at most the union over \(j=0,\ldots,k-1\) of the events \(p\mid n\) and \(p\mid\lfloor f(n)+j\rfloor\) for some prime \(p>R\). Each polynomial \(f+j\) has the same irrational nonconstant coefficient. Holdridge's Theorem 1.3 (arXiv:2611.02223v1) shows that this finite union has upper density tending to zero as \(R\to\infty\). Hence \(\operatorname{dens}(B_k)=C_k\) for every fixed \(k\). The product is positive because its factors are positive and its tail differs from one by a summable series \(\sum_{p>k}k/p^2\).

**2. Exactly maximal runs.** The defining indicator for \(E_r\) equals
\[
\bigl(1-\mathbf1_{\{\gcd(n,t_n-1)=1\}}\bigr)
\left(\prod_{j=0}^{r-1}\mathbf1_{\{\gcd(n,t_n+j)=1\}}\right)
\bigl(1-\mathbf1_{\{\gcd(n,t_n+r)=1\}}\bigr).
\]
Expand the two boundary factors. The first term has density \(C_r\). Either of the two single-boundary additions gives the same \(C_{r+1}\), since adding an integer constant to \(f\) preserves the hypotheses and translates the index interval. Including both boundaries gives \(C_{r+2}\). Their alternating sum is exactly (1), not a heuristic assumption of independence between neighboring coprimality events.

**3. Strictly positive density at every length.** Choose two distinct primes \(P,Q>r+1\). Impose \(P\mid n\), \(t_n\equiv1\pmod P\), \(Q\mid n\), and \(t_n\equiv-r\pmod Q\). Then \(P\mid(t_n-1)\) and \(Q\mid(t_n+r)\), but neither prime divides any of the \(r\) interior shifts. At every other prime \(\ell\), require the ordinary interior block to be coprime. The finite-prime density of these conditions is the product of two factors \(1/P^2,1/Q^2\) and all the positive interior factors \(1-\min\{\ell,r\}/\ell^2\) for \(\ell\notin\{P,Q\}\). The same large-prime estimate as in step 1 proves that their limiting density equals this strictly positive convergent product. These conditions imply membership in \(E_r\), proving \(\delta_r>0\) for all \(r\).

**4. The sharp prime-resonance asymptotics.** Set \(Q_r=C_{r+1}/C_r\). Direct comparison of the Euler factors, including the case \(p=r+1\), gives
\[
Q_r=\prod_{p>r}\left(1-\frac1{p^2-r}\right),\qquad
\frac{\delta_r}{C_r}
=(1-Q_r)^2+Q_r(Q_{r+1}-Q_r).
\tag{3}
\]
By Mertens' product theorem and the prime number theorem with partial summation,
\[
\prod_{p\le r}\left(1-\frac1p\right)
\sim\frac{e^{-\gamma}}{\log r},\qquad
\sum_{p>r}\frac1{p^2}\sim\frac1{r\log r},\qquad
\sum_{p>r}\frac1{p^4}=O(r^{-3}).
\]
It follows from \(\log(1-x)=-x+O(x^2)\) that
\[
C_r\sim\frac{e^{-\gamma}}{\log r},
\qquad 1-Q_r\sim\frac1{r\log r}.
\tag{4}
\]
Indeed the tail of \(C_r\) contributes \(\exp(O(r\sum_{p>r}p^{-2}))=1+o(1)\), while the sum of the local logarithmic errors for \(Q_r\) is \(O(\sum_{p>r}p^{-4})\).

When \(r+1\) is composite, the sets of primes in \(Q_r\) and \(Q_{r+1}\) coincide. Termwise comparison gives \(Q_{r+1}-Q_r=O(\sum_{p>r}p^{-4})=O(r^{-3})\), which is \(o((1-Q_r)^2)\). Equations (3)–(4) yield the second branch of (2).

When \(r+1=p\) is prime, exactly the factor belonging to \(p\) disappears between \(Q_r\) and \(Q_{r+1}\). All other factor changes total \(O(r^{-3})\). The missing factor contributes
\[
Q_{r+1}-Q_r
=\frac{1+o(1)}{p^2-r}+O(r^{-3})
\sim\frac1{p^2}.
\]
This dominates \((1-Q_r)^2\sim1/(r^2\log^2r)\). Equations (3)–(4) therefore give \(\delta_{p-1}\sim e^{-\gamma}/(p^2\log p)\), the first branch of (2).

## Verification

The self-contained Python script `verify_prime_resonance.py` checks the local formula by direct residue-pair enumeration at every prime through nineteen and block lengths through twelve; checks exact Chinese-remainder block and maximal-run counts over both residue coordinates at moduli \(6,30,210\); checks positivity of finite-prime approximations through length twenty-four; and directly enumerates the deterministic polynomial \(f(X)=\sqrt2 X^2\) for \(n\le100000\) using the exact identity \(\lfloor\sqrt2 n^2\rfloor=\lfloor\sqrt{2n^4}\rfloor\) implemented by integer square roots. It passed 166 finite checks. Numerical examples of maximal-run densities are \(\delta_3\approx0.001664\) and \(\delta_4\approx0.011283\), showing a visible jump when \(r+1\) changes from composite four to prime five. Finite checks confirm arithmetic and numerical consistency; they neither establish infinite natural density nor prove prime-number-theorem asymptotics.

## Relationship to prior work

Holdridge, *On the probability that the integer parts of polynomials are coprime* (arXiv:2611.02223v1, first public November 1, 2026), proves the two-coordinate coprimality density and the necessary large-prime estimate. This supplies the substantive analytic input to step 1. It does not state densities of *consecutive shifts of a floor polynomial* or the prime/composite resonance in their maximal-run lengths.

The published result *Coprimality densities for split integer polynomials and equidistributed integer parts* gives, for a product of distinct shifts of \(n\) coprime to a floor-polynomial coordinate, an Euler product with the **same local factors** as \(C_r\). This is an important numerical/CRT equivalence of block densities, not a claim that the one-point Euler-product sequence is new. Its underlying event is \(\gcd(\prod_{h\in H}(n+h),\lfloor f(n)\rfloor)=1\), different from \(\gcd(n,\prod_{j=0}^{r-1}(\lfloor f(n)\rfloor+j))=1\). The present result uses the recent large-prime theorem for the latter event and adds the exact positive maximal-run distribution and the analytically sharp dichotomy (2). The old Euler product alone does not state (2).

The published results *Exact higher-order correlations and maximal runs of regular residues* and *Exact cyclic run-length spectrum of square-gcd totatives* employ second differences of finite-modulus correlation counts for different residue predicates. Their second-difference technique is classical and not claimed as novel. Neither establishes the varying-modulus, irrational-polynomial-floor density nor the prime-resonant asymptotics. Sanna and Szikszai (2017) study consecutive **arguments** of fixed integer polynomials and pairwise relations among their values, not this fixed-modulus run of shifts of a floor value. Mertens' theorem and the prime number theorem supply classical analytic ingredients; no originality is claimed for them separately.

## Limitations

The polynomial must have an irrational nonconstant coefficient and degree at least two. The statement gives asymptotics in the run length after taking a natural-density limit; it supplies no error bound when \(r\) grows together with the sampling parameter \(n\). The proof relies on Holdridge's published large-prime result, not an independent reconstruction of its long analytic proof. No novelty is claimed for the simple finite-prime local factor, standard second-difference identity, or Mertens' formula. Equivalent asymptotic statements might exist in older work on generalized Schemmel/Jacobsthal totients under a different formulation; the inspected records did not reveal one. Independent proof and bibliographic review have not been performed.

## References

1. Philippa Holdridge, *On the probability that the integer parts of polynomials are coprime*, arXiv:2611.02223v1 (first submitted 2026-11-01), https://arxiv.org/abs/2611.02223; Theorems 1.2–1.3, Section 6.
2. *Coprimality densities for split integer polynomials and equidistributed integer parts*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-coprimality-densities-for-split-integer-polynomials-and-equidist--bcbc904e31ef/RESULT.md; complete theorem/proof inspected.
3. *Exact higher-order correlations and maximal runs of regular residues*, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-higher-order-correlations-and-maximal-runs-of-regular-resi--ff65dda93828/RESULT.md; exact fixed-modulus comparator.
4. *Exact cyclic run-length spectrum of square-gcd totatives*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-cyclic-run-length-spectrum-of-square-gcd-totatives--f1ff76c679ca/RESULT.md; second-difference comparator.
5. Carlo Sanna and Márton Szikszai, *A coprimality condition on consecutive values of polynomials*, arXiv:1704.01738v1 (2017), https://arxiv.org/html/1704.01738v1.
6. Classical Mertens product theorem and the prime number theorem with partial summation (standard analytic-number-theory inputs).
