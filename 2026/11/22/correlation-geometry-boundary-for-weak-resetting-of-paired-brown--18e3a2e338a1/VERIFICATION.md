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

Whitening gives the wedge of angle arccos(-rho): the unit inward normals after whitening have inner product rho. The positive survival-tail amplitude gives moment cutoff k<pi/(2 alpha), with logarithmic divergence at equality. Independently solved the generator equations in the space of homogeneous polynomials vanishing on the axes (replay: python /workspace/branches/independent_replay.py 1, SymPy, D=1; restore D^(-k) in moment k). This yields all three stated polynomials. To justify rather than assume uniqueness, apply stopped Dynkin at time t to each polynomial P_k; its remainder E[P_k(X_t); T>t] tends to zero. Gaussian moments and Hölder bound it by O(t^k) times P(T>t)^(1-1/p), and p can be chosen large enough when the tail exponent exceeds k. Induction and the Markov property identify the forcing integral k times the expected integral of the (k−1)st remaining-time moment with E[T^k]. The reset renewal quotient A/(1-rA) uses the exponential clock independent of each excursion. For rho>=0 the unreset mean diverges while the quotient is finite for every positive r. When only m1 is finite, (A(r)-m1)/r tends to minus infinity by monotone convergence and the quotient differs from A by O(r). When m2 exists, the linear coefficient has opposite sign to cU+6−9c²; the root is physical exactly for 2<=U<3. All such roots exceed sqrt(3)/2, so m3 is finite. The independently simplified equality coefficient after dividing out (xy)^3/D^3 is (162−161c²)/(720c³(4c²−3)), positive throughout the physical interval. The conclusions are local in reset rate, not claims about all-rate optima.

## originality

PASS

The standard Poisson criterion together with previously available wedge moments covers the strict first-order classification after a change of coordinates; credit that implication explicitly. What distinguishes the complete sharp local theorem as stated is resolving the physical zero-slope set, with an explicit coefficient of fixed positive sign on the whole set. The inspected prior moment and restart formulas do not supply this third-moment conclusion or the full strict local result including equality.

## value

PASS

The zero-derivative curve is a necessary part of a sharp decision rule for weak resetting and cannot be classified using mean and variance alone. Its uniform second-order sign, on every attainable start geometry where the first-order test is silent, resolves that issue without a numerical rate search. The scope is meaningful for the local correlated-search problem and does not require an all-rate optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
