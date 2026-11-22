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

Complementing all four frequency bits in one column does not change a character on a column of X with exactly two ones. Thus only three relative bits per column matter: eight types, and column permutations reduce the 2^24 n=3 frequencies to 1716 histograms, each with exact multiplicity 2^(2n)(2n)!/prod(c_v!). Selecting the six possible row pairs per column gives coefficient [z_1^n...z_4^n]prod_v P_v(z)^c_v. Dynamic programming storing three row counts (fourth determined by 2t) has O(n^3) states, 2n steps and six transitions, O(n^4) per histogram, O(n^11) overall; coefficients have O(n) bit length. An independently written integer DP enumerated all 1716 n=3 type histograms, reproduced all 29 signed levels and multiplicities, 8388608 zeros and Parseval 2^24*1860. Inspection of the pinned verify_eulerian_k46.py and its source CSV blob confirms it recomputes every orbit coefficient and does 256 auxiliary direct signed sums, rather than claiming sampled frequencies exhaustive. Exactly half frequencies are odd weight and vanish by complement symmetry; the exact census shows none of the even-weight ones vanish, giving range equal to complement-even functions and norm-one projection. Minimum nonzero 4 and maximum1860 give condition465.

## originality

PASS

Nester already established 1860 unsigned Eulerian orientations of K_{4,6}; that count is explicitly excluded from novelty. The assessed contributions are the all-frequency signed eight-type compression with a polynomial-time enumeration scheme and the complete 4x6 signed 29-level Fourier census and recovery gap, not standard orbit-counting or Fourier diagonalization alone.

## value

PASS

This is the first non-square four-row Eulerian-orientation grid K_{4,6}, where the signed spectral census answers exactly how much information convolution loses and its optimal L² recovery stability. Eight-type compression gives an all-width polynomial-time exact method replacing 2^(8n) direct characters. The 29-level spectrum, half-rank and sharp gap are independently useful invariants of a natural balanced-table family, not an arbitrary tiny slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
