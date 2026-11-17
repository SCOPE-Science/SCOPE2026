# High-energy physical-time occupation and Pareto concentration in a lifted chemical center

## Finding

Consider the three-species mass-action system
\[
\dot x=x(ax-by),\qquad \dot y=by(x-y-d),\qquad \dot z=by(x-y-d),
\]
where \(0<a<b\), \(d>0\), and the positive stoichiometric class is \(z-y=d\). Put \(\lambda=b-a\),
\[
V=\frac{by}{ax},\qquad W=\frac{bd}{\lambda x},\qquad
f(s)=s-1-\log s,\qquad H=a f(V)+\lambda f(W).
\]
For each \(h>0\), the level \(H=h\) is a positive periodic orbit. Write \(T(h)\) for its period **in the displayed physical time**, and \((X_h,Y_h,Z_h)\) for its state at a uniformly selected physical time in one period. The following conclusions hold, with constants depending only on \(a,b,d\):

1. The exact leading period law has a logarithmic error:
\[
T(h)=\frac{h}{abd}+O_{a,b,d}(\log(2+h)),\qquad h\to\infty.
\]
2. The rescaled first-species concentration has a Pareto law in **total variation**:
\[
d_{\mathrm{TV}}\left(\mathcal L\left(\frac{hX_h}{bd}\right),\ \mathrm{Pareto}(1,1)\right)
=O_{a,b,d}\!\left(\frac{\log(2+h)}h\right),
\]
where \(\mathrm{Pareto}(1,1)\) has density \(s^{-2}\mathbf1_{\{s\ge1\}}\) on \((0,\infty)\).
3. The unscaled state converges in probability to the boundary equilibrium \((0,0,d)\), yet its physical-time means remain exactly
\[
\mathbb E X_h=\frac{bd}{\lambda},\qquad
\mathbb E Y_h=\frac{ad}{\lambda},\qquad
\mathbb E Z_h=\frac{bd}{\lambda}
\quad\text{for every }h>0.
\]
The contrast between convergence in probability and nonvanishing means exhibits a rigorous rare-excursion, non-uniform-integrability mechanism.

## Assumptions and scope

All parameters \(a,b,d\) are fixed throughout the high-energy limit, with \(0<a<b\) and \(d>0\). Initial data are strictly positive and satisfy \(z-y=d\). The energy \(h\) is the value of the explicitly defined first integral \(H\), not an amplitude, Euclidean distance, or physical energy. Periods and sampling use the original time variable \(t\); an auxiliary clock \(\tau\) appears only in the proof. Total variation is \(\sup_A|\mu(A)-\nu(A)|\). No assertion is made for parameter limits \(a\uparrow b\), \(d\downarrow0\), or other stoichiometric classes.

## Proof

**1. Exact clock and periodic levels.** From \(z=y+d\), the displayed system is a two-dimensional quadratic flow. Introduce \(w=1/x\), \(v=y/x\), and \(w_*=\lambda/(bd)\). Define \(d\tau/dt=1/w=x\). Direct differentiation gives
\[
\frac{dV}{d\tau}=\lambda V(1-W),\qquad
\frac{dW}{d\tau}=aW(V-1),\qquad
\frac{dt}{d\tau}=w_*W.
\]
Consequently \(H=a f(V)+\lambda f(W)\) is conserved, since
\[
\frac{dH}{d\tau}=a\lambda(V-1)(1-W)+a\lambda(W-1)(V-1)=0.
\]
The strictly convex \(f\) has its unique minimum zero at \(1\), diverges at both ends of \((0,\infty)\), and each level \(H=h>0\) is a smooth compact simple closed curve with no equilibria. Thus every such level supports a periodic orbit. Integration of \(d\log V/d\tau=\lambda(1-W)\) over one complete circuit shows \(\int W\,d\tau=T_\tau\); therefore the physical-time period is exactly \(T(h)=w_*T_\tau(h)\).

**2. The exact physical-time occupation density.** For \(q>0\), let \(v_-(q)\in(0,1)\) and \(v_+(q)\in(1,\infty)\) solve \(a f(v)=q\). Let \(w_-(h)<1<w_+(h)\) be the roots of \(\lambda f(w)=h\), and put \(q_h(w)=h-\lambda f(w)\). Every \(w\in(w_-,w_+)\) is traversed once on each branch \(V=v_-(q_h(w))\) and \(V=v_+(q_h(w))\). Because \(dW/d\tau=aW(V-1)\) and \(dt/d\tau=w_*W\), the unsigned physical-time element per branch is \(dt=w_*|dW|/(a|V-1|)\). Define
\[
B_h(w)=\frac1{1-v_-(q_h(w))}+\frac1{v_+(q_h(w))-1},\qquad
I_h=\int_{w_-}^{w_+}B_h(w)\,dw.
\]
Then the exact physical-time density of \(W\) is \(B_h(w)/I_h\) on \((w_-,w_+)\), and \(T(h)=w_*I_h/a\). The inverse functions are well defined and the square-root singularities of \(B_h\) at the endpoints are integrable.

**3. Quantitative normalization of this density.** Uniformly for all large \(h\),
\[
I_h=(w_+-w_-)+O_a(\log(2+h))=\frac h\lambda+O_{a,\lambda}(\log(2+h)).
\]
Here is a proof of the required global integral estimate, including the turning points. Write
\[
B_h(w)-1=\frac{v_-(q)}{1-v_-(q)}+\frac1{v_+(q)-1},\qquad q=q_h(w).
\]
By Taylor's theorem at the nondegenerate minimum of \(f\), both summands are \(O_a(q^{-1/2})\) for \(0<q\le1\). For \(q\ge1\), the first is \(O_a(e^{-q/a})\), because \(v_-\le e^{-q/a}\); the second is bounded by \(a/q\), since \(f(v_+)\le v_+-1\). On \(w\le1/2\) and \(w\ge2\), the change of variable \(q=h-\lambda f(w)\) has \(|dw/dq|\le2/\lambda\). On \([1/2,2]\), \(q=h-O_{\lambda}(1)\), so both summands are uniformly \(O_{a,\lambda}(1/h)\) for large \(h\). Integrating the displayed bounds gives
\[
0\le\int_{w_-}^{w_+}(B_h-1)\,dw=O_{a,\lambda}(\log(2+h)).
\]
Finally \(f(w_+)=h/\lambda\) gives \(w_+=h/\lambda+O_{\lambda}(\log(2+h))\), while \(w_-\in(0,1)\). This establishes the asserted normalization and, since \(w_*/(a\lambda)=1/(abd)\), the period law.

**4. Total variation and the Pareto variable.** The physical-time law of \(W\), with density \(B_h/I_h\), differs from uniform measure on \([w_-,w_+]\) in total variation by at most \((I_h-(w_+-w_-))/I_h=O(\log h/h)\). Rescaling by \(\lambda/h\), that interval becomes \([\lambda w_-/h,\lambda w_+/h]\), whose uniform law is within \(O(\log h/h)\) total variation of uniform \([0,1]\). Thus \(U_h=\lambda W/h\) tends to uniform \((0,1)\) with the stated rate in total variation. The identity
\[
\frac{hX_h}{bd}=\frac{h}{\lambda W}=\frac1{U_h}
\]
is exact. Total variation contracts under measurable push-forward; the reciprocal of a uniform \((0,1)\) variable has density \(s^{-2}\mathbf1_{\{s\ge1\}}\). This proves the Pareto assertion.

**5. Boundary concentration and the stationary-mean paradox.** Under physical-time sampling, the probability of the \(V=v_+\) branch is at most \(I_h^{-1}\int 1/(v_+-1)\,dw=O(\log h/h)\). On the \(V=v_-\) branch, for every \(\delta\in(0,1/2)\), on the event \(U_h\in[\delta,1-\delta]\) one has \(q_h(W)\ge c_\delta h\) for all large \(h\), and hence \(V=v_-(q_h(W))\le e^{-c_\delta h/a}\). The probability of the complement is at most \(2\delta+o(1)\). It follows that \(W\to\infty\), \(V/W\to0\) in physical-time probability. Since \(x=1/(w_*W)\), \(y=(a/b)V/(w_*W)\), and \(z=y+d\), the state converges in probability to \((0,0,d)\). On the other hand, exact integration of \(d\log x/dt=ax-by\) and \(d\log y/dt=b(x-y-d)\) around each orbit gives the two equations \(a\mathbb EX_h=b\mathbb EY_h\) and \(\mathbb EX_h-\mathbb EY_h=d\). Solving and using \(Z_h=Y_h+d\) proves all three asserted exact means. Positive concentrations converging in probability to zero but retaining positive means cannot be uniformly integrable.

## Verification

A standalone `verify_lva.py` script checks the defining coordinate and first-integral identities symbolically (SymPy), and evaluates the exact two-branch period quadrature at several finite energies (SciPy). Its finite quadrature values illustrate approach to the analytical slope \(1/(abd)\); they do not prove the infinite-energy limits. Run `python verify_lva.py` with Python 3, SymPy, NumPy and SciPy installed. The proof above supplies the global inverse-branch bounds and the asymptotic error estimates independently of the script.

## Relationship to prior work

Banaji, Boros and Hofbauer (arXiv:2304.02303v1, Section 5.2 and Theorem 10) identify the Lifted LVA center and give its time-changed Lotka–Volterra reduction; that center and reduction are **not** claimed as new. Boulnois (arXiv:2301.00673v1, Sections 3–4) develops exact period quadratures and high-energy asymptotics for classical Lotka–Volterra dynamics; Genda, Fidlin, Lenci and Gendelman (DOI:10.1007/s11071-024-10667-y, Appendix C) also analyze its large-energy period. These period studies are antecedents, not excluded by different terminology. The present result instead uses the original mass-action physical-time weighting \(dt=w_*W\,d\tau\) to derive a quantitative **total-variation** Pareto law for a chemical concentration and accompanying boundary concentration/nonuniform-integrability phenomenon. An independent priority review could uncover an equivalent phase-occupation calculation outside the inspected papers.

## Limitations

This is an exact fixed-parameter, large-energy limit within the positive center classes; it is not a global classification outside \(z-y=d>0\) or away from \(a<b\). The logarithmic error rate is an upper bound, not claimed optimal. The usual-time Lotka–Volterra period asymptotics and center existence are prior results. The result concerns deterministic uniform physical-time sampling of one orbit, not stochastic reaction noise. No independent external audit is asserted.

## References

- M. Banaji, B. Boros and J. Hofbauer, *Oscillations in three-reaction quadratic mass-action systems*, arXiv:2304.02303v1 (first public 2023-04-05), especially Section 5.2, equations (24)–(26), and Theorem 10. https://arxiv.org/abs/2304.02303
- J.-L. Boulnois, *Predator-Prey Linear Coupling with Hybrid Species*, arXiv:2301.00673v1 (2022-12-29), Sections 3–4. https://arxiv.org/abs/2301.00673
- A. Genda, A. Fidlin, S. Lenci and O. Gendelman, *Effects of seasonal hunting and food quantity variations on the Lotka-Volterra model*, Nonlinear Dynamics (online 2024-12-05), Appendix C. https://doi.org/10.1007/s11071-024-10667-y
