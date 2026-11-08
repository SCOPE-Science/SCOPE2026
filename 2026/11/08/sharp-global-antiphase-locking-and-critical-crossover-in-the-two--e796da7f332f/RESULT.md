# Sharp global antiphase locking and critical crossover in the two-clock sine map

## Finding
Consider the degree-one circle map
\[
F_h(\theta)=\theta+2h\sin\theta\pmod{2\pi},\qquad h>0.
\]
The antiphase fixed point \(\theta=\pi\) attracts **every other circle point except the in-phase fixed point** \(\theta=0\) exactly when \(0<h\leq1\). For \(h>1\), antiphase is locally repelling. At the sharp, nonhyperbolic boundary \(h=1\), define the circular error \(v_n=\operatorname{dist}_{\mathbb T}(F_1^n(\theta_0),\pi)\). Every orbit other than the in-phase fixed point converges to antiphase. If it does not reach antiphase in finitely many steps, there is a finite constant \(C(\theta_0)\) such that
\[
\boxed{v_n^{-2}=\frac23n+\frac9{20}\log n+C(\theta_0)+o(1).}
\]
The excluded finite-hitting seeds form a countable set and already converge exactly. Moreover, for any fixed \(v_0\in(0,1]\), \(\theta_0=\pi\pm v_0\), and any fixed \(t>0\), the *subcritical finite-time crossover* satisfies
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon\,\operatorname{dist}_{\mathbb T}\!\left(F_{1-\varepsilon}^{\lfloor t/\varepsilon\rfloor}(\theta_0),\pi\right)^{-2}=\frac{e^{4t}-1}{6}.}
\]
In particular, \(\sqrt{n}\,v_n\to\sqrt{3/2}\) for every non-finite-hitting critical orbit. These assertions concern the quotient phase difference, not the absolute common phase of the two oscillators.

## Assumptions and scope
The phase space is \(\mathbb T=\mathbb R/2\pi\mathbb Z\). All iterations use the physical one-update clock, not a second-iterate reparameterization. The parameter \(h\) is the positive edge weight times the update strength, normalized so the two-vertex graph has edge weight one. The circular distance \(v\in[0,\pi]\) is the smallest angular distance to antiphase. For the crossover statement the starting distance \(v_0\in(0,1]\) is held fixed while \(\varepsilon\to0^+\). A finite-hitting orbit is one with \(F_1^m(\theta_0)=\pi\) for some integer \(m\ge0\). The \(o(1)\) critical remainder is pointwise in the non-finite-hitting initial point; no uniform estimate over all initial points is asserted.

## Proof
**1. Global and sharp parameter classification.** Set \(u=\theta-\pi\in(-\pi,\pi]\) and write \(K=2h\). The canonical representative of the next error is \(u'=u-K\sin u\) whenever \(0<K\le2\). Indeed, for every \(0<|u|<\pi\),
\[
0<K|\sin u|<2|u|,
\quad\text{so}\quad |u-K\sin u|<|u|<\pi.
\]
The same strict decrease holds at every nonfixed iterate. The only possible nonzero limiting error would satisfy \(|u-K\sin u|=|u|\), which is impossible by the displayed strict inequality (equivalently use compactness and continuity of the error decrement). Therefore every point other than \(\theta=0\) tends to \(\pi\), and no other periodic orbit exists for \(0<h\le1\). For \(h>1\), \(F_h'(\pi)=1-2h<-1\), hence antiphase is locally repelling and cannot attract all nearby points. This establishes the exact closed global-locking interval.

**2. Critical pointwise law.** At \(h=1\), \(v_{n+1}=|v_n-2\sin v_n|\), which is strictly between zero and \(v_n\) except when the next iterate lands exactly at antiphase. For any orbit never hitting antiphase, \(v_n\downarrow0\), and eventually \(2\sin v_n-v_n>0\), giving
\[
 v_{n+1}=2\sin v_n-v_n=v_n\left(1-\frac{v_n^2}{3}+\frac{v_n^4}{60}+O(v_n^6)\right).
\]
Set \(w_n=v_n^{-2}\). Taylor expansion with a controlled remainder yields
\[
 w_{n+1}-w_n=\frac23+\frac3{10w_n}+O(w_n^{-2}).\tag{1}
\]
First, \(w_n/n\to2/3\) by telescoping and Cesàro averaging, because the increment tends to \(2/3\). Thus \(w_n=(2/3)n+O(\log n)\), using (1) and \(w_n\asymp n\). Subtracting the main and logarithmic terms gives
\[
\left(w_{n+1}-\frac23(n+1)-\frac9{20}\log(n+1)\right)-
\left(w_n-\frac23n-\frac9{20}\log n\right)=O\!\left(\frac{\log n}{n^2}\right).
\]
The right side is absolutely summable, so the corrected sequence has a finite limit \(C(\theta_0)\), proving the two-term expansion. For each \(m\), the equation \(F_1^m(\theta)=\pi\) has finitely many solutions: a nonconstant real-analytic circle map iterate cannot be identically \(\pi\), since \(0\) is fixed. Their union is countable.

**3. Subcritical crossover.** Fix \(v_0\in(0,1]\) and \(0<\varepsilon\le1/10\). Set \(h=1-\varepsilon\). For every \(v\in(0,1]\), elementary sine inequalities give
\[
0<2h\sin v-v\le v\left(1-\frac{19h}{60}v^2\right)<v.
\]
Consequently the iterated error obeys \(v_{n+1}=2h\sin v_n-v_n\in(0,v_n)\), and \(w_n=v_n^{-2}\) obeys \(w_n\ge w_0+cn\) for some universal \(c>1/2\). Write \(A_\varepsilon=(1-2\varepsilon)^{-2}\) and \(B_\varepsilon=2(1-\varepsilon)/[3(1-2\varepsilon)^3]\). The same analytic Taylor expansion, uniform for \(v\in(0,1]\) and \(\varepsilon\in[0,1/10]\), gives
\[
 w_{n+1}=A_\varepsilon w_n+B_\varepsilon+R_{n,\varepsilon},\qquad |R_{n,\varepsilon}|\le \frac{C_0}{w_n}.
\]
For \(n=\lfloor t/\varepsilon\rfloor\), summing this affine recurrence and using \(w_k\ge w_0+ck\), \(A_\varepsilon^n\le e^{O(t)}\), gives a remainder bounded by \(O_t(\log(n+1))\). Multiplication by \(\varepsilon\) makes it vanish. Since \(A_\varepsilon^{\lfloor t/\varepsilon\rfloor}\to e^{4t}\), \(B_\varepsilon\to2/3\), and \(\varepsilon/(A_\varepsilon-1)\to1/4\), we obtain
\[
\varepsilon w_{\lfloor t/\varepsilon\rfloor}\longrightarrow
\frac{2}{3}\cdot\frac{e^{4t}-1}{4}=\frac{e^{4t}-1}{6}.
\]
This completes the proof.

## Verification
The companion `verify.py` checks the exact Taylor coefficients of the reciprocal-square recurrence and several independent numerical orbits and crossover ratios. These checks support, but do not replace, the global sine inequality and summable-remainder proof. Reproduce with `python verify.py` and Python 3 plus SymPy. The hypotheses and boundary conventions are explicit above; finite numerical iterates do not prove an infinite-time assertion.

## Relationship to prior work
Buescu–D'Aniello–Oliveira (arXiv:2610.10993v1, October 7, 2026), Sections 2, 3 and 5, establish the two-vertex phase quotient, strict descent for \(0<h<1\), and Morse–Smale dynamics for \(0<h<1/2\). Their general strict-descent coefficient vanishes at \(h=1\), and their result does not give the endpoint's global convergence, the exact logarithmic correction, or its precritical scaling function. The original Oliveira–Melo (2015) experimental two-clock model concerns phase-opposition synchronization; it is not a source for these exact endpoint iterates. Standard sine-circle-map literature already establishes the linear multiplier criterion and noninvertible-map threshold; neither is claimed as new. Prior work on flip normal forms provides generic algebraic convergence mechanisms; the new scope is the global circle-map endpoint, evaluated coefficient \(9/20\), and finite-time crossover on the physical update clock. A previously published result on alternating two-colour period-two orbits concerns \(h>1\) and does not imply the \(h=1\) endpoint law.

## Limitations
This is a theorem for the exact two-clock sinusoidal phase quotient only, not an arbitrary oscillator network, noisy physical clock, heterogeneous coupling law, or continuous-time model. It does not classify all dynamics for \(h>1\), prove uniform endpoint convergence over an initial phase interval containing the repelling fixed point, or provide a uniform critical remainder over finite-hitting seeds. The crossover limit is for fixed initial distances at most one radian. A general theory of one-dimensional flip normal forms may reproduce parts of the local asymptotic calculation; historical-priority claims for the evaluated global and crossover statement remain provisional. Independent external validation has not been performed.

## References
1. J. Buescu, E. D'Aniello, and H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, first publicly available October 7, 2026. https://arxiv.org/html/2610.10993v1 .
2. H. M. Oliveira and L. V. Melo, *Huygens synchronization of two clocks*, Scientific Reports **5**, 11548 (2015), https://doi.org/10.1038/srep11548 .
3. *Synchronization–desynchronization transitions in networks of circle maps with sinusoidal coupling* (2023), https://doi.org/10.1088/1674-1056/acc062 .
