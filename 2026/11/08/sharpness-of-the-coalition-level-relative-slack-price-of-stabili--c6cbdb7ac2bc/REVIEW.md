# Mathematical review

## Correctness — PASS

The general statement follows by applying \(0\le r(S)\le\delta W(S)\) first to pairs to force \(v_{ij}\ge0\), and then to arbitrary partitions to compare the sum of within-coalition pair values with the grand coalition's pair total. The grand coalition admits no profitable move to the empty coalition. For the three-participant family the only positive slack is \(r(\{1,2\})=\delta\), exactly its allowed cap. All five partitions are compared; every nongrand one contains a singleton with a strictly profitable join to another coalition. A full exact-rational checker reproduced \(2245\) parameter instances. Finite tests are supplementary; all-parameter and all-size results rest on the symbolic inequalities.

## Originality — PASS, with residual risk

Hasan's publicly accessible July 2026 paper, Corollary 5.12, proves the same universal upper bound but explicitly leaves open whether the **coalition-level** assumption permits a better bound. Proposition 5.13 proves sharpness only for the weaker partition-level condition and uses a positive singleton slack that fails the stronger condition. The new construction transfers slack to a two-person coalition and meets the stronger condition with equality. Searches of contemporaneous research records, primary text, and associated literature did not recover the same sharpness result. An unindexed independent resolution or a later uninspected revision remains possible. The 2021 Donahue–Kleinberg welfare/stability study employs different cost functions and has no comparable coalition-wise retained-surplus hypothesis.

## Mathematical value — PASS

The resolved sharpness question is explicit in the motivating paper and determines whether a practically interpretable, stronger affordability hypothesis improves its worst-case stability-efficiency guarantee. The structural deduction that **all** pairwise transfers must be nonnegative under that hypothesis and the three-participant minimal witness explain why the original weaker construction can be repaired without weakening the assumed bound. This is a worst-case result, not an assertion about particular estimated training benefits.

## Limits

Arbitrary primitive coalition surplus functions are permitted, exactly as in the motivating model. The construction may fail under additional monotonicity or shape constraints, and does not estimate a physical learning task. The sharp value is a supremum, not a positively parameterized equality claim. Public-source chronology uses the July 21, 2026 posted preprint rather than the later July 29 arXiv upload.

Self-review: passed. Independent audit: not yet performed.
