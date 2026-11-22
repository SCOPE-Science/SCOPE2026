# Exact short-block one-deletion codes on Dyck words and the first fractional-packing gap

## Finding
A Dyck word of semilength \(m\) is a binary word with exactly \(m\) ones and \(m\) zeros and at least as many ones as zeros in every prefix. Let \(\mathcal D_m\) be the labeled, indexed set of these words, and let \(D_1(w)\) be the set of distinct words obtained by deleting exactly one symbol from \(w\). A code \(C\subseteq\mathcal D_m\) corrects one deletion if \(D_1(u)\cap D_1(v)=\varnothing\) whenever \(u\ne v\) in \(C\). Define \(A_m\) as its maximum cardinality.

**Theorem (exact finite spectrum and first gap).** For every integer \(1\le m\le6\),
\[
(A_1,A_2,A_3,A_4,A_5,A_6)=(1,1,2,4,9,24).
\]
For the natural fractional deletion-shadow packing program, namely maximizing \(\sum_{w\in\mathcal D_m}x_w\) subject to \(x_w\ge0\) and \(\sum_{w:y\in D_1(w)}x_w\le1\) for every possible output \(y\), the exact optima are
\[
(F_1,F_2,F_3,F_4,F_5,F_6)=\left(1,1,2,4,\frac{29}{3},\frac{3269}{131}\right).
\]
Thus \(m=5\) (word length ten) is the **first** semilength at which this relaxation is not integral, with exact gap \(F_5-A_5=2/3\). At length twelve, the sharp capacity is \(24\) out of \(132\) Dyck words, while the fractional relaxation has value \(3269/131\).

| Semilength \(m\) | Dyck words | Distinct possible deletion outputs | Exact code capacity \(A_m\) | Exact fractional optimum \(F_m\) |
|---:|---:|---:|---:|---:|
| 1 | 1 | 2 | 1 | 1 |
| 2 | 2 | 4 | 1 | 1 |
| 3 | 5 | 10 | 2 | 2 |
| 4 | 14 | 28 | 4 | 4 |
| 5 | 42 | 84 | 9 | \(29/3\) |
| 6 | 132 | 264 | 24 | \(3269/131\) |

## Assumptions and scope
The alphabet is precisely \(\{0,1\}\), with \(1\) interpreted as an up-step. The decoder receives a length-\(2m-1\) string with **exactly one arbitrary deleted symbol**, with no indication of its position; the received word need not be Dyck. Duplicate outputs created by deleting different positions of the same source are counted **once**, not with multiplicity. Codebooks need not be linear, symmetric, or checksum-defined. All endpoints, labels, and fixed finite ranges are part of the claim; no formula beyond \(m=6\) is asserted.

## Proof
**1. Exact packing duality.** Associate to each input \(w\in\mathcal D_m\) its finite output set \(D_1(w)\). Pairwise disjoint output sets are necessary and sufficient for zero-error one-deletion correction. Therefore any code characteristic vector is feasible for the linear relaxation above. Its dual assigns nonnegative rational weights \(b_y\) to outputs such that \(\sum_{y\in D_1(w)}b_y\ge1\) for every source \(w\); the objective minimizes \(\sum_yb_y\). Weak duality follows directly by interchanging finite sums:
\[
\sum_wx_w\le\sum_w x_w\sum_{y\in D_1(w)}b_y
=\sum_y b_y\sum_{w:y\in D_1(w)}x_w\le\sum_yb_y.
\]
In particular, the integral capacity satisfies \(A_m\le\lfloor\sum_yb_y\rfloor\).

**2. Explicit witnesses and rational certificates.** The complete `certificates.json` includes, for each \(m=1,\ldots,6\), a list of \(A_m\) actual Dyck codewords with disjoint one-deletion shadows, a sparse nonnegative rational primal vector \(x\), and a sparse nonnegative rational dual vector \(b\). Omitted entries are zero. The two *independent* packaged exact-arithmetic programs regenerate **every** Dyck source and **every** distinct deletion output, and check **each** primal inequality, **each** dual inequality, disjointness of the witness codeword shadows, and the exact objective values. These are finite certificates, not solver logs or numerical tolerances.

The rational primal and dual objectives agree at each \(m\). The values are exactly \(1,1,2,4,29/3,3269/131\). Consequently the LP optimum is precisely the displayed common rational value by weak duality. Every listed code has cardinality equal to the floor of that rational value, so the integral capacities are exactly the displayed integers. In particular, the last upper bound follows from \(3269/131<25\) and a 24-codeword witness; the first fractional separation follows from \(29/3>9\), while all smaller \(m\) have matched integral and fractional objectives.

**3. Finite completeness.** All semilengths \(1\le m\le6\) and all source/output possibilities at each semilength are generated from the defining prefix-balance condition, not sampled. A second generator uses combinations of the \(m\) up-step positions in an integer bit mask, then applies a separate bit-deletion formula. The two independent representations agree on all six certificate layers, hence the claimed *finite* classification has no unsampled parameter or hidden extrapolation. The proof does not infer anything from a timeout or claim an all-length result.

## Verification
In the same directory as `certificates.json`, execute `python3 verify.py` and `python3 verify_independent.py` using Python 3 and only its standard library. Both output their verified source counts, output counts, integral witness sizes, and exact rational LP objectives for all six parameters and finish with `EXACT_DYCK_CERTIFICATES_OK` and `INDEPENDENT_DYCK_OK`, respectively. No external optimizer is needed for replay. The certificate data includes every input needed for verification and uses canonical binary strings as keys.

## Relationship to prior work
Kulkarni and Kiyavash (2012) developed deletion-shadow hypergraph packing and dual upper bounds for constrained sources, with a run-length-limited application, rather than this Dyck-language optimum and fractional spectrum. Cullina, Kulkarni and Kiyavash (2012) determined optimal colorings of general constant-weight deletion graphs; an optimal coloring does not imply the independence number of the induced Dyck subgraph. In a related result entitled *Exact balanced single-deletion code sizes through length twelve and the first fractional-packing gap*, the unrestricted balanced weight-\(m\) layer has integral optimum equal to the Catalan number through semilength six, and its LP first becomes fractional at semilength four. The present Dyck restriction is a **proper and qualitatively different source universe**: its code capacities are much smaller and its first LP gap occurs at semilength five, not four.

A separate result, *Dyck-restricted two-read deletion graph: a vertex-marked bijection and sharp degree*, joins two Dyck words only when they share **two** distinct one-deletion outputs; it explicitly does not determine single-deletion code capacities. Here two source words are incompatible if they share **at least one** output. Its graph independence numbers and output hypergraph are consequently different. The published general frameworks do not determine the exact values in this theorem. A differently indexed or unpublished historical computation may still exist.

## Limitations
The capacity and exact LP profile cover only semilengths one through six; no assertion of asymptotic behavior, optimal-codebook counts, or a Catalan-type formula for larger semilengths is made. The certificates are fully finite exact-arithmetic mathematical evidence, but they have not undergone independent expert audit. Historical-priority coverage, particularly unpublished Dyck coding enumerations or alternative descriptions of the same hypergraph, is not exhaustive.

## References
1. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128 (first public posting 2012-11-13), https://arxiv.org/abs/1211.3128.
2. D. Cullina, A. A. Kulkarni and N. Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, arXiv:1211.4056 (first public posting 2012-11-16), https://arxiv.org/abs/1211.4056.
3. *Exact balanced single-deletion code sizes through length twelve and the first fractional-packing gap*, published 2026-11-02; https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-balanced-single-deletion-code-sizes-through-length-twelve--c1dc18cb3082/RESULT.md.
4. *Dyck-restricted two-read deletion graph: a vertex-marked bijection and sharp degree*, published 2026-11-08; https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-dyck-restricted-two-read-deletion-graph-a-vertex-marked-bijectio--3635f93f657f/RESULT.md.
