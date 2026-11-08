# Self-review

## Correctness — PASS

The optimal-scale reduction follows by algebra from the exact cumulant generating function. The central lemma proves strict monotonicity of \(\Theta\) through exact positive power-series coefficients and the decreasing coefficient-quotient identity, not numerical sampling. Its endpoint limits yield the unique global optimizer and sharp transition \(s=\lambda b^2/3\). Taylor expansion and direct large-argument asymptotics establish both quantitative regimes. The standalone checker passes 624 finite rational/numerical diagnostics. Finite checks do not establish the continuum proof; the identities and sign argument in `RESULT.md` do.

## Originality — PASS (best-knowledge, historical-priority risk)

The most directly relevant prior theorem is Chen (arXiv:2610.00032v1), which gives the unrestricted variance-matched sub-gamma variational formula and discusses Gaussian smoothing. It therefore implies an *unsolved supremum representation* for the present special family. Its inspected complete manuscript does not identify the one-third Gaussian variance transition, prove monotonicity of the particular stationary equation, quantify the unique optimizer, or derive the quadratic and logarithmic expansions. Those concrete evaluations are the claim, not the inherited variational reduction. Klar and Müller's M-class results imply an abstract transform-order characterization, and Leskelä and Välimaa address a different Poisson-shaped variance proxy. Searches of related record summaries and accessible primary sources yielded no direct coverage; that does not prove absence in all prior literature. An equivalent special-function or reliability-theory calculation is a residual historical-priority risk. The author-hosted 2003 PDF was accessible in extracted text, but rendered-page inspection timed out.

## Mathematical value — PASS

Independent Gaussian smoothing is a natural operation in concentration theory. The exact variance-matched scale is a meaningful nonasymptotic tail parameter; the theorem classifies when the local third cumulant suffices and when a nonlocal optimizing tilt is necessary, with a sharp transition and nontrivial high-noise logarithmic correction. This is a complete motivated one-parameter phase diagram, not an arbitrary finite example or restatement of the general variational formula.

## Scope and limitations

The theorem requires independent Gaussian and fixed-jump Poisson components, right-tail exponential moments, and variance proxy fixed at the true variance. The verification script provides reproducible finite diagnostics, not machine certification of universal inequalities. Independent mathematical and priority assessments have not been performed.

Self-review: passed. Independent audit: not yet performed.
