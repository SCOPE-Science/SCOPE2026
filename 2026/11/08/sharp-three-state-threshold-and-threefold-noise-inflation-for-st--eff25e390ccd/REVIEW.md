# Scientific review

**Correctness: PASS.** Independent exact-rational transition calculations confirm the three-state balance formulas and example for rational cases. The analytic proof bounds every trajectory into an invariant four-state set, identifies all recurrent classes, derives the stationary masses by balance and the mean, proves uniqueness and convergence, and establishes the strict sharp factor \(3\) by an exact derivative identity. The proof uses no numerical extrapolation or infinite enumeration. The mean and variance statements are normalized on the unit lattice.

**Originality: PASS, with residual risk.** The closest quantized-training source (Li et al. 2017, Theorem 5/Appendix F) studies an asymptotic regime with a genuinely random stochastic-gradient law, not the exact negative-slope deterministic-gradient iteration. Connolly et al. (2020/2021) concern rounding errors, Croci et al. (2022) survey error analysis, and Xia et al. (2025) study descent-oriented small steps. A published negative-slope floor-quantization theorem concerns deterministic periodic orbits. Related unpublished or unindexed three-state stochastic-rounding calculations may exist. No search outcome is treated as proof of uniqueness.

**Value: PASS.** A single natural parameter family of scalar quadratic descent steps receives a complete stationary-law classification with a sharp support threshold and global, scale-free noise-inflation bound. It identifies a practical distinction between conditional unbiasedness/mean contraction and excess stationary variance in oscillatory but stable quantized iterations. The finding deliberately does not claim a downstream high-dimensional theorem.

**Scope and reproducibility.** The only randomness is the one final unbiased lattice-rounding operation at each step; no floating-point intermediate errors are modeled. The exact argument works for all allowed real parameters. Run `python3 verify.py` to reproduce the finite exact-rational checks and inspect `verification_output.txt` for their recorded output. This is a self-review, not external certification.

Self-review: passed. Independent audit: not yet performed.
