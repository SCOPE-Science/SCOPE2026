# Self-review

## Correctness — PASS

The exact identities are consequences of an explicit finite Walsh block transform. Its support occurs only at zero and one-bit prefixes, so an evaluation with two initial one-bits \(a<b\) collapses to \(4^a-2^a(2\,4^{b-a-1}+1)/3\). Integer powers give the exact strict-negative condition \(3a\le2b-3\), with the \(a=0,b=1\) zero boundary accounted for. Haar-cylinder counting and three elementary geometric series establish the three closed formulas for every allowed integer, including \(n=1,2,3\). An independent exact-integer Walsh–Hadamard enumeration checks the formulas through \(n=12\), the threshold through bit \(84\), and the finite sum through \(n=60\). The finite tests do not stand in for the proof.

## Originality — PASS relative to inspected evidence

Blahota's 2026 abstract gives the sharp overall supremum \(71/50\), dyadic monotonicity and limit \(4/3\), not the phase-explicit finite norms or \(2/3\) convergence exponent. The paper's full body could not be retrieved, however, and it would be incorrect to call the paper itself noncovering; this remains a significant source-access risk. Nagy's 2008 accessible article gives the original Skvorcov decomposition, Walsh–Paley dyadic Fejér values, and maximal-kernel inequalities; its inspected statements do not explicitly carry out the two-one-bit sign count or derive the phase constants. It supplies a powerful starting identity but not the claimed final quantitative theorem without further nontrivial analysis. Semantic published-finding corpus searches for exact dyadic norms, the three constants and equivalent sign-count representations returned only results for other Walsh kernels/operators. Accessible historical claims were inspected for duplicate statements; no matching claim was found. This is conditional best-knowledge originality, not a proof of priority or completeness.

## Mathematical value — PASS

The result resolves the rate missing from the motivating dyadic limit, showing a fractional exponent and a nontrivial periodic rescaling with **three distinct exact constants**. This quantifies the finite-resolution stability cost of Walsh–Kaczmarz Fejér summation, where the corresponding Walsh–Paley dyadic norms equal one. The structural first-two-one-bit sign description explains why the exponent is \(2/3\), rather than producing a superficial restatement of the qualitative limit. The exact finite-index classification is naturally motivated; it is not an arbitrary numerical slice.

## Closest sources and residual risks

Closest source: I. Blahota, arXiv:2607.13684, 2026-07-15, abstract accessible but full paper unavailable; the possible overlap within its proofs is the principal originality risk. K. Nagy, JIPAM 9(1), Article 16 (2008), was inspected at its character definitions and main theorem and proof, particularly the Skvorcov kernel splitting formula. G. Gát, Studia Mathematica 130 (1998), is additional background and was not available as a complete inspected article. Independent literature checking cannot rule out all equivalent formulations or unindexed results.

Self-review: passed. Independent audit: not yet performed.
