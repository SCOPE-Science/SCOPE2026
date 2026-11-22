# Scientific review

## Correctness

**PASS.** The deletion channel and constrained source are explicitly defined, with no constraint imposed on received strings. Exhaustive maximum-clique branch-and-bound on the exact compatibility graph establishes the integer optima \((1,3,4,8,12,22)\) for lengths \(2\) through \(7\), and length \(1\) follows directly. The complete search uses valid greedy coloring upper bounds, not a time-limited answer; the length-seven traversal visits \(1,526,900\) recursion nodes. Independently formulated mixed-integer linear optimization confirms the integer values. Rational primal/dual weights, checked against every incidence entry in exact arithmetic, establish the fractional optima. Both construction and all output signatures are checked separately. Risk: finite algorithm correctness must be reproduced from the included code; no mathematical proof is claimed beyond the stated lengths.

## Originality

**PASS, qualified.** Comparison was based on implications under the **same source language and channel**, not matching terminology. Kulkarni and Kiyavash's constrained-source result is a general fractional bound and a binary zero-run example, not an evaluated ternary maximum-run-one integer table. Nguyen et al. give quaternary DNA constructions with different objectives rather than these exact finite capacities. Benerjee and Banerjee study Hamming-distance homopolymer-free codes, where the receiver neither deletes nor loses symbol indices. Related two-read deletion reconstruction and known-position erasure results are weaker observational models and do not establish the one-read single-deletion optimum. Research-record queries returned no equivalent finite classification. Risk: mathematical-index coverage and historical unpublished enumerations are incomplete; absence of indexed hits is not uniqueness proof.

## Mathematical value

**PASS.** Four information bits require at least \(16\) distinct codewords. The exact values \(M_6=12\) and \(M_7=22\) prove the minimum feasible short-block length of seven under two naturally coupled channel and sequence restrictions. The nontrivial integrality gap \(P_7-M_7=11/4\) also quantifies the limitation of the usual fractional shadow-packing method and identifies a reproducible finite benchmark for constrained synchronization coding. This is a natural finite design cutoff, not an arbitrary parameter perturbation. Risk: its direct application is limited to the ternary maximum-run-one model, not DNA's usual four-letter alphabet.

## Scope and closely related literature

The closest framework is the constrained-source deletion hypergraph in Kulkarni and Kiyavash, 2012, https://arxiv.org/abs/1211.3128 . Later related coding constructions are Nguyen et al., 2020, https://arxiv.org/abs/2001.02839 , and homopolymer-free Hamming theory is Benerjee and Banerjee, 2023, https://arxiv.org/abs/2305.10741 . These objects and claim implications are distinguished in RESULT.md. The proof depends on finite exhaustive computation with complete reproducible code, with no all-length extrapolation.

Self-review: passed. Independent audit: not yet performed.
