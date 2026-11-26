---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The up-step weight attaches once when extending each legal prefix; the state recurrence therefore returns the unnormalized signed sum at height 0 after ten steps. An independent exhaustive direct sum over all 42 ballot bases and all 1024 masks reproduced the histogram and parity partition: the sole all-zero normalized row is (1,1,1), with 32 entries, and every other row is nonzero entrywise. First and last steps supply two free endpoint-frequency bits. Thus the rank is 896, the sharp nonzero gap is 2, and the top magnitude is 42. The disjoint odd-parity blocks force minimum weight three with 2·2·4 choices at that weight. Odd base counts 1 and 5 exclude zeros at semilengths one and three. For Z=s₀+U⊥, character orthogonality gives the inverse multiplier of 1_Z as (1/8)(−1)^{s₀·x}1_U; subtraction from δ₀ gives the exact signs and mass 7/4. An average of translation conjugates of any projection still has image in the same range and fixes it pointwise. It is diagonal under Walsh transform and thus is the unique spectral projection. Translations are isometries at both endpoints, and a delta or a sign-matched input attains the corresponding kernel-mass bound.

## originality

PASS

The supported distinction is the exact affine real zero locus for the full semilength-five basis family. The general projection theorem is prior; the eight-shift kernel and evaluated sharp constant are consequences of the new Fourier support, not a new general optimality principle.

## value

PASS

The full ten-step base family is the first singular case among odd semilengths, not a chosen arbitrary subset. Its exact missing characters partition into a simple affine coset, supplying both a sharp inverse gap on the surviving modes and an eight-shift, endpoint-optimal way to excise the null modes. Those exact data are useful for testing Fourier recovery and distinguishing genuine degeneracy from mere divisibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
