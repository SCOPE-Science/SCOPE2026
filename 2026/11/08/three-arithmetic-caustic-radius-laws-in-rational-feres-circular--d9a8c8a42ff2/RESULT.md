# Three arithmetic caustic-radius laws in rational Feres circular billiards

## Finding

In the unit circular billiard with the Feres triangular random-reflection law, fix an integer \(n\ge 7\) and the base angle \(\alpha=\pi/n\). Start with normalized Liouville distribution for the boundary position and outgoing angle and then evolve according to the Feres probabilities. For any trajectory let \(R\) be the radius of the largest concentric disk missed by every straight flight segment, equivalently the minimum nonnegative tangent-circle radius \(\lvert\cos\phi\rvert\) among its encountered outgoing angles \(\phi\). The random variable \(R\) is well defined almost surely, is constant under shifting the path, and has the following *complete* distribution.

Put \(a=\pi/n\). For \(0\le r\le\sin(a/2)\) when \(n\) is odd, or \(0\le r\le\sin a\) when \(n\) is even, its cumulative distribution function is

\[
\mathbb P(R\le r)=
\begin{cases}
 r/\sin(a/2),&n\text{ odd},\\[2pt]
 r/\sin a,&n\equiv2\pmod 4,\\[2pt]
 r\cot a+1-\sqrt{1-r^2},&n\equiv0\pmod4.
\end{cases}
\]

Outside the indicated supports, the cumulative distribution function is zero below the support and one above it. Thus \(R\) is exactly uniform in two of the three congruence classes; for \(n\equiv0\pmod4\) its density is \(\cot a+r/\sqrt{1-r^2}\) on \((0,\sin a)\). The first two moments are

\[
(\mathbb ER,\mathbb ER^2)=
\begin{cases}
(\tfrac12\sin(a/2),\tfrac13\sin^2(a/2)),&n\text{ odd},\\[2pt]
(\tfrac12\sin a,\tfrac13\sin^2 a),&n\equiv2\pmod4,\\[2pt]
(a/2,\tfrac23(1-\cos a)),&n\equiv0\pmod4.
\end{cases}
\]

In particular, the expected area of the excluded central disk is exactly \(\pi\mathbb E R^2\). The essential supremum of the radius is \(\sin(\pi/(2n))\) for odd \(n\), versus \(\sin(\pi/n)\) for even \(n\): an arithmetic factor-two difference in the large-\(n\) essential maximal radius.

## Assumptions and scope

Write the unit-circle collision state as \((s,\theta)\in[0,2\pi)\times(0,\pi)\), where \(s\) is the boundary position and \(\theta\) the outgoing angle with the oriented tangent. The deterministic circular step is \((s,\theta)\mapsto(s+2\theta\bmod2\pi,\theta)\). At each collision the Feres law selects one of the angular transformations

\[
T_1(\theta)=\theta+2a,\quad T_2(\theta)=-\theta+2\pi-4a,\quad
T_3(\theta)=\theta-2a,\quad T_4(\theta)=-\theta+4a
\]

with the state-dependent probabilities of Vales and Pinto-de-Carvalho [1, Section 3.1]. Only branches with strictly positive probability are admissible. Invariant normalized Liouville measure [1, Proposition 4.5] is

\[
\frac{ds}{2\pi}\,\frac{\sin\theta}{2}\,d\theta.
\]

A flight chord leaving at angle \(\theta\) is tangent to a centered circle of *nonnegative Euclidean radius* \(\lvert\cos\theta\rvert\); the absolute value removes the irrelevant signed-radius convention. The minimum of these radii over an infinite trajectory gives the radius of the largest concentric disk avoided by all its chords. The definition is almost-sure and concerns the complete infinite trajectory, not a finite list of collisions. Angles on the finite set of branch boundaries are immaterial to the continuous initial law.

## Proof

**1. The accessible angle class.** Fix \(0<t<a\). Since every angular branch is a sign change followed by an even multiple of \(a\), all positive-probability images of \(t\) lie in the following set:

\[
\mathcal C_t=
\begin{cases}
\{t+2ka:0\le k\le m\}\cup\{2ka-t:1\le k\le m\},&n=2m+1,\\[2pt]
\{t+2ka:0\le k\le m-1\}\cup\{2ka-t:1\le k\le m\},&n=2m.
\end{cases}
\]

This set has exactly \(n\) members in \((0,\pi)\). They are all reachable, not merely algebraically possible: successive \(T_1\)-branches reach the displayed positive-\(t\) ladder; after the first \(T_1\) step the branch \(T_4(t+2a)=2a-t\) reaches the other ladder, and repeated \(T_1\) steps reach its remaining members. Every step of these ladders has positive probability. Specifically, \(p_1(x)>0\) whenever \(0<x<\pi-2a\), and the required bridge has the strictly positive weight

\[
p_4(t+2a)=\frac{\sin(a-t)}{2\cos a\sin(t+2a)}>0.
\]

The inverse of a positive \(T_1\)-transition is a positive \(T_3\)-transition; the \(T_2,T_4\) moves are involutive on their positive-probability domains [1, Remark 1]. Therefore the resulting finite angular Markov chain is irreducible. It visits every member of \(\mathcal C_t\) infinitely often almost surely, even when the chain is periodic. Consequently

\[
R(t)=\min_{\phi\in\mathcal C_t}|\cos\phi|.
\]

Each of the \(n\) expressions \(t+2ka\) and \(2ka-t\), as \(t\) ranges over \((0,a)\), sweeps exactly one of the \(n\) disjoint intervals \((ja,(j+1)a)\), \(0\le j<n\). Thus almost every initial angle \(\theta\in(0,\pi)\) lies in a unique class \(\mathcal C_t\), and the representative \(t\in(0,a)\) is unique.

**2. The geometric nearest-angle calculation.** The closest angular point to \(\pi/2\) is obtained directly from the two interlaced ladders. For odd \(n\), one of the ladders has the point \(\pi/2+(t-a/2)\) or \(\pi/2+(a/2-t)\), and all other points are farther away. For \(n\equiv2\pmod4\), the closest points flank \(\pi/2\) at distance \(a-t\). For \(n\equiv0\pmod4\), the closest points flank \(\pi/2\) at distance \(t\). As the distances lie in \([0,\pi/2)\), the minimum unsigned chord offset is

\[
R(t)=
\begin{cases}
\sin|t-a/2|,&n\text{ odd},\\[2pt]
\sin(a-t),&n\equiv2\pmod4,\\[2pt]
\sin t,&n\equiv0\pmod4.
\end{cases}
\]

**3. Pushforward of stationary Liouville measure.** The joint stationary angular density is \(\tfrac12\sin\theta\); the angular Markov chain never leaves its class. Hence the representative \(t\) has density \(w_n(t)=\tfrac12\sum_{\phi\in\mathcal C_t}\sin\phi\). Finite trigonometric sums give the exact normalized densities

\[
w_n(t)=
\begin{cases}
\displaystyle\frac{\cos(t-a/2)}{2\sin(a/2)},&n\text{ odd},\\[7pt]
\displaystyle\frac{\cos(t-a)}{\sin a},&n\text{ even},
\end{cases}\quad 0<t<a.
\]

Indeed, writing \(n=2m+1\) gives \(\sum_{k=1}^{m}\sin(2ka)=\tfrac12\cot(a/2)\), while for \(n=2m\) the analogous sum up to \(m-1\) is \(\cot a\). Each density integrates to one over \((0,a)\).

If \(n\) is odd, the two inverse branches of \(r=\sin|t-a/2|\) have combined Jacobian-weight \(1/\sin(a/2)\), proving the uniform distribution. If \(n\equiv2\pmod4\), putting \(u=a-t\) makes the density proportional to \(\cos u\,du\), and \(r=\sin u\) is uniform on \((0,\sin a)\). Finally, for \(n\equiv0\pmod4\), the change \(r=\sin t\) produces

\[
\frac{w_n(\arcsin r)}{\sqrt{1-r^2}}
=\cot a+\frac{r}{\sqrt{1-r^2}}.
\]

Integration gives the stated piecewise cumulative law. For the moments, use the uniform laws in the first two cases; in the third, direct integration yields \(\mathbb ER=a/2\) and \(\mathbb ER^2=2(1-\cos a)/3\). Multiplying the second moment by \(\pi\) gives the excluded-disk area mean. All boundary cases have zero initial measure.

## Verification

The independent, standard-library checker `check_caustic.py` constructs all \(n\) accessible angles explicitly and compares the direct minimum of \(|\cos\phi|\) with the proposed representative formulas. It also checks the exact orbit-sine sums, the Liouville normalization, the cumulative distributions at internal radii, and the two moment formulas by high-resolution numerical quadrature for every integer \(7\le n\le50\). Its run reported 14,036 successful direct comparison cases, 44 normalization integrals, and 88 moment integrals. The checks include all three residue classes modulo four; they are finite corroboration, not an all-parameter proof. The proof above is the infinite statement.

Run with `python3 check_caustic.py` using only the Python standard library.

## Relationship to prior work

Vales and Pinto-de-Carvalho [1] define the Feres circular random billiard, its positive-probability angular branches, Liouville invariance, finite angular classes for rational \(a/\pi\), and the qualitative concept of a random caustic. They do **not** give the Liouville-distributed caustic-radius law, its congruence-class trichotomy, or the expected excluded-disk area. Vales [2] develops the same angular equivalence classes on constant-curvature surfaces and gives the explicit examples \(n=7,8\), but does not compute these statistical quantities. The finite Markov-class geometry and invariant measure are therefore inherited, whereas the global class-weight pushforward and the full exact law above are additional calculations. General billiard and random-map theory [3] is background, not a claim of novelty for the underlying transition mechanism.

## Limitations

The theorem is restricted to rational triangular roughness angles of the form \(a=\pi/n\) with integer \(n\ge7\), to the unit Euclidean disk, and to Liouville-distributed initial angles. It does not assert the same law for arbitrary rational numerators, irrational roughness angles, other table shapes, or nonstationary initial distributions. It does not give a finite-time law for the first visit to the closest-angle state, or a uniform mixing rate. The physical radius is nonnegative, despite the signed cosine convention sometimes used for oriented angle parametrization. The stationary distribution is not an assertion of parameter identifiability under finite observations. Other unindexed equivalent formulations could exist; independent expert assessment has not been performed.

## References

[1] T. Vales and S. Pinto-de-Carvalho, *A Random Billiard Map in the Circle*, arXiv:2005.01892 (first public submission 2020-05-05), especially Sections 3.1, 4.1, 5, and 6.3. https://arxiv.org/abs/2005.01892

[2] T. Vales, *Random circular billiards on surfaces of constant curvature: Pseudo integrability and mixing*, arXiv:2212.00872 (first public submission 2022-12-01), especially Sections 3, 4, and 6. https://arxiv.org/abs/2212.00872

[3] R. Feres, *Random Walks Derived from Billiards*, in *Dynamics, Ergodic Theory, and Geometry* (2007), pp. 179–222, DOI:10.1017/CBO9780511755187.008. The framework predates [1] and does not by itself provide the circle-specific caustic-radius distribution.
