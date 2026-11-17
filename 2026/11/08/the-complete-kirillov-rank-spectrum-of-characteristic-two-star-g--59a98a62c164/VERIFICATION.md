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

PASS: The defining star class-three brackets yield a Kirillov block matrix with zero central rows and off-diagonal augmented m x (m+1) block T=[-alpha | B], B symmetric zero diagonal (alternating in characteristic two). Rank Kirillov=2 rank T; free functional coordinates on c and x_i contribute q^(m+1). The standard exact finite-field count of rank-2k alternating matrices is H_m,k=[m choose 2k]_q q^(k(k-1)) product_{j=1}^k(q^(2j-1)-1), obtained by radical selection and GL(2k,q)/Sp(2k,q). For such B precisely q^(2k) alpha vectors lie in its image, giving rank 4k; the other q^m-q^(2k) give rank 4k+2. Sum yields entire displayed P_mq and sum at t=1 equals q^dimL. Full maximal 2m rank is attainable for both parities of m, hence index 1+binom(m,2). Independent exact F2 counts m=2:(0:8,2:24,4:32), m=3:(0:16,2:112,4:448,6:448), and bounded larger m matched. General finite-field proof is analytical, not extrapolated.

## originality

PASS

PASS (best knowledge): Gallo–Videla primary full text defines precisely the three-step graph Lie algebra and gives dimensions/centers, not its entire coadjoint Kirillov rank distribution. Published K_{a,b} three-step index theorem explicitly requires a,b>=2 and excludes star a=1; even if its index limit were inferred, it does not provide the full rank multiplicities. Classical alternating-form rank distribution and GL/Sp counts are credited. No checked earlier source gives the added-covector star Kirillov rank polynomial over every q of characteristic two.

## value

PASS

PASS: The complete rank law counts all coadjoint stabilizer dimensions in a natural nilpotent graph Lie family, refining a single generic index to every stratum and measuring finite-field representation geometry. Its Gaussian-binomial weighted distribution is an exact natural invariant not reduced to an isolated tiny example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
