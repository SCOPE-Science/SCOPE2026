# Scientific assessment

## Correctness — PASS
Hensel's lemma gives one root lift per simple residue root, and factoring off that root makes the remaining local polynomial a unit. Intersection of two residue balls yields an exact joint-tail count of \(N_{\min(t,s)}p^{k-\max(t,s)}\) for every depth. Summing the tails proves the stated bivariate probability generating function; the same sums give the covariance and the quadratic sign classification. The proof is self-contained modulo classical Hensel lifting and prime-adic measure. The standalone integer-count program checks 1,228 finite marginal, mixed-tail, and cross-moment identities; no finite test is mistaken for an infinite proof.

## Originality — PASS within the inspected evidence
The nearest single-polynomial tree classifications are Medina–Moll–Rowland (2015) and Boultinghouse et al. (2023). Snyder (2023) treats trees for products, completely for rationally split polynomials, but does not state or derive the joint distribution and covariance-sign theorem for two separately observed polynomials. In particular the present result applies to irreducible rational quadratics with simple mod-prime roots, which are not covered by Snyder's completely rationally split theorem. Statement/implication comparisons and explicit source inspections are recorded in `AUDIT.json`; no identical or stronger law was found. Residual risk: an equivalent mixed-moment formula could exist in local zeta-function literature not indexed in the searches.

## Value — PASS
Valuation trees usually record a single function or a product. The new invariant measures dependence between two separately evaluated polynomials at the **same integer**, which their marginal valuation trees do not determine. A whole-prime, all-depth law and an unexpectedly sharp positive/negative/zero covariance boundary for quadratic pairs are structurally informative, including at irreducible rational examples. This is more than a single modular computation or an arbitrary parameter slice; it quantifies root-tree intersection from root distances.

## Limitations
Only simple residue roots are covered, and there is no claim about singular reductions, all-length finite-prefix discrepancy, or guaranteed historical priority. The routine lifting and ball-measure ingredients are classical. Independent scientific review has not been performed.

Self-review: passed. Independent audit: not yet performed.
