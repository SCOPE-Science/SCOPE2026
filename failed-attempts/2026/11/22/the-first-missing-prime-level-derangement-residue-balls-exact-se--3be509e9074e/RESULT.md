# The first missing prime-level derangement residue balls: exact seven-adic frequencies

## Finding

Let \(D_0=1\) and \(D_n=nD_{n-1}+(-1)^n\) for all integers \(n\ge1\); these are the classical derangement numbers. For every integer \(k\ge1\), set \(M=7^k\). Then, for **every** residue \(r\in\mathbb Z/M\mathbb Z\),
\[
\boxed{\#\{0\le n<2M:D_n\equiv r\pmod M\}=c_{r\bmod7},\qquad
(c_0,c_1,c_2,c_3,c_4,c_5,c_6)=(2,3,3,0,0,3,3).}
\]
In particular, exactly \(5\cdot7^{k-1}\) residues modulo \(7^k\) occur, precisely those congruent to \(0,1,2,5,6\pmod7\). Each such residue occurs with natural index density \(c_{r\bmod7}/(2\cdot7^k)\), and the closure of the derangement values in \(\mathbb Z_7\) has normalized Haar measure \(5/7\). The least index period modulo \(7^k\) is \(2\cdot7^k\); the general periodicity theorem is known and is not asserted as new.

Furthermore, seven is the **least prime with a missing derangement residue already at the first prime level**: the reductions of the derangement sequence are surjective modulo each of \(2,3,5\), whereas the residue classes \(3,4\pmod7\) never occur.

## Assumptions and scope

All indices are nonnegative integers. A residue frequency counts indices in a complete index period, not the number of distinct integer values. For any integer \(n\ge0\), \(D_n\) is the number of fixed-point-free permutations of an \(n\)-element set. The symbol \(\mathbb Z_7\) denotes the seven-adic integers and \(\nu_7\) the seven-adic valuation. The density statements are natural densities of index sets, not densities among numerical values of derangement numbers. All quantifiers in the theorem range over every positive integer \(k\) and every residue \(r\) modulo \(7^k\).

## Proof

**1. A seven-adic interpolation.** For each integer \(j\ge0\), define the falling-factorial polynomial
\[
P_0(X)=1,\qquad P_j(X)=\prod_{h=0}^{j-1}(X-h),\qquad
F(x)=\sum_{j\ge0}(-1)^jP_j(x),\quad x\in\mathbb Z_7.
\]
For every \(x\in\mathbb Z_7\), each block of seven consecutive factors contains a factor divisible by seven, so \(\nu_7(P_j(x))\ge\lfloor j/7\rfloor\). Hence the series converges uniformly; on each disc \(a+7\mathbb Z_7\), it converges as a restricted integral series in the local coordinate. The derivative series converges there as well, because differentiating each monomial removes at most one factor, and the remaining valuation bound tends to infinity with \(j\). Each integer polynomial is one-Lipschitz; uniform convergence implies that \(F\) is one-Lipschitz on \(\mathbb Z_7\). Consequently \(F(n)\bmod 7^k\) depends only on \(n\bmod7^k\). By inclusion–exclusion, the series terminates at an integer \(n\ge0\) and
\[
F(n)=(-1)^nD_n.
\]
The finite integer recurrence for derangements yields \(F(x+1)=1-(x+1)F(x)\) first at nonnegative integers and then at every \(x\in\mathbb Z_7\) by continuity and density. Therefore
\[
F'(x+1)=-F(x)-(x+1)F'(x).
\]

**2. The complete prime-level derivative certificate.** At zero, \(F(0)=1\), while direct differentiation of the falling factorials gives
\[
F'(0)=-\sum_{j\ge0}j!\equiv-874\equiv1\pmod7,
\]
because all factorials from \(7!\) onward vanish modulo seven. Applying the displayed two recurrences for \(a=0,1,\dots,5\) gives the exact table
\[
\begin{array}{c|rrrrrrr}
a\bmod7&0&1&2&3&4&5&6\\\hline
F(a)\bmod7&1&0&1&5&2&5&6\\
F'(a)\bmod7&1&5&4&1&5&1&3
\end{array}
\]
**Every local derivative is a seven-adic unit.** The table may also be obtained directly from the finite sums of \((-1)^jP_j(a)\) for \(0\le j<7\) and \((-1)^jP_j'(a)\) for \(0\le j<14\), since the omitted terms vanish modulo seven.

**3. Exact isometries and surjectivity on local balls.** Let \(a\in\{0,1,\dots,6\}\), and let \(x,y\in a+7\mathbb Z_7\), \(x\ne y\). The polynomial telescoping identity gives
\[
\frac{P_j(x)-P_j(y)}{x-y}
=\sum_{i=0}^{j-1}\left(\prod_{h<i}(x-h)\right)
 \left(\prod_{h>i}(y-h)\right).
\]
For \(j\ge14\), there are at least two indices \(h\) congruent to \(a\pmod7\) among the factors, so deleting at most one index leaves a factor divisible by seven in every summand. The quotient series converges by the same valuation argument as in Step 1. For \(j<14\), reduction modulo seven sends both \(x,y\) to \(a\); the quotient reduces to \(P_j'(a)\). Thus
\[
\frac{F(x)-F(y)}{x-y}\equiv F'(a)\not\equiv0\pmod7.
\]
Therefore the restriction of \(F\) to each disc is an exact isometry:
\[
\nu_7(F(x)-F(y))=\nu_7(x-y).
\]
It is also onto the full disc \(F(a)+7\mathbb Z_7\). Indeed, suppose \(x_h\equiv a\pmod7\) has been chosen so that \(F(x_h)\) matches a prescribed target modulo \(7^h\). The seven lifts \(x_h+t7^h\) satisfy
\[
F(x_h+t7^h)\equiv F(x_h)+t7^h F'(a)\pmod{7^{h+1}};
\]
since \(F'(a)\) is invertible modulo seven, exactly one lift matches the target modulo \(7^{h+1}\). The compatible sequence converges to a unique preimage. Thus for every \(k\ge1\), each of the seven input residue discs maps bijectively, modulo \(7^k\), to a complete output residue disc.

**4. Exact fibers of derangements.** The value row of the table shows that the multiplicities for \(F(x)\equiv r\pmod{7^k}\), as a function of \(r\bmod7\), are
\[
(m_0,m_1,m_2,m_3,m_4,m_5,m_6)=(1,2,1,0,0,2,1).
\]
Since \(7^k\) is odd, in \(0\le n<2\cdot7^k\) every input class \(n\bmod7^k\) occurs exactly once at an even index and exactly once at an odd index. On the even indices \(D_n=F(n)\), and on the odd indices \(D_n=-F(n)\). The number of indices with \(D_n\equiv r\) is therefore \(m_r+m_{-r}\), which gives the stated seven-entry frequency table. The missing classes are exactly \(3,4\pmod7\); the supported classes form the five entire residue balls. The finite index period gives the densities and cardinalities immediately; each supported ball has Haar measure \(1/7\), proving the closure measure \(5/7\).

**5. Least period and minimal prime.** The interpolation gives period \(2\cdot7^k\). Modulo seven, this is the least period: its only proper positive divisors are \(1,2,7\), excluded respectively by comparing \(D_0\) with \(D_1\), \(D_1\) with \(D_3\), and \(D_0\) with \(D_7\). Any period modulo \(7^k\) must therefore be even and divisible by seven. If such a period \(T\) is not divisible by \(7^k\), the equality \(D_T\equiv D_0\pmod{7^k}\) would imply \(F(T)\equiv F(0)\pmod{7^k}\), contradicting the local isometry on \(7\mathbb Z_7\). Hence the least period is \(2\cdot7^k\). This is also a specialization of known general results. Finally, direct recurrence modulo \(2,3,5\) gives every residue class at each of these smaller primes, while the seven-adic table proves the omission modulo seven. The least-prime statement follows.

## Verification

Run `python3 verify.py` with the Python 3 standard library. The independent finite checker evaluates all seven local values and derivatives from integer falling-factorial polynomials, counts every residue over a full period for \(k=1,2,3,4,5\), checks proper-divisor period obstructions for the first four exponents, and compares the smaller primes directly. It finishes with

```text
VERIFY_OK exact_assertions=19665 exponents=1..5 max_modulus=16807 local_table=7
```

These finite computations corroborate the proof, but the universal conclusions for all exponents follow from the derivative certificate, isometry, lifting argument, and parity splitting, not from extrapolation.

## Relationship to prior work

Miska (2015) established general modular periods for derangements, developed prime-adic interpolation and zero/valuation criteria (including the prime seven). O'Desky and Richman (2020) developed broader prime-adic derangement interpolation and incomplete-gamma methods. Those results explain the analytic framework; they do not by themselves provide the evaluated seven-entry image and index-frequency table at all seven-power levels. Previously published complete frequency results at the prime five show a full five-adic image, rather than this first prime-level failure of surjectivity. Earlier work at the prime three determines a different, quadratic critical-image phenomenon. The present contribution is the **evaluated first omitted prime-level spectrum** and its exact all-power multiplicity law, not the general interpolation technique or period theorem.

## Limitations

The classification covers the classical derangement sequence only at the prime seven. It does not determine every possible prime's residue-frequency spectrum, or numerical-size densities of the derangement values. The proof method shares its general framework with established prime-adic interpolation and with known frequency results at smaller primes. Complete historical publication priority is not certified, and independent mathematical validation has not been performed.

## References

- Piotr Miska, *Arithmetic Properties of the Sequence of Derangements and its Generalizations*, arXiv:1508.01987, first public version 2015-08-09, https://arxiv.org/abs/1508.01987.
- Andrew O'Desky and David Harry Richman, *Derangements and the p-adic incomplete gamma function*, arXiv:2012.04615, first public version 2020-12-08, https://arxiv.org/abs/2012.04615.
- Zhi-Wei Sun and Don Zagier, *On a curious property of Bell numbers*, arXiv:1008.1573, first public version 2010-08-09, https://arxiv.org/abs/1008.1573.
- Zhi-Wei Sun, Xiaojuan Wu, and Jujuan Zhuang, *Congruences on the Bell polynomials and the derangement polynomials*, arXiv:1009.2929, first public version 2010-09-15, https://arxiv.org/abs/1009.2929.
- *The exact five-adic residue frequencies of derangement numbers*, published indexed result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-exact-five-adic-residue-frequencies-of-derangement-numbers--63bd728ea23f.
- *Exact ternary residue-image spectrum of the derangement numbers*, published indexed result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-ternary-residue-image-spectrum-of-the-derangement-numbers--6836cc8a259d.
