---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A cyclic word with q^n-1 distinct n-windows gives a closed edge-simple trail in the directed de Bruijn graph. Subtracting its balanced degrees from the full degrees shows that the sole missing edge is a loop, hence a^n. Removing such a loop from a full tour is exactly deletion within its constant run; the run cannot be longer because the loop occurs only once. Deleting outside the q disjoint constant windows preserves every loop and therefore cannot yield a qualifying trail. This gives qn successful indexed positions and q distinct outcomes. In a shortened trail the vertex a^(n-1) has q-1 outgoing incidences. Inserting the missing loop at each restores a full tour. Distinct gaps yield distinct cyclic tours since deleting the unique loop recovers the cyclic order of distinct old edges with the gap identified. Thus double counting gives q D_q(n)/(q-1) with the stated classical D_q(n). Independently, deleting a loop leaves all rooted arborescence counts unchanged and changes just one BEST factorial from (q-1)! to (q-2)!, verifying the fixed-letter count. For n=1 the graph has one vertex and q labeled loops; deletion works at every letter, there are (q-2)! shortened cyclic orders per missing letter, and insertion has q-1 gaps, including the single gap for q=2.

## originality

FAIL

The binary count is explicitly prior, and the nonbinary structural and census claims are mechanically implied by an earlier indexed two-deficit classification and its actual balance/BEST argument together with the classical puncturing rules. The identification of successful indexed deletions and their fibers is a direct consequence, not an independent remaining claim. This does not assert that the exact combined wording was previously printed.

## value

FAIL

One-symbol deletion robustness and complete short-cycle census are natural questions, and the exact numbers are useful as background. The statement as an independent contribution reduces to the one-edge balance argument, one standard factorial ratio, and classical single-loop insertion/deletion. No separately useful unknown exact invariant remains beyond those mechanically implied facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
