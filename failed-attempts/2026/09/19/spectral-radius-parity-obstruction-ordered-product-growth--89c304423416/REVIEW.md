# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **failed**.

Correctness: PASS. The explicit period-two construction is correct. Direct differentiation gives the stated matrices at the two orbit points and their two-step product is diagonal with multipliers \(e^{2a}\) and \(e^{2b}\), so the per-iterate Lyapunov exponents are \(a\) and \(b\). Exact multiplication gives \(h_{2k}=a\) and \(h_{2k+1}=(a+b)/2\). For the representative parameters \(a=0.2\), \(b=-0.8\), \(s=0.8\), independent recomputation gives one-step spectral radii \(0.8\) and approximately \(0.6860145451\), odd-horizon rate \(-0.3\), even-horizon rate \(0.2\), and singular-value rate \(0.2\) at every tested horizon. The general periodic checkpoint identity and the subadditive singular-value replacement are also mathematically valid.

Originality: FAIL. A published 18 September 2026 record was inspected in full and already proves the same source-specific correction: a smooth deterministic periodic cocycle with a simple top Lyapunov exponent has \(h_{2k}=a\) and \(h_{2k+1}=(a+b)/2\), so the spectral-radius block rate need not converge; it also gives the eigenvector-alignment failure, periodic return-time identity, endpoint-transversality mechanism, frame dependence, and the singular-value repair. The present record supplies a cleaner planar period-two realization in which both one-step spectral radii are below one and the parity branches have opposite signs. Those are stronger witness features, but they are a routine strengthening of the already-published counterexample mechanism rather than a distinct final mathematical claim. Under the required implication/coverage standard, the packaged novelty claim therefore fails.

Scientific value: PASS. The strengthened witness is scientifically useful because it shows that every individual step can be spectrally stable while the top Lyapunov exponent is positive and the proposed diagnostic alternates stability sign forever. The source correction itself is important. Rejection is due to prior coverage, not lack of mathematical relevance.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
