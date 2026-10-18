# Independent mathematical audit

## correctness

PASS

For the actual two-parameter DRLE distribution alpha>0,beta>=2 obtained by floor discretization of parent survival (1+cx)exp(-lambda x) with lambda=alpha/beta, c=lambda/(beta-1), q=exp(-lambda), the stated S_n=P(X>=n)=(1+cn)q^n is exact. Subtraction gives p_n=q^n(A+Bn), A=1-q(1+c)>0, B=c(1-q)>0; hence G(z)=A/(1-qz)+Bqz/(1-qz)^2, convergence radius 1/q and finite probabilistic MGF iff t<lambda; rational continuation is not expectation when t>=lambda. Exact hazard h_n=1-q-qc/(1+cn) strictly increases to 1-q with gap asymptotic q/n. Logarithmic inversion of (1+cm)exp(-lambda m)=u yields m=(1/lambda)[log(1/u)+loglog(1/u)-log(beta-1)]+o(1), and lattice quantile differs O(1). Independently checked algebraic PGF against the survival and inversion scales numerically. The original 2026 DRLE paper uses S(x)=P(X>x)=S_{x+1}; that harmless shift was accounted for and is not a distinct law. Correctness of these deductions does not establish novelty or value.

## originality

FAIL

Decisive earlier full-text coverage: Alazwari et al., AIMS Mathematics 11 (2026), §§2.1–2.4 and §3.1, Eq.(1.1),(2.1)–(2.7), Proposition 1, Lemma 2.3, Proposition 2, already give the same DRLE floor discretization, exact PMF, survival, hazard and rational MGF. The exact radius/positive MGF convergence interval is a direct root-test/geometric-series implication of their closed MGF with double pole and q=e^{-alpha/beta}. The loglog quantile is not explicitly printed there, but follows immediately by logarithmic inversion of their exact survival; it is a mechanically implied asymptotic special consequence, not an independently new nonstandard theorem. Do not represent this as proof that the earlier paper printed the loglog term: it supplies sufficient stronger data to derive it.

## value

FAIL

The earlier original DRLE paper gives the *exact* PMF/survival, hazard including monotonicity, and the closed rational MGF on the same full parameter domain. The present remaining convergence interval is immediate from a double-pole geometric series; the loglog quantile term is a standard two-line inversion of the original known linear-geometric survival, with only O(1) lattice accuracy and no additional structural, parameter-uniform stability, inferential or extremal theorem. The natural tail question is motivated, but the particular claimed addition is mechanically implied by the published distribution formula and too narrow to support an independent mathematical finding at the stated C/O/V standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
