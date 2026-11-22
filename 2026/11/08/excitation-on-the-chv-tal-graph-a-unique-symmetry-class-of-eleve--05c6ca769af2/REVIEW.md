# Independent mathematical audit

## correctness

PASS

The specified 24 undirected edges define a 12-vertex degree-four graph. Encoding s=sum_i x_i 3^i enumerates exactly 531441 configurations, with every successor computed by synchronous 1->2, 2->0, 0->1 iff an excited neighbor. For a functional graph, Kahn indegree-zero stripping leaves precisely the periodic vertices; reversing removed order gives tau(s)=1+tau(Fs) and p(s)=p(Fs). I inspected actual chvatal_enum.cpp, chvatal_independent.py, their saved census data, and all 13 source blobs in the frozen tree. Independently built and ran an original C++17 full successor/indegree/period/delay program over all 531441 configurations. It reproduced all six primitive cycle counts (1:1,3:4768,4:294,7:1012,10:504,11:8), 27693 periodic states, all 52 joint table rows exactly, maximal entry 10 and 64 maximizers (32->3,32->11), and all eight 11-cycle representatives (11084,11085,11163,11167,15440,15441,15519,15523). Independent explicit automorphism images from source code preserve all 24 edges and map the first eleven-cycle into all eight distinct cycles. Each vertex fires exactly thrice on each eleven-cycle. Since the computation exhausts a precisely finite state space, unlike sample trajectories this is a complete proof conditional only on reproducible small integer programs and edge specification. Independently reconstructed Git tree from actual 13 blob identities matches SHA 52d309d62ad3eb77eb4bf69c10e38f928290e819.

## originality

PASS

The all-state period and first-entry-time census, orbit counts and automorphism transitivity for the exact labelled Chvatal graph under synchronous threshold-one 3-state Greenberg-Hastings dynamics were not established by inspected earlier graph-theory or general excitation results. General cycle-density/activity theorems determine activity or synchrony conditions, but not the 52-class joint basin census, eight spatially transitive 11-cycles, or sharp 10-step entry split. The published Resultary entry matching this record is the same finding and not an earlier independent theorem. An unindexed numerical census remains a real residual historical-priority risk.

## value

PASS

The Chvatal graph is the canonical smallest triangle-free four-regular four-chromatic graph; its dense yet triangle-free circuits make excitation-wave structure nontrivial. The result supplies the exact first-entry/period census for all 531441 initial states, automorphism classification of period-eleven temporal oscillations and a sharp two-period extremal transient split. The symmetry orbit is more than a raw cycle count and the complete reproducible basin statistics give a mathematically motivated, self-contained benchmark for activity and stabilization on an extremal graph. These are not consequences of the prior general activity theorems, nor a known static graph table. The result does not claim a universal theorem for all regular graphs; its natural complete finite classification meets the same value bar as other exact fixed-graph dynamical invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
