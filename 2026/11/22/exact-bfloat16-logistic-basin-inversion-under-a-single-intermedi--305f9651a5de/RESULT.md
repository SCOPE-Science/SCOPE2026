# Exact bfloat16 logistic basin inversion under a single intermediate rounding

## Finding

Let \(S\) consist of the 16,257 distinct nonnegative bfloat16 numbers in \([0,1]\), including subnormals and the positive zero encoding; let \(R\) denote rounding to the nearest bfloat16 value with ties resolved to even. At logistic parameter four, compare the two precisely specified finite maps
\[
A(x)=R\bigl(4x(1-x)\bigr),\qquad
B(x)=R\bigl(4x\,R(1-x)\bigr),\qquad x\in S.
\]
Operations not surrounded by \(R\) are exact real operations. In particular, multiplication by four is exact before the displayed final rounding. No other intermediate rounding, reassociation, or implicit floating-point promotion is assumed. Both maps take \(S\) into itself.

The **complete** functional graphs have the following primitive cycles, basins (including all periodic states), and least unsigned bfloat16 cycle encodings:

| Map | Least cycle encoding | Least period | Basin cardinality |
| --- | --- | ---: | ---: |
| \(A\) | `0x0000` | 1 | 4,374 |
| \(A\) | `0x3f40` | 1 | 65 |
| \(A\) | `0x3dbc` | 11 | 11,818 |
| \(B\) | `0x0000` | 1 | 14,797 |
| \(B\) | `0x3f40` | 1 | 65 |
| \(B\) | `0x3e8d` | 4 | 1,395 |

In both maps `0x3f40` is the real fixed state \(3/4\). There are no other periodic orbits. The respective maximum numbers of steps to first enter a cycle are 81 and 99, and the sums of first-entry times over all encodings are 623,656 and 773,744.

**Basin inversion:** of the 16,257 successor edges, exactly **275** differ between \(A\) and \(B\). Nevertheless the exact cross-classification of all starting states is

| Basin under \(A\) | Basin under \(B\) | Number of starting codes |
| --- | --- | ---: |
| Zero | Zero | 4,374 |
| Eleven-cycle | Zero | 10,423 |
| Eleven-cycle | Four-cycle | 1,395 |
| Three-quarter fixed point | Three-quarter fixed point | 65 |

All other intersections are empty. Thus a change in only 275 one-step edges sends **10,423** of the 16,257 initial encodings from a nonfixed period-eleven basin to the absorbing zero fixed point. This is an exact finite-state statement, not a claim about probabilities under Lebesgue measure.

## Assumptions and scope

The unsigned bfloat16 encoding has one sign bit, eight exponent bits with bias 127, and seven stored fraction bits. The domain uses exactly the nonnegative codes `0x0000` through `0x3f80` inclusive, with negative zero excluded. All computations use gradual underflow and round-to-nearest, ties-to-even. The encoded values are interpreted as exact dyadic rationals, and both displayed \(R\) operators perform mathematically correct rounding. These definitions do not prescribe the hidden arithmetic of a compiler or a floating-point hardware platform; \(A\) and \(B\) are two explicitly specified evaluation trees, not interchangeable implementations.

A basin is the set of initial codes whose unique forward orbit reaches a stated cycle. Periods, transient lengths, and basin cardinalities refer to the discrete graph on \(S\). Uniform counting on the encodings is **not** a uniform distribution of real initial conditions. The domain includes \(x=1\), which maps to zero under either rule.

## Proof

**Exact encoding grid.** Put \(U=2^{133}\) and write a nonnegative code \(j=128e+f\), where \(0\le f<128\). The integer \(v_j=Ux_j\) is
\[
v_j=\begin{cases}f,&e=0,\\ (128+f)2^{e-1},&e\ge1.\end{cases}
\]
In the relevant range the integer list \((v_j)_{0\le j\le\texttt{0x4080}}\) is strictly increasing, with \(v_{\texttt{0x3f80}}=U\) and \(v_{\texttt{0x4080}}=4U\). The extended grid through four contains all output-rounding candidates. The unit scaling is exact, including for subnormals.

For a nonnegative rational argument \(a/b\) expressed in the scaled integer units, define \(Q(a,b)\) to be the code minimizing \(|a-bv_j|\), choosing the *even* code at a tie. Since the finite grid is strictly ordered, binary search locates the two neighboring candidates; comparison of their integer gaps determines \(Q\) without approximate arithmetic. For input code \(i\) with scaled value \(v_i\), the complete successor functions are
\[
\begin{aligned}
 a_i&=Q\bigl(4v_i(U-v_i),U\bigr),\\
 k_i&=Q(U-v_i,1),\\
 b_i&=Q\bigl(4v_i v_{k_i},U\bigr).
\end{aligned}
\]
Direct exhaustive evaluation for every integer code \(0\le i\le\texttt{0x3f80}\) verifies \(a_i,b_i\le\texttt{0x3f80}\), so both maps preserve their stated domain. The loop constructs exactly 16,257 successors for each map; there are no unexamined initial values.

**Complete graph classification.** For each unclassified vertex, follow its unique successor until reaching either a labeled vertex or a vertex already visited in the present traversal. In the second case, the repeated terminal segment is a complete primitive cycle. Label its members with distance zero; then label each preceding vertex in reverse order with its successor's cycle and distance plus one. If a previous labeled vertex is reached, only the reverse labels are needed. Induction along each reversed chain proves these labels correct. Every integer code is considered, hence every cycle and every basin is exhaustively included. This is a proof for the complete *finite* state space, not extrapolation from sampled orbits.

The standalone exact-arithmetic verifier computes the six cycle entries in the table and checks that the basins sum to 16,257 for each map. As an independent graph traversal check it also removes all zero-indegree vertices, identifies cycles in the remaining core, and propagates labels backward through incoming edges; this reproduces the full four-cell basin-cross table above. A second rounding implementation based on exact rational `Fraction` distances reproduces **all 32,514 one-step successors** (and the staged intermediate rounding at every state). Therefore the key numerical assertions follow from explicit exhaustive integer operations with independently cross-checked rounding and graph procedures.

**Whole-transition witnesses.** The SHA-256 digests of the complete arrays of 16-bit successor codes, serialized in ascending input-code order with each successor in unsigned little-endian form, are

- \(A\): `6efc7e1f5494acc14c02fdcdcfcf81312842f5c55761c31ff024202ef8e2964e`;
- \(B\): `e310df8a10ff661ac6d08e6dca42337365c254b48be4dd074f99f2a731ed7870`.

These digests supplement, but do not replace, the exhaustive mathematical and arithmetic checks implemented in `verify.py`.

## Verification

From a directory containing this result and `verify.py`, run `python3 verify.py`. It requires only the Python 3 standard library and prints `BFLOAT16_EXACT_LOGISTIC_GRAPHS_OK` after completing both state graphs, both independent graph decompositions, all 16,257 independent exact-rational neighbor checks, midpoint-tie checks, and the recorded digests and cross-basin table. This was executed on the delivered verification source with no external numerical library.

## Relationship to prior work

Klöwer, Coveney, Paxton and Palmer's public 2022 preprint, followed by its 2023 open-access article, explains spurious stabilization and periodic collapse in reduced-precision simulations. The 2023 article explicitly includes bfloat16 logistic bifurcation diagrams and identifies severe fidelity issues, but it does not compute either fully specified finite successor graph, its exact 16,257-state basin census, or the 275-edge/10,423-basin transition.

Sayed, Radwan, Rezk and Fahmy (2017) study finite *fixed-point* arithmetic, operation order and logistic periods, not nearest-even bfloat16. Miyazaki and collaborators (2011) study rounding in integer representations of logistic maps, with no demonstrated coverage of the two specific bfloat16 graphs; only the abstract was accessible in this examination. Recently published exact binary16 logistic graph classifications concern the **different** 5-exponent/10-fraction IEEE half format and other evaluation trees. Those results already document evaluation-sensitive periodic spectra, which is prior knowledge, but neither the state sets nor the rounding edges agree with bfloat16; they do not imply these cycle and basin counts. The real logistic conjugacy and familiar finite-graph enumeration algorithm are likewise background, not claimed as discoveries.

The increment here is an exact, natural bfloat16 census and its unexpectedly large **basin inversion across just 275 changed edges**. It is motivated by the explicitly investigated bfloat16 phenomenon and quantifies the attracting-set dependence which a bifurcation plot or Monte Carlo sample cannot certify. This is not a general theorem predicting spectra at arbitrary parameters or formats.

## Limitations

The result applies only at logistic parameter four, to nonnegative bfloat16 states in \([0,1]\), and to the two exact rounding trees specified above. It does not establish the exact operation order of published software plots, forecast behavior in higher dimensions, or a uniform real-initial-condition basin proportion. The full-period and basin assertions are exhaustive **finite** computations only; they do not establish new infinite-state dynamics. Independent mathematical review has not been performed. Publication-priority risk remains for unindexed implementations or a prior identical bfloat16 census not exposed by the inspected sources.

## References

1. M. Klöwer, P. V. Coveney, E. A. Paxton, T. N. Palmer, *Periodic orbits in chaotic systems simulated at low precision*, Research Square preprint posted 8 November 2022, https://doi.org/10.21203/rs.3.rs-2223046/v1; expanded open-access article, *Scientific Reports* **13** (2023), 11410, published 14 July 2023, https://doi.org/10.1038/s41598-023-37004-4; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC10349059/.
2. W. S. Sayed, A. G. Radwan, A. A. Rezk, H. A. H. Fahmy, *Finite Precision Logistic Map between Computational Efficiency and Accuracy with Encryption Applications*, *Complexity* (2017), 8692046, https://doi.org/10.1155/2017/8692046.
3. T. Miyazaki, S. Araki, Y. Nogami, S. Uehara, *Rounding Logistic Maps over Integers and the Properties of the Generated Sequences*, *IEICE Transactions* E94-A (2011), 1817–1825, https://doi.org/10.1587/transfun.E94.A.1817 (abstract inspected).
4. *Two exact binary16 logistic cycle spectra under algebraically equivalent evaluation* (2026), public research record https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-exact-binary16-logistic-cycle-spectra-under-algebraically-eq--35a3ca4a276d.
5. *Exact complete expanded-evaluation binary16 logistic cycle census* (2026), public research record https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-incompatible-complete-cycle-spectra-for-half-precision-log--46d23de07c7c.
