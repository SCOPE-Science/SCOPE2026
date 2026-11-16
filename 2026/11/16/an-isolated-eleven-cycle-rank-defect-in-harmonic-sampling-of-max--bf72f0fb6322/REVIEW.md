# Scientific review

## Correctness — PASS
The gap characterization is an exact bijection between maximal independent sets and cyclic compositions into \(3,4,5\). Conditioning on one or two sites gives the stated integer-count products, and dividing by the cyclic total count yields the explicit covariance. Fourier eigenvalues are exactly those of a circulant covariance. At nonzero frequency the positivity criterion is the existence of a configuration with a nonzero Fourier coefficient; a one-site gap slide \((3,5)\leftrightarrow(4,4)\) supplies that witness for \(n=8\) and every \(n\ge11\). The remaining short cases are elementary explicit configurations. The interval of attainable sizes controls the constant mode. A separate bit-mask enumeration and direct Fourier evaluation passed the packaged finite regression tests through \(n=17\); the infinite assertion is proved symbolically.

## Originality — PASS, historical priority provisional
The relevant primary literature treats (a) all dominating sets of cycle powers and their counting recurrences (Galvin–Zhang, 2024) or (b) minimum independent-domination size in degree-bounded graphs (Cho–Kim–Kim–Oum, 2022). Neither result states or implies the complete affine-span and Fourier nullity classification for the **uniform inclusion-maximal** set ensemble on squared cycles. Known first-coordinate harmonic analyses for ordinary cycles use \(2,3\)-gaps and do not transfer their rank thresholds to \(3,4,5\)-gaps. The general cyclic renewal coefficient formula is standard and is not claimed as independently novel; the novel content assessed here is the complete rank and exceptional-nullity pattern. Residual risk is an earlier differently phrased affine-span or local-pattern theorem for cycle squares.

## Mathematical value — PASS
The rank is a natural coordinate-reconstruction invariant for the uniformly sampled independent dominating sets of a fundamental graph-power family. Determining it for **every** cycle length resolves both the exact onset of full-dimensional sampling and the counterintuitive isolated rank loss at eleven sites after full rank at nine and ten. This is not an arbitrary finite test or a cosmetic reparametrization of the ordinary-cycle result, because the permitted gap set and the singular-size pattern differ. No stronger downstream consequences are asserted.

## Scientific limits
The finding is restricted to the uniform maximal-set ensemble; no generic stability bound or quantitative small-positive-eigenvalue estimate is established. The comparison to prior research is based on material actually inspected; an undiscovered equivalent formulation remains possible.

Self-review: passed. Independent audit: not yet performed.
