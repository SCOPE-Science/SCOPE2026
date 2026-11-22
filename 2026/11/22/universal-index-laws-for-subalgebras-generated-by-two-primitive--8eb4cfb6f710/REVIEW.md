# Scientific review

## Correctness

**PASS.** Every primitive idempotent is conjugate to \(e_{11}\), and its second factor is exactly a trace-one, determinant-zero matrix. Peirce-corner projections give the *full* generated \(R\)-subalgebra rather than merely its size. The only nontrivial finite-ring count is the two-root lifting argument for \(bc\in\mathfrak m\), valid in every residue characteristic, while the both-unit case is counted directly. The normalization \(q^{2m-1}(q+1)\), exact finite histogram, limit, tail bound, and expected-index formula follow by explicit algebra. Nine independent finite-ring enumerations and selected generated-span checks passed. Limitation: the result does not assert universality for arbitrary non-chain local rings.

## Originality

**PASS, qualified.** Rowen–Segev (2016, arXiv:1609.04899) proves the two-idempotent structural theory and the known full-generation criterion, including the exceptional residue-field size two; neither is claimed as a new structural statement here. The new claim is the complete chain-ring valuation-pair and additive-index distribution, its index-order poset, and the quadratic-versus-tight asymptotic dichotomy. Ito–Terwilliger (2009, arXiv:0906.3839) analyzes universal alternating-idempotent word bases over fields. The closest published field-generation census only treats residue fields and does not imply the arbitrary-length valuation spectrum. The published field-generation record was inspected in full: it supplies an exact all-arity formula over fields but no higher-length chain-ring valuation-index census. A separate scalar-free field-subring record was also inspected in full and is a different counting problem. Unindexed equivalent local-ring enumerations remain a residual possibility.

## Value

**PASS.** A pair of primitive projections is a minimal natural generating system for matrix algebras. Determining not only whether generation succeeds but the entire index spectrum of the generated integral Peirce orders reveals exact local-ring size dependence and contrasts the tight typical logarithmic index with a quadratically diverging mean additive index. The count is uniform across equal and mixed characteristic and gives every attainable fixed-first-idempotent order and its multiplicity. This is a complete invariant, not an arbitrary finite sample or only a restatement of the classical generation threshold.

## Evidence and limits

The mathematical derivation is in `RESULT.md`, and the independent finite-input enumerations are `checker.py` and `checker_output.txt`. Closest inspected archival texts: Rowen–Segev, Sections 1–3 (structure and exceptions); Ito–Terwilliger, Sections 1–2 and selected results in Sections 5, 7, 8 (universal idempotent word algebra). Finite-field generation records and finite-chain-ring background were also searched. Full access to all unindexed/local-ring literature was not possible; independent scientific audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
