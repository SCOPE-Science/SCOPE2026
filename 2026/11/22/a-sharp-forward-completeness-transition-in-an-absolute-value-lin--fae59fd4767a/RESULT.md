# A sharp forward-completeness transition in an absolute-value line-equilibrium flow

## Finding
For the locally Lipschitz vector field
\[
\dot x=y,\qquad \dot y=-ax+yz,\qquad \dot z=b|y|-cxy-x^2,
\]
where \(a>0\), \(b\leq0\), and \(c\in\mathbb R\), **every real initial-value problem has a global forward solution if and only if \(c\geq0\)**. When \(c<0\), an explicitly described nonempty open set of initial data blows up in finite positive physical time. Regardless of the sign of \(c\), the equilibrium line \(\{(0,0,z):z\in\mathbb R\}\) supports every invariant Borel probability measure carried by complete solutions: no nonstationary recurrent dynamics is possible.

## Assumptions and scope
Solutions are maximal classical solutions of the displayed system in \(\mathbb R^3\). The vector field is locally Lipschitz, including across \(y=0\), hence each initial state has a unique maximal solution. Forward completeness means its maximal forward lifetime is infinite **for every** initial state. When \(c<0\), put \(k=-c>0\). Choose any \(R>0\) satisfying
\[
R>\max\left\{1,\frac{4|b|}{k},\frac{\sqrt{96}}{k},\left(\frac{192a}{k^2}\right)^{1/4}\right\}.
\]
Then every initial state in the open set
\[
\mathcal U_R=\left\{x>R,\quad y>\frac{k}{24}x^3,\quad z-\frac{k}{2}x^2> -\frac{k}{4}x^2\right\}
\]
blows up before time \(12/(kx(0)^2)\). Here blow-up means the Euclidean norm diverges at its finite maximal forward lifetime. The exact rate of divergence and the behavior of trajectories outside \(\mathcal U_R\) are not asserted.

## Proof
**1. Monotone shear.** For all parameters define \(w=z+cx^2/2\). Direct differentiation yields the exact transformed equations
\[
\dot x=y,\qquad \dot y=-ax+\left(w-\frac c2 x^2\right)y,\qquad \dot w=b|y|-x^2\leq0.
\]
In particular, \(w(t)\leq w(0)\) throughout every forward existence interval.

**2. Global continuation for \(c\geq0\).** Since \(z=w-cx^2/2\leq w(0)\), the coercive oscillator energy \(E=(ax^2+y^2)/2\) obeys
\[
\dot E=z y^2\leq 2\max\{w(0),0\}E.
\]
Gronwall's inequality bounds both \(x\) and \(y\) on every bounded time interval, even if a maximal lifetime were finite. The equation \(\dot w=b|y|-x^2\) then bounds \(w\), hence \(z=w-cx^2/2\), on that interval. The local continuation theorem excludes any finite maximal lifetime. This includes the boundary \(c=0\).

**3. An explicit forward-invariant escape sector for \(c<0\).** Put \(k=-c>0\) and \(w=z-kx^2/2\). Introduce
\[
g=y-\frac{k}{24}x^3,\qquad h=w+\frac{k}{4}x^2.
\]
Inside the closed inequalities \(x\geq R\), \(g\geq0\), \(h\geq0\), one has \(y\geq kx^3/24>0\) and \(z=w+kx^2/2\geq kx^2/4\). The vector field points strictly inward at each face. On \(x=R\), \(\dot x=y>0\). On \(h=0\), using \(x>4|b|/k\) and \(y\geq kx^3/24\),
\[
\dot h=by-x^2+\frac{k}{2}xy
\geq -x^2+\frac{k}{4}xy
\geq -x^2+\frac{k^2}{96}x^4>0.
\]
On \(g=0\), since \(h\geq0\),
\[
\dot g=-ax+\left(w+\frac{3k}{8}x^2\right)y
\geq -ax+\frac{k^2}{192}x^5>0.
\]
The strict boundaries and uniqueness imply positive invariance for every starting state in \(\mathcal U_R\). Throughout its lifetime, \(\dot x=y\geq kx^3/24\), so
\[
\frac{d}{dt}\frac1{x^2}=-\frac{2y}{x^3}\leq-\frac{k}{12}.
\]
A positive solution cannot persist after \(12/(kx(0)^2)\), proving finite-time blow-up; local continuation forces its norm to diverge.

**4. Compact stationary statistics.** Along any nonstationary trajectory, \(w(t)\) strictly decreases over every positive time interval. For \(b<0\), \(b|y|-x^2\) can vanish only at \(x=y=0\). For \(b=0\), if \(\int_{s}^{t}x(\tau)^2\,d\tau=0\), then \(x\equiv0\) on that interval, whence \(y=\dot x\equiv0\), and uniqueness makes the solution stationary. A recurrent nonstationary state would force the continuous scalar \(w\) to return arbitrarily close to its strictly smaller value at a positive elapsed time, contrary to monotonicity. Poincare recurrence for any invariant Borel probability measure on complete trajectories therefore forces full mass onto the equilibrium line. Conversely every probability supported on that line is invariant.

## Verification
The accompanying `check.py` symbolically checks the shear derivative, energy derivative, both escape-sector face formulas, and the exact positive polynomial margins. Run `python3 check.py` with Python 3 and SymPy. These identities are algebraic checks, not a substitute for the continuation, barrier or recurrence arguments above.

## Relationship to prior work
Abdulkareem, Amen and Hussein's 2022 preprint studies zero-Hopf limit cycles and the Darboux integrability of the same nonsmooth three-dimensional system. Its inspected complete text does not present the above nonpositive-injection global continuation/blow-up criterion. Pham and collaborators' 2019 study treats chaotic behavior and multistability in the same model, but its complete paper was not available for direct examination. An earlier 2016 infinite-equilibria flow paper investigates a related chaotic-flow setting rather than establishing the present sharp sign criterion. Published global blow-up and recurrence results for other quadratic or jerk flows do not logically entail this model-specific transition.

## Limitations
The theorem assumes \(a>0\), \(b\leq0\); no assertion is made for \(b>0\) or \(a\leq0\). For \(c<0\) the constructed escape set is sufficient, not a complete escape-basin classification. No global backwards-time statement is made. The stationary-measure conclusion concerns invariant probability measures on complete trajectories; it does not preclude compact invariant heteroclinic sets. Novelty comparison is limited by incomplete access to the 2019 source and possible unindexed equivalences. Independent review has not been performed.

## References
1. A. A. Abdulkareem, A. I. Amen and N. H. Hussein, *Limit cycles and Integrability of a continuous system with a line of equilibrium points*, arXiv:2210.03775, first public version October 7, 2022. https://arxiv.org/abs/2210.03775 (complete accessible text https://arxiv.org/html/2210.03775v2).
2. V.-T. Pham, C. Volos, S. Jafari, A. Ouannas and T. T. Dao, *Chaotic behaviors in a system with a line equilibrium*, European Control Conference, 2019, pp. 2603–2607. https://doi.org/10.23919/ECC.2019.8795971.
3. V.-T. Pham et al., *A Chaotic System with an Infinite Number of Equilibrium Points: Dynamics, Horseshoe, and Synchronization*, Advances in Mathematical Physics (2016), Article 4024836. https://doi.org/10.1155/2016/4024836.
