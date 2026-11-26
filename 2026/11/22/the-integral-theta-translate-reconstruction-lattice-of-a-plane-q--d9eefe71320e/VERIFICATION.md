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

A smooth plane quartic has genus three and is nonhyperelliptic. An effective even theta characteristic of degree two would have at least two sections, giving a degree-two pencil, impossible here. The mod-two theta parity theorem in characteristic ≠2 identifies the 28 effective odd characteristics with the value-one locus of a nondegenerate Arf-zero quadratic form based at an even characteristic. In hyperbolic coordinates q(u,v)=u·v; the support is q=1, not q=0. The polarization gives zero autocorrelation of the sign of q at nonzero shifts, yielding the 28/12 incidence counts and M²=16I+12J with M1=28·1. The constant eigenvalue 28 and the other absolute eigenvalues 4 prove full rank and index 7·2^128. An independent exact integer Smith calculation, constructing the matrix from the parity formula without the uploaded verifier, returned 1^8,2^14,4^20,8^14,16^7,112. This agrees with the source's modular algorithm, whose unit pivots and divisions of an all-even residual block compute the valuations below its precision cutoff. The determinant has only one odd prime factor, which divisibility ordering attaches to the largest invariant factor. Finally M(7M−3J)=112I; every column of the inverse has some entry −3/112 in lowest terms, and all entries have denominator dividing 112. Thus each individual point basis vector has exact order 112. Changing the even characteristic just reindexes the family of all translates. These are formal incidence-lattice statements, not claims about divisor classes or Jacobian torsion as an integral lattice.

## originality

PASS

The quadratic difference set, symplectic theta model and Menon design parameters are established; they are not credited as discoveries. The supported distinct contribution is the complete integral Smith quotient for the specific 64-by-64 support-translate design, together with its interpretation as the formal point reconstruction obstruction. The relevant graph-development Smith table is for a different matrix, and the available sources on the specific Menon/SDP designs do not establish exact Smith coverage. This is a bounded conclusion; the 1994 same-parameter design tables could not be fully compared.

## value

PASS

All translates and all two-torsion points form a canonical, small incidence problem rather than an arbitrary slice. The Smith factors give the complete formal integral obstruction to reconstructing point vectors from theta incidence, data needed to distinguish integral from rational generation and not supplied by the design spectrum. The sharp multiplier 112 has a clear interpretation, although it is a direct consequence of the Gram identity and is not alone the novelty. The full exact quotient is independently useful in both the theta-torsor and Menon incidence formulations, without requiring a claim about geometric divisor groups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
