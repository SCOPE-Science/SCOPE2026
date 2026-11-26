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

Legendre's formula gives (p-1)W_p(n)=2S_p(n)-(n-1)s_p(n). Splitting at p^L gives the displayed exact difference, with all terms except (a+1)s_p(t) divisible by p^L after multiplication by p-1. The alternate carry formula can be checked by counting, for each m=p^h, those j for which j mod m exceeds n mod m in each complete block; it gives W_p(n) divisible by p^j whenever n+1 is. On aligned p^i-blocks the digit-sum character bound is |1+zeta+...+zeta^(p-1)|^i. Choosing a common upper bound strictly between max(1,max_zeta |1+...+zeta^(p-1)|) and p, then summing over the at most p-1 blocks per scale in a prefix, gives a power saving for arbitrary cutoffs. For j<k, the linear coefficient in the compressed congruence has exact valuation j, so the conditional law is uniform on p^j multiples; j>=k forces zero. Each j<k contributes (p-1)/p^(k+1) per permissible residue, and the last stratum adds p^(-k) at zero. The histogram is the generating-function count of tail digit sums, including r=k; one free digit already gives exact uniformity modulo p. For L>=1, setting a=0 gives a remainder coefficient congruent to -(L+1) at t=1 and to -L at t=p+1, so some remainder has valuation exactly L. At L=0 the witness a=0,t=1 works for every k>=1 since W_p(1)=0 and (p-1)^(-1) is a unit. Independent Legendre-valuation enumeration supplied 1,406 bounded checks at p=2,3,5 (blocks up to 2,000 indices); replay: /workspace/branches/3e039027-151e-40e3-bbc6-20471bee4a29/replay.py and replay-output.txt in that directory. The finite replay does not establish the natural density or the uniform quantifiers.

## originality

PASS

The pointwise valuations of the full row product (equivalently the reciprocal unreduced Farey product) are known. The supported increment is the sharp low-digit compression together with the exact conditional and unconditional all-precision natural laws and finite histograms. The subset of these claims equivalent to older pointwise formulas is not counted as original.

## value

PASS

The valuation of a full Pascal row product is a natural aggregate rather than a selected binomial coefficient. Its nonuniform law is explained by the valuation strata of n+1, and the sharp split depth gives an exact finite counting procedure at arbitrary output precision. These give distinct usable information on the whole sequence beyond the known term formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
