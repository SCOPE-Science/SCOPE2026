# Quadratic near-axis resonances obstruct exponential relaxation in two-speed threshold resetting

## Finding

A particle travels from \(L>0\) to zero at constant speed and immediately returns to \(L\). At time zero and after every reset, independently draw the flight duration \(T\), taking the values \(a,b>0\) with probabilities \(p,q=1-p\in(0,1)\), respectively. The speed on that flight is \(L/T\). Let \(\mu=pa+qb\), let \(P_t\) be the position law, and put \(m(t)=\mathbb E[X_t/L]\). Positions at a reset are defined just after the reset.

**Mean relaxation for irrational \(b/a\).** The position law tends weakly to uniform on \([0,L]\) but its total variation distance to uniform is one at every finite time. The mean tends to \(1/2\), with the quantitative lower bound
\[
\limsup_{t\to\infty}\sqrt{t}\,|m(t)-1/2|\ \ge\ \frac{\sqrt{\mu}}{2\sqrt{2\pi pq}}.
\]
In particular the mean cannot relax exponentially. The bound comes from exact jumps: for nonnegative integers \(j,k\) with \(j+k>0\),
\[
m((ja+kb))-m((ja+kb)^-)=\binom{j+k}{j}p^j q^k.
\]

There is also a spectral obstruction for this specific observable. Write \(D(z)=1-pe^{-az}-qe^{-bz}\). For any sequence of positive integers \(K\to\infty\) with integers \(M\) such that \(\delta_K=2\pi(Kb/a-M)\to0\), the known two-generator Dirichlet-polynomial expansion gives simple zeros of \(D\) of the form
\[
\zeta_K=\frac{2\pi iK}{a}-\frac{iq}{\mu}\delta_K-\frac{pqa^2}{2\mu^3}\delta_K^2+O(\delta_K^3).
\]
**These zeros are genuine poles of the mean-position transform** for all sufficiently large approximants along the sequence. The denominator expansion itself is not a new result; see Lapidus and van Frankenhuijsen [3], §3.5.2, especially (3.29) and (3.32).

**Classical comparison for rational \(b/a\).** Write \(a=uh,b=vh\) with coprime positive integers \(u,v\). For each \(s\in[0,h)\), \(P_{nh+s}\) converges exponentially in \(n\), in total variation, to
\[
\nu_s=\frac h\mu\left[p\sum_{j=0}^{u-1}\delta_{L(1-(s+jh)/a)}+q\sum_{j=0}^{v-1}\delta_{L(1-(s+jh)/b)}\right].
\]
Its mean normalized by \(L\) is \(1/2+(h/2-s)/\mu\). The phase law and the rate in the lattice case are not asserted as new.

## Proof

Let \(F=p\delta_a+q\delta_b\) and let \(U=\sum_{n\ge0}F^{*n}\) include the initial reset at zero. For any continuous \(g\) on \([0,L]\), conditioning on the last reset gives
\[
\mathbb E[g(X_t)]=\int_{[0,t]}B_g(t-s)U(ds),\qquad
B_g(r)=\sum_{T\in\{a,b\}}\Pr(T)\,g(L(1-r/T))\mathbf1_{[0,T)}(r).
\]
The upper endpoints of the two indicators are excluded because the particle resets there. The kernel \(B_g\) is compactly supported and directly Riemann integrable. For irrational \(b/a\), the law \(F\) is nonarithmetic: the two phases cannot both be one at a common nonzero frequency. The nonarithmetic key renewal theorem gives the limit \(\mu^{-1}\int_0^\infty B_g(r)\,dr=L^{-1}\int_0^L g(x)\,dx\). At any finite \(t\), a finite number of duration sequences suffice to describe position, because each completed flight lasts at least \(\min(a,b)\). Thus \(P_t\) is supported on a finite set that has uniform measure zero. We use total variation normalized as \(\sup_A|P(A)-Q(A)|\).

For the jump formula, fix \(t=ja+kb>0\). Only finitely many finite sequences are relevant in a neighborhood of \(t\), so the expected left limit equals the left limit of the mean. Each sample path resetting at \(t\) jumps from left limit zero to normalized position one; all other paths are continuous there. Since \(b/a\) is irrational, no different pair of nonnegative integer counts can yield the same \(t\). Therefore a reset at \(t\) occurs exactly when the first \(j+k\) draws consist of \(j\) draws of duration \(a\) and \(k\) of duration \(b\). Order does not matter, and summing these disjoint events gives the asserted jump.

Choose \(j_n=\lfloor np\rfloor\), \(k_n=n-j_n\), and put \(t_n=j_n a+k_n b=n\mu+O(1)\). Stirling's formula gives \(\binom{n}{j_n}p^{j_n}q^{k_n}\sim(2\pi npq)^{-1/2}\), because \(j_n-np\) stays bounded. The maximum of \(|m(t_n)-1/2|\) and \(|m(t_n^-)-1/2|\) is at least half that jump. The left-limit value can be approximated to error at most \(1/n\) by choosing an actual time in \((t_n-1/n,t_n)\). Multiplication by \(\sqrt{t_n}\) proves the lower bound for a limsup over actual times. This is a lower bound, not a matching upper estimate.

To identify the poles for the mean itself, use \(g(x)=x/L\). Integrating the affine one-flight profile gives, for \(\Re z>0\),
\[
\mathcal Lm(z)=\frac{B(z)}{D(z)},\qquad
B(z)=\frac1z-\frac{p(1-e^{-az})/a+q(1-e^{-bz})/b}{z^2}.
\]
The numerator has a removable singularity at zero with \(B(0)=\mu/2\), and \(D'(0)=\mu\). For citation and normalization of the prior expansion, the change \(z=2\pi iK/a+w\) gives the equation \(pe^{-aw}+qe^{-bw-i\delta_K}=1\). This is (3.28) of [3] with its real root shifted to zero, weights \(a,b\), normalized coefficients \(p,q\), and perturbation \(i\delta_K\). The expansion can also be checked directly for either ordering of \(a,b\): the implicit derivative in \(w\) is nonzero at \((0,0)\), and differentiating the implicit equation yields \(w'(0)=-iq/\mu\) and \(w''(0)=-pqa^2/\mu^3\). Rational approximation supplies the required sequences. The real part is strictly negative for large \(K\) because \(\delta_K\ne0\) and the quadratic coefficient is negative, and \(D'(\zeta_K)\to\mu\). At these roots both exponentials tend to one and \(|\zeta_K|\to\infty\), so \(B(\zeta_K)=1/\zeta_K+O(|\zeta_K|^{-2})\ne0\). Thus the mean transform does not cancel the simple poles. If \(m(t)-1/2\) had an exponential bound, its transform \(G\) would extend analytically to a wider half-plane. The identity \(D(z)(G(z)+1/(2z))=B(z)\) would then extend away from zero, contradicting noncancellation at a pole in that half-plane.

For the classical lattice comparison, put \(u_n=U(\{nh\})\). Its generating function is \(1/(1-pz^u-qz^v)\). There is no zero of its denominator inside the unit disk. A zero on the circle requires \(z^u=z^v=1\), hence \(z=1\), a simple pole. Subtracting \((h/\mu)/(1-z)\) leaves a function analytic on a disk of radius greater than one. Thus \(u_n=h/\mu+O(\rho^n)\) for some \(\rho<1\). The allowed ages at \(nh+s\) are \(s+jh\) with \(0\le j<u\) for duration \(a\) and \(0\le j<v\) for duration \(b\); the mass factors are \(p u_{n-j}\) and \(q u_{n-j}\). This gives the limit and the total variation rate on its finite support. Summing the two finite arithmetic progressions gives the displayed sawtooth mean, with the phase-zero value distinct from the left-phase limit.

## Verification and scope

The jump formula and its bound follow from the analytic proof, not from finite-time simulation. The accompanying `checker.py` supplies finite consistency diagnostics for selected rational phase limits and numerical complex poles for one irrational ratio. It does not certify the infinite sequence, the jump lower bound, or the weak limit. These results assume a fresh initial draw, exactly two fixed positive durations with nonzero probabilities, ballistic motion, and immediate resets. The bound is not an optimal-rate assertion, and the displayed expansion is not asserted at arbitrary frequencies.

## Relationship to prior work

Das–Majumdar–Pal [1] give the threshold-reset renewal description, a uniform equilibrium for speed-density models, and a periodic propagator for a single deterministic speed. Boyer [2] relates near-axis zeros to weak Diophantine conditions and obstructions to uniform exponential renewal convergence over classes of tests. The two-term denominator expansion is an instance of the earlier expansion for nonlattice Dirichlet polynomials [3]. The model-specific contribution here is the exact jump formula and rate lower bound for the instantaneous mean of a freshly reset particle, together with the fact that the known denominator poles are not canceled for that observable. No priority is claimed for the renewal limit, the two-term expansion, or the lattice comparison.

## References

1. R. Das, S. N. Majumdar and A. Pal, *Freezing transition and shock-like transients in ballistic random walks under threshold resetting*, arXiv:2611.16733v1, §§II–III and VII.
2. J.-B. Boyer, *The speed of convergence in the renewal theorem*, arXiv:1506.07625, §§2 and 4.
3. M. L. Lapidus and M. van Frankenhuijsen, *Fractal Geometry, Complex Dimensions and Zeta Functions*, §3.5.2, Lemma 3.29 and equations (3.28)–(3.32), https://math.ucr.edu/~lapidus/confidential/FGCD1.pdf .
