# Sharp five-point trace bound for radius-two Boolean Hamming balls

## Finding

Let \(Q_d=\{0,1\}^d\), for each integer \(d\ge1\), with Hamming distance \(\operatorname{dist}(x,y)=|\{i:x_i\ne y_i\}|\). For each center \(c\in Q_d\), write \(B_2(c)=\{x\in Q_d:\operatorname{dist}(x,c)\le2\}\), and let \(\mathcal B_{d,2}=\{B_2(c):c\in Q_d\}\). Traces are \(\operatorname{Tr}(S)=\{S\cap B_2(c):c\in Q_d\}\).

**Sharp five-point trace theorem.** For every \(d\ge1\) and every five-element \(S\subseteq Q_d\) contained in some \(B_2(c)\),
\[
|\operatorname{Tr}(S)|\le27.
\]
The constant \(27\) is attained in \(Q_6\) by
\[
S=\{e_5,\ e_1+e_2,\ e_1+e_3,\ e_2+e_3,\ e_4+e_5\},
\]
where addition is over \(\mathbb F_2\). Hence no five-element set is shattered by \(\mathcal B_{d,2}\), in any dimension.

**Exact dimension threshold.** The VC dimension of \(\mathcal B_{d,2}\) is
\[
\operatorname{VCdim}(\mathcal B_{d,2})=
\begin{cases}
0,&d=1,2,\\
1,&d=3,\\
3,&d=4,\\
4,&d\ge5.
\end{cases}
\]

The five-point statement concerns supports contained in a radius-two ball, as necessary for shattering. It does **not** assert that arbitrary five-point supports have at most \(27\) traces.

## Assumptions and scope

The alphabet is exactly binary; the radius is exactly two and is inclusive. All ball centers belong to the same \(Q_d\); centers outside the hypercube and varying radii are not permitted. The dimension \(d\) ranges over all positive integers. The five-point trace bound includes the empty trace among its \(32\) possible traces. A support is shattered if and only if all of its \(2^{|S|}\) traces occur.

The upper bound is an exhaustive **finite combinatorial certificate after a dimension-independent reduction**, not extrapolation from testing finitely many ambient dimensions. The exact certificate enumeration and a separate low-dimensional check are supplied in `verify.py`.

## Proof

### Reduction to finitely many column multisets

Suppose that a five-element support \(S=\{x^{(1)},\ldots,x^{(5)}\}\) lies in \(B_2(c_0)\). Translation by the binary word \(c_0\) preserves Hamming distance and all traces, so assume \(c_0=0\). Each of the five rows \(x^{(i)}\) has Hamming weight at most two.

Discard coordinates that are zero in all five rows. Every remaining coordinate has a nonzero five-bit **column mask** \(a\in\{1,\ldots,31\}\), indicating the rows with a one in that coordinate. Its multiplicity is at most two: since \(a\ne0\), at least one row contains that coordinate, and any three repetitions would give that row weight at least three. Thus a configuration is specified by multiplicities \(\nu_a\in\{0,1,2\}\) satisfying
\[
\sum_{a=1}^{31}\nu_a\,\mathbf 1_{\{i\in a\}}\le2
\qquad(i=1,\ldots,5).
\]
Here \(i\in a\) means that the \(i\)-th bit of \(a\) equals one. The five reconstructed rows must be distinct. Conversely, **every** admissible five-row configuration occurs in this list after a coordinate permutation. The number of nonzero coordinates is at most ten.

Write \(U=\sum_a\nu_a\) for this number. A candidate ball center \(c\) is determined, for trace purposes, by its active-coordinate part \(t\in\{0,1\}^U\) and by the number \(j\) of its ones in the discarded all-zero coordinates. For every row \(x^{(i)}\), the distance is exactly
\[
\operatorname{dist}(c,x^{(i)})=\operatorname{wt}(t\oplus x^{(i)})+j.
\]
If the total center weight is at least five then the distance to every row of weight at most two exceeds two, so the trace is empty. Therefore all nonempty traces arise from \(\operatorname{wt}(t)+j\le4\). Four auxiliary all-zero coordinates realize each possible value \(j=0,\ldots,4-\operatorname{wt}(t)\). They also realize the empty trace. Every trace possible in the original dimension is consequently among the traces of this **saturated template**, whose ambient dimension is at most fourteen.

### Exhaustive finite certificate

The recursive function `enumerate_columns` in `verify.py` takes the 31 nonzero masks in increasing order. For each mask it considers multiplicities zero, one, and two, pruning exactly when a row's weight would exceed two. It therefore visits every feasible column multiset, without a random sample or an unproved orbit-classification step. The function `inspect` reconstructs the five rows, discards configurations with duplicate rows, and evaluates all center patterns with active Hamming weight at most four and all allowable auxiliary weights. It forms exact five-bit traces by the displayed distance formula.

The executable enumeration yields **14,778** feasible column multisets, of which **7,260** have pairwise distinct rows. The maximum trace count over all 7,260 distinct-row configurations is **27**, and no configuration realizes all 32 traces. The trace-count histogram over distinct-row configurations, in the format (number of traces, number of configurations), is
\[
(17,6),(18,300),(19,100),(20,365),(22,1097),
(23,2385),(24,1590),(25,860),(26,240),(27,317).
\]
The integer operations used by the certificate are exact. This exhaustive classification, together with the reduction valid for arbitrary \(d\), proves the universal five-point bound. The supplied script can be read line by line and rerun without external packages.

The witness \(S\) in the statement, represented as integers \([16,3,5,6,24]\) using bit positions \(0,\ldots,5\), has exactly 27 traces by direct enumeration of all \(64\) centers in \(Q_6\), establishing sharpness. Specifically, the five absent positive-subset masks (using the displayed row order) are \(15,19,21,25,30\).

### Exact low-dimensional boundary

For \(d\le2\), every radius-two ball is all of \(Q_d\), and the VC dimension is zero. For \(d=3\), each radius-two ball is the complement of one vertex, so singletons are shattered, while no two-point support admits the empty trace; the dimension is one.

In \(Q_4\), complementation by antipodes gives
\[
Q_4\setminus B_2(c)=B_1(c+\mathbf 1),
\]
so the radius-two ball family has exactly the same shattered supports as the radius-one ball family. The latter shatters the three unit vectors \(e_1,e_2,e_3\) but cannot shatter four: a four-point support admitting the full trace lies in a closed radius-one star; if the star center belongs to the support, the other three leaves cannot be selected without it, and if four leaves belong to the support, any three cannot be selected without the fourth. In either case, the unique center of a radius-one ball containing any three distinct leaves is the star center. Hence the VC dimension is three in \(Q_4\).

For every \(d\ge5\), the four unit vectors \(\{e_1,e_2,e_3,e_4\}\) are shattered by radius-two balls. The full trace is realized by center zero; each three-element trace by the sum of its three selected unit vectors; each two-element trace by the sum of its two selected unit vectors; each singleton trace \(\{e_i\}\) by the center \(e_i+e_5\); and the empty trace by \(e_1+e_2+e_3+e_4\). The five-point bound rules out any larger shattered support. This proves the dimension formula.

## Verification

Run `python3 verify.py` with Python 3.10 or later. The script prints `TEMPLATE_CERTIFICATE_PASS 14778 7260 0 27`, then the complete trace histogram, exact direct dimension checks for \(d=1,\ldots,6\), the sharp 27-trace witness and the four-point shattering witness. Successful completion ends with `ALL_RADIUS_TWO_CUBE_CERTIFICATES_PASS`.

The low-dimensional checks independently enumerate Boolean distance tables rather than using the column-template code. The finite template enumeration is the critical universal certificate, whose completeness is proved in the reduction above; the independent finite checks are corroboration, not a substitute for that reduction. The numeric assertions in the code deliberately fail if the enumerated results differ from the claimed values.

## Relationship to prior work

Adler, Benediktsson and Macpherson (arXiv:2007.16042, first public July 31, 2020) analyze **open radius-one neighborhoods** in Hamming and Johnson graphs and prove the VC-dimension three bound for open Hamming neighborhoods. Their Section 4 addresses Hamming graph adjacency and its traces, not the radius-two closed balls considered here. In particular, an open radius-one neighborhood and a closed radius-two metric ball are different concept families, and a bound for the former does not imply the dimension-four threshold or the sharp 27-trace local bound for the latter.

Chalopin, Chepoi, Mc Inerney, Ratel and Vaxès (arXiv:2206.13254, first public June 27, 2022) study compression schemes for balls in graphs. Their general framework motivates fixed-radius ball classification, while their concrete results concern trees, cycles, interval graphs, trees of cycles, cube-free median graphs and related graph classes. The inspected passages do not provide the binary-hypercube radius-two classification or the 27-trace bound.

## Limitations

The five-point numerical bound uses an auditable exhaustive finite certificate, not a compact all-human case-free inequality. It is restricted to the binary alphabet, fixed radius two and supports admitting the full trace. The exact full shatter function at sizes other than five is not determined. The primary literature inspected does not establish comprehensive historical priority under all terminology (e.g. metric range spaces, translation families or binary code balls). No independence or third-party verification is claimed.

## References

1. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042 (first submitted 2020-07-31), https://arxiv.org/abs/2007.16042 .
2. J. Chalopin, V. Chepoi, F. Mc Inerney, S. Ratel and Y. Vaxès, *Sample compression schemes for balls in graphs*, arXiv:2206.13254 (first submitted 2022-06-27), https://arxiv.org/abs/2206.13254 .
