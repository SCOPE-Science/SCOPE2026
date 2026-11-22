# Mathematical review

## Correctness — PASS

The ambient algebra has dimension \(\binom{m+2}{2}\); the relevant coordinates consist of \(m+1\) first-diagonal entries and \(m\) second-diagonal entries, leaving \(m(m-1)/2\) free. Matrix-path counting gives the three output coordinates, and the second-diagonal vector enters the central coordinate linearly. The only first-diagonal zero patterns supporting nonzero central coordinate when the common middle product vanishes are exactly one internal zero or two adjacent zeros. Counting these patterns yields \((q-1)^{m-1}((m-1)q+1)\). All other counts follow without division by field-dependent constants, so the proof covers every finite characteristic, including \(q=2\). The positivity and strictness of three sizes follow from the binomial theorem. Direct full-matrix and smaller-data tests in the embedded checker passed, but general validity rests on the written algebraic proof.

## Originality — PASS, subject to historical-priority uncertainty

The closest directly overlapping earlier calculation is the explicit cubic-power fiber census for \(N_5(k)\), which is *exactly* the \(m=3\) instance of the present theorem. It is credited, not presented as an independently new special case. This theorem quantifies **every** near-top power exponent \(m\ge2\) in arbitrary characteristic, including a new nontrivial \(m\to\infty\) conditional central-concentration law. It is neither a mere change of constants nor a one-step numerical increment.

Bier's 2012 unitriangular verbal-width theorem proves power-map surjectivity for \(n\le p^t+2\); Sosnovsky's 2012 triangular-group theorem determines verbal width; Dolfi–Singh–Yadav's 2019 study examines power images and conjugacy classes and recalls the same boundary. All these are consistent with the present image statement but none states the count \(\#\{X:X^m=Z\}\) for every prescribed target or the conditional limiting law. Ekhad–Zeilberger's earlier square-zero theorem covers a zero-target case in a different all-upper-triangular setting, without the present prescribed nonzero fibers. Database searches for root fibers, aliases, near-top dimension, and the limiting ratio identified no dominating general formula. These searches do not prove worldwide novelty, and possible historical equivalent counts remain a stated risk.

## Value — PASS

This is a complete, characteristic-independent invariant for an infinite natural family of niltriangular matrix algebras at the last full-surjectivity dimension. Its sharp transition in the distribution of *nonzero* powers is not visible from the known image or width results: conditioned on being nonzero, a uniformly chosen power becomes central with probability tending to one, at the explicit rate \((q+1)/m\) for fixed field size. The theorem gives root multiplicities relevant to power word maps on growing finite unitriangular groups whenever the exponent is a characteristic power, and supplies an exact baseline for larger dimensions where surjectivity can fail.

## Closest literature and residual limitations

Sources: Bier (2012), DOI:10.1142/S0218196712500191; Sosnovsky, arXiv:1201.6513 (posted January 31, 2012); Dolfi–Singh–Yadav, arXiv:1905.04244; Ekhad–Zeilberger, arXiv:math/9512224. The first two were consulted in accessible full text, and Dolfi–Singh–Yadav in complete web-rendered text; for Ekhad–Zeilberger only its visible abstract was used, so no whole-document noncoverage claim is inferred from it. The theorem does not handle arbitrary offsets \(n-m\), higher-superdiagonal target geometry, or power exponents without the near-top relation. No independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
