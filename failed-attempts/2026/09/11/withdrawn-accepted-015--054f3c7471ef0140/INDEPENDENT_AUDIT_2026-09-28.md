# Independent Audit — 2026/09/11/015

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `01bd49c4acaca5c975eba2331a1d8d5435ce1b32`  
**Disposition:** **FAILED**

## Correctness

**Verdict:** FAIL

The record's finite Gaussian-envelope arithmetic is internally consistent as a bespoke overlap ratio, but that ratio is not the standard l^2 decoupling quantity. Its denominator is a sum of fourth powers of per-plate L^4 norms, whereas l^2 decoupling aggregates cap norms in an l^2 square sum before taking the p-th power. In addition, W_T are positive physical-space tube envelopes with no oscillatory phase or demonstrated Fourier localization to cone plates, so they are not by themselves admissible extension/wave-packet test functions for the decoupling inequality. Finally, a certificate at the single fixed scale R0=4096 cannot rule out an asymptotic epsilon/exponent improvement across scales. Thus R_*>=138.4 does not imply the stated conclusion that the old cone decoupling exponent is attained or that an epsilon-improvement is impossible.

## Originality

**Verdict:** FAIL

The exact 96-envelope configuration may be bespoke, but after removing the invalid decoupling implication it is only a custom finite-scale overlap construction. It does not establish an original theorem about cone decoupling. Bourgain-Demeter already formulate and prove the relevant l^2 cone decoupling framework; the audited record does not connect its custom ratio to that framework by a valid reduction.

## Scientific value

**Verdict:** FAIL

As a visualization of bush/plank overlap the construction may be pedagogically useful, but the research value claimed in the record depends on a sharpness implication that is not proved. The package therefore does not supply a scientifically valid obstruction to improved cone decoupling.

## Limitations

- The numerical lower bound concerns only the record's custom ratio at R0=4096.
- No admissible Fourier-localized test function or standard l^2 decoupling lower bound is supplied.
- A single scale cannot establish asymptotic exponent sharpness.

## Independent checks

- Recomputed the stated core and single-tube estimates and found no arithmetic issue decisive enough to rescue the implication.
- Compared the record's R_* denominator to the standard l^2-decoupling aggregation.
- Verified the assigned tree is unchanged through the checked commit and current main for the target path.

## Literature and comparison

- [Bourgain–Demeter, The proof of the l^2 Decoupling Conjecture](https://annals.math.princeton.edu/2015/182-1/p09): Primary cone-decoupling framework; the theorem is explicitly an l^2 decoupling result, so a sharpness certificate must address the standard l^2 cap aggregation and admissible frequency localization.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at the assigned tree. Git history comparison found no changes to this record between the assignment inventory, the dispatcher checked commit, and current `main`. No repository writes were made by this audit.
