# Scientific review

## Correctness

**PASS.** The argument starts from the published Gessel–Lucas congruence for the Franel sporadic Apéry-like sequence, separately validates its applicability to the prime \(29\), and computes the complete digit-root and derivative tables by exact integer recurrence. The one-digit zero set is precisely \(\{12,14,16\}\); the normalized correction is \(c_d+m b_d\), with roots \(17,14,11\). For unique-zero-digit indices, the middle possibility forces a second zero digit and is excluded. Digit counting gives the claimed exact length law; `verify.py` independently reproduces the finite table and checks a finite index range. The unrestricted conclusion follows from the published congruence, not from the finite experiment.

## Originality

**PASS, with bibliographic risk.** The strongest prior result is Straub's 2023 general Gessel–Lucas theorem; it supplies the two-state congruence but does not state the specialized \(29\)-adic valuation language or frequencies. The 2014 Schulte–VanSchalkwyk–Yang report identifies prime \(29\) as type III by a single index and fully treats the first valuations for primes \(5,7,13\), not for \(29\). Published related recurrence and digit-language results, and semantically similar research records, were compared for logical coverage. An unindexed instance-specific classification might still exist; this is not a proof of universal priority.

## Value

**PASS.** The smallest odd type-III prime was identified in the motivating Franel valuation classification but lacked an explicit first-shell law there. The new result gives the complete infinite index language and exact finite-depth frequencies, including two surprising higher-neighbor obstructions that invalidate counting forbidden digits alone. This is a natural structurally motivated boundary of the earlier type-II digit-count pattern, not an arbitrary numerical slice; it makes no claim about the uncomputed higher valuation levels.

Self-review: passed. Independent audit: not yet performed.

