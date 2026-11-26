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

I independently enumerated compatible permutations of the nine points and lines in both the classical and affine incidence models; each gives 42 matchings and every edge occurs 14 times. For each frequency S the parity of its negative matching count is the parity of the sum of those edge marginals over S, which is even. Therefore the signed sum is 42 modulo 4, never zero. Translating the matching masks by one reference mask and taking successive binary spans produces all 1024 elements of the cycle space: matching differences are even-degree, and the connected graph has cycle rank 27−18+1=10. I evaluated the 1024 signed sums by direct dot-product character evaluation in that basis, without a spanning-tree gauge or fast transform. Their absolute histogram is (2:504, 6:342, 10:81, 14:96, 42:1). Each character of the cycle space has 2^17 full extensions, whose sums differ only by the reference-mask phase. This proves the full multiplicities and the Hilbert norm and condition number. Direct reciprocal Fourier inversion in the translated space gave every stated numerator count, with no zero entries and absolute sum 1,676,288 at denominator 1024·210. I checked all 1024 direct XOR convolution identities; translating the kernel back by the same reference matching gives the full-group inverse because the translations cancel in characteristic two. Hence its support is exactly the matching coset. A delta input attains the kernel ℓ^1 norm for the ℓ^1 operator, and choosing the input signs to align all terms at one output attains the same norm on ℓ^∞. Both equal 1637/210, for unnormalized convolution on the full space.

## originality

PASS

The 42 matchings, gauge principle and reciprocal Fourier inversion are not new. The distinct claim is the Pappus-specific full signed-multiplier classification in absolute value together with the exact all-coordinate inverse support and endpoint amplification. The strongest same-day Resultary analogues use essentially the same method but different graphs or range-projection operators, with explicitly different spectra and constants. Prior Pappus sources treat ordinary matchings, their flip graph, or complements as two-factors, not evaluation over all edge signs. No inspected result or implication supplies the frozen spectrum or inverse data; this is a bounded statement about the exact invariant, not a claim of global priority.

## value

PASS

For the classical Pappus Levi graph this is a complete, useful recovery invariant, not the ordinary matching count or adjacency spectrum. Zero-free signed convolution distinguishes full recovery from projection onto a proper Fourier range in comparable cubic graphs. The exact endpoint amplification, substantially different from the Hilbert inverse norm, and complete affine inverse support matter for worst-case pointwise or total-error recovery. Neither is supplied by the unsigned count nor the generic Walsh method, and the exact histogram makes the inverse calculation checkable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
