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

For the host 0101... of length m+t, greedily embed each binary output v of length m. The final minimum index is m-1+c(v), where c(v)=v_1+sum of equality indicators between adjacent bits. Thus v is a distinct length-m deletion descendant iff c(v)≤t. The map v↔(first bit,equality flags) is invertible over F2 and yields the known unweighted Hamming-ball count. Weight u per one and z per unit cost gives the exact two-state transfer polynomial P_m=(1,uz) [[z,u],[1,uz]]^(m-1)(1,1)^T, with recurrence P_m=z(1+u)P_(m-1)+u(1-z²)P_(m-2), and summing costs ≤t gives the claimed rational generating function (1+s-sh)/((1-h)(1-sh(1+u)-s²u(1-h²))). Run-composition minimization proves the exact weight support t≥max(0,m-2k-1,2k-m) and saturation threshold t=m-1 except for the all-ones word, which needs t=m. Complement pairing changes c by one, and counting odd r=m-t runs proves the explicit signed imbalance (m-2k)/a *binom(m-k-1,a-1)*binom(k-1,a-1), with correct one-run, even-run and end cases. Independently compared direct output sets for 546 (n,m,k) cells, including all corresponding parity cases. These are finite corroborations of an unrestricted bijective proof.

## originality

PASS

Earlier Flaxman–Harrow–Sorkin proves maximal unweighted distinct-subsequence enumeration for alternating words and provides a length-unweighted rational enumeration, which is explicitly excluded from novelty. The submitted composition-refined trivariate generating function, exact k-weight support and signed complementary weight bias are not implied by summing over k. Related alternate-host deletion residue/complement results constrain outputs to a prescribed alternating subsequence and different block words. No full-text published result inspected here supplies the identical fixed-composition distribution or parity law; originality remains qualified.

## value

PASS

For a canonical extremal source in deletion/subsequence combinatorics, the exact distribution of distinct outputs by composition is a natural strengthening of the known total count. A sharp first-appearance threshold for each weight and explicit parity-sensitive imbalance can matter to constant-composition deletion channels and combinatorial enumeration. The result is a self-contained all-parameter structural enumeration rather than a trivial table or a restatement of the total formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
