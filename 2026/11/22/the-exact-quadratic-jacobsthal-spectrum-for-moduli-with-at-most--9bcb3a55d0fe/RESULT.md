# The exact quadratic Jacobsthal spectrum for moduli with at most two prime factors

## Finding

For each integer \(N\ge2\), let
\[
 j_{T^2}(N)=\max\{m\ge0:\text{some positive integer }x\text{ has }\gcd(x+i^2,N)>1\text{ for all }1\le i\le m\}.
\]
Write \(C_k(N)\) for the number of classes \(x\bmod N\) satisfying these conditions for \(1\le i\le k\), with \(C_0(N)=N\). If \(N\) has one or two distinct prime factors and \(R=\operatorname{rad}(N)\), then for all \(k\ge0\),
\[
 C_k(N)=(N/R)C_k(R).
\]
For a prime radical \(p\), the counts are \(C_1(p)=1\), \(C_2(p)=\mathbf1_{p=3}\), and \(C_k(p)=0\) for \(k\ge3\). For a two-prime radical \(pq\) with \(p<q\),
\[
\begin{aligned}
C_1(pq)&=p+q-1,\\
C_2(pq)&=\begin{cases}q,&p=3,\\2,&p\ne3,\end{cases}\\
C_3(pq)&=\mathbf1_{p\in\{2,3,5\}},\\
C_4(pq)=C_5(pq)&=\mathbf1_{3\mid pq},\\
C_k(pq)&=0\qquad(k\ge6).
\end{aligned}
\]
Thus \(j_{T^2}(N)=2\) for \(R=3\) and \(1\) for other prime radicals. For \(R=pq\) it is \(5\) if \(3\mid pq\), \(3\) if \(p\in\{2,5\}\) and \(q>3\), and \(2\) otherwise. Exactly \(C_k(N)-C_{k+1}(N)\) classes have an initial run of exactly \(k\) non-coprime shifted squares. For each two-prime radical supporting at least three terms, exactly one class survives the first three indices, and the unique longest-run class modulo that radical is the same survivor.

## Assumptions and scope

All primes are rational primes. The radical is the product of the distinct prime divisors of \(N\). Indices start at \(1\), and \(x\) is fixed throughout a run. Every residue class has a positive representative. Prime powers are allowed; no statement is made for radicals with three or more prime divisors. The invariant and its indexing agree with Kalmynin and Konyagin's definition.

## Proof

**Radical reduction.** For every integer \(z\), \(\gcd(z,N)>1\) if and only if \(\gcd(z,R)>1\). Each survivor modulo \(R\) has exactly \(N/R\) lifts modulo \(N\).

**Prime-local fibers.** A residue \(x\bmod\ell\) covers precisely the indices with \(i^2\equiv -x\pmod\ell\). The fibers among the first six indices are

| Prime | Equal-square fibers among indices \(1,\ldots,6\) |
|---|---|
| \(2\) | \(\{1,3,5\},\ \{2,4,6\}\) |
| \(3\) | \(\{1,2,4,5\},\ \{3,6\}\) |
| \(5\) | \(\{1,4,6\},\ \{2,3\},\ \{5\}\) |

For every \(\ell\ge7\), the first six indices are distinct modulo \(\ell\), so a fiber has at most two indices by the degree-two bound over a field. Among the first three indices, the square differences have absolute values \(3,5,8\), so their squares are distinct modulo every prime \(\ell\ge7\).

**One prime.** The first index forces \(x\equiv-1\pmod p\). It also covers index \(2\) if and only if \(p=3\), and cannot then also cover index \(3\) because \(9-1=8\).

**Two primes, first two indices.** By CRT the pairs covering index \(1\) form a union of sets of sizes \(q\) and \(p\) that intersect in one pair. For index \(2\) as well, if neither prime is \(3\), one prime must cover index \(1\) and the other index \(2\). The two assignments give distinct CRT pairs. If one prime is \(3\), covering both indices forces \(x\equiv-1\pmod3\): otherwise the other prime would have to cover both, which is impossible. Conversely this congruence covers both, leaving the residue modulo the other prime arbitrary. For \(p=3\) this gives \(q\) pairs, and for \(q=3\) it gives \(p=2\) pairs.

**Third index.** If \(p\ge7\), no fiber covers two among the first three, so no pair of fibers covers all three. With \(p=2\), indices \(1,3\) cannot both be covered by the odd prime \(q\) since their square difference is \(8\). At least one must be covered by \(2\), which forces the odd-index fiber and then forces the \(q\)-residue by index \(2\). This works also for \(q=3\) and \(q=5\). With \(p=3<q\), prime \(3\) can cover the pair \(\{1,2\}\). This is forced for \(q\ge7\), when the other prime can cover only one index. When \(q=5\), covering \(\{2,3\}\) by \(5\) still requires \(3\) to cover index \(1\), which forces its same fiber \(\{1,2\}\); if \(3\) covers only index \(3\), \(5\) cannot cover \(\{1,2\}\). Thus the residue mod \(3\) is forced in every case, and index \(3\) determines the unique \(q\)-residue. With \(p=5<q\), the pair \(\{2,3\}\) must be covered by \(5\), leaving index \(1\) to force the \(q\)-residue. Each forced pair exists by CRT.

**Fourth and fifth indices.** With \(p=2,q>3\), the two possible nonempty \(2\)-fibers among the first four are \(\{1,3\}\) and \(\{2,4\}\); their uncovered pairs have square differences \(12\) and \(8\), respectively, so no such \(q\) can cover either pair. With \(p=5,q\ge7\), the fibers among the first four are \(\{1,4\}\) and \(\{2,3\}\), whose respective uncovered pairs have square differences \(5\) and \(15\); again neither can be covered by \(q\). When \(p=3<q\), the unique class surviving three indices has \(x\equiv-1\pmod3\) and \(x\equiv-9\pmod q\). Its \(3\)-residue covers indices \(4,5\). When \((p,q)=(2,3)\), the unique third-index survivor is \(x\equiv5\pmod6\), which also covers indices \(4,5\). These exhaust the cases by monotonicity.

**Sixth index.** For \(p=3<q\), the unique five-index survivor has \(x+36\equiv2\pmod3\) and \(x+36\equiv27\pmod q\), both nonzero. For \(R=6\), the unique survivor gives \(x+36\equiv5\pmod6\), also coprime to \(R\). Consequently no residue survives six indices and none can survive more. The stated maxima and exact-length counts follow from the nested survivor sets.

## Verification

The supplied standard-library script `verify_quadratic_jacobsthal.py` documents direct gcd enumeration over the 1,059 eligible moduli up to 1,600, and comparison with CRT-local cover enumeration over the 210 distinct prime pairs \(p<q<79\). The frozen verification record reports agreement for the stated counts. The finite checks do not substitute for the proof covering all primes and exponents.

## Relationship to prior work

Kalmynin and Konyagin introduce the polynomial analogue of the Jacobsthal function. Their Theorem 1 bounds \(j_f(P(y))\) below along primorials, and Theorem 3 evaluates the average maximal local-fiber size for monomials. Neither result gives the exact initial-run residue counts for every radical with one or two prime divisors. The contribution here is that complete low-support classification, including the initial-run frequency distribution and uniqueness of the long survivor. This comparison does not establish worldwide priority.

## Limitations

The theorem concerns initial shifts \(x+i^2\) for \(i=1,2,\ldots\), not maximal runs starting at arbitrary index positions. It neither treats radicals with three or more prime divisors nor other polynomials.

## Reference

A. Kalmynin and S. Konyagin, *A polynomial analogue of Jacobsthal function*, [arXiv:2302.00459](https://arxiv.org/abs/2302.00459), first posted 1 February 2023; *Izvestiya: Mathematics* **88** (2024), 225–235, [DOI: 10.4213/im9467e](https://doi.org/10.4213/im9467e).
