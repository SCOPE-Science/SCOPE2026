# Independent mathematical audit

## correctness

PASS

Independent reconstruction by enumerating the available line submasks for each fixed point set gave the occupation counts (1,14,70,154,147,56,14,2), parities 232/226 and configuration orbits 13/14 under the 168 incidence-preserving linear maps. The invariant odd-to-even block has a kernel, so the full odd-by-even block has rank at most 225 and the chiral Hamiltonian has nullity at least 8. Exact integer ranks at 0,1,-1,2 were 155,216,216,225, respectively; point-occupation parity conjugates t to -t. A further check at zero: point slices with 0,1,2,4,7 available lines occur 64,35,21,7,1 times. On each slice the line flip hypercube has zero multiplicity binomial(k,k/2) for even k and zero for odd k, giving 64+42+42=148. Without executing the frozen code, /workspace/heawood_review_check.py read the supplied minor indices, reconstructed the entries and compared both exact integer determinants (FLINT) to the displayed polynomials on 226 distinct integers -25 through 200, in two batches (outputs /workspace/heawood_review_check_a.txt and /workspace/heawood_review_check_b.txt). Both sides have degree at most 225; this independently certifies both identities, not just sampled ranks. At nonzero real t, Q(t)/t^4 is 1440u^2+7125u-19898 for u=t^2+t^-2≥2: increasing there, with value 112 at 2. The two remaining factors vanish at disjoint parameter sets. Thus some 225-minor survives precisely where required, and the formula 458-2rank gives the stated 148/26/8 on the full space. This is an exact finite algebraic check for the specified Hamiltonian, not a formal proof certificate or a claim for other dynamics.

## originality

PASS

The general PXP blockade model, spectral reflection and symmetry-resolved chiral index are known. The supported distinct result is the exact Heawood-specific one-parameter nullity classification, especially that no other real nonzero point-to-line drive ratio can change the generic nullity. The line drive is fixed at one; the exact same-ID catalogue hit is the finding itself. The inspected analogues and primary sources do not supply the full kernel formula.

## value

PASS

The finite graph and perturbation are canonical: the Fano incidence structure distinguishes two shores, and changing their relative drive preserves collineation symmetry while testing equal-shore enhancement. The exact all-real count separates the ordinary parity bound of six, the invariant-sector bound of eight, and the extra eighteen at equal magnitude, with no undetected real exceptions. This is a useful finite benchmark of a symmetry-preserving blockade spectral problem, not a stand-alone claim about arbitrary arrays or the dynamics of all states.

The dated certificate retains the supplied scientific assessment, sources and limitations.
