# Independent audit — wall-concentrated restriction datum
- Record: `2026/09/10/010`
- Audited tree: `81607455e62c9e1c78af604006a637a42af066a3`
- Audited branch/commit: `main` / `e96707428e1608ae0287a471173e57e9f975206d`
- Disposition: **FAILED**

## Correctness

**FAIL**

- The record states that because the five frequency discs are centered on xi1=0, every tube direction has zero first component and every centerline remains in the wall plane x1=0. This is false for the actual radius-0.2 discs: they include frequencies with xi1!=0. The committed subcap census itself contains xi1=+/-0.1 centers and directions with nonzero first component.
- The reported fine rho=0.9701 is not an integral over all of B_100: verify_fan_rho_fine.py truncates x1 to [-30,30] and uses finite Riemann grids/cap quadrature. No rigorous enclosure of the omitted region or quadrature error is present in that verifier. Therefore the exact full-ball energy-ratio inequality is not proved by the archived computation.
- Even if the numerical wall concentration is qualitatively correct, 'available single-step power gain 0' is not a mathematical consequence of a decoupling constant being at least one, an endpoint theorem being unavailable, or one prescribed route failing to produce delta=0.02. Those observations do not prove that every admissible single-step argument has zero gain.
- These are load-bearing issues for the headline 'blocking' certificate, not merely presentation defects.

## Originality

**FAIL**

- Polynomial-partitioning restriction arguments already split into cellular and wall/tangential cases, and tangential wave-packet concentration near an algebraic wall is a standard phenomenon in Guth's framework and its successors.
- The specific finite choices R=100, D=3, P=x1*x2*x3, five discs, custom N/B threshold and quadrature table are engineered parameters. Without a rigorous new theorem showing an extremal obstruction, the table is not a substantively new mathematical object.

## Scientific value

**FAIL**

- The record does not refute the target restriction inequality and does not establish a theorem that a specified class of one-step arguments cannot improve the exponent.
- A non-rigorous finite-scale numerical example of standard tangential concentration can be exploratory diagnostics, but it is not sufficient as an accepted scientific finding under the record's stronger 'blocking' headline.

## Reproducibility and source checks

- Inspected fallback_certificate.py and verify_NB_W.py: they generate 5/5 and 25/25 wall-bound counts under their own sampling protocol.
- Inspected verify_fan_rho.py and verify_fan_rho_fine.py: both use finite frequency and spatial quadrature; the fine computation truncates x1 to [-30,30].
- Verified directly from gdir in the committed code that xi1=+/-0.1 subcaps have nonzero first direction component, contradicting the universal x1=0 centerline rationale.
- Checked the headline logical step from numerical concentration to impossibility of a single-step gain; the cited general restriction results do not supply that implication.

## Literature comparison

- [A restriction estimate using polynomial partitioning](https://doi.org/10.1090/jams827): Guth's polynomial-partitioning method for restriction in R^3 is the foundational prior framework in which cellular versus wall/tangential wave-packet behavior is treated; tangential concentration is therefore not itself a new phenomenon.
- [Weighted restriction estimates using polynomial partitioning](https://doi.org/10.1112/plms.12046): Shayya develops further restriction estimates using Guth's polynomial-partitioning framework, reinforcing that wall/tangential cases are standard analytical structure rather than a new finite-scale mechanism.

## Limitations

- The finite-scale computations are not interval-certified.
- The failure finding concerns the claimed rigorous obstruction/blocking interpretation, not the usefulness of the scripts as exploratory numerical diagnostics.
- The audit does not assert that the reported approximate rho is numerically wrong; it finds that it is not a rigorous certificate of the stated full-ball ratio.
- A repaired exploratory note could retain the numerical experiment, but that would not cure the originality/value failure of the accepted research claim.

## Publication decision

The record is scientifically rejected and should be relocated atomically, with its complete existing package preserved, to `failed-attempts/2026/09/10/withdrawn-accepted-010--a2e0a6b6d6568757`. This audit adds evidence and a `FAILED_ATTEMPT.md` marker before relocation. No GitHub change is claimed as already applied.
