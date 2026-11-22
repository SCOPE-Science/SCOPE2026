# Review of the finite-size deficiency-mark law

## Correctness: PASS
For each permitted part \(u_j\), the marking event is counted exactly by removing mandatory copies from smaller parts, fixing its actual multiplicity, and excluding any additional copies of that part; summing yields formula (1) in RESULT.md. The individual mark-generating functions telescope exactly to the ordinary \(\ell\)-regular partition generating function. The difference of two marked probabilities is evaluated **before** asymptotic extraction, avoiding the invalid subtraction of two uncontrolled single-mark \(o(1)\) terms. A Gaussian lattice sum supplies the \(t^{1/2}\) factor, and Euler-product saddle localization gives the corresponding \(n^{-1/4}\) coefficient. The constant and its dependence on \(\ell,s\) agree with exact-arithmetic diagnostics. The actual verifier independently enumerates all restricted partitions for its finite test range. Computation does not establish the infinite theorem; the analytic estimates in RESULT.md do.

## Originality: PASS, with residual priority risk
Priya–Bhowmick–Meher (2026-11-05) give a least-gap generating function with a variable marking *location*, but do not derive the stopping-part multiplicity spectrum or its signed first correction. Wagner's 2011 Theorem 3 supplies only a leading one-gap local limit, including regular permitted-part sets. The published November 2026 joint least-gap law for regular partitions is a leading weak vector law and expressly does not claim exact tie-event probabilities or first finite-size marks. A published October 2026 law for unrestricted partitions gives uniform marked limits but no \(n^{-1/4}\) signed correction. These prior theorems are not denied: the new claim is only the first **nonzero quantitative correction** for an \(\ell\)-regular marked distribution and the resulting sharp tie bias. A possibly unindexed signed second-order expansion is the main remaining priority risk.

## Mathematical value: PASS
The stopping mark is a natural statistic attached to the recent least-\(r\)-gap theory, and a uniform limit hides systematic finite-size asymmetry. The result gives the complete mark-by-mark first correction for every fixed modulus and multiplicity threshold, establishes its strict ordered signs, and resolves the leading positive bias of exact equality events. Neither a merely renamed Rayleigh law nor an isolated numerical parameter is claimed.

## Limitations
All parameters are fixed as partition size grows; no error bound uniform in growing parameters is proved. Standard Euler-product saddle estimates are analytic inputs. An unindexed broader refinement remains possible. Finite calculations corroborate, not certify, the infinite asymptotic. No independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
