# A sharp arithmetic trichotomy for two-frequency sine equidistribution

## Finding
For every pair of distinct positive integers \(m<n\), put \(d=\gcd(m,n)\), \(r=m/d\), \(s=n/d\), and \(S=r+s\). For the unit circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), set
\[
\mathcal E_{m,n}=\sup_{\mu\in\mathcal P(\mathbb T)}\min\left\{\int\sin(mx)\,d\mu(x),\int\sin(nx)\,d\mu(x)\right\}.
\]
Then the sharp constant has the complete arithmetic classification
\[
\boxed{\mathcal E_{m,n}=c_S=\begin{cases}
\cos\dfrac{\pi}{2S},&S\text{ odd},\\[2pt]
\cos\dfrac{\pi}{S},&S\equiv0\pmod4,\\[2pt]
1,&S\equiv2\pmod4.
\end{cases}}
\]
The equivalent two-harmonic one-sided coefficient problem has the exact answer
\[
\sup\{a+b:a,b\in\mathbb R,\ a\sin(mx)+b\sin(nx)\le1\text{ for all }x\in\mathbb R\}=c_S^{-1}.
\]
For \(c_S<1\) its unique maximizing coefficient pair is
\[
\boxed{(a,b)=\frac{(s,r)}{S c_S}.}
\]
For \(c_S=1\), the maximizer is nonunique (every nonnegative pair \(a+b=1\) works); no assertion of a complete dual-coefficient classification is made in this degenerate case.

The **entire set of maximizing probability measures**, however, is classified in every case. Define
\[
T_{m,n}=\{x\pmod{2\pi}:\sin(mx)=\sin(nx)=c_S\}.
\]
Then a probability measure is maximizing if and only if it is supported on \(T_{m,n}\). This set consists of \(d\) points for \(S\not\equiv0\pmod4\), and of \(2d\) points for \(4\mid S\). Thus for coprime frequencies the optimizing measure is uniquely atomic except at the divisible-by-four resonance, where any mixture of two exact contact atoms is optimal.

Moreover let \(Q(x)=[s\sin(mx)+r\sin(nx)]/S\). The contact points are nondegenerate strict maxima, with
\[
c_S-Q(t+u)=\frac{mn c_S}{2}u^2+O_{m,n}(|u|^3)\qquad(t\in T_{m,n}).
\]
Consequently there exists \(K_{m,n}>0\) such that
\[
c_S-Q(x)\ge K_{m,n}\operatorname{dist}_{\mathbb T}(x,T_{m,n})^2
\]
for every \(x\), and any probability measure whose smaller sine expectation is at least \(c_S-\varepsilon\) satisfies
\[
\int\operatorname{dist}_{\mathbb T}(x,T_{m,n})^2\,d\mu(x)\le\varepsilon/K_{m,n}.
\]
The local quadratic coefficient is exact; an optimal global value of \(K_{m,n}\) is not asserted.

## Assumptions and scope
All frequencies are positive integers, distinct, with \(m<n\). Coefficients in the one-sided sine inequality are unrestricted real numbers; the extremal measures are all Borel probability measures on the full circle. There is no absolutely-continuous restriction. All angles use radians, and all trigonometric norms are unnormalized pointwise suprema. Common integer frequency factors act by the covering \(x\mapsto dx\), so the proof reduces to coprime frequencies \(r<s\).

## Proof
**1. Reduction.** The map \(x\mapsto dx\pmod{2\pi}\) is surjective and sends both Fourier frequencies to \(r,s\). Every probability measure on the reduced circle has a preimage probability measure. Both extremal values therefore depend only on coprime \(r,s\), and each reduced contact point has exactly \(d\) lifts. Prove the statements first for coprime \(m,n\), so \(S=m+n\).

**2. Every stationary value of the natural supporting sine.** Define
\[
F(x)=n\sin(mx)+m\sin(nx),\qquad F'(x)=mn[\cos(mx)+\cos(nx)].
\]
By the cosine product identity, all stationary points lie in the union of the two grids
\[
Sx=(2j+1)\pi\quad\text{or}\quad(n-m)x=(2j+1)\pi.
\]
At the first grid, \(\sin(nx)=\sin(mx)\), hence \(F(x)=S\sin(mx)\). At the second grid, \(\sin(nx)=-\sin(mx)\), hence \(F(x)=(n-m)\sin(mx)\). In particular every value on the second grid is at most \(n-m\).

**3. Exact maximum on the first grid.** Put \(x_j=(2j+1)\pi/S\) for \(0\le j<S\). The residues \(m(2j+1)\) modulo \(2S\) are all odd residues if \(S\) is even (then coprimality makes \(m\) odd). If \(S\) is odd, they are all odd residues for odd \(m\), or all even residues for even \(m\). Therefore the largest value of \(\sin(mx_j)\) is the sine of the permitted residue nearest to \(S/2\). For odd \(S\) that residue is at distance \(1/2\); for \(S\equiv0\pmod4\) there are exactly two nearest odd residues, at distance \(1\); for \(S\equiv2\pmod4\) the unique odd residue \(S/2\) occurs. These three cases give exactly \(c_S\) and one, two, or one contact points on the reduced circle, respectively.

The first-grid maximum \(S c_S\) strictly exceeds \(n-m\). Indeed \(S\ge3\), and for \(S=3\) the inequality follows from \(3\cos(\pi/6)>1\). For \(S\ge4\), \(c_S\ge\cos(\pi/S)\) and
\[
S(1-c_S)\le\frac{\pi^2}{2S}\le\frac{\pi^2}{8}<2\le2m=S-(n-m).
\]
Thus the second stationary grid cannot produce a global maximum. As a nonconstant smooth periodic function achieves its maximum at a stationary point, it follows that
\[
\boxed{F(x)\le S c_S\text{ for every real }x},
\]
with equality precisely when \(\sin(mx)=\sin(nx)=c_S\), namely on the finite contact set described above. In the noncoprime case the same conclusion follows by scaling back, with \(F(x)=s\sin(mx)+r\sin(nx)\).

**4. Primal and dual sharpness.** Divide the inequality just proved by \(S\) and integrate it against any probability measure. Because its left side is a convex combination of the two sine expectations, the smaller expectation cannot exceed \(c_S\). A point mass at any contact point makes both expectations equal \(c_S\), proving \(\mathcal E_{m,n}=c_S\).

Conversely, if a measure realizes the value \(c_S\), each sine expectation is at least \(c_S\) while their weighted average is at most \(c_S\). Equality must hold in the integrated supporting inequality, so the measure assigns full mass to its precise equality set \(T_{m,n}\). Every measure on this set conversely realizes equality, giving the complete extremal-measure classification.

For the coefficient problem, evaluating any candidate one-sided inequality at a contact point gives \((a+b)c_S\le1\). The explicit coefficients \((a,b)=(s,r)/(S c_S)\) attain this upper bound by the sharp supporting inequality, proving the exact dual optimum. If \(c_S<1\), at a contact point \(t\), \(\cos(mt)\ne0\) and \(\cos(nt)=-\cos(mt)\). Every optimal coefficient pair has equality at \(t\) and hence its derivative must vanish there, implying \(am=bn\). Along with \(a+b=c_S^{-1}\), this forces the stated unique coefficients. If \(c_S=1\), every nonnegative pair summing to one is feasible because each sine is at most one, proving nonuniqueness.

**5. Quantitative local sharpness.** For the normalized weighted supporting function \(Q=F/S\), differentiation gives \(Q''(t)=-mn c_S\) at each contact point, and all contact points are strict global maxima. Taylor's theorem yields the displayed quadratic coefficient. Compactness and strict positivity of the ratio \([c_S-Q(x)]/\operatorname{dist}(x,T_{m,n})^2\) away from contacts, together with its positive contact limits, give a positive global constant \(K_{m,n}\). Integrating this inequality and using \(\min\{\mathbb E\sin(mx),\mathbb E\sin(nx)\}\le\mathbb E Q\) proves the concentration estimate.

## Verification
The standalone `checker.py` independently enumerates all stationary grids, checks contact counts and values, tests the candidate one-sided inequality over an auxiliary mesh, and checks the predicted maximizer for 358 coprime pairs with frequencies through 34. Separately, sampled two-variable linear programming was compared with the formula on 12 representative pairs including large coprime frequencies. These are finite corroborations only; the proof above establishes the universal quantifiers and boundary cases.

## Relationship to prior work
Esser, Tao, Totaro and Wang solve a different, richer sine-inequality problem in which **all consecutive harmonics** \(1,\ldots,M\) are allowed and the sum of their coefficients is maximized. Their explicit formula groups complementary-frequency terms of the shape \((M+1-k)\sin(kx)+k\sin((M+1-k)x)\), which is a pertinent overlap in method and motivation. Their Theorem 2.1, as inspected, does not state the individually sharp two-frequency constant for every pair nor classify the extremal probability measures and unique sparse dual coefficients. The new theorem fixes exactly two frequencies instead of allowing the others, and the reduced-frequency arithmetic yields its three-class law.

Alzer and Kwong examine coefficient-weighted positivity inequalities for longer trigonometric sums on restricted angular intervals, rather than the global two-frequency one-sided minimax problem. Related Fourier coefficient optimization records concern Carathéodory–Fejér positivity, bounded-variation harmonic bodies, or two-character extrapolation rather than the present measure-minimax functional. These are distinctions of statements, not an assertion that matching keywords prove novelty.

## Limitations
No global *optimal* quantitative concentration constant \(K_{m,n}\) is identified, and the full set of dual coefficient maximizers in the degenerate class \(c_S=1\) is not classified. The result concerns only two sine harmonics on the full circle; no higher-dimensional or more-than-two-harmonic analogue is claimed. Historical-priority assessment is best-knowledge, not an independent literature audit: an older unindexed two-harmonic inequality may already contain the statement. The result has not been independently validated.

## References
1. L. Esser, T. Tao, B. Totaro and C. Wang, *Optimal sine and sawtooth inequalities*, arXiv:2107.11058, first public 23 July 2021, https://arxiv.org/abs/2107.11058 . Especially Theorem 2.1 and the proof in Section 2.
2. H. Alzer and M. K. Kwong, *Inequalities for trigonometric sums*, arXiv:2307.04464, first public 10 July 2023, https://arxiv.org/abs/2307.04464 . Especially the introduction and Theorems 1–6.
