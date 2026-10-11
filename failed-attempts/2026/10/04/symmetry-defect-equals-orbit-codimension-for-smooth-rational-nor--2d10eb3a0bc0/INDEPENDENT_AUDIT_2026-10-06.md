# Independent mathematical audit

## correctness

PASS

For \(S=\mathbb P(E)\) with \(E=\bigoplus_i\mathcal O_{\mathbb P^1}(a_i)\), the standard projective-bundle automorphism sequence gives dimension \(h^0(\operatorname{End}E)-1+3=h^0(\operatorname{End}E)+2\). Since \(\operatorname{End}E\) has rank \(k^2\) and degree zero, Riemann--Roch yields \(h^0-h^1=k^2\), and splitting cohomology gives \(h^1=\sum_{i>j}\max(a_i-a_j-1,0)\). Harris's degeneration order makes the balanced orbit dense in the fixed-\((d,k)\) smooth-scroll locus, so orbit codimension is the difference from the balanced orbit dimension, exactly \(h^1(\operatorname{End}E)\). The elementary inequality in the package correctly maximizes this defect uniquely at \((1,\ldots,1,d-k+1)\). The package checker independently verifies the formulas on 2212 positive splitting types and the published surface specialization.

## originality

FAIL

The novelty-bearing package is mechanically implied by standard published ingredients. The projective-bundle automorphism exact sequence is already printed in the scroll literature, and general rational-normal-scroll sources give the same automorphism-dimension formula from the splitting data. Harris's degeneration theorem orders fixed-degree scrolls by balance and identifies the balanced type as dense; modern restatements identify the unique least-balanced degeneration. Once these are combined, the equality between symmetry excess and orbit codimension is the immediate orbit-stabilizer dimension identity, while the claimed extremal type is the terminal element of the same degeneration order. The package's short inequality supplies a clean numerical restatement but does not escape implication-level coverage.

## value

FAIL

The equality is a clean synthesis, but after the standard automorphism formula and balance degeneration theorem are in hand, orbit codimension follows by the elementary orbit-stabilizer dimension formula and the extremal type follows from the same degeneration order. This is useful exposition rather than an independently substantial structural gap under the common value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
