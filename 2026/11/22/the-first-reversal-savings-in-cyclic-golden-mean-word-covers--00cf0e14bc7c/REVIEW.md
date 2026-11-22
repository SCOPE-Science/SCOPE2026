# Mathematical review

## Correctness — PASS

The complete finite proof reduces circular no-`11` covering to a closed walk in the exact overlap digraph. Every reversal class is represented by one mask bit; exhaustive BFS from every starting vertex determines minimum length for each of the five orders. An independent brute-force program examines every circular bitstring of each shorter length and checks all cyclic windows directly, then validates explicit optimal examples. Both programs passed; no inference to larger orders is attempted.

## Originality — PASS (qualified)

The closest full-text primary paper, Burris–Motta–Shipman (2016), studies unrestricted-alphabet unoriented de Bruijn graphs, not the golden-mean shift. Previously indexed all-order golden-mean covers are oriented, while unrestricted reversal-cover results concern full binary alphabets. No indexed statement of the exact reversed, run-constrained n=6 bound and first-saving threshold was identified. A previously unindexed finite optimization or a worked special case of the general Eulerization framework might cover this result; that residual risk is recorded.

## Value — PASS

The order-six case is the first strict reduction caused by treating reflected words as equivalent in a constrained synchronization-source universal cycle. The reduction from 28 to 23 symbols is substantial and motivates a subsequent all-order study, but no all-order statement is implied here.

## Sources and limitations

- https://arxiv.org/abs/1608.08480
- https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-fibonacci-length-for-cyclic-covers-avoiding-adjacent-ones--115d2faf86fa
- https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-shortest-cyclic-binary-reversal-covers-through-order-five--d2dd86a41c28

Only orders two through six are proved. Independent audit was not conducted.

Self-review: passed. Independent audit: not yet performed.
