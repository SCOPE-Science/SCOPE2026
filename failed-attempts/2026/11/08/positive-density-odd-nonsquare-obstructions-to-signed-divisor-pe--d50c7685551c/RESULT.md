# Positive-density odd nonsquare obstructions to signed divisor perfection

## Finding
Let \(\sigma(n)\) be the sum of all positive divisors of \(n\), and let \(\mathcal P\) denote the positive \(\{-1,1\}\)-perfect integers in the sense of Ross: for \(n>1\), every divisor strictly between \(1\) and \(n\) receives a sign, and their signed sum together with \(1\) equals \(n\). Define
\[
\mathcal E=\{n\ge1: n\text{ is odd and nonsquare},\ \sigma(n)>2n,\ n\notin\mathcal P\}.
\]
**The set \(\mathcal E\) has positive lower natural density.** Quantitatively, set \(a=11025=3^2 5^2 7^2\), \(S=\sigma(a)=22971\), \(Y=4S=91884\), and \(\rho_Y=\prod_{p\le Y}(1-p^{-1})\), over primes. Then
\[
\liminf_{X\to\infty}\frac{\#\{n\le X:n\in\mathcal E\}}{X}\ge \frac{3\rho_Y}{4a}>0.
\]
More generally, for every odd abundant square \(a\), any integer \(m>1\) with \(\gcd(a,m)=1\), \(m\) odd and nonsquare, and \(\sigma(a)(\sigma(m)-m)<m\) gives \(am\in\mathcal E\). The quantitative density assertion holds with \(Y=4\sigma(a)\) and \(\rho_Y\) as above.

## Assumptions and scope
All variables are positive integers, except the real counting bound \(X>0\). The sum-of-divisors function includes \(1\) and \(n\). A number is abundant when \(\sigma(n)>2n\). A number is nonsquare when it is not a perfect square. Density is lower asymptotic density, not a claim that the full natural density of \(\mathcal E\) exists. This theorem concerns signed presentations using *every* proper nontrivial divisor with sign \(-1\) or \(+1\), not semiperfect subset sums.

## Proof
**Step 1: a divisor-sum obstruction.** Let \(a\) be an odd abundant square. Every prime dividing \(a\) has even exponent, so \(\sigma(a)\) is odd. Set \(S=\sigma(a)\) and \(\Delta=S-2a=2q+1>0\) for an integer \(q\ge0\). Let \(m>1\) be odd, nonsquare, coprime to \(a\), and put \(s=\sigma(m)-m\), \(E=Ss\), \(n=am\). Multiplicativity gives
\[
\sigma(n)-2n=\Delta m+E>0,
\qquad
H=\frac{\sigma(n)-2n}{2}=qm+\frac{m+E}{2}.
\]
Since \(m\) is nonsquare, \(\sigma(m)\) is even; since \(m,S,\Delta\) are odd, \(H\) is integral. If \(E<m\), then
\[
qm+E<H<(q+1)m.
\]
Every divisor of \(am\) is uniquely \(d e\), with \(d\mid a\), \(e\mid m\), by coprimality. Any sum \(T\) of distinct divisors excluding \(1\) and \(n\) therefore has the form \(T=Bm+R\), where \(B\) is a nonnegative integer (contributions with \(e=m\)) and
\[
0\le R\le \sum_{d\mid a}d\sum_{e\mid m,\,e<m}e=S(\sigma(m)-m)=E.
\]
If \(B\le q\), then \(T\le qm+E<H\); if \(B\ge q+1\), then \(T\ge(q+1)m>H\). Thus no such subset sums to \(H\). The signed-presentation relation \(n=1+\sum_{1<d<n,d\mid n}\varepsilon_d d\), \(\varepsilon_d\in\{-1,1\}\), is equivalent (by switching negative signs from the all-positive sum) to a subset sum of proper nontrivial divisors equal to \(H\). Hence \(n\notin\mathcal P\). As \(a\) is a square and \(m\) is a coprime nonsquare, \(n\) is odd nonsquare, proving \(n\in\mathcal E\).

**Step 2: a positive-density set of admissible cofactors.** For fixed \(Y=4S\), let \(P=\prod_{p\le Y}p\) and \(\rho_Y=\varphi(P)/P>0\). For \(m\) coprime to \(P\), put
\[
f(m)=\frac{\sigma(m)}m-1=\sum_{d\mid m,\,d>1}\frac1d\ge0.
\]
The number of integers \(h\le T\) coprime to fixed \(P\) is \(\rho_Y T+O_Y(1)\). Interchanging a finite sum, and using \(\gcd(m,P)=1\) if and only if both factors in \(m=dh\) are coprime to \(P\), yields
\[
\sum_{\substack{m\le X\\\gcd(m,P)=1}} f(m)
=\rho_Y X\sum_{\substack{1<d\le X\\\gcd(d,P)=1}}\frac1{d^2}+O_Y(\log(2X)).
\]
Any such \(d>1\) has no prime divisor at most \(Y\), hence \(d>Y\). Therefore \(\sum_{d>Y}d^{-2}\le Y^{-1}\), and
\[
\sum_{\substack{m\le X\\\gcd(m,P)=1}} f(m)\le \rho_Y X/Y+o_Y(X).
\]
By the elementary counting form of Markov's inequality, the number of these \(m\) for which \(f(m)\ge 1/S\) is at most \(S\rho_Y X/Y+o_Y(X)\). Consequently at least
\[
\left(1-\frac{S}{Y}\right)\rho_Y X+o_Y(X)=\frac{3\rho_Y}{4}X+o_Y(X)
\]
integers \(m\le X\) are coprime to \(P\) and satisfy \(S(\sigma(m)-m)<m\). All are odd and coprime to \(a\), because every prime dividing \(a\) is at most \(a<\sigma(a)\le Y\), so it divides \(P\). Deleting squares costs at most \(\lfloor\sqrt X\rfloor\) terms and deleting \(m=1\) costs one. Mapping the remaining \(m\) injectively to \(n=am\) yields the asserted lower density \(3\rho_Y/(4a)\) for \(\mathcal E\).

**Step 3: a concrete core.** For \(a=3^2 5^2 7^2=11025\), multiplicativity gives \(S=(1+3+9)(1+5+25)(1+7+49)=13\cdot31\cdot57=22971>2a=22050\). Hence \(a\) is an odd abundant square and the stated quantitative bound applies.

## Verification
Run `python3 verify.py` to reproduce exact-integer checks for the core and four admissible cofactors, including prime, squarefree composite, and repeated-prime nonsquare cofactors. Each example verifies the strict divisor-sum gap and all algebraic identities. `verification_output.txt` records the executed output. The infinite-density argument follows from the proof above, not the finite checks.

## Relationship to prior work
Ross (2024), Conjecture 17, proposed that every odd nonsquare abundant integer is \(\{-1,1\}\)-perfect. Campbell (2026) disproved it using \(ap\), where \(a\) is an odd abundant square and \(p>\sigma(a)\) is prime (Theorem 3.1); this produces an infinite but density-zero prime-indexed construction. Campbell's Theorem 2.4 independently gives positive density of nonperfect abundant integers via **even** numbers \(18m\), using a small-abundancy lemma. The present result combines a generalized odd-core obstruction with a cofactor density sieve to prove **positive lower density within the odd nonsquare counterexample set**, which neither earlier statement implies. The small-abundancy mechanism and divisor-sum decomposition have their precedents in Campbell's proofs and are not claimed as new independently.

## Limitations
We do not prove existence of a natural density (as opposed to a positive lower density), optimize the explicit small constant, classify all odd nonsquare nonperfect abundant integers, or obtain an efficient least-element bound. The result uses standard density arguments and is close in technique to Campbell (2026), so broader unindexed equivalent literature is a priority risk. Finite numerical verification does not replace the infinite proof. No independent audit has been performed.

## References
1. J. M. Campbell, *Disproofs of two conjectures concerning nondeficient numbers*, arXiv:2607.11043v1 (first public July 13, 2026), Sections 2 and 3. https://arxiv.org/abs/2607.11043
2. T. Ross, *A Perfect Number Generalization and Some Euclid–Euler Type Results*, Journal of Integer Sequences **27** (2024), Article 24.7.5, especially Theorem 15 and Conjectures 16–17. https://cs.uwaterloo.ca/journals/JIS/VOL27/Ross/ross3.pdf
