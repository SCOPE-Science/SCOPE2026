# Independent mathematical audit

## correctness

PASS

Across each fixed-j cut, the number of h steps leaving equals the number entering because the map is a permutation; the steps are all in the same direction, so this is independent of j. The v argument uses fixed-i cuts. Thus the packing condition is necessary. The image of the additive residue map is g times a whole cyclic group with fibers of size g. Denote a=pN, b=qM. An active band is covered once by the incoming h targets [0,a) and v targets [a,a+b); each has exactly one predecessor in the band, even if one interval is empty. This proves the matching, covers equality and axes, and gives a and b labels of the two types respectively per band. Distinct selected bands give distinct active sets; proper circular translates are distinct because a nonempty proper circular block has a unique entering boundary, also after rescaling by g. For the phrase 'one valid local cycle permutation', the construction really has one cycle per band: gcd(a,b) divides MN by coprimality of p,q (check prime valuations), so it equals g. The local residue rotation by a/g cycles through (a+b)/g residues; each full residue revolution displaces a site by (b/g,-a/g), of order g since gcd(p,q)=1. The word-linear selector computes one residue per site; setup is also within O(MN). At the origin all choices are d. For spins, each dual choice marks one same-spin edge per triangle. The local even flip parity yields a flat Z2 edge assignment, with periods M-H and N-V modulo 2; zero periods give precisely two spins by connectedness. Independent brute force separately enumerated matchings and ground states on 3x3, 3x4, 4x3 and 4x4, checking support, both bounds and the parity-filtered factor two. Replay python3 /workspace/checks/4.py; output /workspace/checks/4.txt. The frozen Newton recurrence and construction code were inspected, not executed; the finite checks are not the all-period proof.

## originality

PASS

Pass is for the explicit residue selector together with its quantitative band-subset and circular-shift witness families. Qualitative finite saturation alone is not credited as new, and the spin lift and factor two are prior.

## value

PASS

It gives an output-linear, no-search witness for any feasible finite slope, resolves the concrete support gap in the inspected source constructively, and makes two quantitative finite-degeneracy guarantees including on admissible spin sectors. Positivity of a characteristic polygon or the mere availability of a coefficient formula would not give these witnesses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
