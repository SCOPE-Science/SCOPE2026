# Independent audit — Subalgebra commutativity of the five-dimensional Heisenberg algebra

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/heisenberg-subalgebra-commutativity-h2--2d0e4a1f7f82`  
**Audited tree:** `9a16924381d3c264a7b84a50fcae93a2bc7c43f3`

## Disposition

**FAILED.** Correctness passes, but originality and standalone scientific value fail because an earlier stronger SCOPE record already contains the same theorem.

## Correctness

**PASS.** The mathematics is correct. The classification of subalgebras into central lifts W direct-sum F_q z and graphs over totally isotropic W follows immediately from projection to the symplectic quotient. For two graph subalgebras, z lies in the sum exactly when the two functionals differ on W intersect U; if they agree there, nonpermutability is exactly omega(W,U) nonzero. The finite symplectic incidence counts then give S(q)=q^5+3q^4+5q^3+6q^2+4q+6 and B(q)=q^4(q+1)(q^2+1)(q^3+2q^2+4q+1). Independent exhaustive enumeration reproduced (S,B)=(158,6000) over F_2 and (693,187920) over F_3, agreeing with the displayed formula.

## Originality

**FAIL.** FAIL. A strictly earlier SCOPE record, `2026/09/18/heisenberg-subalgebra-commutativity-degree--e3fb5b5762fa`, was committed before the assigned record and already proves a general exact formula for H_m(q) for every rank m. Its m=2 specialization is exactly the same S(q), B(q), rational commutativity degree, subalgebra classification, and graph-pair nonpermutability criterion. It additionally proves the all-rank large-field phase transition. The assigned record's principal theorem is therefore fully subsumed by prior content in the same repository.

## Scientific value

**FAIL.** FAIL as a standalone validated finding. Although the derivation is correct and readable, its scientific contribution is already contained in a stronger earlier SCOPE theorem. Repackaging the m=2 specialization with an exhaustive checker does not provide enough new scientific value to justify a separate validated record.

## Independent checks

- Re-derived the graph-subalgebra permutability criterion from the central coordinate.
- Checked the finite symplectic line/Lagrangian incidence counts used for H_2.
- Independently exhaustively enumerated all Lie subalgebras for q=2 and q=3 and matched the stated bad-pair counts.
- Fetched the earlier 2026/09/18 all-ranks SCOPE record and verified that its m=2 specialization is term-for-term identical to the assigned theorem.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.19086 — Muhie--Otera--Russo source introducing the invariant and treating the rank-one Heisenberg case.
- https://arxiv.org/abs/1312.0296 — Finite-group subgroup-commutativity context cited by the assigned record.
- https://github.com/SCOPE-Science/SCOPE2026/tree/main/2026/09/18/heisenberg-subalgebra-commutativity-degree--e3fb5b5762fa — Earlier stronger SCOPE theorem giving exact H_m(q) formula for all m and the identical H_2 specialization.

## Limitations

- The failure is about originality and standalone scientific value, not mathematical correctness.
- No claim is made that the underlying H_2 formula itself is false.
- The earlier all-ranks SCOPE record should remain the validated locus for this result.

## Repository identity

The assigned source-tree SHA `9a16924381d3c264a7b84a50fcae93a2bc7c43f3` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
