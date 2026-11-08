# Scientific review: dephasing-optimized quantum-dimer capture-time fluctuations

## Correctness — PASS

The claim is for one finite, explicitly normalized Lindblad model with two site dephasing jumps, one continuous sink of population decay rate \(2J\), and an initial donor excitation. The survivor generator is a real four-by-four matrix. The embedded checker reproduces both exact resolvent moment formulas, the relative-variance derivative, the threshold equation, and the mean-optimum comparison. Uniform absorption is justified by the lack of a nonzero nonabsorbing positive state together with compactness of normalized density matrices. The global minimizer classification is proved using coefficient signs and Descartes' rule; large-detuning asymptotics use root bracketing and a uniform polynomial expansion. Numerical quadrature of 32 survival integrals at 16 parameter pairs independently tests the moment normalization. Finite tests are supplementary, not the basis for statements for all detunings.

## Originality — PASS, with residual risk

Mülken and Schmid (2010, arXiv:1008.4022) directly model a detuned dissipative quantum dimer. Their full paper examines survival probability, fixed-survival-fraction decay intervals, and longest relaxation; this paper is the closest dynamical model and could implicitly allow the new integrals to be computed. It does not explicitly establish a global optimum for the coefficient of variation, a sharp threshold at \(\sqrt{2\sqrt{21}-9}\), or the strict gap to the mean optimum. Wu, Silbey, and Cao (2012 preprint/2013 article, arXiv:1207.6197) cover mean trapping-time scaling and a donor/acceptor example, not variance optimization. Coates, Lovett, and Gauger (2022 preprint, arXiv:2210.11875) investigate multiple efficiency maxima from steady-state injection/extraction in disordered networks; their objective and protocol differ from a single first capture. Friedman, Kessler, and Barkai (2016, arXiv:1611.05676) use discrete repeated projective measurements, not a continuously absorbing Lindblad sink. Semantic searches for first-capture fluctuations, two-site quantum jump waiting times, and dimer dephasing/variance optima revealed no directly covering result. This is evidence of an apparent gap, not a proof of publication priority.

## Mathematical value — PASS

The full first-absorption-time dispersion is a natural reliability diagnostic independent of mean transport time. The exact finite detuning threshold identifies a counterintuitive control regime in which dephasing strictly improves timing reliability while necessarily worsening mean latency. The global root classification and limiting two-unit separation quantify a real trade-off rather than merely computing a moment or incrementally adjusting a coefficient. The physical matching \(2J\) means the sink's no-jump amplitude damping strength equals the coherent hopping amplitude. The restriction is explicit; extension to arbitrary sink strengths remains open.

## Limitations and external checks

Only the matched sink-rate, single-excitation, Markovian model is covered. The 2010 dimer survival law may permit implicit recovery of some formulas; prior equivalent optimization may be unidentified. No independent external mathematical validation has been performed. No claims about projectively sampled first detection, source-driven steady-state efficiency, thermal environments, or all sink strengths are made.

Self-review: passed. Independent audit: not yet performed.
