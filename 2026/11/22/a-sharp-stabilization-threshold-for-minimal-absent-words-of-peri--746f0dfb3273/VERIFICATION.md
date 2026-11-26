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

Primitive rotations are distinct even after dropping their final symbol, since a shared length-(d−1) prefix would fix the final symbol by the common letter counts. This proves both uniqueness of phase and the length-d bound for minimal absences of the infinite periodic language by matching the overlap of the two proper end factors. At n≥2d−2 every phase of length d−1 is present, so all periodic minimal absences persist. Any further finite-prefix minimal absence must be a periodic factor. For such a factor of length l≥d, its prefix forces its phase i to satisfy i+l=n+1; its suffix can then fit only if the next phase wraps to 0, so i=d−1. The candidate's two proper end factors occur at d−1 and 0, whereas the candidate itself cannot fit. For d=1 the finite prefix of a single repeated symbol has just the unused letters and a^(n+1); substituting n=std gives the power formula for every d. At the supplied d=5 sharpness example, 11011 is a periodic minimal absence but its suffix 1011 does not occur in the length-7 prefix. Independently, for every d≥2, the primitive period 0^(d−1)1 has periodic minimal absence 1·0^(d−2)·1: its two end factors occur periodically, but its ones are too close. Its prefix 1·0^(d−2) first ends at length 2d−2, so this minimal absence is lost at n=2d−3. This checks even the pointwise worst case over roots of each length d≥2. Both supplied enumerators were inspected but not executed; their reported runs are finite corroboration, not the proof.

## originality

PASS

Credit the circular antidictionary formula and the exact distinct-run power subclass to prior work. The distinct claim is the single finite-endpoint obstruction for arbitrary primitive periods and arbitrary sufficiently long prefixes, with a sharp threshold; no retrieved stronger statement supplies that claim.

## value

PASS

The theorem explains exactly how a linear cut changes a standard invariant of a periodic language. It handles incomplete periods, identifies a single changing word without enumerating the growing prefix, and locates the earliest universally valid cutoff. The representation is compact, although explicitly outputting the long word still takes time proportional to its length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
