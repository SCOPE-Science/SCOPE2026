---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Goursat parametrizes additive subgroups of Z/p^n x Z/p^m uniquely as (a,b,c,t), 0<=c<=min(n-a,m-b), t unit mod p^c (c=0 trivial). Subbrace multiplicative closure reduces via generator products to p^(k+a)t≡p^(ell+b) mod p^c; ideal absorption by ambient (1,0),(0,1) reduces to c<=min(k,ell). Summing phi(p^c) units gives S=Σ[p^s+1_(k+a=ell+b) p^(k+a) max(0,M-k-a)] and I=Σp^min(M,k,ell), with M=min(n-a,m-b),s=min(M,k+a,ell+b). Dedekind iff k>ell,m=ell+1 or ell>k,n=k+1, using explicit nonideals otherwise. Independently generated all additive subgroups and tested ring/ideal closure in multiple small prime-power products (p=2,3), reproducing (18,18), other contrasts. Algebraic proof covers all p,n,m,k,ell in stated domain; C PASS.

## originality

PASS

Earlier general Dedekind skew-brace and Hamiltonian-ring theory gives qualitative structural criteria but no inspected exact Goursat-weighted all-subbrace and all-ideal total formulas for the full rank-two cyclic radical-ring product family. Kruse–Price 1969 primary text gives mod-p subring/ideal-count congruences and uniqueness-by-order classifications; those do not imply the precise integer totals. The 1968 Kruse H-ring full text remains inaccessible under a disconnected institutional VPN and this creates a named risk, not an automatic originality failure. O PASS best of knowledge for exact quantitative distribution, not for the qualitative Dedekind concept.

## value

PASS

A natural first product of individually Dedekind cyclic nilpotent radical rings can fail to have all subbraces ideals; the exact census S,I and sharp positive defect S-I give a useful structural quantitative refinement for a whole infinite family with phase boundary. Goursat parametrization makes the count reproducible and transferable to other rank-two brace lattices. Neither correctness nor code alone is the value basis. V PASS.

The dated certificate retains the supplied scientific assessment, sources and limitations.
