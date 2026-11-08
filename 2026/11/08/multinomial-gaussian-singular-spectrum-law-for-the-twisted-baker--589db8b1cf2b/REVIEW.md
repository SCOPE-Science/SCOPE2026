# Scientific review: Gaussian singular-spectrum law

## Correctness

**PASS.** On either branch the derivative is an explicitly signed monomial matrix, and composition shows that the singular values are exactly the powers of two of cyclic suffix-occupation counts. Under normalized Lebesgue measure each binary word has measure \(2^{-n}\), so the counts are a half-lazy directed-cycle Markov occupation vector. For any centered test function \(g\), the equation \(h(j)-h(j+1)=2g(j)\) has a periodic solution. Its martingale increments have conditional variance exactly \(g(j)^2\), making the Gaussian covariance \((1/m)I_m-(1/m^2)\mathbf1\mathbf1^\top\). Sorting, second-moment uniform integrability, and dimension-two binomial reduction justify each stated consequence. Direct integer-matrix enumerations and seeded covariance experiments passed; they are not proofs of the limit.

## Originality

**PASS, within the checked sources.** The primary Saiki–Takahasi–Yorke paper proves Bernoulli coding, periodic multiplier behavior, periodic-point equidistribution, and mixing, but does not provide this typical-orbit *joint singular-spectrum* limit or its explicit mean top-expansion constant. A nearby three-dimensional Gaussian calculation concerns uniformly sampled periodic-point weakest return eigenvalues, not the full finite-time singular spectrum of volume-sampled trajectories in every dimension. A published exact real-spectrum residue law likewise concerns periodic eigenvalues, not the asserted distribution. Classical Markov-chain martingale CLTs supply proof machinery and are not claimed as original. The possibility of an unindexed equivalent application remains a priority risk.

## Value

**PASS.** The motivating map was designed to juxtapose twisting, stretching, and nonuniform expansion. The exact all-dimensional covariance equality with the independent multinomial benchmark is a substantive structural cancellation for a nonreversible dependent walk, not a generic mixing consequence. It determines every finite-time Lyapunov-coordinate fluctuation, the sharp positive \(\sqrt n\)-order mean top-singular-value correction, and the limiting condition-number law. These are natural quantitative observables unavailable from the originating paper's periodic density and equidistribution theorems.

## Closest literature and limitations

The closest primary article is Saiki, Takahasi and Yorke, *The twisted baker map*, arXiv:2202.04304 (initial submission 2022-02-09). General Markov martingale background is due to Gordin and Peligrad (arXiv:0910.3448) and Jones (arXiv:math/0409112). A previously recorded three-dimensional periodic-orbit central limit law shares a cyclic-occupation covariance but not the sampled objects or dimension scope. The conclusion requires fixed \(m\), normalized Lebesgue initial conditions, and almost-everywhere derivatives, and is about singular values rather than multiplier eigenvalues. Independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
