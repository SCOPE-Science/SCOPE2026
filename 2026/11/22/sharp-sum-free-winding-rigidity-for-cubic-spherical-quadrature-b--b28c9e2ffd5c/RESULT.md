# Sharp sum-free winding rigidity for cubic spherical quadrature by one-phase Fourier curves

## Finding
For every integer \(d\ge3\), let \(r_j>0\), \(\sum_{j=1}^d r_j^2=1\), \(w_j\in\mathbb Z\), and \(\gcd(|w_1|,\ldots,|w_d|)=1\). Consider the one-parameter diagonal torus orbit on the unit sphere in \(\mathbb C^d\cong\mathbb R^{2d}\):
\[
\gamma(t)=(r_1e^{i(w_1t+\phi_1)},\ldots,r_de^{i(w_dt+\phi_d)}),\quad 0\le t<2\pi.
\]
Its normalized arclength measure is a spherical \(3\)-design if and only if
\[
r_1=\cdots=r_d=\frac1{\sqrt d},\qquad w_j\ne0,\quad |w_j|\ne|w_k|\ (j\ne k),
\]
and the set of positive absolute winding numbers \(A=\{|w_1|,\ldots,|w_d|\}\) is **sum-free with repetitions**, meaning
\[
a+b\notin A\quad\text{for all }a,b\in A,\text{ including }a=b.
\]
Every such curve has arclength at least
\[
\boxed{\ell(\gamma)\ge 2\pi\sqrt{\frac{4d^2-1}{3}}.}
\]
Equality holds precisely when \(\{|w_1|,\ldots,|w_d|\}=\{1,3,\ldots,2d-1\}\), allowing permutation, independent frequency-sign changes, and arbitrary starting phases. In particular the previously known symmetric moment curve is the **unique minimal winding spectrum within this natural diagonal-orbit class**, and the classification includes all other primitive constant-modulus one-phase designs. No such curve is a spherical \(4\)-design.

## Assumptions and scope
A spherical \(q\)-design curve here means a smooth closed embedded curve whose **normalized arclength** reproduces the normalized rotation-invariant probability measure of \(S^{2d-1}\) on restrictions of all real polynomials of total degree at most \(q\). Its parameter \(t\) is angular and covers the curve exactly once: primitivity of the integer winding vector ensures this, because every radius is positive. Nonzero winding is a consequence of the design condition, rather than an initial hypothesis. Arbitrary initial phases are permitted. The theorem optimizes **only the indicated constant-coordinate-modulus, single-frequency-per-complex-coordinate, one-parameter torus orbit class**; it does not prove global minimality among all spherical design curves. The theorem is given for \(d\ge3\), although the elementary argument also works for \(d=2\), where related curves were known.

## Proof
**1. Reduction to circle Fourier moments.** The derivative of \(\gamma\) has constant squared speed \(v^2=\sum_jr_j^2w_j^2\). The primitive condition implies that the closed curve is traversed exactly once on \([0,2\pi)\): if \(\gamma(s)=\gamma(t)\), then \(w_j(s-t)\in2\pi\mathbb Z\) for every \(j\), and Bézout's identity gives \(s-t\in2\pi\mathbb Z\). Provided the speed is positive, normalized arclength is therefore uniform \(dt/(2\pi)\). For complex monomials
\[
M_{\alpha,\beta}(z)=\prod_{j=1}^dz_j^{\alpha_j}\overline z_j^{\beta_j},
\qquad |\alpha|+|\beta|\le3,
\]
the curve's normalized integral equals
\[
\left(\prod_jr_j^{\alpha_j+\beta_j}e^{i(\alpha_j-\beta_j)\phi_j}\right)
\mathbf1_{\{\sum_j(\alpha_j-\beta_j)w_j=0\}}.
\]
These monomials span the complexification of the real polynomial space through degree three.

**2. Exact spherical target moments.** The normalized unit sphere distribution is invariant under independent rotations of the \(d\) complex coordinates. Thus the sphere average of every nonconstant monomial of total degree at most three is zero except \(z_j\overline z_j\), whose average is \(1/d\); the constant has average one. In particular, the degree-one moments force all \(w_j\ne0\). The degree-two diagonal moments force \(r_j^2=1/d\) for all \(j\). For distinct \(j,k\), the moments \(z_j\overline z_k\) and \(z_jz_k\) must vanish, ruling out \(w_j=w_k\) and \(w_j=-w_k\). Hence all absolute windings are distinct.

**3. Cubic resonance.** With nonzero, pairwise-distinct absolute windings, an undesired nonzero cubic moment exists if and only if some three signed windings sum to zero, repetitions of indices allowed. For any positive absolute values \(a,b,c\), an equation \(\pm a\pm b\pm c=0\) is equivalent, after moving the unique term with opposite sign, to \(a+b=c\) in some ordering. Conversely an equality \(a+b=c\), including \(a=b\), gives a cubic monomial using the appropriate coordinates or conjugates whose Fourier frequency is zero and whose amplitude is strictly positive. Its spherical mean is zero because total degree is odd. Therefore cubic exactness holds exactly when \(A\) is sum-free (with repetitions), proving both necessity and sufficiency at degree three.

**4. Sharp extremum and equality.** Order the positive windings \(1\le a_1<\cdots<a_d\). Every prefix \(\{a_1,\ldots,a_j\}\) is sum-free. Put \(m=a_j\). The reflection \(x\mapsto m-x\) partitions the integers \(1,\ldots,m-1\) into \(\lfloor(m-1)/2\rfloor\) pairs and possibly a fixed middle integer if \(m\) is even. From each reflection pair at most one value can belong to the prefix, because two values totaling \(m\) contradict sum-freeness; the middle value \(m/2\), when present, is itself excluded since repetition is allowed. Consequently \(j-1\le\lfloor(m-1)/2\rfloor\), so \(a_j\ge2j-1\). It follows that
\[
\ell(\gamma)^2=\frac{4\pi^2}{d}\sum_{j=1}^da_j^2
\ge\frac{4\pi^2}{d}\sum_{j=1}^d(2j-1)^2
=\frac{4\pi^2}{3}(4d^2-1).
\]
The odd integers are sum-free, since any sum of two odd integers is even. Equality in the sum of squares is possible if and only if \(a_j=2j-1\) for every \(j\), proving both sharpness and rigidity within the class. The primitive condition is automatic for the equality set because it contains one.

**5. Exclusion of strength four.** Degree four would require exactness of \(|z_j|^4\). Along any degree-three design orbit the value is \(1/d^2\), while under normalized sphere measure it is \(2/[d(d+1)]\), by the standard complex-sphere fourth moment (also obtained from two-dimensional Dirichlet/Gaussian normalization). For \(d>1\) these values disagree; thus no member of the class has strength four.

## Verification
The standalone `CHECK.py` enumerates every signed primitive integer winding vector in \(d=3,4\) with coordinate magnitudes at most seven. For each, all complex monomials of degrees one through three are checked symbolically through their exact integer Fourier frequencies, and the result is compared with the distinct-absolute-value sum-free criterion. It independently enumerates sum-free subsets of \(\{1,\ldots,16\}\) with up to five elements and verifies the sharp termwise and squared-norm bounds. The finite checks are regression tests **only**: the proof in sections 1–5 supplies the all-dimensional result. Run `python3 CHECK.py` with Python 3 (standard library only).

## Relationship to prior work
Ehler and Gröchenig [1] introduced exact spherical design curves in 2023 (arXiv version 1 publicly posted June 19, 2023) and gave constructions and a general existence theorem. King and Mixon [2], first posted July 16, 2026, explicitly state the symmetric moment curve with windings \(1,3,\ldots,2d-1\) as a known spherical \(3\)-design and conjecture its **global** length-minimality on odd spheres (Conjecture 17, 2026 version inspected). Thus the existence, exactness, and putative global optimality of that particular curve are **not claimed as new**. The present result instead proves the exact **necessary-and-sufficient additive-resonance classification for arbitrary primitive diagonal windings** and rigorously minimizes arclength over that whole restricted class, including equality characterization. Lindblad [3] treats asymptotic existence of general design curves on \(S^3\), rather than this finite-strength winding optimization. Closely related published harmonic-trace and sampling-rank results address recovery from Clifford tori or fixed winding curves, not moment cancellation and sharp arclength in the full one-phase family.

## Limitations
The one-parameter constant-amplitude ansatz is essential. Neither global optimality among all curves, nor stability under arbitrary non-toric perturbations, nor strength four is established. All dimensions \(d\ge3\) are covered analytically, while regression computations cover only finite cases. The complete 2026 King–Mixon manuscript was inspected through its publicly accessible full-text transcription; potential independent treatments outside indexed literature remain a priority risk. No independent mathematical audit is claimed.

## References
1. M. Ehler and K. Gröchenig, *t-Design Curves and Mobile Sampling on the Sphere*, arXiv:2306.13152v1 (June 19, 2023), https://arxiv.org/html/2306.13152v1 .
2. E. J. King and D. G. Mixon, *Short Spherical t-Design Curves*, arXiv:2607.15386v1 (July 16, 2026), https://arxiv.org/abs/2607.15386 ; publicly readable full-text transcription at https://www.researchgate.net/publication/410593879_Short_spherical_t-design_curves .
3. A. Lindblad, *Asymptotically Optimal t-Design Curves on S3*, arXiv:2408.04044v1 (August 7, 2024), https://arxiv.org/abs/2408.04044 .
