# Exact binary two-list single-deletion optima through length seven

## Finding

Let \(A_2(n;1,2)\) be the largest size of a binary length-\(n\) code for which every exact single-deletion output belongs to no more than two distinct codewords. For every integer \(n\) from \(2\) through \(7\),

\[
\bigl(A_2(n;1,2)\bigr)_{n=2}^{7}=(3,4,7,12,19,33).
\]

At \(n=7\), the value \(33\) is strictly larger than \(32\), the size of the union of any two distinct Varshamov--Tenengolts syndrome classes (all eight classes have size \(16\)). Moreover, since a binary length-seven uniquely single-deletion-correcting code has at most \(16\) codewords [3], an optimal \(33\)-word two-list code cannot be expressed as the union of two uniquely single-deletion-correcting codes. This structural separation does not follow from the mere existence of two syndrome classes.

## Assumptions and scope

All words are finite binary strings; leading zeros are retained. For a word \(x=x_1\cdots x_n\), let \(D(x)\) denote the **set**, not multiset, of length-\(n-1\) words obtained by deleting exactly one position. A code \(C\subseteq\{0,1\}^n\) is admissible when

\[
\forall y\in\{0,1\}^{n-1},\quad
\bigl|\{x\in C:y\in D(x)\}\bigr|\le2.
\]

Every integer \(2\le n\le7\) is included, and there is no claim for longer lengths, other alphabets, or more deletion errors. This is worst-case combinatorial list decodability, not an average channel-error statement.

## Proof

Index each length-\(n\) word by its usual \(n\)-bit integer \(j\), from \(0\) to \(2^n-1\), retaining leading zeros. Index outputs analogously. Set \(M_{yj}=1\) if the output indexed by \(y\) belongs to \(D(j)\), and set it to zero otherwise. The model is the finite integer packing problem

\[
\max\sum_j z_j,\qquad
\sum_j M_{yj}z_j\le2\quad(\forall y),\qquad z_j\in\{0,1\}.
\]

The file `certificate.json` supplies an explicit feasible set of codeword indices for each of the six blocklengths. The independent checker recomputes every deletion output from the displayed indices and tests all output multiplicities, so the lower bounds are exact.

For upper bounds, the certificate gives a finite binary decision tree covering all \(2^{2^n}\) possible selected-word subsets without enumerating them individually. A branch forces one variable to \(1\) or \(0\). Write \(P\) for the forced-one indices, \(Z\) for the forced-zero indices, and \(F\) for all remaining indices. For each output, the residual capacity is

\[
r_y=2-\sum_{j\in P}M_{yj}.
\]

A branch is impossible if any \(r_y<0\). Otherwise each rational-dual leaf supplies nonnegative weights \(\alpha_y\) for outputs and \(\gamma_j\) for unassigned words such that

\[
\sum_y M_{yj}\alpha_y+\gamma_j\ge1\qquad(j\in F).
\]

It follows **for every integral or fractional admissible completion** that

\[
\sum_j z_j\le|P|+\sum_y r_y\alpha_y+\sum_{j\in F}\gamma_j.
\]

The actual stored multipliers are nonnegative integers divided by exactly \(10^8\). At every dual leaf the checker verifies all inequalities by integer arithmetic and verifies that the right-hand side is **strictly below** one more than the claimed optimum. Because a code size is an integer, this proves the upper bound. A count leaf instead verifies that even selecting every unassigned word cannot exceed the optimum. Every internal node checks both branches of a previously unfixed source index; hence the leaves exhaust all assignments.

For \(2\le n\le6\), one root dual certificate suffices for each length. For \(n=7\), the complete certificate has \(103\) nodes, including \(51\) binary branches and \(52\) independently checkable leaves. There is no reliance on the correctness or optimality announcement of the numerical program used to discover the witness: its complete proposed proof is validated using exact arithmetic by `checker.py`.

One explicit \(33\)-word code at length seven is

```
0000000 0000011 0000111 0001000 0001010 0001110 0010101
0011100 0011111 0100010 0101000 0101101 0110001 0110110
0110111 0111001 1000001 1001001 1001011 1001100 1001111
1010010 1011010 1011110 1100000 1100011 1100110 1110000
1110101 1110111 1111000 1111100 1111111
```

The eight standard length-seven VT residue classes, defined by the weighted coordinate sum modulo \(8\), each contain exactly \(16\) words. Their pairwise unions therefore have size \(32\). The comparison with arbitrary unions of two unique-deletion codes is also verified directly: `certificate.json` contains a separate capacity-one length-seven upper-bound tree of \(25\) nodes (with \(13\) leaves) and a feasible \(16\)-word code. Thus the capacity-one bound \(16\), already known in the literature [3], is independently certified in this package.

## Verification

In a directory containing `certificate.json` and `checker.py`, execute `python3 checker.py`. The checker requires only the standard Python library. It regenerates every binary source and deletion output, tests every supplied feasible code for both list capacity two and the supporting length-seven unique-decoding capacity-one case, checks all branching operations and all exact dual inequalities, and enumerates the VT syndrome-class sizes. Its verified output is `VERIFY_OK`, with the six optima and the branch counts given above. The mathematical correctness of the finite claims rests on these exact finite inequalities and constructive witnesses, not on an optimization solver's unverified termination status.

## Relationship to prior work

Lin [1] defines the general deletion list-decoding hypergraph and proves asymptotic bounds for arbitrary fixed deletion and list parameters. The present finite model is the exact \(k=1,t=2\) specialization; its six cardinalities and the length-seven separation from two unique-deletion codes are not stated in the inspected definitions and principal theorem. Kiah, Wei and Zeng [2] give constant-list insertion/deletion bounds and explicitly discuss a three-codeword length-two example, so the initial \(n=2\) value is already in that literature; their quantitative results do not imply the exact length-seven value. No [3] treats unique single-deletion correction (list size one), including the length-seven optimum \(16\), but not the capacity-two hypergraph problem. Published related finite results for two deletions and for one deletion together with substitutions address different output-incidence constraints; one does not imply the present capacity-two, one-deletion packing optimum.

The exact optimum \(33\) and the resulting non-decomposability statement are the contribution here. Priority relative to unindexed finite tables or computational studies cannot be guaranteed by the searches performed.

## Limitations

The profile is finite, not an all-length formula. No complexity bound for encoding or list decoding is established. A code of cardinality \(33\) need not be unique or structurally classified, and the certificate does not enumerate all optimal codes. The argument uses exact finite rational arithmetic but is not independently audited. Originality is assessed against the identified and inspected literature, not conclusively established against every possible historical source.

## References

[1] A. D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650, first public September 22, 2026. https://arxiv.org/abs/2609.26650

[2] H. M. Kiah, H. Wei and R. Zeng, *Constant-List Insertion--Deletion Codes: New Bounds and an Improvement of Levenshtein's Lower Bound*, arXiv:2609.21395, first public September 18, 2026. https://arxiv.org/abs/2609.21395

[3] A. No, *Nonasymptotic Upper Bounds on Binary Single Deletion Codes via Mixed Integer Linear Programming*, Entropy **21** (2019), 1202. https://doi.org/10.3390/e21121202

[4] V. Guruswami and J. Håstad, *Explicit two-deletion codes with redundancy matching the existential bound*, arXiv:2007.10592, first public July 21, 2020. https://arxiv.org/abs/2007.10592
