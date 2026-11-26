# Independent mathematical audit

## correctness

PASS

A monochromatic petal is absorbing, and a mixed one locks precisely when the current hub equals one endpoint. After one update every remaining mixed petal uses the other two colors. If the hub moved, the second update locks them all, leaving an idempotent hub update; if it stayed, petals are unchanged at the second update, and any new hub color was a unique winner which subsequent locks only strengthen. I independently enumerated all labelled 3-color initial states for m=1 through 5 by building the graph and, at each vertex, counting old neighbor colors and retaining the old color on a nonunique maximum. Iterate until the first unchanged step and bin by prior updates. The tuples for times 0–3 were (9,18,0,0), (45,126,72,0), (153,1062,972,0), (789,10926,7968,0), (3849,81918,87540,3840), with no unsettled states. The m=5,6,7 witnesses check by direct petal scores, and adding one constant petal of each color adds the same 2 to every hub score, covering every larger size. With hub 0 the stable petal types give counts (2k,2a+t,2b+t); incumbent retention is exactly the stated union of conditions, including ties that exclude the hub. Under uniform draws over the five admissible ordered petal types, a=b is a zero-sum event with increment law (1/5,3/5,1/5) on (-1,0,1), so the span-one local limit gives sqrt(5/(4 pi m)). The hub-leading sector outside this event is bounded by Hoeffding at exp(-m/50), using mean -2/5 and range length 4. For i.i.d. initialization, the good event A>B+D and A>C+D puts 0 strictly ahead even if every residual mixed petal subsequently locks for the initial challenger. Each inequality fails with probability at most exp(-2m/81) by its summands' mean 2/9 and range length 2. On the good event T is at most 1 if the first hub does not move and exactly 2 if it does; independent color symmetry and the O(m^-1/2) initial tie probability give the limits since T=0 is exponentially rare.

## originality

PASS

The nearest exact graph comparison is the binary friendship-graph census; the nearest exact three-state graph comparison has a cyclic successor rule. Neither gives the closed ternary windmill dynamics with ties retained, its sharp exceptional boundary, or its equilibrium and random-time laws. Same-rule nearby records address different neighborhood geometries. Generic concentration and local-limit tools are not claimed new.

## value

PASS

The windmill is a natural shared-hub family on which binary and ternary rules behave differently. The theorem identifies the first size giving an additional transient round and explains why those worst cases become rare. The tie sector determines a specific square-root correction to the equilibrium entropy, not just an exponential rate or a small-instance count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
