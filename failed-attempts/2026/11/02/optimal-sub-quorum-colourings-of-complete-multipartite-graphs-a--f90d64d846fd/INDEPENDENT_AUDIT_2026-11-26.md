# Independent mathematical audit

## correctness

PASS

With s colored vertices and largest occupied size a, every color class has at least ceil((s-a+1)/2) members. For a>=2 and s>=a+2 the identity (a+1)(s-a+1)-2s=(a-1)(s-a-1)>0 gives at most a classes. If s=a the support is edgeless; if s=a+1 its star center forbids all-singleton color classes; if a=1 the support is complete and allows at most two classes. Since M>=3, an optimum hence occupies an entire largest part A. Writing t for the colored outsiders yields t(M-2)<=M, with the integer bound excluding t=2 for M>=3. A sole outsider sees all M vertices and at most one partner, so t=1 is feasible only with M=3 and a shared color; each triple vertex then meets quorum because its colored closed neighborhood has size two. For M=3,t=3 every class is a pair, and quorum at A forces pairs to cross into the outside set. Each outsider already has a colored closed neighborhood of size four from itself and A, so any adjacency to a second outsider would violate quorum. The outsiders are one full second triple and the matched-pair condition suffices. The pure-part construction always works. Counting disjoint families gives p, 3p(N-3), and 6 binom(p,2), with the two full parts unordered. The free naming action multiplies by M! because all classes occur. The frozen checker was inspected, not run: it is finite and filters for exactly M colors, so it does not itself exclude larger palettes; the proof gives the unrestricted bound.

## originality

FAIL

The scalar maximum is prior, and a distinct published Resultary proof already establishes the stronger structural statement that each color meets a chosen largest occupied part when there are at least three colors. Its local inequality yields all proposed configurations and counts by immediate equality and outsider-neighborhood tests. The exact rounded enumeration need not be printed verbatim to be covered. This finding is stronger than a title match or a priority inference from date labels.

## value

FAIL

The optimum solution space and its sharp size-three behavior are natural questions. In this record the surviving increment over the inspected same-problem structure consists of immediate small outsider cases and elementary multiplicity arithmetic; no independent enumeration obstacle or new meaningful structural invariant is resolved. The record does not address small-maximum regimes, symmetry classes, suboptimal palettes, or different hosts, so there is no valuable distinct remainder here to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
