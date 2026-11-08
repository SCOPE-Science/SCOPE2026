# A strict density separation for the \(42\)- and \(1806\)-power-sum congruences

## Finding
For \(Q\in\{42,1806\}\), let
\[
\mathcal N_Q=\left\{n\in\mathbb Z_{\ge1}:\sum_{j=1}^{Qn}j^{Qn}\equiv n\pmod{Qn}\right\},
\qquad \delta_Q=\lim_{X\to\infty}\frac{\#(\mathcal N_Q\cap[1,X])}{X}.
\]
Both densities exist and satisfy the **strict, quantitative inequality**
\[
\boxed{\delta_{1806}-\delta_{42}>\frac{47}{17200}>\frac1{400}.}
\]
In particular, \(\delta_{42}<\delta_{1806}\), settling the specific order left undecided in the 2013 study of these power-sum congruences by Grau, Oller-Marcén, and Sondow.

## Assumptions and scope
All indices and moduli are positive integers. The result concerns exactly the two fixed multipliers \(Q=42\) and \(Q=1806=42\cdot43\); there is no assertion of monotonicity for general multipliers. Density is ordinary natural density on the positive integers, not a logarithmic density. Computed rational inequalities below can be checked using only exact integer arithmetic and elementary primality tests.

## Proof
**1. An elementary prime obstruction.** For any positive *even* integer \(m\), put \(S(m)=\sum_{j=1}^{m}j^m\). The standard prime-power lifting identity gives
\[
S(m)\equiv-\sum_{\substack{p\mid m\\p-1\mid m}}\frac{m}{p}\pmod m.
\tag{1}
\]
For completeness, if \(p^a\mid m\), summing one complete block modulo \(p^a\) gives \(\sum_{j=1}^{p^a}j^m\equiv-p^{a-1}\) when \(p-1\mid m\), and zero otherwise, modulo \(p^a\). This follows by induction on \(a\) from the power-sum identity over \(\mathbb F_p\), expanding the \(p\) translates of each residue modulo \(p^{a-1}\); for \(p=2\) the cross term is also divisible by \(2^a\) because \(m\) is even. Multiplication by the number \(m/p^a\) of blocks and the Chinese remainder theorem yield (1).

For \(Q=42\) and \(Q=1806\), every prime dividing \(Q\) has \(p-1\mid Q\), and direct addition gives
\[
1+\sum_{p\mid Q}\frac Qp=Q.
\tag{2}
\]
Take \(m=Qn\). Equation (1), together with (2), says \(S(Qn)\equiv n\pmod{Qn}\) if and only if no prime \(p\nmid Q\) with \(p\mid n\) also satisfies \(p-1\mid Qn\). Indeed, a nonempty set of such extra primes cannot cancel: modulo the highest power of any one extra prime dividing \(Qn\), its term \((Qn)/p\) is nonzero, whereas all other terms \((Qn)/r\), \(r\ne p\), vanish. As \(p\) is coprime to \(p-1\) and does not divide \(Q\), the obstruction is equivalent to
\[
\boxed{\mathcal N_Q=\mathbb Z_{\ge1}\setminus
\bigcup_{\substack{p\text{ prime}\\p\nmid Q}}
\left\{n:\frac{p(p-1)}{\gcd(Q,p-1)}\mid n\right\}.}
\tag{3}
\]

**2. Isolating the additional prime \(43\).** Set
\[
\mathcal P=\{p\text{ prime}:p\nmid1806,\ p\not\equiv1\pmod{43}\},
\quad a_p=\frac{p(p-1)}{\gcd(42,p-1)},
\quad U=\{n:a_p\nmid n\text{ for all }p\in\mathcal P\}.
\]
Every \(a_p\) is coprime to \(43\). For \(Q=42\), the prime \(p=43\) contributes exactly the forbidden modulus \(43\); every further prime \(p\equiv1\pmod{43}\) contributes a modulus divisible by \(43\), which is therefore redundant. Hence
\[
\mathcal N_{42}=U\cap\{n:43\nmid n\}.
\tag{4}
\]
For \(Q=1806\), the obstruction \(p=43\) disappears. The primes in \(\mathcal P\) impose exactly the same obstructions as for \(Q=42\). Each remaining prime has the form \(p=43k+1\) for a positive even integer \(k\), and its new forbidden modulus is
\[
b_k=\frac{(43k+1)k}{\gcd(42,k)}.
\]
Consequently,
\[
\mathcal N_{1806}=U\setminus\bigcup_{\substack{k\ge2\ \mathrm{even}\\43k+1\ \mathrm{prime}}}\{n:b_k\mid n\}.
\tag{5}
\]

**3. Existence and comparison of densities.** Since \(a_p\ge p(p-1)/42\) and \(b_k\ge43k^2/42\), the respective reciprocal-modulus series converge. The densities of the finite periodic sieves therefore converge to the densities of their infinite intersections; their omitted tails have upper density bounded by the corresponding reciprocal sums. Write \(u=\delta(U)\). Every finite common sieve is coprime to \(43\), so the Chinese remainder theorem makes each residue class modulo \(43\) equally frequent. Passing to the convergent limit, (4) and (5) give
\[
\delta_{42}=\frac{42}{43}u,
\qquad
\delta_{1806}\ge u-S,
\quad
S=\sum_{\substack{k\ge2\ \mathrm{even}\\43k+1\ \mathrm{prime}}}\frac{\gcd(42,k)}{k(43k+1)}.
\tag{6}
\]

**4. A finite exact certificate and elementary tails.** The only primes in \(\mathcal P\) up to \(100\) are
\[
5,11,13,17,19,23,29,31,37,41,47,53,59,61,67,71,73,79,83,89,97.
\]
Exact rational summation (see `verify.py`) gives
\[
C:=\sum_{\substack{p\in\mathcal P\\p\le100}}\frac{\gcd(42,p-1)}{p(p-1)}<\frac{227}{1000}.
\tag{7}
\]
Since \(\sum_{r>100}1/[r(r-1)]=1/100\), the union bound yields
\[
u\ge1-C-\frac{42}{100}>\frac{353}{1000}.
\tag{8}
\]
For the exceptional primes \(43k+1\), exact rational summation over the \(109\) even indices \(2\le k\le1000\) at which \(43k+1\) is prime gives
\[
S_{\le1000}:=\sum_{\substack{2\le k\le1000,\ k\ \mathrm{even}\\43k+1\ \mathrm{prime}}}\frac{\gcd(42,k)}{k(43k+1)}<\frac9{2000}.
\tag{9}
\]
For the omitted tail, \(\gcd(42,k)\le42\) and \(43k+1\ge43k\), whence
\[
S-S_{\le1000}\le\frac{42}{43}\sum_{k>1000}\frac1{k^2}<\frac{42}{43000}.
\tag{10}
\]
Combining (6)–(10) gives
\[
\delta_{1806}-\delta_{42}\ge\frac{u}{43}-S
>\frac{353}{43000}-\frac9{2000}-\frac{42}{43000}
=\boxed{\frac{47}{17200}}.
\]
This proves the claim.

## Verification
Run `python3 verify.py` with a standard Python 3 installation. It uses `fractions.Fraction`, `math.gcd`, and deterministic trial-division primality tests; no external dependencies or downloaded tables are needed. It recomputes the two strict rational comparisons (7), (9), checks the lower-bound algebra and verifies the prime-obstruction characterization against direct modular power sums for \(70\) small examples, plus \(299\) finite sieve decompositions. The finite checks are not substitutes for the proof of the infinite sums and density limits.

## Relationship to prior work
Grau, Oller-Marcén, and Sondow, arXiv:1309.7941, obtain the divisor-obstruction description and existence of the two densities, but explicitly state that they cannot prove \(\delta_{42}<\delta_{1806}\) (end of Section 4). The separation in this note adds a comparison through the appearance/disappearance of the \(43\)-divisibility obstruction and two rationally certified finite sums with rigorous infinite tails. OEIS A229300 and A229301 record the separate congruence sequences and their density intervals; neither provides the cross-density inequality.

## Limitations
The explicit lower bound is not the exact difference, and no exact value of either density is claimed. The result addresses only this pair of multipliers and does not settle the more general conjecture on densities for arbitrary weak primary pseudoperfect multipliers. Originality is based on inspected primary literature, the named sequence records, and targeted mathematical-record searches; a differently phrased unpublished or unindexed proof cannot be ruled out. No independent mathematical audit is claimed.

## References
1. J. M. Grau, A. M. Oller-Marcén, J. Sondow, *On the congruence \(1^m+2^m+\cdots+m^m\equiv n\pmod m\) with \(n\mid m\)*, arXiv:1309.7941 (first released 2013-09-30), especially Section 4, Corollary 2 and the paragraph preceding Conjecture 1. https://arxiv.org/abs/1309.7941
2. OEIS A229300, integers satisfying the corresponding congruence for \(Q=1806\). https://oeis.org/A229300
3. OEIS A229301, integers satisfying the corresponding congruence for \(Q=42\). https://oeis.org/A229301
