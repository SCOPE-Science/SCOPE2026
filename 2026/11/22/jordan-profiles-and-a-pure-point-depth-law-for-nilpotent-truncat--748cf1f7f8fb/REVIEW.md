# Self-review

**Scientific claim:** Jordan profiles and a pure-point depth law for nilpotent truncated substitution endomorphisms.

## Correctness (C): PASS

Every unital endomorphism is a substitution on one nilpotent generator. The noninvertible maps have order at least two; a composition multiplies positive orders, so the ideal nilpotency cutoff and the order of every iterate follow. Distinct leading degrees of image monomials determine the exact ranks, and the finite-difference identity determines the entire Jordan type. Leading coefficients and remaining free coefficients give the full exact count. The geometric order law and an exponentially negligible tail prove weak convergence. The independent checker constructs and tests actual substitution matrices in eleven exhaustively enumerated prime-field cases; results are recorded in `checker_output.txt`. Boundary \(N\ge3\), all finite fields, and zero substitution are handled separately. No inference of infinite validity from the finite checks is used.

## Originality (O): PASS, with priority uncertainty

The 2015 paper *Submonoids of the Formal Power Series* studies support-closed composition submonoids, not Jordan types of nonunit finite truncations or limiting depth statistics. Bavula's 2008 work studies polynomial monomorphisms and characteristic-zero factorizations. Published finite-field Jordan enumerators of multiplication maps on width-two monomial algebras do not imply the Jordan ranks of substitution homomorphisms; published chain-evolution endomorphism results apply to different, nonassociative algebras. Existing first-degree and order-multiplication arguments are explicitly acknowledged, not claimed novel. The strongest novelty assertion is the assembled all-level Jordan census and its limiting law; unidentified wider theorems remain a genuine priority risk.

## Value (V): PASS

The intrinsic linearization of every nonunit in a natural, finite-dimensional associative endomorphism monoid has a complete Jordan classification across all truncation lengths and characteristics. Its exact enumerator and nonconcentrating infinite-atomic depth limit reveal a stable arithmetic law hidden by mere nilpotence. This is a natural structural invariant of substitution monoids, not an arbitrary finite slice or one unexplained numerical gain; the proof provides reusable leading-order control of all iterated ranks.

## Source and scientific limitations

The earliest public archival source is Bavula, arXiv:math/0701211 (2007-01-07); Enochs–Jenda–Ozbek, arXiv:1510.05984v1 (2015-10-20), is the closest source on formal-series composition. Literature and published-record search do not establish uniqueness; some priority risk persists. This review is internal to the mathematical package and does not represent independent external validation.

Self-review: passed. Independent audit: not yet performed.
