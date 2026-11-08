# Scientific review

## Correctness

PASS. The one-to-one correspondence between a marked path and a rooted forest with the path vertices as specified roots gives the denominator \(k n^{m-1}\). Deleting selected off-path leaves and selected path endpoints counts compatible forests as \((k-s)(n-r-s)^{m-1}\); the resulting mixed binomial moments determine the full finite law. Subtraction establishes the exact sign-changing conditional-mean difference. A uniform Taylor expansion on moderate distances and Gaussian distance tails yield the stated Rayleigh-scale regression and covariance limit. The separate finite enumeration verifies the critical moment formula but is not used as an infinite proof.

## Originality

PASS, with historical-priority uncertainty. The inspected Pitman enumeration gives the rooted-forest identities, but not the conditional leaf-count generating polynomial or its sharp mean optimizer. Aldous's classical random-tree study treats marginal properties. Remmel–Williamson's multivariate spanning-tree framework does not yield an explicitly inspected match. Berzunza Ojeda–Janson treat distance profiles and leaf-biased trees in a different conditioning scheme. Joyal's mapping–tree correspondence carries the already-known conditional mapping indegree-zero factorial moments precisely to the **off-path** leaf marginal: this and its leading covariance are covered and excluded from the originality claim. The closest inspected Cayley-tree finding additionally provides **one endpoint's conditional degree**. Neither prior result supplies the **joint off-path/endpoint leaf law**, which creates the nonmonotone conditional mean and sharp cubic-root maximum. Those distinguishing statements were not located in targeted statement/implication searches; some older multivariate enumerations may nevertheless imply them.

## Value

PASS. Total leaves are a basic global statistic, and the separation of marked vertices is a basic geometric statistic of the same random tree. The result resolves their complete finite conditional distribution and a surprising scale competition: local endpoint suppression and global off-path leaves produce a mean curve with a \(n^{1/3}\)-scale optimum even while typical marked separation is \(n^{1/2}\). The exact conditional law and quantitative covariance distinguish it from a textbook marginal count or an arbitrary parameter slice.

## Closest literature and limitations

The principal ingredients are classical labeled-forest counts and the previously known mapping off-path marginal; the claimed contribution is the newly coupled endpoint/remaining-forest law and its cubic-root optimizer. The leading covariance shares a known mapping counterpart and is a supporting consequence, not a separate novelty claim. Historical bivariate generating-function coverage has not been ruled out absolutely. The proof is specific to uniform labeled trees. Finite exhaustive checks are not replacements for the general proof.

Self-review: passed. Independent audit: not yet performed.
