# Review of the square-scale fitted-Poisson empirical test result

## Correctness: PASS

The statistic has the exact source normalization: it is the **full** \(\ell_1\) discrepancy, not half-total-variation. The proof controls estimated-mean substitution with the exact Hellinger affinity, derives a finite-binomial mean identity, and establishes concentration by bounded differences. A Poisson local limit and justified finite-window truncation yield the critical Gaussian-occupancy integral; separate estimates prove the two outer regimes. The modal-density calculation gives a strictly increasing profile and a positive, explicitly calculated \(3/2\)-power singularity at each integer-occupancy threshold. The standalone checker passes 126 independent finite checks. The analytic arguments, not that finite checker, support the infinite assertions.

## Originality: PASS, qualified

The primary Kirui et al. preprint (arXiv:2402.12866) and the earlier 2023 thesis both provide the weighted \(L_1\) statistic; the thesis also gives the classical Poisson mode fact. Their inspected Sections 2–4 and Chapters 3–5 do not contain the increasing-intensity null limit or its singularity ladder. The general empirical-distribution concentration theory of Berend and Kontorovich (2012) and occupancy approximation of Barbour (2009) supply techniques but not the full curve. Related mathematical record searches found no directly dominating statement. Potential broader generic results not inspected remain a priority risk. The source preprint's earliest verified precise public day is 2024-02-20; a 2023 thesis was examined but a public repository-deposit day was not established.

## Value: PASS

The result describes a real statistical calibration boundary: even under an exact Poisson null, the full empirical/fitted mass-function discrepancy switches from nearly zero to nearly its maximum when the alphabet width outgrows the available sample. Its nontrivial critical curve and infinitely many non-smooth occupancy-mode transitions are structurally informative, beyond a routine fixed-parameter consistency statement.

## Closest literature and limitations

Main sources are Kirui et al., arXiv:2402.12866 and doi:10.37920/sasj.2025.59.1.2; Kirui's 2023 thesis, Chapter 3; Berend–Kontorovich, arXiv:1205.6711; and Barbour, arXiv:0902.0879. The result concerns one statistic and its null law only. It does not analyze bootstrap critical values, type-I rejection probability or power. Classical Poisson local limits, mode formulas, and empirical-process concentration are credited. Other general occupancy asymptotics may cover components of the finding.

Self-review: passed. Independent audit: not yet performed.
