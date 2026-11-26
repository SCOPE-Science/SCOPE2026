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

At the first possible second topple of w, each other vertex has contributed at most once along each edge. Thus w has at most c(w)+1_{w=v}−b_w grains after its first topple, strictly below threshold by stability and b_v≥1. For a full avalanche c(v)=d_G(v)−1, v topples first, and all nonsink vertices topple exactly once. At each u≠s,v its final height is η(u)=c(u)−b_u, nonnegative and less than d_{G−s}(u). The sequence after toppling v is the Dhar test on G−s rooted at v: at yet-unfired sites both the actual height and degree threshold decrease by b_u relative to the original process. Conversely any recurrent η there extends to c by that inverse shift and setting c(v) to maximum; the same legal topplings stabilize c+δ_v with full support. The constructed c is recurrent because the sequence remains legal from c+b, and each vertex toppled once returns precisely c. Disconnected deletion prevents spread beyond the source component. The singleton deletion has one recurrent empty configuration, agreeing with the one-vertex tree count even for multiple sink edges. For the wheel, the hub deletion gives a cycle; the rim deletion gives the fan. The fan reduced tridiagonal determinant (endpoint diagonal 2, interior 3 for a path of length at least two vertices, off-diagonal −1, and determinant 1 for one path vertex) has determinant recurrence t_k=3t_{k−1}−t_{k−2}, with 1,3 giving F_{2k}. With β=φ⁻² each wheel eigenvalue is β⁻¹(1−βω)(1−βω⁻¹) over n-th roots ω, giving β⁻ⁿ(1−βⁿ)²=L_{2n}−2. The exact probabilities and their limits follow with fixed sink-neighbor drive and uniform recurrence.

## originality

FAIL

Earlier wave/forest and held-site burning results cover the central count and restriction mechanism. The arbitrary-loopless-multigraph held-site law in Bou-Rabee, arXiv:2610.13940v1, Lemma 2.1, gives τ(G−s) by the explicit reduction below; its §4.2 Eqs. (4.5)–(4.6) already implement the restriction of post-wave heights to recurrent states on the wave-induced graph in a box, where a full wave has a singleton complementary sink. The exact hub numerator and total wheel count are prior, and the rim numerator is the known fan count once the covered rule is applied. This is demonstrated mathematical implication, not a claim that the original wording or arbitrary-graph full-avalanche formula appears verbatim in those sources.

## value

FAIL

The maximal-avalanche event is natural and the wheel comparison illustrates real boundary dependence. Nevertheless the central count is a mechanical extremal specialization of existing wave/burning and forest structure, and the rim versus hub formulas insert already known fan, cycle and wheel counts. The record does not establish a further independent structural result, sharp unknown invariant, or nonmechanical remainder worth accepting on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
