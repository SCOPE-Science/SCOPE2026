# Independent mathematical audit

## correctness

PASS

All M softmax logits g_m in R^(p+1) can be shifted by the same u with exp(x~^T u) cancelling from every numerator and denominator, so unconstrained likelihood is exactly constant along p+1 dimensions and not identifiable merely up to label switching. Conversely full affine rank and equality of all gate functions identifies log-odds (g_m-g_M)^T x~, making the common shift the only representation gauge. Fix g_M=0 to remove it. BIC counts 3,8,13,18 for M=1..4 match component counts 3M plus 2(M-1) rather than unconstrained all-M logits. Primary 2026 source Proposition 3 fails to explicitly state needed normalization, though its numerical table already adopts baseline gate. These claims are mathematically sound and the supplied verifier and independent cancellation algebra checked.

## originality

FAIL

REJECT due decisive stronger published prior mathematical coverage, not mere matching vocabulary: Jiang–Tanner 1999 generic mixtures-of-experts identifiability and Huang et al 2023 softmax-gated mixture-of-experts Proposition 1 explicitly state that any common translation of ALL gate intercepts and slope vectors leaves the mixture distribution unchanged; this includes the F-LLoM gates as a direct special case. Their quotient/baseline convention also precedes 2026 F-LLoM. The identified omission in the 2026 Proposition 3 is genuine source-specific editorial/theorem-qualification feedback, but its exact obstruction and fix are already general published knowledge, mechanically specialized; under strict corollary coverage no independent original mathematical claim survives.

## value

PASS

The finding has practical source-specific value: a named published identifiability proposition omits the baseline restriction although its numerical likelihood and BIC degrees of freedom already use it; unrestricted Hessian is singular and would mislead variance inference. Value is assigned PASS for documenting this consequential scope error and reconciling published Table 1/2, notwithstanding already-covered mathematical originality. Overall disposition is failed because O fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
