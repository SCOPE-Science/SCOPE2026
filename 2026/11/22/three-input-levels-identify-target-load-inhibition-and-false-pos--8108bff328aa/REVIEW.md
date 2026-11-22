# Scientific assessment: three-level inhibited environmental-DNA detection

## Correctness — PASS

The proof starts from explicit Poisson target-copy counts, per-copy independent thinning and an independent constant false-positive mechanism. Log-negative probabilities give exactly \(y_j=a+j\theta q^j\). Eliminating the positive target parameters yields one quadratic equation in the nonnegative background intensity. Its two real algebraic roots are \(a\) and \(a+4\theta q(1-3q+3q^2)\), and the second root contradicts \(y_1-a>0\). The physical root gives the explicit inverse. A continuous two-input parameter family proves minimality, the exact Jacobian is positive, and adjacent-response differences prove the three regimes and their boundary equalities. A standalone standard-library checker passes 46,824 exact rational assertions; the finite diagnostics do not prove the real-parameter statement.

## Originality — PASS (best-knowledge review)

Wilcox et al. (2013), *PLOS ONE* 8:e59520, https://doi.org/10.1371/journal.pone.0059520, examines eDNA assay specificity, sensitivity, and false positives. Schultz and Lance (2015), *PLOS ONE* 10:e0141503, https://doi.org/10.1371/journal.pone.0141503, develops a Poisson survey-sensitivity model and discusses inhibition but not this simultaneous three-dose inverse. Both complete open-access articles were inspected. McKee et al. (2015), *Biological Conservation* 183:70–76, https://doi.org/10.1016/j.biocon.2014.11.031, experimentally addresses dilution and inhibition; only a public abstract was accessible. General exponential-reconstruction theory provides overlapping techniques, but no inspected source established the constrained global minimum-three-level inverse with the positivity exclusion. A full historical priority search and the inaccessible McKee paper remain residual risks; the search cannot prove novelty.

## Value — PASS

The object is a minimal-level calibration question under three confounded mechanisms that directly affect interpreting ecological detection: template-copy scarcity, loss of efficiency from carried inhibitors, and a fixed false-positive mechanism. Complete recovery from exact population positivity rates avoids unnecessary assumptions that response rises with dose, distinguishes a spurious formal inverse from a physically admissible one, and proves two levels insufficient. This is a natural sharply specified identifiability boundary and mechanistic benchmark, not an empirical claim that these assumptions fit all assays.

## Limitations

The model assumes homogeneous independent wells, exactly controlled \(1:2:3\) input levels, a per-copy efficiency \(q^j\), and a dose-invariant independent background probability. True probabilities require repeated wells, and finite-sample stability is not established. At vanishing target intensity or extreme inhibition, conditioning deteriorates. Results about occupancy-survey temporal covariances are not equivalent to this static three-dose inverse. The full text of McKee et al. was not inspected and broader inverse-response literature could overlap.

Self-review: passed. Independent audit: not yet performed.
