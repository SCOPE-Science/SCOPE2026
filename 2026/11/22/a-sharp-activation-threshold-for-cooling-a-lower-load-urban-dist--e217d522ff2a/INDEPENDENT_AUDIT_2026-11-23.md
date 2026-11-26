# Independent mathematical audit

## correctness

PASS

The frozen equilibrium is uniquely solvable with positive entries of the inverse since the determinant is D0+By-y²>0 on the budget interval. Differentiating the sum gives the increasing numerator Q=qy²+2Cy+qD0-CB and Q(B/2)=qD(B/2). For q>0 its boundary sign decreases strictly as B increases through the stated threshold; for q=0 the optimum is the unique equal split. In the frozen single-source case the hottest cell is always the source cell and its temperature is strictly increasing in y; the exact comparison at B=5, y=1/3 was independently recomputed. The opening words 'opposite boundary allocation' can mislead: the peak optimum is the same all-in-source boundary as the low-budget sum optimum, not the other endpoint. The precise frozen formulas are correct. The submitted checker was read, not executed; its docstring and actual filename differ. The revised proof limits the sources to H1>H2>0 and verifies both optimizers. Implicit differentiation gives T'=M^(-1)(T1,-T2); the first component is strictly positive when T1>=T2 and the second strictly negative when T2>=T1. The sign switch of T1-T2 gives the peak threshold B_p=(1-h)a/h and the unique feasible equalizing split above it, with zero remote allocation at and below it. At equality the balance forces q=tau(B-2y) and therefore E'=-q/D<0; at B=B_p and y=0 this proves B_a<B_p, and at interior equalization it puts the sum optimum strictly to the right. Rationalizing Q's positive zero yields the stated aggregate allocation. The revised 'python3 verify_thresholds.py' replay ran successfully over 180 exact rational budget cases and the displayed strict comparison; it is a finite check, not the continuous proof.

## originality

PASS

The original single-source effect and sum/peak contrast are exact corpus overlap under a parameter relabeling, not independent mathematical novelty. The overlapping records are co-dated, so this does not establish historical order. The revised claim discards that case, retains the genuine unequal-positive-input aggregate result and gives the joint aggregate/peak phase diagram with a second finite threshold and interior equalization. No inspected result implies the revised diagram or its positive-source aggregate classification; unresolved literature limits are stated. This is not a pass for the frozen single-source novelty.

## value

PASS

Both cells emitting heat is the natural general case and changes the peak-optimal structure, rather than constituting an arbitrary parametric slice. Peak cooling starts later and eventually equalizes, yet the aggregate criterion then still assigns more to the lower-source cell. The exact joint diagram distinguishes the intermediate regime of exclusive aggregate activation from disagreement between two positive allocations. It is a useful stationary two-state benchmark independent of the already-covered source-free example, not a quantitative real-city prescription.

The dated certificate retains the supplied scientific assessment, sources and limitations.
