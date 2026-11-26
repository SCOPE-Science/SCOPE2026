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

Each admissible one-hot word is exposed by selecting its symbol coordinate in each block. Given two words, the face restricting each block to their two symbols has vertices indexed by zero-sum choices from their difference support. If only empty and full choices work, that face is exactly their segment; otherwise complementary proper choices form a second pair of vertices with the same midpoint, excluding an edge. Binary minimal dependencies of size s>=3 are obtained by picking an ordered independent (s-1)-tuple on the selected positions and forcing the last element to be their sum; for s=2 there is a repeated nonzero symbol. This gives exactly the stated products and squared length 2s. Translation makes the per-vertex census constant and dividing by two counts undirected edges. Support size at most three ensures adjacency, whereas four identical nonzero differences give a counterexample for n>=4. At fixed d the highest allowed term has degree d+1 in n. At fixed n>=4 the s=n term is q^(n-1)-(2^(n-1)-1)q^(n-2)+O(q^(n-3)), the s=n-1 term contributes n q^(n-2)+O(q^(n-3)), and smaller supports contribute O(q^(n-3)); dividing by q^(n-1)-1 gives the stated dense limit. For d=2 the characters are labels modulo common shift. Pair differences sum to 4 times label-equality minus 1. For triple differences, start with free x,y and third x+y; excluding x=0, y=0, and x=y gives the all-labels-equal term of weight 16, three pair-equality terms of weight -4 and constant +2. Summing over positions gives the stated histogram eigenvalues and the quotient by four gives multiplicities. Independently check the gap by putting F_n=(degree-lambda)/4=(n-1)A-2R, where A counts differing pairs and R counts rainbow triples. For r=n-max(m), remove one occurrence of the most frequent label; if r>=2 the remainder is nonconstant. With A0 the cross-pair count among the r minority positions, the exact decrement is F_n-F_(n-1)=r(2n-2-r)-A0, at least r(2n-3/2-3r/2). This concave quadratic on [2,3n/4] is strictly greater than 2n-3 at both endpoints for n>=4 (excesses 2n-6 and 1+(n-4)(21n-16)/32), proving the strict inequality for r>=2 inductively from n=3. For r=1 the exact value is (n-1)^2. Thus for n>=4 there are exactly 3n minimizing nonconstant characters up to common shift. The n=2,3 skeletons are complete on 4 and 16 vertices, giving precisely the exceptions. An independent exact replay of the frozen finite gap range agrees with the analytic verification.

## originality

PASS

The object, vertex transitivity, even-parity rank-one alias and general adjacency criterion are prior foundations, not distinct claims. The supported distinct statements are the all-rank explicit Euclidean support-resolved census with its two limits and the four-symbol Fourier formula with the sharp all-order gap and multiplicities. No equivalent numerical or spectral result was found in the inspected passages and catalogue comparisons. This is a bounded best-knowledge decision, with a materially relevant thesis and possible phylogenetic comparison gaps disclosed.

## value

PASS

The full transversal polytope and its induced metric are natural existing objects. The exact support-resolved edge counts determine degree and show two opposing density regimes, not merely adjacency of particular examples. For the four-symbol family the explicit spectrum and minimized nonconstant gap with eigenspace dimension determine an exact expansion invariant of a natural infinite family. The sharp optimization is substantive beyond the generic Cayley diagonalization and uniform enumeration methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
