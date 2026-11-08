# Sharp phase locking of Wigner-caustic cusps in the first two odd support harmonics

## Finding
Let \(a>0\), \(b\ge 0\), \(\phi\in\mathbb R/(2\pi\mathbb Z)\), and \(R>8a+24b\). Consider the strictly convex constant-width oval whose normal-angle support function is
\[
h(\theta)=R+a\cos(3\theta)+b\cos(5\theta+\phi).
\]
Its Wigner caustic is the midpoint locus of parallel-tangent pairs, with the natural parametrization by unoriented normal angle \(\theta\in\mathbb R/(\pi\mathbb Z)\). Put \(\lambda=3b/a\). The number of **ordinary cusp parameters**, away from the transition locus, is completely determined as follows.

* For \(0\le\lambda<3/5\), it is **three**, for every phase \(\phi\).
* For \(\lambda>1\), it is **five**, for every phase \(\phi\).
* For \(3/5<\lambda<1\), define
\[
s(\lambda)=\arccos\!\left(\frac54\sqrt{1-\lambda^2}\right),\qquad
\delta(\lambda)=\frac53s(\lambda)-\arctan\!\left(\frac53\tan s(\lambda)\right),
\]
so \(0<\delta(\lambda)<\pi/3\). Let \(d(\phi)=\min_{k\in\mathbb Z}|\phi-2k\pi/3|\) (on a real lift, hence \(0\le d(\phi)\le\pi/3\)). There are **five** ordinary cusp parameters when \(d(\phi)<\delta(\lambda)\), **three** when \(d(\phi)>\delta(\lambda)\), and exactly three ordinary cusp parameters plus one double-zero singular parameter when equality holds.

At \(\lambda=3/5\), there are three ordinary cusps unless \(\phi\equiv 2k\pi/3\), in which case there are **two ordinary** cusps and one triple-zero singular parameter. At \(\lambda=1\), there are five ordinary cusps unless \(\phi\equiv(2k+1)\pi/3\), in which case there are **three ordinary** cusps and one double-zero singular parameter. A zero of multiplicity \(m\in\{1,2,3\}\) of the speed factor yields locally a \((m+1,m+2)\)-type parametrized plane-curve singularity: respectively \((2,3)\), \((3,4)\), and \((4,5)\).

The area is \(A=\pi R^2-4\pi a^2-12\pi b^2\). Thus the fraction of the disk-area deficit contributed by the fifth harmonic is
\[
\eta=\frac{12b^2}{4a^2+12b^2}=\frac{\lambda^2}{3+\lambda^2}.
\]
In this complete two-harmonic class, **five ordinary Wigner cusps are possible for some phase if and only if \(\eta>3/28\)**; they occur for **every phase if and only if \(\eta>1/4\)**. At equality the exceptional phases have nonordinary singularities, as specified above.

## Assumptions and scope
A normal-angle support function \(h\) parametrizes an oval by \(\gamma(\theta)=h(\theta)n(\theta)+h'(\theta)t(\theta)\), where \(n(\theta)=(\cos\theta,\sin\theta)\) and \(t(\theta)=(-\sin\theta,\cos\theta)\). Its curvature radius is \(h+h''\). The condition \(R>8a+24b\) implies \(h+h''=R-8a\cos3\theta-24b\cos(5\theta+\phi)>0\), so the oval is smooth, strictly convex, and of width \(2R\). It is the **lowest two nontranslation odd Fourier-harmonic model** of a smooth constant-width oval: the first harmonic only translates, while the third and fifth encode its first two genuine shape modes. The claim concerns cusps of the normal-angle parametrization counted on the normalization \(\mathbb R/(\pi\mathbb Z)\); it does not assert the absence of self-intersections or of coincident image points.

## Proof
**1. From opposite tangents to a scalar zero equation.** Because the oval is strictly convex, all parallel-tangent pairs have normal angles \(\theta\) and \(\theta+\pi\). The Wigner midpoint map is
\[
W(\theta)=\frac12\bigl(\gamma(\theta)+\gamma(\theta+\pi)\bigr)
= f(\theta)n(\theta)+f'(\theta)t(\theta),\qquad
f(\theta)=a\cos3\theta+b\cos(5\theta+\phi).
\]
The equality \(W(\theta+\pi)=W(\theta)\) gives its natural \(\pi\)-periodic parametrization. Differentiating and using \(n'=t\), \(t'=-n\),
\[
W'(\theta)=(f+f'')t(\theta)=-8a\,q_{\lambda,\phi}(\theta)t(\theta),\quad
q_{\lambda,\phi}(\theta)=\cos3\theta+\lambda\cos(5\theta+\phi).
\]
Consequently its singular parameters are exactly zeros of \(q\) modulo \(\pi\). A simple zero gives a nondegenerate ordinary cusp, since at the zero the successive derivatives of \(W\) have nonzero determinant. More generally, if \(q\) vanishes to order \(m\), integration along the rotating tangent gives leading tangent and normal coordinates of orders \(m+1\) and \(m+2\), with nonzero coefficients.

**2. The only possible collisions.** A multiple zero must satisfy \(q=q'=0\), hence
\[
\cos(5\theta+\phi)=-\frac{\cos3\theta}{\lambda},\qquad
\sin(5\theta+\phi)=-\frac{3\sin3\theta}{5\lambda}.
\]
Squaring and adding gives the **necessary exact condition**
\[
\lambda^2=\cos^2 3\theta+\frac9{25}\sin^2 3\theta
=1-\frac{16}{25}\sin^2 3\theta.
\]
Thus no multiple zeros occur when \(\lambda<3/5\) or \(\lambda>1\). Root counts cannot change under a deformation without crossing a multiple zero. For \(\lambda=0\), \(q=\cos3\theta\) has three simple zeros modulo \(\pi\); for a pure fifth harmonic \(q=\cos(5\theta+\phi)\) there are five. Homotopy proves the two universal regimes.

**3. Exact intermediate phase boundaries.** Fix \(3/5<\lambda<1\), let \(s=s(\lambda)\in(0,\pi/2)\), and write \(\theta=\pi/2+x\). Then
\[
q=\sin3x-\lambda\sin(5x+\phi),\qquad q'=3\cos3x-5\lambda\cos(5x+\phi).
\]
At a multiple zero the scalar condition forces \(x=\pm s/3\) near \(\pi/2\). The two trigonometric equalities then force \(\phi=\mp\delta(\lambda)\) modulo \(2\pi\). Rotating \(\theta\) by \(2\pi/3\) leaves the third harmonic unchanged and shifts the fifth phase by \(\pm2\pi/3\); thus **all** multiple-zero phases are precisely
\[
\phi\equiv\frac{2k\pi}{3}\pm\delta(\lambda)\pmod {2\pi},\qquad k=0,1,2.
\]
The derivative of \(\delta\) with respect to \(s\) is positive:
\[
\frac{d\delta}{ds}=\frac53\frac{(16/9)\tan^2s}{1+(25/9)\tan^2s}>0,
\]
and its endpoint values are \(0\) and \(\pi/3\). Therefore the six boundary phases are distinct and divide phase space into alternating arcs. At \(\phi=0\), \(q=\cos3\theta+\lambda\cos5\theta\) equals \(\cos\theta\,P(\cos^2\theta)\), where
\[
P(u)=16\lambda u^2+(4-20\lambda)u+(5\lambda-3).
\]
For \(3/5<\lambda<1\), \(P(0)>0\), \(P(1/2)=-(1+\lambda)<0\), and \(P(1)=1+\lambda>0\). The two distinct roots in \((0,1)\) supply four zeros of \(q\) modulo \(\pi\), and the factor \(\cos\theta\) supplies the fifth. At \(\phi=\pi/3\) the count is three, since it equals three at \(\lambda<3/5\) and that phase cannot lie on a critical boundary before \(\lambda=1\). Local constancy between the six boundaries gives the claimed complete classification.

**4. Multiplicity at transitions.** At a multiple zero, the second derivative is
\[
q''=-9\cos3\theta-25\lambda\cos(5\theta+\phi)=16\cos3\theta.
\]
For \(3/5<\lambda\le1\), the critical double zeros have \(\cos3\theta\ne0\) (at \(\lambda=1\), it equals \(\pm1\)). At \(\lambda=3/5\), critical phases are \(2k\pi/3\), the critical zero has \(\cos3\theta=0\), and
\[
q'''=27\sin3\theta+125\lambda\sin(5\theta+\phi)=-48\sin3\theta\ne0.
\]
This proves the stated double and triple multiplicities and ordinary-cusp counts at the endpoints.

**5. Sharp area-energy cutoffs.** The support-area identity \(A=\frac12\int_0^{2\pi}(h^2-h'^2)\,d\theta\), and Fourier orthogonality, give \(A=\pi R^2-4\pi a^2-12\pi b^2\). Since \(\eta=\lambda^2/(3+\lambda^2)\) increases strictly with \(\lambda\ge0\), the exact phase regimes imply: existence of a phase with five *ordinary* cusps iff \(\lambda>3/5\), and five ordinary cusps for all phases iff \(\lambda>1\). These translate to \(\eta>3/28\) and \(\eta>1/4\), respectively. Scaling \(a,b\) down at fixed ratio and choosing sufficiently large \(R\) ensures that every spectral regime is realized by strictly convex ovals.

## Verification
The standalone standard-library script `verify.py` replays 1,386 off-boundary tests comparing a direct sign-change enumeration of \(q\)'s zeros with the stated phase diagram, numerically verifies the double-root identities on four intermediate amplitude slices and the exact energy thresholds, and checks the exceptional endpoints. It prints `TWO_MODE_WIGNER_CAUSTIC_PHASE_DIAGRAM_OK 1386` on success. Those finite tests support transcription and numerical consistency; the infinite claim rests on the analytic proof above, not on enumeration.

## Relationship to prior work
The classical cusp criterion, geometric definition of the Wigner caustic, and generic odd cusp-number bound are established in older literature, notably Domitrz and Zwierzyński (2016), and in the Fourier support-function treatment of Zwierzyński (2016). The latter gives the area formula and a general odd-harmonic representation of the caustic, but not the present amplitude–phase cusp-count classification or the two sharp fifth-mode energy cutoffs. The published two-mode result for support \(R+a\cos2\theta+b\sin5\theta\) has **five Wigner cusps regardless of its even-harmonic coefficient**, because even modes cancel from the midpoint map; that statement does not imply the 3-to-5 transition arising from the competition of two **odd** modes here. The 2014 affine-equidistant literature supplies general singularity criteria, not the displayed explicit phase boundaries. These works are acknowledged as ingredients and closest comparisons rather than claimed new here.

## Limitations
This is a complete cusp-parameter classification only in the two lowest genuine odd-harmonic **constant-width** support family. It does not classify general smooth ovals, curves with additional Fourier modes, centre-symmetry-set cusps, self-intersection topology, or geometric positions of cusp images. The strict-convexity condition is sufficient, not claimed optimal. Exceptional phases give nonordinary singularities and are expressly excluded from the phrase "five ordinary cusps." Search-based originality is provisional; independent historical and mathematical review is not performed.

## References
1. M. Zwierzyński, *The Constant Width Measure Set, the Spherical Measure Set and isoperimetric equalities for planar ovals*, arXiv:1605.02930v1, first public 2016-05-10, especially Sect. 2 and formulas (2.1)--(2.11).
2. W. Domitrz and M. Zwierzyński, *The geometry of the Wigner caustic and affine equidistants of planar curves*, arXiv:1605.05361v1, first public 2016-05-17, especially Sect. 2 and the convex-oval cusp criteria.
3. W. Domitrz and P. de M. Rios, *Singularities of equidistants and global centre symmetry sets of Lagrangian submanifolds*, Geometriae Dedicata 169 (2014), 361--382, DOI:10.1007/s10711-013-9861-2.
4. W. Domitrz and M. Zwierzyński, *The geometry of the Wigner caustic and a decomposition of a curve into parallel arcs*, Analysis and Mathematical Physics 12 (2022), article 7, DOI:10.1007/s13324-021-00617-x, first journal release 2021-11-16.
