# Independent mathematical audit

## correctness

PASS

Under the stated synchronous neighbor-only rule, A and A′ agree by symmetry and all relevant edges are initially active (gaps .21 and .29). Consequently a₁=.07 and b₁=K/[2(K+1)]. While the edges are active, d=b−a and e=s−b satisfy the displayed nonnegative gap recurrence, with ramp increment in [0,.001]. For K=1 the first pair (.18,.251) enters [0,.2]×[0,.3], mapped into itself since d′≤11/60 and e′≤.251. For K=2 the initial (.21,.29) belongs to [0,.3]², where d′≤.3 and e′≤.201. Inclusive confidence makes these inductive checks sufficient. At t≥500 the ramp increment vanishes and for each K the positive gap matrix has row sums 1 and 2/3 in some order, so its square has maximum row sum strictly below one. Therefore a and b converge to 1. For K≥3, the first ordinary gap is at least .305, outside the bound, while the nonnegative source gap is at most .126. A and A′ then keep averaging each other at .07; B follows the source with one-step lag. This is permanent since the ordinary gap stays above .43 and the subsequent source gap is at most .001. This also verifies nonempty eligible neighborhoods in every case. The observable excludes sources and equals (2a+b)/3, so the separated limit is 19/50 and the drop is 31/50. Replay: frozen RESULT.md, proof lines 29–73. The supplied Fraction checker was inspected, not executed; finite trajectories are not the basis of the all-K, infinite-time conclusion.

## originality

PASS

Best-of-knowledge pass for the exact fixed three-ordinary-node, attractive-only weighted witness and its full integer phase classification, not for a new update rule, novel segregation mechanism, or first example of qualitatively worse outcomes with more sources. Tarantino et al. already give that qualitative behavior numerically. The exact model of the source bundle is an increase in one effective edge weight and should not be advertised as isolating count at constant aggregate strength. The checked stronger-looking source-count theorem is about pace in a homogeneous group, not about rupture at the fixed placement considered here.

## value

PASS

This is a fully solved motivated counterexample to monotone influence in the aggregate input strength at fixed placement. It isolates permanent loss of an otherwise attractive ordinary bridge without repulsion, random source placement, changing ordinary topology, or varying ramp speed. The exact 2-to-3 source cutoff and large limiting loss come from one strict first-step inequality and a proof that the low-strength regimes never rupture; they are not a numerical anomaly. The value is the transparent model witness, not a universal cutoff, minimum number of agents, or behavioral prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
