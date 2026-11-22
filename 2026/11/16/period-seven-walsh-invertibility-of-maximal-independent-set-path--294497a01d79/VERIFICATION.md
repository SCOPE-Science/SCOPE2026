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

For n>=2 maximal independent path configurations are binary words avoiding 11, 000 and endpoint 00. The exact 00,01,10 transfer T(z) with row v_2=(0,z_2,z_1) and column w=(0,1,1)^T counts precisely this set. Direct integer multiplication of the alternating seven-sign block gives B=[[1,0,0],[0,1,-2],[0,0,-1]] with Bw=-w for every prefix; this extends zero witnesses at n=2,3,5 by seven vertices. The unweighted maximal independent set count obeys a_n=a_(n-2)+a_(n-3) and has parity period seven, odd exactly at residues 0,1,4,6; an odd signed character sum cannot vanish. Independent brute-force enumeration and exact Walsh-Hadamard transforms n=2..10 agree with all residues and the transfer law, but the finite check is not used in place of the all-n proof.

## originality

PASS

Best-of-knowledge: actual proof and cited primary/read indexed comparisons distinguish the specific result from older general tools and different objects; this is not a guarantee of priority.

## value

PASS

Simultaneous zero-freeness at all Boolean characters is a meaningful inverse property of a natural path kernel. The universal seven-letter involution and sharp periodic classification provide a nontrivial structural transfer law beyond the textbook Padovan count, with explicit singular-frequency construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
