# Exact initial profile of binary two-list three-deletion codes

## Finding

Let \(D_{2,3}(n)\) denote the largest cardinality of a set \(C\subseteq\{0,1\}^n\) for which **every** binary word \(y\) of length \(n-3\) is a subsequence of **at most two distinct** members of \(C\). Then, for every integer \(3\le n\le10\),

\[
\bigl(D_{2,3}(3),D_{2,3}(4),\ldots,D_{2,3}(10)\bigr)
=(2,3,4,4,4,7,10,14).
\]

In particular, length eight is the first blocklength admitting more than four codewords under exactly three deletions and list-size two. All eight values are established by matching explicit codes and exact rational upper-bound certificates; they are not inferred from a numerical solver's optimality report.

## Assumptions and scope

The alphabet is the labeled binary alphabet \(\{0,1\}\). Exactly three positions are deleted from an input word of length \(n\); the output is the remaining order-preserving subsequence of length \(n-3\). Multiple deletion patterns yielding the same output count as one possible output. The decoder is allowed a list of at most two *distinct* original codewords for each output. The theorem covers every integer \(3\le n\le 10\), and no larger length is claimed.

## Proof

For each fixed \(n\), let \(\mathcal X_n=\{0,1\}^n\) and \(\mathcal Y_n=\{0,1\}^{n-3}\). Define the incidence matrix
\[
A_{y,x}=\begin{cases}1&\text{if }y\text{ is an order-preserving subsequence of }x,\\0&\text{otherwise.}\end{cases}
\]
The two-list condition is exactly \(\sum_{x\in C} A_{y,x}\le2\) for every \(y\in\mathcal Y_n\).

The attached `CERTIFICATE.json` lists a witness code \(C_n\) for every \(n\), as well as nonnegative rational weights \(w_y\) on \(\mathcal Y_n\). The entry `dual_denominator` is the common positive denominator for the integer numerators in `dual_weights`; all omitted outputs have weight zero. For each \(x\in\mathcal X_n\), define the **derived**, nonnegative supplementary weight
\[
s_x=\max\left\{0,1-\sum_{y\in\mathcal Y_n}A_{y,x}w_y\right\}.
\]
This definition guarantees \(1\le\sum_y A_{y,x}w_y+s_x\) for every \(x\). Consequently every feasible code satisfies
\[
\begin{aligned}
|C|&\le\sum_{x\in C}\biggl(\sum_yA_{y,x}w_y+s_x\biggr)\\
&\le2\sum_{y\in\mathcal Y_n}w_y+\sum_{x\in\mathcal X_n}s_x=:U_n.
\end{aligned}
\]
All terms are nonnegative; the second inequality uses the exact two-list constraints. Hence \(|C|\le\lfloor U_n\rfloor\).

Direct exact-rational evaluation of the furnished weights and all \(2^n\) words produces the following table:

| \(n\) | Explicit witness size | Exact dual upper bound \(U_n\) | Integer upper bound |
|---:|---:|---:|---:|
| 3 | 2 | \(2\) | 2 |
| 4 | 3 | \(3\) | 3 |
| 5 | 4 | \(4\) | 4 |
| 6 | 4 | \(4\) | 4 |
| 7 | 4 | \(4\) | 4 |
| 8 | 7 | \(22/3\) | 7 |
| 9 | 10 | \(659/60\) | 10 |
| 10 | 14 | \(2693/180\) | 14 |

Every listed witness satisfies \(\sum_{x\in C_n}A_{y,x}\le2\) for every output \(y\), as independently checked by `check.py`, so \(D_{2,3}(n)\ge|C_n|\). The rational upper bounds satisfy \(\lfloor U_n\rfloor=|C_n|\), proving the claimed equalities for all eight lengths. This is a finite proof by completely specified certificates, with no reliance on floating-point optimization, partial enumeration, or assumptions beyond the definition.

## Verification

Run `python3 check.py` in the directory containing `CERTIFICATE.json` and `check.py`; no nonstandard Python libraries are needed. The checker reconstructs every source word and every received word, computes subsequence membership by a left-to-right greedy scan, verifies each listed code and both nonnegativity and coverage of the rational weights, independently reconstructs the supplementary weights, and checks that the exact rational dual objective lies between the witness size and the next integer. It also checks the explicitly printed objective for each length. The entire finite domain is covered for every \(n\in\{3,\ldots,10\}\).

## Relationship to prior work

Andrew D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650 (initial release September 22, 2026), defines the same \(t\)-list \(k\)-deletion condition and proves asymptotic existence bounds for general parameters; the complete eight-page preprint was inspected, including its definitions, theorems, proofs, and references. It does not give these exact finite three-deletion optima or their witnesses and rational upper certificates. Guruswami and Håstad, *Explicit Two-Deletion Codes with Redundancy Matching the Existential Bound*, arXiv:2007.10592 (2020), discuss asymptotic two-deletion list decoding, a different deletion count. Related finite exact two-list/two-deletion and three-deletion reconstruction results concern different predicates: a two-deletion list code and a multiple-read pairwise ambiguity problem respectively.

The new contribution is **only** the exact finite-length profile for the stated three-deletion, two-list model and its verifiable certificates, not the definition or the general asymptotic theory of list-decodable deletion codes.

## Limitations

The proof stops at \(n=10\). It does not give an all-length recurrence, asymptotic rate improvement, a classification of all optimal codes, a polynomial-time encoder, or independent expert validation. Historical priority beyond the accessible inspected primary literature and indexed research records remains open; no absence-of-search-hits assertion is used as a proof of novelty. The particular upper-bound weights were initially found computationally, but their verification and the proof depend only on the exact rational data printed in the package.

## References

1. Andrew D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650, first released September 22, 2026, https://arxiv.org/abs/2609.26650.
2. Venkatesan Guruswami and Johan Håstad, *Explicit Two-Deletion Codes with Redundancy Matching the Existential Bound*, arXiv:2007.10592, first released July 21, 2020, https://arxiv.org/abs/2007.10592.
3. Noga Alon, Gabriela Bourla, Ben Graham, Xiaoyu He and Noah Kravitz, *Logarithmically larger deletion codes of all distances*, IEEE Transactions on Information Theory 70 (2024), 125–130, https://arxiv.org/abs/2209.11882.
