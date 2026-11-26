# Independent mathematical audit

## correctness

PASS

Connected support at fixed edge count has j doubled right vertices and a nonempty incidence at every other right vertex; one doubled vertex suffices to join the two left vertices. The Walsh local factor is a_i b_i for a double and a_i+b_i for a single. Thus all d discordant positions must be doubled. Pulling out the discordant factors −1 and the product of all concordant signs leaves the elementary symmetric sum of order j−d of the concordant signs, i.e. K_{j−d}(h;n−d), with 2^{n−j} from the singles. Counting frequencies gives the stated rank and singular values with counting-measure convolution: d=j attains the least positive magnitude and the trivial character the largest. The case j=n has no forced zeros and consists of one graph; j<n admits d=j+1. At j=2 the d=1 root requires odd n, while d=0 has roots (n±√n)/2 iff n is square, since 2K₂=(n−2h)²−n. These are disjoint frequency classes, and the two roots for a square n≥4 are both valid. Ran independently written /workspace/branches/reproduce_fixed_excess.py with python3, checking all signed coefficients for (n,j)=(2,2),(3,2),(4,2),(4,3),(4,4),(9,2). The odd-square case had 168 zeros at d=0, 1260 at d=1 and rank 22124. The frozen reproducibility instructions name checks/check_unicyclic.py, but the packaged file is checks/check_bicyclic.py; inspection shows it in fact checks the unicyclic formula along with all fixed-excess signed spectra in its finite range. This path error does not invalidate the theorem.

## originality

FAIL

Demonstrated coverage by the distinct 2026-11-16 Resultary finding on fixed-excess bipartite spectra, not merely by the earlier j=1 tree result. The predecessor uses n+1+k edges and 0≤k≤n−1. Substituting k=j−1 matches every graph, signed Walsh factor, frequency count, rank and sharp positive spectral bound. Its k=1 classification already gives both rank corrections, including the perfect-square correction. No independent remainder was identified in the frozen claim.

## value

FAIL

The spectrum and its arithmetic classification are useful invariants, but this submission independently adds no new invariant, theorem, or interpretation. Relabelling the earlier excess parameter, noting its immediate invertibility endpoint, and reproducing the known census numerically do not constitute a surviving valuable finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
