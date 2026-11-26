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

For p>=5 the digit rule follows directly from the Laurent constant term under Frobenius: the least-significant digit factor has exponents of magnitude <p, so in taking the constant term only its exponent zero can match the higher factors. The recurrence excludes adjacent zero digits by descent, using invertibility of 3j, and T_0=T_1=1. From the generating function F and F=(1−2x−3x²)^((p−1)/2)F(x^p) modulo p, T_(p−1)=(-3)^((p−1)/2)≠0, so both boundary digits are allowed. With a nonempty forbidden set, consecutive admissible integers in a full block have a shared high prefix, change one digit to its successor in the ordered allowed alphabet, and reset the lower j digits from p−1 to 0. Their distance is 1+(d'−d−1)p^j. Isolated forbidden digits make d'−d either 1 or 2; each of the z single-digit holes occurs with a^(L−j−1) high prefixes, and both block endpoints are allowed. This proves exactly the zero runs of length p^j with the stated counts and global maximality, using the most significant forbidden digit for the equivalent block construction. For nonzero runs, each allowed high prefix gives the interior gaps and the two edge pieces. Each adjacent allowed high-prefix pair joins precisely one right and one left piece. The carry changes one digit across one of p−1−2z adjacent allowed pairs, giving the stated E; distinct mergers cannot span another run inside a length-p block since that block has a zero. The 0,1 pair ensures a join for L>=2, and the largest joined or interior run is strictly below p and attained globally. For z=0 all indices are allowed; no finite uniform nonzero-run bound is asserted. Independent direct modular polynomial convolution verified both histograms on seven (p,L) cases, including zero-free, one-hole, and two-hole alphabets.

## originality

PASS

Supported distinct result is the joint exact finite-block length census and sharp global bound when the digit alphabet has a hole, not the digit-product theorem, admissible population, or the known p=5 zero-free case. Related primary and catalog statements inspected do not give these exact multiplicities or the jointly sharp dichotomy.

## value

PASS

Run lengths are intrinsic to the natural ordering of this classical sequence, and complete base-p blocks are matched to the Lucas product. Density alone misses the coexistence of arbitrarily long divisible stretches and a uniformly bounded sharp maximum of nondivisible stretches. Exact multiplicities with endpoint accounting clarify how holes propagate across scales, and give more information than the admissible population or example runs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
