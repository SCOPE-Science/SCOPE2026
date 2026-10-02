# Independent audit — SCOPE-20260909-084

Audited at: 2026-09-30T23:18:42Z

Disposition: **failed**

## Correctness

**FAIL** — The reported numerical midpoints are plausible and the analytic truncation/Simpson majorants are carefully structured, but the package calls the intervals certified while its verifier uses ordinary binary floating-point evaluations of gamma, exp and cosine and then inserts a fixed 1e-7 allowance justified only by a heuristic “few thousand ulps” argument. There is no proved error bound for the underlying libm transcendental evaluations or directed-rounding interval arithmetic. The package itself states that the computation is not bit-verified interval arithmetic. Therefore the exact enclosure claim, as stated, is not proved by the supplied certificate.

Sources/evidence:
- Actual package artifacts/verify_sections.py and artifacts/verify_log.txt at the audited source revision.
- Independent inspection of the Simpson, Hermite and tail majorants and the unproved floating-point allowance.

Residual risks:
- The true values are very likely inside the printed intervals, but likelihood is insufficient for a claim of certified enclosure.
## Originality

**FAIL** — Even setting the certification gap aside, the six directional values are direct numerical specializations of the standard Fourier section formula. König’s open-access paper states the normalized section function, gives the same Fourier representation for arbitrary directions, records the known theorem that coordinate hyperplanes are minimal for p>2, and discusses numerical behavior at p=4 supporting main-diagonal maximality. The finite six-direction ranking is therefore covered as a routine evaluation of established machinery rather than a new implication.

### Originality comparison details

**Equivalent formulations.** The package’s psi-product integral is the p=4, n=5 specialization of the published general formula.
- König defines the same normalized section function and gives the general Fourier integral representation for every direction.

**Broader coverage.** The qualitative minimum component is already a theorem and the evaluated directions sit inside a pre-existing arbitrary-direction formula.
- König reports the Meyer–Pajor minimum theorem for coordinate sections and discusses p=4 numerical evidence for the main diagonal in the broader extremal problem.

**Exact database or table.** Originality is implication-based rather than wording/table-match based.
- No identical six-number table was found, but that absence does not overcome coverage by the general formula plus routine quadrature.

**Claim versus prior implication.** The six values require numerical evaluation but no new mathematical reduction beyond the established formula.
- König Proposition 2.1 gives the normalized section as a one-dimensional product Fourier integral for arbitrary a, exactly the framework specialized by the record.

### Source inspections
- **On maximal hyperplane sections of the unit ball of l_p^n for p>2** — BROADER_COVERAGE. Material read: Full open-access HTML, especially introduction, Proposition 2.1, and the p=4 numerical discussion. Evidence: General arbitrary-direction Fourier formula, coordinate-minimum prior theorem, and p=4 main-diagonal numerical motivation are all already present.

Originality residual risks:
- No identical printed six-direction table was located, but the stronger formula and routine-evaluation character are decisive under the requested originality standard.
## Scientific value

**FAIL** — A six-point numerical benchmark can be useful for calibration, but here it neither proves the global p=4 extremizer conjecture nor derives a new stability constant, cutoff, or structural lemma. Coordinate minimality is already known, diagonal maximality is already a motivated conjectural direction in the literature, and the remaining four values are routine evaluations. This falls below the requested value bar.

Sources/evidence:
- König’s full article frames the actual extremal problem and p=4 conjectural behavior.
- The package itself limits the result to a fallback six-direction table.

Residual risks:
- A rigorously certified table could still serve as reproducibility infrastructure, but that role alone is not a standalone mathematical contribution under the specified standard.

## Limitations

- The supplied floating-point certificate does not prove its claimed rigorous intervals.
- Even if numerically correct, the six-value table is a routine specialization of prior arbitrary-direction formulas.
