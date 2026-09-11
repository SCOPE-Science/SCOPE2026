# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — WITHDRAWN (superseded by output/target_exit.json, CLEAN_EXIT)

The earlier TARGET character construction claimed in Sec. 4 of a previous
version of this file is FALSE and is hereby withdrawn. It is preserved only
as a record of the blocked route; it is not claimed.

- Fatal flaw: the forward-cone corner `c_j A_j c_j ≅ M_{k_j}(C(Y_j))` with
  `k_j ≥ 24 > 1` admits no unital *-homomorphism to `C` (matrix-unit proof:
  a unital homomorphism out of `M_n`, `n > 1`, would force `1 = 0`).
  The same kills any unital `χ_j : A_2 = M_24(C(X_2)) → C`.
  Hence the designed point-fiber evaluation is the zero map, not a character.
- Fallback binary test also fails: gap arithmetic `(6−2)/24 = 1/6` verifies,
  but the Euler obstruction was argued over the wrong base (`X_1`, dim 6,
  vs stage-2 projections over `X_2`, dim 26) and Cuntz persistence to
  `Cu(W_fast)` plus the `< 1/24` tail-distortion budget were never closed.

Final outcome: NO_RESULT via CLEAN_EXIT. See `output/target_exit.json`
and `output/research_report.json`. The replayable stage/rho script
`output/artifacts/verify.py` (VERIFY_OK) is retained only as arithmetic
audit, not as a theorem about `W_fast`.
