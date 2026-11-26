# Independent mathematical audit

## correctness

PASS

The horizon is inclusive, so S_0=1−h. With u=1−2a and w=2−2b the four survivor-domain intervals have lengths u,3a−1,2−3b,2b−1. The two intermediate image endpoints 4a−1 and 4b−2 lie strictly in the hole, so the source images cover exactly the claimed destination intervals, up to null endpoints. The four-state inverse-branch operator sends (1,n+1,n+1,1) to (1,n+2,n+2,1)/2, giving density 2^(−n)(1,n+1,n+1,1) at time n. Integrating its outer and inner components gives 2^(−n)[2h+(n+1)(1−3h)], hence the stated tail and, by summation, the mean 4−8h. Normalization gives outer mass 2h/[1−h+n(1−3h)] tending to zero and the two inner weights in the statement, with convergence in total variation. The examples both have width 1/4 and respective left weights 8/25 and 14/25; reflection of the first would instead give (39/100,64/100). The partition endpoints u,a,b,w eventually hit the hole under the literal map, so they do not add surviving itineraries. An infinite survivor either alternates forever between the two outer pieces, stays in an inner piece, or exits the outer cycle at one finite time to one inner loop. Expansion gives at most one point per itinerary, and the periodic points are exactly those stated. The number of finite admissible itineraries grows only linearly; each itinerary has a bounded number of orbit-separated points at any fixed separation scale, yielding zero entropy. The all-parameter replay is the image and density argument (RESULT.md lines 37–77); the exact inverse-interval checker was inspected, not executed, and its finite samples are not used as proof.

## originality

PASS

Credit the prior exact diagonal and boundary-hole results, including the previously computed terminal profile at one boundary hole. A distinct record also gives all-horizon laws for asymmetric holes, but with different widths and different laws. The surviving distinct result is the all-horizon equal-width identity on an open off-diagonal cell together with continuously varying terminal weights; neither the symbolic plateau literature nor the inspected exact families give that result.

## value

PASS

The natural inverse question is whether complete escape-time data identify the state conditioned on survival. The explicit open cell offers a stronger counterexample than equal exponential rates or a symmetry: all finite escape probabilities agree at fixed width, but a fixed observable, the terminal probability on the left half, can be varied strictly. The four-state calculation also makes the mechanism transparent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
