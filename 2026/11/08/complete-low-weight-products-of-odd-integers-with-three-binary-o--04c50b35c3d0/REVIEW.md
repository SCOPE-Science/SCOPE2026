# Scientific assessment

## Correctness — PASS
For positive odd factors of binary weight three, the published Kaneko–Stoll global bounds specialize to \(ab<2^{14}\) at product weight two and \(ab<2^{23}\) at product weight three [1, Theorems 2.1–2.2]. Binary exponent parametrizations make each remaining product range finite: exactly \(13\) candidate weight-two products and \(231\) candidate weight-three products. The exact product-first divisor census checks all possible smaller factors and returns one plus six pairs. The independent factor-first search checks \(3672\) admissible pairs and returns the same list. Both computations have been executed and their outputs match the included logs. The proof explicitly rules out product weight one. The bound for the infinite domain rests on the published theorem, not the finite check alone.

## Originality — PASS within inspected evidence
The main paper [1] states effective bounds, not the seven-case complete classification of two equal-weight-three factors. The independently read square case [2] covers the diagonal pair \(\{7,7\}\) only as a member of a wider square theorem. Public result [3] gives the distinct weight-\(2\)-by-weight-\(3\) case (three-bit product pairs \(\{3,7\},\{5,7\}\)); neither its statement nor its implication covers the equal-weight-three classification. Targeted searches of exact triples, aliases, and OEIS/product tables did not identify a fully covering statement. Residual risk: an unindexed equivalent enumeration, or a comprehensive table not found, could exist. Search failures are not proofs of novelty.

## Mathematical value — PASS
Kaneko–Stoll explicitly pose which small triples of factor/product binary weights are solvable, and their general bounds leave exact low-weight solution sets open. The first genuinely symmetric weight-three-by-weight-three case has a complete, sharp answer at the two smallest achievable nontrivial product weights, with just seven unordered pairs and largest product \(1029\). It is a natural finite classification of multiplicative cancellation under binary carries, rather than an arbitrary numerical slice. This modest, self-contained exact result provides a checkable benchmark; it does not claim a new broad theorem or any stronger bound in general weights.

## Closest literature and limits
[1] H. Kaneko and T. Stoll, *Products of integers with few nonzero digits*, arXiv:2112.03077v1 (2021-12-06), Theorems 2.1–2.2, full manuscript read in relevant sections.

[2] K. Aloui et al., *On the binary digits of n and n squared*, arXiv:2203.05451v1 (2022-03-10), relevant full-text sections read.

[3] *Exact (3,2,3) binary-weight product classification*, public record: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-3-2-3-binary-weight-product-classification--28456ef398f9, RESULT.md read.

Remaining risks are publication overlap and dependence on the published nontrivial carry bound. Independent scientific verification has not taken place.

Self-review: passed. Independent audit: not yet performed.
