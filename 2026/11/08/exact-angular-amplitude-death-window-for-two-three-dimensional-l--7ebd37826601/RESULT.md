# Exact angular amplitude-death window for two three-dimensional limit-cycle oscillators

## Finding

For two equally fast three-dimensional oscillators, **the rotation-axis angle exactly determines whether coupling can stabilize the zero state**. Let \(K>0\) be the total mean-field coupling parameter, \(\omega>0\) the common rotation magnitude, and \(\theta\in[0,\pi]\) the angle between the axes. Define
\[
L(K,\omega)=\frac{2}{K}\left(1+\frac{(K-2)^2}{\omega^2}\right),\qquad
U(K,\omega)=\frac{K-1}{K}\left(1+\frac1{\omega^2}\right).
\]
The zero equilibrium is **locally exponentially asymptotically stable** precisely when
\[
K>3,\quad \omega^2>2K-3,\quad
L(K,\omega)<\sin^2(\theta/2)<U(K,\omega). \tag{1}
\]
The angle window is nonempty precisely when the first two strict inequalities hold, and its width in \(\sin^2(\theta/2)\) is
\[
U-L=\frac{K-3}{K}\left(1-\frac{2K-3}{\omega^2}\right). \tag{2}
\]
Consequently, an admissible angle and coupling exist for a given \(\omega\) **if and only if** \(\omega>\sqrt3\). For perpendicular axes \(\theta=\pi/2\), condition (1) becomes
\[
K>4,\qquad \omega^2>\frac{4(K-2)^2}{K-4}; \tag{3}
\]
its smallest possible frequency threshold is \(\omega>4\sqrt2\), attained as a sharp infimum at \(K=6\). For fixed \(\omega>4\sqrt2\), the complete coupling window for perpendicular axes is
\[
\frac{\omega^2+16-\omega\sqrt{\omega^2-32}}8
<K<\frac{\omega^2+16+\omega\sqrt{\omega^2-32}}8.
\]
The large difference between the optimal-angle and perpendicular-axis thresholds is an exact orientational effect, not frequency heterogeneity between oscillators.

## Assumptions and scope

Fix two vectors \(r_1(t),r_2(t)\in\mathbb R^3\). For two **unit** vectors \(u_1,u_2\in\mathbb R^3\) with \(u_1\cdot u_2=\cos\theta\), consider
\[
\dot r_i=(1-|r_i|^2)r_i+\omega u_i\times r_i
+\frac K2(r_{3-i}-r_i),\qquad i=1,2. \tag{4}
\]
This is the two-node specialization of the mean-field model of Zou, He, Senthilkumar and Kurths [1]. Parameters are time-independent, \(K>0\), \(\omega>0\), and \(0\le\theta\le\pi\). The classification concerns the equilibrium \((r_1,r_2)=(0,0)\) and **local exponential stability**. It is not a classification of all attractors or global basins; exponential stability is not asserted at equality boundaries.

## Proof

**1. Rotational normal form and hidden involution.** Simultaneously rotate coordinates so that, for \(\alpha=\theta/2\), the two frequency axes are
\[
u_1=(\sin\alpha,0,\cos\alpha),\qquad
u_2=(-\sin\alpha,0,\cos\alpha).
\]
Put \(h=K/2\), \(a=\sin\alpha\), \(b=\cos\alpha\). The skew rotation matrices \(W_i x=\omega u_i\times x\) obey \(W_2=RW_1R\), where \(R=\operatorname{diag}(-1,-1,1)\) is an orthogonal involution. The Jacobian at zero is
\[
M=\begin{pmatrix}(1-h)I_3+W_1&hI_3\\hI_3&(1-h)I_3+W_2\end{pmatrix}.
\]
The two invariant three-dimensional linear subspaces \(\{(v,Rv):v\in\mathbb R^3\}\) and \(\{(v,-Rv):v\in\mathbb R^3\}\) give similar blocks \((1-h)I_3+W_1+hR\) and \((1-h)I_3+W_1-hR\). Direct evaluation of the two tridiagonal determinants, with \(z=\lambda-1\), yields the **exact factorization**
\[
\det(\lambda I_6-M)=P_+(z)P_-(z),
\]
\[
P_+(z)=z^3+4hz^2+(4h^2+\omega^2)z+2h\omega^2a^2,
\]
\[
P_-(z)=z^3+2hz^2+\omega^2z+2h\omega^2b^2.\tag{5}
\]
This argument also applies when the two axes coincide or are antiparallel.

**2. Cubic Hurwitz criteria.** Set \(u=a^2=\sin^2(\theta/2)\), so \(b^2=1-u\). Express the cubic \(P_-(\lambda-1)\) as \(\lambda^3+A\lambda^2+B\lambda+C\), obtaining
\[
A=2h-3,\quad B=\omega^2-4h+3,\quad
C=2h-1+[2h(1-u)-1]\omega^2,
\]
\[
AB-C=2(hu-1)\omega^2-8(h-1)^2. \tag{6}
\]
For a real monic cubic, Hurwitz stability is equivalent to the four strict conditions \(A>0\), \(B>0\), \(C>0\), and \(AB>C\). Under \(A>0\) and \(AB>C>0\), the condition \(B>0\) is automatic. Hence the minus block is Hurwitz precisely when
\[
h>\tfrac32,\quad
(hu-1)\omega^2>4(h-1)^2,\quad
[2h(1-u)-1]\omega^2>1-2h. \tag{7}
\]
The plus cubic has coefficients
\[
A_+=4h-3,\quad B_+=4h^2-8h+3+\omega^2,\quad
C_+=[2hu-1]\omega^2-(2h-1)^2,
\]
\[
A_+B_+-C_+=8(h-1)^2(2h-1)+2[h(2-u)-1]\omega^2.\tag{8}
\]
When \(h>3/2\), \(A_+>0\), \(B_+>0\), and \(A_+B_+-C_+>0\). It remains to show \(C_+>0\) follows from (7). The middle inequality of (7) forces \(1<hu\le h\) and
\[
\omega^2>\frac{4(h-1)^2}{hu-1}
>\frac{(2h-1)^2}{2hu-1}.
\]
For completeness, the positivity of the cross-multiplied numerator is
\[
E=(4h^2-12h+7)(hu)+4h-3>0.
\]
Indeed, if its coefficient of \(hu\) is nonnegative, use \(hu>1\) to bound \(E>4(h-1)^2\); otherwise use \(hu\le h\) to obtain \(E\ge(h-1)(2h-1)(2h-3)>0\). Thus \(C_+>0\) and the plus block is automatically Hurwitz when the minus block is. Therefore (7) is equivalent to **all six eigenvalues of \(M\) having negative real parts**.

**3. Exact angular interval and thresholds.** Inserting \(h=K/2\) into (7) gives \(K>3\) and the two strict angular bounds in (1). Their difference is exactly (2). For \(K>3\), this interval is nonempty if and only if \(\omega^2>2K-3\); in that case \(0<L<U<1\). Existence over some \(K>3\) is therefore equivalent to \(\omega^2>3\): choose any \(K\) strictly between \(3\) and \((\omega^2+3)/2\), and then any \(u\in(L,U)\). Specializing \(u=1/2\) gives (3), whose right side has unique minimum \(32\) at \(K=6\). Solving the associated quadratic inequality in \(K\) gives the stated perpendicular-axis window.

**4. Nonlinear conclusion and boundaries.** The vector field (4) is smooth and its nonlinear remainder at the origin is cubic. A Hurwitz Jacobian implies local exponential asymptotic stability by the standard linearization theorem. Conversely, local exponential stability of a smooth equilibrium requires the derivative of its flow, hence the linearized semigroup, to decay exponentially, so its Jacobian must be Hurwitz. Equalities in (1) thus do not yield exponential stability; they need not imply nonlinear instability or exclude slower nonlinear convergence. This establishes the stated if-and-only-if claim without making global claims.

## Verification

The companion script `verify_window.py` uses Python's standard library only. Running `python3 verify_window.py` passed **4,096 exact rational checks** on 512 rational parameter configurations: seven independently evaluated values of each full six-dimensional characteristic determinant per configuration, and one comparison of the complete cubic Routh–Hurwitz inequalities against the angular-window criterion. The proof above, not this finite grid, establishes the quantifiers for all real admissible parameters.

Numerical examples: \(K=4,\omega=3\) gives \(L=13/18<U=5/6\), so axes with \(\sin^2(\theta/2)=4/5\) are stable, whereas orthogonal axes are not. For \(K=6,\omega=6\), the permissible squared-half-angle interval is \((13/27,185/216)\). These are illustrations, not an exhaustive scan.

## Relationship to prior work

Zou, He, Senthilkumar and Kurths [1] defined the high-dimensional coupled-oscillator system, obtained amplitude-death conditions for distributions of natural rotations in a thermodynamic limit, and referred separately to finite-network linearization in supplementary material. The theorem above is an exact two-node, equal-rotation-magnitude, **arbitrary inter-axis angle** stability classification, including a closed angular window and a sharp finite-pair frequency threshold; the main text's distributional spectral relations do not state this formula. Gogoi and collaborators [2], Sections III.1.2 and IV, analyze two three-dimensional oscillators with misaligned axes and symmetry-preserving or breaking coupling, predominantly via invariant manifolds and numerical parameter explorations. That work does not give the stated exact angular interval, and its reported low-frequency oscillation-death regimes do not determine the high-frequency local stability of the zero equilibrium. Classical two-dimensional nonidentical Stuart–Landau death conditions concern a different axis/frequency geometry [3]. The claim is about the new explicit classification, not about discovering amplitude death or the underlying oscillator model.

## Limitations

The theorem is restricted to exactly two oscillators, equal positive angular speed, isotropic diffusive coupling, unit individual linear growth, and local exponential stability at the origin. It does not identify all other equilibria, basin sizes, global attraction, or nonlinear bifurcation type at nonhyperbolic boundaries. The 2023 source's complete finite-network supplementary analysis was not obtainable for full-text comparison; its possible implications for this explicit two-axis specialization remain a publication-priority risk. An equivalent calculation in unindexed literature also cannot be ruled out by searches alone.

## References

1. W. Zou, S. He, D. V. Senthilkumar, J. Kurths, *Solvable Dynamics of Coupled High-Dimensional Generalized Limit-Cycle Oscillators*, arXiv:2302.05603 (first posted 2023-02-11); *Physical Review Letters* **130**, 107202 (2023), doi:10.1103/PhysRevLett.130.107202. Full main text: https://arxiv.org/abs/2302.05603.
2. P. B. Gogoi, A. Prasad, A. Patel, R. Ramaswamy, D. Ghoshal, *Dynamics of coupled \(D\)-dimensional Stuart-Landau oscillators*, arXiv:2511.19052v1 (2025-11-24), especially Section III.1.2. https://arxiv.org/html/2511.19052v1.
3. N. Punetha et al., *Dynamical effects of breaking rotational symmetry in counter-rotating Stuart-Landau oscillators*, *Physical Review E* **98**, 022212 (2018), doi:10.1103/PhysRevE.98.022212 (abstract-level contextual comparison).
