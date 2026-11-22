# Scientific review

## Correctness — PASS

For every positive \(\alpha,\beta,\gamma,L\), the forward-conditioning calculation gives an exact saved-transmission probability. The derivative factors into a strictly positive multiplier and the difference between the expectation \(m_L\in(0,1)\) and a strictly increasing elementary function \(\Phi_d(s)\) whose range contains \(m_L\). This proves exactly one interior global optimizer, not only a numerical stationary point. A strict stochastic order of the duration-indexed weighted time variable proves decreasing optimal start. Both singular equal-rate and zero/infinite-length boundaries are explicit. The exact \(17/648\) example was independently checked by fractions; a piecewise-ODE numerical checker passed 1,231 assertions. Numerical checks are not used as the infinite-parameter proof.

## Originality — PASS (best-knowledge, priority qualified)

The primary literature on one-shot epidemic contact reductions considers nonlinear population SIR or stratified epidemic control, and the closest published indexed results concern finite-generation branching rearrangements, source placement on contact paths and evolving-trait contact windows. Their proved statements do not yield the exact full-parameter competing-risk optimization for one initially latent source, one eventual target, fixed perfect blockade duration and an infinite horizon. The closest related literature was compared at the level of dynamics, control, target functional and quantifiers. Database search does not prove novelty. Equivalence to a broader historical stochastic scheduling or reliability theorem remains a residual risk, and a full comparison with Feng–Iyer–Li (2021) distinguishes the models: their nonlinear SIR theorem permits an immediate optimum when reproduction is subcritical, whereas this individual latent-stage competing-risk model has a strictly delayed optimum for all positive rates.

## Value — PASS

A natural finite-control benchmark receives a full global classification rather than a special-case calculation: delaying a temporary blockade is *always* strictly beneficial relative to starting immediately, irrespective of positive progression, infection and recovery rates; the unique optimal start decreases strictly with duration, with both endpoints characterized analytically. This separates a linear competing-risk/latent-stage mechanism from the familiar nonlinear susceptible-depletion explanation for delayed epidemic interventions and provides an exact reference problem for checking more complex control formulations. The model is intentionally idealized and is not offered as operational medical advice.

## Closest literature and limits

Hollingsworth et al. (2011) discuss competing epidemic intervention goals; Shim (2013) analyzes age-stratified influenza vaccination and distancing; Di Lauro et al. (2021), Britton and Leskelä (2023), and Feng et al. (2021) examine nonlinear population-level contact controls. All five named scientific papers were materially inspected, with the relevant mathematical models and theorems read in full. The indexed mathematical results were compared by their stated claims; full GitHub texts of some nearby records were inaccessible and are not certified as noncovering. The theorem does not extend to general nonlinear epidemic prevalence, imperfect blockade or several targets.

Self-review: passed. Independent audit: not yet performed.
