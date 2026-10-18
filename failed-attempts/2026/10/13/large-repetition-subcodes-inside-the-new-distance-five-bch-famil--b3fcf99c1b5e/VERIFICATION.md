---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For s>=2, n=(2^(2s)+1)(2^s-1), both cases of Wang--He--Yi--Zheng Lemma 6 supply a five-element support in one residue class mod r_s=n/5 or n/51. Since the BCH code is cyclic, its shifts by t=0,..,r_s-1 are all codewords with disjoint supports. They generate [5,1,5]_2 direct summands, hence W_R=(1+z^5)^r_s, A_5j(C)>=binom(r_s,j) and d_j(C)<=5j. Over GF(2), the two root sum identities were checked independently, including polynomial divisibility for the order-51 pattern and 58 finite arithmetical cases; infinite divisibility is algebraic. The code family, precise normalization and ambient lower bounds are mathematically sound.

## originality

FAIL

The complete closely relevant primary paper Wang--He--Yi--Zheng arXiv:2609.00532 Lemma 6 (pp6-8) explicitly supplies the EXACT five subgroup roots for the order-5 case and the EXACT order-51 exponent set {0,3,21,33,44}; Theorem 7 (pp8-9) makes a BCH codeword from them. By the pre-existing defining property of a cyclic code, translating that one word through the r_s distinct residue classes is mandatory, gives pairwise disjoint words immediately, and yields all claimed subcode enumeration and GHW inequalities by elementary independence. Thus the presented theorem is already entailed by the specifically published construction plus the standard definition, despite lacking matching subcode wording in the prior title/theorem; it does not pass O.

## value

FAIL

The macroscopic subcode and weight-spectrum implications are useful to know, but in this precise family every asserted numerical/structural component is an immediate textbook consequence of the exact prior published supported codeword and cyclicity, without a new optimization, classification or unknown bound. It is a routine corollary rather than a distinct motivated mathematical advance satisfying V as an independent finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
