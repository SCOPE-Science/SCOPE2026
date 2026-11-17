# Independent mathematical audit

## correctness

PASS

For independent two-stage Coxian T=E_a+B E_b with a,b>0,0<=q<=1, the equilibrium age A has transform z(w)=(1-L_T(iw))/(iw E[T])=ab(b+aq+iw)/((b+aq)(a+iw)(b+iw)). In energy basis rho*_{jk}=rho0_{jk}z(omega_jk). The exact purity-minus-Hilbert–Schmidt-overlap term is sum |rho0_jk|²(|z|²-Re z); direct independent SymPy reduction yielded a² b q(b−a+aq) omega² /((b+aq)² (a²+omega²)(b²+omega²)), and the variance calculation gives identical prefactor (ab/2)(1−CV²). All kernel terms are >=0, strict exactly for nonzero-gap coherences equivalently [H,rho0]!=0. For q=0 and q=1−b/a when a>b the entire T Laplace transform simplifies to Exp(a)/Exp(b), respectively. Differentiating u/((a²+u)(b²+u)) yields unique u=ab maximizer unless zero prefactor. The reset mixed-state quantity is HS overlap, not Uhlmann fidelity. None of these steps depends on finite samples.

## originality

PASS

The general renewal-reset density-matrix spectral formula of Sevilla & Valdés-Hernández and Poisson equality observation are explicitly older premises. The inspected accessible primary text does not state the exact two-stage Coxian CV² sign factorization, unique q crossover, distributional exponential coincidence and sharp balanced-qubit witness. Related Erlang-reset phase theorems concern an integer-shape Gamma family not this independently switched two-exponential clock. Since the old general equations algebraically imply the result after nontrivial specialization, originality is provisional but this meaningful exact classification survives best-of-knowledge comparison.

## value

PASS

The sign of stationary quantum purity relative to reset overlap changes at a universal variance threshold independent of Hamiltonian spectrum or Hilbert-space dimension for all noncommuting states; the Coxian family has an explicit sharp phase boundary and gap that maximizes the effect. This resolves a motivated renewal-clock phenomenology question rather than reporting a numerical simulation or textbook rewrite. The mixed-state fidelity distinction is important.

The dated certificate retains the supplied scientific assessment, sources and limitations.
