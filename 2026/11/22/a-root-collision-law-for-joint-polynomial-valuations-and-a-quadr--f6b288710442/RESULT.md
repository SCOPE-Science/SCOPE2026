# A root-collision law for joint polynomial valuations and a quadratic covariance trichotomy

## Finding
Let \(p\) be an odd prime, and let \(f,g\in\mathbb Z[X]\) be nonzero polynomials. Assume **each root of each reduced polynomial in \(\mathbb F_p\) is simple** (the reduced polynomial need not split). Let \(r_f,r_g\) be the numbers of those roots. For every common residue root \(a\), denote its unique Hensel lifts in \(\mathbb Z_p\) by \(\alpha_a\) for \(f\) and \(\beta_a\) for \(g\), and put
\[
 d_a=\nu_p(\alpha_a-\beta_a)\in\{1,2,\ldots\}\cup\{\infty\}.
\]
Here \(p^{-\infty}=0\). For Haar-uniform \(U\in\mathbb Z_p\), put \(X=\nu_p(f(U))\) and \(Y=\nu_p(g(U))\). Both are finite almost surely.

**Exact joint law.** For \(|z|,|w|\le1\),
\[
\begin{aligned}
\mathbb E[z^Xw^Y]
&=1+\frac{r_f(z-1)}{p-z}+\frac{r_g(w-1)}{p-w}\\
&\quad +(z-1)(w-1)\sum_{a\in T}
\frac{1-(zw/p)^{d_a}}{p-zw}
\left(1+\frac{z}{p-z}+\frac{w}{p-w}\right),
\end{aligned}
\]
where \(T\) is the set of common residue roots. Interpret \((zw/p)^\infty\) as zero. This determines every joint valuation frequency. In particular,
\[
\boxed{\operatorname{Cov}(X,Y)=
\frac{(p+1)\sum_{a\in T}(1-p^{-d_a})-r_fr_g}{(p-1)^2}.}
\]

**Sharp sign consequence for two quadratics.** If both reduced polynomials have exactly two distinct roots, let \(r=|T|\). When \(r=0\), the covariance is strictly negative; when \(r=2\), it is strictly positive. When \(r=1\), the covariance is strictly positive for every \(p\ge5\). For \(p=3\) and \(r=1\), it is strictly negative if the two lifted roots are distinct, and zero exactly when those lifts coincide. These alternatives exhaust all such pairs of quadratic polynomials.

## Assumptions and scope
The prime is any odd prime, and polynomial coefficients are ordinary integers. The requirement is simplicity at **all actual roots modulo \(p\)**, not squarefreeness or complete splitting of the entire polynomial modulo \(p\). It permits irreducible polynomials over \(\mathbb Q\) that split at \(p\), as well as polynomials with no root modulo \(p\). Polynomials identically zero modulo \(p\) are excluded because their residue roots are not simple. A valuation of zero is infinite; this occurs only on a finite Haar-null set and hence does not affect the distribution.

For a finite exact statement, put \(X_k(n)=\min(k,\nu_p(f(n)))\) and \(Y_k(n)=\min(k,\nu_p(g(n)))\) for \(n\) modulo \(p^k\). For all \(1\le t,s\le k\), set \(N_m=\#\{a\in T:d_a\ge m\}\). Then the number of residue indices satisfying both inequalities is **exactly**
\[
\boxed{\#\{n\bmod p^k:X_k(n)\ge t,\ Y_k(n)\ge s\}
=N_{\min(t,s)}p^{k-\max(t,s)}.}
\]
The marginals are exactly \(r_fp^{k-t}\) and \(r_gp^{k-s}\). All single pair frequencies at finite precision follow by taking adjacent differences of these tail counts. For any fixed pair of finite valuations, the corresponding ordinary natural density among nonnegative integers equals the stated Haar probability.

## Proof
**1. Valuation on each simple-root disk.** For every root \(a\) of \(f\) modulo \(p\), Hensel's lemma gives a unique \(\alpha_a\in\mathbb Z_p\) reducing to \(a\). The polynomial identity \(f(x)=(x-\alpha_a)u_a(x)\) over \(\mathbb Z_p[X]\) holds, with \(u_a(\alpha_a)=f'(\alpha_a)\) a unit. For every \(x\equiv a\pmod p\), \(u_a(x)\) is a unit, so \(\nu_p(f(x))=\nu_p(x-\alpha_a)\). For every other residue class, \(f(x)\) is a unit. The same holds for \(g\). Therefore \(\Pr(X\ge t)=r_fp^{-t}\), and similarly for \(Y\), for every \(t\ge1\).

**2. Intersection of the two root trees.** For \(t,s\ge1\), a point where \(X\ge t,Y\ge s\) belongs to a ball \(\alpha_a+p^t\mathbb Z_p\) and a ball \(\beta_b+p^s\mathbb Z_p\). Such balls intersect if and only if their centers agree modulo \(p^{\min(t,s)}\); when they do, the intersection is one ball of measure \(p^{-\max(t,s)}\). The two roots must have the same residue modulo \(p\), and each residue identifies at most one root of each polynomial. Consequently
\[
\Pr(X\ge t,Y\ge s)=p^{-\max(t,s)}N_{\min(t,s)}.
\]
The argument is exact modulo \(p^k\) as well: the intersection comprises \(p^{k-\max(t,s)}\) residue classes. This proves the claimed finite-depth formula.

**3. Joint generating function.** For each finite nonnegative integer \(h\), use \(z^h=1+(z-1)\sum_{t=1}^h z^{t-1}\). Multiplying the identities for \(X,Y\) and taking expectations expresses the joint generating function in terms of the marginal and mixed tails. Absolute convergence for \(|z|,|w|\le1\) follows from the geometric tail bounds. Each common root pair contributes, for \(d=d_a\),
\[
\begin{aligned}
H_d(z,w)&=\sum_{\substack{t,s\ge1\\\min(t,s)\le d}}
 z^{t-1}w^{s-1}p^{-\max(t,s)}\\
&=\sum_{m=1}^{d}\frac{(zw)^{m-1}}{p^m}
\left(1+\frac{z}{p-z}+\frac{w}{p-w}\right)\\
&=\frac{1-(zw/p)^d}{p-zw}
\left(1+\frac{z}{p-z}+\frac{w}{p-w}\right).
\end{aligned}
\]
The same identity holds for \(d=\infty\) by a convergent geometric series. Inserting the marginal tails and these contributions yields the displayed joint law.

**4. Covariance and quadratic signs.** The tail sums give \(\mathbb EX=r_f/(p-1)\) and \(\mathbb EY=r_g/(p-1)\). Grouping mixed tails by \(m=\min(t,s)\), the diagonal contributes \(p^{-m}\) and the two off-diagonal strips contribute \(2p^{-m}/(p-1)\). Thus
\[
\mathbb E[XY]=\frac{p+1}{p-1}\sum_{m\ge1}\frac{N_m}{p^m}
=\frac{p+1}{(p-1)^2}\sum_{a\in T}(1-p^{-d_a}),
\]
and subtraction proves the covariance identity. In the quadratic case \(r_f=r_g=2\), the numerator is \((p+1)\sum_{a\in T}(1-p^{-d_a})-4\). With zero matches it equals \(-4\). With two matches it is at least \(2(p+1)(1-1/p)-4>0\) for every odd prime. With one match it equals \(-4\cdot3^{-d_a}\) at \(p=3\), and is at least \((p+1)(1-1/p)-4=(p^2-4p-1)/p>0\) for \(p\ge5\). This proves every case, including equality when \(p=3,d_a=\infty\).

## Verification
The standalone file `verify.py` recomputes simple roots modulo consecutive prime powers without using the above generating-function formula, enumerates all indices modulo each tested power, and checks every finite-depth marginal, mixed tail, and exact cross moment using rational arithmetic. Eleven tests at primes \(3,5,7\), to depths four through six, include pairs of quadratics irreducible over \(\mathbb Q\), no common roots, one or two common residue roots, separation depths one and two, and exact coincident lifts. All 1,228 exact identities passed. These checks test the finite instances; the unrestricted-prime, all-depth statements are established by the proof above, not by enumeration.

For concrete irreducible examples: at \(p=3\), \(f(x)=x^2-x+3\) and \(g(x)=x^2+x+3\) have one common root class with separation depth one, giving covariance \(-1/3\); at \(p=5\), \(f(x)=x^2-x+5\) and \(g(x)=x^2-2x+5\) similarly give \(1/20\); at \(p=7\), \(f(x)=x^2-2\) and \(g(x)=x^2-44\) have two matched classes of depth one, giving \(17/63\).

## Relationship to prior work
Snyder's *Products of p-Adic Valuation Trees* (first posted 22 August 2023) describes valuation trees of products of rationally split polynomials and certain higher-degree products. It provides a natural starting point for comparing how two individual valuation trees overlap, but does not state their joint Haar law, the complete finite-depth cross-tail count, or the covariance sign trichotomy. The present theorem also covers polynomials irreducible over \(\mathbb Q\) whose residue roots are simple, a case outside Snyder's rationally split complete-tree theorem.

Boultinghouse et al.'s *The p-Adic Valuation Trees for Quadratic Polynomials for Odd Primes* (first posted 28 September 2023) classifies individual quadratic valuation trees by discriminant. Medina, Moll and Rowland's *Periodicity in the p-adic Valuation of a Polynomial* (2015) gives foundational single-polynomial periodicity and lifting results. None of their inspected statements specifies the joint frequencies or sign behavior for distinct input polynomials. The present proof relies on standard Hensel lifting and ball intersections, and does **not** claim those ingredients as original.

## Limitations
The simple-residue-root hypothesis is essential to this formula: at a multiple root, valuations can acquire nonunit local factors, and an identical pair of root-ball count formulas need not hold. The exact law is a limiting distribution over ordinary integers and an exact count on full prime-power blocks, not a uniform error bound for every finite prefix length. The theorem does not classify arbitrary pairs with singular reductions. Historical priority beyond the inspected sources is not certified; the general result may admit an equivalent formulation in local zeta-function or resultant literature.

## References
1. D. Snyder, *Products of p-Adic Valuation Trees*, arXiv:2308.11718, v1 dated 2023-08-22, https://arxiv.org/abs/2308.11718 .
2. W. Boultinghouse, E. Hammett, S. Hu, O. Kozhushkina, R. Snyder, J. Trulen, *The p-Adic Valuation Trees for Quadratic Polynomials for Odd Primes*, arXiv:2309.16637, v1 dated 2023-09-28, https://arxiv.org/abs/2309.16637 .
3. L. A. Medina, V. H. Moll, E. Rowland, *Periodicity in the p-adic Valuation of a Polynomial*, arXiv:1505.02302, first posted 2015-05-09, https://arxiv.org/abs/1505.02302 .
