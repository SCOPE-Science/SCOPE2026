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

The scalar unit is a central direct factor and the other factor is the affine group. For a fixed affine element (t,u), commutation is (t−1)z=us with 1+s a unit. The unrestricted kernel has size q^(m+min(ν(t−1),ν(u))). When ν(u)<ν(t−1), a forbidden s of residue −1 is impossible; otherwise each forbidden s has q^ν(t−1) lifts in z. The centralizers and both class families follow. Under conjugation the multiplier is fixed and the translation becomes yu+(1−t)z with y a unit, so the valuation bins used to divide by class size are invariant. A character nontrivial on the socle yields an injective additive-dual parameterization, since each nonzero ideal contains the socle; induction from unit stabilizers gives one layer of q^j irreducibles per valuation with orbit degree w_j, besides the zero-orbit U linear characters of the affine factor. The scalar factor replicates each degree U times. The q=2 overlap of degree one and the extra socle-sized affine center are correctly included. The class total, order, commuting probability and complex algebra decomposition then follow. An independent orbit enumeration on Z/4 and F4[e]/e² reproduced both spectra; the latter includes nonprime residue size. In particular it gave class counts {1:12,3:12,4:36,12:48,16:96} and degrees {1:144,3:48,12:12} for q=4, m=2.

## originality

FAIL

A distinct indexed affine-group record states an all-length classification implying both complete distributions and their consequences by the scalar direct product. This is demonstrated mathematical coverage, not an inference about priority from the two records' shared date.

## value

FAIL

The complete spectra are natural invariants, but as a separate result this frozen delivery adds only the routine effect of an abelian direct factor and immediate corollaries of already covered affine distributions. No new invariant determination or independently useful sharper boundary survives that reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
