---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For a designated r-subset of sinks in one bipartition, forced incident edges leave B_{a−r,b} acyclic orientations; mixed-part sink sets are impossible. Subset marking gives A_{a,b}(z)=B_{a,b}+∑_{r≥1}C(a,r)B_{a−r,b}(z−1)^r+∑_{r≥1}C(b,r)B_{a,b−r}(z−1)^r, hence bivariate EGF B(x,y)[exp((z−1)x)+exp((z−1)y)−1]. With H=1−(exp x−1)(exp y−1), diagonal p_n=2c_n(z)/c_n(1)−1, c_n(z)=[x^ny^n]exp(zx+y)/H. At ρ=log2, H_x=H_y=H_xx=H_yy=−2, H_xy=−4, and independently computed Q=16ρ³(1−ρ)>0. Khera–Lundberg's source theorem verifies strictly minimal diagonal smooth point; applying entire-numerator ACSV uniformly on bounded |z|≤R gives c_n(z)/c_n(1)=exp((z−1)ρ)+O_R(n−1). Then p_n(z)=2^z−1+O_R(n−1), Cauchy estimates give all-k error C_R/(nR^k) and summable TV error. Independent exhaustive orientation counts for n=1..3 gave sink histograms 2; (12,2); (186,42,2) agreeing with poly-Bernoulli totals 2,14,230. Symbolic Q identity proved independently. Finite tests do not establish ACSV bounds.

## originality

PASS

PASS best-of-knowledge: the complete zero-truncated Poisson(log 2) law for the number of sinks in uniform acyclic K_{n,n}, including uniform complex-disc O_R(n^-1) PGF control and geometric local probability errors, was not stated in the directly related source material inspected. Established poly-Bernoulli enumeration, general sink polynomials, unique-sink atoms and multivariate ACSV are excluded from originality credit.

## value

PASS

Natural intrinsic count of terminal vertices in uniformly random acyclic bicliques has a nondegenerate, non-Gaussian, fully specified limiting distribution with a quantitative total-variation rate and geometric uniform local controls. A useful benchmark contrasting with the known Gaussian longest-path statistic; not merely another isolated finite table or a restatement of the unique-sink atom.

The dated certificate retains the supplied scientific assessment, sources and limitations.
