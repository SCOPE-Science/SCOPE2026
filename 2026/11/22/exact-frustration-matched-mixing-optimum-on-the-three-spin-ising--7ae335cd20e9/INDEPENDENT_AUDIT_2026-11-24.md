# Independent mathematical audit

## correctness

PASS

The claim uses zero field and independent rate-one updates at each site, not one total update per unit time. Conditional spin means are a*sigma2−b*sigma3, c*(sigma1+sigma3), and a*sigma2−b*sigma1 in site order. Global spin flip splits the eight monomials into even and odd sectors. The linear exchange-antisymmetric decay rate is 1−b; the reflection-symmetric block has rates 1+(b±sqrt(b²+8ac))/2. The cubic quotient has rate 3. Quadratics modulo constants give the three respective linear rates shifted by one; together with the constant these exhaust the spectrum, so the full gap is the lesser of 1−b and 1−rho with rho²+b*rho=2ac, rho>0. For h<1, a>c>b and rho>b, while for h>1, a<c<b and rho<b. Since b'>0 and a'≤0 (also at h=0), rho'=(2ca'−b'rho)/(2rho+b)<0. The crossing at h=1 has a=b=c, yielding the unique gap maximum 1−c; setting s=sech²(2t) for t=beta K the slopes are t(3−s)/6 and −t(1+s)/2. The fixed-h limits are zero off the optimum and 1/2 at it. In the window h=1+u/t one has a→(1−tanh u)/2, b→(1+tanh u)/2, c→1/2. The limiting positive root is a (since a+b=1 and 2c=1 in the limit), so the two branches give (1−|tanh u|)/2. Five independently constructed eight-state generators gave the same exact characteristic polynomial by rational Faddeev–LeVerrier, covering both sides and equality: /workspace/branches/5e947fd0-7b63-4359-b26d-4eea87ce2831/independent_spectrum_check.py. The uploaded code was not executed and the rational sample does not establish the real-parameter theorem.

## originality

PASS

The supported distinct claim is the full signed-triangle defect law, its strict branchwise optimum and cusp, and the scaling window. The Glauber rates, linear closure and homogeneous-ring setting are prior. Neither the ferromagnetic cycle monotonicity result nor the inspected general signed-chain domain-wall spectrum gives the competition of odd spin modes that is essential here. The judgment is limited to compared statements and known implications, not absolute priority.

## value

PASS

The triangle is the smallest simple cycle carrying frustration. The exact full-gap result shows that strengthening a single negative bond first removes a relaxation bottleneck and then creates another, and quantifies the change of dominant mode. The nonzero limiting optimum versus vanishing gap at every fixed mismatched bond and the exact 1/(beta K) crossover are physically meaningful distinctions not captured by the static ground-state energies or by a mere linear-mode calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
