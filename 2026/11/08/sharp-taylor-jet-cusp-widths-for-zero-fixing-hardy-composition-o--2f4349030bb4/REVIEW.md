# Review of the sharp Berezin cusp-width theorem

## Correctness — PASS
The kernel formula follows directly from the normalized Szegő kernel. The first nonlinear term of a zero-fixing symbol contributes \(c r^{m+1}e^{i(m-1)\theta}\) to the Berezin transform, uniformly in angle. Schwarz–Pick and the tip-isolation estimate ensure that points in sections near \(1\) cannot originate from boundary-radius parameters. Solving the real-coordinate section equation gives \(r^2\sim\varepsilon/(1-a)\); choosing the two extremal phases of the leading coefficient realizes both imaginary bounds. These steps support the *exact* constant and exponent, not just finite-sample evidence.

## Originality — PASS, best-knowledge comparison
Bourdon, Le, and Thompson, arXiv:2610.17634v1 (2026), Section 3.4, Lemma 3.10 and Theorem 3.11, establish the qualitative cusp at \(1\), while Section 4 classifies convexity for linear symbols. Their accessible full open HTML was inspected, including the proof of the cusp and the linear convexity section. Cowen and Felder, arXiv:2109.12095, Sections 4–5, treat rotations, automorphisms and convexity questions. The qualitative classification mentioned in this package is readily informed by those predecessors and **is not asserted to be independently new**. No inspected source states or implies the sharp section-width exponent \((m+1)/2\) and coefficient \(2|c|(1-a)^{-(m+1)/2}\) for every first nonlinear Taylor order. The prior qualitative fact that a corner angle can be arbitrarily small does not determine this quantitative law. Searches for jet-based or cusp-width formulations and a comparison of research records found no direct coverage. Absolute priority cannot be certified.

## Mathematical value — PASS
The 2026 source calls the tip a cusp without specifying a rate. The theorem resolves its natural local shape invariant, showing that one operator-theoretic image set encodes the degree and normalized strength of the first nonlinear symbol term. All orders \(m\ge2\) are covered, rather than a special quadratic example. The sharp two-sided result describes the actual width of full vertical slices, not just a pointwise bound along one chosen parameter ray.

## Limits and nearest literature
The quantitative law requires a real multiplier \(-1<a<1\) and a first nonzero nonlinear Taylor coefficient. It does not recover the phase of that coefficient, nor does it describe nonreal tangents or the global Berezin boundary. The leading-order argument is elementary analytic but the exact section maximization and inverse-jet interpretation are not claimed in the cited literature. An older geometric boundary theorem may still imply it. The computational checker corroborates finite examples only; its output does not prove an asymptotic theorem.

Self-review: passed. Independent audit: not yet performed.
