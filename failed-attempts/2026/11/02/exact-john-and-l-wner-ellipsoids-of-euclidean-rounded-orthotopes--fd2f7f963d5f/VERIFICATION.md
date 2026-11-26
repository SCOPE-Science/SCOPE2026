---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The coordinate bound applies to every translated and rotated inner ellipsoid; Hadamard gives the volume and forces the diagonal centered shape at equality, which is attained by splitting each axial stretch between the box and ball. The feasible positive box corners are exactly those with sum of squared excesses above the half-lengths at most r^2. A maximizing corner is at least a coordinatewise and strict concavity of the log product gives the positive normalized solution v_i(a_i+r v_i)=c. Expanding the outer quadratic about v gives the claimed negative remainder: r/c-r^2/z_i^2 is strictly positive because z_i^2-rc=a_i z_i>0. This both gives enclosure and forces exactly the signed contacts. Sign averaging and AM–GM of the eigenvalues give the determinant lower bound for every enclosing shape and force q=0 and Q=d diag(z_i^2) at equality. At r→0 the outer corners converge to a; at r→∞ the products of v_i+a_i/r converge uniformly on the compact positive unit ball to the product of v_i, with unique maximizer v_i=1/sqrt(d). The ratio limits follow. The analytical proof, not the finite optimizer checks, is decisive.

## originality

FAIL

The earlier coaxial box–ellipsoid theorem explicitly includes the Euclidean rounded box, gives the same unrestricted Löwner semiaxes, entire contact set and volume, and uses the same containment certificate under substitution. The John calculation is not stated there, but the main novelty distinction in the frozen record (an exact unrestricted Löwner/contact classification not already covered by a broader theorem) fails. The outer-corner maximum follows from that certificate, and the remaining volume statements are elementary consequences with the inner ellipsoid.

## value

FAIL

An unrestricted exact outer contact classification would be useful, but that information is already available in equal or greater generality. Removing it leaves an immediate Hadamard bound saturated by the explicit coordinatewise dilation, plus routine volume arithmetic and limits using the known outer formula. No independent substantive remainder supports a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
