# The exact cyclotomic denominator of a shifted \(q\)-central binomial product

## Finding
For all positive integers \(n,k,j\), consider the shifted \(q\)-central binomial rational function
\[
H_{n,k,j}(q)=\frac{1-q}{1-q^{kn+j}}
\prod_{a=1}^{n}\frac{(1-q^{ka})(1-q^{ka+j})}{(1-q^a)^2}.
\tag{1}
\]
Put \(m=\gcd(n,j)\) and let \(u\) be the largest positive divisor of \(m\) coprime to \(k\):
\[
u=\prod_{\substack{p\mid m\\p\nmid k}}p^{\nu_p(m)}.
\tag{2}
\]
(The empty product is \(1\).) The **exact denominator in lowest terms** of (1) is
\[
D_{n,k,j}(q)=\prod_{\substack{d\mid u\\d>1}}\Phi_d(q)
=\frac{q^u-1}{q-1}=1+q+\cdots+q^{u-1}.
\tag{3}
\]
Here \(\Phi_d\) is the \(d\)-th cyclotomic polynomial, and "lowest terms" means coprime integer polynomials, normalized to constant term \(1\). In particular,
\[
H_{n,k,j}(q)\in\mathbb Z[q]
\quad\Longleftrightarrow\quad
\operatorname{rad}(\gcd(n,j))\mid k.
\tag{4}
\]
Every cyclotomic factor appearing in (3) has exponent exactly one.

The original proposed condition \(\gcd(n,j)\mid k\), which appeared as a problem in the 2008 paper and again in a 2012 dissertation, is sufficient but **not necessary**. In fact, for every prime \(p\) and \(a\ge2\), the triple \(n=j=p^a\), \(k=p\) satisfies (4) while violating the proposed condition. The smallest such example is \((n,k,j)=(4,2,4)\), for which
\[
H_{4,2,4}(q)=\Phi_2(q)^3\Phi_4(q)\Phi_5(q)\Phi_6(q)^2\Phi_8(q)^2\Phi_{10}(q)
\in\mathbb Z[q].
\tag{5}
\]
This is a complete replacement classification, not merely a counterexample.

## Assumptions and scope
All three parameters \(n,k,j\) are positive integers, and the expression is treated as an element of \(\mathbb Q(q)\), not as a function evaluated at singular roots of unity. The arithmetic radical is \(\operatorname{rad}(m)=\prod_{p\mid m}p\), with \(\operatorname{rad}(1)=1\). The variable \(q\) is indeterminate. No assumption of primality or coprimality of the parameters is imposed.

## Proof
For each integer \(d\ge1\), write \(e_d\) for the multiplicity of \(\Phi_d(q)\) in (1), with a negative value denoting a denominator factor. Since \(1-q^h\) has precisely one \(\Phi_d\) factor when \(d\mid h\), we get, for \(d\ge2\),
\[
e_d=\sum_{a=1}^{n}
\bigl(\mathbf1_{d\mid ka}+\mathbf1_{d\mid(ka+j)}-2\mathbf1_{d\mid a}\bigr)
-\mathbf1_{d\mid(kn+j)}.
\tag{6}
\]
The prefactor \(1-q\) contributes only to \(d=1\), where \(e_1=1-1+2n-2n=0\).

Fix \(d\ge2\). Put \(g=\gcd(d,k)\), \(A=\#\{1\le a\le n:d\mid ka\}\), \(B=\#\{1\le a\le n:d\mid(ka+j)\}\), and \(C=\mathbf1_{d\mid(kn+j)}\). Then
\[
e_d=A+B-2\lfloor n/d\rfloor-C,
\qquad A=\lfloor n/(d/g)\rfloor.
\tag{7}
\]
If \(g\ge2\), then \(A\ge2\lfloor n/d\rfloor\). Also \(B\ge C\), since whenever \(C=1\), the endpoint \(a=n\) is included in \(B\). Consequently \(e_d\ge0\).

Now suppose \(g=1\). There is a unique residue \(r\in\{1,\ldots,d\}\) for which \(kr+j\equiv0\pmod d\). Write \(n=td+s\), \(0\le s<d\). The first and third counts in (7) cancel, so
\[
e_d=\mathbf1_{r\le s}-\mathbf1_{r\equiv s\, (\mathrm{mod}\ d)}.
\tag{8}
\]
Indeed \(B=t+\mathbf1_{r\le s}\) with \(r=d\) representing the zero residue, and \(C=\mathbf1_{r\equiv s\, (\mathrm{mod}\ d)}\). If \(C=1\) and \(s>0\), then \(r=s\), so the first indicator in (8) is \(1\) and \(e_d=0\). If \(s=0\), then the first indicator is \(0\), and \(e_d=-1\) precisely when \(r=d\). These two equalities are equivalent to \(d\mid n\) and \(d\mid j\), because \(k\) is invertible modulo \(d\). Otherwise \(e_d\) equals \(0\) or \(1\).

Therefore the **complete negative cyclotomic spectrum** of (1) is
\[
e_d=-1\quad\Longleftrightarrow\quad
 d>1,\ d\mid\gcd(n,j),\ \gcd(d,k)=1.
\tag{9}
\]
No exponent is smaller than \(-1\). The divisors of \(m=\gcd(n,j)\) that are coprime to \(k\) are exactly the divisors of \(u\) from (2). Their cyclotomic product is (3). Because cyclotomic polynomials are distinct monic irreducibles in \(\mathbb Z[q]\), these negative factors cannot cancel against the numerator, while every other factor has nonnegative exponent. This proves the exact reduced denominator (3) and the equivalence (4). The sign is \(+1\), since the original ratio and its cyclotomic factorization have constant coefficient \(1\).

For \(n=j=p^a,k=p\), the integer \(u\) is \(1\), proving polynomiality; when \(a\ge2\), \(\gcd(n,j)=p^a\nmid p\), which disproves necessity of the originally proposed condition. Formula (5) follows either by applying (6) at the relevant divisors or by exact polynomial cancellation.

## Verification
Run `python3 verify.py` using Python 3 without external packages. The verifier checks the cyclotomic exponents directly from the defining product for all 4,500 triples \(1\le n\le20\), \(1\le k,j\le15\), across every divisor order up to \(kn+j\). It checks that the negative exponents are exactly those of (9), and that they form the complete denominator (3). It also compares independent exact rational evaluations of the defining product with its cyclotomic factorization at \(q=2,3\) for ten representative triples.

The successful local replay printed:
```
VERIFY_OK cases=4500 d_levels=1..kn+j polynomial=3473 nonpolynomial=1027
negative_cyclotomic_exponents=exact_all_cases independent_rational_evaluations=20 PASS
counterfamilies n=j=p^a k=p for a>=2: proven symbolically in RESULT.md
```
The unrestricted theorem is proved by (6)–(9); finite verification alone does not establish it.

## Relationship to prior work
Straub, Moll and Amdeberhan introduced this \(q\)-central binomial family and posed polynomiality of \(H_{n,k,j}(q)\) under the proposed condition \(\gcd(n,j)\mid k\) in Section 5 of their 2008 preprint. Straub repeated the proposed condition as Problem 14.5.2 in a 2012 dissertation. Their work supplies the family definition and the problem; it does not give the exact reduced denominator (3). The cyclotomic factorization method \(1-q^h=\prod_{d\mid h}\Phi_d(q)\) is classical and is not claimed as new. The claim here is its exact all-parameter application to (1), including the corrected radical criterion and infinite counterfamily.

## Limitations
The theorem establishes integrality over \(\mathbb Z[q]\), not coefficientwise nonnegativity, combinatorial interpretation, irreducibility of the numerator, or behavior when \(t\) in the two-variable function is independent of \(q\). A later unlocated proof of the same corrected characterization remains possible; independent historical priority verification has not been performed.

## References
1. A. Straub, V. H. Moll, and T. Amdeberhan, *The \(p\)-adic valuation of \(k\)-central binomial coefficients*, arXiv:0811.2028v1, publicly posted 2008-11-13, especially equations (4.4), (5.3), (5.7) and the problem after (5.7). https://arxiv.org/abs/0811.2028
2. A. Straub, *Arithmetic Aspects of Random Walks and Methods in Definite Integration*, PhD dissertation, Tulane University, 2012, Chapter 14, particularly equations (14.51)–(14.55) and Problem 14.5.2. https://arminstraub.com/downloads/pub/dissertation.pdf
