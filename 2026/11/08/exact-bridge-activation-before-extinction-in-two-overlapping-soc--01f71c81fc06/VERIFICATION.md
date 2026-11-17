---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For exactly two hyperedges A and B, source size a>=3, overlap 1<=c<min(a,b), target threshold k, all A initially active, all B\A inactive, per-vertex exponential recovery delta, whole-group activation rates alpha and beta, c<k forces P=0. If c>=k, excursions start from all A active; competing clocks yield success S=E beta/(alpha+beta)*(1-exp(-(alpha+beta)T_B)), extinction E=E exp(-alpha T_A-beta T_B), and renewal P=S/(S+E). The r=c-k+1-th overlap death rank J is hypergeometric w_j=binom(j-1,r-1) binom(a-j,c-r)/binom(a,c), independent of exponential spacings with rates (a-i+1)delta. Their Laplace products give the displayed exact finite sums. At fixed a,c,k,beta,delta, S~beta/alpha and E~a!delta^a/alpha^a, so 1-P~a!delta^a/(beta alpha^(a-1)), independent of c,k in leading term. Independently solved exact rational full 2^a microstate harmonic chains for a=3..5 across overlap/threshold examples including c<k; formula agrees. The original concrete case P=720/767 is reproduced.

## originality

PASS

Best-of-knowledge PASS. De Arruda et al (Nature Communications 2023) give the underlying simultaneous group-activation threshold rule and investigate hyperedge overlap/phase transitions, including a one-edge hyperblob calculation; the inspected complete public main article does not give the exact two-overlap first B-clock probability and universal strong-alpha coefficient. St-Onge and Higham–de Kergorlay use nodewise group infection or spectral SIS, mathematically different events. The de Arruda supplementary materials were not fully read; this remains a material priority risk, not an automatic O failure.

## value

PASS

PASS. In threshold hypergraph contagion, whether a finite infectious source activates a neighboring overlapping group before extinction is a natural first-bridge observable. The hypergeometric death-rank formula collapses a growing absorbing state space to a short explicit finite sum; the leading strong-reinforcement failure term unexpectedly loses all overlap and target-threshold dependence despite finite-alpha dependence. This is a motivated reusable exact benchmark, not an arbitrary one-off calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
