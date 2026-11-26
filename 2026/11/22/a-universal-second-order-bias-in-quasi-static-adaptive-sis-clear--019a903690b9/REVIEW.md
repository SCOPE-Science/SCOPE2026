# Independent mathematical audit

## correctness

PASS

At the stated parameters τn=γ+w and the correlation equilibrium is (0,a,1/n), a=(n-1)/(2n). The fast block has trace -γ(3n-1)/(n-1) and determinant 2γ²n/(n-1), so both fast eigenvalues are stable. The center tangent in (x,p,q) is (1,0,a). Eliminating q from the two fast nullclines on the positive branch gives Eq. (83) of the cited original. At the cusp set h=p_qs/a; the equation is ((1+x)/(1-x))h²+[2/(n-1)-x]h-(n+1)/(n-1)-x=0. Its root through 1 has coefficients h₁=0, h₂=-(n-1)/n and h₃=(n-3)(n-1)/(2n²). For the full graph, invariance gives these same first and second jets because the scalar flow starts at order three. At order three the change in the fast jet from quasi-static to full is J_f⁻¹(0,-aK)ᵀ, K=γ(n-1)/n, since q′(0)=a and p′(0)=0. Its p component is aKγ/det J_f, hence the quartic scalar coefficient increases by K²/(2γ) from E_qs=γ(n-1)(n-3)/(2n²). This independently gives E=γ(n-1)(n-2)/n². For the attracting cubic center dynamics, the invariant plane x=0 is the local strong-stable leaf through the equilibrium. Nearby positive states have positive center phase by local stable foliation and invariance of that leaf, and the exponential tracking error is negligible at the claimed orders. The local full equilibrium is attracting on the center manifold and in the stable directions; the assertion is local to the deterministic closure. For either scalar equation, y=1/x satisfies dt/dy=y/K+E/K²+O(y⁻¹). Integration and inversion give x=(2Kt)^(-1/2)+(E/2K²)t⁻¹+O(t^(-3/2)log t), yielding the gap 1/(4γ) and the strict opposite signs for 2<n<3. In particular the two t⁻¹ coefficients at (n,γ)=(5/2,1) are 1/6 and -1/12. Replay: RESULT.md §§1–4 and arXiv:2610.05467v1 Eqs. (73)–(83). Inspection of verify.py confirms separate symbolic jets; its optional numerical runs only test the leading amplitude of the full flow, not the asymptotic gap. The uploaded script was not executed.

## originality

PASS

The fast-equilibrium closure and cusp location are prior. The supported distinct claim is the paired critical physical-time expansion, in particular the nonzero universal t⁻¹ bias and its sign consequence, not a new SIS threshold or a new pair closure.

## value

PASS

At a natural degeneracy where fast equilibration gets the leading law right, the explicit difference quantifies exactly what the approximation loses on its own equation. Independence of the mean degree and initial condition, and opposite signs on a nontrivial interval, make the comparison informative beyond a Taylor coefficient in isolation. It is not offered as a stochastic-network result or a basis for real-world epidemic intervention.

The dated certificate retains the supplied scientific assessment, sources and limitations.
