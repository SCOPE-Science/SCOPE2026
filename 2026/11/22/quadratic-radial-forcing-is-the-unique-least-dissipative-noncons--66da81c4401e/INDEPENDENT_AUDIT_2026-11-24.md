# Independent mathematical audit

## correctness

PASS

With D=diag(1,1,η), stationarity makes the current J divergence-free; in the full even-coordinate entropy rate ∫J·D⁻¹J/p, the stationary log-density gradient and the equilibrium drift gradient drop out upon integration. This leaves η⁻¹∫fJ_z=V/η−E[fZ]; f is independent of z, so the axial density derivative integrates to zero. For the integration steps one can condition the stationary axial convolution on the current transverse state v: the backward OU history is e^(−u)v plus Gaussian noise, and Z is the resulting random smooth mean plus independent standard Gaussian noise. Polynomial bounds on the mean and its derivatives give finite score moments (conditional Jensen), as well as a polynomial bound on |log p| by Jensen on the Gaussian mixture. These justify integration with cutoffs. Stationary convolution gives E[fZ]=∫₀^∞e^(−ηu)E[f_u f_0]du. The squared transverse radius divided by two has Exp(1) law and generator 2s∂²+2(1−s)∂, so the centered Laguerre modes have eigenvalues −2m. The entropy weights are therefore 2m/[η(η+2m)], a bounded multiplier on L²; the calculation extends from finite sums. Strict increase gives the unique quadratic mode (4c²=V), and the difference of the second and first weights is 2/[(η+2)(η+4)], with equality exactly on modes 1 and 2 (transverse degrees 2 and 4). Each weight is strictly below 1/η and they converge to it; admissible normalized polynomial modes prove nonattainment and sharpness. The supplied checker’s generator recurrence follows by applying the joint generator to ZS^k; the reported finite checks were inspected as evidence, not rerun or relied on for the theorem.

## originality

PASS

The force profile, stochastic-thermodynamic identities and OU mode calculus are prior. The distinctive claim is the full stationary entropy shape optimization at fixed transverse Gaussian variance, including the sharp remainder and equality classes. No inspected source combines the same admissible force class and entropy functional so as to cover that optimization directly.

## value

PASS

The budget compares physically different profile shapes on a common stationary force scale. The result explains why the earlier optical quadratic is extremal and quantitatively controls all deviations across an infinite smooth class, nonperturbatively. The sharp second-mode remainder and unattained upper endpoint distinguish it from merely computing the quadratic example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
