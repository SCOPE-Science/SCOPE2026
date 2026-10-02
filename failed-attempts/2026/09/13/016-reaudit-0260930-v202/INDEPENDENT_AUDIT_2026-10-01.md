# Independent audit — 2026-10-01

## Final claim

For C_n at n=4,5,6 and for F4, the specified short- versus long-root zonotopes have the stated positive exact Alexandrov-Fenchel determinant-sum deficits.

## Disposition

**failed**

## Correctness — PASS

The determinant-sum reduction is correct for zonotopes. Independent exact enumeration reproduced the C_n values S0,S1,S2,N for n=4,5,6, including N=1528320, 815212800 and 663997432320. An independent exact Fraction/Bareiss replay of the F4 construction reproduced S0=159, S1=1032, S2=4680 and N=218592. The support-function comparisons also show the short- and long-root zonotopes are not homothetic. The core strict-deficit claims are therefore correct; the phrase 'extremal witness' is misleading terminology because the computed deficits are strict, not equality/extremal cases.

## Originality — PASS

Best-of-knowledge searches found the standard root-zonotope literature and the general Alexandrov-Fenchel equality theory, but no prior source tabulating these exact C4/C5/C6/F4 short-versus-long mixed-volume deficits. The exact finite values appear new as computations, although originality does not by itself establish value.

### Equivalent formulations

Equivalent formulations use coefficients of the volume polynomial of Z_short+t Z_long or transversal determinant sums; no exact prior values were located.

### Broader coverage

Broader theory makes the computation routine but does not itself furnish the four exact rows.

### Exact database or table

This is a best-of-knowledge originality PASS for the numerical rows only.

### Claim versus prior implication

The rows are computational consequences of standard formulas, not quoted prior values; this weak form of originality is separated from the failing value assessment.

## Scientific value — FAIL

The final result consists of four small-rank evaluations of the standard zonotope determinant-sum formula. The package does not motivate n=4,5,6 or the F4 row as a sharp cutoff, classification boundary, unknown invariant needed downstream, or obstruction to a conjecture. Once the generators are specified, the values are mechanically enumerable. Correctness and best-of-knowledge novelty therefore do not supply the substantive mathematical reason required by the shared value standard.

## Checked sources

- https://doi.org/10.1007/s00031-008-9031-z
- https://arxiv.org/abs/2011.04059
- Resultary published-findings semantic search

## Residual risks and limitations

- The repository's n=6 script uses rounded floating determinants with a tracked deviation plus exact spot checks; the independent re-enumeration reproduced its aggregate values.
- The exact values could exist in specialized computational tables not indexed by the searches performed.

The exact finite determinant sums are reproducible, but the selected small-rank rows are routine evaluations of the standard zonotope polarization formula and are not motivated as a natural cutoff, classification, or independently needed invariant.
