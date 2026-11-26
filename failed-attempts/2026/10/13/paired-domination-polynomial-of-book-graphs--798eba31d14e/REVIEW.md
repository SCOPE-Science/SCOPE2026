# Independent mathematical audit

## correctness

PASS

The graph is the Cartesian product of the star and P_2, with a shared spine edge and no edges between distinct pages away from the spine. With no spine selected, an empty page is undominated and a singleton is unmatched, so all pages must be full. With only a selected, domination or matchability forces every x_i to be selected, and exactly one x_i can lack its partner y_i: it must match a, and parity requires it. The reflected case uses b. With both spine vertices selected, domination is automatic and a singleton page can match only its corresponding spine vertex; hence there is at most one of each orientation, and parity permits only zero or two. The constructive matchings in all admissible states verify sufficiency. This counts sets, not matchings. The contributions are x^2(1+x^2)^n, n(n-1)x^4(1+x^2)^{n-2}, 2n x^{2n}, and x^{2n}; n=2 gives x^2+9x^4+x^6. Thus the spine is the unique minimum for n>=2, and evaluating at one gives the claimed total. For n=1 each of the four edges of C_4 gives a paired dominating set, as does the full graph. The frozen verification description and finite checker were read without executing it.

## originality

FAIL

There is demonstrable full coverage in a distinct indexed theorem: the quadrilateral-books result states the identical all-set polynomial for every n>=2 and proves the equivalent four-class census. It also gives a refined inclusion-minimal classification that the frozen record does not claim. This is a finding about exact coverage in the checked corpus, not a claim that the later-dated record was available first, that the frozen record derived from it, or that the result was known at the time of the frozen record. The unresolved 2016 source is not a reason for failure.

## value

FAIL

The square book and its paired-domination polynomial are natural and the exact census is useful in isolation. Under the distinct-contribution requirement for a narrow invariant, however, the whole census, polynomial and classifications are already available in the checked corpus. The frozen claim does not leave a further mathematical contribution beyond that documented coverage; this does not diminish the usefulness of the formula itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
