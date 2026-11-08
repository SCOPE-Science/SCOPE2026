# Scientific review

## Correctness — PASS

For each spatial sine eigenmode, the theta update is a scalar stable recurrence with exact control coefficient and an exactly summable finite-horizon Gramian. The supplied proof reconstructs the minimum-energy interpretation, provides uniform estimates for both directions, and proves necessity by a highest-frequency subsequence. The finite-T critical formula is derived using the logarithm of the recurrence factor. All relevant quantifiers and boundary cases, including theta equal to one half and either critical parameter equal to zero, are explicit. The accompanying standalone verifier gave `VERIFY_OK 108`; its tests are supplementary rather than a replacement for proof.

## Originality — PASS, qualified

The closest inspected work includes Kwon and Nunda (arXiv:2610.40461v1), whose fully discrete CN test uses a low-mode target, and Boyer and Hernández-Santamaría (2025), whose equation (160) *already* gives the theta-scheme infinite-horizon moment denominator. This established factor is not claimed as a novelty. The present claimed classification is the finite-horizon full-actuation sharp two-parameter mesh equivalence and high-mode critical profile. Boyer, Hubert and Le Rousseau (2011) treat theta-scheme relaxed observability; their full text remained inaccessible, so priority is qualified. Search comparisons also included relevant published mathematical records and known historical claims.

## Value — PASS

All high-mode terminal targets must be considered to justify uniform hard-terminal-energy discretization, whereas low-mode refinement can miss the obstruction. The exact frontier gives a useful and sharp time–space coupling choice: CN allows steps proportional to spatial width, but any fixed off-centered theta scheme requires the squared spatial width. A two-variable boundary law also distinguishes bounded bias from hidden energy blow-up in stable schemes.

## Scientific limitations and nearest literature

Results concern the Dirichlet centered-difference heat operator, full actuation, fixed final time, exact arithmetic, and the declared endpoint control-energy norm. They do not imply partial-control null controllability, nonlinear convergence, or continuum limit control convergence. The full 2011 journal article could not be materially compared. This is an independent-priority risk rather than a failure of the reconstructed finite-dimensional proof.

Self-review: passed. Independent audit: not yet performed.
