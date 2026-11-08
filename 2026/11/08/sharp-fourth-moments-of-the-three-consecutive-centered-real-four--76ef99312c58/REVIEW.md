# Scientific review: sharp fourth moments of three consecutive real Fourier harmonics

## Correctness — PASS

The object is the full six-real-dimensional space of real, mean-zero trigonometric polynomials supported on \(\{\pm1,\pm2,\pm3\}\) with normalized circle measure. Fourier orthogonality gives the exact quartic form (1) in `RESULT.md`. Its only mixed phase-dependent terms are associated with the resonances \(1+1+1=3\) and \(1+3=2+2\), and both signs can be simultaneously attained. The minimum reduces by the exact decomposition (2), the inequality \(2ac\le a^2+c^2\), and a one-variable cubic derivative with two positive roots and a unique global minimum. The maximum follows from two independent equality-forcing symmetrizations of the first two coefficient magnitudes and another cubic derivative with a unique positive zero. The exact nonnegative deficits (7) and (8) characterize all equality cases. The checker reruns a complete symbolic Fourier enumeration, derivative and root-count verifications, and coefficient diagnostics. These computations are auxiliary to the complete analytical proof; no finite sample is treated as an infinite certificate.

## Originality — PASS, with residual bibliographic uncertainty

The closest inspected primary sources are Nursultanov–Ruzhansky–Tikhonov (arXiv:1403.3430v1) and Schmidt (arXiv:1302.2766v1). The former gives broad spectral-count/Nikol'skii estimates and identifies the sharp \(L^2\to L^\infty\) case, without deriving these exact mean-zero degree-three \(L^4/L^2\) endpoints or their equality families. The latter studies asymptotic fourth moments of analytic unimodular polynomials, rather than all coefficients on conjugate-symmetric six-character support. Published four-consecutive-character and three-character exact fourth-moment results have different one-sided Fourier supports and do not contain the two simultaneous resonance relations in (1). A related exact two-tone first/third-harmonic lower bound determines the value of the present minimum on a proper subspace but does not imply that adding the second harmonic leaves the minimum unchanged, nor does it determine the six-dimensional upper endpoint. A related three-harmonic result for \(\{1,2,4\}\) has different quartic resonance structure and a different sharp interval. Publicly indexed records involving the symmetric third Fourier cutoff address operator contractions, not directly the present norm optimization. A specialized unindexed exact classification could still exist; this uncertainty is not asserted away.

## Mathematical value — PASS

The object is the first full centered real trigonometric space where two distinct quartic resonances interact. The sharp minimum is attained on the proper two-tone subspace even though the maximal norm genuinely requires all three harmonics, and both endpoints have rigid algebraic ratio characterizations. The result solves the complete six-dimensional norm range, not just an isolated example, and its exact positive deficit identities give stability controls. These features distinguish it from a routine application of a general Nikolskii bound or a table lookup.

## Limits

The proof applies only to continuous-circle Haar measure, real-valued zero-mean functions of degree at most three, and exponent four. It gives no general higher-degree classification, no discrete cyclic aliasing claim, and no optimal Euclidean comparison norm. Novelty judgments rely on the indexed literature and material that could actually be inspected; inaccessible specialized sources are a remaining risk. No independent mathematical assessment has been performed.

Self-review: passed. Independent audit: not yet performed.
