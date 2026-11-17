---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For odd n and fixed 0<phi<1, remote reversal K>= (n+1)/2 has K~Bin(n,p), p=phi^2(2+phi)/[(1+phi)(1+phi+phi^2)]<1/2. The tilted law Q makes C>A balanced while both adjacent margins exceed 1/2 by delta=(1-phi^2)/(2(1+2phi)(2+phi))>0, allowing Hoeffding exponential suppression of adjacent failures on the remote event. Opposite orientation has Chernoff base beta_2 strictly less than beta by exact (1-t)^2(1+t^2)>0 at t=sqrt(phi). Stirling plus a geometric upper-tail summation yields sqrt(2/(pi n))*sqrt(p(1-p))/(1-2p)*beta^n[1+O_phi(1/n)]. Independently enumerated all 6^3 labeled ballots at phi=1/2, finding 32/1029 cycle probability, matching the package. Finite n does not prove asymptotics.

## originality

PASS

The sharp directed-cycle asymptotic for three candidates, including the explicit n^-1/2 constant and exponential separation of the two orientations, is not implied by the examined Mallows Condorcet-WINNER asymptotics or single-peakedness probabilities. Best-of-knowledge assessment, not chronological novelty proof.

## value

PASS

Majority-cycle probability is a natural social-choice invariant; the explicit sharp constant and separate exponentially suppressed orientation strengthen mere convergence-to-zero for a fixed nonuniform Mallows culture. The derivation identifies which pairwise reversal controls the rare cycle and a sharp first-order asymptotic, potentially useful in probabilistic voting analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
