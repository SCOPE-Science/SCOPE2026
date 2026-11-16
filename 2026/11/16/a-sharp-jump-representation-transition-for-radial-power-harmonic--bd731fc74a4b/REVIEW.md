# Scientific review: radial-power harmonic Dirichlet boundary jumps

## Correctness — PASS

The weighted energy is defined with normalized area and the complex derivative pair, avoiding a factor-of-two ambiguity. The exact Fourier multiplier is \(\psi_\alpha(n)=n^2B(n,\alpha+1)\). Direct beta-function evaluation proves the positive Poisson-mixture representation for \(0<\alpha\le1\). Classical finite-geometric-sum integration handles \(\alpha=0\). Above one, the multiplier tends to zero despite a positive first eigenvalue; for **any** positive off-diagonal jump measure, Cesàro averaging and Fatou's lemma force the total jump measure to vanish. This does not use rotation invariance. The Poisson mixture has exactly infinite activity below one, rate one at one, and yields the stated singular asymptotics. The first positive eigenvalue is the sharp spectral gap. `CHECK.py`, run from the actual document directory, passed 674 supplementary finite assertions. No finite assertion is used as a universal proof.

## Originality — PASS relative to inspected sources

The recent foundational paper of Bourabiaa et al., arXiv:2607.26870 (2026-07-29), introduces the positive-jump Douglas class, proves general superharmonic sufficiency and the existence of associated Hunt processes, and explicitly raises classification and jump-kernel identification in its §5 Problems 1 and 4. Its §4.2 computes only the classical constant-weight wrapped Cauchy case; Appendix A.2 studies the different stable symbols. The present **iff** for all radial-power parameters, the exact beta–Poisson mixture, its sharp angular singularity, and the finite-activity compound-Poisson endpoint were not found in that source. Bao, Göğüş and Pouliasis (2018, first electronically published 2017-05-19) cover general superharmonic weights and discuss the radial powers, but their reviewed sections study Dirichlet spaces and composition operators, not this sharp positive jump characterization. Actual published-finding corpus searches returned adjacent but different topics; no equivalent or dominating claim was observed in the checked evidence.

**Closest literature:** Bourabiaa et al. (2026), sections 2, 4, 5, Appendix A; Bao–Göğüş–Pouliasis (2018), introduction, §2, §5. The known superharmonic implication is explicitly prior, not proposed as novel. A search cannot establish global priority, and an equivalent result could exist under conditional-negative-definiteness, subordination, or Lévy-symbol terminology.

## Mathematical value — PASS

The 2026 source explicitly asks for concrete characterization and a description of Lévy dynamics. For the canonical radial powers, the result determines the entire sharp admissible parameter interval and a strict obstruction beyond it, rather than one more isolated example. The jump-law calculation reveals a genuine qualitative transition from infinite-activity paths to finite-activity compound Poisson motion at the exact endpoint, together with the singular coefficient and spectral gap useful for boundary potential theory. General construction of the Hunt process, superharmonic sufficiency, and wrapped Cauchy motion are previously established and are not counted as this contribution.

## Scientific limitations and residual risk

The result is specific to radial powers; general weight classification is not settled. The positive representation is not asserted to be unique. The analytical proof is a self-review, not an independent audit. Historical equivalence under differently named Lévy or harmonic-extension frameworks remains possible, though no inspected source gives decisive coverage.

Self-review: passed. Independent audit: not yet performed.
