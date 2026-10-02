# Review status

Independent audit date: 2026-10-01 UTC

Disposition: **failed**.

- Correctness: **PASS** — The determinant-sum reduction is correct for zonotopes. Independent exact enumeration reproduced the C_n values S0,S1,S2,N for n=4,5,6, including N=1528320, 815212800 and 663997432320. An independent exact Fraction/Bareiss replay of the F4 construction reproduced S0=159, S1=1032, S2=4680 and N=218592. The support-function comparisons also show the short- and long-root zonotopes are not homothetic. The core strict-deficit claims are therefore correct; the phrase 'extremal witness' is misleading terminology because the computed deficits are strict, not equality/extremal cases.
- Originality: **PASS** — Best-of-knowledge searches found the standard root-zonotope literature and the general Alexandrov-Fenchel equality theory, but no prior source tabulating these exact C4/C5/C6/F4 short-versus-long mixed-volume deficits. The exact finite values appear new as computations, although originality does not by itself establish value.
- Scientific value: **FAIL** — The final result consists of four small-rank evaluations of the standard zonotope determinant-sum formula. The package does not motivate n=4,5,6 or the F4 row as a sharp cutoff, classification boundary, unknown invariant needed downstream, or obstruction to a conjecture. Once the generators are specified, the values are mechanically enumerable. Correctness and best-of-knowledge novelty therefore do not supply the substantive mathematical reason required by the shared value standard.

The detailed source comparisons and residual risks are recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
