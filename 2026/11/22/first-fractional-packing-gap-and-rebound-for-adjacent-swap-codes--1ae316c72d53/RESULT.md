# First fractional-packing gap and rebound for adjacent-swap codes on Fibonacci words

## Finding

A transmitted binary word of length \(n\) must avoid `11`. The channel permits no error or one swap of two adjacent unequal bits. Words are linear, and received words may contain `11`. Write \(M_n\) for the largest code with disjoint sets of possible outputs, \(P_n\) for the fractional packing optimum of those output sets, and \(N_n\) for the number of labeled maximum codebooks.

The exact profiles through length ten are:

| \(n\) | \(M_n\) | \(P_n\) | \(N_n\) |
|---:|---:|---:|---:|
| 1 | 2 | 2 | 1 |
| 2 | 2 | 2 | 2 |
| 3 | 3 | 3 | 3 |
| 4 | 4 | 4 | 3 |
| 5 | 6 | 6 | 9 |
| 6 | 8 | 8 | 24 |
| 7 | 12 | \(61/5\) | 56 |
| 8 | 18 | 18 | 24 |
| 9 | 25 | \(126/5\) | 1260 |
| 10 | 38 | \(115/3\) | 480 |

The first strict fractional gap occurs at \(n=7\); equality returns at \(n=8\), and strict gaps recur at \(n=9,10\). In all ten cases \(M_n=\lfloor P_n\rfloor\), so these gaps do not give a failure after rounding. At length seven, four of the 56 maximum codebooks are invariant under coordinate reversal, giving 30 reversal classes. At length eight, none of the 24 maximum codebooks is reversal-invariant, giving 12 classes.

The fractional and optimizer profiles are the focus. The integer profile is a baseline for the gaps and census, and is already recoverable from the unrestricted fixed-weight table OEIS A085684 by the shortening below.

## Assumptions and scope

Let \(\mathcal F_{n,k}\) consist of the length-\(n\) binary words of weight \(k\) avoiding `11`, and let \(\mathcal F_n=\bigcup_k\mathcal F_{n,k}\). There are no endpoint constraints or wraparound swaps. For \(w\in\mathcal F_n\), define \(B(w)\) to consist of \(w\) itself and all words obtained by swapping one pair of adjacent unequal bits. In particular, the possible outputs are not restricted to \(\mathcal F_n\). The fractional packing problem is
\[
P_n=\max\left\{\sum_{w\in\mathcal F_n}x_w:\ x_w\ge0,\quad \sum_{w:z\in B(w)}x_w\le1\ \text{for each possible }z\right\}.
\]
A labeled codebook is an unordered set of words with labeled coordinate positions; reversal is not quotiented out when defining \(N_n\). The table concerns only \(1\le n\le10\).

## Proof

**Weight decomposition.** Every output has the same weight as its source. Thus the maximum sizes and fractional optima add over the weight blocks, whereas the counts of maximizers multiply. The counts of reversal-fixed maximizers also multiply, since reversal preserves weight.

**Relation to unrestricted fixed-weight packing.** At fixed weight \(k>0\), write a source as the increasing tuple \(a_0,\ldots,a_{k-1}\) of positions of its ones, numbered from zero. Its separation constraints \(a_{i+1}-a_i\ge2\) say exactly that the shifted tuple \(b_i=a_i-i\) is strictly increasing in \(\{0,\ldots,n-k\}\). This gives a bijection to unrestricted weight-\(k\) binary words of length \(n-k+1\), and commutes with the respective reversals. For unrestricted words of equal weight, the adjacent-swap distance is \(\sum_i|a_i-a'_i|\): a swap changes one coordinate by one, and one can successively move a coordinate toward its target without collision. For a required left move, choose the first coordinate requiring one; a blocking predecessor would also require a left move. If only right moves remain, use the last coordinate requiring one. Thus the distance is preserved by shortening. Two radius-one balls in this graph intersect exactly when their centers are at distance at most two. It follows that the integer optimum, number of maximizing codebooks and reversal census in each block are precisely those of the unrestricted shorter problem.

The fractional optimum in each block is also preserved. After the same shift of coordinates, all strictly increasing received tuples give exactly the shorter unrestricted constraints, including zero error. A reachable non-strict tuple has a single repeated pair \((x,x)\), formed by moving one coordinate of a strictly increasing tuple by one. Its only possible shorter sources are obtained by replacing the pair with \((x-1,x)\) or \((x,x+1)\), retaining only strictly increasing tuples in range. If there is only one such source, its coefficient is bounded by the row at its no-error output. If both exist, the tuple with pair \((x-1,x+1)\) is strictly increasing, in range, and is one move from both. Its constraint implies the repeated-pair constraint by nonnegativity. Therefore the extra rows from outcomes containing `11` are redundant *for this reduction*; they remain in the stated channel and in the certificate. The weight-zero block has a single source and output.

**Exact integer and rational verification.** The supplied `certificate.json` gives explicit disjoint-ball codebooks and rational primal and covering-dual weights for all 40 weight blocks. The verifier enumerates all admissible sources and generates every possible output by a literal swap or no change. It forms the graph with edges between distinct sources whose output sets intersect. For any remaining vertex set \(S\) and selected vertex \(v\), every independent set either omits \(v\) (the problem on \(S\setminus\{v\}\)) or contains it (one plus the size on \(S\setminus(\{v\}\cup N(v))\)). The larger of the two branch optima gives the optimum, and their maximizing counts add in case of equality. The empty set has size zero and one maximizer. This recurrence counts all maximizing sets without duplication. The verifier also checks each listed codebook for admissibility and disjointness of its complete output sets.

The verifier checks the nonnegativity and all inequalities for the rational packings \(x_w\) and rational covers \(y_z\). The cover inequalities are \(\sum_{z\in B(w)}y_z\ge1\) for every source \(w\). In each block the two objective sums agree, proving optimality by weak duality. The exact rational arithmetic includes rows containing `11`. Summing the block optima gives the displayed fractional values. At the lengths with a gap, the only contributing blocks are \((n,k)=(7,2),(9,4),(10,2)\), with integer and fractional optima \((4,21/5),(4,21/5),(9,28/3)\), respectively.

For \(n=7,8\), the recurrence also lists every maximizing set in each block and tests invariance under the coordinate-reversal permutation. Multiplying block counts gives 56 and 24 labeled optima, of which four and zero are fixed. Burnside’s lemma gives the displayed reversal classes.

## Verification

Run `python3 verify.py` with `certificate.json` next to it. The checker uses the Python standard library and `fractions.Fraction`; it requires no numerical optimizer. The expected marker is `VERIFY_OK`, followed by the ten rows and the reversal results at seven and eight. The shortening argument is proved above, but is not required by the verifier, which works directly with the original output sets. The certificate and checker concern only the displayed finite range.

## Relationship to prior work

Write \(T(\ell,k)\) for the unrestricted length-\(\ell\), weight-\(k\) integer optimum. Then \(M_n=\sum_{k=0}^{\lceil n/2\rceil}T(n-k+1,k)\), with the weight-zero summand equal to one. The entries of OEIS A085684 through \(\ell=10\) (together with the trivial weight-zero case) give every integer value displayed above. For example, the five summands at \(n=7\) are \(1,3,4,3,1\). In particular, Gómez Soto, Leaños, Ríos-Castro and Rivera and OEIS A085680 give the weight-two integer summands via \(T(n-1,2)\). By contrast, the unrestricted aggregate OEIS A057608 sums the optima at a single common length and cannot be substituted for these fixed-weight data. These integer-size tables do not give the fractional optimum or the optimum-codebook and reversal counts used here.

Kovačević studies runlength-constrained shift correction with prescribed boundary markers and primarily asymptotic bounds. Kovačević, Kiah and Goyal study adjacent-transposition bounds for unrestricted alphabets. The Fibonacci-cube 2-packing literature uses single-bit Hamming adjacency, and the deletion-shadow framework changes the received length. Related exact finite profiles for directed bit changes on Fibonacci words or adjacent swaps on Dyck words change the channel or the source. The contribution here is the exact fractional and optimizer census for the displayed adjacent-swap packing instances and the resulting first gap and return to equality; neither the packing framework nor previously known unrestricted integer values are claimed as new.

## Limitations

No result for \(n>10\), asymptotic capacity, or integer-rounding failure is asserted. The shortening comparison and the finite output certificates do not establish historical priority over all unindexed fixed-weight tables.

## References

1. N. J. A. Sloane, OEIS A057608, https://oeis.org/A057608.
2. J. M. Gómez Soto, J. Leaños, L. M. Ríos-Castro, and L. A. Rivera, *The packing number of the double vertex graph of the path graph*, https://arxiv.org/abs/1711.03682; see also OEIS A085680, https://oeis.org/A085680.
3. M. Kovačević, *Runlength-Limited Sequences and Shift-Correcting Codes: Asymptotic Analysis*, https://arxiv.org/abs/1803.06117.
4. M. Kovačević, H. M. Kiah, and K. Goyal, *Bounds on Codes Correcting Adjacent Transpositions*, https://arxiv.org/abs/2509.06692.
5. A. Castro, S. Klavžar, M. Mollard, and Y. Rho, *On the domination number and the 2-packing number of Fibonacci cubes and Lucas cubes*, https://doi.org/10.1016/j.camwa.2011.03.012.
6. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, https://arxiv.org/abs/1211.3128.
7. OEIS A085684, triangle of unrestricted binary single-adjacent-transposition code sizes by length and weight, https://oeis.org/A085684.
