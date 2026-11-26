---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The square-zero vectors have zero e_2 coordinate and x_1=±x_3; the other lines must contain idempotents in S, and the idempotent equations give exactly the stated z_lambda when lambda differs from 2. For an independent plane check, in the basis (u,w,e_2) the products are u²=w²=0, uw=-2u, e_2u=e_2w=0 and e_2²=(lambda/2-2)u+lambda e_2-(lambda/2)w. A plane not containing u has basis w+b u, e_2+a u. Its closure forces b=a=0 by squaring the first vector and multiplying the two, then requires lambda=4. Planes containing u correspond to lines closed under multiplication in the two-dimensional quotient by Ku, which has just the two directions w and e_2-w/2; their preimages are W and S. The intersections are the stated ones, and Ku is an ideal, so both Frattini formulas follow. S²=S explains non-solvability. The reasoning allows characteristic 3 and all other allowed fields. The frozen finite-field checker was inspected but not executed.

## originality

FAIL

A distinct indexed record, 2828ce45dd11, gives the very same complete ordinary-subalgebra lattice, including the Boolean case, over the same fields. It is indexed with a later date; this is a finding of present equivalent coverage, not a finding of earlier priority or dependence. The Frattini and dual-atomistic assertions not stated there are immediate from that exact lattice and, for the ideal, the one-line check that Ku is an ideal. The idempotent threshold and non-solvability are already in Hu–Wen. No distinct substantive remainder is established.

## value

FAIL

A complete ordinary-subalgebra classification for a non-solvable evolution family is inherently useful, but that classification already exists in the matching record. The remaining invariant calculation is a direct meet of the already listed coatoms, followed by an elementary ideal check, and the two threshold values are already determined by the matched results. The remaining difference does not warrant a separate finding or a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
