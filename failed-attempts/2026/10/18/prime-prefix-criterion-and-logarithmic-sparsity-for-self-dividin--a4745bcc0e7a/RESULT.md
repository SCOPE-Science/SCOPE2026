# Prime-prefix criterion and logarithmic sparsity for self-dividing decimal repunits

## Finding
For every integer \(n\geq1\), let \(R(n)=(10^n-1)/9\) and call \(n\) *self-dividing* when \(n\mid R(n)\). Then \(1\) is self-dividing. Every self-dividing \(n>1\) has an ordered prime factorization
\[
n=3^a\prod_{i=1}^{r}p_i^{e_i},\qquad a\geq1,\quad 3<p_1<\cdots<p_r,\quad e_i\geq1.
\]
Conversely, such a positive integer is self-dividing if and only if for **every** \(1\leq i\leq r\),
\[
\operatorname{ord}_{p_i}(10)\mid 3^a\prod_{j<i}p_j^{e_j}.
\]
The empty product permits all \(3^a\), \(a\geq1\). Moreover, self-dividing integers with **exactly two distinct prime factors** are precisely
\[
3^a q^b\quad(a,b\geq1,\ q>3\text{ prime},\ \operatorname{ord}_q(10)\mid3^a),
\]
and infinitely many distinct choices of \(q\) occur. This gives an exact prime-by-prime construction, not merely a finite parameter list.

Write \(A(X)=\#\{1\leq n\leq X:n\mid R(n)\}\). Define the real quadratic character \(\chi(p)=\bigl(\frac{10}{p}\bigr)\) for odd primes \(p\neq5\), extended as the primitive Dirichlet character modulo \(40\). Thus \(\chi(p)=1\) precisely when
\[
p\\bmod40\in\{1,3,9,13,27,31,37,39\}.
\]
Every self-dividing \(n>1\) is divisible by \(3\) and has only prime factors with \(\chi(p)=1\). Put
\[
C_{40}=\frac1{\sqrt\pi}\left[\frac25L(1,\chi)\prod_{\chi(p)=-1}\left(1-\frac1{p^2}\right)\right]^{1/2}>0.
\]
Here the product runs over odd primes other than \(5\), and converges absolutely. Then, as \(X\to\infty\),
\[
A(X)\leq\left(\frac{C_{40}}3+o(1)\right)\frac{X}{\sqrt{\log X}}.
\]
In particular the set of self-dividing repunit lengths has natural density \(0\). This is an upper bound; equality in this asymptotic bound is **not** asserted.

## Assumptions and scope
All integers and primes are positive. The order \(\operatorname{ord}_p(10)\) is defined only for primes \(p\nmid10\). The exponent \(a\geq1\) is unrestricted; \(r\geq0\) and the indices \(p_i\) are distinct odd primes exceeding \(3\). The analytic statement concerns **the lengths \(n\)**, not the density of repunit values \(R(n)\) among positive integers. Logarithms are natural; the constant \(C_{40}\) is explicitly defined by a convergent Euler product and a classical Dirichlet \(L\)-value.

## Proof
**1. Lowest prime and ordered necessity.** Every \(R(n)\) ends in digit \(1\), hence a self-dividing \(n\) is coprime to \(10\). Suppose \(n>1\) and let \(p\) be its least prime divisor. If \(p\neq3\), then \(p\geq7\). Since \(p\mid R(n)\), we have \(10^n\equiv1\pmod p\), so \(d=\operatorname{ord}_p(10)\mid n\). But \(d>1\) because \(p\nmid10-1=9\), and \(d\mid p-1\). Thus some prime smaller than \(p\) divides \(n\), a contradiction. Hence \(3\mid n\). For any other prime divisor \(p_i>3\), its order \(d_i\mid p_i-1\) divides \(n\) and all prime factors of \(d_i\) are smaller than \(p_i\). Therefore \(d_i\mid 3^a\prod_{j<i}p_j^{e_j}\), proving necessity.

**2. Sufficiency including every exponent.** Suppose all displayed order tests hold. For \(p_i>3\), let \(d_i=\operatorname{ord}_{p_i}(10)\); then \(d_i\mid n\), \(p_i\nmid d_i\), and the odd-prime lifting-the-exponent identity gives
\[
\nu_{p_i}(R(n))=\nu_{p_i}(10^{d_i}-1)+\nu_{p_i}(n/d_i)\geq 1+e_i\geq e_i.
\]
For \(3\), lifting the exponent at \(10\equiv1\pmod 3\) gives
\[
\nu_3(R(n))=\nu_3(10^n-1)-\nu_3(9)=(2+\nu_3(n))-2=a.
\]
Every prime-power factor of \(n\) therefore divides \(R(n)\); thus \(n\mid R(n)\). Restricting to \(r=1\) proves the exact two-support description.

**3. Infinitely many two-support lengths.** For each \(a\geq1\), the Bang–Zsigmondy primitive-divisor theorem applied to \(10^{3^a}-1\) supplies a prime \(q_a\) of multiplicative order exactly \(3^a\) modulo \(q_a\). Its exceptional cases do not occur for base \(10\) and exponent \(3^a\geq3\). Then \(q_a\notin\{2,3,5\}\), \(q_a>3\), and \(3^a q_a^b\) is self-dividing for every \(b\geq1\). Distinct values of \(a\) force distinct \(q_a\) because their multiplicative orders differ. (No assertion is made that all two-support choices have this primitive order.)

**4. Character obstruction.** Every prime factor \(p_i>3\) of a self-dividing \(n\) has \(d_i\mid n\), and \(n\) is odd. Therefore \(d_i\) is odd and divides \((p_i-1)/2\), hence Euler's criterion yields \(\chi(p_i)=\bigl(\frac{10}{p_i}\bigr)=1\). At \(p=3\), \(\chi(3)=1\). Quadratic reciprocity identifies \(\chi\) as the real quadratic character modulo \(40\) with the eight stated positive residue classes.

**5. Sharp count for the containing multiplicative set.** Let \(B\) be the multiplicative set with all prime factors \(p\) satisfying \(\chi(p)=1\), and write \(B(X)\) for its counting function. Its Dirichlet series \(F(s)\), for \(\Re(s)>1\), satisfies the exact Euler-factor identity
\[
F(s)=\prod_{\chi(p)=1}(1-p^{-s})^{-1},\qquad
F(s)^2=\zeta(s)L(s,\chi)(1-2^{-s})(1-5^{-s})\prod_{\chi(p)=-1}(1-p^{-2s}).
\]
The last product converges absolutely for \(\Re(s)>1/2\). As \(L(1,\chi)>0\), the standard Selberg–Delange theorem for the displayed \(\zeta(s)^{1/2}\)-type Dirichlet series yields
\[
B(X)\sim C_{40}\frac{X}{\sqrt{\log X}}.
\]
The Dirichlet series for the subset of \(B\) divisible by \(3\) is **exactly** \(3^{-s}F(s)\), since \(\chi(3)=1\). The same theorem gives its count as \((C_{40}/3+o(1))X/\sqrt{\log X}\). Every self-dividing \(n>1\) belongs to that subset. Adding the isolated integer \(1\) proves the stated upper bound and zero density.

## Verification
The accompanying standalone Python 3 verifier compares the prime-prefix criterion against the independent exact divisibility test \(10^n\equiv1\pmod{9n}\) for each \(1\leq n\leq120000\), and tests four distinct primitive-order seeds together with three exponents each. It printed `SELF_DIVIDING_REPUNIT_EXACT_REGRESSION_OK range=1..120000 hits=27 primitive_examples=4`. The script also checks the character obstruction. These are finite consistency checks; the infinite theorem requires the proofs above, including classical lifting the exponent, primitive divisors, and Selberg–Delange.

## Relationship to prior work
OEIS A095250 (Amarnath Murthy, dated June 17, 2004) directly records the remainder of the length-\(n\) repunit modulo \(n\) and notes the prime and power-of-three cases. OEIS A172372 records the least length at which a given prime divides a repunit. Murthy's earlier paper concerns divisors of repunits at prime digit lengths rather than complete characterization of indices self-dividing by their own repunits.

Wu and Lou, *Permutation-Invariant Niven Numbers* (first publicly available as arXiv:2508.01611, 2025; later *Symmetry* 18 (2026), 186), formulate \(10^k\equiv1\pmod{9k}\) and conjecture a construction with several specified primes. Their density-zero assertion is about the **integer values** of all permutation-invariant Niven numbers; it does not bound the density of admissible **lengths**. Their printed finite-prime parameter conjecture is not assumed or proved here. The present order-prefix equivalence allows arbitrarily many possible primes and determines all self-dividing lengths, while the analytic bound concerns those lengths. The earlier published construction criterion for Novák numbers uses the different condition \(m\mid2^m+1\), which neither implies nor is implied by the repunit theorem.

## Limitations
This result does not count the actual self-dividing lengths asymptotically, prove that the logarithmic exponent \(1/2\) is optimal, describe digit bases other than ten, or settle the published finite-prime parameter conjecture. Standard classical theorems are invoked with their exact hypotheses but are not reproved here. Searches and checked source texts may miss an earlier equivalent derivation; no independent originality certification has been performed. The Murthy 2000 paper has a year but no verified initial publication **day**, so June 17, 2004 (the dated OEIS record) is used as the earliest inspected **date-specific** public source evidence for the exact remainder question, without asserting it precedes the older article.

## References
1. Amarnath Murthy, OEIS A095250, *Repunit of length \(n\) reduced modulo \(n\)*, June 17, 2004, https://oeis.org/A095250.
2. Michel Lagneau, OEIS A172372, least repunit length divisible by an odd prime, February 1, 2010, https://oeis.org/A172372.
3. Amarnath Murthy, *On the Divisors of Smarandache Unary Sequence*, *Smarandache Notions Journal* 11 (2000), https://fs.unm.edu/SNJ/OnTheDivisorsOfSmarandacheUnary.pdf.
4. Huiling Wu and Senyue Lou, *Permutation-Invariant Niven Numbers*, arXiv:2508.01611 (2025), https://arxiv.org/abs/2508.01611; *Symmetry* 18 (2026), article 186, https://doi.org/10.3390/sym18010186.
5. Classical Bang–Zsigmondy theorem on primitive prime divisors of \(a^m-b^m\); classical lifting-the-exponent lemma; classical Selberg–Delange theorem for Euler products with \(\zeta(s)^z\)-type singularities (\(z=1/2\)).
