---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For r=2^s−1 and m=2^s, factor the root a on each input disk a+mZ₂ with a<r. All remaining factors after extracting constants are 1 modulo 2 coefficientwise, since |a−h|<m. The root prefactor has valuation s−v₂(a+1), using r·binom(r−1,a)=(r−a)binom(r,a) and Lucas parity. The normalized quotient between any two parameters is odd, so the normalized map is a bijective isometry. Exactly 2^(j−1) centers give scale 2^j. In the last disk a=r the unique product factor of scale two is 1+2t, all others being 1 mod 4, and the image is the odd disk with scale two. The all-disk shift m·2^(k−1) preserves values; its half fails on the odd disk for k≥2. It is the least period because the least positive period divides any period, so if smaller it would divide this half-shift. (The proof's wording that any smaller period divides the exhibited period should refer to the least period.) Lucas settles k=1. Each branch samples 2^(k−1) t's per period: for scale 2^j it contributes 2^(min(j,k)−1) to every admissible residue, including all t's for y=0 when j≥k, and no others. Normalized Haar on the image ball is the conditional pushforward, yielding the stated density. The additional check `python3 /workspace/reproductions/exact_checks.py 5` confirms all residues and the half-period failure at s=7 with k=1,3,6,7,8; the proof is decisive for unbounded parameters.

## originality

FAIL

The least-period and image claims are already covered by classical general results. More decisively, the separate all-column dyadic-isometric-doubling record proves, in its standalone branch lemma, the exact scale and image ball of every fixed-column input disk. Its lemma specializes directly to the claimed full Mersenne fiber and Haar formulas. This is demonstrable coverage, not a priority inference from a shared date, and does not depend on the unlocated cubic-column note.

## value

FAIL

Mersenne fixed columns are a natural family and the formula is convenient, but as a distinct finding it is a direct evaluation of already available general branch data plus known period information. The application does not require a new invariant, argument beyond routine specialization, or a substantively distinct remainder. It is useful as an example of the general theorem, not a standalone contribution under the exact-invariant criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
