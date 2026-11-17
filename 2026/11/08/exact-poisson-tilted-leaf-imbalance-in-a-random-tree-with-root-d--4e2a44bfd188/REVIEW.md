# Independent mathematical audit

## correctness

PASS

For a state (N,I,D), a root event at rate 1 sends (N,I,D) to (2N+1,2I-1,D+1); nonroot leaves at rate (N+I)/2 send I to I-1, other nonroot vertices send I to I+1. The generator yields G I=-2, G(I^2)=I^2-6I+N and G(I z^D)=[2(z-1)I-(1+z)]z^D. With E z^D=e^{(z-1)t}, solve the forced ODE from initial (3,1,0); differentiation and the second moment ODE give the stated mixed transform, covariance and exact variance. Independently checked the symbolic generator substitutions, including the boundary at z=1 and e^t coefficients. Moment localization is supported by finite size moments; simulations alone not invoked.

## originality

PASS

The full Björnberg–Mailler source supplies the continuous-time root-doubling model, asymptotic size, root-event clocks and limiting degree proportions, but not the joint Poisson-tilted leaf-imbalance transform or its finite-time covariance. Classical recursive-tree leaf results omit the global doubling shock.

## value

PASS

The imbalance I=2L-N is a natural centered leaf count whose degree-density limit is zero; exact finite-time variance of exponential order and negative covariance with the number of global doublings expose genuine second-order dependence invisible in first-order degree proportions. Poisson tilting also gives every conditional mean E[I|D=k].

The dated certificate retains the supplied scientific assessment, sources and limitations.
