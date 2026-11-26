# Independent mathematical audit

## correctness

PASS

Independent score calculation for the two Poisson means gives determinant e0 e1 g²/f: the downstream-only rank-one contribution cancels in the determinant and the source measurement supplies the second direction. With d=μ−λ, r=λ/d and t=exp(−dx), logarithmic differentiation gives the stated quadratic P. Its roots have negative product, P(0)>0 and P(1)=−2, giving a simple unique root in (0,1), with strict unimodality and the asserted distance cap. At the root the t derivative of the log-score is negative, while its p derivative is 1/[p+(1−p)t]², giving dx*/dp<0. Writing P=rp+b t−a t², the positive root (b+sqrt(b²+4arp))/(2a) yields t*/p→r/(1−r) for r<1 after rationalization, t*/sqrt(p)→1/sqrt(2) at r=1, and t*→(r−1)/(r+1) for r>1. This gives every displayed distance limit, including constants. The opening 'half the logarithmic slope' means half the limiting supercritical coefficient as μ decreases to 2λ, not half the coefficient at an arbitrary fixed μ>2λ; the exact formulas are unambiguous. This is a local design at a nominal p with known rates and fixed efforts, not a uniform finite-sample guarantee. Replay: RESULT.md lines 34–58 and the quadratic calculation above; the inspected checker and VERIFICATION.md document finite corroboration, not the proof.

## originality

PASS

The supported distinct result is the global one-distance optimum and its singular rare-source-fraction classification in this fixed-rate Poisson model. First-order transport and Fisher/local-D methods are not new. The strongest matching catalogue statement has similar physics and Poisson data but a different unknown, reference configuration and asymptotic variable; no equivalent or dominating statement was established in the inspected evidence.

## value

PASS

The exact boundary tells whether a locally informative sampling site stays at a finite distance for a rare source class or moves logarithmically far away; at the boundary a different balance sets the slope. The sharp coefficients and strict unimodality also govern when an accessibility cap binds. This is useful beyond applying the standard Fisher identity, while remaining conditional on a deliberately idealized steady two-class count model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
