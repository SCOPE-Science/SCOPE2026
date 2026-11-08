# Scientific review

## Correctness

**PASS.** The claim fixes a positive constant drive, deterministic initial phase-space state, the exact two-jump work convention, and the underdamped parameter range. The mean response follows from the homogeneous fundamental matrix; the variance follows both from the equilibrium-covariance subtraction identity and from the independent noise convolution. Strict log-concavity of the positive first-lobe impulse response proves the needed derivative inequality for the standardized displacement, while later times are dominated by the first global response maximum and the monotonically increasing accumulated variance. Algebra yields the exact Gaussian law and all small-friction constants. The supplied standalone code passed 421 symbolic/numerical diagnostics after execution; finite checks do not replace the continuum arguments.

## Originality

**PASS, with residual publication-priority risk.** Relevant direct comparisons are Yao--Bao--Hou's full 2026 source [1], Schüttler and collaborators' full 2025 source [2], and the 2008 optimal-control literature [3]. The general ideal-work and ideal-variance formulas, harmonic step response, and Gaussian oscillator covariance are explicitly acknowledged as prior. The new claim is the complete time-optimality theorem in a specified two-jump active-force protocol simultaneously for mean work and single-trial sign reliability, plus the universal near-ideal variance ratio and sharp rare-failure equivalent. The most relevant full-text comparisons do not state those pulse-restricted conclusions. An inaccessible or unindexed analysis of the exact same pulse protocol is the principal residual novelty risk, not proof of its absence.

## Value

**PASS.** The motivating study isolates physical implementability as an unresolved consideration: its unrestricted work optimizer requires ideal boundary impulses. The restricted two-jump protocol needs only a single held trap displacement (though jumps still have infinite bandwidth). Its exact optimal dwell time, its coincident mean/reliability timing, the relative variance penalty \(\pi^2/8\), and the exponentially small high-quality failure probability quantify a specific experimentally motivated performance tradeoff. The coupled mean-and-sign objective and universal asymptotic comparison make the result more than the textbook overshoot of a damped oscillator.

## Sources and limitations

[1] https://arxiv.org/html/2610.38653v1 (model, exact unrestricted work and variance, implementability discussion, Appendix C); [2] https://arxiv.org/html/2501.18613 (overdamped work and measurement efficiency); [3] https://pubmed.ncbi.nlm.nih.gov/18624523/ (ideal underdamped boundary operations, abstract-level inspection). There is no finite-bandwidth theorem, no work-cost accounting for force generation or initial state preparation, and no claim about repeating cycles with nonzero inherited velocities. Publication priority remains subject to independent examination.

Self-review: passed. Independent audit: not yet performed.
