# Review of the Pappus semitotal-domination exchange theorem

## Correctness: PASS

The exact domain is the cubic eighteen-vertex point-line incidence graph specified by the nine Pappus triples, and only six-element semitotal dominating configurations are used. The lower bound \(\gamma_{t2}\ge\lceil36/7\rceil=6\) is the cited degree lemma of Goddard–Henning–McPillan; nine explicit total dominating six-sets attain it. An elementary counting argument shows all total six-sets are efficient open dominating, and the displayed incidence triples classify them as a \(3\times3\) grid. The rigidity lemma excludes every single-vertex replacement from these nine sets by triangle- and square-freeness.

For the remaining classification, two different standalone graph representations and algorithms enumerate all \(\binom{18}{6}=18564\) candidates, obtaining \(297\) admissible six-sets and the same sharp exchange data. The LCF bitmask program generates neighbors by replacement; the incidence program uses unordered pairs of subsets. Both compute \(1026\) jump edges, \(432\) slide edges, one mobile component of size \(288\), and nine isolates, with jump radius/diameter \(6/6\) and slide radius/diameter \(8/10\). The independent orbit program checks \(216\) automorphisms and five orbits of sizes \(9,18,54,108,108\). The three verifier scripts and their recorded outputs are embedded with the theorem.

Limits: the numerical connectivity and distance statements are computer-assisted **complete finite proofs**, not symbolic statements about all cubic graphs. There is no assertion of a global diameter for either disconnected full exchange graph.

## Originality: PASS, with residual priority risk

The directly inspected author manuscript *Semitotal Domination in Graphs* (Goddard–Henning–McPillan, Utilitas Mathematica 94, 2014) establishes the definition and degree bounds, as well as extremal and complexity results. It does not classify the Pappus six-sets or their token-exchange graphs. The full-text arXiv paper *On the semitotal dominating sets of graphs* (Alikhani–Zaherifar, arXiv:2107.01424) treats named graph families and semitotal counting polynomials, without the Pappus graph or the claimed exchanges.

The related *On matching and semitotal domination in graphs* (Henning–Marcon, 2014, DOI 10.1016/j.disc.2014.01.021) was available only through its abstract and metadata. It concerns characterization and bounds, not the Pappus reconfiguration in the accessible material. Its unavailable full text is recorded as a risk, rather than falsely described as completely checked.

Henning–Marcon (2016) proves an upper bound for claw-free cubic graphs, but the girth-six Pappus graph has an induced claw centered at each vertex and is outside the stated hypothesis.

Mathematical-record searches and recoverable prior claims concerning Pappus domination, locating/identifying codes, zero forcing, edge-colouring, matchings and matching complexes do not imply the theorem: their feasible configurations or moves are different. The known Pappus ordinary-domination number \(5\) and prior locating-code six-set results do not enumerate the \(297\) semitotal minima. The nine efficient total dominating states may independently be known, but the theorem's original target is their precise isolation inside the full semitotal exchange network and the exact connected mobile sector, metrics and orbits.

Risk: an unindexed enumeration or inaccessible specialized paper could contain these exact state counts, exchanges or stronger coverage. Searches alone do not establish global priority, and no such claim is made.

## Value: PASS

Semitotal domination interpolates between domination and total domination, so its optimal configurations naturally test how a weaker coverage condition changes the *mobility* of efficient total placements. On a canonical symmetric incidence graph, all nine efficient open dominating sets are provably frozen while the other \(288\) minima form one connected exchange sector under either movement rule. The exact jump/slide diameter separation \(6\) versus \(10\), the five automorphism orbits and the \(3\times3\) geometric organization give a useful structural benchmark, not merely a recomputation of a familiar domination number. The general rigidity lemma explains the exceptional states beyond this one graph.

## Review status

Self-review: passed. Independent audit: not yet performed.
