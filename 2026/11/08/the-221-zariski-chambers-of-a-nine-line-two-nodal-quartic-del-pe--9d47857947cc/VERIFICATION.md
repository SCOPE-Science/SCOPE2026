---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact verification and limits

The supplied `verify_chambers.py` reconstructs all eleven curve classes in the rank-six Picard lattice of the ordinary five-point plane blow-up, computes their integral intersections, and applies Sylvester's criterion using exact rational arithmetic to all \(2^{11}=2048\) supports. The independent incidence-graph count selects compatible cross-pair lines, exceptional divisors, and zero, one or two root curves without matrix determinants. Both algorithms agree coefficient by coefficient:

\[
\begin{aligned}
F_0(t)&=1+9t+26t^2+30t^3+13t^4+t^5,\\
F_1(t)&=2t+18t^2+46t^3+38t^4+4t^5,\\
F_2(t)&=t^2+8t^3+16t^4+8t^5.
\end{aligned}
\]

The script prints `ALL_CHECKS_PASSED`; its exact output is included in `verify_output.txt`. To replay, run `python3 verify_chambers.py` using only the standard Python library. This verifies the finite intersection-lattice census; it does **not** prove that the candidate curve list is exhaustive on the surface. That geometric fact follows instead from the two Bézout inequalities and adjunction in `RESULT.md`. Realization of all negative-definite supports as chambers invokes the established Bauer--Funke--Neumann correspondence. The anticanonical volume dichotomy invokes Bauer--Schmitz and the nef-big property of the relevant blow-downs. The proof is over \(\mathbb C\) under precisely the stated incidence assumptions; the distinct eight-line \(2A_1\) type is excluded. Historical priority remains subject to independent inspection of inaccessible specialist literature.

No independent audit or external validation has been performed.
