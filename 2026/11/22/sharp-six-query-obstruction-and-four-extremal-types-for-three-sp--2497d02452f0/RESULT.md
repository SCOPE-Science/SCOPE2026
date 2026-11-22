# Sharp six-query obstruction and four extremal types for three-sparse binary parity

## Finding
Let \(\mathcal P_n^{(3)}\) consist of the Boolean functions \(h_{ijk}(x)=x_i\oplus x_j\oplus x_k\), with three **distinct** coordinate indices \(1\le i<j<k\le n\), acting on the complete query domain \(\mathbb F_2^n\). Let \(N_3(d)\) be the least number of coordinates permitting a set of \(d\) input queries whose every \(d\)-bit answer pattern is attained by some \(h_{ijk}\). Then
\[
\boxed{(N_3(3),N_3(4),N_3(5),N_3(6))=(6,7,8,10).}
\]
For **nine** coordinates and **six** fixed input queries, at most \(63\) of the \(64\) possible labels can occur, and this bound is sharp. Up to invertible relabeling of the six queries, the trace profile depends only on the three-dimensional kernel of the six-by-nine coordinate-signature matrix. Exactly \(2304\) such kernels attain \(63\) traces. Under permutation of the nine coordinates they form exactly four orbits, of sizes \(1260,756,252,36\). Reduced-row-echelon bases, encoded as ordinary nine-bit integers from least significant to most significant coordinate, may be chosen as
\[
(5,62,448),\quad(5,14,496),\quad(1,10,508),\quad(1,2,508),
\]
respectively. These are exact finite classifications, not asymptotic statements.

## Assumptions and scope
Everything is over the binary field. The parity hypotheses use **exactly three** mutually distinct coordinate positions, not one, two, or at most three. The query domain is all binary words of length \(n\). The number \(N_3(d)\) concerns static VC shattering of \(d\) distinct queried words, not an adaptive mistake tree. In particular, existence at \(n\) implies existence at every larger coordinate count by padding unused coordinates. The classification makes no assertion about thresholds beyond \(d=6\), or about Littlestone dimension.

For a list \(x^{(1)},\ldots,x^{(d)}\) of candidate queries define the \(d\)-bit signature of coordinate \(i\) by \(v_i=(x_i^{(1)},\ldots,x_i^{(d)})\). Then the complete set of observed label words is the restricted triple sumset \(\{v_i\oplus v_j\oplus v_k:i<j<k\}\). Thus the question is equivalent to covering all of \(\mathbb F_2^d\) with the XORs of three distinct indexed columns (equal column values are allowed at different positions). This equivalence is used in both directions.

## Proof
**Signature reduction.** Evaluation of the three-coordinate parity hypothesis \(h_{ijk}\) on the fixed query list gives the label word \(v_i\oplus v_j\oplus v_k\), by coordinatewise associativity. Conversely, any list of \(n\) binary \(d\)-bit signatures defines \(d\) input words by transposing their bit matrix; if all \(2^d\) distinct label words occur, no two input rows can be equal, so they are genuinely distinct queries. This proves the reduction exactly.

**Quotient enumeration.** Write \(W_3\) for the set of binary words of Hamming weight three in \(\mathbb F_2^n\). Any \(d\)-by-\(n\) signature matrix \(A\) yields exactly the label set \(A(W_3)\). If \(\operatorname{rank}(A)<d\), fewer than \(2^d\) patterns are possible. Otherwise \(K=\ker(A)\) has dimension \(k=n-d\), and \(A(W_3)\) is in bijection with those cosets of \(K\) that intersect \(W_3\). In particular its cardinality depends on \(K\), not on the chosen quotient isomorphism. Conversely, every \(k\)-plane is the kernel of a full-rank map \(A\), so checking all \(k\)-planes checks all possible shattering query supports up to an invertible transformation of their labels.

Each \(k\)-plane has a **unique** reduced row echelon basis. Enumerate all increasing pivot positions \(p_1<\cdots<p_k\); in row \(i\), pivot \(p_i\) is one, other pivot columns are zero, every earlier column is zero, and every later nonpivot column can independently be zero or one. This lists every plane exactly once. For each weight-three \(w\), eliminate its pivot bits with those rows and count the distinct resulting coset representatives. The implementation `enumerate.cpp` performs this exhaustive enumeration and `independent.py` independently checks it by marking the entire union \(W_3+K\), dividing its size by \(2^k\). Their results agree.

The complete test profiles required for the thresholds are:

| \(n\) | \(d\) | \(k=n-d\) | Number of kernels | Maximum traces | Kernels with all \(2^d\) traces |
|---:|---:|---:|---:|---:|---:|
| 5 | 3 | 2 | 155 | 7 | 0 |
| 6 | 3 | 3 | 1395 | 8 | 1120 |
| 6 | 4 | 2 | 651 | 14 | 0 |
| 7 | 4 | 3 | 11811 | 16 | 4480 |
| 7 | 5 | 2 | 2667 | 26 | 0 |
| 8 | 5 | 3 | 97155 | 32 | 1120 |
| 9 | 6 | 3 | 788035 | 63 | 0 |

In each row the enumerated number equals the Gaussian binomial coefficient \(\binom nk_2=\prod_{j=0}^{k-1}(2^{n-j}-1)/(2^{k-j}-1)\). These counts and the two logically different coset-evaluation methods establish **exhaustive** failure at the indicated smaller coordinate counts; failed searches or timeouts are not used as impossibility evidence. For \(d=6,n\le8\) there are at most \(\binom83=56<64\) hypotheses, so only \(n=9\) needs the nontrivial exhaustive obstruction. For \(d=3,4,5\), monotonicity then excludes all smaller \(n\) once the displayed predecessor fails.

**Explicit constructions.** For \((d,n)=(3,6),(4,7),(5,8),(6,10)\), the following lists of coordinate signatures respectively cover all \(2^d\) label words via XOR of three distinct indices:

```
(3,6):  0,0,0,1,2,4
(4,7):  0,0,12,1,2,4,8
(5,8):  0,24,7,1,2,4,8,16
(6,10): 0,0,0,63,1,2,4,8,16,32
```

`verify_witnesses.py` directly recomputes all triple XORs. For the last construction, the three zero columns and six basis columns cover weights zero through three; the all-ones column together with two other columns covers weights four through six. Deleting one zero yields the nine-column support \(0,0,63,1,2,4,8,16,32\), which realizes **exactly** the 63 nonzero label words and misses zero. This supplies sharpness of the nine-column obstruction independently of enumeration.

**Extremal orbit classification.** The exhaustive enumerator finds precisely \(2304\) kernels covering 63 cosets, recorded as their canonical RREF bases in `best_kernels_9.txt`. The second verifier reproduces that number by an independent coset-union method. The script `verify_orbits.py` starts with exactly those 2304 canonical bases and applies all eight adjacent coordinate transpositions, reducing each transformed basis to RREF. These transpositions generate \(S_9\); graph-orbit traversal therefore gives all coordinate-permutation orbits. It obtains the four orbit sizes and representatives above, whose sizes sum to \(2304\). This is a full orbit enumeration, not a partial heuristic.

## Verification
Compile `enumerate.cpp` with a standard C++17 compiler and run it for all seven \((n,k)\) profiles in the table, including `./enumerate 9 3`. Run `python3 independent.py` for an independently parameterized whole-coset check (the full seven-profile run requires no dependencies beyond the Python standard library). Run `python3 verify_witnesses.py` to test all displayed signature examples, and `python3 verify_orbits.py` to check the four symmetry orbits against the included exact best-kernel list. The file `independent_results.jsonl` records the complete quotient-coverage frequency distribution for each profile. All sources and finite witnesses are included within this package. Full coverage has a finite, exhaustive certificate for the **specified** small parameters only; nothing is inferred for unexamined \(d\).

## Relationship to prior work
Achlioptas and Theodoropoulos (2017) study sparse XOR constraints and their LDPC structure as a tool for probabilistic model counting, motivating exact-weight parity restrictions but not identifying the present three-coordinate static shattering thresholds or their extremal kernels. Guingona, Kolesnikov, Nierwinski and Soucy (2021) study the VC and Littlestone dimensions of much broader zero-set families of linear functions; taking an arbitrary nonzero linear combination does **not** characterize the exact-three-coordinate subfamily. A published technical study entitled *Static and adaptive shattering of two-coordinate parity hypotheses* reduces exact-two-coordinate parities to **two-summand** additive bases and computes thresholds for that different concept class. An exact binary functional-batch-code result of dimension three and six requests concerns multiple disjoint recovery sets, not one fixed-weight-three parity word for each output. The current claim is not a restatement or formal corollary of those inspected results. Historical priority remains open to additional, potentially unindexed, additive covering or coding references.

## Limitations
The obstruction at \((d,n)=(6,9)\) and its four-orbit census rely on exhaustive finite-state enumeration plus independently coded recomputation, not a closed-form conceptual upper-bound inequality. They are proved **only** for the explicitly listed small finite parameters. The 2304 count is of three-dimensional kernels, not of labeled six-by-nine matrices or of arbitrary query families of every rank. No adaptive-learning assertion, uniform asymptotic law, or unverified impossibility is claimed. No external independent audit or exhaustive historical-priority certification has been performed.

## References
1. D. Achlioptas and P. Theodoropoulos, *Probabilistic Model Counting with Short XORs*, arXiv:1707.09467v1 (first posted 2017-07-29), https://arxiv.org/abs/1707.09467.
2. V. Guingona, A. Kolesnikov, J. Nierwinski, and R. Soucy, *Littlestone and VC-Dimension of Families of Zero Sets*, arXiv:2109.04805v1 (first posted 2021-09-10), https://arxiv.org/abs/2109.04805.
3. *Static and adaptive shattering of two-coordinate parity hypotheses*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-static-and-adaptive-shattering-of-two-coordinate-parity-hypothes--7499a8b054ac.
4. *Exact binary dimension-three six-request functional batch length*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-exact-binary-dimension-three-six-request-functional-batch-length--4abf711d3224.
