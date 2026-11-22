---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS: Logistic comparison bounds prey x<=B. On E>=AD, g_+/q integrable through x=0 (g_+ vanishes near zero if E>AD, and g/q=D(x^p+C)/[M(x+A)] when E=AD). With Y*=2R(B^p+C)/M, y>=Y* forces xdot<=-qy/2 and d(log y+2∫_0^x g_+/q)/dt<=0; excursions give a uniform predator bound and forward globality including equality. On E<AD, δ=D-E/A>0 gives ydot>=δy² and finite terminal time, 1/y(t)=∫_t^Tg(x(s))ds. Since g<=D, y>=1/[D(T-t)]; logarithmic prey comparison gives x=O((T-t)^κ), κ=M/[D(B^p+C)]>0, so g(x)=δ+O(τ^κ) and y=1/(δτ)(1+O(τ^κ)). Then xdot/x=-ν/τ+O(1+τ^(κ-1)), ν=M/(Cδ), an integrable error; x/τ^ν→c in (0,infinity), and xdot~-νcτ^(ν-1). The limiting derivative trichotomy at ν<1,=1,>1 follows. Independently checked symbolic cancellation g/q at E=AD; no finite simulation used as general proof.

## originality

PASS

PASS best-of-knowledge: Earlier 2024 Patra–Maitra–Kundu material explicitly treats D>E/A as sufficient blow-up; the 2023 Srivastava group-defence paper describes blow-up/quenching for some data. Neither accessible theorem statement includes the converse E>=AD global uniform bound across all positive starts together with positive-amplitude power law and ν-derivative trichotomy. Some original 2024 full-body material was not lawfully retrievable, so possible broad equivalence is residual rather than a reason to automatically fail.

## value

PASS

PASS: the exact parameter-wide threshold resolves whether the printed undelayed ecological flow can blow up and distinguishes three mathematically different prey derivative behaviors. The sharp all-positive-data converse and boundary are useful structural results in a model with reported conflicting quenching simulations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
