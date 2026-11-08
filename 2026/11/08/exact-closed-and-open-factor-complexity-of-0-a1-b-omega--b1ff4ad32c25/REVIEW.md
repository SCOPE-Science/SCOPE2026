# Review of exact two-run periodic closed/open complexity

## Correctness — PASS

The statement covers all positive integers \(a,b,n\), defines closed words by complete first return to a nonempty proper border (with letters closed), and excludes the empty word. The period \(0^a1^b\) is primitive. The first-positive-occurrence displacement of a prefix starting at offset \(j\) in a run of length \(d\) with remainder \(r=d-j\) is \(1\) below length \(r\), \(a+b-j\) at length \(r\), and \(a+b\) above length \(r\). This is checked by tracing transitions, which locate a unique phase. A length-\(n\) factor is closed exactly when its proper border length \(\ell\) satisfies \(n=\ell+R(\ell)\). That partitions the long-factor contributions into \(\min(d,h-1)\) ordinary phases and at most one parity phase per run, where \(h=n-a-b>0\). For \(n\le a+b\), the only mixed closed factors are two-transition factors with equal exterior-run lengths; every other possibility is unary or unbordered. All cyclic phases are distinct from length \(a+b\) onward, and the exact total factor complexity is \(\min(n,a)+\min(n,b)\). At \(n=a+b+\max(a,b)\) all phases are closed; at the preceding length at least one is open. Direct tests check 10,010 factor-length cases over \(1\le a,b\le15\); the packaged verifier checks 5,254 cases by a separate border-occurrence algorithm. These finite checks are corroboration only; the structural proof establishes the infinite theorem.

## Originality — PASS, qualified

Parshina and Postic (arXiv:2005.06254, first public 2020-05-13) introduce the open/closed factor complexity questions and prove general links with periodicity and aperiodicity, but no full explicit length profile for a one-zero-run/one-one-run primitive period was found in their inspected results. Parshina and Puzynina (arXiv:2111.00863) study extremal closed-rich behavior and sufficient conditions, not this two-parameter pointwise spectrum. Badkobeh, Fici, and Lipták (arXiv:1305.6395) prove general results about closed factors, including first-return and exponent properties, but not this explicit profile. Comparisons with the accessible historical claim ledger and published-finding corpus mathematical search results did not locate an equivalent or stronger profile. In particular, previously recorded finite increasing-gap closed factors and maxima over arbitrary finite words do not imply a formula at every factor length of \((0^a1^b)^\omega\). A differently formulated or unindexed prior result remains possible; bibliographic searches never prove global uniqueness.

## Value — PASS

The question refines the general closed/open complexity theory by finding the exact profile, not just eventual vanishing of open complexity, in a simple but nontrivial infinite two-parameter family. The formulas exhibit a parity-sensitive pre-saturation regime, distinguish short factors from recurrent long factors, and identify a sharp first length after which no open factors remain. This is an exact natural structural classification of a standard periodic family, not a numerical table, routine substitution, or generic eventual-periodicity corollary.

## Closest literature and limitations

References: O. Parshina and M. Postic, *Open and closed complexity of infinite words*, arXiv:2005.06254; O. Parshina and S. Puzynina, *Finite and infinite closed-rich words*, arXiv:2111.00863; G. Badkobeh, G. Fici and Z. Lipták, *On the Number of Closed Factors in a Word*, arXiv:1305.6395. The proof does not cover arbitrary periodic words with more than two runs per primitive period. No independent scientific audit has occurred, and a bibliographic equivalence could have been missed.

Self-review: passed. Independent audit: not yet performed.
