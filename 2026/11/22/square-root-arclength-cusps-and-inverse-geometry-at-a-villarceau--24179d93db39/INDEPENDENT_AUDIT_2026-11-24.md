# Independent mathematical audit

## correctness

PASS

The frozen proof does not establish the Finding as written: equation (6) contains an extra factor a on both sides, inconsistent with the stated angular coefficients for general radii. The transition from a truncated node equation to the uniform length defect is also only sketched. This is a defect in the written proof, not evidence that the stated angular coefficients are false. The repaired proof has the same claim and derives the normalization from exact smooth node coordinates U=√(r²+k)u, V=(u²+v²−a²)/2+k. Direct substitution yields Q/4=V²−U²+a²k−k², with smooth metric having node weights 1/r, 1/a. With η=√|a²k−k²|, each quadrant is a half-hyperbola, with longitudinal weights exchanged across k=0. Subtracting the critical ray and its lost vertex segment and rescaling gives ηJ, with integrable lower singularity and quadratic tail. The stated elliptic change of variable and F′(t)=tK(t) give J=−mF(p/m). In the fixed chart squares, varying k in the metric costs O(|k|); the spatial metric correction for the difference of the smoothed and critical lengths is bounded by integrating Cη²(1/x+1/√(x²−η²)), including an O(η²) missing-segment correction. The regular complementary arcs have O(|k|) changes with one-sided smooth cutting points. There are eight half-branches total and mη∼(R/r)√|k|, with no additional factor a. The angular conversion k∼2ra(β−β*) then agrees with both original coefficients. Positivity and the side comparison follow from monotonic F; the ratio is strictly decreasing with endpoints ∞ and 0, and the recovered scale follows by substitution. Both endpoint sections and zero length of the two isolated crossings are consistent with the chosen measure. Fresh exact-radial-quadrature spot checks (not execution of the uploaded checker) at (R,r)=(2,1) predicted C_−≈6.04965949 and C_+≈20.00955644; approach ratios (4πR−L)/√ε at ε=10⁻³, 3·10⁻⁴, 10⁻⁴, 3·10⁻⁵ were respectively 5.70191, 5.86004, 5.94045, 5.98994 from below and 20.31699, 20.18700, 20.11469, 20.06806 from above. To replay, integrate both positive radial branches with the derivative density in (1), using quadrant symmetry and a quadratic substitution from the upper angular endpoint on the plus side. The repaired verification notes distinguish chord sums on the same radial parametrization from an independently derived contour; the original numeric source was inspected, not run.

## originality

PASS

The repaired proof preserves the precise torus-specific boundary-length coefficients and the inverse determination of both radii from those coefficients alone. The distinct contribution is not the classical Villarceau circles, the elliptic functions, or square-root length behavior from general nodal smoothing. The closest indexed nodal-arclength paper is a genuine conceptual overlap; its available statement does not provide this torus normalization or recovery law. The plausible older geometry sources remain a bounded access risk.

## value

PASS

At the classical change of topology the perimeter need not follow the area cusp. The exact torus coefficients quantify the two-sided loss, detect a particular equal-loss shape, and recover both geometric radii from local length observations alone. A mere square-root exponent or the classical circle configuration would not supply this inverse geometry. Repair preserves that motivated precise invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
