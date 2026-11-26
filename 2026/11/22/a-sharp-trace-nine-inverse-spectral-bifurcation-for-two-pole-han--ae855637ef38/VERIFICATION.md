---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The two geometric columns of V are independent and the positive eigenvalues of VV* equal those of V*V; its positive off-diagonal entry makes them distinct. With p=ab and q=a²+b², the trace fixes (1−a²)(1−b²)=(1−p²)/(T−1) and q=(T−2+Tp²)/(T−1). The determinant is the reciprocal of the former product minus (1−p)⁻². The discriminant for a²,b² is (1−p²)((T−2)²−T²p²)/(T−1)², so the precise nondegenerate range is 0≤p<(T−2)/T. The reconstructed squares have nonnegative sum, nonnegative product p²<1, and positive product of their complements, so both are in [0,1); p=0 is allowed. The derivative of D_T has the sign of −Q_T, where Q_T=Tp²+(3−T)p+1. At T>9 the vertex is inside the interval and Q_T is negative there, but Q_T(0)=1 and Q_T((T−2)/T)=1+(T−2)/T>0, proving both critical points are admissible. The three strictly monotone branches give the claimed open interval; the cross-multiplied cubic bounds every fiber by three, including endpoints. At T=9, Q_9=9(p−1/3)², and the derivative denominator (1−p)³(1+p)² equals 128/243 at p=1/3, giving the cubic coefficient −729/64 and strict monotonicity through the flat point. For an exact replay of the witness at T=12,D=199/20, the numerator of D_T−D after multiplication by 20(1−p)²(1+p) is 1−41p+199p²−199p³; its signs at p=0,1/10,1/2,5/6 are +,−,+,−, so all three roots exist in the admissible interval. The stated checker was inspected but not executed.

## originality

PASS

The closest general theorem does contain the Gram matrix after a Cayley transform, but it inverts richer, weighted spectral data. The inspected primary and indexed statements do not establish the eigenvalues-only fiber cardinality or its trace-nine transition under the fixed-unit Hankel mass constraint. This passes the supported specialized classification, not novelty of Gram reduction, Cauchy spectral theory, or inverse moment problems.

## value

PASS

Fixing both masses at one removes the usual free normalization parameters and leaves as many unknowns as measured eigenvalues. It is not then evident that spectra can have three preimages or that the entire low-trace region is identifiable. The sharp trace boundary, open interval of triple ambiguity, and flat cubic at criticality give useful limits on reconstruction from spectral data alone, including the loss of first-order inverse conditioning at the critical fiber. The inverse statement concerns a motivated two-atom Hankel class, not a single numerical isospectral coincidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
