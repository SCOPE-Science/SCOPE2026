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

PASS: From amplitude/phase equations, the active-support Jacobian is [[0,-4 diag(sigma_j chi_j I_j)],[-V_S,-kappa I]], with characteristic det[lambda(lambda+kappa)I-4DV_S]. For V_S PSD, 4DV_S has the same characteristic polynomial as real symmetric 4 sqrt(V_S) D sqrt(V_S), including singular PSD, so mu is real. Nonzero lambda=i omega would give mu=-omega²+i kappa omega nonreal: impossible for any mixed phase signs and common kappa>0. For symmetric a,b>0 dimer b<=a is PSD. For every b>a, the constructive branch with epsilon=(b-a)/(2b), I_e=I(1-epsilon), I_o=I(1+epsilon) yields t<0,d>0 and a Routh-Hurwitz threshold kappa_c²=2 b chi I (3b+5a)/a, omega²=2a chi I(b-a)/b. Independent SymPy factored t²-2kappa_c² t-4d identically to zero and confirmed threshold, as well as supplied exact witness. The crossing is transverse, not a nonlinear cycle existence theorem.

## originality

PASS

PASS best-of-knowledge: Gómez–del Pino October 2026 derive related active-mode Jacobian and particular dimer Hopf conditions; the inspected abstract and source package attribution establish these inputs as prior. Distinct new theorem is PSD no-internal-Hopf for any N with mixed signs and converse realizability iff b>a for every positive symmetric dimer coupling ratio. No equivalent stronger matrix criterion located in Resultary search. The relevant Gómez–del Pino full arXiv paper could not be fetched, and authorized Oxford access reports VPN disconnected, so a priority risk is explicitly retained rather than asserted away.

## value

PASS

PASS: A uniform spectral-signature obstruction for every dimension and every active support is a structural bifurcation boundary, with a sharp converse that gives explicit physically admissible stationary parameter paths. It distinguishes indefinite nonlinear interactions from merely strongly driven PSD networks; not a routine numerical threshold for one example. It is restricted to internal spectral crossing under equal positive damping and says nothing by itself about nonlinear Hopf normal forms or dormant-mode instabilities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
