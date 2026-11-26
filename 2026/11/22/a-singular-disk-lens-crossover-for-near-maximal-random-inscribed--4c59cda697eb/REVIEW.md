# Independent mathematical audit

## correctness

PASS

The radial formula follows by solving (r|cos θ|+c)²+r²sin²θ=1 for r≥0. With a=1-c, b=√(1-c²) and 0≤x≤a, the top boundary leaves ellipse deficit 2cx(a-x)/(ab²); interior points cannot supply additional contacts. The determinant bound after axial normalization therefore gives the stated maximum and exactly two ordered maximizing axis pairs for c>0. At one pair the radial terms begin a+caα²/2 and b-c|δ|; the sine factor begins 1-(δ-α)²/2. The deficit is a²bα²+2ac|δ|+o(α²+|δ|). Compactness localizes to the two pairs, and this positive local form bounds the scaled coordinates. The limiting region x²+|y|≤1 has area 8/3 and null boundary. Multiplying by the inverse Jacobian ε^(3/2)/(2a²c√b) and density 1/π² and counting both pairs gives the stated coefficient, density 3/8, and equal marks; a uniform angle difference gives the exact disk formula. For c=O(ε), Q_c≤2|sin(Φ−Θ)| confines the difference to O(√ε) of π/2. The uniform radial expansion and Lipschitz absolute cosine then give scaled deficit z²+2λ(|cos Θ|+|sin Θ|−1), with bounded z and a null boundary. Integrating the admissible z-length proves G, including its positive value at any finite λ. At large λ, setting s=2λt near each endpoint gives integral 1/(3λ) per endpoint. Replay: RESULT.md §§1–4; VERIFICATION.md and verify.py were inspected, not executed. Marked convergence is for fixed positive c; G's large-λ asymptote does not imply arbitrary joint limits with c/ε→∞.

## originality

PASS

The enclosing ellipse, axial contacts and the associated deterministic determinant bound, as well as the circle's elementary sine law, are not the distinct contribution. It is the sharp random upper endpoint for fixed positive c, the c/ε crossover and the fixed-c conditional directional law under independent angle-uniform sampling of centered opposite pairs. The inspected sources do not establish that distributional result; the conclusion is bounded, not a claim of first publication.

## value

PASS

For a disk the maximizing pairs form a continuum, whereas positive lens separation leaves isolated optimizer pairs with one quadratic and one cusp direction. The change from ε^(1/2) to ε^(3/2), explicit interpolation when separation and deficit have the same scale, and quantitative conditional concentration measure the loss of rotational freedom. These are useful features of near-optimal centered quadrilateral sampling, not a repackaging of the maximum ellipse.

The dated certificate retains the supplied scientific assessment, sources and limitations.
