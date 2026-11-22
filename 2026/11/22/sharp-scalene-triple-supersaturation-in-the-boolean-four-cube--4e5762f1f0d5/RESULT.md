# Sharp scalene-triple supersaturation in the Boolean four-cube

## Finding

Let \(Q=\{0,1\}^4\subset\mathbb R^4\), with its ordinary Euclidean metric. For any vertex subset \(X\subseteq Q\), let \(T(X)\) be the number of unordered triples of distinct vertices of \(X\) whose three pairwise Euclidean distances are distinct. Define \(m(k)=\min_{X\subseteq Q,\,|X|=k}T(X)\), for integers \(0\le k\le16\). Then

\[
m(k)=\begin{cases}
0,&0\le k\le8,\\
16r+4\binom r2+4\max\{0,r-4\},&9\le k\le16,\quad r=k-8.
\end{cases}
\]

For \(6\le k\le8\), the minimizers are exactly the subsets contained in one of the two eight-vertex parity classes \(E=\{v:\sum_i v_i\equiv0\pmod2\}\) or \(O=Q\setminus E\). For \(9\le k\le15\), the minimizers are exactly the sets consisting of all eight vertices of one parity class together with \(r=k-8\) vertices of the other parity class selected to contain the smallest possible number \(\max\{0,r-4\}\) of antipodal pairs \(\{v,\mathbf1-v\}\). At \(k=16\), the whole cube is the only set. No uniqueness/classification assertion is made for \(0\le k\le5\).

The minimum values and numbers of labelled minimizing subsets for \(k=6,7,\ldots,16\), respectively, are

| \(k\) | minimum \(m(k)\) | number of minimizers |
|---:|---:|---:|
| 6 | 0 | 56 |
| 7 | 0 | 16 |
| 8 | 0 | 2 |
| 9 | 16 | 16 |
| 10 | 36 | 48 |
| 11 | 60 | 64 |
| 12 | 88 | 32 |
| 13 | 124 | 64 |
| 14 | 164 | 48 |
| 15 | 208 | 16 |
| 16 | 256 | 1 |

## Assumptions and scope

Every point of \(Q\) is a four-bit vector. Its binary integer encoding is \(0,\ldots,15\); the squared Euclidean distance between encoded vertices \(u,v\) equals the Hamming weight of their bitwise exclusive-or. All subsets are literal subsets of these sixteen fixed vertices, not arbitrary points in the continuous cube, not congruence classes, and not multisets. Scalene means three *pairwise distinct* positive side lengths; an isosceles triple is its complement among triples of distinct vertices (equilateral triples included). The formula has no unproved asymptotic or unrestricted-dimensional extension.

## Proof

**Geometric reduction.** Since squared side lengths take values in \(\{1,2,3,4\}\) and their sum is even for three Boolean vertices, direct coordinate counting shows that the three distinct squared-length patterns can only be \((1,2,3)\) and \((1,3,4)\). Explicitly, the sum of the three Hamming distances counts twice the number of nonconstant coordinates and is at most eight. Of the increasing triples from \(\{1,2,3,4\}\), exactly those two have even sum at most eight and satisfy the triangle inequalities for Hamming distance. They are realized. The certificate's direct triple loop counts 192 instances of the first and 64 of the second, or 256 scalene triples in the full four-cube.

**Sharp construction and its structure.** Points of the same parity have squared mutual distances only \(2\) or \(4\), so no triple entirely inside one parity class is scalene. Fix one full parity class \(E\), and let \(B\) be any \(r\)-element subset of the opposite parity class. For each \(b\in B\), exactly four vertices of \(E\) are at squared distance \(1\) from \(b\), and the other four at squared distance \(3\). Their cross-pairs yield precisely \(4\cdot4=16\) scalene triples containing \(b\) and two points of \(E\). A pair of vertices of \(B\) at squared distance \(2\) extends to four scalene triples with one vertex of \(E\); an antipodal pair at squared distance \(4\) extends to eight. Hence, if \(a(B)\) is the number of antipodal pairs contained in \(B\),

\[
T(E\cup B)=16r+4\binom r2+4a(B).
\]

Each parity class consists of four disjoint antipodal pairs, so \(a(B)\ge\max\{0,r-4\}\), with equality attained by taking at most one vertex from each pair until all four pairs are represented and then filling remaining pairs. This supplies the displayed candidate value and every asserted example, including the transition at \(r=4\).

**Exhaustive lower bound and equality verification.** The required *global* lower bound (among all subsets, including those that meet both parity classes without containing either one completely) and the statement that the above constructions account for *every* equality case are established by the following complete, exact finite recurrence, independently checked by the supplied standalone script `check_iso4.py`.

Order the sixteen vertices by their binary encodings \(0,1,\ldots,15\). Encode a subset by its sixteen-bit incidence mask \(M\). Put \(F(0)=0\). If \(M\ne0\), let \(h\) be the largest selected vertex index and \(M'=M\setminus\{h\}\). Then

\[
F(M)=F(M')+\sum_{\substack{u<v<h\\u,v\in M'}}
\mathbf1\!\left(\left|\{d(u,v),d(u,h),d(v,h)\}\right|=3\right),
\qquad d(u,v)=\operatorname{popcount}(u\mathbin{\mathrm{xor}}v).
\]

This recurrence is an identity: the new triples are precisely those containing \(h\). Its masks range over every integer \(0\le M<2^{16}\), with each term referring to a smaller mask, so it is a finite proof procedure covering exactly \(65\,536\) subsets, not a sampling argument. The code constructs all \(\binom{16}{3}=560\) possible triples, records exactly the 256 scalene ones, fills all recurrence values, and independently recomputes the result for **all** masks by direct inclusion over those 256 triples. It obtains the displayed exact minimum and count for every cardinality, then verifies for **every** mask of size at least six that it attains the minimum if and only if it satisfies the asserted parity/antipodality classification. All operations are integers and Boolean comparisons; no numerical approximations or unexecuted case reductions are needed. The included source is the full certificate, rather than a log-only assertion.

The parity-construction identity is also independently verified for all \(2\cdot2^8=512\) such subsets. Thus both the global extremality and equality classifications follow from a reproducible, exhaustively checked finite derivation.

## Verification

Run `python3 check_iso4.py` with Python 3.8 or later; it uses only standard-library `itertools` and `math`. Its successful output begins with `PASS: all 65,536 subsets, 256 scalene triples, exact minima, extremizers, and parity identity` followed by the eleven table rows for \(6\le k\le16\). The two counting procedures are implemented separately: maximal-index recurrence and full direct membership testing. All sixteen vertex encodings and all 65,536 masks are enumerated explicitly, and each proposed equality description is checked in both directions.

## Relationship to prior work

Yury Ionin, *Isosceles Sets* (2009), introduced and studied isosceles subsets of binary Hamming spaces, proved general cardinality bounds and discussed parity families; see especially his Sections 1, 3 and 4. Hyunjun Yi, *Isosceles sets and two-distance sets in Euclidean space* (arXiv:2611.05421, initial public version dated 2026-11-02), proves global extremal-size and structural results for isosceles sets in Euclidean spaces, not the present exact number of offending triples at every cardinality of a fixed Boolean four-cube. Padmini Mukkamala's *Triangle-free subsets of the Hypercube* (arXiv:2506.18782) concerns equilateral fixed-distance triples, not the mixed-distance scalene triples counted here. These are scientifically related but do not, in the inspected material, imply the complete four-cube supersaturation profile or its equality classification. No general novelty guarantee is inferred from search results alone.

## Limitations

The theorem applies **only** to the sixteen vertices of the four-dimensional Boolean cube. It does not solve the isosceles-set supersaturation problem in larger Hamming cubes or for arbitrary Euclidean configurations. The proof of global optimality is exact exhaustive finite enumeration, not a dimension-free structural inequality. The certificate verifies finite completeness but is not independent mathematical peer review. Earlier unindexed or inaccessible computations might have anticipated portions of this result.

## References

1. Hyunjun Yi, *Isosceles sets and two-distance sets in Euclidean space*, arXiv:2611.05421v1 (2026-11-02); https://arxiv.org/abs/2611.05421 and https://arxiv.org/html/2611.05421.
2. Yury J. Ionin, *Isosceles Sets*, Electronic Journal of Combinatorics **16** (2009), R141, https://doi.org/10.37236/230; full text https://www.combinatorics.org/ojs/index.php/eljc/article/download/v16i1r141/pdf/.
3. Padmini Mukkamala, *Triangle-free subsets of the Hypercube*, arXiv:2506.18782 (2025), https://arxiv.org/abs/2506.18782.
