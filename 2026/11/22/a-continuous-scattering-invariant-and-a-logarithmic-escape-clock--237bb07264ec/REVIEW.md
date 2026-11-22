# Scientific review

**Claim assessed:** existence, nonconstancy and continuity of a positive scattering invariant on the explicitly given open escaping cone of the quadratic zero-forcing flow, together with the universal \(4\log\log t\) correction and the \(2/t\) scattering-coordinate correction.

## Correctness: PASS
The four coordinate equations are derived directly from the printed polynomial vector field and independently symbolically checked. Inward boundary derivatives at \(p=1/2\), \(p=2\), and \(qx=1/10\) are strict. Explicit reciprocal bounds show forward existence and square-integrability of \(qx\). The stable convolution for \(p-1\), Cauchy--Schwarz, and the exact logarithmic derivative yield a positive finite scattering limit. Uniform tail control gives continuity; a small-start asymptotic proves it is nonconstant. Inverting the increasing height coordinate proves the second-order clock, and the stable convolution proves the \(2/t\) term. A numerical trajectory checks consistency, not infinity.

## Originality: PASS within the inspected evidence
The 2019 originating study establishes the equation and examines homoclinic bifurcations; only the author-upload abstract and metadata could be retrieved, so its uninspected full text is a named priority risk. The complete 2024 Qu--Yang article examines non-Darboux integrability, equilibrium distributions, local bifurcations, and the Poincaré sphere at infinity, without an original-time scattering invariant or second-order escape law. A pre-existing theorem for the identical zero-forcing cone (opaque record `fcfe8e03-c010-46c6-89dc-471d7b2c2296`) already proves the leading laws; these are **not** novel. It does not state the finite invariant, its nonconstancy, the state-resolving constant term, or the renormalized \(2/t\) correction. The leading laws do not imply those finer statements. A contextual 2020 paper computes heteroclinic connections to infinity in a different parameter setting; its abstract does not cover the asserted original-time limit. Searches for aliases and stronger exact classifications returned no decisive covering result. No claim of exhaustive worldwide novelty is made.

## Value: PASS
The invariant \(\mathcal L\) preserves an explicit nontrivial piece of initial-state information along trajectories escaping to infinity, while the \(4\log\log t\) and constant terms resolve physical-time escape beyond the known leading-order estimate. It provides a quantitative refinement of the published infinity phase portrait, motivated by a naturally degenerate equilibrium-line parameter choice. It is not a trivial rewriting of the leading \(q^2\sim8\log t\) law: the proof requires a convergent renormalized generator integral. This complements, rather than contradicts, the known obstruction to algebraic/Darboux global first integrals.

## Limits and risks
The domain is a strict forward-invariant open region, not a whole-space basin. The scattering constant is defined by a convergent trajectory integral, not a closed elementary expression. The original 2019 paper full text could not be inspected through available routes, and there may be unindexed equivalent asymptotics. The analytical proof is reviewed in this package; no external mathematical validation is asserted.

Self-review: passed. Independent audit: not yet performed.
