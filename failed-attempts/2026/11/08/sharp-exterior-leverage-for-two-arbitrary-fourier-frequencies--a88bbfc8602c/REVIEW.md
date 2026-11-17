# Independent mathematical audit

## correctness

PASS

For Lebesgue L² norm, the exact two-tone Gram is 2[[1,s],[s,1]], so the fixed-gap optimum is K_d=(1-s cos(dx))/(1-s²). For d>=2, |s|<=1/d gives K_d<=2, strictly below B(x)=(1+3x²)/2. For 0<d<2 the supplied h(d) curvature makes F_d(1)>0, and a rational Taylor polynomial bounds F_d' by positive 3(1-u²)-d²u=d^4(160-d^4)/4800. The confluent affine reproducing kernel proves sharpness. Independent SymPy expansion recovered K_d=B(x)-[(15x^4+6x²-5)/120]d²+O_x(d^4), with positive coefficient at |x|>=1. No finite sample substitutes for all real parameters.

## originality

FAIL

The entire claim, including the exact K_d formula, nonattainment, sharp universal exterior constant (1+3x²)/2, and identical positive coefficient (15x^4+6x²-5)/120, appears in the 2026-11-01 full published sharp two-frequency exterior theorem. The earlier result even supplies all fixed-gap maximizers and a distinct complete proof. No final theorem component survives coverage.

## value

FAIL

An exact collision-defect invariant would be motivated for spectral separation and extrapolation, but the preceding published theorem proves its precise coefficient, domain, positivity, and extremizers. This is a known formula recomputation, not an independent valuable finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
