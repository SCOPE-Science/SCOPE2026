# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260914-011`

Disposition: **FAILED**

## Correctness — PASS

The package contains six positive-imaginary-part Krawczyk shape boxes whose stored Krawczyk images lie strictly inside them. The verifier source constructs the stated filling and checks the full logarithmic gluing system before propagating the certified intervals through the cusp cross-section. The stored enclosure \(0.4654775688468905<\operatorname{Re}(\theta_6)<0.4654775688495280\) and \(1.1939928091790021<\operatorname{Im}(\theta_6)<1.1939928091826787\) is outside both proposed band bounds. The runtime lacked the same topology package, so the computation was not independently re-executed end-to-end, but the committed interval data, verifier logic, slope setup, and strict inclusions were inspected and found internally consistent.

## Originality — PASS

The magic-manifold filling classification and general cusp-shape deformation literature do not give this filled cusp-modulus enclosure. Exact-value searches found no independent table containing the same value, so the certified numerical counterexample is best-of-knowledge original.

## Scientific value — FAIL

The package certifies one counterexample to a numerical band, but it does not identify an external theorem, natural extremal threshold, asymptotic boundary, or other mathematical reason for the particular band constants. With only one family member certified and no broader mechanism extracted, the result does not pass the required scientific-value bar despite the careful certification.

## Literature and prior-coverage checks

- **Dehn filling of the magic 3-manifold** — https://arxiv.org/abs/math/0204228. not exact coverage: The work classifies non-hyperbolic fillings but does not report this cusp modulus.
- **Cusp shapes under cone deformation** — https://doi.org/10.4310/jdg/1226090484. general bounds, not exact coverage: The work bounds changes in cusp shape under cone deformation rather than tabulating this filling.
- **SnapPy manifold documentation** — https://snappy.computop.org/manifold.html. method support only: The documentation confirms s776 is a built-in manifold and describes cusp computations; it does not give the filled n=6 value.

## Limitations and residual risk

- The scientific rejection is for insufficient motivation/value, not because the interval counterexample was found false.
- A second independent interval-library/SnapPy rerun was unavailable in this runtime.
- End-to-end rerun of the SnapPy-dependent certificate was unavailable in the audit runtime; correctness rests on independent inspection of the committed interval certificate and verifier logic rather than a second SnapPy execution.
