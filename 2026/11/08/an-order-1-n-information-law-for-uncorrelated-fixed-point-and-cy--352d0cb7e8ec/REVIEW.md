# Scientific review

## Correctness — PASS

The claim concerns two exactly specified integer statistics of a uniformly sampled function. The rooted-forest enumeration gives the cyclic-core distribution, while the conditional cyclic permutation gives the rencontres conditional law; the marginal fixed-point count is exactly binomial. These identities prove zero covariance and strictly positive mutual information at every size at least two. The exact KL chain identity, a superfactorial chi-square majorant for the rencontres-to-Poisson divergence, and a separate second-order binomial-to-Poisson KL estimate prove the \(\mathcal J/n\) law. The constant's finite approximation has a proven error bound below \(1.5\cdot10^{-24}\). The standalone code passed 341 checks, including full map enumeration through six vertices. Numerical checks are corroboration, not substitutes for the infinite proof.

## Originality — PASS, with documented priority risk

Hansen and Jaworski (2010) explicitly use conditional uniform permutations on the cyclic vertex set, but their inspected 19-page paper develops conditional component-size distributions and a Poisson–Dirichlet limit, not the mutual information between fixed-point count and cyclic-core size. Soria's 1996 lecture presents random mapping generating functions and marginal limit laws, not the entropy-deficit constant. Flajolet–Odlyzko (1990) is a closely related, broad random-mapping framework; its accessible abstract and bibliographic record do not establish the target statement, but the complete author-posted archive source was inaccessible for inspection. Searches for joint law, entropy deficit, conditional rencontres distribution, and the information coefficient did not identify a statement implying the asserted \(1/n\) law. Comparisons against available prior findings on random maps (cyclic core versus origins, cycles versus origins, and components versus component sizes) did not supply the fixed-point/cyclic-core information theorem.

This is not a claim that the earlier conditional-permutation representation is new. The proposed addition is the quantitative rare-core contribution to nonlinear dependence, including its exact universal coefficient and proof of negligibility of the Poisson marginal replacement. Broader existing information-theoretic or random-mapping work could implicitly yield the same constant; historical priority is not independently established.

## Value — PASS

The fixed-point count and cyclic-core size are canonical statistics of functional graphs. Their exact zero covariance might misleadingly suggest independence, yet the entropy-based dependence remains strictly positive and has a sharp decay coefficient. The coefficient is controlled by the rare fixed-size cyclic cores rather than the typical order-\(\sqrt n\) cores, a structural feature not apparent from the usual marginal limit theorems. This is a motivated quantitative dependence invariant with a natural information-theoretic interpretation, not a parameter-relabeling or arbitrary small example.

## Literature and limits

- J. C. Hansen and J. Jaworski, *Random mappings with a given number of cyclical points*, Ars Combinatoria 94 (2010), full text: https://combinatorialpress.com/article/ars/Volume%20094/volume-94-paper-34.pdf .
- M. Soria, *Distribution of Image Points in Random Mappings*, Algorithms Seminar, November 10, 1996: https://algo.inria.fr/seminars/sem96-97/soria.html .
- P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, EUROCRYPT 1989 / LNCS 434 (1990): https://doi.org/10.1007/3-540-46885-4_34 .

The theorem is restricted to uniform mappings and to the two aggregate counts. The asymptotic remainder is only \(o(1/n)\); no exact higher-order expansion or general nonuniform mapping extension is asserted.

Self-review: passed. Independent audit: not yet performed.
