# An effective golden-mean repeller and its Lyapunov law in a replicator family

## Finding
For the two-strategy replicator map
\[
f_{a,b}(x)=\frac{x}{x+(1-x)e^{a(x-b)}},\qquad 0<x<1,
\]
**every** \(a\ge100\) and \(1/4\le b\le2/5\) admit a compact uniformly expanding invariant Cantor set \(Q_{a,b}\subset(0,1)\) on which the dynamics is topologically conjugate to the one-sided golden-mean shift (binary sequences without consecutive ones). In particular \(h_{\mathrm{top}}(f_{a,b})\ge\log\varphi\), with \(\varphi=(1+\sqrt5)/2\), on this entire unbounded two-parameter strip.

There is a unique maximum-entropy invariant probability \(\mu_{a,b}\) on this specified repeller. Its (positive) Lyapunov exponent has the following **uniform** two-term asymptotic as \(a\to\infty\), with \(b\) anywhere in \([1/4,2/5]\):
\[
\begin{aligned}
\chi(\mu_{a,b})={}&\frac{\varphi^2}{\varphi^2+1}\log a\\
&+\frac{\varphi}{\varphi^2+1}\log[b(1-b)]
 +\frac1{\varphi^2+1}\log[2b(1-2b)]
 +O(a^{-1}).
\end{aligned}
\]
At the distinguished game-balance parameter \(b=1/3\), the two nontrivial branch factors coincide, so the constant term simplifies exactly to \(\varphi^2(\varphi^2+1)^{-1}\log(2/9)\). No assertion is made that the displayed sufficient cutoff \(100\) is optimal.

## Assumptions and scope
All parameters are real. The state space is the open interval \((0,1)\). Let \(h(x)=\log((1-x)/x)\). It conjugates \(f_{a,b}\) with
\[
g_{a,b}(y)=y+\frac{a}{1+e^y}-ab,\quad y\in\mathbb R.
\]
For each parameter pair put \(I_0=[-2,2]\), \(I_1=[ab-5,ab+5]\), and define
\[
K_{a,b}=\bigcap_{n\ge0}g_{a,b}^{-n}(I_0\cup I_1),\qquad Q_{a,b}=h^{-1}(K_{a,b}).
\]
The symbols are indexed so that \(I_0\) is the central decreasing branch and \(I_1\) the far-right increasing branch. The maximum-entropy measure means the pushforward of the unique Parry measure on the golden-mean subshift through this explicit coding, **not** an invariant law describing typical Lebesgue initial data.

## Proof
**1. Uniform interval covering.** The elementary bounds \(7<e^2<15/2\) imply
\[
u_-:=\frac{e^2}{1+e^2}>\frac78,\qquad u_+:=\frac1{1+e^2}<\frac18.
\]
Throughout the stated strip, the intervals are disjoint since \(ab-5\ge20>2\). Direct substitution gives
\[
\begin{split}
g(-2)-(ab+5)&=a(u_--2b)-7>100(7/8-4/5)-7=1/2,\\
g(2)+2&=4+a(u_+-b)<4-100/8<0.
\end{split}
\]
Also \(0<a e^{5-ab}\le100e^{-20}<10^{-3}\); this holds uniformly because \(a\mapsto ae^{-a/4}\) decreases for \(a>4\). Hence
\[
g(ab-5)<-5+10^{-3}<-2,\qquad
2<5<g(ab+5)<6<ab-5.
\]
The exact derivative \(g'(y)=1-a e^y/(1+e^y)^2\) is negative on \(I_0\), with \(|g'|>9\), and lies in \((999/1000,1)\) on \(I_1\). Indeed \(e^2/(1+e^2)^2>1/10\), while \(a e^{5-ab}<10^{-3}\). The preceding endpoint bounds therefore give, with full branch coverage,
\[
g(I_0)\supset I_0\cup I_1,\qquad
 g(I_1)\supset I_0,\qquad g(I_1)\cap I_1=\varnothing.
\]

**2. Coding and hyperbolicity.** Let \(\Sigma_A\) denote the one-sided subshift with adjacency matrix \(A=\begin{pmatrix}1&1\\1&0\end{pmatrix}\). Each permitted edge \(i\to j\) has a single smooth inverse branch of \(g|_{I_i}\) defined on all of \(I_j\). No itinerary can have the forbidden edge \(1\to1\). Every two consecutive permitted symbols contain a zero, and consequently \(|(g^2)'|>9(999/1000)>8.99\) along \(K_{a,b}\). The nested inverse cylinders therefore have diameters tending to zero uniformly. Every sequence in \(\Sigma_A\) defines one and only one point of \(K_{a,b}\), and these points vary continuously in the product topology. Since \(I_0\cap I_1=\varnothing\), the coding is injective and is a topological conjugacy. The invariant set is Cantor and uniformly expanding; its entropy is \(\log\varphi\), yielding the stated lower bound for the full interval map.

**3. Lyapunov asymptotic.** The golden-mean Parry measure has stationary symbol weights
\[
\pi_0=\frac{\varphi^2}{\varphi^2+1},\qquad \pi_1=\frac1{\varphi^2+1},
\]
and directed-edge weights \(w_{00}=\varphi/(\varphi^2+1)\), \(w_{01}=w_{10}=1/(\varphi^2+1)\). Write \(L(y)=1/(1+e^y)\), so \(g'(y)=1-aL(y)(1-L(y))\). For an edge \(0\to0\), both the present and next coordinates are in \([-2,2]\), and the exact recurrence implies \(L(y)=b+O(a^{-1})\). For an edge \(0\to1\), the next coordinate lies in \([ab-5,ab+5]\), and the same recurrence implies \(L(y)=2b+O(a^{-1})\). These estimates, including their constants, are uniform for \(b\in[1/4,2/5]\). Consequently,
\[
\begin{array}{ll}
\log|g'(y)|=\log a+\log[b(1-b)]+O(a^{-1})&\text{on edge }00,\\
\log|g'(y)|=\log a+\log[2b(1-2b)]+O(a^{-1})&\text{on edge }01,\\
\log|g'(y)|=O(ae^{5-a/4})&\text{on edge }10.
\end{array}
\]
Integrating over the Parry measure and using \(w_{00}+w_{01}=\pi_0\) proves the formula. Since \(h\) is a smooth diffeomorphism on the compact repeller, its derivative contributes only a bounded coboundary, so this Lyapunov exponent agrees with that of \(f_{a,b}\). The identity \(b(1-b)=2b(1-2b)\) has the unique solution \(b=1/3\) within the parameter strip, proving the final simplification.

## Verification
The accompanying `VERIFY.py` checks a rational-series certificate for \(7<e^2<15/2\) and \(e^{20}>100000\), the endpoint-covering and derivative inequalities for 25 representative parameter pairs, the Parry weights, the exact \(b=1/3\) branch balance, and nine numerically recovered period-two branch itineraries against their analytical expansion. The script is **not** used to extrapolate finite tests to the continuous parameter strip. All global inequalities and asymptotics are proved above. Run `python3 VERIFY.py` with the standard library.

## Relationship to prior work
Kryzhevich, Zhang, and Chmara (arXiv:2412.16379, first posted 2024-12-20), Theorem 4.1 and Lemma 5.1, already establish a qualitative golden-mean repeller for every fixed \(b\ne1/2\) once \(a\) exceeds an unspecified threshold depending on \(b\). They also provide the logit conjugacy and an abstract inverse-branch construction. **Those facts are not claimed as new.** The new assertions here are an explicit *uniform* certified cutoff throughout a nontrivial closed interval of \(b\), a concrete choice of coding intervals with two-step expansion, and the uniform two-term Lyapunov law for the unique maximum-entropy measure, which the inspected source does not state. Kryzhevich and Zhang (arXiv:2603.20685) revisit the qualitative construction, without these evaluated bounds. Chotibut et al. (2021) study the original replicator family; Bielawski et al. (arXiv:2411.01495) instead focus on attracting rational-rotation-like periodic orbits. As usual, the numerical value of a safe sufficient threshold is not claimed to be intrinsic or sharp.

## Limitations
This is an **existence** and statistical-expansion statement for one explicitly coded repeller, not a classification of all invariant sets or of typical attracting dynamics. Neither exact optimality of \(a=100\) nor a full-space entropy equality is established. The error in the Lyapunov expansion is uniform only over \(b\in[1/4,2/5]\). The bound concerns positive exponents on this repeller, not every ergodic invariant measure of the full map. Historical-priority comparison is based on accessible material; general pre-existing thermodynamic formalism provides some proof tools but not the evaluated parameter-dependent law itself.

## References
1. S. Kryzhevich, Y. Zhang, M. Chmara, *Bifurcations and invariant sets for a family of replicator maps from evolutionary games*, arXiv:2412.16379v1, 2024-12-20. https://arxiv.org/abs/2412.16379
2. S. Kryzhevich, Y. Zhang, *Shift maps and statistical invariants for some dynamical systems*, arXiv:2603.20685v1, 2026-03-21. https://arxiv.org/abs/2603.20685
3. J. Bielawski, T. Chotibut, F. Falniowski, M. Misiurewicz, G. Piliouras, *Interval maps mimicking circle rotations*, arXiv:2411.01495v1, 2024-11-03. https://arxiv.org/abs/2411.01495
4. T. Chotibut, F. Falniowski, M. Misiurewicz, G. Piliouras, *Family of chaotic maps from game theory*, Dynamical Systems 36 (2021), 48–63. DOI:10.1080/14689367.2020.1795624.
