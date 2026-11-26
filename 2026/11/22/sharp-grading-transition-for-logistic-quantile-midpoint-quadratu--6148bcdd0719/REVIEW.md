# Independent mathematical audit

## correctness

PASS

For f normalized by f(0)=0, weighted Cauchy–Schwarz gives at most exp(|x|/2) growth, so the boundary terms against F-G vanish. The error functional has Riesz derivative (G-F)/rho; its squared energy is finite since G-F is a logistic tail outside the nodes. Under u=F(x), dx/rho=du/[u^2*(1-u)^2], and the cumulative weights telescope to a_j then b_j, giving the exact two integrals. At j>=2 on the left half, the reciprocal denominator (not the denominator in one sentence of the proof) is O_p((j/n)^(-2p)) and each distance integral is bounded by the cube of the width, with width O_p(n^-p*j^(p-1)); hence the cell bound O_p(n^-p*j^(p-3)). In the first cell the left numerator cancels u^2 and the other half starts at u comparable to n^-p; this gives O_p(n^-p). Symmetry (and an O_p(n^-3) central cell for odd n) completes tail control. For p<2 one has the stated fixed-j scaled integrals and a summable majorant. For p=2, uniformly for J<=j<=epsilon*n, both half-widths are j/n^2 times (1+O(1/j+j/n)); throughout such a cell u=(j/n)^2 times (1+O(1/j+j/n)). Integrating each squared distance gives n^2 times the cell error equal to (2/3j)*(1+O(1/j+j/n)). The remainder in the sum over that range is bounded, and the first J and compact interior cells contribute O_(J,epsilon)(n^-2), proving the 4/3 log coefficient after reflection. For p>2 the n^2-rescaled endpoint tail is O_p(epsilon^(p-2))+o(1), and the bulk limit has density psi_p'^3/(12*psi_p^2*(1-psi_p)^2). With r=t/(1-t), the numerator expands as r^(p-3)*(1+r)^4 and the integral is the stated sum of beta terms with arguments 1±(k-2)/p; reflection gives the formula. For p=1 the joined unit cells integrate by 1-2j/v+j^2/v^2, yielding the stated telescoping rational and log-gamma sum with limit log 2 by Stirling. Finally, on [1/4,3/4], even signed constant-exact rules give a step function with at most n+1 segments; minimizing the squared error on each segment and applying Jensen gives E_n^2>=1/[6(n+1)^2]. All asymptotics are for fixed p and the homogeneous norm. The archived high-precision diagnostic is finite, inspected and not rerun.

## originality

PASS

Best of current knowledge: the full fixed-p trichotomy and exact constants for this deterministic, mass-exact power-logit midpoint family in derivative energy are distinct. Integration by parts, general discrepancy tools and the known feasibility of first-order quadrature are not themselves credited as novel.

## value

PASS

For a canonical probability-coordinate midpoint family, this gives a sharp design rule: ungraded sampling has only n^-1/2 error, critical grading pays a logarithmic penalty, and every fixed p>2 attains the optimal power. It quantifies the cost of endpoint undersampling and distinguishes graded choices by exact constants. These are useful family-specific conclusions in the homogeneous norm; neither general quadrature order nor globally best leading constants are new claims here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
