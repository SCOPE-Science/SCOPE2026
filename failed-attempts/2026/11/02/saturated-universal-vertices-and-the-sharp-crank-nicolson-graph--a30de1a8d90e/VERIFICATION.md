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

For s=h/2, the positive resolvent gives C(2s)=2(I+sL)^{-1}-I, and each resolvent diagonal strictly decreases from 1 to 1/N. For D=c(NI-J)-L, D is positive semidefinite and D1=0. On the zero-sum subspace the resolvent is (αI−sD)^{-1}, α=1+sNc. Expanding in the eigenbasis of D bounds it from below by α^{-1}I+sα^{-2}D, with equality on the projection of e_i exactly when De_i=0 (s>0). This proves the cap bound, the saturated-universal criterion, and the reserve. The frozen proof does not actually justify optimality of the coefficient: remove conductance ε on one edge of the saturated complete graph. At either endpoint C(h_0)_{ii}/ε=2s_0/[α(α−2s_0ε)] tends to the claimed coefficient as ε↓0, for every allowed N and c. For a part of size b, the projector weights 1/N, 1/b−1/N, 1−1/b give a return diagonal exceeding the singleton diagonal by (b−1)x/[(1+Nx)(1+(N−b)x)] for x=sc>0; this increases strictly with b. Its 1/2 crossing is the stated positive quadratic root. This verifies the finite horizon, strictness, optimizer statements and N=2 exception. The star example refers to c=1 for a unit-weight star (or spokes all c after scaling). The attached rational checker was inspected; it is finite evidence and does not test the optimal coefficient.

## originality

FAIL

The earlier unweighted result gives the very same comparison, equality criterion and neighbor-edge invariance with a proof using only a positive-semidefinite deficit Laplacian. Its proof transfers without a new step to the pairwise cap. The stated linear reserve is the tangent estimate from that same published resolvent interpolation; its optimal coefficient is the first derivative for a one-edge deficit. The complete-multipartite package also has exact coverage in a distinct same-day finding, via B=c|E|, including the minimum-part endpoint and strict monotonicity. Day-level dates do not establish priority for this overlap. The decisive issue is mathematical coverage and routine implication, not the access limits of the literature search.

## value

FAIL

Identifying sharp positivity thresholds is useful, but the multipartite family already has the exact relevant threshold law. The rest changes the missing-edge weights in the known complement comparison and retains its first-order tangent. There is no sufficiently substantive untouched result in the frozen claim to justify a repaired acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
