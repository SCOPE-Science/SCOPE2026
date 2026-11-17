# Physical-time circle conjugacy and exact period arithmetic for a discontinuous risk reset map

## Finding
Consider the discrete planar reset system
\[
 F(x,s)=(x',s'),\qquad x'=-r x+(\beta+r)s,\qquad
 s'=\Psi(s+x'-x),\qquad
 \Psi(u)=\begin{cases}u,&|u|\le1,\\0,&|u|>1.\end{cases}
\]
For every \(0<r<1\), \(\beta>1\) with \(r(\beta+1)>1\), there is an explicit invariant union \(K\) of four line segments, with appropriate half-open endpoints, on which **the original one-step map \(F\), not merely its Poincaré return, is Borel conjugate to a rigid rotation of a circle of circumference \(2(1+a)\) by distance \(1\)**. Here
\[
 \mu=\frac r{1+r},\quad \nu=\beta+\mu,\quad
 L=\log(\nu/\mu),\quad
 a=\frac{\log(1/r)}L\in(0,1/2).
\]
Consequently:

1. If \(a=p/q\) in lowest terms, every point of \(K\) has the **same prime period**, exactly \(2(p+q)/\gcd(q,2)\). In particular it is \(p+q\) for even \(q\), and \(2(p+q)\) for odd \(q\).
2. If \(a\) is irrational, every orbit in \(K\) is dense in its planar closure; the restriction is uniquely ergodic and its Koopman operator has pure point spectrum \(\{e^{2\pi i k/[2(1+a)]}:k\in\mathbb Z\}\).
3. For any section-started trajectory in \(K\), the time \(t_n\) of its \(n\)-th subsequent visit to \(s=0\) satisfies \(t_n=n(1+a)+z_n-z_0\), where \(z_j\in(0,1]\) is an explicit logarithmic coordinate. In particular \(|t_n-n(1+a)|<1\) for all \(n\). Thus the reset frequency is exactly \(1/(1+a)\), with bounded discrepancy, for every orbit in \(K\).
4. When \(a\) is irrational, the unique invariant probability on \(K\) has the explicit four-segment formula in the proof below; its section mass is \(1/(1+a)\) and its nonreset intermediate-state mass is \(a/(1+a)\).

## Assumptions and scope
The branch convention is **strict** resetting: if \(|u|=1\) the output is \(u\), not zero. The state space is \(\mathbb R\times[-1,1]\). All results concern the specified recurrent subsystem \(K\), not the entire state space: the full system also has a segment of equilibrium points. No global basin-of-attraction or transverse stability is claimed. The half-open endpoint convention is essential to the exact conjugacy and period statement.

Set
\[
 q_1=\frac1{1+r},\quad q_2=\frac1{(1+r)(\beta+1)},\quad
 \chi=\beta(1+r)+r,\qquad X(z)=\mu e^{Lz}.
\]
The domain condition is exactly \(\mu>q_2\); one has \(\mu<q_1<\nu\), \(\chi\mu=r\nu\), \(\chi q_1=\nu\), and \(\nu/\mu=\chi/r\). It follows that \(0<a<1/2\). Let
\[
 S_\pm=\{(\pm X(z),0):0<z\le1\},\quad
 I_\pm=\{F(\pm X(z),0):0<z\le a\},\qquad
 K=S_+\cup S_-\cup I_+\cup I_-.
\]
These four sets are disjoint (the two intermediate segments have nonzero opposite signs of \(s\)); they are Borel arcs, not four closed intervals.

## Proof
**1. Exact first-reset branches.** For \(x>0\) and initial \((x,0)\), the first iterate is \((-rx,-(1+r)x)\) if \(x\le q_1\), and \((-rx,0)\) if \(x>q_1\). If \(q_2<x\le q_1\), the tentative second value of \(s\) is \(-(\beta+1)(1+r)x<-1\); hence the second iteration resets, at \((-\chi x,0)\). By odd symmetry the corresponding assertions hold for \((-x,0)\). Because \(\mu>q_2\), the first return of a section point \((\pm x,0)\), \(x\in(\mu,\nu]\), is therefore exactly
\[
 (\pm x,0)\longmapsto
 \begin{cases}(\mp\chi x,0)&\mu<x\le q_1\quad\text{after 2 steps},\\
 (\mp r x,0)&q_1<x\le\nu\quad\text{after 1 step}.
 \end{cases}
\]
The magnitudes lie in \((\mu,\nu]\), since multiplication by \(\chi\) maps \((\mu,q_1]\) onto \((r\nu,\nu]\), while multiplication by \(r\) maps \((q_1,\nu]\) onto \((\mu,r\nu]\).

**2. Logarithmic return and special roof.** The coordinate \(z=\log(x/\mu)/L\in(0,1]\) converts the unsigned first return to
\[
 z\longmapsto z-a+\mathbf1_{\{z\le a\}},
 \qquad \tau(z)=1+\mathbf1_{\{z\le a\}}.
\]
Indeed \(e^{-La}=r\) and \(e^{L(1-a)}=\chi\). Both expressions use the right-closed representation of the circle \((0,1]\), so they also hold at \(z=a\) and \(z=1\). The first expression is rotation by \(-a\) modulo one, and \(\tau(z)\in\{1,2\}\) is the **number of actual steps between resets**, not an artificial time parameter. The sign changes at each reset.

**3. Exact original-time conjugacy.** Put \(\Lambda=1+a\) and \(\Gamma=2\Lambda\). Represent the circle of circumference \(\Gamma\) by \((0,\Gamma]\), with addition modulo \(\Gamma\) returning values to that right-closed interval. Define the bijection \(H:(0,\Gamma]\to K\) on four consecutive arcs:
\[
 H(\theta)=\begin{cases}
 (X(\theta),0),&0<\theta\le1,\\
 F(X(\theta-1),0),&1<\theta\le\Lambda,\\
 (-X(\theta-\Lambda),0),&\Lambda<\theta\le\Lambda+1,\\
 F(-X(\theta-\Lambda-1),0),&\Lambda+1<\theta\le\Gamma.
 \end{cases}
\]
The four images are exactly \(S_+,I_+,S_-,I_-\). The branch equations in step 1, together with \(X(z-a)=rX(z)\) and \(X(1+z-a)=\chi X(z)\), give by direct inspection of the four arcs
\[
 F(H(\theta))=H\bigl((\theta+1)\bmod\Gamma\bigr)
 \qquad(0<\theta\le\Gamma).
\]
For example, a positive section phase \(z\le a\) moves first to the positive-labelled intermediate arc at phase \(1+z\) and next to the negative section at phase \(2+z\); a section phase \(z>a\) moves directly to the opposite-sign section at phase \(1+z\). The negative-sign cases follow by odd symmetry and reduction modulo \(\Gamma\). At the strict boundary \(z=a\), the **right-closed arc convention** assigns the intermediate state to the endpoint \(\theta=\Lambda\) and the subsequent section point \((-\nu,0)\) to \(\theta=\Lambda+1\); no boundary point is discarded. Thus \(F|_K\) is Borel conjugate to rigid translation by \(1\) on this circle.

**4. Periods and irrational dynamics.** For \(a=p/q\) reduced, the normalized rotation angle is \(1/\Gamma=q/[2(p+q)]\). Its reduced denominator, hence every prime period on \(K\), is \(2(p+q)/\gcd(q,2)\). If \(a\) is irrational, the rotation angle is irrational; rotation minimality and unique ergodicity transfer through the piecewise continuous Borel bijection. Every point of \(K\) lies in the closure of each orbit because every arc of \(H\) is continuous on its right-closed parameter interval. The irrational rotation has Haar probability as its unique invariant probability. Its Koopman eigenbasis is \(e^{2\pi i k\theta/\Gamma}\), giving the stated pure point spectrum, with no claim about the Koopman spectrum outside \(K\).

**5. Reset clock and invariant probability.** At consecutive section returns, the log coordinates obey \(z_{j+1}-z_j=-a+\mathbf1_{\{z_j\le a\}}\). Summing the return times \(\tau(z_j)=1+\mathbf1_{\{z_j\le a\}}\) telescopes to
\[
 t_n=n(1+a)+z_n-z_0,
 \qquad |t_n-n(1+a)|<1.
\]
The formula is exact for every section-started point of \(K\), including rational and boundary phases. At irrational \(a\), the invariant probability is
\[
 \eta=\frac1{2(1+a)}\sum_{\varepsilon\in\{-1,1\}}
 \left[\int_0^1\!\delta_{(\varepsilon X(z),0)}\,dz+
 \int_0^a\!\delta_{F(\varepsilon X(z),0)}\,dz\right].
\]
Each of its four terms is the image of normalized arc length under \(H\), and the two section arcs have combined mass \(1/(1+a)\). The section visit frequency and its complement follow. This completes the proof.

## Verification
A standalone exact-rational checker `checker.py` reconstructs the **original** reset update \(F\), not an assumed return map. For \(r=1/2\) and \(\beta=(2^q-1)/3\), integers \(3\le q\le12\) give \(a=1/q\); 4,750 prime-period assertions, 11,940 exact branch checks and 170 exact original-step phase-circle assertions are checked, including the exceptional cut locations. A separate 10,000-case deterministic floating-point sweep tests the exact one- and two-step return formulas for admissible parameters. These finite checks corroborate, but do not prove, the all-real-parameter theorem. The proof relies on the four explicit branch equations above.

## Relationship to prior work
Kryzhevich, Avrutin, Begun, Rachinskii and Tajbakhsh (arXiv:2104.11825v3, sections 7–8) define the discontinuous risk reset model and derive a logarithmic Poincaré interval translation. In its one-discontinuity parameter region they observe that the **unsigned first-return map**, viewed after identifying endpoints, is a circle rotation. That reduction and its formulas are prior work. The present result instead **linearizes every original physical iterate** by exhibiting the four-arc circle \(H\), thereby resolving the return-time suspension, the sign alternation, exact common prime physical periods, original-clock discrepancy, and the unique stationary law/spectrum on the recurrent component. The extra conjugacy is not automatic from a circle-rotation first-return map for arbitrary return-time roofs.

Arnold et al. (arXiv:1605.00584) analyze a different system with the saturated stop operator \(\Phi(u)=\max(-1,\min(1,u))\); it is not the strict-to-zero reset operator used here. General special-flow and rotation theory supplies context for the roof construction but not this specific four-arc conjugacy. The analysis is confined to the stated parameter sector and half-open recurrent subsystem.

## Limitations
The result does not classify initial conditions outside \(K\), global basins, transverse attraction, dynamics beyond \(r(\beta+1)>1\), nor the other interval-translation regimes. The full planar map contains equilibria and does **not** inherit global unique ergodicity. The circle conjugacy is Borel/piecewise continuous, not a homeomorphism from an ordinary Euclidean circle onto the embedded arcs. Literature-priority searches cannot exclude every equivalent presentation of the same return-time suspension; an independent audit remains unperformed.

## References
1. S. Kryzhevich, V. Avrutin, N. Begun, D. Rachinskii, K. Tajbakhsh, *Dynamics of Systems with a Discontinuous Hysteresis Operator and Interval Translation Maps*, arXiv:2104.11825v3 (first posted 2021-04-23), https://arxiv.org/abs/2104.11825 . Especially sections 7–8.
2. M. Arnold, N. Begun, P. Gurevich, E. Kwame, H. Lamba, D. Rachinskii, *Dynamics of Discrete Time Systems with a Hysteresis Stop Operator*, arXiv:1605.00584 (2016), https://arxiv.org/abs/1605.00584 . Distinct saturation convention.
3. B. Fayad and A. Windsor, *A dichotomy between discrete and continuous spectrum for a class of special flows over rotations*, Journal of Modern Dynamics 1 (2007), 107–122, https://doi.org/10.3934/jmd.2007.1.107 . General special-flow context.
