# Independent mathematical audit

## correctness

PASS

Independently built each neighborhood from the two shore strides and spoke, then used bitmasks of vertices per color to build each labeled transition map. At each vertex at most one color can occur twice; if no color occurs twice the corresponding bit is inherited from the current state. For each of 59049 ternary states per graph, exact iteration found the first x with F^2(x)=x; it was found by depth 5 (prism) or 7 (Petersen) in every case, excluding longer cycles without assuming any general period theorem. F(x)=x separates period one from primitive period two, whose labeled recurrent states are divided by two for orbit counts. The replay independently matches both frozen histograms and least-encoded witnesses. Binary enumeration of 1024 states per graph gives (14 fixed, 55 primitive two-cycles) on both. In order (fixed, primitive two-cycle orbits, fixed basin, two-cycle basin, unanimous basin, maximum preperiod), the ternary rows are (219,1410,17049,42000,12063,5) and (579,2175,37899,21150,33543,7). Fixed palettte counts are (3,36,180) and (3,36,540). Replay: python3 /workspace/branches/plurality_reproduction.py; the certificate is exact and exhaustive for these finite maps only.

## originality

PASS

Pass is for the joint comparison of the two exact synchronous dynamics, especially the opposition of primitive-cycle count and total oscillatory basin population, not for the known binary baseline, each equilibrium number considered alone, or a general period-two principle. Indexed same-day static overlaps are material and credited; neither accessible statement covers the synchronous basin-period comparison.

## value

PASS

These classical cubic ten-vertex graphs are a motivated comparison because the binary recurrent counts match exactly. The ternary census separates the two not just by a different count, but by a reversed ordering between number of oscillatory attractors and fraction of initial states cycling. The exact labeled basin and first-entry counts give a reusable complete benchmark for that distinction; no family-wide generalization or utility of arbitrary small graph enumerations is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
