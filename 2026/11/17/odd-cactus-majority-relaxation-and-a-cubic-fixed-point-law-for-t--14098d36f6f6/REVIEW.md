# Independent mathematical audit

## correctness

PASS

For a two-cycle x<->y on an even-degree graph, each flipping vertex v must have strictly more than half its neighbors opposite at both phases. Partition flipping neighbors into initially opposite p_v and same q_v, and fixed neighbors into h0,h1; adding two majority inequalities gives p_v-q_v>=2, so p_v>=2. The graph induced by opposite-colored flipping edges is bipartite and has minimum degree>=2, hence contains an even cycle; contradiction. Generic symmetric threshold theorem bounds eventual period to <=2, giving fixation. For T_n, encode disagreements b_i on cut vertices: blocks of three ones impossible; two-run cannot touch boundaries; internal singleton one-run has two ear assignments, boundary singleton one, strict internal length-two one-run one. Weighted state transfer M=[[1,1,0],[2,0,1],[1,0,0]] yields T generating function (1+z)/(1-z-2z^2-z^3) and Q_n=2(T_(n-1)+T_(n-2)), hence claimed rational function, recurrence and PF asymptotic. Independently brute-enumerated all 2^(2n+1) states for n=1..7 and matched fixed and two-step-return Q=2,6,12,26,56,120,258. The unrestricted statement follows from the even-cycle obstruction plus period theorem, not finite enumeration.

## originality

PASS

General symmetric-threshold period-at-most-two theorem is known Goles–Olivos 1980; it cannot exclude 2-cycles only on even-degree no-even-cycle graphs. Turau tree dynamics excludes cyclic chains. Exact Resultary triangular clique windmills are K1 join rK3, different topology and degree parity from vertex-glued triangular chains; a separate same-chain three-state excitation count uses a different update alphabet. No earlier all-n Q_n cubic recurrence or even-cycle obstruction found. Primary Goles full text access unavailable, acknowledged separately rather than automatic O failure.

## value

PASS

The parity plus even-cycle obstruction gives a graph-structural sufficient condition for true fixed convergence beyond trees, and the natural 2n+1-vertex triangular cactus family has a closed, nontrivial cubic recurrence and exact equilibrium rarity. Independently useful exact enumeration and qualitative convergence criterion; not a routine restatement of period<=2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
