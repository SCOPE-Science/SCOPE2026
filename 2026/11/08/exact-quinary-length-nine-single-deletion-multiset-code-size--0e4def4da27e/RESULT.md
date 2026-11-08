# Exact quinary length-nine single-deletion multiset code size

## Finding

For the alphabet \(\{0,1,2,3,4\}\), a length-nine multiset is a vector \(x\in\mathbb Z_{\ge0}^{5}\) with \(\sum_{i=0}^4 x_i=9\). A *one-deletion-correcting multiset code* is a set \(C\) of these vectors such that two different members cannot yield the same vector of total weight eight after decrementing one positive coordinate. The exact maximum is

\[
S_5(9,1)=143.
\]

The size is achieved by the residue-zero code

\[
C_0=\left\{x:\sum_{i=0}^4 i x_i\equiv0\pmod5\right\}.
\]

This settles the length-nine instance of the quinary single-deletion optimality conjecture in the cited 2026 paper. It does not settle that conjecture for all blocklengths.

## Assumptions and scope

All symbols are distinguishable types, but occurrences of the same type are indistinguishable; there is no positional order. Deletion removes exactly one occurrence of an arbitrary present symbol. Codes are arbitrary subsets of the \(715\) possible length-nine multisets, with no linearity or symmetry restriction. The quantity \(S_5(9,1)\) is the unrestricted maximum cardinality.

## Proof

**Reduction to a finite integer program.** Write \(V=\{x\in\mathbb Z_{\ge0}^5: \sum_i x_i=9\}\) and \(P=\{y\in\mathbb Z_{\ge0}^5: \sum_i y_i=8\}\). Stars-and-bars gives \(|V|=\binom{13}{4}=715\) and \(|P|=\binom{12}{4}=495\). For \(y\in P\), the five possible one-symbol extensions are \(N(y)=\{y+e_i:0\le i\le4\}\), where \(e_i\) is the \(i\)-th coordinate unit vector.

Two distinct codewords share a one-deletion output if and only if both belong to the same \(N(y)\). Thus the mathematical optimization is *exactly* the following finite binary integer program, with one variable \(u_x\) for every \(x\in V\):

\[
\begin{aligned}
\text{maximize }&\sum_{x\in V}u_x,\\
\text{subject to }&\sum_{i=0}^{4}u_{y+e_i}\le1\quad(y\in P),\\
&u_x\in\{0,1\}\quad(x\in V).
\end{aligned}
\]

This proves both directions of the reduction: every valid code yields a feasible integral vector, and every feasible integral vector picks a valid code. The model has exactly \(715\) binary variables, \(495\) five-term inequalities, and \(2475\) nonzero coefficients.

**Constructive lower bound.** The checksum \(\sigma(x)=\sum_i i x_i\pmod5\) changes by \(i\pmod5\) when a symbol of type \(i\) is added to a received multiset. Therefore distinct extensions of the same \(y\) have different checksums. Every checksum class is a valid one-deletion code. Cyclically relabeling symbol types \(i\mapsto i+1\pmod5\) changes the checksum of a length-nine multiset by \(9\equiv4\pmod5\). Because repeated addition of four reaches every residue, the five checksum classes are equinumerous, hence each contains \(715/5=143\) vectors.

**Exhaustive upper bound.** The complete binary integer program is generated and solved by the included `checker.py`. A HiGHS branch-and-bound global optimization run reports status `0` (optimal), an integral optimum \(143\), a minimizing-objective dual bound \(-142.99999999999955\), and a zero relative mixed-integer gap. This excludes feasible cardinality \(144\) or larger, because the objective is integer. The checker also independently tests all \(\binom{143}{2}=10153\) pairs in the explicit checksum code.

For additional cross-validation, `checker_edges.py` uses a different model: it enumerates all \(4950\) unordered distance-one pairs of the \(715\) vertices and imposes one two-term incompatibility constraint per pair, rather than the preceding five-term inequalities. Its independent branch-and-bound optimization likewise reports optimum \(143\) and a zero gap. Both programs construct their complete models from the definitions, not from stored search logs or external input tables.

Together the explicit lower-bound construction and the complete finite optimization yield \(S_5(9,1)=143\).

## Verification

Run `OPENBLAS_NUM_THREADS=1 python checker.py` and `OPENBLAS_NUM_THREADS=1 python checker_edges.py` with the dependency versions described in `requirements.txt`. Both are executable source files and regenerate every variable, neighbor relation and constraint. Successful completion requires global solver status `0`, an optimal objective of \(143\), an upper-bound certificate from the solver's branch-and-bound search, and direct solution-feasibility assertions. The paired models provide an independent combinatorial encoding of the same optimization.

The proof of the finite upper bound is computational and depends on correct functioning of the integer-programming implementation. These files do **not** contain a separate machine-checkable rational infeasibility certificate for the hypothetical size-\(144\) instance. A solver timeout, a nonoptimal status, or merely finding a code of size \(143\) is *not* a proof of the upper bound. The reported full-optimization statuses, rather than incomplete searches or the displayed decimals alone, are essential.

## Relationship to prior work

Kreindel, Barouch Essayag and Zabokritskiy's *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results* (first public January 9, 2026), arXiv:2601.05636, Section 5.5, reports exact quinary values for lengths \(1\) through \(8\) and states as Conjecture 21 that the finite-field checksum construction is optimal except for two small exceptions. Its results cover the lower-bound construction at length nine but do not contain this length-nine exact upper bound; it identifies the absence of general higher-dimensional simplex-grid independence formulas.

The same authors' *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes* (first public March 18, 2026), arXiv:2603.18322, develops general constructions and ball-volume bounds rather than this exact length-nine independence number. The broader Kovačević–Tan bounds recalled in the first paper give asymptotic information but do not imply equality at this finite parameter. The problem is one of multiset codes, not ordinary length-nine sequence deletion codes.

## Limitations

This exact statement concerns one deletion from five-symbol *multisets* of length nine. It does not give a general formula for other alphabet sizes, deletion radii or lengths, and it does not classify all optimal codes. The upper-bound demonstration is a reproducible complete mixed-integer computation using a floating-point implementation, not a standalone exact-rational proof certificate. Independent mathematical validation and comprehensive historical-priority confirmation have not been performed.

## References

1. A. Kreindel, I. Barouch Essayag, A. L. Zabokritskiy, *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, arXiv:2601.05636v2, Section 5.5, Conjecture 21; first public January 9, 2026. https://arxiv.org/html/2601.05636v2
2. A. Kreindel, I. Barouch Essayag, A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322v1; first public March 18, 2026. https://arxiv.org/html/2603.18322v1
3. N. Kovačević and V. Tan, foundational multiset/permutation-channel coding results, as cited and analyzed in reference 1.
