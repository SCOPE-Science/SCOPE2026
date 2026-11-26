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

On four consecutive sites the two distinct noncrossing local pairings must occur in opposite upper and lower positions to produce one component, giving exactly two choices; the two-site component has one choice. Distinct marked components have disjoint supports. For k=r+s labeled windows, ordering the blocks and putting 2n−2r−4s unused sites in k+1 gaps gives k! times binomial(2n−r−3s,k), the stated falling factorial. Removing all marked vertices in both halves is bijective: arcs of the remaining matching can enclose an inserted block but cannot interlace an arc wholly within that block. This gives the squared Catalan ratio, includes empty gaps and the case of zero remaining sites, and confirms the inadmissible moments vanish. At (1,0), (0,1), (1,1), the identity and C_{n−1}/C_n=(n+1)/(2(2n−1)) give the displayed means and covariance. For n≥3 the cubic shifted by n=m+3 is 10m³+49m²+56m+8. For k≤K sqrt(n), the log Catalan ratio differs from −(r+2s)log 4 by O((r+2s+1)/n), and expanding each log in the falling factorial has remainder O((k+1)^3/n²). Substituting k=r+s leaves quadratic coefficients −3/4, −5/2, −7/4 after the common 1/n. These are the two diagonal corrections to the factorial moments and the mixed coefficient in Theorem A.1 of Berzunza Ojeda–Holmgren–Janson: 64(13/128−1/8)/2=−3/4, 512(−5/1024)=−5/2, and 4096(121/8192−1/64)/2=−7/4. Mean scales are n/8 and n/64, standard scales sqrt(n), and the uniform range proved contains the theorem's required rectangle. The determinant is 387/262144 and the stated correlation follows. The frozen checker was inspected but not executed.

## originality

PASS

The known shape-by-shape theory already gives the X marginal, including its factorial moments, and applies separately to each orientation contributing to Y. The full mixed transform and its explicit nonzero negative dependence, rather than those marginal results or the general high-moment theorem, are the distinct contribution.

## value

PASS

These are the smallest two possible sizes with full consecutive support, a canonical test of the multitype fluctuation problem. The explicit covariance detects persistent geometric exclusion missed by the known marginals; the exact finite array also fixes the whole joint law rather than an isolated moment or one enumeration cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
