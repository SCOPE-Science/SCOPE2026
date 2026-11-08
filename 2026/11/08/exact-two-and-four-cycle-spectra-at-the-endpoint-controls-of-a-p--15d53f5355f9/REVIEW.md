# Self-review

**Claim assessed:** Exact two- and four-cycle spectra at the endpoint controls of a parity-hybrid skew tent map, including fixed-point spectra and dynamical zeta functions, for every integer \(m\ge2\).

## Correctness — PASS

The defining floor and ceiling branches reduce exactly to \(S_1(z)=N-1-z\) and \(S_{N-1}(z)\equiv z+1\pmod N\), including both endpoints. The parity hybrid then gives explicit affine reflections for each two-step iterate. Since \(N\) is divisible by four, the even and odd solutions of the two linear congruences are disjoint in precisely the required way. This proves that every orbit has length two or four (only four at the second control) and gives the entire cycle census and zeta factors. The boundary \(m=2\) is handled separately for permutation order. The standard-library checker recomputed the original definitions and all advertised finite cycle counts for \(m=2,\ldots,14\). It is supporting evidence, not the infinite proof.

## Originality — PASS within checked evidence

The main source, Choi et al. (2026), introduces the exact hybrid in Definition 1, proves general bijectivity in Theorem 2, and gives a discrete Lyapunov exponent statement in Theorem 3; its empirical investigations and concluding discussion do not state a complete endpoint cycle census. Indeed the source explicitly identifies systematic study of period lengths as an open direction. Its large discrete Lyapunov exponent cannot imply the claimed finite order: permutations of the same state space can have different orders, and the pure endpoint skew tent \(S_{N-1}\) itself has order \(N\), unlike the parity hybrid. Analogous short-period/zeta results on finite graph maps, coupled cat maps, and other combinatorial automata concern different map definitions and do not cover this one. A paper on digital skew-tent period distributions was located only at abstract/caption level; it apparently concerns the nonhybrid map, but its full text could not be checked. Historical priority is therefore provisional. The specific comparison details and residual risks are recorded in AUDIT.json.

## Mathematical value — PASS

Period length is an explicitly identified gap in the source's study of a proposed pseudorandom-state generator. The result is an all-precision, complete periodic classification at both natural extremal admissible parameters, including exact cycle numbers, dynamical zeta functions, and an explicit control-asymmetry: one endpoint has two two-cycles, the other has none. The sharp four-step bound is independent of state-bit precision and contrasts with the source's large discrete Lyapunov diagnostic; it provides a concrete obstruction to treating that diagnostic alone as a guarantee of long unprocessed outputs. This is not a routine substitution into an existing cycle table; the endpoint simplification and parity selection must be combined and their two-step congruences exhausted.

## Closest literature and limitations

The closest source is Choi et al., *Some New Maximally Chaotic Discrete Maps*, Entropy **28** (2026), 131, DOI 10.3390/e28010131. The result does not classify interior controls or postprocessed outputs and does not challenge the source's definition of finite-state discrete Lyapunov exponent. Full publisher-page inspection was limited to substantial accessible scientific material for Sections 2–5; an older digital-skew-tent paper was inspected only via abstract and figure caption. These are remaining historical-inspection risks, not gaps in the algebraic proof.

Self-review: passed. Independent audit: not yet performed.
