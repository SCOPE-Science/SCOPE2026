# Independent audit — spherical-join diameter/profile claim
- Record: `2026/09/10/011`
- Audited tree: `09662dc9e35a6ffefc8db8cf6a452e7e688c0180`
- Audited branch/commit: `main` / `e96707428e1608ae0287a471173e57e9f975206d`
- Disposition: **FAILED**

## Correctness

**PASS**

- In the spherical join J_a=S^2(1)*S^1_a, the t=0 factor S^2 is isometrically embedded. An antipodal pair therefore has distance pi, while the spherical-join metric has diameter at most pi; hence diam(J_a)=pi for every 0<a<=2pi.
- Minimizing the join cosine formula gives ecc(t)=pi-t for a<=pi and ecc(t)=acos(-sqrt(cos^2 t+cos^2(a/2) sin^2 t)) for a>pi, so radius=max(pi/2,a/2).
- The standard join volume density integrates to vol(J_a)=4*pi*a/3 and edge-link volume pi*a, with normalized link density a/(2*pi). The topological join S^2*S^1 is S^4.
- The archived proof notes and replay scripts are consistent with these direct analytic derivations.

## Originality

**FAIL**

- Rong-Wang state the standard join structure for Alexandrov spaces of curvature >=1: the two factors sit as convex subsets at mutual distance pi/2. The standard spherical-join definition also preserves the factor metric.
- Once one factor is S^2(1), which already has antipodes at distance pi, the constant-diameter conclusion is immediate: diam(J_a)>=pi from the factor and diam(J_a)<=pi from the curvature-normalized join metric. The claimed 'no diameter transition' is therefore a direct two-line consequence of standard join machinery, not a new theorem.
- The eccentricity, radius, volume and link formulas are elementary one-parameter calculations from the same standard metric/density. Their absence as a prepackaged table in a searched paper does not make the assembled profile substantively original.

## Scientific value

**FAIL**

- Correcting the target's mistaken monotonicity premise is useful project hygiene, but the corrected diameter statement and associated profile are standard-geometry consequences rather than a new research result.
- The record may serve as an expository or diagnostic note on which functional is constant versus varying; that utility is insufficient for an accepted standalone finding under the originality/value axes.

## Reproducibility and source checks

- Re-derived the diameter lower/upper bounds from the join cosine formula.
- Re-derived the two eccentricity cases and radius max(pi/2,a/2).
- Recomputed the join and link volume integrals and round endpoint normalizations.
- Inspected the committed proof notes and replay-driver source; no numerical step is load-bearing for the headline.

## Literature comparison

- [Finite Quotient of Join in Alexandrov Geometry](https://arxiv.org/abs/1609.07747): Rong and Wang summarize the standard Alexandrov join construction: the factors occur as convex subsets with all cross distances pi/2, within a curvature >=1 join.
- [Alexandrov geometry: foundations](https://arxiv.org/abs/1903.08539): Alexander, Kapovitch and Petrunin provide standard foundations for Alexandrov joins and related metric constructions used by the record.

## Limitations

- The audit does not claim the exact profile is commonly tabulated verbatim; it finds the profile mechanically derivable from established join formulas.
- The separate strainer-modulus question was not proved by the record and is not part of the accepted headline.
- The audit accepts all quantitative formulas as stated for a being the circumference of S^1_a.
- The scientific failure is due to originality/value, not mathematical correctness.

## Publication decision

The record is scientifically rejected and should be relocated atomically, with its complete existing package preserved, to `failed-attempts/2026/09/10/withdrawn-accepted-011--94492e8706e20cda`. This audit adds evidence and a `FAILED_ATTEMPT.md` marker before relocation. No GitHub change is claimed as already applied.
