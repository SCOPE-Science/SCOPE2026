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

Independent exact reconstruction from the seven cyclic Fano lines gave a connected cubic graph on 28 vertices with 42 edges, 84 distinct perfect matchings of size 14, 28 matchings through every edge, and pair co-occurrence counts 0:84, 4:21, 6:168, 8:168, 10:84, 12:168, 14:168. Branching on the minimum available degree exhausts matchings because every perfect matching chooses exactly one available neighbor of that vertex. In the sign product expansion modulo 8, the constant is 84, every linear term is a multiple of 8, and the even pair counts kill all quadratic terms. On each matching a vertex switch contributes one minus sign; a connected graph has 2²⁷ distinct vertex switches, and a spanning tree fixes exactly one representative of each orbit. In the supplied BFS gauge, the independent integer transform and direct 84-term sums agree at all 32,768 frequencies, with absolute counts 4:21000, 12:9548, 20:1890, 28:300, 36:28, 84:2, and the stated signed splits. Thus the entire group spectrum has no zero, and the extreme singular values 4 and 84 give condition number 21 for the unnormalized convolution. The signed splits refer to the BFS tree in the verifier (root the first lexicographically ordered triple, visit neighbors in increasing order), not to arbitrary spanning trees.

## originality

PASS

Biggs establishes the Coxeter graph's unsigned count, and a distinct same-day result on Desargues uses the same mod-eight mechanism. Neither gives the Coxeter pair-incidence premise or its 15-bit signed spectrum. The distinct claim is the graph-specific exact classification and invertibility; no originality is credited for the generic Walsh decomposition, switch reduction, or Boolean sign-product identity.

## value

PASS

This is the complete character spectrum of a canonical matching measure on a classical symmetric graph, not a selected finite sample. It settles potential cancellation for every binary edge signing and determines both invertibility and exact numerical conditioning. The pair-incidence explanation pinpoints the obstruction to a zero, and the precise extrema and multiplicities could be reused in studying the inverse or comparing symmetric graphs. The value is the exact invariant of Coxeter, rather than novelty of the computation or a claimed universal law for cubic graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
