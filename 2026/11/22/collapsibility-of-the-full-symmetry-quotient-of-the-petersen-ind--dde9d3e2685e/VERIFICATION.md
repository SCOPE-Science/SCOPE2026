---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Pass the corrected RESULT.md in /workspace/repairs/5/. The original's terminal ID 2570 is wrong: dimension-first order makes IDs 0–22 the vertices, and 2570 has dimension 3. Under precisely that indexing the certificate actually leaves ID 21. This is a concrete numerical error in the text, not a failure of the collapse or a change in its indexing. Independent reconstruction and replay (independent_check.py and independent_full.json under /workspace/branches/8a8943a8-06a7-4341-8601-d50d42480064/) give 785 nonempty forest faces, 23 face orbits, 15,255 orbit cells with vector (23,283,1535,3984,5230,3360,840), integral boundary-square zero on every cell, and 7,627 successive valid free-face deletions leaving that vertex. The certificate SHA-256 is 542dc0c6bc9cd5fe217c95eecc1a01f5a32dff27ea72c0895ad3828a429dda1a. The uploaded verifier was inspected only; it checks exactly one zero-cell, not its ID. The full automorphism group is determined by the five maximum independent stars and their pairwise intersections. In the repaired proof, the ranks of the support of a point of a closed chain simplex determine its support within that simplex, and group elements preserve ranks and barycentric coefficients. This proves each closed simplex embeds into the quotient, not merely that there are no inversions on open simplices. Omitted ranks distinguish its faces, including the two intermediate cofaces that would exist below any higher surviving coface. Thus unique immediate coface gives an elementary collapse of the actual regular quotient-cell subcomplex, and not just algebraic cancellation. The full original evidence remains unchanged; no certificate data or verification status was changed. This is a finite mathematical replay, not formal proof-assistant verification.

## originality

PASS

Pass the repaired claim of an explicit collapse of the ordinary quotient by the full automorphism group to the best of current knowledge. Correcting the terminal cell label and supplying the rank-based embedding justification do not expand the novelty claim. The exact same unquotiented complex, its group action and rational quotient acyclicity are prior coverage, not claims of novelty. The earlier fixed sets and related quotient or equivariant collapse results do not imply this ordinary orbit-cell collapse.

## value

PASS

The Petersen graph and its full action on the induced-forest complex form a canonical finite test case for how passage to an ordinary orbit quotient changes topology. The original has nonzero fifth homology, whereas the quotient has an explicit cellular collapse, strictly stronger than the already implied rational acyclicity. This determines the quotient's integral and simple-homotopy behavior and gives a reusable incidence certificate on the exact object, not just a one-off group-orbit count. Correcting the survivor ID leaves that motivation and mathematical contribution intact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
