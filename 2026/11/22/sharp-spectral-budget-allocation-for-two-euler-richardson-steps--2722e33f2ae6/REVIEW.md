# Self-review

## Correctness — PASS

The claim uses a strict spectral interval \(0<\mu<L\), nonnegative real step lengths with fixed sum, and the robust worst-case norm over the complete interval. The exact product reduction is reversible, the minimax crossing is unique by pointwise strict monotonicity, and convexity in the spectral variable exhausts all active extrema. The explicit threshold ordering and two positive-root identities prove the entire piecewise formula, not merely candidates from differentiation. The final nonexpansion horizon is derived from the active equioscillation constraints, with strict inequalities between boundaries. The separate checker confirms 1,886 scalar minimizations, exact rational balances and eight critical stability horizons. Finite checks corroborate the analytic argument but are not substitutes for it.

## Originality — PASS, with qualifications

The most relevant earlier framework is the Chebyshev minimax residual polynomial discussed by Agarwal–Goel–Zhang (2021) and Takabe–Wadayama (2020). That unrestricted degree-two optimum fixes exactly one total step sum, whereas this theorem optimizes **every** externally prescribed sum and specifies four further non-Chebyshev regimes. The published stagewise-safe Richardson frontier enforces individual nonexpansivity rather than a fixed sum and gives a different feasible set. Classical real-axis Chebyshev stability optimization covers the large-condition-number endpoint of the stability corollary, which is explicitly not claimed independently as a novel generic result. Rack–Vajda's discussion of Zolotarev's first problem involves prescribed leading coefficients, unlike the prescribed constant and linear coefficients here. The complete conditional-sum optimizer and small-condition-number frontier have not been located in the inspected sources. Historical equivalents in specialist constrained polynomial approximation remain a residual risk.

## Value — PASS

In explicit two-stage diffusion integration or scheduled quadratic relaxation, the total elapsed integration/relaxation parameter can be externally fixed while the two steps may be allocated freely. The result gives the entire robust best allocation, identifies when one full step is better than two positive steps, and shows where the worst spectral mode migrates from an endpoint to the interior and back. The sharp safe horizon can be twice that of equal stepping for \(\kappa\ge2\), and can be much larger for nearly flat spectra, even though individual steps may be expansive. These are operationally meaningful stability facts beyond an arbitrary chosen numerical constant. They do not imply better accuracy, noise robustness, or intermediate-stage stability.

## Evidence and limitations

The primary full-text comparisons cover the residual-polynomial and Chebyshev method sections of Agarwal–Goel–Zhang (2021) and Takabe–Wadayama (2020), plus the classical iteration treatment of Schöberl. A published-result search of constrained approximations and the related source on Zolotarev polynomials was also made. The potential existence of an equivalent classical weighted-polynomial theorem is not excluded. Scientific verification here is same-model only.

Self-review: passed. Independent audit: not yet performed.
