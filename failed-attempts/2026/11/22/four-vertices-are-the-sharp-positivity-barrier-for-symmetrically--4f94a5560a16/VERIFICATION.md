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

FAIL

The stated all-step contraction equivalence for every nonempty graph is false if nonempty means having a vertex, as allowed by the stated connected graph scope: on the one-vertex graph L=0 and M=I even for s<1/4. The equivalence holds precisely on the nonzero-Laplacian class: the spectral decrement is (2/s)x/(1+x)^2, attaining 1/(2s) when h=2/(s lambda) for any positive eigenvalue lambda. The principal positivity claim itself checks out. Independently differentiating the path resolvent from tridiagonal continuants (H_z=-z d[(I+zL)^(-1)]/dz) reproduces all off-diagonal classes on P2, P3 and P4; K3 follows from L=3(I-P_constants), and the singleton is immediate. The only off-diagonal sign change on P4 has numerator z(z+1)(2z^3-6z^2-5z-1), with one positive zero 3.7101505426193419…; spectral calculus gives H_z,ii<=1/4 and therefore nonnegative diagonals for s>=1/2. The strict negativity beyond the cutoff follows for all s>0, without claiming sufficiency below it when s<1/2. The frozen script was inspected, not executed; the independent continuant replay is /tmp/opencode/frozen-review-replay.py, function graph_filter, and supplements the analytic sign argument.

## originality

FAIL

A distinct Resultary finding gives exactly the matched-splitting minimality and sign classification, and that statement mechanically implies the claimed variable-s positivity classification. This is a finding of equivalent coverage, not a finding of historical priority from a common posting date. The edge-bearing spectral threshold is a scalar rescaling of the matched-splitting spectral bound and can also be read off the already published scheme; it does not supply a distinct surviving claim.

## value

FAIL

The sharp small-graph separation of maximum-principle preservation from energy contraction is meaningful, but that separation and its exact threshold are already in the matched-splitting record. The purported added variable s only rescales off-diagonals at a rescaled time, and the remaining diagonal and spectral bounds are elementary consequences of the same formula. No distinct worthwhile remainder is established; a wording correction for L=0 would not rescue this.

The dated certificate retains the supplied scientific assessment, sources and limitations.
