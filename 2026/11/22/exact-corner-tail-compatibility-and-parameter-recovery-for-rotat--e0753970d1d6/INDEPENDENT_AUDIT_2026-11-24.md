# Independent mathematical audit

## correctness

PASS

The Clayton r-coordinate lower marginal at common threshold t is exactly t[r−(r−1)t^θ]^(−1/θ), so its first-order coefficient is r^(−1/θ). A lower–upper pair has mass t−Cθ(t,1−t)=O(t^(2+θ)) by factoring t and expanding; an upper–upper pair has mass O(t²) by bounded density near (1,1). Thus every wrong sign assignment on at least two constrained coordinates is o(t). For m≥3 the sole matching numerator orientation is s, whereas the conditioning event has the two matching orientations s and s⊕e_i. Dividing the first-order coefficients gives exactly hπ_s/(π_s+π_{s⊕e_i}), with a strictly positive denominator. Opposite directions share that denominator; their sum recovers h and hence the unique θ>0. Taking the ratio of the opposite coefficient to the given one gives π_{s⊕e_i}/π_s. Positivity, reciprocal reversal and the square relations make path products independent: exchange adjacent distinct flips using a square and remove repeated flips via immediate reversal, reducing to the ordered list of flipped coordinates. The connected cube then yields unique positive normalized weights. The modified m=3 example has a ratio 5/3 on the changed edge and unit ratios on the other edges of a square, so it passes the edge-sum test but is not realizable. The independent exact-rational computation python3 /workspace/checks/frozen_math_checks.py 3 verifies inclusion–exclusion for the uniform three-dimensional example (θ=1) at widths 10^−3, 10^−5 and 10^−7, giving conditional ratios 0.3320680454, 0.3333205568 and 0.3333332056; convergence for all admissible inputs is analytic, not inferred from these ratios.

## originality

PASS

The rotations, mixture model and intended conditional observables are prior. Against the inspected papers, the correctly normalized common-parameter formula and intrinsic compatibility and unique inverse theorem survive. Pan–Nieto-Barajas–Craiu's v3 Eq. (3) prints a nonshrinking upper interval inconsistent with the immediately following example. The comparison is to the intended extreme bands, and the all-lower test below avoids that typographical ambiguity altogether.

## value

PASS

For a preexisting multivariate extreme-dependence model, the theorem corrects the normalization of a specified conditional observable and shows that those limit data alone identify all the mixture weights and the shared parameter. The face relations give falsifiable constraints beyond local consistency; the explicit incompatible table demonstrates their need. These are substantive statements about model calibration and restrictions, not a claim about sample efficiency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
