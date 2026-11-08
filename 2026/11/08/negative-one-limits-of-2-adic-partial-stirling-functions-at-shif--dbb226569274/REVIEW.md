# Self-review

## Correctness — PASS
The proof uses the exact rational identity \(n!P_n(-1)=\sum_{j=1}^{n}2^{j-1}/j\), obtained by adding elementary binomial-harmonic integrals. The dyadic logarithm gives \(\sum_{j\ge1}2^{j-1}/j=0\) and hence an exact tail formula. The odd factorial units converge for fixed \(a\), and a uniform valuation bound on the tail terms justifies exchanging \(e\to\infty\) and the infinite sum. Legendre's digit-sum valuation and separation of the binary supports complete the result. All quantifiers specify fixed positive \(a\), fixed nonnegative \(\Delta\), and \(e\to\infty\). A finite standalone verifier confirms independent small cases but is not the infinite proof.

## Originality — PASS, qualified
The nearest primary result is Davis (2014), Theorem 2.6, which addresses only nonnegative input \(x\), while the paper explicitly discusses an unsolved convergence question for nonintegral/nonnegative-complement \(2\)-adic arguments; \(-1\) is not a case of its proved limit formula. Davis (2013) proves the general factorial-unit limit but does not formulate the weighted partial Stirling negative-one limit. Targeted research-record, publication, and equivalence searches did not find the all-\(a\), all-\(\Delta\) formula. This is evidence of noncoverage, not a claim of exhaustive historical priority. The older 2011 partial-Stirling paper was searchable at abstract level but its full text was inaccessible during comparison; overlap risk is retained. The relation to classical binomial-harmonic identities means a differently phrased derivation might exist.

## Mathematical value — PASS
The 2014 investigation proves convergence at nonnegative inputs and raises the question of convergence for other \(2\)-adic arguments, including eventually periodic ones. The explicit negative input \(-1\) is the simplest eventually periodic integer not addressed by that theorem. The result treats every offset and every scaling coefficient simultaneously; its exact constant is a product of a short-index partial-Stirling value and an established factorial unit. The separate dyadic-logarithm mechanism demonstrates why one cannot simply substitute a negative exponent into the earlier positive-input formula. This is an infinite-parameter, motivated boundary theorem rather than a new name for a known nonnegative-input formula.

## Closest sources and residual risks
Davis, arXiv:1402.0433v1, Theorem 2.6 and Conjecture 2.13 (full text inspected); Davis, arXiv:1301.6285v1, Theorem 1.1 (full text inspected). Other potential literature can contain the binomial-harmonic identity in another notation. The full text of Davis's 2011 partial-Stirling study was not retrieved. The proof is self-contained apart from standard 2-adic facts, but specialist priority review and independent mathematical audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
