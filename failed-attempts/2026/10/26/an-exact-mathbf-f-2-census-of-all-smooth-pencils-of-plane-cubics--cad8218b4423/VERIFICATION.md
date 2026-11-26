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

In characteristic two the homogeneous Euler identity for cubics is F=XF_X+YF_Y+ZF_Z, so the chartwise derivative-ideal unit test is equivalent to geometric smoothness. Unordered triples {F,G,F+G} count binary two-spaces once; the 168 invertible substitutions are all projective coordinate changes. Distinct geometrically smooth plane cubics have no common component by Bézout and smoothness, so each base scheme has length nine. Reducedness is equivalent to full Jacobian rank at every geometric common zero. An independently written exhaustive calculation reproduced 336 smooth forms, 5544 pencils, 37 orbits, and the 4508 reduced/1036 nonreduced masses. Separate finite-extension enumeration through residue degree nine reproduced all 37 reduced-support partitions by divisor inversion; the degree cutoff follows from scheme length and does not truncate the smoothness test. Replay: branches/8361f75b-d376-4d04-bbca-f3a8bc1cd7ab/reproduce.py and support.py, with reproduce.out and support.out. The extension calculation certifies support, not individual local multiplicities. This is an exact replay and proof check, not formal verification.

## originality

FAIL

The earlier extension-incidence theorem explicitly gives the same 5544 fixed-coordinate pencils and 37 rational projective orbits, even with the same stabilizer distribution and canonical representatives. These are two central components of the frozen claim, not coincidental counts or general existence bounds. The earlier theorem's rational base-point tabulation does not give the reduced/nonreduced split or the Frobenius support-degree partitions; no duplication of these refinements is established here. The FAIL concerns the frozen census as a whole, not the truth of the numbers or a separately re-audited refinement.

## value

PASS

The already published headline counts do not themselves confer value. The geometric base-scheme refinement does: the reduced/nonreduced split distinguishes pencils with transverse intersections from pencils with geometric multiplicities, and the 37 support partitions provide exact residue degrees needed to compare the base schemes over extension fields. These are natural invariants of this complete finite family, not another count of already catalogued rational points. This value assessment does not cure the originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
