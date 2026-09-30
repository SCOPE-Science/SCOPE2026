# Independent Audit — 2026/09/12/047

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `d58c42a00798b8379728b2812c9402c9e1beeb93`
- Disposition: **FAILED**

## Correctness

**PASS** — The scaling counterexample is mathematically sound. With p=N^(-5/12), q^2=Np=N^(7/12), the normalized fourth cumulant tends to a nonzero constant and the known sparse-edge correction is order q^(-2)=N^(-7/12). Multiplication by N^(2/3) produces the divergent exponent 2/3-7/12=1/12, so a statistic centered rigidly at 2 cannot have a tight Tracy-Widom limit.

## Originality

**FAIL** — Lee-Schnelli's 2016 paper already states in its abstract that sparse random matrices exhibit Tracy-Widom fluctuations only after inclusion of a deterministic sparsity-induced spectral-edge shift, and for Erdos-Renyi identifies a shift of order (Np)^(-1). The record selects an admissible power-law p and plugs that standard shift into N^(2/3) scaling. This is a direct specialization of the cited prior mechanism rather than a new edge phenomenon.

## Scientific value

**FAIL** — The explicit exponent arithmetic is a useful sanity check, but the headline merely demonstrates that omitting a known deterministic sparse-edge correction breaks a fixed-centering formulation. It does not establish a new universality regime, correction term, or quantitative theorem beyond the existing sparse-edge result.

## Sources

- Local law and Tracy-Widom limit for sparse random matrices (Ji Oon Lee; Kevin Schnelli): https://arxiv.org/abs/1605.08767 — Abstract: Tracy-Widom fluctuations hold when a deterministic sparsity-induced edge shift is included; for Erdos-Renyi the shift is order (Np)^(-1).

## Limitations

- This audit accepts the record's stated cumulant expansion and does not claim the counterexample computation is false.
- The rejection concerns originality and value relative to the known sparse-edge shift theorem.

GitHub was read only as evidence; no repository mutation was performed in this audit chat.
