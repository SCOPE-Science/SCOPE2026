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

A successful visit to corridor patch j spends ℓ≥1 seasons there with path weight (qA_j)^(ℓ−1) q b_j; the target contributes the success sum (1−q)∑(s₀q)^ℓ for ℓ≥0. Multiplication applies because advances are ordered and renew the process. These series converge at both endpoints under the hypotheses, with H_n(0)=H_n(1)=0. The derivative of log H_n has the sign of the left side of (1) minus 1−s₀. Each summand of that left side is a product of (1−q)/(1−A_jq) and 1/q−s₀, both strictly decreasing and positive on the interior, with the full sum falling from infinity to zero. Appending a positive summand moves the unique root strictly right. A different policy at each site maximizes the passage factors by q=1 and the target factor by q=0, yielding the strict cue benchmark. To check the long-corridor law, for fixed q<1 the stationarity sum is bounded below by n(1−q)(1−s₀q)/q, so its unique solution tends to 1. For δ=1−q_n the sum of reciprocals of 1−A_j+A_jδ is K_n(1+O(δ/ε)), uniformly in n; the stationarity equation then gives δK_n→1 and δ=O(1/n) since n≤K_n≤n/ε. Alternatively, conditional on successful passage under the cue policy the patch residence seasons are independent geometric variables with means 1/(1−A_j). The dormancy penalty in the chain is their summed-time generating function at q_n. The log error relative to −δK_n is O(nδ²/ε²) from the series of log(1−δ) and log(1+A_jδ/(1−A_j)), so the passage penalty tends to e^−1. The target factor is asymptotic to δ/(1−s₀). At s₀=1 the conditional target success is one for q<1 and zero for q=1, giving a supremum but no maximum, as claimed. The five-patch equation reduces to 123q²−288q+160=0 with the stated smaller root in (0,1); finite checks in the inspected but unexecuted uploaded script are not needed for the proof.

## originality

PASS

The classical waiting-time passage identity and conceptual dormancy/dispersal tradeoff are not new. On the sources actually examined, the finite optimizer and strict append response combined with the sharp heterogeneous cue-relative asymptotic distinguish the frozen claim. This is a best-of-knowledge decision with explicitly bounded access, not historical certification.

## value

PASS

The sharp extra 1/K_n loss quantifies a natural restriction on using one germination probability across distinct habitat states, in a setting where absolute success can already decay exponentially. The heterogeneous optimizer and its strict response to added distance go beyond a homogeneous geometric-sum example. This is a clean idealized single-seed benchmark, not field calibration, population fitness or deployment advice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
