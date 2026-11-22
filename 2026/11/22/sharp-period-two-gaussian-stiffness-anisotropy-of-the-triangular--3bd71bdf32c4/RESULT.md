# Sharp period-two Gaussian stiffness anisotropy of the triangular lattice

## Finding

Let \(\Lambda\subset\mathbb R^2\) be the unit-density triangular lattice with primitive vectors
\[
e_1=s(1,0),\qquad e_2=s(1/2,\sqrt3/2),\qquad s=\sqrt{2/\sqrt3}.
\]
Put \(a=e_1+e_2\), \(b=e_1-e_2\), \(A=|a|=\sqrt3s\), \(B=|b|=s\), and \(L=\mathbb Za+\mathbb Zb\). Thus \(a\perp b\), \([\Lambda:L]=2\), and \(AB=2\). For each relative shift \(v\in\mathbb R^2\) for which the cosets are distinct, define the periodic point configuration
\[
C_v=L\cup(e_1+v+L).
\]
Its Gaussian pair energy per point, with self-interactions excluded, is
\[
\mathcal E_\alpha(v)=\lim_{R\to\infty}\frac1{|C_v\cap B_R|}\!
\sum_{\substack{x,y\in C_v\cap B_R\\x\ne y}}e^{-\alpha|x-y|^2},\qquad\alpha>0.
\]
We use orthonormal axes \(\widehat a=a/A\) and \(\widehat b=b/B\), so \(v=v_a\widehat a+v_b\widehat b\). The Hessian \(D^2\mathcal E_\alpha(0)\) is diagonal in these axes, with strictly positive eigenvalues \(\lambda_A(\alpha)\), \(\lambda_B(\alpha)\). For every \(\alpha>0\),
\[
\boxed{\lambda_A(\alpha)>3\lambda_B(\alpha)>0.}
\]
The factor three is the **best universal constant**: \(\lambda_A/\lambda_B\to3\) as \(\alpha\to\infty\). More precisely,
\[
\frac{\lambda_A(\alpha)}{\lambda_B(\alpha)}
=3+\frac{4}{\alpha B^2}+O(\alpha^{-2})\qquad(\alpha\to\infty),
\]
whereas the broad-Gaussian regime obeys the exponentially anisotropic law
\[
\frac{\lambda_A(\alpha)}{\lambda_B(\alpha)}
=\frac13\exp\!\left(\frac{2\pi^2}{3\alpha B^2}\right)(1+o(1))
\qquad(\alpha\downarrow0).
\]
The same **strict threefold ratio** holds for the Hessian of every nonzero finite positive Gaussian mixture \(\sum_{j=1}^m c_j e^{-\alpha_j r^2}\), with \(c_j,\alpha_j>0\), under the same geometric displacement. In addition, the Gaussian energy has a unique global relative-shift minimum at \(v\equiv0\pmod L\), a qualitative fact included for context rather than claimed as a new optimum.

## Assumptions and scope

All distances are Euclidean; the basis \(a,b\), the physical Cartesian displacement coordinates \((v_a,v_b)\), and the density-one normalization above are fixed. The energy formula defines a smooth, \(L\)-periodic analytic continuation to all \(v\). At shifts satisfying \(e_1+v\in L\), the union has only one coset and its density changes; statements about point-configuration energy exclude those coincidences, while the analytic continuation remains well-defined. Derivatives are always taken at \(v=0\), where the two cosets are distinct. No shape deformation, arbitrary phonon mode, or general periodic perturbation is included. Rotating to either of the other two index-two sublattices gives the same spectrum.

## Proof

**1. Exact energy reduction and lattice geometry.** Since \(e_1=(a+b)/2\) and \(a\perp b\), the displacement between representatives of the two cosets is a vector from \(e_1+v+L\). Gaussian absolute convergence and the standard two-representative periodic energy identity give
\[
\mathcal E_\alpha(v)=\sum_{\ell\in L\setminus\{0\}}e^{-\alpha|\ell|^2}
+\sum_{\ell\in L}e^{-\alpha|e_1+v+\ell|^2}.
\]
Define for \(T>0\)
\[
F_T(t)=\sum_{k\in\mathbb Z}
\exp\!\left[-\alpha\bigl(T(k+\tfrac12)+t\bigr)^2\right].
\]
Orthogonality separates the cross-coset term exactly:
\[
\mathcal E_\alpha(v)=E_{\mathrm{within}}+F_A(v_a)F_B(v_b).
\tag{1}
\]
In particular \(\mathcal E_\alpha(0)\) equals the usual triangular-lattice Gaussian energy, and the factor \(AB=2\) ensures density one.

**2. Global shift minimizer and exact Hessian.** For \(q_T=\exp[-\pi^2/(\alpha T^2)]\), one-dimensional Poisson summation gives
\[
F_T(t)=\frac{\sqrt\pi}{T\sqrt\alpha}
\vartheta_4\!\left(\frac{\pi t}{T},q_T\right),
\]
where the classical Jacobi product (an established identity) is
\[
\vartheta_4(z,q)=\prod_{j\ge1}(1-q^{2j})
\left((1-q^{2j-1})^2+4q^{2j-1}\sin^2z\right).
\tag{2}
\]
All factors are positive, and each achieves its unique minimum modulo \(\pi\) at \(\sin z=0\). Hence \(F_T(t)>F_T(0)>0\) for \(t\notin T\mathbb Z\), which also shows that (1) is minimized precisely when \(v\in L\). Moreover \(F_T'(0)=0\), and differentiating the uniformly convergent logarithm of (2) twice yields
\[
K_T(\alpha):=\frac{F_T''(0)}{F_T(0)}
=\frac{8\pi^2}{T^2}
\sum_{j\ge1}\frac{q_T^{2j-1}}{(1-q_T^{2j-1})^2}>0.
\tag{3}
\]
The mixed derivative of (1) vanishes at \(v=0\), so
\[
\lambda_A=F_A(0)F_B(0)K_A(\alpha),\qquad
\lambda_B=F_A(0)F_B(0)K_B(\alpha).
\tag{4}
\]
This includes the full normalization of the energy per point, rather than per unit cell.

**3. Strict, sharp anisotropy.** Let \(x_T=\pi^2/(\alpha T^2)\). Using \(e^{-u}/(1-e^{-u})^2=1/(4\sinh^2(u/2))\) in (3), obtain
\[
\frac{K_T(\alpha)}{T^2}
=\frac{2\alpha^2}{\pi^2}
\sum_{j\ge1}\left[
\frac{x_T}{\sinh((2j-1)x_T/2)}\right]^2.
\tag{5}
\]
For every \(c>0\), \(x\mapsto x/\sinh(cx)\) strictly decreases for \(x>0\): the logarithmic derivative equals \(1/x-c\coth(cx)<0\), since \(u\coth u>1\). Because \(A>B\) implies \(0<x_A<x_B\), comparing the strictly positive terms in (5) proves
\[
\frac{K_A}{A^2}>\frac{K_B}{B^2}.
\]
Then (4) and \(A^2=3B^2\) imply \(\lambda_A/\lambda_B>3\). Every step holds for all positive \(\alpha\) without finite truncation.

**4. The two limiting regimes.** As \(\alpha\to\infty\), only \(k=0,-1\) contribute at leading order to each shifted Gaussian sum and its second derivative, and the next squared distance is \(9T^2/4\), a gap of \(2T^2\). Therefore
\[
K_T(\alpha)=\alpha^2T^2-2\alpha
+O_T\!\left(\alpha^2e^{-2\alpha T^2}\right).
\]
Taking the quotient at \(A^2=3B^2\) gives \(\lambda_A/\lambda_B=3+4/(\alpha B^2)+O(\alpha^{-2})\). Thus three is the largest lower bound valid uniformly in \(\alpha\). For \(\alpha\downarrow0\), the rapidly convergent dual sum in (3) gives
\[
K_T(\alpha)=\frac{8\pi^2}{T^2}
\exp\!\left[-\frac{\pi^2}{\alpha T^2}\right]
\left(1+O_T\!\left(e^{-\pi^2/(\alpha T^2)}\right)\right),
\]
so (4) directly yields
\[
\frac{\lambda_A}{\lambda_B}=\frac{B^2}{A^2}
\exp\!\left[\frac{\pi^2}{\alpha}
\left(\frac1{B^2}-\frac1{A^2}\right)\right](1+o(1)),
\]
which specializes to the stated exponential law.

**5. Positive mixtures.** For a finite mixture with each \(c_j>0\) and \(\alpha_j>0\), add the component energies. Its two Hessian eigenvalues are respectively \(\sum_j c_j\lambda_A(\alpha_j)\) and \(\sum_j c_j\lambda_B(\alpha_j)\), in the same axes. Their difference after subtracting three times the second is \(\sum_jc_j(\lambda_A(\alpha_j)-3\lambda_B(\alpha_j))>0\). No assertion is made for signed mixtures or mixtures whose second derivatives do not converge.

## Verification

The standalone, standard-library `verification/check.py` recomputes the two-dimensional cross-coset Gaussian energy by direct double sums, compares it to the exact product (1), differentiates independent real-space one-dimensional Gaussian sums, and compares these derivatives to the Jacobi-product Hessian (3). It tests both asymptotic regimes and the strict ratio over a range of positive parameters, with 49 numerical assertions. Run with `python3 verification/check.py`. These finite checks corroborate, but do not replace, the infinite-sum argument (2)–(5).

## Relationship to prior work

Faulhuber and Petersen, *Uniqueness of the hexagonal lattice's universal optimality* (arXiv:2611.06278; first public posting 4 November 2026), establish global Gaussian optimality and equality rigidity among periodic configurations. Their results imply strict energy minimality but do not state the two polarization curvatures or the sharp ratio for an index-two relative-shift mode. Leblé, *The hexagonal lattice is universally locally optimal* (arXiv:2511.03353), proves local energy lower bounds for general bounded perturbations using spectral measures; the present explicit, all-parameter **two-mode curvature ratio** is not that general theorem's stated bound. Hardin and Tenpas, *Universally Optimal Periodic Configurations in the Plane* (arXiv:2307.15822), already establish the two-coset qualitative optimality via theta functions and explicitly use the classical Jacobi product. Bétermin's *Minimal Soft Lattice Theta Functions* (arXiv:1809.00473) proves translated-lattice minimization results; Bétermin and Faulhuber's *Maximal Theta Functions* (arXiv:2007.15977) concerns centered/alternating lattice theta extremality. Those established minima, and the Jacobi product itself, are not claimed as new. The additional assertion isolated here is the exact uniform spectral separation \(\lambda_A>3\lambda_B\), its optimal factor, and its limiting scale dependence for the specified perturbation.

## Limitations

The result is restricted to fixed-period, fixed-lattice, two-coset relative translations. It neither calculates the full spectrum of arbitrary periodic lattice displacements nor gives a uniform coercivity constant against all configurations or a complete stability theorem. Other translated-lattice and theta-function literature could contain equivalent derivative inequalities even when the same period-doubling terminology is absent. The cited independent earlier results are not re-proved. The numerical tests are not an exhaustive or computer-assisted infinite proof. Independent audit of the new comparison and theorem has not been performed.

## References

1. M. Faulhuber and P. Petersen, *Uniqueness of the hexagonal lattice's universal optimality*, arXiv:2611.06278 (first publicly posted 2026-11-04), https://arxiv.org/abs/2611.06278.
2. T. Leblé, *The hexagonal lattice is universally locally optimal*, arXiv:2511.03353 (2025), https://arxiv.org/abs/2511.03353.
3. D. P. Hardin and N. J. Tenpas, *Universally Optimal Periodic Configurations in the Plane*, Discrete Analysis 2025:26, arXiv:2307.15822, https://arxiv.org/abs/2307.15822.
4. L. Bétermin, *Minimal Soft Lattice Theta Functions*, Constructive Approximation 52 (2020), arXiv:1809.00473, https://arxiv.org/abs/1809.00473.
5. L. Bétermin and M. Faulhuber, *Maximal Theta Functions — Universal Optimality of the Hexagonal Lattice for Madelung-Like Lattice Energies*, Journal d'Analyse Mathématique 149 (2023), arXiv:2007.15977, https://arxiv.org/abs/2007.15977.
6. Classical Jacobi triple product and Poisson summation formulas; see, for instance, Hardin–Tenpas, Section 2.5.
