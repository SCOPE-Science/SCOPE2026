# Unbounded stable-state multiplicity and fold staircase in a sinusoidal three-echelon flow

## Finding

Fix real parameters \(a,m,c>0\) and \(r>a/m\). In the autonomous, sinusoidally modified three-echelon flow
\[
\dot x=-ax+my,\qquad
\dot y=rx+p\sin x-y-xz,\qquad
\dot z=xy-cz,
\]
let \(p\ge0\) vary while the other four parameters remain fixed. Put \(B=r-a/m>0\), \(C=a/(mc)>0\), and let \(N_{\mathrm{eq}}(p)\) count distinct real equilibria and \(N_{\mathrm{sink}}(p)\) count equilibria at which all three eigenvalues have negative real part. Then, as \(p\to+\infty\),
\[
N_{\mathrm{eq}}(p)=\frac{2}{\pi C^{1/3}}p^{1/3}+O(1),\qquad
N_{\mathrm{sink}}(p)=\frac{1}{\pi C^{1/3}}p^{1/3}+o(p^{1/3}).
\]
In particular, the number of *simultaneously locally asymptotically stable* stationary operating states is unbounded as the amplitude of the bounded-in-state sinusoidal feedback increases.

There is also an explicit infinite staircase of equilibrium folds. Set \(R=\sqrt{B/C}\), \(P(x)=Cx^3-Bx\), and, for any integer \(j\ge1\) with \(2\pi j>R\), let \(I_j=(2\pi j,(2j+1)\pi)\). The number
\[
p_j=\min_{x\in I_j}\frac{P(x)}{\sin x}
\]
is positive, attained at exactly one interior point \(x_j\), and the sequence of these thresholds is strictly increasing. There are no equilibrium first-coordinate roots in \(I_j\) for \(p<p_j\), one double root for \(p=p_j\), and precisely two simple roots for \(p>p_j\). The negatives of these roots occur simultaneously by symmetry. Defining \(t_j=(2j+1/2)\pi\), one has
\[
x_j=t_j-\frac3{t_j}+O(t_j^{-3}),\qquad
p_j=Ct_j^3-\left(B+\frac92 C\right)t_j+O(t_j^{-1})
\]
as \(j\to\infty\). These are scalar equilibrium folds; no assertion of immediate three-dimensional stability at a fold is needed or made.

## Assumptions and scope

All variables and parameters are real. The flow is exactly the three-echelon sinusoidal-feedback system above, with no state-positivity restriction; the originating model also discusses negative coordinates and has a \((x,y,z)\mapsto(-x,-y,z)\) symmetry. The feedback amplitude \(p\) is unbounded only as a mathematical parameter; this is not a claim that arbitrarily large uncertainty amplitudes are economically realistic. Counts concern isolated finite equilibria, not periodic or chaotic attractors, and the asymptotic statements fix \(a,m,c,r\) while varying \(p\).

## Proof

**1. Exact scalar reduction and finite root count.** At an equilibrium, the first and third equations give \(y=ax/m\) and \(z=ax^2/(mc)=Cx^2\). The second then reduces to
\[
h_p(x):=Bx-Cx^3+p\sin x=0.
\]
Conversely, each real root determines one equilibrium. The function is odd. For fixed \(p\), the cubic term dominates at infinity, so every root lies in a compact interval; analyticity and nonidentity imply finitely many roots. For \(x>R\), \(P(x)>0\), and the equation becomes \(p\sin x=P(x)\). Consequently no roots occur on negative-sine lobes. Let \(T_p>R\) be the unique solution of \(P(T_p)=p\); there are no positive roots beyond \(T_p\), and \(T_p=(p/C)^{1/3}+O(p^{-1/3})\).

**2. Exactly two roots per fully activated lobe.** On any \(I_j\) with \(2\pi j>R\), \(h_p=-P+p\sin x\) is strictly concave because \(h_p''=-6Cx-p\sin x<0\). It is negative at both endpoints. Hence its unique maximum crosses zero at a unique amplitude \(p_j=\min_{I_j}P/\sin\); the root counts are respectively zero, one double, or two simple roots as stated. If the lobe midpoint \(t_j\le T_p\), then \(h_p(t_j)=p-P(t_j)\ge0\), so that lobe has two roots except at one possible equality. If the entire lobe starts above \(T_p\), it has none. There are only boundedly many ambiguous lobes, since each has fixed length \(\pi\) and they are separated by another \(\pi\). All roots with \(x\le R\) contribute \(O(1)\) to the count, uniformly for large \(p\): on the compact interval \([0,R]\), \(h_p/p\to\sin x\) in \(C^1\) and \(\sin x\) has finitely many simple zeros. Thus the number of positive roots is \(T_p/\pi+O(1)\); including negatives and the origin proves the equilibrium-count formula.

**3. Increasing folds and their asymptotics.** Since \(P\) is strictly increasing on \((R,\infty)\), for every \(x\in I_j\) the shifted point \(x+2\pi\in I_{j+1}\) satisfies \(P(x+2\pi)/\sin(x+2\pi)>P(x)/\sin x\). The minima are strict and satisfy \(p_{j+1}>p_j\). At the minimum, \(P'(x_j)\sin x_j=P(x_j)\cos x_j\), so \(x_j\) lies left of \(t_j\). Writing \(x_j=t_j-\delta_j\) gives
\[
\tan\delta_j=\frac{P'(t_j-\delta_j)}{P(t_j-\delta_j)}
=\frac3{t_j}+O(t_j^{-3}),
\]
whence \(\delta_j=3/t_j+O(t_j^{-3})\). Expanding \(P(t_j-\delta_j)/\cos\delta_j\) gives the stated two-term expression for \(p_j\). The strict concavity also gives \(h_p''(x_j)<0\), while \(\partial_p h_p(x_j)=\sin x_j>0\), proving nondegenerate scalar fold contact.

**4. Complete stability test.** At an equilibrium indexed by \(x\), its Jacobian is
\[
J(x)=\begin{pmatrix}-a&m&0\\r+p\cos x-Cx^2&-1&-x\\(a/m)x&x&-c\end{pmatrix}.
\]
The characteristic polynomial is \(\lambda^3+A_1\lambda^2+A_2\lambda+A_3\), where
\[
A_1=a+c+1,\quad
A_2=a(1+c)+c-mr-mp\cos x+(1+a/c)x^2,\quad
A_3=-mc\bigl(B-3Cx^2+p\cos x\bigr)=-mc h_p'(x).
\]
The Routh–Hurwitz conditions are \(A_2>0\), \(A_3>0\), and \(A_1A_2>A_3\) (with \(A_1>0\) automatic). On each fully activated positive-sine lobe, the lower root satisfies \(h_p'>0\), hence \(A_3<0\) and cannot be a sink. At most one *positive-coordinate* sink therefore occurs on each such lobe.

**5. Almost all activated lobes contain sinks.** Fix \(\eta\in(0,1)\). Consider all sufficiently large \(p\) and all lobes satisfying \(2\pi j>R\) and \((2j+1)\pi\le(1-\eta)T_p\). At their midpoint \(h_p>0\), hence there is a right-hand root \(x_{j,+}\in(t_j,(2j+1)\pi)\), where \(\cos x_{j,+}<0\). Furthermore
\[
0<\sin x_{j,+}=\frac{P(x_{j,+})}{p}\le\frac{P((1-\eta)T_p)}{P(T_p)}\longrightarrow(1-\eta)^3<1.
\]
Therefore \(\cos x_{j,+}\le-\kappa_\eta<0\) uniformly over those lobes once \(p\) is large. All roots satisfy \(x^2=O(p^{2/3})\). Uniformly over this family,
\[
A_2=mp|\cos x|+O(p^{2/3}),\quad
A_3=mcp|\cos x|+O(p^{2/3}),\quad
A_1A_2-A_3=m(a+1)p|\cos x|+O(p^{2/3}),
\]
so every right root is a hyperbolic sink. Reflection produces a second sink at negative \(x\). The number of qualifying positive lobes is \((1-\eta)T_p/(2\pi)+O(1)\). Thus
\[
\liminf_{p\to\infty}\frac{N_{\mathrm{sink}}(p)}{T_p}\ge\frac{1-\eta}{\pi}.
\]
Conversely the \(O(1)\) compact roots and at most one positive sink per lobe, together with symmetry, imply \(\limsup N_{\mathrm{sink}}(p)/T_p\le1/\pi\). Letting \(\eta\downarrow0\) proves the stable-equilibrium asymptotic. Hyperbolic sinks are locally asymptotically stable by the linearization theorem.

## Verification

The accompanying Python script `check_equilibria.py` (with package requirements in `requirements.txt`) reconstructs all four characteristic coefficients symbolically; verifies the determinant identity; locates positive-sine-lobe roots at two large amplitudes for the published parameter quadruple; checks the full Routh–Hurwitz test; and compares the fold minimum with the derived two-term large-index expansion. Successful execution prints `VERIFY_OK`. The finite examples only corroborate the proof and are not evidence that a finite census establishes an infinite asymptotic.

## Relationship to prior work

Johansyah et al. (2026), Equation (6), introduced exactly the model above, derived its equilibrium equations, and numerically found an origin and two stable nonzero equilibria at the parameter values \((m,n,r,k,p)=(14,11,55,6,0.2)\). Their bifurcation figures explore multistability for moderate amplitudes, but do not state an unbounded equilibrium/sink count, asymptotic cube-root law, or complete increasing sequence of fold thresholds. The underlying cubic-versus-sine root-count mechanism is classical; what is added here is the quantitative simultaneous **three-dimensional sink** law for this specified coupled flow. The 2025 three-tier supply-chain article uses a different jerk-form vector field with absolute-value nonlinearity; the September 2026 four-dimensional supply-chain paper concerns a different four-state system. A published finite fixed-parameter sine-controlled multiscroll equilibrium census concerns a distinct vector field and does not imply the parameter-uniform theorem here.

## Limitations

The assertions hold for fixed positive \(a,m,c\), \(r>a/m\), and unbounded \(p\); no financial feasibility or policy claim is made for large amplitudes. The number of sinks is determined to leading order, not by an exact finite-\(p\) formula. The theorem does not characterize global basins, chaotic attractors, or the precise Hopf stability transitions near every scalar fold. In particular, a newly created branch need not be a sink immediately at its fold. Historical priority remains provisional because not every potentially relevant external article could be fully inspected. Independent audit has not been performed.

## References

1. M. D. Johansyah et al., “Nonlinear dynamics and control of a 3-echelon chaotic supply chain system having two stable equilibrium points,” *Scientific Reports* **16**, 21190 (first publicly available 14 April 2026), https://doi.org/10.1038/s41598-026-46161-1. Exact model in Eq. (6), equilibrium computation and stability in Sect. 2, parameter bifurcations in Sect. 3.
2. J. Nahar et al., “Dynamic behavior and control analysis in a new chaotic three-tier supply chain system with a sinusoidal modelling uncertainty for resilient manufacturing networks,” *Scientific Reports* **16**, 431 (first published 30 December 2025), https://doi.org/10.1038/s41598-025-29907-1. Different jerk-form model.
3. J. Nahar et al., “Dynamic analysis, and offset boosting control of a new multi-echelon chaotic supply chain model with a sinusoidal nonlinearity for SDG-oriented resilient logistics,” *Scientific Reports* (21 September 2026), https://doi.org/10.1038/s41598-026-72344-x. Different four-dimensional model, compared using accessible abstract and metadata.
