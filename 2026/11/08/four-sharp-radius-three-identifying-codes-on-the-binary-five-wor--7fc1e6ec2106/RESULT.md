# Four sharp radius-three identifying codes on the binary five-word de Bruijn digraph

## Finding

Let \(G\) be the directed binary de Bruijn graph whose vertices are all \(32\) words in \(\{0,1\}^5\), with an arc from \(a_1a_2a_3a_4a_5\) to \(a_2a_3a_4a_5b\) for each \(b\in\{0,1\}\). A radius-three identifying code is a set \(S\) of vertices such that the sets \(I_S(v)=S\cap B^-_3(v)\) are nonempty and distinct for all vertices \(v\), where \(B^-_3(v)\) comprises vertices from which \(v\) is reachable by a directed walk of length at most three.

**Theorem.** The minimum cardinality of a radius-three identifying code in \(G\) is exactly \(16\). Moreover, there are exactly four labeled codes of this minimum cardinality. They are all the sets

\[
S_{b,c}=F\cup\{0001b,1110c\},\qquad b,c\in\{0,1\},
\]

where the following is a literal set of fourteen five-bit words:

```text
F = {
  00001, 00101, 00110, 01000, 01011, 01100, 01110,
  10001, 10011, 10100, 10111, 11001, 11010, 11110
}
```

Thus the four codes correspond to \((b,c)=(0,0),(1,0),(0,1),(1,1)\). Under simultaneous interchange of the two alphabet symbols, they form exactly three equivalence classes: the first and fourth codes are exchanged, and the other two are fixed. This is equivalence under alphabet interchange only, not a claim about any larger group.

## Assumptions and scope

All words are **indexed vertices**, not cyclic necklaces, and the graph is directed. Self-loops and paths of length zero are included when forming closed in-balls. The radius is exactly three, and the alphabet is exactly \(\{0,1\}\). Distinct codes are distinct subsets of the labeled vertex set. No condition is imposed on the placement or distance of the selected vertices except the identifying property.

The integer \(16\) is the established general lower-bound specialization \(2^4(2-1)\), which is reproduced below. The new statement is that this lower bound is attained at the critical length \(5=2\cdot3-1\), and that the four indicated subsets exhaust equality.

## Proof

**1. Explicit in-balls.** If \(v=v_1v_2v_3v_4v_5\), then

\[
B^-_3(v)=\{v\}\cup\bigcup_{d=1}^{3}
\{xv_1\cdots v_{5-d}:x\in\{0,1\}^d\}.
\]

Indeed, a directed walk of length \(d\) erases the first \(d\) symbols of its initial vertex and appends the last \(d\) symbols of its terminal vertex. This formula is valid for \(d=0,1,2,3\) even when the resulting words coincide at different lengths.

For a four-bit prefix \(p\), the two vertices \(p0\) and \(p1\) have the same incoming predecessors at every strictly positive path length at most three: those predecessors depend only on the first \(5-d\) target symbols. Therefore

\[
B^-_3(p0)\mathbin{\triangle}B^-_3(p1)\subseteq\{p0,p1\}.
\]

If neither \(p0\) nor \(p1\) belongs to an identifying code \(S\), the two intersections with \(S\) are equal. Hence every identifying code contains at least one of \(p0,p1\) for each of the sixteen prefixes \(p\); in particular \(|S|\ge16\). Equality forces the **one-per-prefix form**

\[
S=\{p f(p):p\in\{0,1\}^4\},
\quad f:\{0,1\}^4\longrightarrow\{0,1\}.
\]

**2. Fourteen of the choices are forced.** For distinct vertices \(v,w\), identification requires

\[
S\cap\bigl(B^-_3(v)\mathbin{\triangle}B^-_3(w)\bigr)\ne\varnothing.
\]

Every symmetric difference in the following table is obtained directly by the formula in step 1. All entries are literal five-bit words; juxtaposition in the right column lists a set, not a sequence.

| Vertices compared | Symmetric difference |
|---|---|
| `00001`, `00000` | `00001` |
| `00101`, `00100` | `00101` |
| `01001`, `01000` | `01000` |
| `01011`, `01010` | `01011` |
| `01101`, `01100` | `01100` |
| `10011`, `10010` | `10011` |
| `10101`, `10100` | `10100` |
| `10111`, `10110` | `10111` |
| `11011`, `11010` | `11010` |
| `11111`, `11110` | `11110` |
| `00100`, `00010` | `01001`, `10010`, `11001` |
| `11101`, `11011` | `00110`, `01101`, `10110` |
| `00010`, `00001` | `00010`, `10001` |
| `00011`, `00001` | `00011`, `10001` |
| `11110`, `11100` | `01110`, `11100` |
| `11110`, `11101` | `01110`, `11101` |

The first ten rows force the ten single-word differences to belong to \(S\). By the one-per-prefix rule, `01001`, `10010`, `01101`, and `10110` are consequently excluded. The next two rows then force `11001` and `00110`, respectively.

The thirteenth and fourteenth rows together force `10001`: otherwise they would force both `00010` and `00011`, contradicting one-per-prefix. Similarly, the last two rows force `01110`: otherwise both `11100` and `11101` would be required. Therefore precisely the fourteen words of \(F\) are forced. Their prefixes are distinct, and the two unassigned prefixes are `0001` and `1110`. There can be **at most four** size-sixteen identifying codes, each of the stated form \(S_{b,c}\).

**3. All four choices identify.** For each \(S_{b,c}\), compute the thirty-two intersections \(B^-_3(v)\cap S_{b,c}\) from the formula in step 1. They are all nonempty and pairwise different. The full \(4\times32\) exact signature table is supplied as `signatures.csv`; its third column is the 32-bit identifying-set incidence mask, with bit \(j\) representing the lexicographically \(j\)-th five-bit word. `verify.py` checks every one of the 128 signatures, and `crosscheck.cpp` independently constructs all radius-three in-balls using reverse-graph breadth-first search. The finite verification involves only four explicitly determined candidates, not a sample of a larger infinite parameter range.

Thus the lower bound is attained and all four equality cases are classified. To verify the final symmetry statement, complement every bit in every word of a code. The resulting map exchanges the masks `6949` and `23335`, and fixes `6951` and `23333`, with masks defined as in the verification section. Hence there are exactly three alphabet-interchange classes. \(\square\)

## Verification

The package contains all of the following standalone artifacts, with no external datasets:

- `certificate.tsv`: the sixteen exact incoming-ball symmetric-difference constraints used in step 2.
- `signatures.csv`: the complete 128-entry identifying-set certificate for all four equality cases.
- `verify.py`: constructs in-balls symbolically, checks every forced difference and all four identifying sets, and independently enumerates all \(2^{16}=65,536\) one-per-prefix candidates. Its output is `VERIFY_OK` with masks `6949,6951,23333,23335`.
- `crosscheck.cpp`: reconstructs the graph by directed arcs, computes in-balls by reverse-graph breadth-first search, and separately enumerates all \(65,536\) candidates. Its output is `CROSSCHECK_OK 4`.
- `generate_signatures.py`: checks or reconstructs the exact signature table.

The mask of a selector function \(f\) is \(\sum_{j=0}^{15}2^j f(p_j)\), where \(p_j\) is the four-bit binary encoding of \(j\). Thus the mask values are reproducible and depend on a precisely defined ordering. To replay in a directory containing the extracted files:

```sh
python3 verify.py
python3 generate_signatures.py --check
c++ -std=c++17 -O2 crosscheck.cpp -o crosscheck
./crosscheck
```

Both independently constructed graph representations agree, including the sixteen-prefix lower bound, the four equality cases, and the three symbol-complement orbits. The proof uses an exhaustive **finite** table only for the fixed binary five-vertex-word graph; it makes no inference about larger alphabet or graph orders.

## Relationship to prior work

Boutin, Horan Goliber and Pelto gave the general lower bound \(q^{n-1}(q-1)\), optimal constructions at lengths \(n\ge2t\), and a nonoptimal upper construction of size \(q^{n-1}(q-1)+q^t\) at the critical length \(n=2t-1\). The original public arXiv record dates to December 18, 2014; the later revised preprint and author-hosted manuscript preserve the critical-case question. Their known results imply here the **lower bound of 16** and the **upper bound of 24**, but do not determine the actual optimum or classify the equality cases. The radius-two, length-three nonbinary case is a different graph and radius and does not imply the present claim.

The new result is only the sharp binary radius-three/length-five boundary case and its complete classification; the general lower bound, existence condition, and all other published constructions are acknowledged as prior work.

## Limitations

The classification holds for binary words of length five and radius three only. It does not establish optimality for arbitrary alphabet sizes, longer critical lengths, other radii, or undirected de Bruijn graphs. The proof relies on finite exact comparisons and complete candidate enumeration but does not require a solver or treat finite experiments as an infinite theorem. Historical priority has been checked against relevant research records and accessible primary texts, but an unindexed equivalent enumeration remains possible; independent scientific and historical-priority validation has not been performed.

## References

1. D. Boutin, V. Horan Goliber, and M. Pelto, *Identifying Codes on Directed De Bruijn Graphs*, first publicly posted December 18, 2014, arXiv:1412.5842. Original record: https://arxiv.org/abs/1412.5842 ; revised full text: https://arxiv.org/pdf/1412.5842 . See Theorems 3.5, 3.6, 3.9, and the critical-length discussion.
2. D. Boutin, V. Horan Goliber, and M. Pelto, author-hosted manuscript of *Identifying Codes on Directed De Bruijn Graphs*, https://people.hamilton.edu/dboutin/publicationpdfs/boutingoliberpelto . See the full critical-length discussion in Section 3.
