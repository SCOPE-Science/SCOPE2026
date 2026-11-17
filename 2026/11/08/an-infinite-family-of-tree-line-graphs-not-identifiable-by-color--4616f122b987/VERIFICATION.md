---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Reconstructed the explicit two-center tree T_m, with each center carrying m pendant edges and m length-two arms; |V(T)|=6m+2 and |V(L(T))|=6m+1. In its line graph the four degree-determined classes b,U,V,Z of sizes 1,2m,2m,2m have degrees 4m,2m,2m+1,1, respectively, and common equitable quotient rows (0,2m,2m,0), (1,m−1,m,0), (1,m,m−1,1), (0,0,1,0). Deleting uA1–vA1 and uB1–vB1 and inserting crossed uA1–vB1, uB1–vA1 preserves each class-to-class degree and therefore all ordinary color-refinement rounds, equivalently C² equivalence. The original line graph has precisely 2*C(2m+1,3) triangles. Two within-center removals lose 2(2m−1) triangles; each crossed edge gains one through central b, so the deficit is 4m−4>0 for all m≥2. Independently built the graphs and checked equitable quotient and triangle counts for m=2,3,5. The proof for every m is the symbolic quotient/triangle argument, not finite experiments.

## originality

PASS

PASS for the precise infinite two-edge-switched line-tree family and unbounded triangle deficit, though the general fact that line graphs need not preserve refinement-related properties is not entirely new. The 2015 Arvind–Köbler–Rattan–Verbitsky result proves that forests are amenable but does not construct this all-m line-graph twin family. An October 18 Resultary classification already gives a *single* nine-vertex tree whose line graph is non-orbit-refinable, so the qualitative line-graph closure obstruction can be inferred with further standard implications. That prior is a different orbit-equivalence assertion and does not state or imply this family of jointly refinement-equivalent nonisomorphic graphs with exact 4m−4 triangle gap. This limited novelty scope is explicit.

## value

PASS

A motivated structural closure question about a standard identification algorithm is answered with an exact infinite witness family and nontrivial triangle-count obstruction visible to stronger graph invariants but invisible to color refinement. It identifies an all-size mechanism via equitable class-preserving switches, not an arbitrary small counterexample or cosmetic reparameterization. The earlier finite orbit-refinement obstruction is acknowledged, preventing overclaim that any obstruction was first discovered here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
