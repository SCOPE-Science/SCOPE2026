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

The sequence probability is exchangeable and the distinguished color's occupancy is beta-binomial. Conditional on that color's count r, its positions are uniform and the others, in order, have the (q-1)-color symmetric urn law. For any adjacent pair the conditional change probability splits into exactly one distinguished position and two others; multiplying by n-1 gives the two terms of (6). Subtraction of the unconditional (n-1)d_q and symmetry give (1), also when n-r is 0 or 1 or q=2. Independently, conditioning on the complete occupancy vector yields E[R_n|N]=(n^2-sum_j N_j^2)/n, and the second factorial moments of the remaining occupancies give the same expression. Writing D=qa+1, E=(q-1)a+1, the leading coefficient b-d is -a(a+1)/(DE); F(r) is strictly negative for r>=2 while F(qr)=r(a+r)(q-1)(qa+2)/(DE)>0. Concavity and the negative limit at infinity prove the ordered roots and exact integer classification. For r=1, F(n)=(n-1)(a+1)/E times (2-na/D). For r large, scaling x=tr gives limiting quadratic -(d-b)t^2+2(1-b)t-(2-b) with an affine O(1/r) correction. Its center is D/a and squared half-width is DE/[a^2(a+1)], verifying (3); strict signs at 1,q and infinity ensure simple roots and the O(1) location error in n. Direct sequential-weight enumeration at q=4,a=2/3,n=2..6 independently agreed for all 20 frequencies, within 6e-16 in the covariance.

## originality

PASS

The most relevant primary run laws encompass the sampling model and the joint run data but do not evaluate the relevant mixed moment or sign regime. The indexed collision and urn sign results change the distribution or at least one random variable. The exact covariance and finite-concentration two-reversal theorem with its singleton and large-frequency boundaries are supported as distinct relative to the inspected sources, not certified historical firsts.

## value

PASS

The theorem describes how temporal diversity and rare observed occupancies associate across sample sizes in a canonical reinforcement model. The global reversal and placement of the positive interval around the exact integer qr, with a qualitatively different singleton case, are information not visible from an unevaluated joint law or a few enumerated parameters. The threshold constants quantify this separation beyond the finite examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
