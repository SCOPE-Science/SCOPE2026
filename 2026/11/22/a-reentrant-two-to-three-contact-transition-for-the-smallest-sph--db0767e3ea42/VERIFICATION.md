---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Strong convexity and coercivity give a unique center; the half-turn about the x-axis interchanges t and −t, so the center lies on that axis. The decisive continuum reduction also has a direct proof. For 0<t<L set λ=(1−cos t)/(1−cos L); then d_x(t)^2=(1−λ)d_x(0)^2+λd_x(L)^2+η²(t²−λL²), where d_x is distance to (x,0,0). Since sin(t/2)/(t/2)>sin(L/2)/(L/2), the last term is strictly negative for η>0. Thus the three samples −L,0,L control the entire ball and there cannot be additional contacts. This also handles the decreasing-throughout case for negative x omitted from the prose list in Proof Step 2; the maximizer conclusion there is correct. The two quadratics intersect at v=−k/[2(1−c)]; to the left the center-sample quadratic is active and strictly decreasing, and to the right the endpoint quadratic minimizes at max(c,v). This recovers both radii and the endpoint-only versus three-contact cases, with three curve contacts at equality even though the endpoints alone certify the ball. For c<0 the criterion is η²≤q(L). The derivative of log q strictly decreases from +infinity to −2/π by the displayed second derivative, q starts at zero and q(π)=4/π², giving the peak, the exact lower and upper crossing rules, the one-point tangency, and the L=π boundary at η=2/π. At fixed L>π/2 the pieces share first derivative 1/[2(1−c)] and have unequal second derivatives 0 and −1/[4(1−c)^3]. Independent high-precision root illustrations (`python3 /workspace/checks/helix.py`, mpmath) give L_*≈2.670778089087041, η_*≈0.6874374448319006 and 2.309578751557750, 3.071208826768052 for η=0.65. The root computation is illustrative; uniqueness and all-span claims follow from the analytic inequalities. The frozen checker was read, not run.

## originality

PASS

Qualified for the exact continuous-arc enclosure and its contacts. The same-day acute-triangle record already evaluates the identical q(L) on the symmetric slice, its maximum and the associated critical pitch; those are shared calculations, not a separate originality credit. The distinct assertion is that the finite symmetric triple actually determines the optimal ball of the entire continuous arc, and determines all its contacts. Neither the triangle-angle optimization nor the full-turn diameter result establishes that containment assertion. No priority ordering within the shared date is inferred.

## value

PASS

The canonical positive-pitch circular helix is a natural nonplanar test for Euclidean containment. A future calculation can enclose a full continuum and know exactly which samples are boundary contacts without optimizing over a mesh or trusting a diameter approximation. Even with the symmetric triple's angle boundary known, transferring it to the true arc minimum ball is meaningful: for nested arcs at a fixed pitch the third contact can appear and later cease to be on the ball, and the true radius is C¹ but not C² in k across contact creation. This is limited to total span at most one turn and positive pitch.

The dated certificate retains the supplied scientific assessment, sources and limitations.
