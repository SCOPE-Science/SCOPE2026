# Every five-adic unit is a central trinomial residue

## Finding

Let \(T_n=[x^0](1+x+x^{-1})^n\) denote the central trinomial coefficient, for all integers \(n\ge0\). Then for every integer \(k\ge1\) and every residue \(u\) not divisible by five modulo \(5^k\), there are **infinitely many** indices \(n\ge0\) with \(T_n\equiv u\pmod{5^k}\). Conversely, \(5\nmid T_n\) for every \(n\). Thus the exact five-adic value closure is

\[
\overline{\{T_n:n\ge0\}}^{(5)}=\mathbb Z_5^{\times}.
\]

## Assumptions and scope

All indices are nonnegative integers; the prime is exactly five. \(\mathbb Z_5\) is the ring of five-adic integers. Every congruence between Laurent polynomials is coefficientwise. We use the published dilation theorem of Pan--Sun: for every prime \(p>3\) and every positive integer \(n\), the difference \(T_{pn}-T_n\) is divisible by \((pn)^2\) in \(\mathbb Z_p\). For \(p=5\), this is \(\nu_5(T_{5n}-T_n)\ge2+2\nu_5(n)\). The original source of the central-trinomial problem is Sun's 2010 preprint; the 2020 preprint on dilation is a later supporting result, not the dating source.

## Proof

**1. Nonvanishing.** Put \(F(x)=1+x+x^{-1}\). Write \(n=\sum_{i\ge0}d_i5^i\), \(0\le d_i\le4\). Frobenius gives \(F(x)^n\equiv\prod_i F(x^{5^i})^{d_i}\pmod5\). In the product, an exponent sum \(\sum_i e_i5^i\) with \(\lvert e_i\rvert\le d_i\le4\) can vanish only if every \(e_i=0\): reduce modulo five, divide by five, and repeat. Therefore

\[
T_n\equiv\prod_i T_{d_i}\pmod5.
\]

The five initial coefficients are \(T_0,T_1,T_2,T_3,T_4=1,1,3,7,19\). Their residues \(1,1,3,2,4\) are units; thus no \(T_n\) vanishes modulo five.

**2. Dilation limits.** Fix a positive integer \(b\). The published dilation congruence quoted above gives \(\nu_5(T_{5^{r+1}b}-T_{5^rb})\ge2r+2+2\nu_5(b)\), so the limit

\[
U_b:=\lim_{r\to\infty}T_{5^rb}\in\mathbb Z_5^\times
\]

exists and satisfies \(U_b\equiv T_b\pmod{25}\). In particular, \(U_2\equiv T_2=3\pmod{25}\).

**3. Separated-support multiplication.** For all nonnegative integers \(a,b\), all \(k\ge1\), and every integer \(r\ge k-1\) such that \(5^{r-k+1}>a\), the elementary Frobenius lifting identity is

\[
F(x)^{5^rb}\equiv F(x^{5^{r-k+1}})^{5^{k-1}b}\pmod{5^k}.
\]

To justify it, for any integral Laurent polynomial \(G\), start with \(G(x)^5\equiv G(x^5)\pmod5\). If integral Laurent polynomials \(A\equiv B\pmod5\), then \(A^{5^s}\equiv B^{5^s}\pmod{5^{s+1}}\), by expanding the binomial. Iterate this identity \(r-k+1\) times, beginning at \(F^{5^rb}\). Every nonconstant monomial on the right has exponent a nonzero multiple of \(5^{r-k+1}\); every monomial of \(F(x)^a\) has exponent of magnitude at most \(a\). Hence the constant term of their product equals the product of their separate constant terms. Taking constant terms gives

\[
T_{a+5^rb}\equiv T_aT_{5^{k-1}b}\equiv T_aT_{5^rb}\pmod{5^k}.
\]

The second congruence follows from the same Laurent polynomial identity after taking constant terms.

**4. Powers appear in the closure.** Fix \(k,m\ge1\). Choose positive integers \(r_1<\cdots<r_m\) successively so large that every \(T_{2\cdot5^{r_i}}\equiv U_2\pmod{5^k}\) and for each \(i\ge2\) the separation condition in step 3 holds with \(a=2\sum_{j<i}5^{r_j}\), \(b=2\), \(r=r_i\). Iterating step 3 yields

\[
T_{2\sum_{i=1}^{m}5^{r_i}}\equiv U_2^m\pmod{5^k}.
\]

Every choice may be made with arbitrarily large final exponent; there are therefore infinitely many realizing indices for each fixed \(k,m\).

**5. Generation of units.** The residue \(3\pmod{25}\) has multiplicative order twenty: \(3^4\equiv6\not\equiv1\pmod{25}\), while its order modulo five is four. By the standard binomial lifting identity, every element congruent to three modulo twenty-five has order \(4\cdot5^{k-1}\) modulo \(5^k\). In detail, \(\nu_5(U_2^{4\cdot5^s}-1)=1+s\) by lifting the exponent. Thus \(U_2\) generates all units modulo \(5^k\). For any unit target \(u\), choose a positive integer \(m\) with \(U_2^m\equiv u\pmod{5^k}\), and apply step 4. This establishes existence, infinite recurrence, and the asserted closure.

## Verification

The supplementary self-contained Python checker uses exact integers. It verifies the first six hundred coefficients against their recurrence, every unit residue modulo five, twenty-five and one hundred twenty-five, the predicted nonvanishing and digit law, the stated dilation congruence for bounded positive inputs, primitive-root orders, and valid separated-support congruences for bounded parameters. Finite checks are corroborative; the proof above covers every index and every modulus. Run `python3 check_central_trinomial.py`.

## Relationship to prior work

Sun, *Congruences involving generalized central trinomial coefficients*, arXiv:1008.3887, first posted 2010-08-23, introduced extensive congruence study of this natural sequence. Pan and Sun, *Supercongruences for central trinomial coefficients*, arXiv:2012.05121, first posted in 2020, prove the dilation congruence invoked in step 2; their Theorem 1.1 is a necessary premise but does not state or imply the full five-adic image alone. A separate published dyadic result classifies all odd values modulo powers of two, not this five-adic case; published modulo-five pair correlations classify a different statistic. The new combination of infinitely separated blocks and the primitive five-adic limit upgrades digitwise modulo-five information to the full inverse-limit image.

## Limitations

The theorem asserts topological density and infinitely many occurrences of each residue; it does not quantify natural frequencies or provide optimal bounds for the first witness. A published equivalent statement may exist under different terminology; the full historical bibliography is not certified. The proof uses the independently published Pan--Sun dilation theorem as an explicitly stated external premise. Computational evidence cannot replace that theorem or the infinite block construction.

## References

1. Z.-W. Sun, *Congruences involving generalized central trinomial coefficients*, arXiv:1008.3887, first public version 2010-08-23, https://arxiv.org/abs/1008.3887.
2. H. Pan and Z.-W. Sun, *Supercongruences for central trinomial coefficients*, arXiv:2012.05121, first posted 2020-12-09, https://arxiv.org/abs/2012.05121, Theorem 1.1.
3. *The On-Line Encyclopedia of Integer Sequences*, A002426, https://oeis.org/A002426 (index of the sequence).
