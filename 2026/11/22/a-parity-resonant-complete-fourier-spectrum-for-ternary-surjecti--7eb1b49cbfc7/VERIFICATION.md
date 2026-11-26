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

For counting convolution on the full ternary group, inclusion–exclusion gives the missing-colour contribution as the product of 2 for every zero frequency coordinate and minus the excluded letter's character at every nonzero coordinate. The singleton terms subtract that product from 1, and summing over the three colours restricts to balanced frequencies. At frequency zero ordinary inclusion–exclusion gives the support cardinality. The roots-of-unity filter on the nonzero digits gives (2^r+2(-1)^r)/3, including the empty r=1 class; only z=0 with even n adds balanced zeros. At odd n the z=1 class uses balanced pairs and realizes magnitude 3; at even n the z=1 class uses a balanced triple and pairs and realizes 9, while other surviving nontrivial classes have magnitude at least 9. The trivial magnitude is maximal by the triangle inequality. For the range projection, diagonal averaging is the inverse transform of the balanced-frequency indicator; at even n subtract the all-nonzero balanced mask. Its inverse transform at a word with n−2 zeros and two ones is (2^(n−2)+5)/3^(n+1), so the range kernel is negative there. The kernel mass is one and its absolute sum is the convolution norm at both endpoints. Multiplicity here means frequencies in a class, with multiplicities added if numerical levels coincide (already at n=3). An independent exact integer-pair enumeration matched all 1,080 frequencies for n=3 through 6 and the projection witnesses −3/81 and −7/729; it is bounded corroboration, not the all-length proof. The supplied checker was inspected, not executed.

## originality

PASS

The binary distinction between symmetry-forced and accidental Fourier zeros has a close published four-colour analogue using the same inclusion–exclusion strategy. The underlying counting formula and method are not new. The specific ternary signed spectrum, extra-zero parity, exact least magnitudes, and sign witness are not supplied by that result or by the earlier onto-word Gram theorem. This is a bounded finding, not a priority guarantee.

## value

PASS

For the natural onto-word indicator, the complete spectrum distinguishes the frequencies erased by translation symmetry from the extra balanced modes erased only at even lengths, with sharp recovery amplification on the retained space. The negative-kernel witness shows that even a small additional proportion of erased modes changes whether orthogonal recovery preserves positivity. These are exact operator-level distinctions from scalar counting and the low-frequency Gram law, not a claim of a new Fourier method. The orthogonal projection's endpoint norm is only separated from one, not evaluated sharply in the even case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
