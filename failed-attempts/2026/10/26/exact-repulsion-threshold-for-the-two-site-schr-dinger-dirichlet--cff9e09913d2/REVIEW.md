# Independent mathematical audit

## correctness

PASS

The primary source's t is the frozen g, and its Hamiltonian convention is i times the time derivative equals twice the Wirtinger energy gradient. The displayed functional and Eq. (51) are consistent with those two normalizations. Independently, at fixed b=|y|² the nonnegative quartic deficit in RESULT.md lines 55–66 is the sum of (a−c)²/8, b(√a−√c)²/2, and the loss from the maximum phase term. For a balanced, phase-matched state with a=c, the energy is −μ−g/4+(U−2g)a+(7g/2)a² for 0≤a≤1/2. Its constrained minimum and all equality conditions give the stated populations, energy and unique ray above and at threshold. Linearizing Eq. (51) in the frame rotating at 2μ+g gives the transverse block with diagonal ±(U−g) and off-diagonals −g,g. Its square is U(U−2g)I; hence −i times this block has a positive real eigenvalue precisely for 0<U<2g, and the block is nonzero nilpotent at equality. Tracing over the other site gives the occupation probabilities as eigenvalues and hence the claimed entropy and expansion. This checks the formulas algebraically; verification.py was inspected, not executed; its recorded finite checks are supplementary. No nonlinear stability or particle entanglement is implied.

## originality

FAIL

The principal constrained optimization is mechanically covered, not just related by a single endpoint. Fransson–Sowa give the U-dependent Hamiltonian at Eq. (51), and Appendix VII.C explicitly performs phase alignment and balance on every fixed outer-occupation slice, and prints the resulting quartic polynomial. The U term is constant on each such slice. Adding it to the prior reduced polynomial and clipping its vertex gives the whole positive-U minimizer classification, and its entropy then follows from the same populations. The exact rotating-frame spectrum is not claimed to be printed in the source, but is a separate elementary first-order calculation directly from its displayed ODE. The failure is on the principal submitted claim and does not assert that the precise spectrum was previously published.

## value

FAIL

An exact matched variational and dynamical threshold would be useful if it required a distinct result for this finite model. Here the main positive-U diagram is the clipped vertex of the prior slice polynomial after adding the already specified linear occupation term. The entropy is a partial trace of those same populations, and the remaining transverse calculation is the first-order spectrum of the 2×2 block at a stated pure occupation in the prior equations. The submission does not establish a distinct dynamical or entanglement result beyond these direct calculations, such as nonlinear behavior at the degenerate orbit. This assessment does not discount finite exact thresholds in general.

The dated certificate retains the supplied scientific assessment, sources and limitations.
