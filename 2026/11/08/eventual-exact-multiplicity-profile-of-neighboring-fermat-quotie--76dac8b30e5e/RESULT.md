# Eventual exact multiplicity profile of neighboring Fermat quotients

## Finding

Fix an odd prime \(p\) and a nonzero integer \(h\) with \(p\nmid h\). For integers \(n\) prime to \(p\), write the integral Fermat quotient as
\[
Q_p(n)=\frac{n^{p-1}-1}{p}.
\]
For every integer \(k\ge1\), let \(R_{p,k,h}(a,b)\) count residue classes \(n\bmod p^{k+1}\) with \(p\nmid n(n+h)\), \(Q_p(n)\equiv a\pmod{p^k}\), and \(Q_p(n+h)\equiv b\pmod{p^k}\). Set
\[
d_p=\varphi(p-1),\qquad K_p=\min\{j\ge1:p^j\ge 8^{d_p}\}.
\]
**Theorem.** For every odd prime \(p\), every shift \(h\) prime to \(p\), and every \(k\ge K_p\), the only nonzero representation multiplicities \(R_{p,k,h}(a,b)\) are one and two. Exactly \(\binom{p-2}{2}\) targets have multiplicity two, and exactly \((p-2)p^k-2\binom{p-2}{2}\) targets have multiplicity one. Consequently the exact cardinality of the pair image is
\[
\#\{(Q_p(n),Q_p(n+h))\bmod p^k:p\nmid n(n+h)\}
=(p-2)p^k-\binom{p-2}{2}.
\]
The formula is valid with the pairs indexed by every integer \(n\), or equivalently by the indicated residue classes modulo \(p^{k+1}\). The integer-only bound \(K_p\) is explicit and need not be optimal; for instance, \(K_3=2\), \(K_5=3\), \(K_7=3\), \(K_{11}=4\), and \(K_{13}=4\).

## Assumptions and scope

Throughout, \(p\ge3\) is prime and \(k\ge1\). For a unit \(n\), Fermat's little theorem makes \(Q_p(n)\) integral, and its residue modulo \(p^k\) depends only on \(n\bmod p^{k+1}\). We count residue classes of inputs, not integers in a prescribed short interval. The special case \(p=3\) has just one residue branch and satisfies the asserted profile for every \(k\ge1\). The proof below treats \(h=1\), then obtains all unit shifts by an exact change of variables.

## Proof

**1. Each nonexceptional residue class defines a full graph.** Let \(\omega:\mathbb F_p^\times\to\mathbb Z_p^\times\) denote the Teichmüller lift: \(\omega(r)\equiv r\pmod p\), \(\omega(r)^{p-1}=1\). The admissible input classes modulo \(p\) for a unit-adjacent pair are \(r=1,\ldots,p-2\). Every \(x\equiv r\pmod p\) has a unique expression \(x=\omega(r)u\) with \(u\in1+p\mathbb Z_p\). The map
\[
1+p\mathbb Z_p\longrightarrow\mathbb Z_p,\quad
u\longmapsto \frac{u^{p-1}-1}{p}
\]
is a bijection for which the valuation of a nonzero output difference is one less than that of the corresponding input difference: writing \(u=1+pt\), the induced polynomial has reduction \((p-1)t\) modulo \(p\), and its derivative is a unit at every \(t\in\mathbb Z_p\). It therefore induces a bijection modulo \(p^k\) for every \(k\). Thus, for each \(r\), as the first quotient ranges over all \(a\bmod p^k\), the second quotient is a uniquely determined function \(b_r(a)\). Each of the \(p-2\) branches has precisely \(p^k\) points.

**2. Every two different branches meet once.** Fix distinct \(r,s\in\{1,\ldots,p-2\}\). Equality of the two first quotients is equivalent to representing both inputs as \(\omega(r)u\) and \(\omega(s)u\) with the same \(u\in1+p\mathbb Z_p\). Equality of their second quotients is similarly equivalent to
\[
\omega(r)u+1=\omega(r+1)v,\qquad
\omega(s)u+1=\omega(s+1)v,
\tag{1}
\]
for a common \(v\in1+p\mathbb Z_p\). The determinant of this two-by-two system, \(\omega(r)\omega(s+1)-\omega(s)\omega(r+1)\), reduces to \(r-s\not\equiv0\pmod p\). Hence (1) has a unique solution over \(\mathbb Z_p\), automatically \(u\equiv v\equiv1\pmod p\) because that is the solution after reduction. The same calculation works modulo \(p^{k+1}\), and the quotient-coordinate bijection from Step 1 shows that the two graphs have exactly one common target modulo \(p^k\).

**3. No three branches have a common exact \(p\)-adic point.** Let \(K=\mathbb Q(\mu_{p-1})\), embedded in \(\mathbb Q_p\) by mapping its roots of unity to Teichmüller lifts. Define
\[
\eta_{rs}=\frac{\omega(r+1)}{\omega(s+1)},\qquad
u_{rs}=\frac{\eta_{rs}-1}{\omega(r)-\eta_{rs}\omega(s)}\in K.
\]
Here \(u_{rs}\) is precisely the first-coordinate unit in the intersection from (1); its denominator reduces to \((r-s)/(s+1)\ne0\pmod p\). For three distinct indices \(r,s,t\), suppose \(u_{rs}=u_{rt}=u\). The corresponding second-coordinate units must also agree, since the equation for index \(r\) uniquely recovers \(v\) from \(u\). Under any complex embedding of \(K\), the three numbers
\[
z_j=\omega(j)u+1=\omega(j+1)v\qquad(j\in\{r,s,t\})
\]
are distinct, because \(u\ne0\) and the roots \(\omega(j)\) are distinct. They belong simultaneously to the circles \(\lvert z-1\rvert=\lvert u\rvert\) and \(\lvert z\rvert=\lvert v\rvert\). Two circles with different centers cannot share three points. This contradiction proves \(u_{rs}\ne u_{rt}\).

**4. An effective bound excludes triple overlaps modulo prime powers.** With the same distinct \(r,s,t\), put
\[
N_{rst}=(\eta_{rs}-1)(\omega(r)-\eta_{rt}\omega(t))
 -(\eta_{rt}-1)(\omega(r)-\eta_{rs}\omega(s)).
\]
This is a nonzero algebraic integer by Step 3. Under every complex embedding, each parenthesized difference of roots of unity has absolute value at most two. By the triangle inequality, \(\lvert \sigma(N_{rst})\rvert\le8\), and therefore
\[
0<\left\lvert\operatorname{Norm}_{K/\mathbb Q}(N_{rst})\right\rvert
\le 8^{[K:\mathbb Q]}=8^{\varphi(p-1)}.
\tag{2}
\]
Both denominators in \(u_{rs}-u_{rt}\) are \(p\)-adic units. If the three graphs shared a target modulo \(p^k\), the two pairwise intersections would have identical first quotient coordinates modulo \(p^k\). The first-coordinate valuation identity in Step 1 would give \(u_{rs}\equiv u_{rt}\pmod{p^{k+1}}\), hence \(N_{rst}\equiv0\pmod{p^{k+1}}\) under the selected \(p\)-adic embedding. Since \(p\equiv1\pmod{p-1}\), \(p\) splits completely in \(K\); in particular, divisibility to this order at one prime above \(p\) forces the rational integer norm to be divisible by \(p^{k+1}\). For \(k\ge K_p\), we have \(p^{k+1}>8^{\varphi(p-1)}\), contradicting (2). Thus no triple intersection is possible in the asserted range.

**5. Fibers and unit shifts.** Every two graphs share exactly one target (Step 2), and no target lies on three graphs (Step 4). There are exactly \(\binom{p-2}{2}\) double fibers. Subtracting their two incidences from the total \((p-2)p^k\) gives the singleton count and the stated image size. Finally, for \(p\nmid h\), the exact integer identity
\[
Q_p(hm)=Q_p(h)+h^{p-1}Q_p(m)
\]
shows that the substitution \(n=hm\) maps the neighboring-pair image by the affine bijection
\[
(a,b)\longmapsto\bigl(Q_p(h)+h^{p-1}a,\ Q_p(h)+h^{p-1}b\bigr)
\pmod{p^k}.
\]
The factor \(h^{p-1}\) is a unit, so all representation multiplicities are preserved. This completes the proof.

## Verification

Run `python verify.py` using Python 3. The script independently enumerates the full input period for ten \((p,k)\) pairs, including five at or beyond the explicit theorem cutoff, reconstructs all pairwise intersections by modular Teichmüller lifts, checks three nonunit-step transforms, and exhibits three triple fibers for \((p,k)=(11,1)\), demonstrating why no unrestricted small-exponent claim is made. It reports:

`VERIFY_OK prime_power_cases=10 shift_cases=3 triple_at_level_one_p11=3`

Enumeration does not prove the theorem for general primes or exponents; Steps 1–5 provide the universal proof.

## Relationship to prior work

Ostafe and Shparlinski, *Pseudorandomness and Dynamics of Fermat Quotients* (arXiv:1001.1504v1, 2010), study consecutive Fermat-quotient vectors. Their Section 4.1, Theorem 11 and Corollary 12 provide exponential-sum and discrepancy estimates for vectors modulo \(p\), not a complete eventual fiber census over \(p^k\). Shparlinski, *Fermat Quotients: Exponential Sums, Value Set and Primitive Roots* (arXiv:1104.3909v1, 2011), obtains single-coordinate image estimates and bounds related to intervals. Chen and Winterhof, *On the Distribution of Pseudorandom Numbers and Vectors Derived from Euler–Fermat Quotients* (2012), treat distribution bounds for generalized vectors; the full text was not accessible in this examination, so priority uncertainty remains. The present result concerns the exact simultaneous image over the full natural prime-power period, rather than discrepancy in short intervals or scalar value sets.

## Limitations

The numerical cutoff \(K_p\) is an effective sufficient bound, not the claimed smallest stabilization level. For example, triples occur at \((p,k)=(11,1)\), whereas the explicit bound is \(K_{11}=4\). The proof does not treat a shift divisible by \(p\), more than two consecutive quotient coordinates, or short input intervals. It establishes no randomness assertion or cryptographic security property. Mathematical originality is a best-knowledge assessment, not proof of historical priority; an unpublished or differently formulated general result may cover the theorem.

## References

1. A. Ostafe and I. E. Shparlinski, *Pseudorandomness and Dynamics of Fermat Quotients*, arXiv:1001.1504 (first posted 2010-01-10), especially Section 4.1. https://arxiv.org/abs/1001.1504
2. I. E. Shparlinski, *Fermat Quotients: Exponential Sums, Value Set and Primitive Roots*, arXiv:1104.3909 (first posted 2011-04-20). https://arxiv.org/abs/1104.3909
3. Z. Chen and A. Winterhof, *On the Distribution of Pseudorandom Numbers and Vectors Derived from Euler–Fermat Quotients*, International Journal of Number Theory 8 (2012), 631–641, DOI 10.1142/S1793042112500352. https://doi.org/10.1142/S1793042112500352
4. Z. Chen and A. Winterhof, *Interpolation of Fermat Quotients*, SIAM Journal on Discrete Mathematics 28 (2014), 1–7, DOI 10.1137/130907951. https://doi.org/10.1137/130907951
