# Scientific assessment

## Correctness — PASS

The diffusion and reset generators are explicitly defined for both protocols; the sign state is symmetric and ergodic, diffusivities are strictly positive, and reset rate is positive. The stationary backward-age construction proves full joint one-time equality, not merely matching moments. The exact generator equations determine the common variance and the conditional-moment semigroup. The strict difference follows from an integral of a pointwise positive kernel, and asymptotics follow by explicit integration, including the degenerate boundary \(r=2k\). The reproducible checker tests symbolic generator identities and independently exponentiates the closed moment matrix at 80 parameter points. Numerical tests support but do not replace the analytic all-parameter proof.

## Originality — PASS, qualified

The closest primary source is Bressloff (2020), DOI 10.1088/1751-8121/ab97e0, whose equilibrium-redraw (F) protocol and static NESS precede this result; neither the NESS itself nor the resolvent method is claimed original. The 2018 Grebenkov full-text section 3 treats switching-diffusion propagators and first passage, but not the two Poisson reset protocols. The 2020 Kumar–Sadekar–Basu full-text article discusses orientation/position interventions on active self-propelled particles; its fixed-orientation full reset is not the equilibrium-redraw hidden-diffusivity model here, and it does not derive the all-lag squared-position comparison. Lux (2024) derives switching diffusion transition estimation, but no reset-memory phase boundary. The published run-and-tumble resetting result *Static-state blindness and a sharp temporal-memory crossover under run-and-tumble resetting* was inspected in full: it obtains a closely analogous two-mode convolution for **linear displacement** under telegraph self-propulsion. Its conclusion does not apply as stated to a Brownian particle with **switching diffusivity** and the higher-order observable \(X^2\); in the present model a fourth stationary moment and a different generator must be evaluated. The similar proof template is an explicit residual originality/value risk, not concealed. This is a qualified self-review rather than proof of first discovery. The complete 2020 Bressloff article was not accessible; uninspected related theory could cover this calculation implicitly.

## Mathematical value — PASS

The hidden-environment issue in experimental time series creates a motivated identification gap: full stationary position–diffusivity measurements cannot distinguish protocols, but temporal fluctuations of local squared displacement can. The theorem supplies an exact robust sign separation at every positive lag and a sharp kinetic threshold at which the dominant memory time switches from reset controlled to environment controlled. The conclusion is an all-parameter classification rather than a parameter substitution or isolated computation; applications to practical finite-sample discrimination are not claimed.

## Closest literature and limitations

- P. C. Bressloff, *Switching diffusions and stochastic resetting* (2020), DOI: 10.1088/1751-8121/ab97e0. Only the first-page publisher preview and abstract were accessible; risk of implicit temporal calculations remains.
- D. S. Grebenkov, arXiv:1812.07249v1 (2018), accessible full-text HTML, relevant section 3 switching diffusion propagators and moment relations, without resetting.
- V. Kumar, O. Sadekar, U. Basu, arXiv:2008.03294v1 (2020), full HTML sections on distinct resetting protocols for active Brownian swimmers.
- T. Lux, DOI: 10.1007/s11222-024-10397-6 (2024), full HTML read, switching-diffusion Fourier likelihood estimators.
- *Static-state blindness and a sharp temporal-memory crossover under run-and-tumble resetting* (2026), published full RESULT.md read, a close two-mode semigroup analogue with a different physical generator and observable.

All statements require symmetric positive switching, nonzero diffusivity contrast, a positive reset rate and Brownian forcing. The result concerns stationary squared-position memory, not dissipation or statistical power.

Self-review: passed. Independent audit: not yet performed.
