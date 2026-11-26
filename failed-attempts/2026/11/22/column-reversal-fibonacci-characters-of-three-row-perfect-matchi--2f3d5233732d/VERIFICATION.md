---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Theorem 3.5 of arXiv:2611.18058 gives the nonequivariant wedge of F_(n-1) spheres in degree n-1 and a contractible n=1 case. Symmetric extension follows from the stated bipartite integrality argument, or by taking the left half and central edges of any extension and mirroring that half to the right. For 2p+s vertices with p swaps, the augmented Lefschetz contribution is -(-1)^(p+s); thus the homology trace is (-1)^n Z_n. Independent transfers reconstructed 14 reachable states, 38 nonzero entries, all 14 vanishing exact moments and Z_1 through Z_4 equal to 0,1,1,0. Cayley–Hamilton gives the all-length recurrence; the stated Fibonacci signs, including F_-1=1 for n=2 and zero trace for n=1, follow. Rational quotient homology is the invariant homology after barycentric subdivision. Reproduction: python3 /workspace/checks/column_transfer.py; this uses subsets of local complete tile choices and does not run the frozen verifier. The Python 3.8 minimum in the frozen verification notes understates the supplied script's bit_count requirement (3.10). This does not affect the theorem or independent check.

## originality

FAIL

A distinct available record, Resultary eda18ed068e3, proves the identical all-width column character for the same edge-vertex perfect-matching complex via its 24-state transfer, then determines the stronger full Klein-four rational character and quotient. It is not merely a hit or an unverified citation: §3 supplies its own column terminal rule, same initial values and exact recurrence argument. This establishes equivalent coverage, not publication priority or ordering among same-day records. The integral trace equals the rational trace of the same automorphism on a free integral group; the n=1 addition is forced by known contractibility.

## value

FAIL

The trace would be a worthwhile invariant if unresolved, but the claimed result is exactly covered, including its rational quotient consequences. The frozen work offers a smaller single-involution encoding and a total-unimodularity proof of a symmetric-extension lemma, rather than a distinct useful mathematical remainder: for this mirror the lemma follows immediately by cutting any extension and reflecting its left matching. The automaton does not add a topological or integral equivariant classification, and the state-count difference has no established standalone consequence. No substantive repair of the supplied claim was identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
