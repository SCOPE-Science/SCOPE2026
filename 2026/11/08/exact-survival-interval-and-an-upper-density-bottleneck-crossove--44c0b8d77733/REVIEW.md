# Self-review

## Correctness — PASS
The exact identity \(F(x)=x[1-(x-\rho)^2/(1-\rho)^2]\) is independently checked symbolically. Its second factorization pins down the unique upper preimage \(s\), strict monotone global dynamics and the exact positive-fold basin. Reciprocal increments prove parabolic convergence. An arctangent summation, with a fixed small cutoff followed by a limit of that cutoff to zero, proves the \(\varepsilon^{-1/2}\) passage laws and initial-density crossover. A finite SymPy and orbit checker tests exact algebra and representative convergence but does not replace the universal proof.

## Originality — PASS, with historical-priority qualification
Pires, Andrade and Herrmann (arXiv:2606.05351v1) derive the GAL fixed-point fold and extinction/tricritical scaling; these facts are not new. Corral, Sardanyés and Alsedà (2018), Corral (2025), and Martin, Tang and Chialvo (2025) establish or study generic finite-time fold/bifurcation scaling, so the square-root slowing exponent and arctangent normal form are not claimed new. Vortkamp and collaborators (2020) document survival intervals and transients for a different Allee map. The inspected accessible complete works do not imply the exact fold cutoff \(s\), its survivor interval, and the nontrivial entry-layer profile with the derivative \(F'(s)\) for this GAL map. Only abstracts/partial text were accessible for some 2025 comparisons; further historical literature remains a risk.

## Mathematical value — PASS
There is a natural sharp global question at the published fold: which initial population densities survive, and how long do those immediately outside the basin appear to survive when the fold is removed? The complete physical basin and the explicit \(\sqrt\varepsilon\) crowding boundary layer distinguish full bottleneck residence from half residence and immediate extinction. This is stronger and more biologically interpretable than merely re-computing a known saddle-node exponent or a model-specific numerical constant.

## Limitations
Claims concern fixed strong-Allee parameters, a deterministic single population on \([0,1]\), and parameter approach from below. Finite tests and absence of indexed collisions do not certify global historical priority. External independent review has not occurred.

Self-review: passed. Independent audit: not yet performed.
