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

A cyclic-image map kills G′ and is specified by its quotient functional and a generator of its image; idempotence means that the map fixes this generator. Normalizing the nonzero quotient line yields λ(u)=1 and a unique generator h above u for that map. Every element of the coset above u has order p and gives a legitimate lift, with exactly p^c choices; no centrality is used. The word ‘central-fiber’ in the proof is inessential and should be understood as an ordinary coset fiber. Equal nontrivial composites would force the same image and hence PQ=Q and QP=P, impossible for distinct maps. Thus adjacency is exactly the two cross-annihilations, giving an independent blow-up. Vertex and degree counts follow by fixing one or two independent functional values. In a clique the image vectors and functionals are biorthogonal, and independent image lines can be chosen in order and the dual coordinates extended freely in p^{k(d−k)} ways. Lifts and division by k! give the stated count. Extending by a basis of the common kernel gives maximal cliques of size d. In d=2 each base vertex has exactly one complement. In d≥3 choose r in ker λ outside span(u,v) (the kernel has dimension ≥2 and excludes u), and choose ρ with ρ(r)=1 and ρ(u)=ρ(v)=0. The intersection ker ρ∩ker μ is nonzero and meets span(r,v) only at zero, furnishing the second intermediary and distance at most three. In d≥4 ker λ∩ker μ contains a line outside span(u,v), producing a common neighbor; same-image distinct projections give nonadjacent pairs even without fibers. In d=3 the explicit pair has common kernel line ⟨e₁+e₂⟩ inside its image span, precluding a common neighbor for every p, including p=2. The component diameters for d=2 are 1 or 2 according to fiber size. Independent replay: python /workspace/replay/checks.py 4 composes the actual maps of an exponent-three Heisenberg group and enumerates complete clique counts by actual composition in F₂⁴ [1,120,1680,3360,840,0]; neither calculation substitutes for the group theorem.

## originality

PASS

The underlying abelian graph is the established nonincident point–hyperplane graph, not a new linear commuting graph. Several of its invariants are known or follow from prior local structure. The verified distinct claim is the exact uniform independent-fiber transfer for all finite prime-exponent groups, with the resulting counts and distance behavior for the actual retractions, irrespective of whether G′ is central. The inspected linear results do not provide that group transfer; the cited group comparisons concern particular families, not that full domain.

## value

PASS

This solves a natural group-endomorphism graph problem on the entire finite prime-exponent class: the actual commutation relation, not only an endomorphism census, loses all multiplication-law information beyond the two quotient sizes. Exact clique and distance invariants make the transfer usable, including for noncentral derived subgroups; no new claim is needed for known projective counts in the abelian base case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
