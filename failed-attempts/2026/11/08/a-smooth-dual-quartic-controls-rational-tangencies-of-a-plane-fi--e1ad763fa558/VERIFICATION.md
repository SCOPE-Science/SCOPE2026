---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For each rational line L on the Asgarli–Ghioca degree q+3 plane-filling curve, restriction factors (s^q t-s t^q)Q_L with Q_L nonzero binary quadratic, so rational tangency contacts are its 0/1/2 roots. The determinant/adjugate identity for diag(c+kb,a,b) yields exactly Hk(a,b,c)=a^3b+b^3c+ac^3+k(b^4+abc^2). Thus N1=#Dk(Fq), and each rational smooth point has one rational tangent giving N0=N2=(q²+q+1-N1)/2. Under root-free T^7+kT^3-1, quartic smoothness and genus3 follow by the displayed singularity elimination; Hasse–Weil gives |N2-q²/2|≤3√q. Independent symbolic determinant check confirms the discriminant identity; stronger earlier complete result proves the same smoothness for all odd prime powers.

## originality

FAIL

FAIL decisive equivalence: The November 2 full published theorem studies the SAME Asgarli–Ghioca pencil and root-free f_k(T). It writes dual line UX+VY-WZ=0 and Δ(U,V,W)=UW³+V³W−kUVW²−kV⁴−U³V. Substituting U=a,V=b,W=−c gives Δ(a,b,−c)=−Hk(a,b,c); thus its quartic, all N_j counts, genus-three smoothness, and 3√q bound are identical. It proves the stronger geometric criterion quartic smooth iff f_k squarefree. The October 18 theorem already gives exactly Hk and exact tangent/bitangent line counts (its smoothness bound conditional). Nothing original remains in the present theorem.

## value

FAIL

FAIL the entire final mathematical assertion, including quartic geometry and sharp-order line counts, is a directly covered corollary of the November 2 published proof. A different singularity-elimination algebra for the same statement does not supply a separate motivated invariant or new boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
