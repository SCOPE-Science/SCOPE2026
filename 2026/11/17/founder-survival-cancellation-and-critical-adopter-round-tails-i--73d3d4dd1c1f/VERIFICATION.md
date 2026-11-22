---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For fixed r and each fixed round horizon the integrated-exposure direct-adoption probability expands as p f_nu(tau) (rho Theta/N)+O(N^-2 Theta^2), so conditional Poisson splitting with surviving parents gives offspring Z=1{E>=tau}+Poisson(c min(E,tau)) with *dependent* survival/contact via common E. Its PGF G(s)=lambda(1-e^{-[lambda+c(1-s)]tau})/[lambda+c(1-s)]+s e^{-[lambda+c(1-s)]tau}. I independently symbolically substituted s=lambda/c and simplified G(s)-s=0, computed G'(1)=1+kappa(c/lambda-1) and G''(1)|c=lambda=2kappa. Strictly convex PGF gives q=min(1,lambda/c). For each fixed K, from 1..K-1 adopters a next-round-extinction probability bounded below by kappa^(K-1)exp(-2rho K tau), giving a uniform geometric stopping tail and passage from finite-horizon convergence to K-first-passage law. Then K increases. At criticality the offspring span is one and finite variance 2kappa; Dwass cyclic identity plus aperiodic local CLT gives n^-3/2/(2sqrt(pi kappa)) and n^-1/2/sqrt(pi kappa). No fixed-N eternal survival or macroscopic-outbreak assertion.

## originality

PASS

Classical Galton–Watson, branching epidemic approximation, and Dwass local-CLT tail are standard. The potentially novel content is their exact conditional correlation law from a named four-compartment synchronous exposure model, the unexpected cancellation q=lambda/c, and a uniform fixed-K finite-population first-passage limit with explicit kappa critical coefficient. The source deterministic R and finite-N extinction do not by themselves imply the probability formula; full primary text remained incompletely accessible, so the priority is best-of-knowledge.

## value

PASS

A founder-count establishment law and a sharp critical occupation distribution for a model with explicit correlation between parent persistence and contacts are mathematically natural, quantitatively informative stochastic refinements of the deterministic epidemic threshold. They distinguish extinction of finite populations from the two-stage threshold event, with a nontrivial exactly simplified probability and kappa-dependent tail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
