# Independent mathematical audit

## correctness

PASS

For fixed C, the only changes to D are UC for the left action and UC+CV for the double action, with U,V arbitrary. Independently the left quotient is restriction of D to ker C, and the double quotient is the map ker C→coker C induced by D. Both maps onto their Hom spaces are surjective. For the second, if D carries ker C to im C then choose V lifting D on ker C through C; D−CV vanishes on ker C and is UC for some U. This yields exactly the asserted sizes and counts, including C=0 and full rank, over any field of order q. Rank-r matrices are counted by the image Grassmannian times the surjection count. With P_j=∏_{i≤j}(1−q^{−i}), stripping off q^{2mr−r²} leaves H=P_m²/(P_r P_{m−r}²)=P_∞^{-1}+O_q(q^{−min(r,m−r)}), uniformly, by the product tail and P_j≥P_∞>0. Left weights have exponent 5m²/4−(r−m/2)². In the middle half the H-error is O_q(q^{−m/4}), and the Gaussian mass on the omitted tails of the appropriate integer/half-integer lattice is negligible, proving both the theta total and the stated TV error. Double weights all have exponent m², and the sum of absolute H deviations is O_q(1), yielding the total and O_q(1/m) TV to discrete uniform. The uniform element nullity bound follows by a union bound over k-dimensional kernel subspaces, at most P_∞^{-1}q^{k(m−k)} of probability q^{−mk} each. This implies concentration of the scaled rank at 1, not full rank with probability tending to one. Substitution into the log-orbit sizes gives the three limits; boundedness gives the expectation 2/3 for the double law.

## originality

PASS

The distinct result is the comparison of three leading-rank laws in the same cubic full-matrix radical, including the parity-theta versus continuum-uniform laws with quantitative errors. General superclass theory, the circle-brace construction, and classical matrix-rank enumeration are inputs. A different same-day unitriangular calculation gives a real qualitative half-rank overlap, not the same algebra or the same rank-resolved comparison.

## value

PASS

Equal weight on elements, left orbits, or double orbits is a natural choice in the same canonical radical; these are not arbitrary restrictions on rank. Comparing their exact spectra isolates a genuine change of scale: near-full rank for points, bounded parity-dependent fluctuations around half rank for left orbits, and a spread across the entire interval for double orbits. The cancellation yielding the third law and its quantitative distinction from the others make the invariant useful for recognizing sampling bias; standard matrix-rank enumeration by itself is not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
