# Independent audit — 2026-10-01

## Final claim

For the explicit smooth quarter-turn skew-product cocycle, the ordered-product spectral-radius rate is zero at every odd horizon and \(\log s\) at every even horizon despite a strict Lyapunov gap, while a smooth rotating-frame conjugacy changes the finite-horizon rate to \(\log s\) at every horizon.

## Correctness — PASS

The assigned construction is mathematically correct. Along the invariant circle the fiber product telescopes to \(R_{\theta+L\pi/2}D^L R_{-\theta}\). For odd \(L\), the quarter-turn factor makes the fiber eigenvalues have modulus one; for even \(L\), the spectral radius is \(s^L\). The singular values are \(s^L\) and \(s^{-L}\) at every horizon, and the rotating-frame conjugacy makes the cocycle constant. An independent numerical replay for \(s=1.7\) and horizons one through eight reproduced the parity law, singular-value growth, and conjugacy mechanism. The finite computation is corroborative; the proof is the exact matrix identity.

Checked sources:
- Assigned package RESULT.md and its verifier at the assigned Git snapshot.
- Published 2026-09-18 finding: Ordered-product spectral growth need not converge to the top Lyapunov exponent, complete RESULT inspected.
- Published 2026-09-19 finding: Spectral-radius parity obstruction to ordered-product Lyapunov convergence, complete RESULT inspected.
- N. Martínez Ramos, Asymptotic behavior of the spectral radius of locally constant strongly irreducible cocycles, arXiv:2507.19624.
- D. Sornette, V. R. Saiprasad, V. Troude, A New Route to Chaos through the Geometric Composition of Non-Normal Amplification, arXiv:2609.18017v1; abstract/bibliographic material inspected, full PDF unavailable in this run.

Residual risks:
- None.

## Originality — FAIL

Originality fails decisively. A public finding dated 2026-09-18 already gives a smooth period-four cocycle with exact parity nonconvergence, a simple top Lyapunov exponent, an endpoint-transversality explanation, and the same moving-frame/coordinate-dependence mechanism. Its co-rotating frame turns the cocycle into a constant diagonal cocycle, exactly the structural phenomenon claimed here. The assigned theorem is therefore a cleaner specialization, essentially the symmetric-exponent case in which the odd-horizon rate becomes zero, not a new implication-level result.

### Equivalent formulations

Searches:
- Published-record semantic query: spectral radius growth nonconvergence smooth cocycle conjugacy endpoint frame mismatch Lyapunov
- Complete 2026-09-18 RESULT comparison
- Complete 2026-09-19 RESULT comparison

Evidence:
- The 2026-09-18 result has \(h_{2k}=a\), \(h_{2k+1}=(a+b)/2\), a periodic endpoint-transversality criterion, and explicit frame dependence.
- The 2026-09-19 result independently supplies a smooth exact parity obstruction and singular-value repair.

Reasoning: The assigned \(h_{\rm odd}=0\) law is obtained from the earlier period-four construction by choosing opposite fiber exponents; the endpoint-frame explanation and coordinate non-invariance are already explicit.

### Broader coverage

Searches:
- 2026-09-18 source-specific correction
- Martínez Ramos cocycle literature

Evidence:
- The 2026-09-18 result is at least as broad on the source-specific correction mechanism and strictly broader in allowing arbitrary \(0<b<a\) before a simple specialization.
- General failure of spectral-radius limits is also acknowledged as older cocycle theory.

Reasoning: The earlier source-specific theorem dominates the central correction; older cocycle theory supplies broader background.

### Exact database or table

Searches:
- Exact parity-law comparison of 2026-09-18 and assigned formulas

Evidence:
- Earlier formula \(h_{2k}=a\), \(h_{2k+1}=(a+b)/2\); assigned formula \(h_{2k}=\log s\), \(h_{2k+1}=0\).

Reasoning: Setting the earlier exponents to \(a=\log s\) and \(b=-\log s\) yields the assigned parity values at the level of the spectral-rate claim.

### Claim versus prior implication

Searches:
- Full 2026-09-18 RESULT
- Assigned RESULT

Evidence:
- The earlier finding already states that moving endpoint frames do not act by similarity and that a co-rotating frame changes the finite-horizon spectral radius while leaving Lyapunov exponents unchanged.
- The assigned result re-expresses that mechanism with a circle skew product and a block-orthogonal conjugacy.

Reasoning: The final claim is a covered special case/repackaging under the required implication standard.

### Source inspections

- **Ordered-product spectral growth need not converge to the top Lyapunov exponent** — Decisive prior coverage of parity nonconvergence, endpoint transversality, and frame dependence. Material read: Complete RESULT.md. Method: Published finding full-text inspection. Evidence: It gives a smooth period-four telescoping cocycle, exact even/odd rates, and a co-rotating frame in which the finite-horizon rate is constant.
- **Spectral-radius parity obstruction to ordered-product Lyapunov convergence** — Additional overlapping coverage; not needed for the decisive rejection. Material read: Complete RESULT.md. Method: Published finding full-text inspection. Evidence: It gives a smooth period-two exact parity law and a singular-value repair.
- **A New Route to Chaos through the Geometric Composition of Non-Normal Amplification** — Not used for whole-document novelty conclusions because full text was unavailable; decisive coverage comes from the earlier published findings. Material read: Abstract/bibliographic material; the full preprint PDF was unavailable in this run. Method: Primary-source abstract inspection after direct full-text attempt. Evidence: The assigned package and earlier public corrections target the same ordered-product spectral-radius statistic.

Checked sources:
- Assigned package RESULT.md and its verifier at the assigned Git snapshot.
- Published 2026-09-18 finding: Ordered-product spectral growth need not converge to the top Lyapunov exponent, complete RESULT inspected.
- Published 2026-09-19 finding: Spectral-radius parity obstruction to ordered-product Lyapunov convergence, complete RESULT inspected.
- N. Martínez Ramos, Asymptotic behavior of the spectral radius of locally constant strongly irreducible cocycles, arXiv:2507.19624.
- D. Sornette, V. R. Saiprasad, V. Troude, A New Route to Chaos through the Geometric Composition of Non-Normal Amplification, arXiv:2609.18017v1; abstract/bibliographic material inspected, full PDF unavailable in this run.

Residual risks:
- The primary source full PDF was unavailable, but this does not affect the originality rejection because the earlier 2026-09-18 coverage is decisive.

## Scientific value — FAIL

The mathematical mechanism is useful, but the assigned contribution does not leave a substantive new gap after the 2026-09-18 result: parity nonconvergence, endpoint transversality, moving-frame dependence, and the singular-value distinction were already established in a stronger source-specific form. The cleaner special case is not independently valuable enough under the required bar.

Checked sources:
- Assigned package RESULT.md and its verifier at the assigned Git snapshot.
- Published 2026-09-18 finding: Ordered-product spectral growth need not converge to the top Lyapunov exponent, complete RESULT inspected.
- Published 2026-09-19 finding: Spectral-radius parity obstruction to ordered-product Lyapunov convergence, complete RESULT inspected.
- N. Martínez Ramos, Asymptotic behavior of the spectral radius of locally constant strongly irreducible cocycles, arXiv:2507.19624.
- D. Sornette, V. R. Saiprasad, V. Troude, A New Route to Chaos through the Geometric Composition of Non-Normal Amplification, arXiv:2609.18017v1; abstract/bibliographic material inspected, full PDF unavailable in this run.

Residual risks:
- None.

## Conclusion

The finding is scientifically rejected because all three axes must pass. Correctness evidence is preserved, but the final claim fails the required originality and scientific-value standards.
