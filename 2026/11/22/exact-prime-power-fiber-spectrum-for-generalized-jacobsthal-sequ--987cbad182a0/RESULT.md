# Exact prime-power fiber spectrum for generalized Jacobsthal sequences at primitive-root parameters

## Finding

For an integer \(a\ge 2\), define the generalized Jacobsthal sequence by
\[
J_0=0,\qquad J_1=1,\qquad J_{n+2}=(a-1)J_{n+1}+aJ_n\quad(n\ge0).
\]
Let \(p\ge5\) be prime, \(r\ge1\), and suppose \(a\) is a primitive root modulo \(p^r\). Put \(q=p^r\), \(T=\varphi(q)=p^{r-1}(p-1)\), and let \(\chi_p\) be the quadratic character modulo \(p\), extended by \(\chi_p(0)=0\). The **least period** of \((J_n\bmod q)\) from index zero is \(T\). For every integer target \(y\), its number of occurrences in one period,
\[
N_q(y)=\#\{0\le n<T:J_n\equiv y\pmod q\},
\]
is exactly
\[
\boxed{N_q(y)=\mathbf 1_{\{\chi_p(1+(a+1)y)=1\}}+\mathbf 1_{\{\chi_p((a+1)y-1)=-1\}}.}
\]
In particular every fiber has multiplicity \(0\), \(1\), or \(2\), determined only by \(y\bmod p\) (and the parameter \(a\bmod p\)). The complete multiplicity histogram is **independent of the primitive-root parameter**. Write
\[
c_p=\begin{cases}
(p-1)/4,&p\equiv1,5\pmod8,\\
(p+1)/4,&p\equiv3\pmod8,\\
(p-3)/4,&p\equiv7\pmod8.
\end{cases}
\]
Then the exact numbers of targets \(y\bmod q\) with \(N_q(y)=j\) are
\[
\boxed{(H_0,H_1,H_2)=p^{r-1}\bigl(1+c_p,\;p-1-2c_p,\;c_p\bigr).}
\]
Thus the image has exactly \(p^{r-1}(p-1-c_p)\) residues and all prime-power levels have the same image proportion and multiplicity proportions as the prime level. As \(p\) grows, the proportions of the three types tend to \((1/4,1/2,1/4)\), with explicit \(p\bmod8\) corrections.

## Assumptions and scope

All quantifiers above are universal over \(a\ge2\), odd prime \(p\ge5\), exponent \(r\ge1\), and target integers \(y\), subject to \(\operatorname{ord}_{p^r}(a)=p^{r-1}(p-1)\). No parity restriction is imposed on \(a\). The primitive-root condition ensures \(p\nmid a(a+1)\): if \(a\equiv-1\pmod p\), its order modulo \(p\) would be two instead of \(p-1\ge4\). The Legendre symbol uses reduction of its argument modulo \(p\). Multiplicities always count **indices in one least period**, not distinct values of the integer sequence.

The theorem does not cover \(p=3\), nonprimitive bases, composite moduli with distinct prime factors, or an unrestricted classification of every generalized Jacobsthal modulus.

## Proof

**1. Explicit formula and period.** The characteristic roots are \(a\) and \(-1\), giving the integral identity
\[
(a+1)J_n=a^n-(-1)^n.
\]
Since \(T\) is even and \(a^T\equiv1\pmod q\), the formula (and invertibility of \(a+1\bmod q\)) implies \(J_{n+T}\equiv J_n\pmod q\) for every \(n\ge0\). Conversely, suppose \(s\ge1\) is any period starting at index zero. Then \(J_s\equiv J_0=0\) and \(J_{s+1}\equiv J_1=1\pmod q\). The explicit formula gives \(a^s\equiv(-1)^s\pmod q\), and substituting this into the second congruence yields
\[
(a+1)(-1)^s\equiv a+1\pmod q.
\]
Because \(p\ge5\) and \(a+1\) is invertible modulo \(q\), \(s\) must be even. Hence \(a^s\equiv1\pmod q\), so \(T\mid s\) by the primitive-root hypothesis. Therefore \(T\) is the least period.

**2. Exact individual fibers.** As \(j\) ranges over \(0,\ldots,T/2-1\), the powers \(a^{2j}\) run exactly once through the square units of \(\mathbb Z/q\mathbb Z\), while \(a^{2j+1}\) run exactly once through the nonsquare units (because \(a\) generates its cyclic unit group). For even and odd indices respectively,
\[
(a+1)J_{2j}+1=a^{2j},\qquad (a+1)J_{2j+1}-1=a^{2j+1}.
\]
For odd prime-power moduli, a unit is a square precisely when its reduction modulo \(p\) has Legendre symbol \(+1\). Accordingly each parity branch contributes either exactly one preimage or none, as specified by the two indicators. This proves the individual-fiber formula and the absence of higher multiplicities.

**3. Exact overlap of the branches.** Multiplication by \(a+1\) permutes residues modulo \(q\), so write \(z=(a+1)y\). A double fiber is exactly a class satisfying
\[
\chi_p(z+1)=1,\qquad\chi_p(z-1)=-1.
\]
These conditions depend only on \(z\bmod p\), so their solution count modulo \(q\) is \(p^{r-1}c_p\), where the prime-level count is
\[
c_p=\frac14\sum_{z\in\mathbb F_p\setminus\{1,-1\}}(1+\chi_p(z+1))(1-\chi_p(z-1)).
\]
The three needed sums on \(z\ne\pm1\) are
\[
\sum\chi_p(z+1)=-\chi_p(2),\qquad
\sum\chi_p(z-1)=-\chi_p(-2),\qquad
\sum\chi_p(z^2-1)=-1.
\]
For completeness, the last identity follows by counting the \(p-1\) pairs \((u,v)\in\mathbb F_p^2\) with \(u^2-v^2=1\): the map \((u,v)\mapsto(u-v,u+v)\) bijects them with the \(p-1\) pairs of nonzero reciprocals. On the other hand their number is \(p+\sum_u\chi_p(u^2-1)\). Therefore
\[
c_p=\frac{p-1-\chi_p(2)+\chi_p(-2)}4.
\]
The standard evaluations \(\chi_p(-1)=(-1)^{(p-1)/2}\) and \(\chi_p(2)=(-1)^{(p^2-1)/8}\) give exactly the stated three cases modulo eight.

**4. Histogram.** Each parity branch is injective and has \(T/2\) targets. The intersection has \(p^{r-1}c_p\) targets, all with multiplicity two. Thus \(H_2=p^{r-1}c_p\), and counting total occurrences gives \(H_1=T-2H_2=p^{r-1}(p-1-2c_p)\). The remaining target classes give \(H_0=q-H_1-H_2=p^{r-1}(1+c_p)\). Subtracting \(H_0\) from \(q\) gives the claimed image cardinality. Every step holds for all stated parameters.

## Verification

The standalone script `verify_jacobsthal.py` uses exact integer recurrence arithmetic, an independent multiplicative-order test, and direct residue histograms. For primes from five through forty-seven it verifies the full per-target Legendre-indicator law, all three histogram counts, and the first-return state at each tested prime power up to a modulus of \(100000\). It also tests the character-sum count and the claimed prime-power repetition of the fiber pattern. It needs only Python 3 standard library and can be run with `python3 verify_jacobsthal.py`. These checks corroborate finite examples; the proof above establishes the theorem for arbitrary prime, exponent and primitive root.

## Relationship to prior work

Al-Kateeb (2019, Definition 1 and Theorem 2) defines this exact one-parameter generalized Jacobsthal sequence and proves the Binet formula; its full text develops generating functions, matrix identities, Catalan/Cassini identities and sums, not the modular fiber spectrum. Bród and Michalski (2022, Sections 2–3) also study this recurrence and its Binet formula, summation and matrix identities; their inspected full text likewise contains no primitive-root prime-power fiber law. Griffiths and Bramham (2015, Theorem 3.5) classify complete-residue moduli for the classical base \(a=2\), but knowing that a sequence is not surjective does not determine the frequencies of absent, singleton and double fibers. A separately published complete-modulus classification for all even bases proves local bijections at primes dividing \(a+1\) and non-surjectivity at other primes. Those hypotheses and conclusions differ: here \(p\nmid a+1\), and the result is a complete quantitative histogram at every prime-power level. Bilgici and Bród (2023) study a differently parameterized \(r\)-Jacobsthal recurrence, not the present root pair \((a,-1)\).

## Limitations

The underlying sequence and its Binet formula predate this finding, and the overlap calculation uses classical character sums. The primitive-root assumption is substantial, and the result does not cover all bases at a fixed prime. For a given prime, such parameters exist, but the theorem does not assert that any **fixed** integer base is primitive for infinitely many primes. The character evaluations are classical, and the innovation claimed is their application to the complete, uniform prime-power fiber spectrum of this specific recurrence, not a new character-sum identity. Neither exhaustive bibliographic priority nor independent validation is claimed; an equivalent general Lucas-sequence fiber theorem outside inspected sources could subsume the result.

## References

1. A. Al-Kateeb, *A Generalization of Jacobsthal and Jacobsthal-Lucas Numbers*, arXiv:1911.11515, first posted November 26, 2019, Definition 1 and Theorem 2. https://arxiv.org/abs/1911.11515
2. D. Bród and A. Michalski, *On generalized Jacobsthal and Jacobsthal–Lucas numbers*, Annales Mathematicae Silesianae 36 (2022), 115–128, online July 1, 2022. DOI: 10.2478/amsil-2022-0011. https://www.math.us.edu.pl/annales/contents/2022/v36i2/02_amsil-2022-0011.pdf
3. M. Griffiths and A. Bramham, *The Jacobsthal Numbers: Two Results and Two Questions*, Fibonacci Quarterly 53(2) (2015), 147–151, Theorem 3.5. https://www.fq.math.ca/Papers1/53-2/GriffithsBramham11172014.pdf
4. G. Bilgici and D. Bród, *On r-Jacobsthal and r-Jacobsthal–Lucas numbers*, Annales Mathematicae Silesianae 37 (2023), 16–31. DOI: 10.2478/amsil-2023-0001. https://reference-global.com/download/article/10.2478/amsil-2023-0001.pdf
