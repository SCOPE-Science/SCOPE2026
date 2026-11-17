# Independent mathematical audit

## correctness

PASS

For each mode a=omega^2, the triangular stationary OU Lyapunov equations give Var(u)=T/[a(1+a tau)] and c_a(t)/Var(u)=[e^-at-a tau e^-t/tau]/(1-a tau), extended at a tau=1. Subtracting e^-s after the critical normalization produces exactly d T_c integral omega^(d-3)(e^-s tau omega²-e^-s)/(1-tau² omega^4). With z=sqrt(tau)omega and T_c/tau->(d-4)/d, the scaled integrand is positive, removable at z=1, and integrable at infinity precisely for 4<d<6. Dominated convergence gives Phi_d(s) and local uniformity. Short-time z=y/sqrt(s) integration gives Gamma((d-4)/2)/(6-d)*s^((6-d)/2); large-time small-z Laplace gives Gamma((d-2)/2)/2*s^(-(d-2)/2). Independently evaluated the d=5 integral and the erfi/erfc closed form with mpmath at s=.04,.2,1,2,10; differences were below 1e-20, and Phi_5(1)=0.429969029096485. These finite checks verify constants, not an unbounded limit or finite-N sphere.

## originality

PASS

The same active spherical Debye model and static critical dimensions were established by Ikeda (2022), whose full accessible text explicitly confines itself to static properties and leaves dynamics for future work. A 2025 work studies temporally hyperuniform rather than OU-persistent forcing. Semantic published-record searches for the precise persistence-clock correction and its two endpoint exponents retrieved the current submission and unrelated processes, not an equivalent prior theorem. This is qualified best-of-knowledge originality, not a completeness proof over all linear Gaussian critical scaling literature.

## value

PASS

The critical temporal autocorrelation is a natural observable left open by the source paper’s static analysis. The theorem provides the complete first positive persistence-clock correction over the nontrivial spectral band 4<d<6, its exact integral and universal coefficients, the crossing of two distinct temporal powers, and a closed d=5 function. This is an independently useful exact critical dynamic invariant with clear hypotheses and no unsupported finite-size claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
