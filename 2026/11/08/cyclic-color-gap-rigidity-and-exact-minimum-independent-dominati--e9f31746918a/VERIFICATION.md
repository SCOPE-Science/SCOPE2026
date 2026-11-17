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

For the categorical (not Cartesian) product C_n x K_q, n>=6,q>=3, every three consecutive layers contain at least two selected vertices in an independent dominating set. Summing yields |S|>=ceil(2n/3); explicit k=floor(n/3) empty layers alternating with monochromatic runs achieves this. A partial occupied layer of size 2,..,q-1 contradicts adjacent domination; a full q-vertex layer forces three local excesses >=1, contradicting total excess <=2. Thus all occupied layers in minimum sets are singletons, organized into k positive monochromatic runs of sizes 2+e_i, sum e_i=r. Neighboring run colors must differ. Cyclic compositions count n/k binom(k+r-1,r); proper color cycle contributes (q-1)^k+(-1)^k(q-1), with k=2 specifically checked. Independent graph-based exhaustive subset enumeration n=6,7,8 q=3 reproduced 18,42,72 minima, while unrestricted proof is combinatorial.

## originality

PASS

Kuenzel and Rall (2022) establish the scalar independent domination number for these products and a general weak-partition description of maximal independent sets; these are explicitly known. Their inspected Section 3 does not provide the exact cardinality-minimal class rigidity, labelled count or cyclic color-gap enumeration. The 2026-11-02 related Resultary polynomial treats P_n x K_q (path), not cyclic C_n x K_q. The remaining exact optimizer classification and count are best-of-knowledge new.

## value

PASS

A natural infinite family of highly symmetric direct-product graphs has an exact minimum-set classification, including the strong monochromatic-gap rigidity and an explicit exponential-color multiplicity with sharp n mod 3 geometry. This is useful finite graph-enumeration data not recoverable from the scalar independent-domination number alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
