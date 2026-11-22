# Exact zero counts and repeated positivity failures for exact-start BDF2 graph heat flow

## Finding

For each integer \(k\ge 2\), let \(g_k\) denote the scalar response of standard constant-step BDF2 to \(u'=-\lambda u\), started with **one exact heat step**, as a function of \(z=h\lambda\):
\[
g_0(z)=1,\quad g_1(z)=e^{-z},\qquad
(3+2z)g_k(z)=4g_{k-1}(z)-g_{k-2}(z)\quad(k\ge2).
\]
Then \(g_k\) has **exactly \(\lfloor k/2\rfloor\) distinct, simple zeros in \((0,\infty)\)**. It is positive from zero to its first root, changes sign at every root, and consequently has exactly
\[
\left\lceil\frac{\lfloor k/2\rfloor}{2}\right\rceil
\]
connected intervals of strictly negative \(z>0\). These intervals include a positive-half-line tail precisely when \(\lfloor k/2\rfloor\) is odd.

For each such \(k\) there exists a finite unweighted star \(K_{1,n-1}\) such that constant-step BDF2 for graph heat flow, with exact first-step startup, assigns **negative hub self-return in at least that many pairwise disjoint bounded open timestep intervals**. Thus the number of separated losses and recoveries of nonnegative graph-heat transfer under this fixed classical multistep method is unbounded as the stage index grows.

At the second BDF2 level \(k=2\), a further sharp graph-order statement holds: **all diagonal self-transitions stay strictly positive for every connected positively weighted undirected graph with at most twelve vertices and every positive step**, whereas the thirteen-vertex unweighted star has a negative hub self-transition. This is a diagonal statement, not a universal claim of full entrywise nonnegativity.

## Assumptions and scope

For scalar decay, \(\lambda>0\), step size \(h>0\), and \(z=h\lambda\). The exact starter is \(g_1=e^{-z}\), not backward Euler. For a finite connected undirected graph with \(n\ge2\) vertices, each present edge has a positive conductance, and the combinatorial Laplacian is \(L_{ii}=\sum_{j\ne i}w_{ij}\), \(L_{ij}=-w_{ij}\) for \(i\ne j\). For arbitrary nonnegative initial column vector \(u_0\), the exact-start BDF2 iterations are
\[
u_1=e^{-hL}u_0,\qquad (3I+2hL)u_k=4u_{k-1}-u_{k-2}\quad(k\ge2),
\]
so \(u_k=g_k(hL)u_0\). Each iterate preserves total mass because \(g_k(0)=1\); this need not preserve pointwise nonnegativity. For the star assertion choose \(u_0=e_c\) at its center \(c\), and vary the same constant timestep \(h\) for all steps of a fixed trajectory index \(k\). A negative self-return is one negative entry of the completed transfer matrix; it does not assert instability or a negative exact heat kernel.

## Proof

**1. Positive region and characteristic roots.** The characteristic polynomial of the scalar recurrence is
\[
(3+2z)r^2-4r+1=0.
\]
For \(0<z<1/2\), put \(s=\sqrt{1-2z}\), so the distinct positive roots are \(r_+=1/(2-s)\) and \(r_-=1/(2+s)\). Solving for the initial values gives
\[
g_k(z)=r_-^k+(e^{-z}-r_-)\frac{r_+^k-r_-^k}{r_+-r_-}>0.
\]
Indeed \(r_-\le1/2<e^{-z}\), and \(r_+>r_->0\). At \(z=1/2\), the repeated root \(1/2\) yields
\[
g_k(1/2)=2^{-k}\bigl[1+k(2e^{-1/2}-1)\bigr]>0.
\]
Thus all positive zeros lie strictly above \(1/2\).

**2. Exact oscillatory phase.** For \(z>1/2\) write
\[
a=3+2z,\quad b=2z-1,\quad \rho=a^{-1/2},\quad
\theta=\arccos(2/\sqrt a)\in(0,\pi/2),
\]
\[
B=\frac{a e^{-z}-2}{\sqrt b},\qquad \phi=\arctan B\in(-\pi/2,\pi/2).
\]
The two characteristic roots are \(\rho e^{\pm i\theta}\). Matching the initial conditions gives the **identity**
\[
g_k(z)=\rho^k\bigl[\cos(k\theta)+B\sin(k\theta)\bigr]
=\rho^k\sqrt{1+B^2}\cos F_k(z),\qquad F_k(z)=k\theta(z)-\phi(z).
\]
The amplitude never vanishes.

**3. Strict phase monotonicity.** Direct differentiation, using \(a=3+2z\) and \(b=2z-1\), gives
\[
\theta'(z)=\frac{2}{a\sqrt b},\quad
\phi'(z)=\frac{2-(4z^2+2z+2)e^{-z}}
{\sqrt b\,[b+(ae^{-z}-2)^2]}.
\]
The key cancellation is
\[
\theta'(z)-\phi'(z)
=\frac{2e^{-z}a\bigl(e^{-z}+z-1\bigr)}
{\sqrt b\,[b+(ae^{-z}-2)^2]}>0,
\]
since \(e^{-z}>1-z\) for every \(z>0\). Therefore
\[
F_k'(z)=(k-1)\theta'(z)+(\theta'(z)-\phi'(z))>0
\quad(k\ge1,z>1/2).
\]
Moreover \(ae^{-z}-2\to4e^{-1/2}-2>0\) as \(z\downarrow1/2\), while \(b\to0\), so \(F_k(z)\to-\pi/2\). As \(z\to\infty\), \(\theta\to\pi/2\) and \(B\to0^-\), whence \(F_k(z)\to k\pi/2\). Thus \(F_k\) continuously and strictly maps \((1/2,\infty)\) onto \((-\pi/2,k\pi/2)\).

**4. Exact zero and sign enumeration.** The zeros of the cosine inside that open phase interval are exactly
\[
F_k(z_j)=\bigl(j+\tfrac12\bigr)\pi,
\qquad j=0,1,\ldots,\lfloor k/2\rfloor-1.
\]
Each target has exactly one solution by the strict monotonicity and endpoint limits. Differentiating the cosine representation shows every root is simple because the prefactor and \(F_k'\) are strictly positive. Since \(g_k(0)=1\) and there are no lower roots, the signs alternate. The number of negative components is exactly the displayed ceiling. No finite root occurs at the limiting phase endpoint \(k\pi/2\).

**5. Graph heat and arbitrarily many disjoint negativity windows.** For an unweighted star \(K_{1,n-1}\), the center basis vector has spectral mass \(1/n\) on the constant eigenvalue and \((n-1)/n\) on eigenvalue \(n\); all other spectral components vanish at the center. Hence, with \(u_0=e_c\),
\[
(u_k)_c=\bigl[g_k(hL)\bigr]_{cc}
=\frac{1+(n-1)g_k(nh)}{n}.
\]
Choose one finite sample point \(z_j\) strictly inside each scalar negative interval and let \(\delta=\min_j[-g_k(z_j)]>0\). Any integer \(n>1+1/\delta\) makes the hub value negative at every \(h_j=z_j/n\). At the separating scalar zeros it equals \(1/n>0\), so these negativity neighborhoods are pairwise separated. For sufficiently small and sufficiently large \(h\), the hub value is positive, because \(g_k(0)=1\) and \(\lim_{z\to\infty}g_k(z)=0\) for fixed \(k\ge2\). Thus at least the stated number of **bounded and disjoint** negative-timestep intervals exist. Since the ceiling grows without bound with \(k\), there is no fixed finite upper bound on the number of separated negativity windows over all stage indices and graph sizes.

**6. Sharp second-stage diagonal threshold.** At \(k=2\),
\[
g_2(z)=\frac{4e^{-z}-1}{3+2z},\qquad
g_2'(z)=\frac{2-4(5+2z)e^{-z}}{(3+2z)^2}.
\]
The derivative has exactly one zero \(z_*\) on \([0,\infty)\), determined by \(e^{z_*}=10+4z_*\). Indeed \(e^z-(10+4z)\) is initially negative, decreases until \(z=\log4\), then increases strictly to infinity. The elementary bounds \(e^3<22\) and \(e^{7/2}>24\) (from truncated exponential series and a geometric tail bound) give \(3<z_*<7/2\). Consequently the unique global minimum is
\[
m_*=g_2(z_*)=-\frac{1}{5+2z_*},
\qquad -\frac1{11}<m_*<-\frac1{12}.
\]
For a connected symmetric \(n\)-vertex Laplacian, the constant normalized eigenvector has squared mass \(1/n\) at every vertex. Spectral decomposition gives, for any \(h>0\),
\[
[g_2(hL)]_{ii}\ge\frac{1+(n-1)m_*}{n}.
\]
This is strictly positive for \(n\le12\). On the thirteen-vertex unit-conductance star, the center spectral measure is supported at \(0\) and \(13\); taking \(h=3/13\) yields
\[
[g_2(hL)]_{cc}=\frac{16e^{-3}-1}{39}<0,
\]
since \(e^3>1+3+9/2+27/6+81/24>16\). Hence the twelve/thirteen-vertex threshold is sharp. More generally, the spectral lower bound is attained at a given vertex precisely when that vertex has equal positive conductance to every other vertex, at the scale \(h=z_*/(nw)\); arbitrary additional edges among its neighbors do not change this equality.

## Verification

The standalone `verify.py` uses SymPy for exact algebraic identities and Python's standard numerical library for supplementary recurrence and phase evaluations. Replaying it checks the central positive derivative numerator, the second-stage minimizing identity, a rational star identity, hundreds of exact rational recurrences, oscillatory phase/recurrence agreement, numerically bracketed root counts through index \(26\), and separated negative star-return samples. Its output is recorded in `VERIFICATION.md`. Numerical root bracketing is **not** the proof of the infinite all-stage zero count; that proof is the analytic phase monotonicity in Steps 2–4.

## Relationship to prior work

Classical BDF2 and the need for a suitable starting procedure are established. Hundsdorfer (1998) studies positivity of implicit/explicit BDF2 blends and proves conditional positivity for linear systems; Hundsdorfer, Ruuth, and Spiteri (2002) study monotonicity-preserving multistep methods and the role of starting methods. Neither inspected full text states an all-stage exact count of zeros as **timestep varies with exact first-step startup**, or arbitrarily many disconnected negative hub-return bands on finite stars.

A separate public research record, *Exact delayed sign loss just beyond BDF2's positivity boundary* (2026), obtains a first-negative **iteration index as a function of fixed timestep** for **backward-Euler startup**; its phase has a different initial coefficient. This is not the exact-start root-count theorem at each fixed index, nor the graph-star reentry consequence. A public Richardson-backward-Euler diffusion result derives a sharp dimension barrier for a different one-step scalar transfer map. TR-BDF2 is a composite one-step scheme and is not the classical two-step recurrence considered here. General positivity radii and scalar characteristic-root formulas alone do not imply the strict phase-difference inequality or the count of all timestep sign bands established above.

## Limitations

The scalar zero classification assumes constant steps, scalar real nonnegative decay and **exact exponential startup**, not backward-Euler or variable-step startup. The graph examples are connected symmetric unnormalized heat Laplacians; no corresponding general claim is made for directed generators, nonlinear problems, or other starters. The universal small-order cutoff concerns **diagonal transfer entries at stage two only**, not all entries or later stages. The construction establishes **at least** the stated number of finite-star negative bands; it does not classify every root of the shifted star response or find the smallest star needed at each stage. Numerical checks cannot certify all stages. A complete literature priority guarantee is impossible, especially for older multistep oscillation literature using different terminology. Independent mathematical validation has not been performed.

## References

1. W. Hundsdorfer, *Partially Implicit BDF2 Blends for Convection Dominated Flows*, CWI report MAS-R9831, December 1998. Full text: https://ir.cwi.nl/pub/4596/04596D.pdf .
2. W. Hundsdorfer, S. J. Ruuth, and R. J. Spiteri, *Monotonicity-Preserving Linear Multistep Methods*, CWI report MAS-R0210, April 30, 2002, later SIAM J. Numer. Anal. 41 (2003). Full text: https://ir.cwi.nl/pub/4231/04231D.pdf .
3. L. Bonaventura and A. Della Rocca, *Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions*, preprint October 14, 2015, https://arxiv.org/abs/1510.04303 .
4. *Exact delayed sign loss just beyond BDF2's positivity boundary*, public mathematical research record (2026): https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-delayed-sign-loss-just-beyond-bdf2-s-positivity-boundary--cf66315c5a14 .
5. *The sharp 28–29 self-transition barrier for Richardson-accelerated graph diffusion*, public mathematical research record (2026): https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-sharp-28-29-self-transition-barrier-for-richardson-accelerat--56edd79ad0f3 .
