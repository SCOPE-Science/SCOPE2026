# Independent mathematical audit

## correctness

PASS

For p=6m+5, use f^{(p−2)/3}/y^p for 1/y² and f^{(2p−1)/3}/y^{2p} for 1/y. The Cartier coefficient test and the parity of f leave only the two inverse-Frobenius arrows swapping dx/y and dx/y², with coefficients P_p and Q_p, and annihilate x dx/y². With D=a²−4 and h=m+1, the substitution D^h Q_p in the large coefficient equation leaves the Q_p equation plus −8hp D^{h−1}Q_p before reduction, so the remainder vanishes mod p. For the polynomial of degree d and parity d the indicial multiplier at degree d−2r is 4r(n−d+r), a unit at all required steps, proving proportionality with the stated leading ratio. Deg Q=m, its binomial boundary values are units, and a multiple root of multiplicity 2≤r≤m<p would force D(a₀)r(r−1)=0. Thus both arrows vanish on exactly m simple smooth roots, or both are nonzero giving stable rank two. Cartier rank zero is superspecial; off the roots p-rank two leaves only the unique elliptic local-local EO component with slopes (1/2,1/2). At p=5 the root case is empty, as made explicit by Q_5=1; both cases occur for p≥11. In the split congruence class the ordinary j=0 elliptic quotient rules out superspeciality for this pencil, not for arbitrary genus-three curves. The complete invariant j=(4−a²)/4 makes the parity/orbit count ceil(m/2). Independent polynomial multiplication and gcd at p=5,11,17,23,41,101 replay with python3 /workspace/review-evidence/reproduce.py 4 (SymPy); the supplied code and VERIFY_OK log were inspected, not executed.

## originality

FAIL

Resultary 9e738692b754 already states the same uniform theorem, including both Cartier arrows, the same factorization with the exact constant, degree, all m simple smooth roots and the two cases for p-rank, a-number and Newton slopes. The change in extraction index is reciprocity of a palindromic quadratic. The unmarked count is an immediate use of the published complete invariant, and the other residue class has already been analyzed in related catalogue records. No unavailable source is the basis for this failure.

## value

FAIL

The all-prime explicit superspecial divisor and strata are valuable questions but are already addressed for this exact pencil. The only surviving apparent extensions are the class tally from sign pairing and the immediate split exclusion or EO interpretation, not new independent structure. The different algebraic organization does not produce a fresh invariant, uniform refinement or unresolved example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
