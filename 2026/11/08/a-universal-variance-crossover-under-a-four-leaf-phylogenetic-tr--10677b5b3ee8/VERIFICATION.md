---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For descendant clade indicators I_e, E I_e=1-q^|D_e| and cov(I_e,I_f)=q^|D_e|(1-q^|D_f|) for nested D_f⊊D_e, zero for disjoint clades. This exactly gives the standard edge-covariance variance identity. The two bottom four-leaf topologies have mean difference q²(1-q) and variance difference q²(1-q)(q³+3q²+8q−5). On grafting the same backbone, each new ancestral edge of descendant size j contributes 2q^j times the bottom mean difference to variance; hence sum j=4..n−1. Independently reconstructed the mean/variance polynomials from all descendant-edge masks for n=4..8; exact symbolic equality held. H_n'(q)>0 and endpoints H_n(0)=−5,H_n(1)=2n−1 imply a unique switch. H_{n+1}=H_n+2q^n gives strict decrease, and uniform geometric-sum limit gives polynomial q^4−2q³−5q²+13q−5 and q_infty≈0.49114. For n<=3 there is only one unlabelled full-binary rooted shape. Finite polynomial checks corroborate, do not prove the all-n graft induction.

## originality

PASS

The Faller–Pardi–Steel 2007/2008 primary paper establishes the general rooted-PD edge-covariance formula (a necessary antecedent), whereas the reviewed new conclusion is an explicit all-n pair of tree topologies with exactly one variance crossover, strict n-monotonicity, and an algebraic limiting threshold despite opposite fixed expectation ordering. Related phylogenetic variance rankings in Resultary involve rarefaction, different tree pairs, or multiple variance peaks and do not directly prove this all-n grafted pair. A broad covariance formula makes the computation possible, but alone does not state the topology family or uniqueness proof.

## value

PASS

This provides a mathematically motivated counterexample to treating higher expected future phylogenetic diversity as an ordering of uncertainty: the expected ranking never changes, yet the variance ranking switches once at a sharp extinction probability. The sharp four-tip onset, monotone dimension-dependent thresholds and exact algebraic limit are reusable structural information about a standard stochastic biodiversity functional, not a mere restatement of edge covariance or isolated finite calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
