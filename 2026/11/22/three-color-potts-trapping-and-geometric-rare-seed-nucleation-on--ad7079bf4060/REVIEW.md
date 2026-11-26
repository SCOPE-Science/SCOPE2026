# Independent mathematical audit

## correctness

PASS

A vertex recoloring changes the agreeing-edge count by its new same-color neighbor count minus its old count. Every allowed change increases this integer, so the chain is acyclic up to absorption and has at most fifteen jumps. Its embedded jump chain chooses uniformly among allowed ordered recolorings, not first among vertices; terminal values therefore propagate uniquely in descending agreement score. A fresh pentagon/pentagram/spokes implementation enumerated all 59,049 labeled states, validated strict score increases on all transitions and propagated exact named terminal probabilities. It reproduced the (population, count, score) rows ((10),3,15), ((5,5),36,10), ((5,3,2),360,8), ((4,3,3),180,7); all four frozen exact uniform-initial fractions and the exact nonconsensus total 1130139522395301525645463/3686384171559531241800000 agree. For all 360 placements it reproduced the five adjacency counts 90,120,30,60,60 and found nonconsensus only in class (0,1), with probability 11/270 and terminal named populations (5,5,0). Thus the uniform-placement mean is 11/810. This independently verifies the agreeing-edge column and the complete seeded terminal law, which are not both reported by the packaged diagnostics. Replay with Python 3 using /workspace/branches/4bd1aaed-95ae-4737-9ff8-939e8c296b3d/independent_petersen_check.py; exact output and each named placement law are in independent_petersen_results.json in the same directory. The finite check exhausts the specified graph and dynamics, not other graphs or rates.

## originality

PASS

PASS is supported by the distinct kinetic content: the full four-class rate-one-per-recoloring absorption probabilities and the placement-selective mixed-minority law. Do not credit the bare total 579 or its one-/two-/three-color split as distinct from the verified same-day Resultary fixed-point census. Its more detailed energy/population breakdown is a useful accompanying census, not the sole basis for originality.

## value

PASS

On the Petersen graph, a natural minimal cubic girth-five example, a complete strict-cooling kinetic benchmark distinguishes which static minima are actually reached and with what mass. In particular the (7,2,1) selection rule isolates an exact difference between identical populations arranged in different local geometries, including the disappearance of the third color on the nonconsensus paths. This is meaningful without extrapolation to other graphs and is not merely the overlapping fixed-point count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
