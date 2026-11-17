---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The squarefree group algebra proof gives a_n²=binom(n,3)I and four residue-class multiplier forms e1+e3,e2+e3,e3,1+e1+e2+e3. Alternating-form normal form computes rank m_{e2}; n≡2 reduces e3=e1e2 to odd n-1 variables; n≡3 involution has ker(A-I) dimension 2^(n-1). Over any field of characteristic 2 same matrices of 0/1 so ranks and Jordan shape extend; Q-powered counts follow. Independent binary GF2 adjacency row reductions n=3..9 reproduce ranks [8,8,12,12,128,128,240] (relevant orders), consistent with statement.

## originality

FAIL

A public full prior theorem (2026-10-25) gives the identical d_H=3 F2 rank and full orbit/time census for all n>=3; it even includes both self-input choices. The current field F_{2^f} variant is mechanically implied via scalar extension: rank/Jordan identities invariant under field extension; configuration counts simply 2^d→Q^d. This is conclusive claim-vs-prior implication, regardless of title, arbitrary Q or slightly different rank normalization.

## value

FAIL

Natural modular Hamming adjacency ranks are valuable in principle, but THIS final claim provides no independently unknown classification: Oct25 prior proves full same infinite-family structural theorem, its rank data and more dynamical configurations. Replacing base-field size is a routine scalar-extension/count substitution, not a substantive new mathematical reason.

The dated certificate retains the supplied scientific assessment, sources and limitations.
