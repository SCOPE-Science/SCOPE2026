---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Exhaustive enumeration of all C(8,4)=70 balanced words with ballot test yields 14, then Walsh columns χ_S for |S|≤2 (37 columns) or ≤3 (93 columns). Direct symbolic Gram determinant computation independently rebuilt from definitions gives for G2 exactly z(z−12)^3(z−32)^3(z−52)(z−64)^3(z³−142z²+5576z−58112) and for G3 exactly (z−64)(z−96)^3(z−104)(z²−184z+8192)^3(z³−294z²+28528z−912896). These give rank 13 and 14. Eight words formed by 3 variable UD/DU blocks between fixed U,D have alternating cube signs, and every degree≤2 character misses some block, so they span the one-dimensional quadratic nullspace. Krawtchouk distance identity independently explains all Gram entries, and root localization identifies exact min/max eigenvalues 12/α and 64/β. Independent SymPy exact integer charpoly/rank reproduced both polynomials, not just claimed logs.

## originality

PASS

Best-of-knowledge original scope after positive mathematical implication comparisons, not inferred from mere negative search. Known Catalan bases, rank obstructions and parity Fourier multipliers are not equivalent to these two integer Gram characteristic polynomials and sharp spectra. A larger general interpolation theorem may imply the ranks but cannot determine singular-value distributions without metric/normalization; stronger coverage of rank is credited and excluded from novelty. Neither generality implies the actual new numerical spectral polynomial; the known 8-term obstruction and Catalan count are treated as foundations rather than claimed as novel independently.

## value

PASS

The first nontrivial Catalan family where pairwise marginal tomography fails has a complete exact operator stability spectrum and sharp condition constants for both observable quotient and cubic full recovery. The explicit nullspace and cubic repair delimit practical identifiability and stability on a natural combinatorial support; this spectral information is distinct from the already known matroid Hilbert ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
