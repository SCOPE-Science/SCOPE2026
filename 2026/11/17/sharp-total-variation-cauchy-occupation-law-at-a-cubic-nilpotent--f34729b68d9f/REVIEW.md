# Mathematical review: sharp total-variation occupation law

## Correctness — PASS

The polynomial flow with \(P(x)=1+\gamma x+\alpha x^2\) and \(\alpha>\gamma^2/4\) has exact first integral \(H=y^2/2+\int_0^x t^3/P(t)\,dt\). Positivity of \(P\), monotone branches of the potential and its quadratic growth establish one global periodic oval per positive energy. The time density and period formulas retain original physical time. The energy-shell change of variables gives \(W(v)=|x_-(v)|^{-3}+x_+(v)^{-3}=c v^{-3/2}+O(v^{-2})\), with \(c=1/(\sqrt2\alpha^{3/2})\). Splitting off this tail and integrating its Abel transform exactly proves \(J(E)-C=O(\log E/E)\), where \(C=2\pi/\sqrt{4\alpha-\gamma^2}\). The normalized-density comparison proves \(d_{\mathrm{TV}}=2c/(C\sqrt E)+O(\log E/E)\) without needing numerical extrapolation. The accompanying standard-library checker passed after extraction from the proposed contents, but its finite samples are only diagnostics.

## Originality — PASS within accessible evidence

The closest primary article, Corbera–Valls (2024), classifies existence of global nilpotent centers in a cubic family containing this subfamily. The inspected abstract, equations (3) and (5), Theorem 2, proof sections, appendices and references do not give the claimed time-occupation density or the total-variation asymptotic. The companion 2024 article studies systems reversible with respect to the other axis. Dias–Llibre–Valls (2018) classifies canonical polynomial Hamiltonian phase portraits rather than this noncanonical time sampling. Previously published records involving Cauchy occupation for a *different* cubic center with restoring force linear in position have logarithmic, not algebraic, convergence scales, and do not imply this formula. Searches by exact equations, total variation, equivalent Abel formulations and period asymptotics identified no direct covering theorem. A general Abelian asymptotic result might reduce part of the proof, and unindexed equivalent results cannot be excluded; there is no claim of independent priority certification.

## Value — PASS

The original classification isolates a natural whole coefficient region of nilpotent global centers but does not quantify high-energy time statistics. A total-variation limit controls all measurable observables, significantly stronger than weak convergence. The asymmetry coefficient changes the *location and scale* of the limiting Cauchy law while the exact quantitative error has a discriminant-dependent prefactor; the event outside the dynamically accessible interval attains the sharp first-order error. The exact physical-period coefficient and its substantially smaller correction isolate the Abel cancellation that determines the rate. This is a motivated analytical characterization across a complete open parameter region, not a single numerical example.

## Closest literature and limitations

The primary article is M. Corbera and C. Valls (2024), Results in Mathematics 79, article 129, DOI 10.1007/s00025-024-02163-x, first publicly available 2024-04-13. See also F. S. Dias, J. Llibre and C. Valls (2018), DOI 10.1016/j.matcom.2017.06.002, and Corbera–Valls (2024) on the opposite reversibility axis, DOI 10.1007/s12215-024-01046-y. The theorem is for fixed \(\alpha>\gamma^2/4\), \(\gamma\ne0\); neither uniformity near the boundary nor the finite-energy exact maximizer is claimed. Mathematical priority is subject to a further human literature assessment.

Self-review: passed. Independent audit: not yet performed.
