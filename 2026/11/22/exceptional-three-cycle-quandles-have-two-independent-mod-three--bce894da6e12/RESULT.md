# Exceptional three-cycle quandles have two independent mod-three second-homology classes

## Finding

Let \(Q_n\) be the conjugacy quandle of all three-cycles in the symmetric group on \(n\) letters, with the right-quandle operation \(x*y=y^{-1}xy\). For \(n=6,7\), the **normalized quandle chain complex** has the following exact second homology over the two small prime fields:

\[
\begin{array}{c|cc}
 & H_2^Q(Q_n;\mathbb F_2)&H_2^Q(Q_n;\mathbb F_3)\\\hline
n=6&\mathbb F_2&\mathbb F_3^2\\
n=7&0&\mathbb F_3^2
\end{array}
\]

In particular, the integral second quandle homology of either exceptional quandle has **exactly two cyclic elementary divisors divisible by three**, while the number of cyclic elementary divisors divisible by two is **one at six letters and zero at seven letters**. These are statements about primary-generator counts, not claims concerning their exponents or the full integral group.

## Assumptions and scope

The underlying set consists of all permutations of cycle type \((3,1^{n-3})\), so its size is \(m=n(n-1)(n-2)/3\). The right-conjugation convention is used throughout; the inversion map identifies it with the transposed left-conjugation convention \(a\triangleright b=aba^{-1}\) used in the motivating reference. Only the two specified values \(n=6,7\), coefficients \(\mathbb F_2\) and \(\mathbb F_3\), and degree-two normalized quandle homology are claimed.

## Proof

For a quandle \(Q\), the normalized degree-one, degree-two and degree-three chain groups over a field \(F\) have bases \([x]\), \([x,y]\) for \(x\ne y\), and \([x,y,z]\) for \(x\ne y\) and \(y\ne z\), respectively. The relevant differentials are

\[
\partial_2[x,y]=[x]-[x*y],
\]

\[
\partial_3[x,y,z]=[x,z]-[x*y,z]-[x,y]+[x*z,y*z],
\]

where a pair with equal entries is zero. The three-cycles form a connected conjugacy class in \(A_n\) for both specified \(n\); thus \(\operatorname{rank}\partial_2=m-1\). This is also checked constructively in the attached program by iterating its conjugation table from one element.

An exhaustive, integer-defined enumeration of the 3-cycles, the normalized pairs and all normalized triples produces the matrix of \(\partial_3\). Exact Gaussian elimination in \(\mathbb F_2\) and \(\mathbb F_3\) gives

| \(n\) | \(m\) | \(\dim C_2\) | \(\dim C_3\) | \(\operatorname{rank}\partial_2\) | \(\operatorname{rank}_{\mathbb F_2}\partial_3\) | \(\operatorname{rank}_{\mathbb F_3}\partial_3\) |
|:--:|--:|--:|--:|--:|--:|--:|
| 6 | 40 | 1,560 | 60,840 | 39 | 1,520 | 1,519 |
| 7 | 70 | 4,830 | 333,270 | 69 | 4,761 | 4,759 |

For reproducibility, the attached `check_exceptional.py` constructs every permutation as an explicit image tuple, calculates every conjugate by composition and inverse permutations, and enumerates every triple. For \(\mathbb F_2\), each column is represented as a binary integer, and exact elimination uses XOR. For \(\mathbb F_3\), two disjoint binary integers encode the coefficient-one and coefficient-two entries in a column. The included `plus_trinary` routine implements addition modulo three via the disjoint-support truth table, and the pivot loop performs ordinary exact field elimination. A new pivot is retained only when the reduced column is nonzero; therefore the final pivot count **equals the rank of the entire enumerated matrix**. This is a terminating exhaustive finite-rank proof, not sampling, numerical approximation or an inference from incomplete enumeration.

The checker also verifies the right self-distributive law, the connectedness needed for \(\operatorname{rank}\partial_2\), and the integer identity \(\partial_2\partial_3=0\) for every normalized triple. It repeats the elimination using reversed degree-two basis order for all stated characteristic-two calculations and for the five- and six-letter characteristic-three calculations. As a control, for \(n=5\) it reproduces the two one-dimensional coefficient homologies implied by the previously established integral group \(\mathbb Z/3\oplus\mathbb Z/2\).

It follows from \(H_2=\ker\partial_2/\operatorname{im}\partial_3\) that the dimensions are \(\dim C_2-(m-1)-\operatorname{rank}\partial_3\), which are exactly the four values asserted. For a finite connected injective quandle the integral degree-two homology is finite, as follows from the finite-representation-group description in the primary reference. Also \(H_1^Q(Q_n;\mathbb Z)\cong\mathbb Z\). The universal coefficient theorem has no contribution from \(\operatorname{Tor}(H_1,\mathbb F_p)\), so the mod-prime dimensions equal the numbers of primary invariant factors divisible by that prime. This proves the integral primary-generator consequences without asserting the exponents.

## Verification

Run `python3 check_exceptional.py` from the directory containing that standalone script. No optional dependencies or internet access are required. The script raises an exception if any structural identity, exhaustive boundary check, expected modular rank, or secondary pivot-order check disagrees. A complete successful output is recorded in `CHECK_OUTPUT.txt`. All 7,220 five-letter, 60,840 six-letter and 333,270 seven-letter normalized triples enter the rank calculation for each prime. The five-letter control is *not* a new finding.

## Relationship to prior work

Maassarani, *Second homology of some quandles* (first public 11 November 2026, arXiv:2611.15826v1), determines the integral second homology for connected odd-cycle quandles **subject to** \(n\ne6,7\). The introduction and Section 2.3 explicitly exclude those two symmetric-group degrees because of their exceptional covering-group behavior; consequently that theorem does not imply any of the four assertions here. Substituting those degrees formally into the inapplicable generic formula suggests the same small-prime dimensions but is not a proof of them.

Bakshi–Ibarra–Mukherjee–Nosaka–Przytycki, *Schur Multipliers and Second Quandle Homology* (arXiv:1812.04704), studies related structures and Alexander quandles, but no covering calculation of these particular exceptional quandle dimensions was identified in the inspected material. The Rig finite-quandle database contains conjugacy quandles of size 40 in its size range, but its ability to calculate quandle homology is not itself a published table of the four dimensions; the 70-element quandle is outside the database's stated below-48 census. Equivalent unpublished calculations remain possible.

## Limitations

Only the mod-two and mod-three coefficient homology groups, and consequently the corresponding integral primary-generator counts, are established. The orders of the torsion factors, all other torsion primes, the full integral invariant-factor decompositions, the cohomology rings and all higher quandle homology remain unclassified by this result. All computations are exact but have not been independently audited. Priority against unpublished datasets and unindexed work is unresolved.

## References

- M. Maassarani, *Second homology of some quandles*, arXiv:2611.15826v1, 11 November 2026. https://arxiv.org/html/2611.15826v1
- R. P. Bakshi, D. Ibarra, S. Mukherjee, T. Nosaka and J. H. Przytycki, *Schur Multipliers and Second Quandle Homology*, arXiv:1812.04704v1, 11 December 2018. https://arxiv.org/abs/1812.04704
- Rig package for GAP, *Racks, quandles, Nichols algebras*, finite-quandle census and homology facilities. https://github.com/gap-packages/rig
