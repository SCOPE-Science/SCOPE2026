---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For P=c₀…c_{q−1} with distinct q≥3 letters and k≥2 copies, q singleton factors force at least one occurrence of each letter in an attractor, so a size-q candidate chooses one position q t_i+i for each letter. The junction factor c_{q−1}c₀ appears only at internal junctions; if c₀ at absolute 0 and c_{q−1} at qk−1 are both chosen, no chosen occurrence meets any junction. Conversely, any other one-per-letter selection meets an internal junction. Every short factor either lies within a period (met by its chosen start letter) or crosses a junction (met by a selected endpoint), while the union of translated occurrences of any factor of length ≥q is a contiguous interval missing less than q letters at either end; evading that interval would force both forbidden endpoints. Hence exactly k^q−k^{q−2} choices are valid. Independently enumerated all distinct literal factors and every one-per-letter candidate for q=3..5,k=2..4 (1,751 candidates), with no discrepancy. The proof covers all q,k, not merely that finite sweep.

## originality

FAIL

Decisive published earlier Resultary theorem dated 2026-10-18 treats ALL prefixes P^m c₀…c_{r−1} for q≥2 and 0≤r<q, and classifies all minimal attractors and their count. Setting r=0,m=k specializes exactly to the submitted complete-period theorem: both failure conditions are t_{q−1}=k−1 and t₀=0, and earlier count m^q−m^{q−2} becomes k^q−k^{q−2}. The earlier theorem is strictly broader. The Nov2 distinct-run-power theorem independently covers all run lengths, and its all-singletons case is the same formula. The full earlier proofs were read, not merely title-matched.

## value

PASS

Classifying every minimum attractor and its cardinality for a natural periodic-permutation word family is a motivated combinatorial invariant. Its single critical junction factor is a mathematically useful local certificate. The proposed family is nevertheless fully solved by earlier stronger results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
