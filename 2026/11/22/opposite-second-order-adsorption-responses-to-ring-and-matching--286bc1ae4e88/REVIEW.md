# Independent mathematical audit

## correctness

PASS

The vacant set only shrinks; after each deposition the first active independent Poisson clock wins with probability its rate divided by the total active rate. For an ordering of a fixed perfect matching, the product of these factors is the probability of that exact history. Independently generated all perfect matchings by matching the least vacant vertex recursively (33 matchings), and summed their histories via forward Taylor-coefficient propagation over each matching's subsets, weighting choices by all active edges, not just those in that matching. At delta=t-1 the edge-probability coefficients are (1,b-a,a^2-ab)/k, where b is its mark indicator and a is the active marked fraction. Readout of value, derivative, and twice the quadratic coefficient gave (903422/3840375,0,276830066540632837/4793798789772300000) for the ring and (903422/3840375,0,-561926341371011/43579988997930000) for spokes. Forward homogeneous propagation over 7314 occupied-state masks also recovered the entire terminal law: 6:868823/6912675, 7:2008042/3142125, 8:903422/3840375. Replay: python /workspace/replays/adsorption.py. With vertices numbered u=0..7, v=8..15, the verified automorphism (image list) [0,8,11,3,4,12,15,7,1,13,14,2,5,9,10,6] carries outer edge (0,1) to spoke (0,8); rotations and u_i ↔ v_{3i} relate all three edge types. Positive total active rates make the finite probabilities analytic near 1, proving the two strict local extrema only, not any global claims.

## originality

PASS

The specific same-graph ring-versus-spoke curvature contrast for GP(8,3) remains distinct on inspected evidence. Geometry-signed adsorption rate effects and nonmonotone weighted dimer jamming are not themselves new. The materially overlapping indexed statements are credited, without claiming relative priority from their dates.

## value

PASS

On a standard symmetric cubic graph, the same number of perturbed edges has the same first-order response at uniform rates, yet changing their arrangement reverses the local effect on full occupancy. The exact sign contrast distinguishes ring and matching geometry without changing graph or total rate perturbation. This makes a useful patterned-rate benchmark beyond a homogeneous terminal table, without implying a general curvature law or global optima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
