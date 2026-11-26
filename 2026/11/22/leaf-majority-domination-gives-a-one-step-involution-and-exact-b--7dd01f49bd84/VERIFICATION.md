---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

All leaves at v copy the same current bit of v, so the image of every state has uniform leaf blocks. On the block-uniform set, the strict inequality m_v>d_H(v) makes the majority at v equal to its leaf-block bit regardless of core neighbors; leaves simultaneously copy the old core bit. Thus the map swaps the two words on this set, maps it bijectively onto itself, and has F³=F on the entire state space. All and only the block-uniform states recur; m_v≥1 ensures their 2^(2k) encodings are distinct, including for isolated vertices. The diagonal has 2^k fixed states and all off-diagonal states pair into two-cycles. The entry-time populations follow because no nonuniform state lies in the image; at minimum mantle size M=k+2|E| by the degree sum. For a fixed initial core word a, the neighbor contribution at v consists of s_v(a) plus the number j of its leaf ones, and equality of the two vote totals retains a_v. Each j has binomial multiplicity, and the leaf choices are independent across v in this count, so W(a,b) counts exactly F⁻¹(z(b,a)). Swapped phase fibres are disjoint, and assigning the target blocks uniformly shows every fibre is nonempty. The path on four vertices in the threshold example fails F³=F as claimed. An independently written direct six-vertex majority enumeration reproduces the double-star fixed basin sizes 1,1,9,9 and two-cycle basin sizes 2,6,6,6,6,18 (python3 /workspace/branches/small_exact_checks.py).

## originality

PASS

The eventual period bound and the passive-vertex mechanism on odd-degree trees are prior. The supported distinct finding is the complete one-step recurrent-set and individual-basin classification for arbitrary cores with strict private-leaf surplus at every vertex. Closely related published corona and pineapple results do not state or imply that full claim under inspected assumptions.

## value

PASS

This is a natural structured family of finite majority networks where a general period bound leaves both the exact entry populations and all attractor weights open. It separates recurrence, independent of topology at fixed core order, from basin sizes that depend on topology even at fixed mantle. For example, with two core vertices and m_v=2, the fixed attractor with core word 01 has basin size 1 with a core edge, and 9 with no core edge (now each degree-two neighborhood tie retains its core bit). The factorization gives reusable access to every labelled basin without enumerating the entire state space to answer a single query. The meaningful contribution is the combined classification, not the observation that leaves copy their neighbor.

The dated certificate retains the supplied scientific assessment, sources and limitations.
