---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The signed matching sum splits by sizes zero through three. Inclusion–exclusion across three row choices produces (1+S1)(1+S2)(1+S3)−(1+S1)C23−(1+S2)C13−(1+S3)C12+2T. Counting matchings yields n^3+2n+1 ≡n+1 mod2, forbidding any zero at even n and requiring even magnitudes at odd n. The explicit H4 block has net C13 shift −4 and W shift 4(1+S2), preserving zero and −2 witnesses when S2=−1; H8 all sign triples has every nontrivial moment zero, preserving ±1 base witnesses at even lengths 2,4,6,8. These constructions prove the all-n parity dichotomy and sharp positive gaps, and Fourier eigenvalue reasoning gives inverse norms. Independent exact full Walsh enumerations n1..6 agree (zero counts 3,0,72,0,2730,0; gaps 2,1,2,1,2,1), not used as infinite proof.

## originality

PASS

Best-of-knowledge new all-matchings signed Fourier invertibility classification for every K3n width; known two-edge-only matching transform has a different zero-free criterion, and Wagner’s Heilmann–Lieb-type sector nonvanishing results do not decide arbitrary independent ±1-edge Walsh specializations on every K3n.

## value

PASS

Exact all-length parity classification and sharp inverse/pseudoinverse norm for a natural full-matching incidence codebook is a meaningful spectral boundary, with structural four- and eight-column witnesses rather than a tiny-instance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
