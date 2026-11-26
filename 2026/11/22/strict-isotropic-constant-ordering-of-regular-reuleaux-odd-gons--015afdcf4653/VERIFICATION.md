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

Scaling reduces to width one. For an odd regular n-gon, the maximally separated vertices subtend π−π/n, so its circumradius is R=1/(2 cos b), b=π/(2n). The unit circular arc opposite each vertex is centered there, with half-angle b. The arc flux is 1−R cos u and the squared radius factor is R²+1−2R cos u. The Green integrals, with factors n/2 and n/4 respectively, give the stated A and I by elementary integration. Rotational symmetry forces L²=I/(2A²), so 4πL²=H(b). In `python3 /workspace/checks/independent_01_05.py` (check 5) I independently differentiated H and checked D³H′=b²P, obtained x_8 from formal division of sine by cosine, recomputed the degree-42 rational polynomial and its exact negative-tail bound, and recovered the H series. On 0<b≤π/6 convexity of tangent gives 1≤x≤2√3/π<7/6 and 0<z=b²<1/3. The tangent ODE inductively bounds a_k≤2^(−k); hence 1≤x_8≤x and x−x_8≤(3/1280)z⁹. Termwise differentiation bounds |P_x| by (13+22M)+(16+8M+48M²+4M³)/3+(48M²+24M³+5M⁴)/9<90 at M=7/6. The coefficient and tangent-tail losses are <1/1000 and <1/100 respectively after division by z², against the leading 64/45. Thus H′>0 on the stated continuum, and H(0)=1 gives strict comparison to the disk. The n^(−4) coefficient is π³/180 and n^(−4)−(n+2)^(−4)=8n^(−5)+O(n^(−6)), proving the gap and exact identification at any width. The frozen PASS is recorded, not rerun; the exact replay and analytic bounds do not infer an infinite statement from sampled orders.

## originality

PASS

The supported distinct content is strict all-order monotonicity, proved by a continuum comparison. The individual formulas and quartic disk defect are prior-covered; the leading adjacent-gap law follows from the prior defect with its remainder (or the analytic formula), and is not credited as a second independent originality claim.

## value

PASS

The all-order strict comparison classifies a canonical constant-width family by a single affine invariant and makes exact order identification independent of width. The small gaps quantify why identification near the disk is sensitive. The continuum sign resolves the low and intermediate orders which the known asymptotic alone cannot settle; no optimization over irregular shapes is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
