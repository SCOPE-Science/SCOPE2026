# Scientific review

## Correctness — PASS

For \(\kappa,D,r,a>0\), the Poisson renewal integral gives the unique, positive, even invariant density. The stationary forward equation in a source-free gap is the homogeneous second-order equation \(D p''+\kappa x p'+(\kappa-r)p=0\). Every zero of \(p'\) away from the origin has second derivative of sign \(r-\kappa\), so the derivative cannot reverse its sign once it leaves zero. For equal symmetric atoms, the distributional jump \(p'(a+)-p'(a-)=-r/(2D)\) plus positivity and tail decay proves the global count of modes. At equality \(r=\kappa\), direct integration gives the normalized plateau. The independent renewal-age checker passed 33 finite checks, without being used in place of proof. Risk: only the expressly stated diffusion and resetting assumptions are covered.

## Originality — PASS (qualified)

Olsen (arXiv:2310.04840, Sections II--V) provides the general renewal measure and all stationary moments for distributed resets in a harmonic potential; the full spatial-mode sign theorem and exact flat plateau are not stated there. Pogorzelec and Dybiec (arXiv:2301.11427, Sections I--IV) discuss multimodality but study a different process (Levy driving, quartic and glued potentials, one-site resetting). Trajanovski et al. (arXiv:2301.12304, accessible Sections I--III) use a fixed reset site and examine comb constraints. Julián-Salgado et al. (arXiv:2311.11897, Sections I--VI) study optimizing free Brownian target search from two reset points, not stationary OU modes. Relevant own prior claims involve a harmonic run-and-tumble mode transition and random-reset first-passage envelopes; neither implies the present derivative-sign classification. The general renewal representation is a strong starting point, but the complete global threshold requires additional ODE sign and jump analysis. Residual risk: an unlocated published calculation could already state an equivalent phase diagram.

## Mathematical value — PASS

For symmetric reset sources with a central gap, the transition from accumulation at the confining minimum to depletion there is a physical localization question. Its exact threshold is independent of the reset distance and diffusion strength, despite those quantities setting the length scales of the steady state. For the two-point model, the analysis gives the complete global mode diagram and an exact nontrivial interval of maximizers at criticality, not merely an isolated curvature sign. This is a structural classification with a testable parameter boundary and goes beyond a numerical modality plot.

Self-review: passed. Independent audit: not yet performed.
