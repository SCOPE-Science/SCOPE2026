# Scientific review

## Correctness — PASS

The full statement concerns every length \(n\ge0\) and positional scattered embeddings, not contiguous patterns or distinct resulting strings. Each letter \(2\) adds exactly the number of prior \(01\) pairs, which makes the positive-contribution partitions \((2)\) and \((1,1)\) exhaustive and disjoint. The unique earliest productive \(1\) forces exactly three regular-language decompositions; their slot-insertion generating functions prove the rational formula without extrapolating from finite data. Partial fractions establish the exact coefficient and asymptotic. Direct enumeration of all ternary words through length eleven and an independent bounded-counter transfer through length fifty reproduce the formula. Risk: the analysis is not formally machine-certified; the human-readable decomposition and each counting step remain open to independent scrutiny.

## Originality — PASS under current evidence, with residual risk

The closest current research source, Bruda (2026), proves a binary fixed-frequency eventual degree theorem and states a broader m-ary form, but no all-length ternary frequency-two enumeration for a pattern using all three symbols. Menon–Singh (2023/2024) studies binary hosts; Mansour–Shabani (2016) explicitly restricts to three-letter patterns with at most two distinct symbols. Similar-looking exact formulas for adjacent trigrams and for universal words concern different statistics or restricted input families. A broad existing algorithm that could theoretically compute the same generating function does not itself state this exact result. Risk: unpublished or unindexed equivalent special-case counts have not been ruled out conclusively; the 2023 binary paper was confirmed by accessible abstract and context rather than directly reviewed in full.

## Value — PASS

The first nontrivial positive-frequency case beyond one positional occurrence is an informative, precisely motivated boundary for alphabet-generalized scattered-subsequence enumeration. The answer resolves *every length*, rather than only its growth type, and the three families expose the combinatorial sources of the squared exponential pole and its coefficient. The formula supplies a concrete benchmark for broader counting methods and an exact rare-event probability. Risk: a general future published formula may subsume the special case; no wider arbitrary-frequency theorem is asserted.

Self-review: passed. Independent audit: not yet performed.
