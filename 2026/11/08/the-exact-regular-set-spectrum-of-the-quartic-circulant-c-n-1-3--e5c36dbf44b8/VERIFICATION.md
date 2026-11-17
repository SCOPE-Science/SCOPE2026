---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The binary membership vector satisfies A x=b1+(a-b)x with mean b/(4-a+b); after mean removal every nontrivial root of unity frequency obeys P_lambda(z)=z^6+z^4+z²+1-lambda z³. Exact cyclotomic orders are lambda=-4:2; -1:5,6; 0:4,8; 1:3,10. Binary separability of sums of coprime-period components plus integral density eliminates mixed 5/6 and 3/10 alternatives. For lambda=0, period 8 or 4 follows; direct residue-neighbor counts give the exhaustive formula 2[2|n]+6[3|n]+30[5|n]+68[8|n]+4[n≡4 mod8]. Independently enumerated all labelled proper subsets for n=7..18 and matched each (a,b) count; T(120)=106 and the bound/equality follow from divisibility without relying on a finite n cutoff.

## originality

PASS

The primary all-quartic-circulant classification by Abdollahi et al gives existence of parameters and explicit solutions but the accessible evidence does not show a full labelled multiplicity census or exact 106 maximum for C_n(1,3). Special efficient domination and (0,4)-regular facts are acknowledged as prior and not claimed new. Resultary searches located no different earlier matching all-parameter enumerator. This is best-of-knowledge PASS with explicit residual risk: the highly relevant updated original paper and Kwon–Sohn–Chen 2020 were not inspected in complete primary text; authorized download stopped at VPN disconnect, not retried or bypassed.

## value

PASS

For a natural connected 4-regular circulant, the theorem turns yes/no existence into a complete labelled periodic-configuration classification and a uniform sharp finite ceiling 106 attained on exactly a modular family. Those precise multiplicities and rigidity are meaningful mathematical refinements for regular/equitable vertex sets, not arbitrary tiny slices or known-table arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
