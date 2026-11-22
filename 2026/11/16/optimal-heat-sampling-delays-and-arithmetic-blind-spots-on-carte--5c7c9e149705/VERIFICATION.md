---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Base Fourier transform gives lambda(theta)=2 sum_r(1-cos theta_r) in [0,4d], while path eigenvalues mu_j=2-2cos(pi j/m) are distinct and eigenvector amplitudes v_j(a)=sqrt(2/m)cos(pi j(a+.5)/m) (j>0). Visibility vanishes exactly when j(2a+1)=m(odd), giving (g-1)/2 invisible modes; the weighted temporal Vandermonde hence has rank min(p,m-(g-1)/2). A compact base-frequency range and uniformly bounded invertible row rescalings give stable frames exactly at full rank. At endpoint, Vandermonde determinant times exp(-tau lambda C_m) is smallest at lambda=4d. Its log derivative equals sum_{i<j} Delta/(exp(tau Delta)-1)-[4d C_m+sum_{i<j}mu_i], and log second derivative strictly negative; zero and infinity limits yield one maximum. The triangular Euler-Maclaurin formula has first correction -m/(2tau), and sum_{i<j}mu_i=m²(1-4/pi²)-2m+O(1); uniform smoothness, monotone implicit function give tau=s_d+c_d/m+O(m^-2). Independently integrated defining double integral with scipy and solved finite stationarity: d1 s=0.1682323819219894,c=0.0587318012130304, width-error times m at m=20,50,100 is .0597264,.0591269,.0589289, approaching c; d2 s=.1003350654556886,c=.020539050871182. Finite computations corroborate but do not prove uniform asymptotic. Critical distinction: graph Laplacian is combinatorial, determinant not minimum frame eigenvalue.

## originality

PASS

General iterated-frame criteria and prior normalized-path D-optimal problems are acknowledged. No confirmed source entails all three of arithmetic visibility, shifted worst-base determinant optimum and corrected wide-strip limit. Full text of a relevant 2026 graph paper could not be read, retained as real risk.

## value

PASS

This exact structural observability law and all-width D-optimal design for natural infinite Cartesian strips addresses a real sensor-placement/time trade-off, with arithmetic invisible modes, a finite optimal two-rail time and a nontrivial first wide-strip correction. The full-space, uniform-in-longitudinal-frequency model is intrinsically motivated, not an arbitrary finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
