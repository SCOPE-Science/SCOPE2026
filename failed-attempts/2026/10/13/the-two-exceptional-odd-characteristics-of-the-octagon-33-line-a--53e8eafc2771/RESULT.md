# The two exceptional odd characteristics of the octagon 33-line arrangement

## Finding

Let \(\rho\) satisfy \(\rho^2=2\), and let \(\mathcal C_8\) be the eight-line projective arrangement over \(\mathbb Q(\rho)\) specified in the next section. Let \(\mathcal O_{33}\) be the collection of all projective lines passing through at least three of the 28 pairwise intersection points of \(\mathcal C_8\). This is the 33-line arrangement introduced by Pokora and Roulleau.

For every **odd prime** \(p\) and every choice of a root \(\bar\rho\in\overline{\mathbb F}_p\) of \(T^2-2\), reduce the 33 normalized integral line equations as defined below. The reductions remain **33 distinct lines**. Writing \(n_m(p)\) for the number of geometric points incident with exactly \(m\) distinct reduced lines, their complete multiplicity census is:

| Odd characteristic | \(n_2\) | \(n_3\) | \(n_4\) | \(n_5\) | \(n_8\) | Total intersection points |
|---|---:|---:|---:|---:|---:|---:|
| \(p\notin\{3,7\}\) | 108 | 40 | 0 | 16 | 5 | 169 |
| \(p=3\) | 12 | 40 | 16 | 16 | 5 | 89 |
| \(p=7\) | 4 | 0 | 24 | 24 | 5 | 57 |

All multiplicities absent from the table are zero. **Among odd primes, the intersection lattice of this integral model is preserved exactly when \(p\notin\{3,7\}\).** For \(p=3\) the root lies in \(\mathbb F_9\), and for \(p=7\) both choices \(\bar\rho=3,4\in\mathbb F_7\) give the same census.

## Assumptions and scope

Work with homogeneous coordinates \([x:y:z]\) on \(\mathbb P^2\). The eight members of \(\mathcal C_8\) are the vanishing loci of the following forms, all over \(K=\mathbb Q(\rho)\):

\[
\begin{aligned}
&x+(\rho-1)y-z, &&x+(\rho+1)y-(\rho+1)z,\\
&x-(\rho+1)y+(\rho+1)z, &&x+(1-\rho)y+z,\\
&x+(\rho-1)y+z, &&x+(\rho+1)y+(\rho+1)z,\\
&x-(\rho+1)y-(\rho+1)z, &&x+(1-\rho)y-z.
\end{aligned}
\]

Take all 28 pair intersections of these forms in characteristic zero. For each pair of distinct such points, take their joining projective line. Retain each line if it contains at least three of the 28 points, and remove duplicates. This constructs precisely 33 lines. To define the integral specialization unambiguously, normalize the coefficient vector of each retained line by dividing by its first nonzero coordinate in \(K\). In this particular construction, all normalized coefficients lie in \(\mathbb Z[\rho]\); no denominators occur. Reduction means coefficient-wise application of \(\rho\mapsto\bar\rho\) to those specific 33 normalized equations, **not** reapplication of the point-line operator to the reduced eight-line seed.

The claim concerns geometric intersection points over an algebraic closure, even when \(\rho\) is not in the prime field. The ramified characteristic \(2\) is excluded. Neither reduced-curve freeness nor the counts of prime-field-rational intersection points are asserted.

## Proof

Represent an element of \(\mathbb Z[\rho]\) by \((a,b)\), meaning \(a+b\rho\), with multiplication
\[
(a,b)(c,d)=(ac+2bd,ad+bc).
\]
Cross products of line coefficient vectors give pairwise intersections; cross products of two point vectors give their joining line. Exact normalization and zero tests reconstruct all 28 seed intersections and all 33 selected lines. Incidence counting over \(K\) yields the published characteristic-zero census \((n_2,n_3,n_5,n_8)=(108,40,16,5)\).

Now take **all** \(\binom{33}{3}=5456\) unordered triples of normalized line coefficient vectors, and evaluate their \(3\times3\) determinants in \(\mathbb Z[\rho]\). Exactly 480 determinants are zero. For each of the 4,976 nonzero determinants \(d=a+b\rho\), calculate the integer field norm \(N(d)=a^2-2b^2\). The **complete set** of absolute nonzero norms is
\[
\{1,2,4,8,14,16,28,32,36,56,64,72\}.
\]
Every prime divisor of every such norm is in \(\{2,3,7\}\). For any odd \(p\notin\{3,7\}\), neither embedding \(\mathbb Z[\rho]\to\overline{\mathbb F}_p\) can send a nonzero determinant to zero: a vanishing determinant would force its integer norm to vanish modulo \(p\). Determinants already equal to zero remain zero. Thus the rank-three dependence relation on every triple is unchanged. In particular, there can be no coincident line pair, and the entire rank-three matroid, hence the intersection lattice, is unchanged.

For the remaining odd primes, compute exactly in the fields \(\mathbb F_3[t]/(t^2-2)=\mathbb F_9\) and \(\mathbb F_7\) with \(t=3\) or \(t=4\). Normalize every nonzero pairwise cross product and group all \(\binom{33}{2}=528\) line pairs by their projective intersection. Each group of \(\binom m2\) pairs corresponds to exactly one \(m\)-fold point because the 33 reduced lines are pairwise distinct in each of these three calculations. The resulting multiplicity histograms are exactly the two exceptional rows of the table. As an independent consistency check, every row satisfies
\[
\sum_{m\ge2}\binom m2 n_m(p)=528.
\]
The exceptional rows differ from the characteristic-zero row, proving that both odd primes are genuinely bad. The preceding norm argument excludes all others. This is an exhaustive finite computation in explicit exact rings, not an inference from finitely many sampled primes.

## Verification

Execute `python3 VERIFY_O33.py` using Python 3 and the standard library only. The program regenerates the 33 lines from the eight seed forms, checks that every normalized coefficient is integral, reproduces the characteristic-zero intersection multiplicities, exhausts every triple determinant, asserts the full norm support and the 480 zero triple determinants, and computes both characteristic-three and characteristic-seven incidence tables in exact finite fields. It also checks several good-characteristic samples, but those samples play **no role** in the all-prime proof. The determinant-norm certificate is what establishes the uniform assertion.

## Relationship to prior work

Pokora and Roulleau, *Construction of free arrangements using point-line operators*, arXiv:2403.20024v1 (29 March 2024), introduce the regular-octagon closure, give its defining equations, and establish that it is a rigid free arrangement of 33 complex lines with multiplicities \(108,40,16,5\) at \(2,3,5,8\)-fold points. The present statement uses their construction and does **not** re-present the characteristic-zero freeness or counts as new. The additional assertion is the complete **odd-characteristic specialization**: precisely two exceptional primes and their full new intersection multiplicities. Their original theorem concerns characteristic zero and does not state these special-fiber counts.

## Limitations

The integral specialization is fixed by the above normalized equations. An arbitrarily chosen projectively equivalent integral model may have a different reduction at a prime where the coordinate change ceases to be invertible. Characteristic \(2\) is outside the theorem because the quadratic coefficient ring ramifies there; the 33 lines need not remain distinct on that fiber. No claim is made that the characteristic-\(3\) or characteristic-\(7\) arrangements are free, or that all their geometric intersection points are rational over \(\mathbb F_p\). The calculation does not settle whether another reference contains an unindexed equivalent arithmetic classification.

## References

1. P. Pokora and X. Roulleau, *Construction of free arrangements using point-line operators*, arXiv:2403.20024v1 (29 March 2024), Theorem B and its proof, https://arxiv.org/html/2403.20024v1.
2. P. Pokora and X. Roulleau, same work, arXiv:2403.20024v3 (16 September 2026), §2, https://arxiv.org/html/2403.20024.
