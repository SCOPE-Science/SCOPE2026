# Sharp diameter and rigid extremizers of binary rank-two code distortion

## Finding

For every integer \(n\ge 2\), let \(\mathcal C_n\) be the collection of binary linear \([n,2]\) codes, allowing zero coordinate positions. For any \(C\in\mathcal C_n\), write \(w(C)=(a_1,a_2,a_3)\) for the **sorted**, strictly positive Hamming weights of its three nonzero codewords. Given two codes with \(w(C)=(a_i)_{i=1}^3\) and \(w(E)=(b_i)_{i=1}^3\), their minimum linear code distortion, as defined by Bennett, Fox and Morrell, is exactly

\[
\mathcal D(C,E)=\frac{\max_{1\le i\le3}b_i/a_i}{\min_{1\le i\le3}b_i/a_i}.
\]

Consequently, the logarithmic distortion between binary rank-two codes is precisely the Hilbert projective distance between their ordered nonzero-weight triples. In particular,

\[
\max_{C,E\in\mathcal C_n}\mathcal D(C,E)=
\begin{cases}1,&n=2,\\ n,&n\ge3.\end{cases}
\]

For every \(n\ge3\), equality holds **if and only if**, after possibly swapping \(C,E\), the respective sorted nonzero-weight profiles are

\[
(1,n-1,n)\quad\text{and}\quad(2t,2t,2t),
\qquad 1\le t\le\lfloor n/3\rfloor.
\]

Up to coordinate permutations, this gives exactly \(2\lfloor n/3\rfloor\) ordered pairs of extremizing code classes (and one ordered pair when \(n=2\)). The first class is the direct sum of a singleton and an \((n-1)\)-coordinate repetition code; the second has exactly \(t\) columns of each of the three nonzero binary two-vectors and \(n-3t\) zero columns.

## Assumptions and scope

All codes are two-dimensional \(\mathbb F_2\)-linear subspaces of \(\mathbb F_2^n\). They need not have full support. A linear code isomorphism \(T:C\to E\) has distortion

\[
\mathcal D_T(C,E)=
\frac{\max_{x\in C\setminus\{0\}}\mathrm{wt}(Tx)/\mathrm{wt}(x)}
{\min_{x\in C\setminus\{0\}}\mathrm{wt}(Tx)/\mathrm{wt}(x)}.
\]

The minimum \(\mathcal D(C,E)\) is taken over all such isomorphisms. Each extends to an invertible map of the ambient \(\mathbb F_2^n\), so this agrees with the ambient-map definition in the cited source. The multiplicities in the sorted nonzero-weight triple are retained.

## Proof

**1. Every permutation of nonzero words is linear.** A binary two-dimensional space has exactly three nonzero vectors. Its invertible linear group has order six and acts as the entire symmetric group on these vectors: two distinct nonzero vectors form a basis, and the third is their sum. Thus optimizing over code isomorphisms is equivalent to matching the three nonzero weights by an arbitrary permutation. Every such subspace isomorphism extends to an ambient invertible linear map by extending source and target bases.

**2. Sorting is optimal.** Suppose \(a_i\le a_j\) and \(b_p\le b_q\). A crossed matching has ratios \(b_q/a_i\) and \(b_p/a_j\), with the former at least the latter. Uncrossing produces \(b_p/a_i\) and \(b_q/a_j\), both inside the closed interval

\[
[b_p/a_j,\ b_q/a_i].
\]

Therefore an uncrossing never increases the maximum matched ratio and never decreases the minimum matched ratio. Successively removing inversions yields a noncrossing, sorted matching whose distortion cannot exceed that of any initial matching. This proves the displayed exact formula, including repeated weights.

**3. Metric interpretation.** For positive triples \(a,b\), let

\[
d_H(a,b)=\log\max_i(b_i/a_i)-\log\min_i(b_i/a_i).
\]

This is the standard Hilbert projective metric on positive triples modulo positive common scaling. Step 2 shows \(\log\mathcal D(C,E)=d_H(w(C),w(E))\). In particular, distortion one means proportional sorted weight profiles. This is compatible with, and does not replace, the general unary-scaling characterization of distortion one in the cited source.

**4. Universal sharp upper bound.** Set \(r_i=b_i/a_i\). For indices \(i<j\), sortedness gives

\[
\frac{r_i}{r_j}=\frac{b_i}{b_j}\frac{a_j}{a_i}
\le\frac{a_j}{a_i}\le n.
\]

For \(i>j\), the symmetric estimate yields

\[
\frac{r_i}{r_j}=\frac{b_i}{b_j}\frac{a_j}{a_i}
\le\frac{b_i}{b_j}\le n.
\]

For \(i=j\) the quotient is one. Because every nonzero codeword has weight between one and \(n\), taking the maximum over all ordered pairs of indices gives \(\mathcal D(C,E)\le n\). For \(n=2\), every binary \([2,2]\) code equals the full ambient space, hence the maximum is one.

**5. Equality rigidity for \(n\ge3\).** Suppose \(\mathcal D(C,E)=n\). Equality in one of the preceding estimates requires, after possibly swapping the two codes, indices \(i<j\) with \(a_i=1\), \(a_j=n\), and \(b_i=b_j\). A binary weight-\(n\) word is the unique all-one word; adding the unique weight-one word changes its weight to \(n-1\). The remaining nonzero word must therefore have weight \(n-1\), giving \(a=(1,n-1,n)\). For \(n\ge3\), the only index pair that can have \(a_i=1\) and \(a_j=n\) is \((i,j)=(1,3)\), so \(b_1=b_3\) and sortedness forces all three weights of \(E\) to coincide.

Write the three nonzero columns of a binary \(2\times n\) generator matrix as \((1,0),(0,1),(1,1)\), with respective multiplicities \(u,v,w\). The weights of its three nonzero codewords are \(u+w,v+w,u+v\). If all three equal \(h\), then \(u=v=w=h/2\). Thus \(h=2t\) with \(t\) a positive integer and \(3t\le n\); the remaining \(n-3t\) columns are zero. Conversely, these multiplicities realize the constant triple \((2t,2t,2t)\). Matching it to \((1,n-1,n)\) gives ratios \(2t,2t/(n-1),2t/n\), whose maximum/minimum quotient is exactly \(n\). This proves both necessity and sufficiency.

**6. Counting extremizers modulo coordinate permutation.** For any fixed labeled basis, if its three nonzero word weights are \(p,q,r\), the numbers of columns of types \((1,0),(0,1),(1,1)\) are respectively

\[
\frac{p+r-q}{2},\quad\frac{q+r-p}{2},\quad\frac{p+q-r}{2}.
\]

A basis change permutes these three nonzero column types; a coordinate permutation reorders columns. Therefore the unordered weight triple determines the code up to coordinate permutation. The profiles listed in Step 5 give \(\lfloor n/3\rfloor\) choices of \(t\) and two ordered orientations for each, which are distinct when \(n\ge3\). At \(n=2\) there is just one code. The classification follows.

## Verification

The standalone file `verify.py` uses exact rational arithmetic. It constructs all feasible rank-two generator-column multiplicity profiles for \(2\le n\le12\), compares the claimed sorted formula against all six possible weight matchings for every ordered pair of profiles, and checks the stated diameter and all equality cases. It additionally enumerates all \(4^n\) two-bit-column sequences for \(2\le n\le7\) and checks the profile characterization directly. A successful run prints `CHECK_OK`, 21,096 direct generator instances, and 19,902 ordered profile-pair comparisons. The proof in Steps 1–6, not the finite experiment, establishes the all-length theorem.

## Relationship to prior work

Bennett, Fox and Morrell (arXiv:2607.26261, first public July 28, 2026; APPROX/RANDOM 2026) introduce linear code distortion. Their Lemma 15 proves the general \(n^2\) upper bound, Lemma 27 gives exact brute-force computation for arbitrary fixed dimension, Corollary 28 gives polynomial-time solvability for sufficiently small dimension, and Proposition 19 characterizes distortion one via unary scaling. These statements are used as background, not attributed to this finding. The new statement identifies the binary dimension-two metric explicitly and computes its sharp global diameter, including every equality case. It is not a general code equivalence algorithm or a new characterization of distortion one in all dimensions.

Bennett and Win (2024, IACR ePrint 2024/782) investigate code-equivalence reductions to graph, matroid, and lattice isomorphism; those reduction results do not assert a sharp distortion diameter. The standard binary two-dimensional column-multiplicity description is elementary and is not itself presented as new.

## Limitations

The sharp diameter and equality classification apply to the binary field and dimension two, with arbitrary zero columns. They say nothing about the extremal distortion for higher dimensions, nonbinary alphabets, or codes constrained to full support. The checker's finite exhaustions are corroboration only. Historical priority is based on the checked literature and indexed-record searches, not an independently exhaustive worldwide bibliography. There has been no independent mathematical audit.

## References

1. H. Bennett, M. Fox, and B. Morrell, *The Code Distortion Problem*, arXiv:2607.26261 (first publicly submitted July 28, 2026); *APPROX/RANDOM 2026*, LIPIcs 392, article 24, DOI: 10.4230/LIPIcs.APPROX/RANDOM.2026.24. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2026.24
2. H. Bennett and K. M. H. Win, *Relating Code Equivalence to Other Isomorphism Problems*, IACR ePrint 2024/782 (2024), subsequently *Designs, Codes and Cryptography* 93 (2025), 701–723. https://eprint.iacr.org/2024/782
