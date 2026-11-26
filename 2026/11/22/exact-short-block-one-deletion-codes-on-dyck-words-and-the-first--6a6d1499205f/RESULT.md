# Exact short-block one-deletion codes on Dyck words and the first fractional-packing gap

## Finding

A Dyck word of semilength \(m\) is a binary word with \(m\) ones and \(m\) zeros and at least as many ones as zeros in every prefix. Let \(\mathcal D_m\) be the set of these words. For \(w\in\mathcal D_m\), write \(D_1(w)\) for its set of distinct outputs after deleting exactly one symbol. A one-deletion-correcting code is a subset of \(\mathcal D_m\) whose members have pairwise disjoint deletion shadows. Write \(A_m\) for its maximum size and \(F_m\) for the optimum of the fractional deletion-shadow packing program
\[
\max\sum_{w\in\mathcal D_m} x_w\quad\text{subject to}\quad x_w\ge0,\qquad \sum_{w:y\in D_1(w)}x_w\le1\quad\text{for every output }y.
\]

**Theorem (exact finite spectrum and first strict objective gap).** For \(1\le m\le6\) the exact values are:

| Semilength \(m\) | Dyck words | Distinct possible deletion outputs | Code capacity \(A_m\) | Fractional optimum \(F_m\) |
|---:|---:|---:|---:|---:|
| 1 | 1 | 2 | 1 | 1 |
| 2 | 2 | 4 | 1 | 1 |
| 3 | 5 | 10 | 2 | 2 |
| 4 | 14 | 28 | 4 | 4 |
| 5 | 42 | 84 | 9 | \(29/3\) |
| 6 | 132 | 264 | 24 | \(3269/131\) |

The first strict gap \(F_m>A_m\) is at \(m=5\) (word length ten), and equals \(2/3\). This is a statement about the all-ones objective, not the first semilength with a nonintegral feasible polytope. In fact the feasible polytope is already nonintegral at \(m=4\), where \(F_4=A_4=4\).

## Assumptions and scope

The alphabet is precisely \(\{0,1\}\), with \(1\) an up-step. The receiver sees a length-\(2m-1\) string after exactly one arbitrary deletion, with no location information. This string need not be Dyck. Each output in \(D_1(w)\) occurs once even if several deletions yield it. Codebooks are unrestricted subsets; there is no linearity, symmetry, or checksum constraint. The table asserts no values beyond \(m=6\).

## Proof

Pairwise disjoint shadows are necessary and sufficient for unambiguous decoding, so the code capacity is the optimum of the same program restricted to characteristic vectors. A nonnegative family of output weights \(b_y\) is a dual cover if \(\sum_{y\in D_1(w)}b_y\ge1\) for each \(w\). Every fractional packing obeys
\[
\sum_w x_w\le \sum_w x_w\sum_{y\in D_1(w)}b_y
=\sum_y b_y\sum_{w:y\in D_1(w)}x_w\le\sum_y b_y.
\]

For each of the six semilengths, `certificates.json` lists a codebook, a sparse rational packing and a sparse rational cover, with omitted weights set to zero. `verify.py` generates all sources by recursively extending admissible prefixes, and regenerates all distinct shadows by deleting one position at a time. It checks code membership and disjointness, the domains and signs of the weights, every packing and cover inequality, and equality of the exact rational objectives with the stated entries. `verify_independent.py` reconstructs the same layers independently by choosing the up-step positions of a bit mask and deleting bits by shifts. Each codebook attains the floor of the corresponding matched packing and cover objectives, proving the code-capacity column. In particular the last upper bound is \(A_6\le\lfloor3269/131\rfloor=24\), matched by a 24-word codebook. The first four rows have equal objectives, while \(29/3-9=2/3\).

To see why the objective claim is distinct from polyhedral integrality, at \(m=4\) take \(p=10101100\), \(q=10110100\), \(t=11011000\). Their deletion shadows are respectively
\[
\begin{aligned}
D_1(p)&=\{0101100,1101100,1001100,1011100,1010100,1010110\},\\
D_1(q)&=\{0110100,1110100,1010100,1011100,1011000,1011010\},\\
D_1(t)&=\{1011000,1111000,1101000,1101100\}.
\end{aligned}
\]
Every pair intersects and no output is common to all three. Setting their weights to \(1/2\) and every other weight to zero is therefore feasible. The three pair constraints restrict on this support to \(x_p+x_q=x_p+x_t=x_q+x_t=1\) at that point. Together with the other coordinates set to zero, they have this unique solution, so it is a fractional vertex. Equivalently, the inequality \(x_p+x_q+x_t\le1\) holds on the convex hull of codebooks but fails at this point.

## Verification

In the directory containing the unchanged `certificates.json` and checkers, run `python3 verify.py` and `python3 verify_independent.py` with standard-library Python 3. The two programs print the reconstructed layer sizes and objective values for all six semilengths, followed by `EXACT_DYCK_CERTIFICATES_OK` and `INDEPENDENT_DYCK_OK`. The nonintegrality example can be verified directly from the three displayed shadows; its conclusion is independent of the certificate table.

## Relationship to prior work

Kulkarni and Kiyavash give the general deletion-shadow hypergraph packing and fractional-cover framework and apply it to constrained sources, including run-length-limited codes. Cullina, Kulkarni, and Kiyavash give colorings of unrestricted constant-weight deletion graphs. Neither method by itself supplies the sharp evaluated capacities or fractional objectives for this Dyck subset. A published computation for the unrestricted balanced weight layer concerns a larger source and has a different first strict objective gap. The Dyck-restricted two-read graph instead joins pairs with two distinct shared reads, not pairs with at least one shared read, and does not give these packing optima.

## Limitations

The result concerns the exact optima only through semilength six; it does not classify optimal codebooks, assert an all-length formula, or locate the first fractional vertex. Different formulations of the same finite packing problem or historical exact enumerations may be unindexed.

## References

1. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, [arXiv:1211.3128](https://arxiv.org/abs/1211.3128).
2. D. Cullina, A. A. Kulkarni and N. Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, [arXiv:1211.4056](https://arxiv.org/abs/1211.4056).
3. [*Exact balanced single-deletion code sizes through length twelve and the first fractional-packing gap*](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-exact-balanced-single-deletion-code-sizes-through-length-twelve--c1dc18cb3082/RESULT.md) (2026-11-02).
4. [*Dyck-restricted two-read deletion graph: a vertex-marked bijection and sharp degree*](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-dyck-restricted-two-read-deletion-graph-a-vertex-marked-bijectio--3635f93f657f/RESULT.md) (2026-11-08).
