# Scientific review

## Correctness — PASS

The precise claim concerns the full three-variable ODE, with positive fear, stricter infected-predator mortality, positive prey and nonzero predator initial conditions, and predator-free invasion equality. The proof verifies positivity, a prey logistic bound, an integrable positive-part bound on total predator growth, global convergence, exponential disappearance of the infected fraction, and the exact critical asymptotic using a stable prey-to-predator ratio equation. The nonstandard step is deriving \(h/P\to-B/\sigma\) **after** global convergence and subexponential predator decay, rather than assuming the center-manifold reduction. The symbolic coefficient and numerical diagnostic code replayed successfully from the packaged file. Numerical integration does not replace proof.

## Originality — PASS on inspected material

The initiating Scientific Reports article [1] was inspected at the equations, predator-free equilibrium and local eigenvalue criterion, infection reproduction analysis, Theorems 4–6, and discussion. Its predator-free stability assertion uses a strict inequality; the article does not state global extinction and sharp amplitudes at equality. The related two-path infected-predator paper [2] uses a different model and was available only as abstract/bibliography, so its full contents are a residual priority risk. Targeted public literature search and published mathematical finding-index searches for predator-free critical extinction, \(t^{-1}\) laws, fear/refuge and infected predators yielded analogous results in different predator systems, not a stronger theorem for the same three-compartment ODE. An unsuccessful search cannot prove priority.

## Value — PASS

The predator-free boundary is ecologically meaningful because predator invasion changes sign there, and a zero eigenvalue does not determine whether predators clear or persist. The theorem resolves global fate of the full infected-predator system at equality and quantifies how fear speeds predator clearance, while a surprising cancellation keeps prey's leading deficit independent of fear, incidence and treatment. This is a structural ecological asymptotic rather than a numerical threshold repeat or an arbitrary parameter slice.

## Scope and closest work

This is a result for the original full system, not a proof of endemic or disease-free coexistence stability. The original paper [1] provides strict local predator-free stability and broader disease-bifurcation results; [2] concerns two pathways of infection. Related critical-extinction results for delayed or stage-structured predators have distinct variables and assumptions and therefore do not imply the specific critical amplitudes here. Residual risks are unindexed equivalent analyses, abstract-only access to [2], and possible earlier unverified preprints. No assertion of priority beyond inspected evidence is made.

Self-review: passed. Independent audit: not yet performed.
