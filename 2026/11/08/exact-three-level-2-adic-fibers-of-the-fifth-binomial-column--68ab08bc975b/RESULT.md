# Exact three-level 2-adic fibers of the fifth binomial column

## Finding
For the integer-valued polynomial \(F(n)=\binom n5\), let \(P_k\) be its least positive period modulo \(2^k\), and let \(c_k(y)\) count the indices \(0\le n<P_k\) with \(F(n)\equiv y\pmod{2^k}\). For every \(k\ge1\),
\[
P_k=2^{k+2}.
\]
For \(k\ge3\) and all residues \(y\pmod{2^k}\),
\[
\boxed{c_k(y)=2+2\mathbf 1_{2\mid y}+8\mathbf 1_{8\mid y}.}
\]
The two initial distributions, in order of their residues, are \((c_1(0),c_1(1))=(6,2)\) and \((c_2(0),c_2(1),c_2(2),c_2(3))=(8,2,4,2)\). Consequently every residue is represented, but with exactly three distinct multiplicities \(2,4,12\) at every level \(k\ge3\).

Equivalently, if \(\mu\) denotes normalized Haar measure on \(\mathbb Z_2\), then the pushforward of \(\mu\) under the continuous extension of \(F\) has density relative to \(\mu\)
\[
\boxed{w(y)=\tfrac12+\tfrac12\mathbf1_{2\mathbb Z_2}(y)+2\mathbf1_{8\mathbb Z_2}(y).}
\]
Its three constant densities are \(\tfrac12\) for odd \(y\), \(1\) for even \(y\notin8\mathbb Z_2\), and \(3\) for \(y\in8\mathbb Z_2\).

## Assumptions and scope
The variable \(n\) ranges over nonnegative integers for finite congruences and over all \(\mathbb Z_2\) for the continuous polynomial extension. All \(k\) are integers \(k\ge1\); no odd-prime assertion is made. The convention \(\binom n5=0\) for \(0\le n<5\) agrees with its integer-valued polynomial expression \(n(n-1)(n-2)(n-3)(n-4)/120\). The count is for one **least** period, not for one residue system modulo \(2^k\).

## Proof
**1. Least period.** Put \(h=2^{k+2}\). The Vandermonde identity gives
\[
F(n+h)-F(n)=\sum_{j=1}^5\binom hj\binom n{5-j}.
\]
For \(1\le j\le5<h\) one has \(\nu_2(\binom hj)=k+2-\nu_2(j)\ge k\); hence \(h\) is a period modulo \(2^k\). Its half cannot be a period: setting \(h'=2^{k+1}\) and \(n=1\) gives
\[
F(1+h')-F(1)=\binom{h'}4+\binom{h'}5.
\]
For \(k\ge2\), the first term has valuation \(k-1\), while the second has valuation \(k+1\). For \(k=1\), they equal \(1\) and \(0\), respectively. Thus the difference always has valuation \(k-1\). Since the least positive period divides any period, it is exactly \(2^{k+2}\).

**2. Eight 2-adic isometric branches.** Write \(n=r+8t\) with \(r\in\{0,1,\ldots,7\}\) and \(t\in\mathbb Z_2\). Exact expansion of the degree-five polynomial yields
\[
F(r+8t)=F(r)+2^{d_r}(u_rt+2H_r(t)),
\]
where \(H_r(t)\in\mathbb Z_2[t]\) and each \(u_r\in\mathbb Z_2^\times\). The full branch table is:

| \(r\) | \(F(r)\) | \(d_r\) | \(u_r\) |
|---:|---:|---:|---:|
| 0 | 0 | 3 | \(1/5\) |
| 1 | 0 | 1 | \(-1/5\) |
| 2 | 0 | 2 | \(1/15\) |
| 3 | 0 | 1 | \(-1/5\) |
| 4 | 0 | 3 | \(1/5\) |
| 5 | 1 | 1 | \(137/15\) |
| 6 | 6 | 2 | \(87/5\) |
| 7 | 21 | 1 | \(459/5\) |

This is a finite **rational identity**, not a numerical pattern: substitute \(r+8t\) into \(\prod_{j=0}^4(n-j)/120\) and collect coefficients. The valuation lists of the coefficients of \(t,t^2,\ldots,t^5\) for \(r=0,1,2,3,4,5,6,7\) are, respectively,
\[
(3,4,6,10,12),\ (1,3,6,9,12),\ (2,\infty,6,\infty,12),\ (1,3,6,9,12),
\]
\[
(3,4,6,10,12),\ (1,3,6,9,12),\ (2,5,6,11,12),\ (1,3,6,9,12).
\]
Here \(\infty\) means a zero coefficient. These lists verify the integrality of \(H_r\) and the oddness of \(u_r\).

For any odd \(u\) and polynomial \(H\in\mathbb Z_2[t]\), the map \(g(t)=ut+2H(t)\) satisfies
\[
\nu_2(g(t)-g(s))=\nu_2(t-s).
\]
It induces a bijection modulo \(2\), and each solution modulo \(2^j\) lifts uniquely to a solution modulo \(2^{j+1}\), because \(g(t+2^j)\equiv g(t)+u2^j\pmod{2^{j+1}}\). Thus \(g\) is a bijective isometry on \(\mathbb Z_2\). Accordingly each branch \(r+8\mathbb Z_2\) maps onto exactly the coset \(F(r)+2^{d_r}\mathbb Z_2\), and its normalized Haar pushforward has constant density \(2^{d_r-3}\) on that coset.

**3. Sum of the eight branch measures.** The four branches \(r=1,3,5,7\) have \(d_r=1\), two mapping onto even and two onto odd targets; their combined density is \(\tfrac12\) everywhere. The two branches \(r=2,6\) have \(d_r=2\) and map onto \(0+4\mathbb Z_2\) and \(2+4\mathbb Z_2\), respectively; together they add \(\tfrac12\) on the even targets. The two branches \(r=0,4\) have \(d_r=3\) and both map onto \(8\mathbb Z_2\); together they add \(2\) there. This proves the stated density \(w\).

A single output class \(y+2^k\mathbb Z_2\) has target Haar mass \(2^{-k}\). By the density formula its preimage mass, for \(k\ge3\), is \(w(y)2^{-k}\). Since \(F\pmod{2^k}\) has period \(2^{k+2}\), that same mass equals \(c_k(y)/2^{k+2}\); multiplication by \(2^{k+2}\) gives the asserted fiber counts. For \(k=1,2\), aggregation of the cosets gives \((6,2)\) and \((8,2,4,2)\).

**4. Position among the first five columns.** The same exact polynomial expansion on eight input classes proves the following lower-column facts. For \(\binom n1\), all eight branches have depth \(3\), with distinct images modulo eight. For \(\binom n2\), all eight branches have depth \(2\), and their images modulo four are \((0,0,1,3,2,2,3,1)\): each target class occurs twice. For \(\binom n4\), all eight branches have depth \(1\), and their images modulo two are \((0,0,0,0,1,1,1,1)\): each target parity occurs four times. In each case, higher-degree coefficients have strictly higher valuation than the first coefficient, so the branch-isometry proof applies and the pushforward is uniform Haar measure on \(\mathbb Z_2\).

For \(\binom n3\), the four odd-input branches have depth \(2\), with images \((0,1,2,3)\) modulo four, providing density \(\tfrac12\) on every target. The four even-input branches have depth \(3\), with images \((0,0,4,4)\) modulo eight, adding density \(2\) on targets divisible by four. Thus its density is \(\tfrac12+2\mathbf1_{4\mathbb Z_2}\), with just two distinct levels. Therefore the fifth column is the **first positive fixed lower binomial index with three distinct dyadic output-density levels**.

## Verification
Run `python3 verify.py`. It checks the eight branch expansions with exact fractions, including every coefficient's 2-adic valuation, then counts the complete least-period fibers for all \(1\le k\le12\). It independently tests the failure of half-periods and the earlier four columns. All arithmetic is exact. The program supplies finite corroboration; the preceding algebraic proof establishes the formulas for every \(k\).

## Relationship to prior work
Sun and Zhang prove that every positive fixed binomial column is dense in \(\mathbb Z_2\), specifically Corollary 1.2 of *Binomial coefficients and the ring of p-adic integers* (arXiv:0812.3089). Their image-surjectivity result does not specify output-fiber multiplicities. **The least-period formula is already recorded in OEIS A349593 and A385557; it is included and proved here only to normalize the new fiber counts, not as an originality claim.** Barat and Grabner's *Distribution of binomial coefficients and digital functions* studies global distributions over the triangular family of pairs \((n,j)\) and fixed row valuations; its asymptotic triangular results do not give the exact fixed-fifth-column law above. The new contribution claimed is the complete three-level fiber law and its structural eight-branch derivation, not the known period or image-surjectivity results.

## Limitations
The theorem covers the fifth lower index and powers of two; it does not provide a classification at odd primes or higher fixed lower indices. The originality comparison was made against accessible primary literature and relevant indexed mathematics records; an unindexed earlier equivalent formula remains possible. The review is not independent mathematical validation.

## References
- Z.-W. Sun and W. Zhang, *Binomial coefficients and the ring of p-adic integers*, arXiv:0812.3089, first submitted 2008-12-16. https://arxiv.org/abs/0812.3089 ; full text: https://arxiv.org/html/0812.3089v5 .
- G. Barat and P. J. Grabner, *Distribution of binomial coefficients and digital functions*, *J. London Math. Soc.* 64 (2001), 523–547. Author-hosted full text: https://www.math.tugraz.at/~grabner/Publications/Binomial.pdf .
- OEIS A349593 and A385557, tables of minimal binomial-column periods, https://oeis.org/A349593 and https://oeis.org/A385557 ; the latter records the period \(2^{k+2}\) for the fifth column.
