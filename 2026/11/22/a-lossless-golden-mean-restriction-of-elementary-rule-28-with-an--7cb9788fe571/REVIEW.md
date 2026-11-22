# Self-review

## Correctness

PASS. The full Rule 28 truth table reduces to `010` and `100` on the cyclic/no-`11` source. A forward local test gives \(x_i=y_i(1-y_{i-1})\); the two forbidden output blocks give the exact reverse implication. This proof holds on both bi-infinite and cyclic configurations, including small rings. The attached verifier tested every cyclic source/output through length 15 from an independent truth-table implementation. The Lucas count follows by trace and is not claimed to be novel.

## Originality

PASS subject to historical priority uncertainty. Salo's expanded Rule 28 paper proves a *full-shift* image condition (`111` avoidance) and uses the *flipped* golden mean shift in a periodic section argument. A published published-finding corpus Rule 28 theorem gives unrestricted cyclic fiber multiplicities via matrix products. Its full statement was inspected; neither specifies the source-restricted isomorphism and extra `0100` exclusion. Accessible research claims were checked for overlap. An alternative earlier recoding remains possible; incomplete original-preprint text is not represented as checked.

## Value

PASS. This is an all-length constrained-reconstruction theorem for a standard nonregular cellular automaton on a canonical hard-core source, not a freely chosen finite window. It provides a finite-type image presentation, local lossless decoder and conjugacy. It leaves unrestricted inverse multiplicity and higher-time dynamics unresolved.

Self-review: passed. Independent audit: not yet performed.
