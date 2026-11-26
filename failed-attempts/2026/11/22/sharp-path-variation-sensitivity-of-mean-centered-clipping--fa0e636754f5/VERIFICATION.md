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

On a chamber a row is either e_i or the arithmetic-mean row P_i; these maps carry constants to constants. A step after j has mean μ=(n−j)/n, has response in [0,μ] to the left and [μ,1] to the right, and thus has output TV at most (j−1)μ+1+(n−j−1)(1−μ)=2j(n−j)/n. The unit steps give the ℓ1 basis of adjacent differences. Line integration across the finitely many affine chambers transfers the bound to arbitrary pairs, also on chamber boundaries by continuity. Alternation on each side, with both bridge sites active, makes every edge bound tight. I checked strict feasibility: zero deviations for all active sites and suitably balanced ± exterior deviations when there are at least two saturated sites; with one saturated site take 3τ/2 at that site and −3τ/(2(n−1)) at the others (n≥3); an all-active cell gives factor 1 for n=2. Thus the mathematical claim, including attainment at every fixed τ>0, is true. Single-input TV uses scalar clipping at a common fixed center for each signal. I inspected the rational checker, not rerun it.

## originality

FAIL

The earlier mean-centered rectification result supplies the exact gain and attained checkerboard mechanism on a larger graph class. Despite the superficially different scalar maps, they have the same relevant affine-mask norms on the path. For each active subset with 0<|A|<n, rectification realizes the rows e_i on A and P_i off A (up to subtracting a common mean from every output) by taking positive centered deviations on A and negative deviations off A, summing to zero. For n≥3, clipping realizes every such mask at every τ>0: if the inactive count c≥2, take zero on A, 2τ(c−1) at one inactive site and −2τ at all the other inactive sites; if c=1 use the configuration in correctness. The remaining masks for clipping have norms 1 (identity) and 0 (constant output). The local maximum over affine pieces is the exact global gain, and a strictly realizable affine mask attains its norm by a sufficiently small step. Thus the sharp clipping formula and its attainment follow directly from the earlier rectification theorem by identifying the relevant mask families; n=2 is the immediate identity-boundary case. This is an established implication from the inspected prior statement, not a failure based on missing full text or a claim that the two maps are identical.

## value

FAIL

The operation is natural and exact worst-case constants are useful, but here the stated contribution is the same attained bridge-cut norm of an already analyzed family of local matrices, made explicit by a short mask realization. No independently useful additional sharp inequality or classification survives the comparison in this frozen claim. No repair was submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
