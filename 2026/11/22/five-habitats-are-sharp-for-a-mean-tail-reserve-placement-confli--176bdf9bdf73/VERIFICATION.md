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

Let P be the two-state matrix with diagonal q and off-diagonal r=1-q. Summing the periodic weights gives tr(P^n)=1+(2q-1)^n>0; overwriting reserve states leaves the original marginal law of all ordinary sites. For n=5 each ordinary site in the separated layout is adjacent to a reserve, so fair spin marginals give mean 7/2. For adjacent reserves the only functional site that can be stranded is the middle of the three ordinary sites, exactly at pattern 010. Summing over the two overwritten sites gives unnormalized weight r^2(P^3)_{00}=q r^2(4q^2-6q+3), strictly positive. Full access means all ordinary sites were functional. The adjacent and separated layouts have unnormalized weights q^2(P^3)_{11} and q((P^2)_{11})^2 from cyclic gaps (1,1,3) and (1,2,2). Their difference is q r^2(q^2-r^2)=q r^2(2q-1). This yields the exact probability gap, the equality case, and the reported example at q=3/4 without relying on the source enumeration. At n=4 every ordinary site is adjacent to some reserve for either layout, giving mean 3 by the fair marginals; at n=3 there is only one layout orbit. Strict placement claims are modulo dihedral symmetry.

## originality

PASS

The independent cycling-refuge theorem already covers spacing and accessible-habitat tails under independence, and Albers et al. already exhibit an adjacency advantage for joint success under a correlated risk model even with equal mean survival. Neither covers the strict mean-versus-full-access conflict, its exact sign boundary, and the minimal cycle size under the stated periodic Ising intervention. The pass is limited to that specific distinct mathematical claim.

## value

PASS

The exact smallest witness shows that optimizing average accessibility can oppose maximizing full accessibility as soon as positive coupling is introduced, even though the independent full-access criterion is indifferent. The two objectives and the change of dependence regime are motivated by independent-cycle and correlated-reserve work. The exact sign change and exclusion of smaller cycles make this useful as a benchmark for placement rules, without pretending a five-site model calibrates a real reserve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
