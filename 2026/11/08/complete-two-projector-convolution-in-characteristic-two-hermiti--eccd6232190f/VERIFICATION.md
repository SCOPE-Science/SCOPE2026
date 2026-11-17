---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Hermitian rank-one idempotents are exactly P(a,z)=[[a,z],[z^q,1+a]] with a^2+a=N(z), because trace=1 and determinant=0 imply idempotence via Cayley–Hamilton; norm surjectivity gives 2+(q-2)(q+1)=q(q-1). S=P+Q has ordinary trace 0 and diagonal s; Q=S+P. Requiring both determinants zero leaves a linear relative-trace equation Tr(z w^q)=s²+s+N(w) and one norm=Artin–Schreier equation. For w=0 only s=0 or 1 works, with all q(q-1) choices. For w≠0 the relative-trace affine line has q z-candidates. The absolute trace of N(z) is either a nonzero affine F2-linear functional (q/2 z and two a each, hence q ordered solutions) or identically 1 (zero solutions), with exceptional condition N(w)∈{s²,(s+1)²}. Each allowed nonscalar target count is (q-2)(q²-1), plus two scalars; square weights give exact energy. Independent complete finite-field pair enumeration for q=2,4,8 gives (|P|,support,energy)=(2,2,8),(12,32,768),(56,380,30464), affirming q=2 boundary. Universal statement is proved by field trace algebra, not finite experiments.

## originality

PASS

Fulton gives a broad formula for XAX*=B by rank, but inspected full text does not impose the two individual norm-one constraints needed for self-adjoint projector pairs. The present complete constrained fiber law/support/energy is a distinct exact classification, to best of knowledge.

## value

PASS

A complete unnormalized ordered convolution law on the natural set of Hermitian one-dimensional orthogonal projections over each binary field; rank-sensitive support, missing matrices and additive energy are useful exact invariants in finite unitary geometry and additive combinatorics. It is not mere reparameterization of full-rank Hermitian matrix counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
