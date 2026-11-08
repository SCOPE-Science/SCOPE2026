# Exact local pair-weight profile of the length-fifteen binary Hamming code

## Finding

Let \(V=\mathbb F_2^4\setminus\{0\}\), and let \(H=(h_0,\ldots,h_{14})\) be any ordering of all fifteen elements of \(V\), each appearing once. Let \(C_H=\{c\in\mathbb F_2^{15}:Hc^T=0\}\), with indexed coordinate positions \(0,\ldots,14\), and use cyclic symbol-pair reads. Define
\[
B(C_H)=\#\{c\in C_H: w_{\mathrm{pair}}(c)=4\}.
\]
Across the \(64,864,800\) distinct indexed codes of this form, the complete distribution is

| \(B(C_H)\) | Number of indexed codes |
|---:|---:|
| 0 | 17,106,784 |
| 1 | 26,741,280 |
| 2 | 15,750,240 |
| 3 | 4,524,160 |
| 4 | 683,520 |
| 5 | 57,216 |
| 6 | 1,600 |

No other value occurs. In particular, precisely \(17,106,784\) indexed Hamming codes have the largest possible minimum cyclic symbol-pair distance within this permutation family, namely \(5\); all the others have minimum pair distance \(4\). The sharp maximum number of pair-weight-four codewords is \(6\).

## Assumptions and scope

All vector arithmetic, including \(\oplus\), is componentwise over \(\mathbb F_2\). Nonzero columns are represented by distinct integers \(1,\ldots,15\), whose four-bit binary expansions encode vectors. Coordinates are indexed and are NOT quotiented by coordinate rotation, reversal, or any other coordinate permutation. Two matrices yield the same code precisely when related by an invertible row transformation over \(\mathbb F_2\). The symbol-pair weight of \(c\) is the number of cyclic positions \(i\) at which \((c_i,c_{i+1})\ne(0,0)\), subscripts modulo fifteen.

## Proof

**Pair-weight criterion.** A nonzero codeword with a proper support \(S\) has cyclic pair weight equal to \(|S|\) plus the number of maximal cyclic runs in \(S\). Every nonzero word in \(C_H\) has Hamming weight at least three because the columns are all distinct and nonzero. If a nonzero word has pair weight four, its Hamming weight must therefore be three and its three support positions must be cyclically consecutive. Conversely every such weight-three word has pair weight four. A three-position indicator is a codeword exactly when the corresponding three columns have xor zero. Consequently
\[
B(C_H)=\sum_{i=0}^{14}[h_i\oplus h_{i+1}=h_{i+2}],
\]
where brackets denote indicators and indices are cyclic.

**Normalization.** There are \(15!\) ordered column matrices. The group \(\mathrm{GL}(4,2)\) of order \(15\cdot14\cdot12\cdot8=20,160\) acts freely by left multiplication, since every nonzero vector occurs as a column. Its orbits are precisely distinct indexed codes. The group is transitive on ordered pairs of distinct nonzero vectors. Accordingly the generating polynomial over distinct codes is \(15\cdot14/20,160=1/96\) times the generating polynomial over column permutations beginning with \((1,2)\).

**Exact finite recurrence.** Let \(U=\{1,\ldots,15\}\). For any used set \(S\supseteq\{1,2\}\) and final ordered pair \((u,v)\), let \(F(S,u,v;z)\) be the polynomial counting completions of the initial sequence \((1,2,\ldots,u,v)\), weighting all newly determined cyclic xor-zero triples by a factor \(z\). The two wraparound triples are delayed until completion. Put
\[
F(U,u,v;z)=z^{[u\oplus v=1]+[v\oplus1=2]},
\]
and, for \(S\ne U\), put
\[
F(S,u,v;z)=\sum_{x\in U\setminus S}z^{[u\oplus v=x]}F(S\cup\{x\},v,x;z).
\]
This is a finite acyclic recurrence: each term adds one unused vector, so it enumerates every allowed permutation exactly once and exhausts all possibilities. Direct integer evaluation gives
\[
\begin{aligned}
F(\{1,2\},1,2;z)={}&1,642,251,264+2,567,162,880z\\
&+1,512,023,040z^2+434,319,360z^3\\
&+65,617,920z^4+5,492,736z^5+153,600z^6.
\end{aligned}
\]
The coefficients sum to \(13!=6,227,020,800\), the number of possible tails after two fixed distinct columns. Dividing all coefficients by \(96\) gives the asserted distribution; their sum is \(15!/20,160=64,864,800\). The two supplied independent programs implement respectively a memoized suffix recursion and a forward state-by-state distribution, and both return these exact coefficients. This computationally evaluated finite recurrence, with its exhaustive state space and bounded arithmetic, certifies the count; no inference from sampled cases is used.

**Minimum pair distances.** If \(B(C_H)>0\), a pair-weight-four word exists and no smaller nonzero pair weight is possible. If \(B(C_H)=0\), pair weight is at least five. Given any adjacent two columns \(h_i,h_{i+1}\), their xor is a third, distinct, nonzero column \(h_j\). The associated weight-three codeword is not supported on three consecutive positions when \(B(C_H)=0\). Its support has a two-position run and an isolated position, so its pair weight is five. Thus distance five occurs exactly in the first row, and four in every other row. The top support value is six, witnessed by the column order \((1,2,3,4,5,8,13,6,10,12,11,7,9,14,15)\); an order with zero forbidden triples is \((1,2,4,3,5,7,6,8,9,10,11,12,14,13,15)\). Direct xor counting checks both witnesses.

## Verification

Run `python3 verify_profile.py` from the extracted package. It checks the exact recurrence, the seven coefficients, total orbit count, both witnesses and the first two factorial moments. Independently compile `forward_profile.cpp` using `c++ -O3 -std=c++17 forward_profile.cpp -o forward_profile` and run `./forward_profile`; the program computes a forward dynamic program for two distinct normalized starting pairs and compares its results. All counts use unsigned 64-bit integers, which accommodate the largest intermediate count since each normalized computation totals \(13!\). A separate analytical check gives
\[
\mathbb E[B]=15/13,\qquad \mathbb E[B(B-1)]=150/143.
\]
For the first moment, each of the fifteen positions is a collinear triple with probability \(1/13\). For the second, pairs of cyclic windows at offsets one, two and at least three contribute respectively zero, \(1/143\), and \(4/715\) to their joint event probabilities; there are respectively fifteen, fifteen, and seventy-five unordered pairs of these types. These identities agree with the complete computed distribution.

## Relationship to prior work

Cassuto and Blaum (2010, 2011) introduced the cyclic symbol-pair channel and its pair metric. Chee et al. (2012 preprint, revised 2013) established general MDS symbol-pair constructions and bounds; Chen, Lin and Liu (2016) obtained lower bounds for constacyclic codes, including coverage of the existence of good cyclic Hamming-code orderings through general methods. These results do not state the distribution over every coordinate permutation of the binary length-fifteen Hamming code. In the equivalent language of the projective Steiner triple system on fifteen points, the nonzero weight-three supports are its thirty-five lines. Blackburn and Etzion (2021) and Erskine and Griggs (2022) study cyclic block-avoiding sequencings; the latter supplies existence examples for all eighty Steiner triple systems on fifteen points, but not counts of the number of blocked consecutive triples among every cyclic sequencing of the projective system. Previous finite results at length seven do not determine the length-fifteen distribution. These are implication comparisons, not claims of exhaustive historical priority.

## Limitations

The finding is an exact finite census for indexed binary Hamming codes of length fifteen and the number of their pair-weight-four codewords. It does not classify full pair-weight enumerators, all code automorphism classes under coordinate rotation or reversal, arbitrary non-Hamming codes, or other Hamming lengths. The maximum pair distance five is optimal **within coordinate permutations of the fixed Hamming code**, not an assertion that the Singleton-type pair bound for arbitrary codes is met. Historical priority remains subject to human verification against unindexed enumerations and literature not accessible in full text.

## References

- Y. Cassuto and M. Blaum, *Codes for symbol-pair read channels*, IEEE ISIT 2010, pp. 988–992, DOI: https://doi.org/10.1109/ISIT.2010.5513753 (IEEE digital listing dated 2010-07-23).
- Y. Cassuto and M. Blaum, *Codes for Symbol-Pair Read Channels*, IEEE Transactions on Information Theory 57 (2011), pp. 8011–8020, https://doi.org/10.1109/TIT.2011.2164891.
- Y. M. Chee, L. Ji, H. M. Kiah, C. Wang and J. Yin, *Maximum Distance Separable Codes for Symbol-Pair Read Channels*, arXiv:1211.1728, first posted 2012-11-07, https://arxiv.org/abs/1211.1728.
- B. Chen, L. Lin and H. Liu, *Constacyclic symbol-pair codes: lower bounds and optimal constructions*, arXiv:1605.03460, first posted 2016-05-11, https://arxiv.org/abs/1605.03460.
- S. Blackburn and T. Etzion, *Block-avoiding point sequencings*, Journal of Combinatorial Designs 29 (2021), pp. 339–366, https://pure.royalholloway.ac.uk/files/41150489/sts_sequencing_final.pdf.
- G. Erskine and T. S. Griggs, *Good point sequencings of Steiner triple systems*, arXiv:2204.02732, first posted 2022-04-06, https://arxiv.org/abs/2204.02732.
