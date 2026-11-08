---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact verification and scope

The theorem concerns only the 105 perfect matchings of the labeled eight-vertex complete graph. Integer arithmetic exhausts all reduced sign assignments, not merely randomly sampled examples.

Run `python3 verify.py`: the code reconstructs all 105 matching masks, verifies uniqueness, performs all 21 layers of the integer Walsh–Hadamard transform on the complete \(2^{21}\)-element space, compares the entire 23-level histogram with fixed reference counts, computes the first two even spectral moments, and derives the fourth moment independently from matching-mask XOR differences. It checks the exact rational endpoint norm and prints `K8_MATCHING_WALSH_CERTIFICATE_PASS` on success.

Compile `cc -O3 -std=c11 hafnian_direct.c -o hafnian_direct`, then run `./hafnian_direct`. This separate direct method reconstructs the matchings recursively and sums all 105 monomial signs at every reduced edge assignment, without a Walsh transform. It checks all 106 possible nonnegative absolute levels (including absent levels), second and fourth moments, and the absolute first moment. It prints `DIRECT_HAFNIAN_CENSUS_PASS` on success.

Mathematical inspection additionally verifies the factor \(128\) in vertex-switching orbits, the normalization \(2^{-28}\) in the convolution kernel, the equality cases for its \(\ell^1\) and \(\ell^\infty\) norms, and the fact that sums of 105 signs cannot vanish. No external dataset or nondeterministic computation is used. These are finite-case certificates; independent mathematical audit is not yet performed and no general larger-order assertion is made.
