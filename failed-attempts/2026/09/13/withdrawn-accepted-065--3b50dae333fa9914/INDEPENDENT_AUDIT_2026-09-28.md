# Independent Audit — 2026/09/13/065

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `8550f23e03054c172fd4eab194bfa0f91dbf04cc`
- Disposition: **FAILED**

## Correctness

**FAIL** — The deposited geometric calculation appears to compute the standard second Seeley-DeWitt coefficient correctly: after the commutative reduction it obtains the integral of R/6-V and shows that integral is negative for nonzero a. The fatal issue is that RESULT.md defines the target coefficient by the displayed four-dimensional expansion Tr(e^{-t Delta_a}) = a0(a) t^{-2} + a2(a) + O(t^epsilon), i.e. a2 is the constant term. For a second-order Laplace-type operator in dimension four the heat expansion has powers t^{(n-4)/2}; the coefficient built from R/6-V is the n=2 coefficient and multiplies t^{-1}, while the constant term is the n=4 coefficient and involves curvature-squared/potential-squared and derivative terms. Therefore the negative integral proved in the record does not determine the a2 that RESULT.md itself places at order t^0. The proof answers a different coefficient-normalization question from the literal admitted target.

## Originality

**PASS** — The specific opposite-warp quantum-torus reduction, the fiberwise phase-gauge argument for theta-independence, and the exact all-a sign calculation for the standard t^{-1} heat coefficient are specialized computations not supplied by the general scalar-curvature and noncommutative-torus references. That narrower computation appears original as an example even though it is attached to the wrong coefficient in the stated target.

## Scientific value

**FAIL** — As deposited, the result does not resolve the coefficient it defines. A scientifically useful repair would have to either change the target/expansion explicitly to the standard t^{-1} coefficient or compute the true constant (a4) coefficient. Because neither repair is present and changing the target is not an audit-side scientific edit, the current record cannot be validated.

## Sources

- Heat Trace Asymptotics on Noncommutative Spaces (Dmitri V. Vassilevich): https://arxiv.org/abs/0708.4209 — Review of heat-kernel asymptotics for generalized Laplacians on noncommutative spaces.
- Heat kernel expansion: user's manual (Dmitri V. Vassilevich): https://arxiv.org/abs/hep-th/0306138 — Standard Laplace-type heat expansion: in dimension four the a2/second Seeley-DeWitt invariant occurs at t^{-1}, while the constant term is a4.
- Scalar curvature for noncommutative four-tori (Farzad Fathizadeh; Masoud Khalkhali): https://arxiv.org/abs/1301.6135 — Background for noncommutative four-torus scalar-curvature/heat-coefficient computations.

## Limitations

- The audit does not reject the symbolic curvature identity R=2 e^{2f}(-f''-3(f')^2) or the integration-by-parts negativity argument for the standard t^{-1} coefficient.
- If the original target intended the conventional a2 coefficient and RESULT.md merely omitted an explicit t^{-1} factor, that external target text would be needed to justify a repair; the deposited record itself is internally inconsistent.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first; Oxford Download was not needed.
