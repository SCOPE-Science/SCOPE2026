# Independent mathematical audit

## correctness

PASS

The repaired theorem concerns fixed n>=3. Conditioning on retained exact sites splits the Gaussian residual into independent bridge pieces, including zero gaps at coincident sites. Double integration gives h^3/12. The all-surviving sum of strictly convex cubes of affine gaps is strictly convex because the gap vector determines the placement; its positive weight gives uniqueness even on the closed boundary. Reflection then fixes the minimizer. A single retained site contributes (x_i-1/2)^2/4 over the midpoint, and the remaining change has absolute bound (n-1)r^2||x-m||_1/4, since active derivatives are bounded by 1/4 and summing the probabilities for a given survivor accompanied by any other gives r(1-q^{n-1}). This gives ||x*-m||=O_n(r). The pair variance changes by -r(y_j-y_i)/16+O(r^2) at scaled locations m+ry. Terms with at least three survivors are O_n(r^4) in risk difference, uniformly for bounded y. The limiting objective has unique ordered minimizer y_i=(2i-n-1)/8, so boundedness, uniformity and comparison with that trial design establish the claimed full convergence. The frozen two-node formula is also mathematically correct but is not claimed in the repair. Independently checked 33 finite integer-coefficient risk polynomials using consecutive-survivor probabilities, with scaled offsets and n=2..12; replay /workspace/branches/spectral_design_replays.js, dropoutCheck. The packaged script was inspected, not run. Its covariance matrix checks are floating point, not rational as implied by the frozen verification prose. The revised notes describe the unchanged checker accurately.

## originality

PASS

The original Finding bundled an exact two-node law which is explicitly covered by a broader, distinct same-day catalogue record; neither chronological precedence nor duplication of the all-n claim follows. The repaired files claim only uniqueness and the high-dropout spacing law for fixed n>=3. The nearest located all-size result uses squared gaps and gives a different coefficient. No inspected result gives or implies the repaired fixed-size cubic-gap law. This is a bounded best-of-knowledge assessment.

## value

PASS

The repaired result resolves the microscopic geometry of the entire optimal design at arbitrary fixed budget at least three. A midpoint limit or a deterministic equal-spacing theorem alone does not say whether sensors actually separate. The first nonzero slope quantifies the effect of rare simultaneous observations and distinguishes estimating an integral from reconstructing the path or minimizing worst-case coverage radius. This is a useful exact asymptotic design law independent of the removed two-site formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
