# Independent mathematical audit

## correctness

PASS

For every n>=3 legal swaps among positions 1,..,n on the cycle, the side-of-home signature L subset {2,..,n-1} is preserved by linear neighboring swaps; canonical two-block sorting legally connects each sector. The wrap swap replaces one early internal label by one late internal label, preserving |L|=exc-1. The canonical form begins at min L and ends at max complement, giving a strictly increasing signature-sum move until the largest-|L| signature is reached. Thus each fixed excedance is one component. Inclusion-exclusion gives its known Eulerian derangement size; the two extreme cyclic shifts are isolated. Direct independent graph construction enumerated all n=3..7 and checked exact components, statistics and isolated states.

## originality

PASS

The November 2 general forbidden-fixed-position theorem exactly supplies the path-only 2^(n-2) signature decomposition, a prior input explicitly credited. It has no wrap-around position swap and hence does not imply the new quotient-by-cardinality classification. A separate 2026-11-08 result allowing two-step position swaps connects the whole derangement graph, a different move generating graph. No inspected primary result implies the wrap-only n-1 theorem.

## value

PASS

Changing one natural local reconfiguration generator from path to cycle collapses exponentially many known path-components to n-1 components while retaining exact classical excedance labels and sizes; a sharp global connectivity classification with constructive paths and precisely two isolated states.

The dated certificate retains the supplied scientific assessment, sources and limitations.
