# Global critical predator clearance with a fear-independent prey deficit

## Finding

In the infected-predator, fear/refuge, saturated-treatment system of Mondal, Sarkar and Sk [1], the **predator-free invasion equality** implies global predator clearance, not merely linear neutral stability. All trajectories with initially positive prey and at least one predator converge to the prey-only equilibrium. Their surviving susceptible-predator population has a universal reciprocal-time amplitude, while any infected-predator population vanishes exponentially. The prey's reciprocal-time deficit has an especially simple coefficient independent of the fear parameter, although predator clearance does depend on fear.

Write \(X\) for prey, \(S\) for susceptible predators, \(I\) for infected predators, and \(P=S+I\). Set
\[
 f(X)=\frac{c(1-m)X}{a+(1-m)X},\quad L=\frac{r-d_1}{d_2},\quad \sigma=r-d_1,\quad \Delta=d_4-d_3.
\]
Assume the exact critical surface \(c_1f(L)=d_3\), and define
\[
 B=rLK+f(L),\qquad D=\frac{c_1f'(L)B}{\sigma}>0.
\]
For every \(X(0)>0\), \(S(0),I(0)\geq0\) with \(S(0)+I(0)>0\),
\[
 \lim_{t\to\infty}(X(t),S(t),I(t))=(L,0,0),
 \qquad \boxed{\lim_{t\to\infty}tS(t)=\frac1D},
 \qquad \boxed{\lim_{t\to\infty}t[L-X(t)]=\frac1{c_1f'(L)}}.
\]
Moreover, \(I(t)\) decreases exponentially eventually (and is identically zero if initially zero). Thus changing \(K\) changes the first limit, but not the second; disease incidence and saturated treatment do not appear in either leading coefficient.

## Assumptions and scope

The original autonomous continuous-time model [1, Eq. (1)] is
\[
\begin{aligned}
\dot X&=\frac{rX}{1+K(S+I)}-d_1X-d_2X^2-f(X)(S+eI),\\
\dot S&=c_1f(X)S-\frac{\lambda SI}{1+bI}-d_3S+\mu I+\frac{\gamma I}{\beta+I},\\
\dot I&=\frac{\lambda SI}{1+bI}-(d_4+\mu)I-\frac{\gamma I}{\beta+I}.
\end{aligned}
\]
The parameters obey \(r>d_1>0\), \(d_2,c,c_1,a,K,d_3,\mu,\gamma,\beta,\lambda,b>0\), \(0<m<1\), \(0<e<1\), \(d_4>d_3\), and \(c_1f(L)=d_3\). The paper also assumes \(\lambda>d_4\); it may be imposed without changing this result. The theorem applies on the nonnegative biological cone with strictly positive initial prey and a nonzero initial predator total. Neither an endemic equilibrium nor an initially absent predator can satisfy its positive reciprocal-time conclusion. The fear coefficient \(K\) is strictly positive for the global argument below.

The exact condition is the **predator** invasion eigenvalue equality at \((L,0,0)\), not the disease-reproduction condition at a positive disease-free equilibrium. These are different threshold surfaces.

## Proof

**1. Positive bounded solutions.** Coordinate-face derivatives are inward or tangent, so \(X>0\), \(S,I\ge0\), and \(P>0\) persist for finite positive times. The prey equation gives
\[
\dot X\le X(\sigma-d_2X).
\]
Let \(U\) solve this logistic equation with \(U(0)=\max\{X(0),L\}\). Scalar comparison gives \(X(t)\le U(t)\), where \(U\ge L\) and \(U(t)-L=O(e^{-\sigma t})\). Summing the two predator equations cancels transmission, recovery and treatment exactly:
\[
\dot P=[c_1f(X)-d_3]S-\Delta I=:F(X)S-\Delta I.
\]
At criticality \(F(L)=0\) and \(F\) is strictly increasing. Consequently
\[
\dot P\le [F(U(t))]_+P,\qquad \int_0^\infty[F(U(t))]_+dt<\infty.
\]
The nonincreasing function \(P(t)\exp[-\int_0^t[F(U(s))]_+ds]\) has a finite nonnegative limit, and the exponential multiplier has a finite positive limit. Thus \(P(t)\to P_\infty\ge0\); the same inequality bounds the solution globally.

**2. Global extinction at equality.** Suppose \(P_\infty>0\). For all sufficiently large \(t\), \(P(t)\ge p>0\). Since \(K>0\), the prey equation implies
\[
\dot X\le X\left(\frac{r}{1+Kp}-d_1-d_2X\right),
\]
so \(\limsup X(t)\le \max\{0,[r/(1+Kp)-d_1]/d_2\}<L\). Hence eventually \(F(X)\le-\delta<0\). Because \(\Delta>0\),
\[
\dot P\le-\delta S-\Delta I\le-\min\{\delta,\Delta\}P,
\]
a contradiction. Thus \(P\to0\). For any \(\epsilon>0\), eventually \(P\le\epsilon\); the prey equation is then sandwiched between the logistic upper comparison and
\[
\dot X\ge X\left(\frac{r}{1+K\epsilon}-d_1-\frac{c(1-m)}a\epsilon-d_2X\right).
\]
Letting \(\epsilon\downarrow0\) yields \(X\to L\).

**3. The infection mode becomes negligible.** If \(I(0)=0\), it stays zero. Otherwise let \(q=I/P\in(0,1]\). Its exact logarithmic derivative is
\[
\frac{\dot q}{q}=\frac{\lambda S}{1+bI}-d_4-\mu-\frac{\gamma}{\beta+I}-F(X)(1-q)+\Delta q.
\]
Using \(X\to L\), \(P\to0\), \(F(L)=0\), and \(0\le q\le1\), its right-hand side is eventually bounded above by a fixed negative constant (for example any rate below \(d_3+\mu+\gamma/\beta\)). Hence \(q=O(e^{-\eta t})\) for some \(\eta>0\). In particular,
\[
\frac{\dot P}{P}=F(X)(1-q)-\Delta q\longrightarrow0.
\]
Therefore \(P(t)\) is subexponential in the useful lower-bound sense: for each \(\epsilon>0\), \(P(t)\ge C_\epsilon e^{-\epsilon t}\) eventually. This implies \(I/P^2=q/P\to0\).

**4. Stable prey-mode slaving.** Let \(h=X-L\). Taylor expansion at \((L,0,0)\), with \(B=rLK+f(L)>0\), gives
\[
\dot h=-\sigma h-BP+O(h^2+|h|P+P^2)+O(I).
\]
Divide by \(P>0\), set \(z=h/P\), and use \(\dot P/P=o(1)\), \(h\to0\), \(P\to0\), and \(I/P=q\to0\). The resulting scalar equation is
\[
\dot z=-[\sigma+o(1)]z-B+o(1).
\]
Its positive limiting damping coefficient gives \(z\to-B/\sigma\). This establishes the nonstandard asymptotic slaving without assuming a center manifold or a priori rate of predator disappearance.

**5. Critical reciprocal-time coefficient.** Since \(F(X)=c_1f'(L)h+O(h^2)\), the total-predator equation gives
\[
\frac{\dot P}{P^2}
 =c_1f'(L)\frac hP(1-q)+O(h^2/P)-\Delta\frac I{P^2}
 \longrightarrow-\frac{c_1f'(L)B}{\sigma}=-D.
\]
Here \(h=O(P)\) and \(I/P^2\to0\) were proved in steps 3–4. Integration of \((1/P)'\to D\) yields \(tP\to1/D\), while \(S=P(1-q)\) gives \(tS\to1/D\). Finally
\[
 t(L-X)=\left(-\frac hP\right)tP\longrightarrow\frac B\sigma\frac1D=\frac1{c_1f'(L)}.
\]
Since \(I=qP\) with exponentially decreasing \(q\) and bounded \(P\), infection itself also eventually decreases exponentially. This completes the proof.

## Verification

The standalone `verify.py` uses exact rational arithmetic to verify the threshold, the derivative \(c_1f'(L)\), and the two coefficients for the following explicitly admissible example:
\[
r=2,\quad d_1=d_2=a=d_3=1,\quad c=6,\quad m=c_1=e=\tfrac12,
\quad d_4=2,\quad\lambda=3,\quad b=\beta=1,\quad\mu=\tfrac14,\quad\gamma=\tfrac12.
\]
For \(K=\tfrac12\), \(L=1\), \(c_1f'(L)=\tfrac23\), \(B=3\), so \(tS\to\tfrac12\) and \(t(1-X)\to\tfrac32\). For \(K=\tfrac14\), the corresponding limits are \(\tfrac35\) and \(\tfrac32\). Finite-time ODE diagnostics from initial \((X,S,I)=(0.8,0.2,0.1)\) are supplementary only; the preceding proof supplies the infinite-time assertions. Run `python verify.py` with Python 3, SymPy and SciPy.

## Relationship to prior work

Mondal, Sarkar and Sk [1] establish the model, positivity, boundedness, and the predator-free equilibrium and give the **strict** local stability condition \(c_1f(L)<d_3\) in their local stability analysis. Their reproduction-number and disease-free results concern an equilibrium with positive susceptible predators; the predator-free equality and its global nonlinear rates are different. The exact cancellation in \(\dot P\), the integrable positive-part upper bound, and the fear-independent prey deficit are the contribution assessed here. Comparable published results on critical extinction in other predator–prey and delayed epidemic systems address different equations or invasion variables and do not establish these coefficients for [1]. The related Sk–Pal–Majumdar–Mondal [2] study uses two infection routes; only bibliographic/abstract material was accessible, so equivalent analyses there remain a priority risk.

## Limitations

The global result uses strictly positive fear \(K>0\), strictly larger infected-predator mortality \(d_4>d_3\), and positive initial prey/predator total. It makes no claim about the borderline \(K=0\) or \(d_4=d_3\), about the disease-only threshold at a coexistence equilibrium, about stochastic survival, or about finite-time extinction. The exponential statement concerns infected predators at the predator-free threshold; its detailed polynomial prefactor is not derived. The exact source date uses the earliest publicly verified release identified (2023-10-03); earlier unseen preprints cannot be excluded. Self-review is not independent validation.

## References

[1] B. Mondal, A. Sarkar, N. Sk, “Treatment of infected predators under the influence of fear-induced refuge,” *Scientific Reports* 13, 16623 (2023), published 2023-10-03, https://doi.org/10.1038/s41598-023-43021-0 ; full open-access article: https://www.nature.com/articles/s41598-023-43021-0 .

[2] N. Sk, S. Pal, P. Majumdar, B. Mondal, “Dynamics of an eco-epidemiological system: Predators get infected in two paths,” *Journal of Computational Science* 69, 102023 (2023), https://doi.org/10.1016/j.jocs.2023.102023 (abstract/bibliographic comparison only).
