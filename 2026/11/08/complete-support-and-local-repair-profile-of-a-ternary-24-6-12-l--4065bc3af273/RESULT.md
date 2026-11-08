# Complete support and local-repair profile of a ternary \([24,6,12]\) LCD code

## Finding

For the *specific displayed* ternary \([24,6,12]\) LCD code \(C_{3,3}\) of An, Hong, Kim and Lim [1], its generalized Hamming weights, defined as \(d_r(C)=\min_{U\le C,\dim U=r}|\operatorname{Supp}(U)|\), are exactly

\[
(d_1,d_2,d_3,d_4,d_5,d_6)=(12,16,19,21,23,24).
\]

There is **exactly one** two-dimensional subcode whose coordinate support has size \(16\); there are respectively three three-dimensional and three four-dimensional subcodes at their support minima. The full Hamming weight enumerator is

\[
\begin{aligned}
W_C(z)={}&1+32z^{12}+70z^{13}+108z^{14}+100z^{15}\\
&+126z^{16}+96z^{17}+84z^{18}+54z^{19}\\
&+48z^{20}+8z^{21}+2z^{22}.
\end{aligned}
\]

Every coordinate is locally repairable from at most three other coordinates, but only nine can be repaired from two: in one-based indexing the locality-two coordinates are \(\{1,2,5,8,11,12,15,23,24\}\); all other 15 coordinates have exact locality three. The code has exactly three weight-three dual checks, up to nonzero scalar multiplication, supported on the disjoint triples \(\{1,15,23\}\), \(\{2,5,11\}\) and \(\{8,12,24\}\). There are exactly \(102\) minimal weight-four dual-check supports (four-element column circuits).

## Assumptions and scope

All field arithmetic is in \(\mathbb F_3\), with \(0,1,2\) interpreted modulo three. The code is the row space of this *particular* \(6\times24\) generator matrix (rows presented as coordinate strings, without separators):

```
100002211002021122200001
010201002021102121022221
001200122202102020111020
000011112222111100000111
000102011100210200110102
000000121101110122021102
```

The row strings reproduce the matrix \(C_{3,3}\) displayed in Proposition 4.1 of [1], whose arXiv manuscript was first made public on 2026-01-28. The conclusions are about this generator and its row space; no classification of all codes with the same length, dimension and distance is asserted. A subcode support is the union of supports of its codewords. A parity check repairing coordinate \(j\) from \(r\) others is a dual word of weight \(r+1\) whose \(j\)-th entry is nonzero.

## Proof

**Step 1: ambient code and minimum distance.** The supplied `checker.py` performs exact Gaussian elimination over \(\mathbb F_3\) and establishes generator rank six and Gram-matrix rank six, hence the Euclidean LCD property. Enumerating the \(3^6=729\) coefficient vectors gives the displayed weight enumerator and therefore minimum distance twelve.

**Step 2: exhaustive subspace census.** Each dimension-\(r\) subspace of \(\mathbb F_3^6\) has a unique reduced-row-echelon basis. Enumerate all strictly increasing pivot sets and all free entries in the corresponding echelon forms. If \(B\) is such an \(r\times6\) basis, the image subcode has support

\[
\{j\in\{1,\ldots,24\}: B G_{\ast j}\ne0\},
\]

where \(G_{\ast j}\) is the \(j\)-th column of the given generator. This tests every subcode once because the generator has rank six. The exact dimension/support-size census is:

| Dimension \(r\) | Support size : number of subcodes |
|---|---|
| 1 | 12:16, 13:35, 14:54, 15:50, 16:63, 17:48, 18:42, 19:27, 20:24, 21:4, 22:1 |
| 2 | 16:1, 17:41, 18:307, 19:955, 20:1721, 21:2598, 22:2716, 23:2018, 24:654 |
| 3 | 19:3, 20:150, 21:1511, 22:5577, 23:12738, 24:13901 |
| 4 | 21:3, 22:267, 23:2361, 24:8380 |
| 5 | 23:24, 24:340 |
| 6 | 24:1 |

The row totals are \(364,11011,33880,11011,364,1\), precisely the Gaussian-binomial counts for subspaces of \(\mathbb F_3^6\). Taking the least support size in each row proves the entire hierarchy; the counts at those minima prove uniqueness and multiplicities. For the unique dimension-two minimizer, a reduced-row-echelon basis in message space is

\[
\begin{pmatrix}0&0&1&1&0&2\\0&0&0&0&1&2\end{pmatrix},
\]

and its zero coordinates are exactly \(\{1,2,9,10,14,15,22,23\}\); its support thus has size sixteen.

**Step 3: local repair.** A dual word supported in a coordinate set \(S\) is a nontrivial dependence of the corresponding generator columns. Exact rank testing finds no zero columns and no proportional column pairs. Among the \(\binom{24}{3}=2024\) triples there are precisely three dependent triples, listed in the Finding. Every such triple is a minimal dependence, hence supports a weight-three dual word with all three coefficients nonzero. Among the \(\binom{24}{4}=10626\) quadruples, precisely \(102\) are minimal dependent sets (rank three, all triple subsets independent). These quadruples cover every coordinate. The union of three minimal triples has nine coordinates, and no smaller dependencies exist. Therefore the exact localities are two on those nine coordinates and three on the other fifteen.

All computations are finite, exhaustive, deterministic and performed in exact integers modulo three. The full algorithm and expected certificates are standalone in `checker.py`; the stated ranks and enumerations are independently checkable by running it.

## Verification

Run `python3 checker.py` with Python 3 and no third-party packages. It checks all \(729\) codewords; all \(56631\) nonzero-dimensional subspaces; every pair, triple, and quadruple of columns; the unique support-sixteen two-dimensional basis; every stated histogram; and rank of both the generator and Gram matrices. The full \(r=1\) histogram is also cross-checked against one half of the weight enumerator for nonzero words. The executable must exit with status zero and print five `PASS:` lines; any mismatch raises an assertion error. No random sampling or numerical tolerance is involved.

## Relationship to prior work

An, Hong, Kim and Lim [1], Proposition 4.1, introduce this exact \(6\times24\) generator and establish its LCD parameters \([24,6,12]\). Their reported theorem concerns construction and minimum distance, not generalized Hamming weights, the complete subcode-support distribution, or per-coordinate dual repair checks. Generalized Hamming weights [2] are relevant to wiretap-II leakage and higher-order erasure phenomena; their computation is also a recognized independent problem [3]. Publicly indexed investigations of two other matrices in the same construction family concern a \([23,4,14]\) code and a \([23,5,12]\) code, neither of which logically specifies the present \([24,6,12]\) subspace census or locality partition.

## Limitations

The claim is an exact characterization of one published concrete code, not a formula valid for all \([24,6,12]_3\) codes. It does not prove optimality of repair locality among all such codes, classify equivalent generators, or determine channel-specific operational performance. The exhaustive certificate constitutes a finite proof when the provided enumeration and rank procedures are checked; no separate formal or independent mathematical audit is claimed. Searches cannot rule out an unindexed pre-existing computation of this generator's support profile.

## References

1. J. An, J.-H. Hong, J.-L. Kim and H. Lim, *Shortest LCD embeddings of binary, ternary and quaternary linear codes*, arXiv:2601.20600, first submitted 2026-01-28, Proposition 4.1, https://arxiv.org/abs/2601.20600 .
2. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory **37** (1991), 1412–1418, https://doi.org/10.1109/18.133259 .
3. R. San-José, *An algorithm for computing generalized Hamming weights and the Sage package GHWs*, arXiv:2503.17764, https://arxiv.org/abs/2503.17764 .
