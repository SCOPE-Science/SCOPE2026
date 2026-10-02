# Projected-Verlet projection-work benchmark on the Cartesian double pendulum

## Scope of the corrected finding
For the Cartesian double pendulum with unit masses and lengths and g=9.81, the supplied projected-Verlet implementation exhibits large, reproducible short-horizon energy drift at the filed anchor and sampled nearby initial data. The earlier version stated a uniform theorem for every h in (0,0.01] and every datum in an open neighborhood. The available floating-point experiments and non-validated RK4/Taylor remainder estimates do not prove that continuum-quantified statement, so it is withdrawn here.

## Exact algebraic observation
Before projection, velocity Verlet for a constant force preserves the separable Hamiltonian exactly in exact arithmetic. With grad U constant,

p_{1/2}=p-(h/2) grad U,  q*=q+h p_{1/2},  p*=p_{1/2}-(h/2) grad U,

and direct expansion gives H(q*,p*)=H(q,p). Consequently, in this implementation every energy change comes from the subsequent position and momentum projections. This identity is exact; it is independent of the numerical experiments below.

## Reproducible numerical observations
At anchor (theta1,theta2,omega1,omega2)=(0.840,0.842,1.918,1.782), the archived table gives H0=-10.944452816369246 and projection-work density w=-64.74051122752584. Over T=10, the archived runs give:

- h=0.01, N=1000: dH=-8.041957890370803 and |dH|/(N h^3)=8041.957890370801.
- h=0.005, N=2000: dH=-5.168375867946214 and |dH|/(N h^3)=20673.50347178485.

Five archived random perturbations within the stated angle/velocity box at h=0.005 also have negative drift between about -4.68 and -5.59 and effective ledger ratios far below 100. The files `artifacts/core.py`, `artifacts/run_anchor.py`, `artifacts/run_exact.py`, and `artifacts/table_anchor.json` contain the implementation and data.

## What is and is not established
The exact constant-force identity and the finite computations above are supported. They are useful benchmark evidence that projection can dominate the energy behavior of this baseline. They do **not** certify the former universal lower bound for every step size and every point of an open set. A validated version of that theorem would require rigorous enclosure of the exact-flow integral, projection solver error, and the uniform Taylor/Gronwall remainders over the whole parameter box.

## References
- M. West, *Variational Integrators* (2004), for the variational/SHAKE-RATTLE background.
- S. Reich, backward-error analysis for numerical integrators, for the contrasting near-conservation theory of symplectic methods.
