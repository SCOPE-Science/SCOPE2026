# Higher support geometry and local repair of a ternary LCD code

## Finding

Let \(C\subseteq\mathbb F_3^{25}\) be the row space of the five-by-twenty-five matrix \(G\) specified below. The exact generalized Hamming-weight hierarchy is
\[
(d_1(C),d_2(C),d_3(C),d_4(C),d_5(C))=(14,19,22,24,25).
\]
The full Hamming weight enumerator is
\[
\begin{aligned}
W_C(z)={}&1+22z^{14}+56z^{15}+62z^{16}+32z^{17}+20z^{18}\\
&+24z^{19}+12z^{20}+4z^{21}+4z^{22}+6z^{23}.
\end{aligned}
\]

For each \(r\), let \(H_r(s)\) be the number of distinct \(r\)-dimensional subcodes of \(C\) with coordinate support of size \(s\). All nonzero entries are as follows; every omitted entry is zero.

| \(r\) | \(s:H_r(s)\) | Number of subcodes |
|---|---|---:|
| 1 | 14:11, 15:28, 16:31, 17:16, 18:10, 19:12, 20:6, 21:2, 22:2, 23:3 | 121 |
| 2 | 19:6, 20:87, 21:291, 22:326, 23:216, 24:205, 25:79 | 1210 |
| 3 | 22:15, 23:255, 24:445, 25:495 | 1210 |
| 4 | 24:25, 25:96 | 121 |
| 5 | 25:1 | 1 |

The generator columns are twenty-five distinct projective points in \(\mathrm{PG}(4,3)\). Exactly fifteen projective lines contain three of these points, and no line contains four. Exactly six projective planes contain six of the points. The dual code has no weight-one or weight-two words, exactly thirty words of weight three, and exactly nine hundred seventy-two words of weight four. In coordinate-local repair, precisely twenty-one coordinates have minimum locality two; positions \(1,7,9,10\), numbered from one, have minimum locality three. In particular, the maximum local repair degree is three, and no two-coordinate repair works at those four positions.

## Assumptions and scope

All arithmetic is over \(\mathbb F_3\). The object is the **specific displayed code**, not every code with the same length, dimension or minimum distance. The five rows of its generator, from top to bottom, are encoded as twenty-five successive field digits:

```text
1000022000110211122121020
0100000222100112111112121
0010021220202220021120200
0001020211122201101002100
0000111102112001011121222
```

A codeword is \(uG\) for \(u\in\mathbb F_3^5\). The support of a subcode is the set of coordinates not identically zero throughout that subcode. By definition, \(d_r(C)\) is the smallest size of the support of any \(r\)-dimensional subcode. The locality at coordinate \(i\) is the least number of *other* coordinates required to reconstruct that coordinate using a linear parity check, equivalently the minimum weight of a dual word nonzero at \(i\), minus one.

## Proof

**Dimension and projectivity.** Row reduction over \(\mathbb F_3\) shows \(\operatorname{rank}(G)=5\); row reduction of \(GG^{\mathsf T}\) also gives rank five (its determinant is \(1\) modulo three). Thus \(C\) is a ternary linear complementary-dual (LCD) code. Each column is nonzero. Normalize each column by multiplying by the inverse of its first nonzero entry: all twenty-five normalized vectors are distinct. This proves projectivity and excludes dual words of weights one and two.

**Complete support enumeration.** Every \(r\)-dimensional subspace of \(\mathbb F_3^5\) has a unique reduced-row-echelon basis \(B\) of size \(r\times5\). Enumerate each increasing pivot sequence and all entries to the right of pivots in nonpivot columns; the remaining entries are forced. For every resulting \(B\), the subcode is \(\operatorname{rowspan}(BG)\) and its support size is
\[
\left|\{j\in\{1,\ldots,25\}: (BG)_{1j},\ldots,(BG)_{rj}\text{ are not all zero}\}\right|.
\]
Exact integer enumeration gives the five rows of the displayed \(H_r(s)\) table. Their totals are, respectively, \(121,1210,1210,121,1\), the Gaussian binomial coefficients \(\binom{5}{r}_3\). Since the enumeration is of every possible reduced echelon form exactly once, this is exhaustive, not sampling. The minima of the support table give the stated five generalized weights. Independent enumeration of all \(3^5=243\) vectors \(uG\) gives the complete weight enumerator, and its nonzero coefficients agree with twice the one-dimensional subcode counts.

**Projective intersections.** For any \(r\)-subspace of messages, its common-zero coordinates are precisely the generator columns lying in its \((5-r)\)-dimensional annihilator. For \(r=3\), these are projective lines; the table says fifteen have three chosen points and none have four. For \(r=2\), the annihilator is a projective plane, and the table gives exactly six planes containing six chosen points.

**Dual checks and locality.** A dual word supported on distinct positions \(j_1,\ldots,j_t\) exists with all those coordinates nonzero exactly when coefficients \(c_h\in\{1,2\}\) satisfy \(\sum_h c_h G_{:,j_h}=0\). Divide by the first coefficient and enumerate the \(2^{t-1}\) remaining possibilities. Exhaustion of all \(\binom{25}{3}=2300\) triples gives exactly fifteen dependent supports, with thirty nonzero weight-three dual words. The positions absent from every such triple are exactly \(1,7,9,10\). Exhaustion of all \(\binom{25}{4}=12650\) four-subsets gives 486 supports of nonzero four-term relations. A four-subset has at least rank three because no projective line contains four columns; consequently each such support gives precisely two scalar-multiple weight-four dual words, for 972 in total. Each of the four positions absent from the triples belongs to at least one such quadruple. No locality-one check exists because the code is projective. The asserted minimum locality at every coordinate follows.

## Verification

Run `python3 checker.py` with a standard Python 3 installation. The self-contained checker reads the complete generator from its own source, verifies row rank and the LCD Gram matrix, independently counts 243 codewords, enumerates every one of the 2663 nonzero subcodes using unique echelon bases, and checks all triples and quadruples for exact nonzero dual relations. It asserts each integer above and the four exceptional positions. No numerical tolerance, randomized sampling, optimization package or external solver is used.

## Relationship to prior work

An, Hong, Kim and Lim introduced this exact ternary \([25,5,14]\) LCD generator in their study of shortest LCD embeddings (Proposition 4.1, fourth displayed generator). Their contribution establishes the existence and minimum distance of the code; the present result identifies the complete higher-support distribution and coordinatewise repair behavior of that particular construction. Wei's generalized Hamming-weight theory explains why higher supports are relevant to wiretap-II information leakage, but does not supply the values for this generator. The dimension-five and projectivity computations distinguish this code from other published LCD constructions, even if they share the same minimum distance.

## Limitations

These are exact properties of one labeled matrix. They do not classify all ternary \([25,5,14]\) codes, establish the optimality of its unknown possible minimum-distance improvement to fifteen, or prove its repair locality optimal among competing codes. The certificate is an exhaustive finite mathematical computation justified by unique reduced-echelon forms, not a symbolic classification of an infinite family. Historical-priority checking cannot exclude all unindexed computational tables. Independent mathematical review remains unperformed.

## References

1. J. An, J.-H. Hong, J.-L. Kim, H. Lim, *Shortest LCD embeddings of binary, ternary and quaternary linear codes*, arXiv:2601.20600, first posted 2026-01-28, revised 2026-06-08, Proposition 4.1. https://arxiv.org/abs/2601.20600
2. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory **37** (1991), 1412–1418. https://doi.org/10.1109/18.133259
