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

The 240 exceptional curves correspond to E8 roots by E↦E+K_S with the negative intersection form; distinct curves have intersection 1−⟨α,β⟩. Summing the weights gives degree 241 and yields L=240I−J+RR^T. Root symmetry gives R^TR=60I and R^T1=0, so the spectrum is 0 once, 240 with multiplicity 231, and 300 with multiplicity 8. This certifies connectedness and tree determinant 240^230·300^8; only 2,3,5 occur. I checked the full integral classification by a different block reduction, not by trusting the submitted modular pivots. In an integral E8 basis let U be the 240-by-9 matrix of rows (1,α), G the E8 Gram matrix and V=diag(−1,G)U^T. Then L=240I+UV and VU=diag(−240,60I_8). The rows of U span Z⊕E8: every root is the difference of two roots (choose a root of inner product −1 and add it), and the roots span E8. Thus U is a split injection, and V is surjective by unimodularity. For p=2,3,5, extend U to a local basis. In that basis V=[VU,W], with W of rank 9 modulo p because VU vanishes modulo p. Changing basis in the complementary 231 coordinates makes W=[I_9,0]. The nine unit pivots in that block leave 222 factors 240 and the remaining block 240(240I_9+VU), with eight factors 72000 and one zero. Removing the single free factor gives the reduced Smith result and exponent exactly. Independent code checked the integral coordinates and primitivity, the two matrix identities, and the pair histogram 6720,15120,6720,120 at weights 0,1,2,3. In particular there are 28920 weighted edges and no seven-primary torsion.

## originality

PASS

The strongest primary source explicitly defines the weighted curve graph and identifies its E8 weight layers. The strongest separate indexed Smith computation concerns only the intersection-one graph. Neither supplies the frozen full-multiplicity group; the integral rank-eight extension requires additional structure beyond the rational spectrum or the prior clique results. This is a bounded best-of-knowledge judgment, not a publication-priority certificate.

## value

PASS

The object is the complete geometric intersection-multiplicity configuration, not a selected collection of E8 layers. Its graph Jacobian is a natural integral divisor-class invariant. The eight factors enlarged from 240 to 72000 exhibit exactly the root-lattice contribution, information absent from a tree count and from the simple intersection-one group's torsion. The result gives precise integral data for future calculations with the weighted exceptional configuration without claiming a degeneration theorem or an arithmetic application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
