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

Alternating site complementation turns exactly the N−1 rate-one reactions into adjacent swaps, and preserves the endpoint pair flip because both endpoints have odd indices. With m even-indexed sites, original even occupation gives K≡m (mod 2), so there are m+1 connected fixed-weight path classes; the endpoint flip connects all successive permitted weights at positive rate. The projected generator B averages endpoint vacancies/occupancies, obtaining b_k=(N−k)(N−k−1)/[N(N−1)] and d_k=k(k−1)/[N(N−1)]. An independent analytic spectrum check triangularizes B on 1,k,…,k^m, a basis by interpolation on the m+1 distinct permitted k's. In B k^j the terms of degree j+1 cancel, and the degree-j coefficient is −4j/N+4j(j−1)/[N(N−1)] = −4j(N−j)/[N(N−1)]. This proves all m+1 distinct eigenvalues including zero without assuming completeness of a parity-restricted polynomial family. The fast block of −L₀ is strictly positive for fixed N; on eliminating it by Schur complement, the small eigenvalue block is −εB plus O_N(ε²). Weyl bounds separate precisely m+1 small eigenvalues from the others, one staying zero. For the slow-time limit, write u=e^{s(L₀/ε+V)}h and Q=I−P; the Q-block is dissipative with fast gap at least g/ε. Variation of constants bounds Qu by e^{−gs/ε}||Qh||+ε||V||||h||/g, so the time-integrated perturbation of Pu from e^{sB}Ph is O_N(ε) on bounded s intervals. For empty start K=m, Bk=−4(k−N/2)/N and the averaged coverage is m/N+k/N², yielding the exact stated expression for each s>0. The isolated uniform K=m shell gives the lower plateau; the positive-rate uniform even-occupation stationary class has marginal 1/2. The fixed-N restriction is essential; no claim at s=0 or of an error uniform in N is made. The frozen CHECK.py is corroboration, not the source of the all-N proof.

## originality

PASS

Pass the specific fixed-odd-ring weak-closing-bond slow spectral splitting and empty-start coverage limit. The underlying reversible adsorption model, parity classes, and distance-two hypercube eigenvalues are established context, not the new claim. The main contribution is the exact reduction of the physical defect problem to the radial pair-flip chain and its spectral and coverage consequences. No inspected prior statement supplies that reduction for this defect.

## value

PASS

Opening the closing bond produces a whole set of conservation-law sectors, not simply a small correction to uniform equilibrium. The result resolves how all the associated zero modes split when that bond is restored and identifies the particular mode observable in empty-start coverage, quantitatively explaining the noncommuting time and defect limits. An exact all-odd-N reduction and full leading slow spectrum are useful beyond just reading off equilibrium coverage or substituting into an auxiliary cube spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
