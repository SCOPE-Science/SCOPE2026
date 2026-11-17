---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Necklaces are binary length-10 words modulo rotation, with adjacency iff a single bit changes after choosing rotations. Complete orbit enumeration/Burnside gives 108 necklaces, 56 even-weight and 52 odd-weight. Single-bit adjacency is bipartite and any simple path has at most 52 odd and 53 even vertices, hence at most 105. The actual CERTIFICATE.txt has 105 pairwise distinct canonical representatives, and 104 successive pairs have Hamming-one representatives. Complete independent checks of all 1024 words and the certificate verify the finite lower bound; combined with the parity inequality this proves exact longest path 105 vertices (104 edges), without assuming a heuristic solver is exhaustive.

## originality

PASS

Karhumäki–Puzynina–Rao–Whiteland give the general parity upper bound and conjectured its sharpness, earlier checking even orders through eight. Mütze’s 2023 survey states the even-order balancedness obstruction to Hamiltonian 1-Gray codes; Degni–Drisko’s earlier Gray orders and 2008 n=9 construction address different settings. No inspected primary passage supplied the exact order-ten 105-vertex witness. PASS best-of-knowledge with incomplete primary 2016 full-text and hidden-equivalent-path risks.

## value

PASS

The exact next even instance of a stated path-sharpness conjecture is a natural finite boundary problem. A complete independently validated 105-word witness closes that natural n=10 case despite not solving the infinite-family conjecture; finite certificate is a legitimate exact structural result, not a randomly selected tiny graph statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
