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

The unnormalized XOR convolution is diagonal on all 45-edge characters, with one summand per unoriented simple octagon. The independent enumeration projects onto four distinct synthemes with successive intersections equal to four distinct duads, and chooses one cyclic orientation and base per cycle. It finds 90 distinct octagons, 16 uses of each edge, and no smaller cycle. The incidence graph is connected: disjoint duads share a syntheme, and two intersecting duads have a third duad disjoint from both. Switching is addition of a cut and fixes all cycle evaluations, hence each switching class has 2^29 frequencies. An independent binary row reduction of the 45-by-90 incidence matrix finds rank 16, so the evaluation image is precisely one word per switching class. Enumerating the image in Gray order and binning by 90−2 times Hamming weight reproduces all eighteen levels and multiplicities. The even edge incidence makes every codeword even weight and every multiplier 2 mod 4. In the original BFS convention cotree mask 85 attains −2; the trivial character attains 90. Fourier diagonalization therefore gives full range, inverse norm 1/2 and condition number 45 for the stated normalization.

## originality

PASS

The 90 octagons, their quadrangle interpretation, and underlying graph symmetry are credited. The nonvanishing congruence follows easily from that known cycle count and edge-transitivity; it is not the differentiating contribution. The exact signed frequencies on switching classes, or equivalently the length-90 evaluation-code weight distribution, survive the comparisons. The closest Resultary entries for other graphs or operators are not stronger statements about this spectrum.

## value

PASS

The Tutte–Coxeter graph is the natural cubic girth-eight cage, and its shortest cycles define a canonical support for recovery by convolution. The spectrum determines the complete cancellation distribution and sharp stability on the full Boolean edge space, beyond the unsigned cycle count or the parity-based nonsingularity alone. It also provides the exact weight enumerator of the associated short-cycle evaluation code, which can be used independently for comparisons with parallel cage constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
