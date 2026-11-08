# Scientific review

**Correctness — PASS.** The positive equilibrium is unique, and the Jacobian, Neumann mode determinants, and simple first-mode crossing follow by exact algebra. A Lyapunov–Schmidt reduction uses the slaved mean and second-harmonic terms and an exact rational-sign certificate to obtain \(S>0\), \(C<0\). Only the first Fourier mode is critical, so standard semilinear parabolic local bifurcation and spectral stability imply two positive attracting nonconstant steady states. The included standalone SymPy checker reproduces the needed differentiations and identities from original reactions.

**Originality — PASS (best-knowledge).** Wang–Zou's 2018 source contains the ratio-dependent, fear-cost-only PDE [Eq. (81)] and uses linear Turing inequalities plus numerical patterns, but the relevant material does not establish an exact nonlinear cubic sign and local attraction of two bifurcating nonconstant equilibria at these parameters. Song–Zou 2014 develops normal forms for a cost-free ratio-dependent system; it does not directly cover the fear-cost model. Semantic research searches and accessible previous claims gave no directly covering result. A literature-coverage risk remains for unindexed model-specific nonlinear analyses.

**Value — PASS.** A positive Turing growth rate does not guarantee the existence of *stable* nearby nonlinear patterns: subcritical branches, unstable equilibria or evolution to distant attractors are possible. Here an exact cubic sign resolves this ambiguity for a biologically motivated cost-only, ratio-dependent predator–prey model and proves robust positive stable pattern coexistence on an open parameter side. This is a qualitative dynamical distinction, not a small numerical adjustment.

**Limits.** One spatial dimension; one exactly specified parameter family; local branches and local stability only, no global ecology or transport. The originating article's linear threshold is treated as prior art, and full publication priority is not certified.

Self-review: passed. Independent audit: not yet performed.
