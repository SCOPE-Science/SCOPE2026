# The first fractional shadow-packing gap for Fibonacci-constrained one-asymmetric-error codes

## Finding
For binary length-\(n\) words with no adjacent ones transmitted over an adversarial single-asymmetric-error channel (at most one \(1\to0\) change), the maximum disjoint-shadow code sizes for \(n=1,\ldots,7\) are
\[
(M_1,\ldots,M_7)=(1,1,2,3,4,6,8).
\]
Their natural fractional output-shadow packing values are
\[
(U_1,\ldots,U_7)=(1,1,2,3,4,6,9).
\]
In particular, the first strict fractional gap is at length \(7\), with ratio \(U_7/M_7=9/8\). Exactly ten labeled eight-word codebooks attain the integer optimum at length \(7\).

## Assumptions and scope
For integers \(n\ge1\), define \(F_n=\{x\in\{0,1\}^n: x_ix_{i+1}=0\text{ for }1\le i<n\}\). Positions are indexed and codebooks are subsets, not ordered lists. The channel is directed: the transmitted word may be unchanged or have *one* of its ones replaced by zero, but never the reverse or multiple changes. Its output shadow is
\[
D(x)=\{x\}\cup\{x-e_i:x_i=1\}.
\]
Every output is again in \(F_n\). The code capacity \(M_n\) is the maximum cardinality of a set \(C\subseteq F_n\) such that \(D(x)\cap D(x')=\varnothing\) for all distinct \(x,x'\in C\). The standard hypergraph output-shadow relaxation is
\[
U_n=\max\Big\{\sum_{x\in F_n}p_x:p_x\ge0,\quad\sum_{x:y\in D(x)}p_x\le1\ (y\in F_n)\Big\}.
\]
It has the covering dual \(\min\sum_{y\in F_n}w_y\), subject to \(w_y\ge0\) and \(\sum_{y\in D(x)}w_y\ge1\) for every \(x\in F_n\). Both LPs have finite feasible optima by elementary linear-programming duality.

## Proof
**Lengths one through six.** The `MAX_CODE` and `EARLY_DUAL` dictionaries in `verify.py` give an explicit codebook \(C_n\) and a set of read outputs \(Y_n\) for each \(1\le n\le6\). The codebook shadows are mutually disjoint. Every source shadow intersects \(Y_n\), and \(|C_n|=|Y_n|\). Assigning weight one to each read in \(Y_n\) and zero elsewhere gives a feasible dual solution of value \(|Y_n|\), while the code's indicator vector is a feasible integral primal solution of that value. Therefore \(M_n=U_n=|C_n|\) for every length through six. All memberships and intersections are checked exactly in `verify.py`, which enumerates every possible constrained source at these lengths.

**Seventh-length fractional value.** `FRACTIONAL_PRIMAL` in `verify.py` lists eleven rational nonzero source weights, each either \(1\) or \(1/2\), summing to \(9\). For every output \(y\in F_7\), the sum of weights of source words whose shadows contain \(y\) is at most one. `FRACTIONAL_DUAL` lists eleven nonzero output weights, also \(1\) or \(1/2\), summing to \(9\). Every one of the 34 source shadows has dual weight at least one. Hence \(U_7=9\), by weak duality (no numerical optimizer is needed).

**Seventh-length integer capacity.** The eight words listed under `MAX_CODE[7]` have pairwise disjoint output shadows, so \(M_7\ge8\). Each of the eight sets in `CLIQUES_7` consists of mutually confusable source words: for every two distinct members \(x,x'\), their output shadows intersect. The union of these eight cliques equals all 34 words of \(F_7\). A valid code can select at most one word from each clique; even though some cliques overlap, their union cover yields \(|C|\le8\). Thus \(M_7=8\) and the gap first occurs at length seven.

**Number of optimizers.** Form the 34-vertex conflict graph in which two vertices are adjacent precisely when their output shadows intersect. For every subset of vertices represented by a bitmask \(S\), let \((\alpha(S),h(S))\) be the maximum independent-set cardinality and the number of independent sets attaining it. Choose any \(v\in S\), put \(S_0=S\setminus\{v\}\) and \(S_1=S\setminus(\{v\}\cup N(v))\). The two exhaustive, disjoint alternatives are excluding \(v\) (\(\alpha(S_0),h(S_0)\)) or including \(v\) (\(1+\alpha(S_1),h(S_1)\)). Keep the larger cardinality and its count, or add counts in a tie. Base case \((\alpha(\varnothing),h(\varnothing))=(0,1)\); edgeless masks have \((|S|,1)\). The exact recurrence visits 2,035 distinct masks using deterministic maximum-current-degree branching and returns \((8,10)\) on the full 34-vertex mask. Every subproblem is smaller, so the recurrence is a finite exhaustive proof, not sampling.

## Verification
Run `python verify.py` with Python 3.9+ and its standard library only. It enumerates all 2, 3, 5, 8, 13, 21 and 34 admissible words at lengths one through seven, independently reconstructs every output shadow, tests every listed codebook and dual support, verifies all rational seventh-length primal/dual constraints using `fractions.Fraction`, checks the eight full confusability cliques and their complete coverage, and evaluates the full independent-set count recurrence. It prints `PASS` with the exact size and optimizer counts. All assertions were run successfully against the package copy of the program. No LP solver or outside data file is needed.

## Relationship to prior work
Polyanskii and Zhang, *Codes for the Z-channel* (first public 2021-05-04), studies arbitrary binary codes against directed asymmetric errors, principally general and asymptotic rate bounds; it does not state this constrained length-seven fractional packing boundary. Rameshwar and Kashyap, *Estimating the Sizes of Binary Error-Correcting Constrained Codes* (first public 2023-01-12), studies run-length-limited constraints but bit-flip and erasure channels and distance-based linear-programming bounds; its constraint family contains the no-adjacent-ones case but its error model and LP differ. Related mathematical research records give a first fractional gap at length six for *deletion* shadows on the same constrained source, which does not imply the directed one-substitution result. Previously established unrestricted single-asymmetric-error code sizes do not imply their optima after restricting codeword inputs. The novelty assessment is relative to the literature and records actually searched, not a claim of exhaustive global priority.

## Limitations
The finite theorem only covers lengths \(1\) through \(7\), not asymptotic code rates or longer-length extrema. The LP dual used here is the elementary incidence-hypergraph shadow packing relaxation, not the stronger constrained Delsarte linear program. The ten optimizers are counted as distinct labeled subsets of the 34 length-seven words; no symmetry-orbit classification is claimed. Independent human/automated validation beyond this package has not been performed. Unindexed historical work on asymmetric constrained codes might contain equivalent short-block data.

## References
- N. Polyanskii and Y. Zhang, *Codes for the Z-channel*, arXiv:2105.01427, first submitted 2021-05-04, https://arxiv.org/abs/2105.01427.
- V. A. Rameshwar and N. Kashyap, *Estimating the Sizes of Binary Error-Correcting Constrained Codes*, arXiv:2301.05098, first submitted 2023-01-12, https://arxiv.org/abs/2301.05098.
