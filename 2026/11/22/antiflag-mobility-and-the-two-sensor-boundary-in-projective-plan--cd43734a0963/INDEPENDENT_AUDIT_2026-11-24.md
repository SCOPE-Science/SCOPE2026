# Independent mathematical audit

## correctness

PASS

The frozen theorem is mathematically correct. Its higher-order pair case analysis bounds the unobserved neighbor count by at least two at every eligible vertex. At order two, only antiflags power dominate. A fresh enumeration using binary triples and dual lines reproduced the 28 pairs and unordered path counts: 84 at distance one; 168 with one and 42 with two geodesics at distance two; 84 with four geodesics at distance three. Slides change the bipartition profile and hence cannot be optimal. The repair in repairs/2/RESULT.md replaces the materially covered Fano mobility claim with the exact all-order first-force threshold, equality configurations and count. For a nonsensor observed vertex x, each selected vertex contributes at most one observed neighbor of x, by incidence uniqueness; a sensor cannot force because all its neighbors are observed. With fewer than q sensors there is no force and fresh coverage is at most (q−1)(q+2)<2(q²+q+1), so γ_P≥q. At equality all q contributions must be present and distinct. For a point x they occupy q different lines in its pencil, and at least one contributor is a line sensor so x is observed. The remaining line is both unique and unobserved. The rule is sufficient by the same observation argument, and duality accounts for line sources. For each fixed point choose its omitted line, then choose independently its line vertex or one of q other points on each remaining line, subtracting the q^q selections with no line sensor. This bijection proves the reported pair count, not a count of distinct placements or target vertices. The repaired verification notes give a replay prescription: form the incidence graph by normalized triples and enumerate all subsets of size ≤q and eligible sources. A separate bitmask check at q=2,3 gave no earlier forces and pair counts 210 and 3,848. The uniform proof does not extrapolate from that test and makes no completion claim at size q for higher orders. Frozen scripts were inspected, not executed.

## originality

PASS

The frozen claim does not pass originality as presented: a distinct Resultary record gives a strictly stronger full Heawood feasibility characterization and the same 28 optima and jump graph with its distance criterion. Same-day dating does not settle priority, but the overlap is demonstrable; the Fano slide and geodesic refinements are short deductions from that characterization and the geometry. The all-order initial obstruction survives. The repaired finding states the sharp first-force budget and classifies and counts all placements with a specified eligible source at that budget, without reasserting Fano mobility as new. The compared sources do not cover the uniform equality and count, and the known order-two endpoint is credited in the repaired text.

## value

PASS

The retained question is the precise boundary at which a small deployment can do anything beyond its initial closed neighborhood, a necessary filter for complete-observation studies. The repaired proof gives a uniform sharp threshold and explains exactly which point/line placements and sources attain it, including their exact profile counts, even without coordinates. This supplies a directly usable search reduction at the minimum starting budget and can distinguish initial activity from complete observation; value does not rest on recounting Fano optima or on an elementary degree bound alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
