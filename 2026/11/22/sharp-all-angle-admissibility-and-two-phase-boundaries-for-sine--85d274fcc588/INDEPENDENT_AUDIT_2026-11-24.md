# Independent mathematical audit

## correctness

PASS

At exponent one the four copula boundary conditions are automatic. The mixed derivative is 1+αβ(1−2u)(1−2v)h(t), where t=βu(1−u)v(1−v). Its continuity makes pointwise nonnegativity equivalent to 2-increasingness, including at a corner by approaching from the interior. At fixed ab=t/β with a=u(1−u), b=v(1−v), maximizing (1−4a)(1−4b) is equivalent to minimizing a+b, so a=b=√(t/β) attains the bound. Reflections across 1/2 give both signs, except when the product is zero and the sign does not matter. This proves the exact admissibility envelope, including Q≥1 from t=0. An envelope contribution exceeds 1 iff |h(t)|>1 and β exceeds the stated scalar objective, which itself exceeds 16t and therefore implies t<β/16. By Cauchy–Schwarz, |h(t)|≤√(1+t²); hence the objective is strictly larger than 16(t+2+1/t). This proves blow-up at both t→0 and t→∞. At each positive finite boundary of the eligible set the denominator |h|−1 tends to zero, giving compact sublevels and attainment. Alternating Taylor bounds at 2 give |h(2)|≥2 times the sine lower truncation at degree 7 minus the cosine upper truncation at degree 8, giving a rational upper bound for the candidate B(2) less than 105.051. Therefore 64<β_c<106 rigorously; an independent diagnostic scan and local minimizations agree with the approximate 103.92133496324 without certifying its digits. The sign of α sin t changes exactly when β/16>π for nonzero α. Finally t(1−4√(t/β)) has maximum β/108 at t=β/36; |h|≤1+t gives the upper bound and sampling within π/2 of that maximum at points with |sin t|=1 loses only O(β⁻¹) from the leading term. This proves the claimed sharp amplitude equivalent 108/β².

## originality

PASS

The sine-FGM construction and quadrant dependence under restricted old admissible parameters are established. The strongest matched prior contains only sufficient bounds at exponent one (β≤8π and |α|≤1/[β(1+β²/256)]); it does not establish the new sharp envelope in that range or beyond. The sine-sign cutoff is a direct consequence of the known formula, not an independently deep novelty claim; it becomes a boundary of the full valid family only after the sharp all-angle validity calculation. The distinct contribution is the full envelope, its first departure, and its large-angle behavior, with the two phase boundaries identified together.

## value

PASS

A known widely parameterized copula construction had a conservative sufficient region. The sharp necessary-and-sufficient test identifies both the onset of stricter amplitude requirements and the earlier loss of quadrant dependence while valid copulas still exist. Its 108/β² asymptotic quantifies the full high-angle shrinkage. The contribution does not rest on the elementary sine sign observation in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
