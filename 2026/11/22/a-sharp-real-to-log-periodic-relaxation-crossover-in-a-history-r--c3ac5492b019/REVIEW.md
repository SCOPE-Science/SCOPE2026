# Scientific review: a sharp real-to-log-periodic relaxation crossover

## Correctness — PASS

The physical Bloch generator has a real mode at \(-2\kappa\) and a complex pair at \(-\kappa\pm i\sqrt{\omega^2-\kappa^2}\) for \(\omega>\kappa>0\). The exact uniform-history Volterra equation for each mode reduces to the regular confluent hypergeometric equation, with a nonzero leading coefficient for each eigenmode. Taking real parts gives the two exact late-time decay exponents. The difference has the sign of \(\omega^2-2\kappa^2-\kappa q\) for every \(q>0\), proving the complete switching classification, strictness, uniqueness and no-transition boundary. The proof explains why a nonzero initial projection is required in each mode. The standalone symbolic and numerical checks agree with the independent original Volterra system; they are supplementary rather than a replacement for the all-parameter proof.

## Originality — PASS, with publication-priority risk

The closest primary paper, de Mauro–Kulkarni–Majumdar (arXiv:2608.02297), establishes uniform-history Kummer dynamics for closed quantum systems, and explicitly identifies open quantum systems as a future direction. This calculation credits its scalar method. The other checked full texts treat real-spectrum classical preferential relocation (Boyer–Evans–Majumdar, arXiv:2411.00641) and fixed-state open quantum resetting (Rose–Touchette–Lesanovsky–Garrahan, arXiv:1806.01298). Their theorems do not imply the positive-rate competition between distinct real and complex Lindblad eigenmodes. Semantic-index comparisons identified uniform-history quantum decay and unrelated dephasing spectral optimizations, but none with the same Lindblad-memory phase boundary. An unindexed equivalent open-system result is still possible, and the Carollo–Wald reference was assessed at abstract level rather than exhaustively.

## Value — PASS

For the smallest open system with competing real and complex decay modes, the result gives a complete physically interpretable threshold and a concrete log-frequency. It identifies when the slowest polarization changes from monotone algebraic decay to logarithmically oscillatory decay although the stationary state is unchanged. This structural prediction is neither an exercise in ordinary Lindblad eigenvalue ordering nor a small improvement to an existing numerical constant: uniform-history resetting nonlinearly maps each complex eigenvalue into an algebraic exponent, changing its relative decay rank. It is an idealized analytical benchmark, not a general theorem for arbitrary dissipators.

## Scientific limitations

The theorem requires nonzero initial projections in both sectors, \(\omega>\kappa>0\), and \(q>0\). It does not cover exceptional points, \(q=0\), nonuniform resetting, arbitrary Lindbladians or experimental noise. Proof details and exact reproduction steps are in `RESULT.md`, `VERIFICATION.md` and `check.py`.

Self-review: passed. Independent audit: not yet performed.
