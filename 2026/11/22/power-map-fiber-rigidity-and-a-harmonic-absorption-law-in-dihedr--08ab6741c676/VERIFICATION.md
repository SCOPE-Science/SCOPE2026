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

From the alternating-word normal form, a further copy either adds its entire even length ℓ or adds ℓ−1 when the length is odd; until saturation the first letter and length parity are preserved. Thus the respective unsaturated lengths are rℓ and r(ℓ−1)+1, cut off at m. Inverting these transformations within each parity and first letter gives exactly one preimage for each attained nonlongest element, including the fixed identity and generators. The cutoffs for ℓ=2h and ℓ=2h+1 give A_r and B_r, respectively, establishing the image and longest fiber counts. At r=2 the sum of floors is (m−3)/2 for odd m, m/2−2 for m divisible by four, and (m−2)/2 for m≡2 mod four. Length two attains the maximum first-passage time ⌈m/2⌉; all other lengths absorb by then. The exact tail is (A_r+B_r)/(m−2)=1/r+O(1/(m−2)) uniformly for 1≤r<⌈m/2⌉ and is zero thereafter. Summing yields log m+O(1); taking fixed-r successive CDF differences yields the normalized mass 1/[k(k−1)] with divergent mean. These arguments cover m=3 and r=1 as well. The uploaded checker and recorded 380120 finite checks were inspected, not run; large-m frequencies are evaluations of the depth formula, not independent evidence of convergence. No computation is needed for the universal proof.

## originality

PASS

No covering quantitative dihedral census was identified in the inspected sources. The pointwise power rule uses the standard normal form and follows by direct iteration of the known product rule; eventual absorption and the abstract limiting mass are not distinct claims of novelty. The supported contribution is the combined all-exponent fiber rigidity and counts, root congruence law, and quantitative hitting-time distribution for uniformly chosen dihedral nonidempotents. This does not assign priority among same-day records.

## value

PASS

The complete finite-time power-map census is an exact invariant of a standard aperiodic monoid and distinguishes the persistence of individual elements from their many-to-one collapse. The mod-four split and the combination of a fixed heavy-tailed limit with a growing finite mean are useful quantitative information not supplied by eventual idempotence or qualitative rank-two normal forms alone. This is a narrow structural classification, not a new universal probability law or a higher-rank theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
