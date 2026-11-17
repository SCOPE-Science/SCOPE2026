# Independent mathematical audit

## correctness

PASS

Height h in t times the join contributes (t-h+1)^d(h+1) lattice points. Summing yields a polynomial with exact Bernoulli-number coefficients. For d<=16 the even Bernoulli bounds check every coefficient, including the linear and upper three coefficients. At d=17, c_17,1=17-B_18=-30301/798. For d>=18 choose largest r<=d congruent 2 mod 4 and k=d+2-r; the coefficient is a positive factor times (r-B_r), and Euler’s Bernoulli-zeta formula gives B_r>r by induction for r=18,22,26,... . Independent rational interpolation confirmed d=1,16,17, including the sign and exact boundary value. The induction is the infinite-dimensional proof, not extrapolation.

## originality

PASS

Prior join-product and large-dilation nonpositivity theorems are credited, but the published results inspected do not identify the sharp undilated cube threshold d=17 and persistence for every d>=18. The stronger all-d Bernoulli sign theorem is nontrivial relative to those statements.

## value

PASS

Whether a standard join preserves coefficientwise Ehrhart positivity despite two positive factors is a natural structural closure question. The sharp first undilated-cube obstruction at dimension 17 and its persistent sign failure provide a new quantitative boundary not supplied by large-dilation examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
