# Independent audit — 2026-09-30

**Record:** `SCOPE-20260910-020`

## Correctness — PASS

Independent symbolic differentiation on the six basis monomials of H_{2,0} plus H_{0,2} reproduced zero for the numerator of the Rossi Paneitz operator. The committed artifacts also verify the cancellation by several routes, including direct vector fields, Takeuchi-normalized formulas, a full degree-2 basis sweep, and an alternate normalization. The theorem and the refutation of the proposed negative degree-2 witness are mathematically correct under the stated fixed-contact-form convention.

## Originality — FAIL

Takeuchi's published full text already gives the exact Rossi Kohn-Laplacian and torsion formulas in equations (5.15)–(5.22), the spherical-harmonic eigenvalues in (5.25), and the bidegree-shift rule in (5.26). Applying those published identities to degree 2 is a short direct specialization whose cancellation yields the claimed kernel. Under the audit bar that counts corollaries and mechanically implied special cases as covered even when not stated verbatim, the final theorem is covered by prior work.

### Structured originality checks

- **equivalent_formulations:** Checked both the operator-numerator form and the spherical-harmonic formulation; they are the same computation after multiplying by the nonzero factor (1-t^2)^2.
- **broader_coverage:** Takeuchi supplies a strictly broader exact formula for the Rossi Paneitz operator on all spherical-harmonic degrees and then analyzes the odd-degree invariant subspaces.
- **exact_database_or_table:** No separate degree-2 table was found, but that absence does not create originality because the general published operator identities determine the degree-2 result directly.
- **claim_vs_prior_implication:** Decisive: equations (5.15), (5.16), (5.25), and (5.26) in the primary source imply the degree-2 kernel after a short basis calculation. The claim is therefore a covered corollary under the stated standard.

## Scientific value — PASS

The calculation is a useful clarification because it rules out a natural even-degree negativity witness and cleanly contrasts with the known odd-degree negative directions. It has diagnostic value for choosing trial functions, even though that does not overcome the originality failure.

## Source inspections

- **Takeuchi, CR Paneitz operator on non-embeddable CR manifolds** — Full HTML, including Section 5.1 formulas (5.15)–(5.22), Section 5.2 spherical harmonics, and the odd-degree analysis. The source provides the general operator identities that directly imply the degree-2 kernel by specialization. https://arxiv.org/html/2407.16185v2
- **Published-findings semantic search** — Exact-match and related Rossi/Panietz findings. No distinct explicit degree-2 record appeared, but the primary-source implication is already decisive. https://github.com/Resultary/2026/tree/main/2026/9/10/SCOPE020

## Residual risks

- The conclusion is a scientific originality rejection, not a transport or access failure.
- The result could remain pedagogically useful, but the audit standard does not count a mechanically implied specialization as original.

## Disposition

**FAILED**. The calculation is correct and scientifically useful, but the novelty claim fails because the final theorem is a direct corollary of prior published formulas.
