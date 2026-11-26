---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The change of variable from age to a fraction of the flight gives zero centered reward on each whole flight for every bounded measurable spatial observable. The absolutely continuous primitive vanishes at both ends of each flight, proving the pathwise identity even across reset jumps. Equilibrium sampling length-biases the duration and makes the age fraction independent uniform. To verify endpoint decorrelation directly, condition on the initial flight and time of the first future renewal. For a bounded continuous test function of the primitive, the ordinary-renewal kernel at age a is E[psi(T H_g(a/T)) 1_{T>a}]; it is continuous by the duration density and dominated by a constant times the integrable decreasing duration tail, hence directly Riemann integrable. The nonarithmetic key renewal theorem and bounded convergence give the independent equilibrium endpoints. Uniform L2 truncation is valid by E[(T*)²]=ET³/ET, giving the stated coefficient. Near-zero covariance is positive by stochastic continuity at a fixed stationary time and Var(g)>0 for nonconstant Lipschitz g; nonnegative covariance at all positive lags would force at least linear growth of integrated variance. For normalized position H=u(1-u)/2 gives moments 1/12 and 1/120 and the exponential coefficient 2/(45 lambda²); Cramér's theorem excludes a Gaussian difference of the nondegenerate nonnegative endpoint variables. The inspected check.py is a finite numerical diagnostic, not evidence for the asymptotic theorem, and was not executed.

## originality

FAIL

A distinct directly inspected catalogue record (87b32b051bde) establishes the same main theorem in equivalent notation, including the normalized-position and exponential specializations after dividing by L². It adds stronger moment results. This is statement-level coverage, not a claim about within-day priority. The negative-lag statement is not seen verbatim in the overlapping finding, but is an immediate consequence of its bounded integrated variance and positive continuous-at-zero covariance; it does not rescue the original finding.

## value

FAIL

The exact occupation law would address a natural fluctuation question, but it is already supplied by the materially overlapping record. The remaining qualitative sign statement gives no lag, scale or signed-correlation law and follows routinely from bounded integrated variance and positive near-zero covariance. Repackaging that corollary alone does not provide a distinct valuable finding under the required standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
