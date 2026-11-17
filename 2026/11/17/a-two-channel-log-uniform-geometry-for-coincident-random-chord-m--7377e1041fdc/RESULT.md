# A two-channel log-uniform geometry for coincident random chord midpoints

## Finding

Let \(U_1,U_2,U_3,U_4\) be four independent points uniform in angle on the unit circle, and let \(M_1=(U_1+U_2)/2\), \(M_2=(U_3+U_4)/2\) be the midpoints of two independent chords. Define \(E_\varepsilon=\{|M_1-M_2|<\varepsilon\}\) for \(0<\varepsilon<1\). Put \(r=|M_1|\), \(L_\varepsilon=\log(1/\varepsilon)\), and define the **mechanism label** \(K_\varepsilon=0\) if \(r\le1/2\), or \(K_\varepsilon=1\) otherwise. Let

\[
T_\varepsilon=\begin{cases}
\log(1/r)/L_\varepsilon,&K_\varepsilon=0,\\
\log(1/(1-r))/L_\varepsilon,&K_\varepsilon=1,
\end{cases}
\qquad \Phi_\varepsilon=\arg M_1,\qquad V_\varepsilon=(M_2-M_1)/\varepsilon.
\]

**Theorem (marked collision law).** Conditional on \(E_\varepsilon\), the joint law of \((K_\varepsilon,T_\varepsilon,\Phi_\varepsilon,V_\varepsilon)\) converges **in total variation** to the law of independent variables: a discrete mechanism \(K\) with \(\Pr(K=0)=2/3\) and \(\Pr(K=1)=1/3\); \(T\) uniform on \((0,1)\); \(\Phi\) uniform on \([0,2\pi)\); and \(V\) uniform by area in \(\{v\in\mathbb R^2:|v|<1\}\).

The center mechanism means both chords are almost diameters, with midpoint radius on a logarithmically uniform scale. The rim mechanism means both are very short chords, with endpoint-distance-to-rim on a logarithmically uniform scale. The sharp ratio of their rare-event weights is **two to one**. The known unmarked small-ball law is

\[
\Pr(E_\varepsilon)=\frac{3}{\pi^2}\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2).
\]

This unmarked formula follows from [1] and is **not claimed as new**. The marked law and its two independent singular mechanisms are the finding.

## Assumptions and scope

All four endpoints are mutually independent and have uniform **angular** distributions, rather than invariant-line or uniform-area-midpoint distributions. The circle has radius one; scaling gives the radius-\(R\) version by replacing \(\varepsilon\) with \(\varepsilon/R\). The event uses Euclidean midpoint distance, and \(\varepsilon\to0^+\). Exceptional cases \(r=0\), \(r=1\), and exact equality in the event have probability zero and do not affect the statement. The branch threshold \(1/2\) is arbitrary: every fixed threshold in \((0,1)\) gives the same limit.

## Proof

**1. Midpoint density.** Writing endpoints as \(e^{i\alpha},e^{i\beta}\), their midpoint equals \(e^{i(\alpha+\beta)/2}\cos((\alpha-\beta)/2)\). Its radius has density \(2/[\pi\sqrt{1-r^2}]\) on \((0,1)\), independently of its uniform angle. Hence its two-dimensional density with respect to planar area is

\[
f(x)=\frac{\mathbf 1_{\{0<|x|<1\}}}{\pi^2 |x|\sqrt{1-|x|^2}}.
\tag{1}
\]

The density is normalized since \(\int_0^1 2\pi r f(r)\,dr=1\). The singularities are \(f(r)\sim1/(\pi^2r)\) as \(r\downarrow0\), and \(f(r)\sim1/(\pi^2\sqrt{2(1-r)})\) as \(r\uparrow1\).

**2. Existing unmarked probability normalization.** By symmetry of unit-circle points,

\[
M_1-M_2\ \stackrel d=\ \frac12(U_1+U_2+U_3+U_4).
\]

Borwein–Straub–Wan–Zudilin [1], Example 4, compute the radius density \(p_4\) of the four-step uniform planar random walk and prove

\[
p_4(s)=\frac{3s}{2\pi^2}\log(1/s)+\frac{9\log 2}{2\pi^2}s+O(s^3\log(1/s))
\qquad(s\downarrow0).
\]

Therefore \(\Pr(E_\varepsilon)=\int_0^{2\varepsilon}p_4(s)\,ds\), so

\[
\Pr(E_\varepsilon)=\varepsilon^2\left[\frac{3}{\pi^2}\log(1/\varepsilon)+\frac{6\log2+3/2}{\pi^2}\right]+o(\varepsilon^2).
\tag{2}
\]

Formula (2), including its constant term, is a consequence of prior work and not part of the novelty claim. Only the leading coefficient is needed for the conditional theorem.

**3. Exact density of the marks.** For \(k=0\), change variables \(r=\varepsilon^t\); for \(k=1\), change variables \(r=1-\varepsilon^t\). In each case require the branch restriction (respectively \(r\le1/2\) or \(r>1/2\)). Under the event, \(v=(M_2-M_1)/\varepsilon\) has \(|v|<1\). Before conditioning, the joint density in coordinates \((k,t,\phi,v)\), with respect to counting measure, \(dt\,d\phi\,d^2v\), is exactly

\[
h_\varepsilon(k,t,\phi,v)=\mathbf 1_{\{|v|<1,\,\text{branch }k\}}\,\varepsilon^2 f(re^{i\phi})f(re^{i\phi}+\varepsilon v)r\left|\frac{dr}{dt}\right|.
\tag{3}
\]

For every fixed \(0<t<1\), angle \(\phi\), and interior \(|v|<1\), \(\varepsilon/r\to0\) in branch zero, and \(\varepsilon/(1-r)\to0\) in branch one. Equation (1) and the Jacobian \(|dr/dt|=L_\varepsilon r\) for branch zero or \(L_\varepsilon(1-r)\) for branch one give

\[
\lim_{\varepsilon\downarrow0}\frac{h_\varepsilon(0,t,\phi,v)}{\varepsilon^2 L_\varepsilon}=\frac1{\pi^4},\qquad
\lim_{\varepsilon\downarrow0}\frac{h_\varepsilon(1,t,\phi,v)}{\varepsilon^2 L_\varepsilon}=\frac1{2\pi^4}.
\tag{4}
\]

For fixed \(t>1\), both limits vanish: in branch zero \(r=o(\varepsilon)\), giving a factor \(r/\varepsilon\), and in branch one \(1-r=o(\varepsilon)\), giving a factor \(\sqrt{(1-r)/\varepsilon}\) whenever the shifted point remains in the disk. For fixed \(t<0\), neither branch restriction holds eventually. Hence (4) describes the a.e. limit on the entire mark space.

**4. Total variation by Scheffé.** Divide (3) by \(\Pr(E_\varepsilon)\). By (2), its pointwise a.e. limit is the probability density

\[
q(k,t,\phi,v)=\begin{cases}
\dfrac1{3\pi^2},& k=0,\ 0<t<1,\ 0\le\phi<2\pi,\ |v|<1,\\
\dfrac1{6\pi^2},& k=1,\ 0<t<1,\ 0\le\phi<2\pi,\ |v|<1,\\
0,&\text{otherwise}.
\end{cases}
\]

Indeed, integration over \(t\), angle and the unit disk gives \((2\pi)(\pi)[1/(3\pi^2)+1/(6\pi^2)]=1\). Each prelimit conditional density also integrates to one. Scheffé's lemma therefore yields \(L^1\) convergence, which is equivalent to total-variation convergence of the conditional laws. Factoring \(q\) gives exactly the independent limiting variables and weights stated above. \(\square\)

## Verification

The standalone Python checker implements independent Cartesian endpoint simulation, exact integration of the two squared-density singular bands, and pointwise convergence of the transformed marked density. Execute `python check.py` with NumPy installed. The printed diagnostics are `SQUARED_DENSITY_TWO_SINGULARITIES_OK`, `MARKED_DENSITY_LIMITS_OK`, and `NEAR_MIDPOINT_COLLISION_DIAGNOSTICS_OK`. The numerical procedure tests consequences of the proof, not convergence for all sufficiently small \(\varepsilon\); the analytical Scheffé argument is essential.

## Relationship to prior work

The classical Bertrand random-chord ambiguity explains why the endpoint-uniform midpoint density differs from the uniform-area-midpoint model [2]. Borwein et al. [1, Example 4 and Theorem 6] prove the four-step walk's complete near-zero unmarked radial density; (2) is their result after a simple scale change and integration. Crucially, this one-dimensional radial law does **not** identify which pairs of original chords are responsible for small differences. The conditional two-channel theorem supplies that information, including the two-to-one weight and independent logarithmic depth and transverse displacement marks. Nearby indexed work on polygon-chord midpoint laws and on chord crossings of nested circles [3,4] treats other supports or observables and does not directly imply the marked collision law. Full texts for those two indexed records were unavailable at review time, which limits priority confidence.

## Limitations

The theorem concerns *two* independently endpoint-uniform chords on a unit circle and their midpoints. It does not cover invariant-line sampling, noncircular boundaries, or collisions of more than two midpoints. No claim of priority over the four-step marginal walk density is made. The historical priority of the conditional mark decomposition remains provisional because non-indexed or inaccessible sources may contain equivalent descriptions. No independent audit has been performed.

## References

[1] J. M. Borwein, A. Straub, J. Wan, W. Zudilin, *Densities of short uniform random walks*, arXiv:1103.2995, first submitted 15 March 2011, *Canadian Journal of Mathematics* 64 (2012), 961–990, Example 4 and Theorem 6. https://arxiv.org/abs/1103.2995

[2] E. Pegg Jr, *Random Chord Paradox*, Wolfram Demonstrations Project, 2008. https://demonstrations.wolfram.com/RandomChordParadox/

[3] *Exact midpoint law and a parity singularity for random polygon chords*, published-finding corpus published research record, 25 October 2026, identified by suffix `83daec57c8af`.

[4] *A logarithmic collision cusp and complete monotonicity for nested-circle random chords*, published-finding corpus published research record, 1 November 2026, identified by suffix `21cbc7a7c0ae`.
