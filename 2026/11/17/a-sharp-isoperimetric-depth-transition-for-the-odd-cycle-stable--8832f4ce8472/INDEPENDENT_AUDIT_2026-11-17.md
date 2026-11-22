# Independent mathematical audit

## correctness

PASS

For every odd n≥5, in fixed Euclidean coordinates, F_n={x≥0,x_i+x_{i+1}≤1}, P_n(s)=F_n∩{∑x_i≤(n−s)/2}, 0≤s≤1. The transfer integral operator Tf(u)=∫₀^{1−u}f(v)dv has complete cosine eigenfunctions and eigenvalues 2(−1)^j/((2j+1)π), so V(F_n)=E_{n−1}/[2(n−1)!]. Coordinate facets are isometric to path fractional polytopes with area E/(n−1)!, and divergence with radial origin shows each edge facet area √2V(F_n), giving S(F_n)=nE(1+1/√2)/(n−1)!. With y_i=1−x_i−x_{i+1}, odd n yields det(I+P)=2 and removes exactly the homothetic simplex ∑y_i<s, y_i≥0, of volume s^n/(2n!), base area s^{n−1}√n/(n−1)! and n removed old-edge facet areas each s^{n−1}/[√2(n−1)!]. No coordinate-facet interior is removed for s≤1. Hence V=E/[2(n−1)!]−s^n/(2n!) and S=nE(1+1/√2)/(n−1)!−(n/√2−√n)s^{n−1}/(n−1)!. Normalization gives I(s)/I(0)=(1−a s^{n−1})/(1−b s^n)^((n−1)/n) with a=(1−√(2/n))/[(1+√2)E], b=1/(nE); derivative has exact sign of bs−a. Thus n=5 has unique interior minimum s*=0.761209517..., while every odd n≥7 decreases to unique s=1 minimum; full cut worsens relative to s=0 only at n=5. Expanding as E→∞ proves E(1−I(1)/I(0))→√2−1. Independent numerical evaluation of exact formulas checked n=5,7,9 signs; inspected exact determinant/Gram checker tests n=3,5,7,9 without taking finite checks as proof.

## originality

PASS

Classical odd-hole inequality and Bärmann–Schneider convex-hull characterization establish the endpoints, and the Oct25 published antiperiodic-Brownian cap result gives exactly the removed simplex volume and fractional ambient volume. Both are fully credited as prerequisites. The complete Oct25 text was inspected directly and contains no Euclidean surface-area evolution or optimized continuous cut depth. The new claim calculates n old boundary facet loss and one new facet gain in Euclidean area and proves an unexpected n=5 vs odd n≥7 minimizer transition. De Vries et al. analyze extended polyhedral descriptions, not this scale-invariant metric. Resultary search retrieved related surface-area papers of different polytope families and the target record, but no stronger same-parameter cut-depth phase diagram. Unindexed equivalent metric corollaries remain possible.

## value

PASS

The isoperimetric area-to-volume quotient is a natural scale-invariant metric for a standard fractional-to-integral cutting-plane interpolation. A full analytic depth evolution finds a counterintuitive strict partial optimum for the pentagon, a sharp switch to full-cut optimality in all larger odd cycles, and the scaled high-dimensional improvement. This is a motivated complete one-parameter geometric optimization, not a known volume-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
