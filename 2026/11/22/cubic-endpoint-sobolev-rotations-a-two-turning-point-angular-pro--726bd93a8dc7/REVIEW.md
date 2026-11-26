# Independent mathematical audit

## correctness

PASS

Reflections and quarter-turns act by signed permutations of the derivative slots. Reducing to 0≤φ≤π/4, write c=cos φ, s=sin φ, r=s/c. The cubic xxy column of the chain-rule matrix is (3c²s,c(c²−2s²),s(s²−2c²),3cs²), and the xyy column has the same absolute sum. In units of c³, this sum is 3r+|1−2r²|+r(2−r²)+3r², giving the two numerators P₋=1+5r+r²−r³ and P₊=−1+5r+5r²−r³. The pure cubic maximum and first-order maximum are c+s; the second-order maximum is (1−r²+4r)/(1+r²). Squaring to compare this with the cubic mixed sum, the respective numerator differences are 2r[3r⁴+4r²+1+6r(1−2r²)] and 2r(26r²−r⁴−9), both positive for r>0 on their branch. The second-order term bounds the first. The chain rule thus gives L₃ as an upper bound. To prove equality, use the same-order Ornstein theorem on D_xxy against the other three cubic monomials. A sequence concentrates the cubic L¹ mass in D_xxy; dilation suppresses orders 0–2, and rowwise reverse triangle inequalities yield the full column sum. The norm identity is therefore on the genuine Sobolev space, not on unconstrained jets. The signs of (1+r²)P′−3rP on the two branches are those of 5−r−13r²−r³ and (1−r)(5r²+18r+5). The root is between 0.57 and 0.58; using P₋(0.58) and the denominator at 0.57 bounds its branch maximum below 8/3. The cusp at 1/√2 is a strict local minimum and 2√2 at r=1 is the strict global maximum on the reduced interval. At nonquarter angles L₃>1, and the unchanged positive zeroth-order norm of a nonzero function forces strict inequality in the complete norm estimate. At quarter-turns all slots are preserved in norm. This verifies both isometry and attainment statements.

## originality

PASS

The originality is the explicit third-order rotational profile: two interior turning points of different types and a diagonal global maximum rather than the order-two oblique maximum. The same-order non-inequality, coordinate-isometry rigidity, and sharpness-by-concentration method are prior ingredients. No broader norm formula settling this profile was found in the bounded comparison.

## value

PASS

For this natural complete endpoint derivative-sum norm, knowing the exact distortion or where it is worst can matter in using rotated coordinates; a generic equivalence bound loses that information. The fixed cubic order resolves a change from the previous natural derivative order: the worst angle becomes diagonal and an interior smooth maximum and distinct cusp minimum appear. The proof realizes the coefficient bound in the function space and rules out attainers, so the sharp result is more than a finite jet computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
