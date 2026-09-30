# Independent Audit — 2026-09-28

**Record:** `2026/09/10/041`  
**Title:** Claimed multiplicity-2 non-faithful tropical bitangent pair  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `f484f14804ade448d37c7011129beb210f2d9f14`  
**Disposition:** **FAILED**

## Independent checks

- Recomputed all weights at W and the elimination x=−y independently.
- Performed an exact symbolic tangency test over Q(t) from the record's full Q0 and B0, rather than inferring tangency from tropical shape labels.
- Compared the claimed faithfulness implication with the actual scope of the BPR/GRW multiplicity-one results.

## Three-axis assessment

- **Correctness — FAIL**: The local initial-ideal arithmetic is compatible with two torus points, but the record's algebraic line B0 is not a bitangent of Q0. Independently substituting y=−t^14 x−t^7 into the stated Q0, clearing Laurent denominators by t^36, and computing gcd_x(P,∂P/∂x) over Q(t) gives gcd=1. In characteristic zero the four intersections are therefore simple, so B0 has no algebraic tangency, let alone two. Moreover the saturated initial ideal (x+y,y²−1) consists of two reduced multiplicity-one torus points; its total tropical intersection multiplicity 2 is not by itself the tropical-multiplicity-one condition used by GRW/BPR for a section of a variety's tropicalization map. The claimed 'non-faithful bitangent pair' inference is unsupported.
- **Originality — UNRESOLVED**: The displayed initial-ideal calculation may be a new computation for these chosen coefficients, but it does not establish the advertised bitangent/nonfaithfulness phenomenon. Priority for that weaker transversal-intersection datum was not established.
- **Scientific Value — FAIL**: Because the exact line is not a bitangent and the faithfulness criterion is misapplied, the record does not deliver the promised obstruction. The surviving determinant/initial-ideal calculation describes an ordinary pair of intersections and does not carry the claimed geometric significance.

## Sources compared

- Repository record 041 RESULT.md: https://github.com/SCOPE-Science/SCOPE2026/blob/main/2026/09/10/041/RESULT.md — Defines Q0, B0, W and infers nonfaithfulness from the multiplicity-2 joint initial ideal.
- Len–Markwig, Lifting tropical bitangents: https://arxiv.org/abs/1708.04480 — Treats actual lifts of tropical bitangents by solving for initial terms of bitangent-line coefficients; a tropical shape/valuation pattern alone is not a proof that a chosen algebraic line is bitangent.
- Cueto–Markwig, Combinatorics and real lifts of bitangents to tropical quartic curves: https://arxiv.org/abs/2004.10891 — Classifies tropical bitangent classes and lift conditions; it does not make every line with the relevant coefficient valuations an algebraic bitangent.
- Gubler–Rabinoff–Werner, Skeletons and tropicalizations: https://arxiv.org/abs/1404.7044 — The multiplicity-one theorem concerns existence/uniqueness of a continuous section on the locus of tropical multiplicity one for a variety's tropicalization map, not a blanket criterion on total joint intersection multiplicity.

## Limitations

- The exact gcd calculation uses the record's coefficients exactly as written over Q(t); because the field has characteristic zero, absence of repeated roots persists after algebraic extension.
- The audit does not dispute the elementary determinant-2 stable-intersection computation; it rejects the bitangent and faithfulness conclusions drawn from it.

This audit is independent of the repository's pre-existing `AUDIT.json`. GitHub was read only as evidence; no repository changes were made by this audit run.
