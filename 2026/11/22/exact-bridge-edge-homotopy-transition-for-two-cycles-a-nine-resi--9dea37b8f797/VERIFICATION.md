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

Deleting one bridge endpoint u and then its closed neighborhood gives the base D=Ind(P_(p-1))*Ind(C_q) and link L=Ind(P_(p-3))*Ind(P_(q-1)), with Y the homotopy cofiber of L→D. When p≡1 the link is contractible; when p≡2 the base is contractible. When p≡0 and p>=6 the inclusion in the first path factor is null because it is a map from a sphere of dimension a-2 to one of dimension a-1; at p=3 the link maps through the equatorial Ind(C_q) in its suspension, which cones off. A join with the null first-factor map is null. Substitution of the path/cycle formulas gives rows (3,2,1), (2,1,1), (1,1,0) with all sphere summands in the claimed dimension. The removed simplices for bridge insertion are precisely those containing {u,v}; the closed star in X meets Y along its edge boundary joined with R=Ind(P_(p-3))*Ind(P_(q-3)). If a residue equals 1 this intersection and the star are both contractible, so the inclusion is an equivalence by a pushout along cofibrations, not merely by inferring equivalence from a contractible quotient. Otherwise the quotient is the double suspension of R, with (3,3) interpreted literally as an interval with its endpoints identified. The long exact sequence gives H_d(Y)→H_d(X) injective with free rank-one cokernel, using reduced homology for d=1; its splitting is integral, not canonical. Inspected `verify.py`, `verification_output.txt` and `VERIFICATION.md`. Their 72 absolute and 36 relative GF(2) results are the recorded bounded checks, not an integral or homotopy proof; the proof also handles the vacuous wedge and empty path.

## originality

PASS

The general vertex and edge cofiber methods are prior art. In particular, the bridge's absolute cofiber and the equivalence when either residue is 1 are direct applications of Adamaszek and the classical path formulas (with the elementary augmented-case convention). The supported distinct contribution is the full multiplicity and dimension table together with the integral primitive-loss conclusion, not the cofiber formula on its own.

## value

PASS

Connecting two cycles is a natural first nontrivial test of how homotopy and integral homology change when a bridge is inserted in a cactus. The full table distinguishes equivalence, loss of one primitive direct summand, and even sphere-to-contractible behavior. This gives information that a qualitative wedge result or knowledge of a relative cofiber alone leaves unresolved; no applicability to longer bridges or arbitrary cactus families is implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
