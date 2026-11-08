# Exact logarithmic row counts for restricted binomial gcds

## Finding

For integers \(m\ge 2\) and \(q\ge2\), let
\[
G(mq;m)=\gcd\left\{\binom{mq}{mj}:1\le j<q\right\}.
\]
Fix a prime \(p\nmid m\), and write \(h=\operatorname{ord}_{m}(p)\) for the multiplicative order of \(p\) modulo \(m\). Let
\[
C_{m,p}(L)=\#\left\{q\ge2:mq<p^L,\ p\mid G(mq;m)\right\}
\qquad(L\in\mathbb Z_{\ge0}).
\]
**Theorem.** For all sufficiently large integers \(L\), \(C_{m,p}(L)\) is an exact rational-coefficient quasipolynomial of degree \(m\), with a period dividing \(h\). Its leading coefficient in every residue class is
\[
\boxed{\frac{1}{m!h^{m-1}}}.
\]
More explicitly, for each \(L\ge0\), let \(n_r(L)=\#\{0\le i<L:i\equiv r\pmod h\}\), and let \(\mathcal M\) be the finite set of matrices \(e=(e_{r,d})\) of nonnegative integers, \(0\le r<h\), \(1\le d<p\), for which the multiset with \(d e_{r,d}\) copies of \(p^r\bmod m\) is a nonempty minimal zero-sum sequence in \(\mathbb Z/m\mathbb Z\). Put \(E_r=\sum_d e_{r,d}\), and \((u)_{k}=u(u-1)\cdots(u-k+1)\) with \((u)_0=1\). Then the *exact*, finite formula is
\[
\boxed{C_{m,p}(L)=
\sum_{e\in\mathcal M}
\prod_{r=0}^{h-1}\frac{(n_r(L))_{E_r}}{\prod_{d=1}^{p-1}e_{r,d}!}
-\mathbf1_{\{p^L>m\}}.}
\]
Only matrices with \(1\le\sum_{r,d}d e_{r,d}\le m\) contribute, so the formula is genuinely finite and does not refer to a search over all rows. For real \(X\to\infty\), the count in the row multiplier variable satisfies
\[
\boxed{\#\{2\le q\le X:p\mid G(mq;m)\}
=\frac{(\log_p X)^m}{m!h^{m-1}}+O_{m,p}((\log X)^{m-1}).}
\]
In particular, positive valuation at any fixed prime is a polylogarithmically rare event; the exponent and exact leading coefficient are uniform across *all* primes coprime to the fixed index restriction.

**Concrete exact-period consequence.** At \((m,p)=(5,2)\), one has \(h=4\), and for sufficiently large \(L\equiv0\pmod4\) and \(L\equiv2\pmod4\), respectively, the corresponding branches are
\[
C_{5,2}(L)=\frac{L^5+40L^4+560L^3-640L^2+6144L-30720}{30720}\quad(L\equiv0\pmod4),
\]
\[
C_{5,2}(L)=\frac{L^5+40L^4+600L^3-640L^2+12944L-59520}{30720}\quad(L\equiv2\pmod4).
\]
Since these branches differ, a quasipolynomial period of \(2\) (or \(1\)) is impossible, so the least eventual quasipolynomial period in this example is **exactly \(4\)**. The explicit finite-profile formula yields these polynomial branches by a finite symbolic sum; alternatively six exact branch evaluations establish each identity because Step 4 proves the degree bound \(5\).

## Assumptions and scope

All integers are ordinary positive integers; \(m\ge2\), \(p\) is prime, and \(\gcd(m,p)=1\). The exact quasipolynomial statement concerns the geometrically growing cutoffs \(mq<p^L\), whereas the last formula concerns ordinary cutoffs \(q\le X\). The valuation event is \(\nu_p(G(mq;m))\ge1\), not maximal valuation. The theorem gives no valuation distribution for powers \(p^j\) with \(j\ge2\), and makes no statement for \(p\mid m\).

## Proof

**1. Lucas's theorem translates the gcd to a minimal zero sum.** Write the base-\(p\) expansion of \(N=mq\) as \(N=\sum_i a_i p^i\), \(0\le a_i<p\). Form a multiset \(W(N)\) containing \(a_i\) copies of \(p^i\pmod m\). Its sum is \(N\equiv0\pmod m\). Lucas's theorem gives \(p\nmid\binom Nk\) exactly when every base-\(p\) digit of \(k\) is at most the corresponding digit of \(N\). Thus there exists a selected proper index \(k=mj\), \(0<k<N\), with \(p\nmid\binom Nk\) exactly when \(W(N)\) contains a nonempty proper zero-sum submultiset. Consequently,
\[
 p\mid G(N;m)\quad\Longleftrightarrow\quad
 W(N)\text{ is a minimal zero-sum sequence in }\mathbb Z/m\mathbb Z.
\]
Here *minimal* means that the whole multiset sums to zero but no nonempty proper submultiset does. There is no assumption of distinct digits or distinct exponents.

**2. Length bound and rigidity at the maximum.** Any minimal zero-sum sequence in a cyclic group of order \(m\) has length at most \(m\): given \(m\) initial terms in a sequence of length greater than \(m\), either a prefix sum vanishes or two of their prefix sums coincide, producing a nonempty proper zero-sum subblock. Furthermore, a minimal zero-sum sequence \((w_1,\dots,w_m)\) of length *exactly* \(m\) consists of \(m\) copies of one additive generator. Indeed, for every ordering the \(m\) prefix sums before the final term are distinct (otherwise a proper consecutive block sums to zero), hence enumerate the group. Swapping any two adjacent terms changes only one of these prefix sums and must leave the enumerated set complete; therefore the terms exchanged are equal. This forces all \(w_i=w\); minimality forces \(w\) to have additive order \(m\).

**3. Finite profile formula.** Since \(p\) is a unit modulo \(m\), the residue \(p^i\pmod m\) depends only on \(i\pmod h\). A base-\(p\) digit \(d\) at an exponent in class \(r\) contributes \(d\) copies of \(p^r\pmod m\). For any admissible profile \(e\in\mathcal M\), the \(n_r(L)\) available positions of class \(r\) can receive digits with counts \(e_{r,1},\ldots,e_{r,p-1}\) in exactly
\[
\frac{(n_r(L))_{E_r}}{\prod_{d=1}^{p-1}e_{r,d}!}
\]
ways, interpreting this as zero when \(E_r>n_r(L)\). Multiplying over \(r\) and summing over all minimal-zero-sum profiles counts precisely the positive multiples \(N=mq<p^L\) whose selected gcd is divisible by \(p\), including the one nonadmissible multiplier \(q=1\) when \(m<p^L\). The digit sequence of \(N=m\) is always minimal zero sum (a proper digitwise subnumber lies strictly between \(0\) and \(m\), hence cannot be divisible by \(m\)). Subtracting that one excluded row proves the displayed exact formula.

**4. Quasipolynomial and leading coefficient.** Each matrix in \(\mathcal M\) has total token number \(\sum_{r,d}d e_{r,d}\le m\) by Step 2. Hence its total occupied positions \(\sum_{r,d}e_{r,d}\) also do not exceed \(m\), and each multinomial expression is a polynomial in the integer variables \(n_r(L)\) of total degree at most \(m\). On any fixed residue class of \(L\pmod h\), each \(n_r(L)\) is an affine function of \(L\), proving eventual quasipolynomiality of degree at most \(m\).

Degree \(m\) requires exactly \(m\) occupied positions, hence exactly \(m\) tokens, and every occupied digit is \(1\). By Step 2, the \(m\) residues \(p^{i}\pmod m\) must then coincide. This is equivalent to all \(m\) exponents belonging to a *single* class \(r\pmod h\), and every such choice is valid because \(p^r\) is an additive generator modulo \(m\). Their contribution is
\[
\sum_{r=0}^{h-1}\binom{n_r(L)}{m}=
\frac{L^m}{m!h^{m-1}}+O_{m,p}(L^{m-1}).
\]
Every other profile has at most \(m-1\) occupied positions, hence contributes \(O_{m,p}(L^{m-1})\). The subtracted exceptional multiplier is eventually constant. This proves the exact degree and leading coefficient.

**5. Arbitrary cutoffs.** For \(X\ge2\), sandwich the number of admissible multipliers \(q\le X\) between counts for neighboring powers of \(p\), with \(L=\lfloor\log_p(mX)\rfloor\). The logarithmic cutoff changes by at most a constant, and the exact quasipolynomial estimate shows that the difference between neighboring-power counts is \(O_{m,p}(L^{m-1})\). Replacing \(\log_p(mX)\) by \(\log_p X\) changes the main term by the same error. The asserted all-\(X\) asymptotic follows.

## Verification

The accompanying standalone `verify.py` independently tests Lucas digitwise divisibility against the minimal-zero-sum criterion for 11,866 parameter instances. It exhausts 763,424 zero-sum words of maximal possible length for small cyclic groups and checks the rigidity claim. It also compares the exact finite-profile formula with direct row enumeration for five nontrivial parameter pairs, including orders \(h=2,3,4\), for \(2\le L\le10\). The script uses exact integer arithmetic. Sample independent sparse counts for \((m,p)=(5,2)\) are \(C_{5,2}(8)=36\), \(C_{5,2}(12)=121\), \(C_{5,2}(16)=311\), \(C_{5,2}(20)=678\). These are checks, not a substitute for the argument above. Run `python3 verify.py` in the extracted package directory.

## Relationship to prior work

Fairfax-Ball (October 1, 2026) proves a sharp maximal \(p\)-adic valuation for the same restricted gcd family, with a least-extremal-row classification for \(m=p^a+1\); this theorem instead classifies the *frequency of any positive valuation* as the row multiplier varies. McTague (2015) proved a stronger rowwise divisibility criterion for \(p\equiv1\pmod m\); the \(h=1\) case of our count is therefore a counting consequence of that prior theorem and is not claimed as new. A 2026 paper on \(p\equiv-1\pmod m\) gives explicit valuations in the \(h=2\) family, so this part may also be recoverable by counting from prior work. Wu (2026) treats the index restriction when it is a prime power and gives further conditional gcd computations. The stated uniform order-\(h\) leading constant and eventual quasi-polynomial for unrestricted coprime \((m,p)\), especially \(h\ge3\), were not found in the inspected sources. Searches do not establish historical uniqueness.

## Limitations

The theorem concerns divisibility by one *fixed* prime as the multiplier grows, and does not estimate the gcd's typical number of distinct prime factors when the prime also varies. The degree \(m\) is fixed before taking \(X\) or \(L\) large, and the error term may depend on \(m,p\). Related unpublished or unindexed zero-sum counting observations remain a priority risk; the full text of the September 2026 minus-one specialization was unavailable during this review. No independent mathematical audit has been performed.

## References

- John Fairfax-Ball, *Sharp p-adic Extrema and Least Extremal Rows for Restricted Binomial GCDs*, arXiv:2610.01328v1, first posted 2026-10-01, https://arxiv.org/html/2610.01328v1.
- Carl McTague, *On the Greatest Common Divisor of Binomial Coefficients*, arXiv:1510.06696, first posted 2015-10-22, https://arxiv.org/abs/1510.06696.
- Chai Wah Wu, *Computing the Greatest Common Divisor of Binomial Coefficients*, arXiv:2606.20940, first posted 2026-06-18, https://arxiv.org/abs/2606.20940.
- John Fairfax-Ball, *Restricted Binomial GCDs at Primes Congruent to -1*, arXiv:2609.37754, posted 2026-09-29, https://arxiv.org/abs/2609.37754.
- Édouard Lucas, *Théorie des Fonctions Numériques Simplement Périodiques*, American Journal of Mathematics 1 (1878), the classical digitwise binomial congruence theorem.
