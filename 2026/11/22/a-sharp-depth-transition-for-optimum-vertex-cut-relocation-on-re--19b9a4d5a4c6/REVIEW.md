# Independent mathematical audit

## correctness

PASS

Deleting either terminal neighborhood shows the minimum is at most three. The straight row and the two one-row detours are three internally disjoint paths, so a cut of size three hits each exactly once and has one selection in each row r−1,r,r+1. Write their columns a,b,c, with 1≤b≤n−2. If a≤b−2, follow the middle row to a+1 then take the upper rail to the far side; if a≥b+2, take the upper rail to b+1 then the middle row. Either bypasses the proposed cut; reflecting gives the lower bound |c−b|≤1 as well. An extra row above the top rail permits a full bypass through the endpoint columns unless a is itself an endpoint, and similarly below. Conversely, color each cut rail to the left/right of its missing vertex. Adjacent cut columns differing by at most one prohibit vertical edges between opposite colors. When an extra band exists beyond a rail, its cut is at a column endpoint, so the entire band receives the single surviving color of that rail. The two terminals thus lie in separate colors. Under legal moves exactly one of a,b,c changes, by one for a slide. At shallow depth two branches each have three consecutive free-coordinate values, giving two P₃ slides and a K₃ jump graph on each branch. A cross-branch jump is possible exactly at n=3, when b agrees, and joins matched free-coordinate values to make the prism. At deep placement both outer coordinates are endpoints; n=3 permits independent endpoint choices (four isolated slide vertices and a jump square), while n≥4 forces both endpoints on the same side and the two configurations disagree in all three coordinates. An independent direct finite grid check enumerated deletion sets of cardinality 0–3, tested reachability by BFS, and compared legal replacement graphs for 27 choices (n=3–5, w=4–6, every interior r); all matched. The finite test corroborates, not replaces, the proof. The supplied two scripts were inspected, not run.

## originality

PASS

The three-rail confinement, general reconfiguration framework and width-three inequalities have prior or overlapping counterparts. The supportable increment is the exact classification for at least four rows: outer-row bypasses impose endpoint restrictions, generating the depth transition and both complete move graphs. Compared passages do not state or cover that classification; this is a best-of-knowledge finding, not a historical order claim about same-day entries.

## value

PASS

Keeping the minimum separator size three while changing only the terminals' depth exposes a structural distinction between cut capacity and mobility. The total slide freeze, and the survival of a connected jump graph for precisely the deep three-column exception, are useful sharp reconfiguration benchmarks, not merely a finite grid census. The result is limited to opposite ends of one interior row, minimum cuts, and one-token moves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
