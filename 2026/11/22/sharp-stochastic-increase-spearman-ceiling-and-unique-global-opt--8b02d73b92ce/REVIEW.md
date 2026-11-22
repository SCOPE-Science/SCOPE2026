# Scientific review

**Claim assessed.** For the exponentiated FGM copula \(C_{\alpha,\delta}(u,v)=uv+\delta(1-e^{\alpha u(1-u)})(1-e^{\alpha v(1-v)})\), its nonindependent positive-dependence members are stochastically increasing precisely at \(\alpha\le 2\). The sharp stochastically increasing Spearman ceiling is \(0.505989303562664776\ldots\) at \((\alpha,\delta)=(2,1/4)\); the unrestricted positive Spearman optimum is uniquely at \(\alpha=3.746989957972222634\ldots\), with correlation \(0.586623892839975836\ldots\), and the high-correlation upper boundary has two distinct shape representations.

## Correctness — PASS

The copula's density reduces admissibility to the extremum of \((1-2u)e^{\alpha u(1-u)}\). Direct differentiation of the conditional CDF gives the necessary-and-sufficient SI sign criterion. Spearman's rho separates into a square of one integral. On \(\alpha\le2\), a positive-integrand representation proves its upper envelope strictly increases. On \(\alpha>2\), the envelope reduces to a positive one-variable function whose derivative has sign controlled by \(Q(s)=\int_0^s e^{-t^2}\,dt-s(1+s^2)e^{-s^2}\). The exact identity \(Q'(s)=s^2(2s^2-1)e^{-s^2}\) proves a unique global optimizer. This is a proof over the continuous full parameter range, not a finite grid inference. The standalone checker independently reproduces exact derivative identities and numerical values.

## Originality — PASS, with residual historical-priority risk

Zachariah, Arshad and Pathak (arXiv:2304.02231, 2023) introduced the model, its admissibility and rank correlation and the sufficient TP2 property on the \(\alpha\le2\) subfamily. The 2025 Zachariah dissertation's relevant Chapter 2 repeats the tabulated maximum and TP2 sufficiency, while Chapter 3 treats another PGF-based model. Their approximate tabulated upper correlation is prior work: a refinement of its decimal alone would not be original. The new statement is the *necessary* stochastic-increase restriction and the *sharp* compatible rank-correlation ceiling, together with a uniqueness theorem for the unrestricted optimizer. Other compared dependence-envelope results concern distinct copula kernels, and none directly imply these claims. Exact historical priority is not certified; a prior alternative derivation could remain undiscovered.

## Value — PASS

The original model was proposed to enlarge achievable dependence. The theorem identifies which part of that gain necessarily sacrifices stochastic monotonicity of conditional outcomes, a structural property relevant when modeling positively ordered responses. Its threshold is exact and attained, rather than an ad hoc discretized optimization; the branch multiplicity also explains why the same rank coefficient cannot recover the dependence-shape parameter on the upper boundary. The modest decimal improvement over the original approximate maximum is not the claimed mathematical value.

## Limits and comparisons

The source's TP2 sufficient region is not conflated with necessity without proof: the direct conditional-CDF sign test supplies the missing converse. The analysis is for positive coupling; independent members satisfy SI trivially and negative-coupling members are not SI. An independent external audit and exhaustive historical-priority verification have not been performed.

Self-review: passed. Independent audit: not yet performed.
