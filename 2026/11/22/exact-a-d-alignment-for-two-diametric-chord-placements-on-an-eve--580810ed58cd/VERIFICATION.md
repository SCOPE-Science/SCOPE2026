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

Frozen RESULT.md line 28 labels a matrix U^TPU but incorrectly gives diagonal 1+m/2; that is the diagonal of I+U^TPU. The complete corrected RESULT.md in repairs/1 corrects the identity and supplies its derivation and the Gram-matrix calculation; the original is unchanged. From g=Pb_0 and g_{j+m}=-g_j one obtains b_0^TPb_0=m/2 and b_t^TPb_0=(m-2t)/2. The cross-correlation S_t satisfies 2S_t-S_{t-1}-S_{t+1}=(m-2t)/2 and S_0=-S_m=m(m^2+2)/24, which uniquely gives the displayed cubic. Consequently the determinant factor is m+1+x and the Woodbury trace gives the stated rational gain. The derivative of the gain is strictly positive, so the discrete maximum of t(m-t) gives both optimizer sets including m=2 and both parities. Substitution of x=m-1 and x=m^2/4+O(1) gives the three stated asymptotics. An independently written grounded-Laplacian calculation matched both formulas and both optimizer sets for every admissible t at 2<=m<=9; see branches/625f4f20-8b81-4afa-8ed1-6b8315f4001e/independent_check.py. The finite check does not replace the proof. Frozen check.py and VERIFICATION.md were inspected, not executed.

## originality

PASS

The repair does not change the claim. Credit the general design objectives and matrix formulas to prior work. The supported distinct contribution is the two explicit laws and complete common equality classification for the restricted even-cycle diameter family. The pertinent circular and two-edge comparison results do not cover that family and both objectives.

## value

PASS

Two diameters are natural longest shortcuts on a unit cycle. Their relative separation changes the exact objectives; the result identifies the full set of common optimizers, and the resistance gain has a factor-of-two separation from adjacent diameters in the leading term while the tree-count ratio grows with size. This is a concrete two-objective benchmark, not simply evaluation of the general matrix identities or a claim about unrestricted augmentation. The proof repair leaves that value intact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
