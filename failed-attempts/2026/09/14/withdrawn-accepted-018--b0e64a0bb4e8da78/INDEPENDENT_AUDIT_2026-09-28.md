# Independent Audit — 2026/09/14/018

Audit date: 2026-09-28 (UTC)
Audited tree: `bf6033a8d389b8494f34a71b38e790181834c904`

## Disposition

**FAILED** — Rejected on originality and value: the exact 2-patch calculation is correct, but Gao–Dong already prove the relevant general decreasing-diffusion phenomenon for patch models with exactly one mobile infected compartment class.

## Correctness

**PASS**. The exact counterexample checks. With D=diag(4,2) and A(1)=[[3,-1],[-1,3]], one gets H(1)=[[3/2,1/2],[1/4,3/4]], trace 9/4, determinant 1, and discriminant 17/16, so its Perron root is (9+sqrt(17))/8<7/4<2=R0(0). The DFE and heterogeneous isolated risks (2,1) are also correct. Thus the submitted “strictly increasing” claim is indeed false.

## Originality

**FAIL**. Gao and Dong’s 2020 theorem already establishes that increasing diffusion of the single mobile infected compartment class makes R0 strictly decrease when patch risks are heterogeneous, and states that the approach applies to epidemic patch models with exactly one migrating infected-compartment class and one transmission route. The submitted exposed-mobile/infective-immobile SEIR example is therefore a concrete 2x2 instance of an already published general monotonicity direction, not a new phenomenon.

## Scientific value

**FAIL**. As an exact sanity-check against a wrongly oriented monotonicity target the example is clear and useful. But once the published general theorem is accounted for, a single rational 2-patch instantiation does not add a new theorem, mechanism, boundary case, or quantitatively significant refinement.

## Evidence and limitations

Repository files were read from the exact assigned/current tree; GitHub was used only as evidence and was not modified. Lawful open-access/preprint sources were checked first:
- https://arxiv.org/abs/1907.12229 — Gao–Dong, Fast Diffusion Inhibits Disease Outbreaks: strict decrease/convexity of R0 under heterogeneous patch risks, with applicability to models having exactly one migrating infected compartment class and one transmission route.
- https://doi.org/10.1090/proc/14868 — Published Proceedings of the AMS version of the same theorem.

Independent checks:
- Independent Fraction arithmetic reproduced H(1), trace 9/4, determinant 1, discriminant 17/16, and R0(1)<R0(0).

No inaccessible material is represented as read. Literature absence was not treated as proof of novelty; where exact prior coverage remained uncertain, the originality axis is explicitly marked unresolved.
