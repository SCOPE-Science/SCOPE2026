# Independent mathematical audit

## correctness

PASS

Independent all-length proof: a vertex in a full column needs a horizontal private witness in an adjacent empty column (a vertex in a nonempty neighboring column cannot serve). An empty column can witness selections of at most one full column, since between two full columns neither row is private. Thus the full-column count is bounded by the empty-column count. In equality, each full column must have exactly one witness-bearing empty column, and it must supply both rows; the other neighbor of this empty column is necessarily empty or absent. A singleton cannot border an empty column under this condition; it cannot border a full one either, since then neither itself nor its mate is private and a nonempty horizontal neighbor supplies no private witness. Hence the word is all singletons or all full/empty. In the singleton case each interior column's two neighbors have equal masks, giving exactly the four period-one or period-two words, all valid. In the full/empty case each column has exactly one opposite neighbor; the opposite links form the unique perfect matching of the path, and all other links join equal masks. This forces even n and gives the two stated prefixes, in which each empty column is dominated and supplies both witnesses to its matched full column. At n=1 the singleton prefixes reduce to the two vertices. This proves the count without running the packaged script. Inspection of verify.py's five-column test, sentinel flush, weight inequalities and tight-product logic also supports the stated certificate interpretation; packaged stdout is recorded evidence, not a fresh reproduction.

## originality

FAIL

The Resultary record dated 2026-10-12 states the exact classification on the same labeled ladders, including both even-only patterns and n=1. This is direct documented prior coverage, not an inference from date alone, a matching count, or a failed search.

## value

FAIL

The equality families are mathematically useful in their own right, but this submission supplies no distinct invariant or structural gain over the previously recorded complete theorem and finite-state approach. Correct verification of the same classification does not constitute a separate advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
