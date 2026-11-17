---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For every n>=3 and labelled cycle C_n, a total outer-independent dominating set has exactly a cyclic distance-three packing as its complement: outside independence forbids adjacent outside vertices, and total domination forbids an outside pair at cyclic distance two. For three nonempty blocks the coalition graph without isolated vertices is P3 or K3. In a path, exactly the two leaf blocks are packing complements; in a triangle, all three are. Seven pair-color states, their 7x7 transition T with characteristic (x^3+x-1)(x^4-x^3-x^2-2x-1), and a weighted 3x3 forbidden-union U with polynomial x^3-x^2-2 give t_n-f_n. Paths are counted twice and unique three-periodic triangles (only 3|n) six times, hence N_n=(t_n-f_n)/2-2*[3|n]. T is primitive; the quartic Perron root dominates all other roots and U, giving N_n~lambda^n/2 with lambda=2.065994892... . Direct independent enumeration by original domination/neighborhood definitions confirmed unordered partitions for n=3..9: (1,6,10,25,63,130,280) with triangle at n=3,6,9, not extrapolation.

## originality

PASS

The original Buntina–Golmohammadi cycle theorem gives only the maximum size three of a TOI-coalition partition; no source actually inspected supplies the labelled unordered optimizer census, its P3/K3 split, or the coupled characteristic-polynomial recurrence. This is best-of-knowledge, not unconditional historical priority, because full primary PDF could not be obtained.

## value

PASS

An exact optimizer census for every labelled cycle is a motivated and nontrivial strengthening of a known extremal size in a recently introduced domination/cooperation notion. The path/unique-triangle classification and growth entropy describe all maximizers, not a tiny-instance table or a mere restatement of the 3-block maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
