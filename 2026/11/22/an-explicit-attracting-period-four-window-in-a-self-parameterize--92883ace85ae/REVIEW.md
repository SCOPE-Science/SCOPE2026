# Independent mathematical audit

## correctness

PASS

The published gain and bias give F_c(x)=[3.9+(x+c)/25]x(1−x), which maps [0,1] into itself. For c in [4989/5000,4991/5000], ∂F/∂c=x(1−x)/25≥0. The displayed F' is positive on I₀,I₁ and negative on I₃; evaluate the monotone parameter-state corners for those three boxes. In I₂, t=x−1/2>0 gives F=B_c(1/4−t²)+t/100−t³/25 with B_c=3.92+c/25. The minimum is bounded by the smaller endpoint image at c_min by concavity, and for the upper bound take c_max, discard the nonpositive cubic, and complete the square. Independent Fraction comparisons verify all four strict containments and the stated outward bounds, respectively [0.14899438,0.14972141], [0.50027712,0.50241377], (0.9899788236,0.9899883133), and [0.03943226,0.03949482] for I₀,I₁,I₂,I₃. Uniformly on [0,1], |F'|≤3.94+1/25<4. On I₂, F'=1/100−2B_ct−3t²/25 decreases in both t and B_c; the inclusive endpoint limits −0.009325163072 and 0.008178434132 give |F'|<1/100. The cyclic strict containments give F_c^4(I₀) inside I₀; the uniform Lipschitz bound is strictly below 4³/100=16/25. There is one return-fixed point in I₀ by contraction, and disjointness excludes periods 1 and 2, proving least period 4, with one cycle point per box and an open local basin. The four-step multiplier gives the per-iterate exponent bound including the possibility of a zero multiplier (exponent −∞). These inequalities cover the parameter endpoints as well as the interior, without sampling c.

## originality

PASS

The model and interval-trapping method are known. The distinct result is a nonzero-width, uniform analytically certified period-four window for the exact ideal logistic polynomial previously studied for broad chaos.

## value

PASS

The parameter slice is motivated by the prior studies' emphasis on eliminating periodic windows in a specific ideal-map configuration. A positive-width interval with an open basin is a mathematically decisive counterexample to parameter-wide absence of periodic attractors; verifying isolated sampled parameters or plotting a coarse sweep would not give that quantitative conclusion. The proof supplies a reusable exact witness in that published family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
