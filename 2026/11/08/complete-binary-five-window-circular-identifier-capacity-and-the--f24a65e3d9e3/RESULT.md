# Complete binary five-window circular identifier capacity and the seven-position obstruction

## Finding

Let \(E(2,k,5)\) be the largest number of length-\(k\) cyclic binary identifiers that can be assigned simultaneously so that every cyclic five-bit window identifies both an identifier and a starting position. Thus the windows within each identifier are distinct, and the window sets for different identifiers are disjoint. For **every integer \(k\geq5\)**,

\[
E(2,k,5)=
\begin{cases}
3,&k=7,\\
\lfloor32/k\rfloor,&k\ne7.
\end{cases}
\]

In particular, seven-position identifiers have a strict packing loss: four identifiers would use only \(28\) of the \(32\) possible windows, but no four can be realized. Three can be realized.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). A length-\(k\) circular identifier \(w=w_0\cdots w_{k-1}\) is read cyclically with indexed starting position, and its five-window set is

\[
W_5(w)=\{w_iw_{i+1}w_{i+2}w_{i+3}w_{i+4}:i\in\mathbb Z/k\mathbb Z\}.
\]

An admissible family \(\mathcal C\) satisfies \(|W_5(w)|=k\) for each \(w\in\mathcal C\), and \(W_5(w)\cap W_5(v)=\varnothing\) for distinct \(w,v\in\mathcal C\). Rotations of the same word are one identifier, not independent messages. The parameter \(k\) is any integer at least five, including lengths beyond the window alphabet size. There are no stochastic or noisy observations and no reversal equivalence.

The conventional eBug number \(E(q,k,\ell)\) is exactly this capacity with alphabet size \(q\) and window length \(\ell\), as formulated by Grubman, Şekercioğlu and Wood [1].

## Proof

**General upper bound.** There are \(2^5=32\) possible five-bit windows. Every admissible length-\(k\) identifier consumes exactly \(k\) of these, without reuse by any other identifier. Hence

\[
E(2,k,5)\le\lfloor32/k\rfloor.
\]

For \(k>32\), no single admissible identifier exists, and the claimed value is zero.

**Matching constructions except at seven.** The accompanying `witnesses.json` contains explicit binary cycles for every \(k=5,6,8,9,\ldots,32\). The number of listed cycles is exactly \(\lfloor32/k\rfloor\) for each such \(k\). Each listed word has length \(k\), its \(k\) cyclic five-windows are pairwise distinct, and the window sets of all words listed for the same \(k\) are disjoint. These are finite explicit witnesses, not inferred from a partial search. The checks can be carried out by reading the windows directly; `verify.py` and `verify_independent.py` carry out these checks by separately implemented methods. Thus every nonexceptional upper bound is attained. At \(k=5\), the six cycles are precisely the nonconstant binary necklaces of length five, an observation already implicit in [1].

**Exhaustive obstruction at seven.** The complete list of cyclic seven-bit binary words with seven *different* five-windows, written in least-rotation form, is partitioned into three rows:

| Row | Complete list of valid cyclic words |
|---|---|
| A | `0000011`, `0000101`, `0000111`, `0001011`, `0001101` |
| B | `0001111`, `0010111`, `0011101`, `0011111`, `0101111` |
| C | `0010011`, `0011011` |

There are \((2^7+6\cdot2)/7=20\) binary rotation classes of length seven. Two are constant; among the other eighteen, exactly the following six repeat a cyclic five-window: `0000001`, `0001001`, `0010101`, `0101011`, `0110111`, `0111111`. The remaining twelve are precisely the table above. This classification can also be verified without any graph enumeration: generate the \(2^7\) binary strings, retain the least rotation in each class, and calculate the seven cyclic five-windows of each. The complete direct verifier does so.

Within **each** of rows A, B and C, every two listed cycles share at least one five-window. These are only \(10+10+1=21\) explicit pair comparisons, all checked by `verify.py`. Therefore an admissible family can contain at most one cycle from each row, and thus at most three cycles in total.

Finally the three cycles `1010000`, `1110001` and `0110010` each have seven distinct five-windows, and their three sets of windows are mutually disjoint. They supply an admissible family of size three. Hence \(E(2,7,5)=3\), completing the proof.

The graph interpretation gives the same statement: these codes are packings of vertex-disjoint directed length-\(k\) cycles in the 32-vertex binary de Bruijn graph of order five [1]. The second verifier independently enumerates its twelve length-seven directed cycles and checks the absence of a disjoint quadruple.

## Verification

The finite data and checks are provided as `witnesses.json`, `verify.py` and `verify_independent.py` in this package. From a directory containing all four files, including this document, run:

```text
python3 verify.py
python3 verify_independent.py
```

The first program checks the exact witness count and all cyclic five-windows for each \(5\le k\le32\), enumerates all binary seven-necklaces, and validates the 12-cycle partition and all 21 intersection comparisons. The second program separately enumerates directed seven-cycles on 32 de Bruijn vertices, checks all quadruples and at least one disjoint triple, and independently recomputes the constructed packings from the listed words. Both checks passed on the complete files. The argument for \(k>32\) is the elementary pigeonhole bound and does not depend on computation.

## Relationship to prior work

Grubman, Şekercioğlu and Wood [1], first publicly available on 2015-02-08, introduce the exact eBug number, its de Bruijn-cycle interpretation, the capacity upper bound, and several constructions. Their paper includes the binary five-window setting (including an example with eight positions) and identifies the prime-alphabet / prime-window regime as a gap in its methods. It does **not** supply the complete \(E(2,k,5)\) profile or the seven-position obstruction in the inspected abstract, problem statement, main theorems, constructions, and conclusion. The present result does not claim novelty for the graph formulation, the counting upper bound, or any isolated construction already implied by those theorems.

Cameron, Gündoğan and Sawada [2] describe the existence and efficient generation of a *single* cut-down de Bruijn cycle of a prescribed length, which does not imply that several cycles of that length can be made vertex-disjoint. Álvarez et al. [3] address the largest number of disjoint cycles without imposing a common prescribed length, together with extremal factors of related graphs; their conclusion does not imply this fixed-length packing profile. Their papers are relevant for terminology and general methods but do not settle the exceptional \(k=7\) comparison.

## Limitations

This is an exact theorem for **binary**, **five-consecutive-symbol**, **noise-free**, **rotation-aware** circular identifiers only. It makes no claim about alphabet sizes above two, other window lengths, reversal-blind cameras, symbol errors, or optimizing additional physical constraints. The construction is explicit but not asserted to be unique. The result has been checked in the cited literature and research records to the extent described in the accompanying review; historical-priority verification by an independent specialist has not been performed.

## References

[1] T. Grubman, Y. A. Şekercioğlu and D. R. Wood, *Partitioning de Bruijn Graphs into Fixed-Length Cycles for Robot Identification and Tracking*, first preprint 2015-02-08, arXiv:1502.02199, https://arxiv.org/pdf/1502.02199; later *Discrete Applied Mathematics* 213 (2016), 101–113, https://doi.org/10.1016/j.dam.2016.05.013.

[2] B. Cameron, A. Gündoğan and J. Sawada, *Cut-Down de Bruijn Sequences*, arXiv:2205.02815, https://arxiv.org/pdf/2205.02815.

[3] N. Álvarez, V. Becher, M. Mereb, I. Pajor and C. M. Soto, *On Extremal Factors of de Bruijn-like Graphs*, arXiv:2308.16257, https://arxiv.org/pdf/2308.16257.
