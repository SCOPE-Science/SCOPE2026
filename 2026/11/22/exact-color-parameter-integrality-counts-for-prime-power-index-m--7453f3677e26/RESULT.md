# Exact color-parameter integrality counts for prime-power-index multinomial Catalan quotients

## Finding

For each prime \(p\), integer \(r\ge1\), and integer \(l\ge1\), set \(m=p^r-1\), \(L=l+1\) and
\[
Q_l(m)=\frac{((l+1)m)!}{(m!)^{l+1}(m+1)^l}.
\]
Write the base-\(p\) expansion of \(mL\) as \(\sum_{j\ge0}d_jp^j\), with \(0\le d_j<p\). Define column sums
\[
A_i=\sum_{j\equiv i\pmod r}d_j\qquad(0\le i<r).
\]
Then the following conditions are equivalent:

1. \(Q_l(m)\) is an integer.
2. \(\sum_jd_j=r(p-1)\).
3. \(A_0=\cdots=A_{r-1}=p-1\).

In every integral case, \(\nu_p(Q_l(m))=0\). In particular, the complete, infinite spectrum of integral color parameters is described by finite digit-column equalities, not just a sufficient condition.

For every \(H=qr+t\) with integers \(q\ge1\) and \(0\le t<r\), the exact number of integral parameters satisfying \((l+1)m<p^H\) is
\[
\boxed{\binom{q+p-1}{p-1}^{t}\binom{q+p-2}{p-1}^{r-t}-1.}
\]
For fixed \(p,r\), with \(w=r(p-1)\), this yields
\[
\#\{1\le l\le X:Q_l(m)\in\mathbb Z\}
=\frac{(\log_p X)^w}{r^w((p-1)!)^r}
+O_{p,r}((1+\log X)^{w-1})
\]
as \(X\to\infty\). Thus the integrality parameters have natural density zero, but have exact positive polylogarithmic growth. For \(r=1\), the leading term is \((\log_p X)^{p-1}/(p-1)!\).

## Assumptions and scope

All quantifiers include \(p=2\), \(r=1\), and \(l=1\). The index \(m=p^r-1\) is fixed when the color parameter \(l\) varies. The quotient is a positive rational number. The claimed integer test relies only on the prime \(p\), since \(m+1=p^r\) is the entire denominator contribution outside the ordinary multinomial coefficient. Other indices \(m\) are not classified by this result.

## Proof

**Step 1: exact valuation.** Let \(s_p(k)\) denote the sum of the base-\(p\) digits of \(k\). Legendre's formula gives \(\nu_p(k!)=(k-s_p(k))/(p-1)\). Since \(s_p(p^r-1)=r(p-1)\), the definition yields
\[
\begin{aligned}
\nu_p(Q_l(m))
&=\nu_p((mL)!)-L\nu_p(m!)-(L-1)r\\
&=r-\frac{s_p(mL)}{p-1}.
\end{aligned}
\]
No other prime can divide the reduced denominator, because \(((mL)!/(m!)^L)\) is an integer and \((m+1)^{L-1}\) is a power of \(p\).

**Step 2: a sharp digit-weight lemma.** Take an arbitrary positive multiple \(K\) of \(m=p^r-1\). From its base-\(p\) digits form \(A_i=\sum_{j\equiv i\pmod r}d_j\). Modulo \(m\) we have \(\sum_{i=0}^{r-1}A_ip^i\equiv K\equiv0\). Whenever some \(A_i\ge p\), perform a cyclic carry: subtract \(p\) from \(A_i\) and add \(1\) to \(A_{i+1}\), with subscripts modulo \(r\). This preserves the weighted sum modulo \(m\) and decreases the sum of coordinates by exactly \(p-1\). Thus it terminates at a vector \(B\) with all coordinates between \(0\) and \(p-1\). Its ordinary weighted value lies in \([0,m]\) and is divisible by \(m\), so it is either \(0\) or \(m\). The zero vector cannot be reached from a nonzero vector: the final carry before reaching zero would have coordinate sum \(p-1\), but executing a carry requires at least \(p\) in one coordinate. Consequently \(B=(p-1,\ldots,p-1)\). It follows that \(s_p(K)=\sum_iA_i\ge r(p-1)\), with equality precisely when no carry was made, or equivalently when each original \(A_i=p-1\).

Combining Steps 1 and 2 proves the three equivalences and the unit assertion.

**Step 3: exact counting.** Let \(H\ge r\), and write \(H=qr+t\) with \(q\ge1\) and \(0\le t<r\). Exactly \(t\) residue classes \(i\pmod r\) contain \(q+1\) positions among \(0,\ldots,H-1\); the other \(r-t\) contain \(q\) positions. For a class containing \(h\ge1\) positions, the number of choices of its digits with sum exactly \(p-1\) is \(\binom{h+p-2}{p-1}\): stars and bars applies because no digit can exceed \(p-1\) when the total is \(p-1\). Choosing digits independently among the classes gives
\[
\binom{q+p-1}{p-1}^t\binom{q+p-2}{p-1}^{r-t}
\]
positive integers \(K<p^H\) with every column sum \(p-1\). Each is divisible by \(m\) since \(p^r\equiv1\pmod m\), so each is uniquely \(K=mL\) with \(L\ge1\). The one case \(L=1\) corresponds to \(l=0\) and is excluded, yielding the displayed formula.

**Step 4: asymptotics for arbitrary cutoffs.** For each \(H\), the exact formula is a degree-\(w\) quasipolynomial in \(H\) with leading coefficient \(1/(r^w((p-1)!)^r)\), and an error of order \(H^{w-1}\). Replacing the threshold \(mL<p^H\) by \(l\le X\) changes the associated digit length by at most a bounded amount. Monotonicity and the fact that the difference of consecutive degree-\(w\) counting polynomials is of order \(H^{w-1}\) give the stated asymptotic with the stated error.

## Verification

The self-contained Python program `multicatalan_checker.py` recomputes \(p\)-adic factorial valuations using repeated integer divisions, checks the independent base-\(p\) digit-column test, and directly counts every permitted \(L\) below the specified digit bounds. Ten complete finite ranges with \(p\in\{2,3,5,7\}\), \(1\le r\le4\), and bounds up to \(2^{13}\), \(3^9\), \(5^6\), and \(7^5\) all passed. These finite tests supplement rather than replace the proof for arbitrary \(p,r,l\).

## Relationship to prior work

Cera Da Conceição (2023) introduced the multinomial Catalan numbers and proved that for fixed \(l\), failures of integrality occur only at finitely many indices \(n=p^r-1\), with a necessary restriction on the digits of \(l+1\) (Theorem 10). The present result fixes one of those potentially exceptional indices instead, gives a necessary **and sufficient** digit-column criterion for every \(l\), and counts the admissible color parameters exactly at all prime-power digit cutoffs. Its exponent and leading constant describe a different asymptotic question from the cited fixed-color theorem. Classical Legendre digit-sum valuations and cyclic carrying are used explicitly, not claimed as new techniques.

## Limitations

The classification is specific to ordinary multinomial Catalan quotients at indices one below a prime power. It does not extend to Lucasnomial quotients or classify arbitrary indices. Novelty is conditional on the inspected primary literature and indexed searches; an equivalent unindexed parameter-spectrum formula cannot be excluded. No independent mathematical review is claimed.

## References

1. J. Cera Da Conceição, *Multinomial Catalan Numbers and Lucas Analogues*, Journal of Integer Sequences **26** (2023), Article 23.9.7, https://cs.uwaterloo.ca/journals/JIS/VOL26/Cera/cera4.pdf. See Theorems 1, 8 and 10 and the introductory definition.
2. A.-M. Legendre's classical factorial-valuation identity, recalled in the preceding article and derived from the base-\(p\) expansion.
