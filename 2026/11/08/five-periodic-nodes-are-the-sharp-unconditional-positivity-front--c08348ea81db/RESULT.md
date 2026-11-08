# Five periodic nodes are the sharp unconditional-positivity frontier for Gauss–Legendre heat stepping

## Finding

Consider the classical two-stage, fourth-order Gauss–Legendre Runge–Kutta end-step applied to the uniform nearest-neighbor semidiscrete heat equation on a periodic cycle of \(n\) distinct nodes. The end-step operator is nonnegative entrywise for **every** dimensionless step size precisely when \(3\le n\le5\). For each \(n\ge6\), its entry connecting neighboring nodes is negative for all sufficiently large steps, even though every eigenvalue of the end-step matrix is strictly positive and at most one.

In detail, put \(A_n=2I_n-S_n-S_n^{-1}\), with \(S_n\) cyclic shift, and
\[
r(z)=\frac{1+z/2+z^2/12}{1-z/2+z^2/12},\qquad T_n(h)=r(-hA_n),\qquad h\ge0.
\]
Then, for every integer \(n\ge3\),
\[
\boxed{\ T_n(h)\ge0\ \text{entrywise for every }h\ge0\ \Longleftrightarrow\ n\le5.\ }
\]
For each fixed \(n\ge6\), the adjacent entry has the explicit sharp large-step expansion
\[
\boxed{\ [T_n(h)]_{0,1}=-\frac{(n-1)(n-5)}{nh}+O_n(h^{-2})\quad(h\to\infty).\ }
\]
In particular, for the six-node cycle at \(h=8\), the adjacent entry is exactly \(-6584/580537\). Every \(T_n(h)\) preserves total mass. This is a classification of one-step **endpoint** positivity, not of the internal stages.

## Assumptions and scope

All operations are in exact real arithmetic. The spatial discretization has equal nearest-neighbor conductances, periodic wraparound, and \(n\ge3\) nodes. The dimensionless time step is \(h=\kappa\Delta t/\Delta x^2\) when the heat diffusivity is \(\kappa>0\), the physical step is \(\Delta t\ge0\), and the mesh spacing is \(\Delta x>0\). The method is the usual two-stage Gauss–Legendre collocation Runge–Kutta rule, whose scalar stability function is \(r\) above. An end-step preserves nonnegative data exactly when its matrix is entrywise nonnegative.

Write \(t_{n,k}(h)=[T_n(h)]_{0,k}\). Circulant symmetry gives \(t_{n,k}=t_{n,n-k}\), so for the small cycles it suffices to list \(0\le k\le\lfloor n/2\rfloor\).

## Proof

**1. Rational form and spectral control.** Since \(A_n\) is symmetric positive semidefinite, the polynomial
\[
D_n(h)=I_n+\frac h2A_n+\frac{h^2}{12}A_n^2
\]
is positive definite for \(h\ge0\). Thus
\[
T_n(h)=D_n(h)^{-1}\left(I_n-\frac h2A_n+\frac{h^2}{12}A_n^2\right).
\]
For any \(x\ge0\), the numerator and denominator of \(r(-x)\) are respectively \(((x-3)^2+3)/12\) and \(((x+3)^2+3)/12\). Therefore \(0<r(-x)\le1\) with equality at \(x=0\); in particular the end-step is symmetric positive definite and a Euclidean contraction, with eigenvalue one on the constant vector. As \(A_n\mathbf1=0\), we also have \(T_n(h)\mathbf1=\mathbf1\) for all \(h\ge0\).

**2. Exact small-cycle kernels.** The entries below follow by multiplying the proposed circulant matrix by \(D_n(h)\) and verifying the numerator matrix identity above; this is a finite polynomial calculation and the verification artifact independently checks every matrix entry.

For \(n=3\), set \(d_3=3h^2+6h+4\). Then
\[
t_{3,0}=\frac{3h^2-2h+4}{d_3},\qquad
 t_{3,1}=\frac{4h}{d_3}.
\]
The diagonal numerator is \(3(h-1/3)^2+11/3>0\), and all other factors are nonnegative for \(h\ge0\).

For \(n=4\), set \(d_4=(h^2+3h+3)(4h^2+6h+3)\). Then
\[
\begin{aligned}
t_{4,0}&=\frac{4h^4+3h^3+6h^2+9h+9}{d_4},\\
t_{4,1}&=\frac{3h}{4h^2+6h+3},\\
t_{4,2}&=\frac{9h^2(h+1)}{d_4}.
\end{aligned}
\]
Every displayed denominator is positive and numerator nonnegative for \(h\ge0\).

For \(n=5\), set \(d_5=25h^4+150h^3+360h^2+360h+144\). Then
\[
\begin{aligned}
t_{5,0}&=\frac{25h^4+30h^3+72h^2+72h+144}{d_5},\\
t_{5,1}&=\frac{72h(h+2)}{d_5},\\
t_{5,2}&=\frac{12h^2(5h+6)}{d_5}.
\end{aligned}
\]
Again all entries are nonnegative. These expressions cover every entry by cyclic symmetry, proving unconditional endpoint positivity for all three sizes.

**3. Green function and all larger cycles.** Let \(A_n^\dagger\) denote the Moore–Penrose inverse of \(A_n\). Its circulant kernel at cyclic offset \(k\in\{0,\ldots,n-1\}\) is
\[
g_{n,k}=\frac{n^2-1}{12n}-\frac{k(n-k)}{2n}.
\]
Indeed, its entries have zero row sum because \(\sum_{k=0}^{n-1}k(n-k)=n(n^2-1)/6\). Direct discrete second differences show \(A_nG_n=I_n-\mathbf1\mathbf1^{\mathsf T}/n\) for the circulant matrix \((G_n)_{ij}=g_{n,(i-j)\bmod n}\). Since this is the zero-mean inverse on the orthogonal complement of the constants, \(G_n=A_n^\dagger\).

For a positive eigenvalue \(\lambda\) of \(A_n\), direct rational expansion gives
\[
r(-h\lambda)=1-\frac{12}{h\lambda}+O_\lambda(h^{-2})\quad(h\to\infty),
\]
while the constant eigenvalue has multiplier \(r(0)=1\). There are finitely many eigenvalues for each fixed \(n\), so the spectral theorem yields the matrix expansion
\[
T_n(h)=I_n-\frac{12}{h}A_n^\dagger+O_n(h^{-2}).
\]
At neighboring nodes,
\[
g_{n,1}=\frac{n^2-1}{12n}-\frac{n-1}{2n}
=\frac{(n-1)(n-5)}{12n}.
\]
Consequently \([T_n(h)]_{0,1}=-(n-1)(n-5)/(nh)+O_n(h^{-2})\), strictly negative at all sufficiently large \(h\) whenever \(n\ge6\). This proves that no larger periodic cycle enjoys positivity for all steps and completes the classification.

**4. A finite exact witness.** For \(n=6\), rational elimination additionally yields
\[
[T_6(h)]_{0,1}=\frac{-2h(5h^4-12h^3-102h^2-144h-72)}{(h^2+6h+12)(3h^2+6h+4)(4h^2+6h+3)}.
\]
Substitution \(h=8\) gives \(-6584/580537<0\). Thus a nonnegative coordinate impulse can produce a negative temperature at its adjacent coordinate in a single step.

## Verification

The standalone `artifacts/verify_gauss_cycle.py` uses exact SymPy expressions. It verifies each small-cycle kernel against all entries of the matrix rational identity, verifies the Green-function Poisson and zero-mean identities for a range of finite cycle sizes, checks rational end-steps and mass conservation, and independently reconstructs the six-cycle witness. The stored execution in `artifacts/verification.txt` records 16,391 successful exact symbolic/rational assertions. The all-\(n\) statement is proved by the spectral and Green-function argument above; checking finitely many sizes cannot replace that argument.

## Relationship to prior work

The existence of the Gauss–Legendre \([2/2]\) Padé stability map, its A-stability, and generic positivity obstructions for diagonal Padé methods are classical, and no novelty is claimed for them. Zappavigna, Colaneri, Kirkland and Shorten (2012) investigate nonnegativity of diagonal Padé maps for general positive systems and exhibit counterexamples, including nonconservative systems; their results do not specify a sharp unconditional-positivity frontier for uniform periodic heat cycles. A related published Markov-generator analysis proves an eight-state minimal dimension for positivity failures at arbitrarily small step sizes. That is a different quantifier and generator class: here every fixed heat cycle is positive at sufficiently small steps, while some cycles lose positivity at **large** steps, with sharp cutoff five.

Gottlieb, Grant, Hu and Shu (2021) develop higher-order unconditionally strong-stability-preserving multi-derivative implicit methods using extra derivative assumptions, rather than the classical Gauss–Legendre method on this cycle. Torlo, Öffner and Ranocha (2022) analyze positive scalar test problems and report the fourth-order Gauss–Legendre scalar multiplier as positive for all steps; scalar spectral positivity is compatible with the negative matrix entry proved here. Wade, Khaliq, Siddique and Yousuf (2005) study diagonal Padé methods **combined with positivity-preserving smoothing** for parabolic problems, which is distinct from the unsmoothed end-step; their full paper was not obtained for theorem-level exclusion.

These comparisons delimit the presently supported novelty claim to the exact cycle-size frontier, explicit small-cycle nonnegative kernels, and universal adjacent large-step sign law. Older or specialized literature may contain equivalent cycle-specific formulations; the originality assessment remains provisional until independently checked.

## Limitations

The theorem concerns a linear, constant-coefficient, uniform periodic nearest-neighbor heat discretization and an exact-arithmetic one-step endpoint map. It makes no claim about Dirichlet boundaries, irregular graphs, anisotropic/variable diffusion, nonlinear heat equations, internal stages, floating-point positivity or a sharp finite-step positivity interval for every \(n\ge6\). The \(O_n(h^{-2})\) remainder is for each fixed size, not uniform as \(n\to\infty\). It is not an assertion that A-stability or positive eigenvalues imply positivity in general; indeed the example refutes that implication.

## References

1. S. Gottlieb, Z. J. Grant, J. Hu and R. Shu, “High order strong stability preserving multi-derivative implicit and IMEX Runge–Kutta methods with asymptotic preserving properties,” arXiv:2102.11939v1, publicly posted February 23, 2021. https://arxiv.org/abs/2102.11939
2. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, “Essentially negative news about positive systems,” *Linear Algebra and its Applications* 436 (2012), 3425–3442. https://doi.org/10.1016/j.laa.2011.12.021
3. D. Torlo, P. Öffner and H. Ranocha, “Issues with positivity-preserving Patankar-type schemes,” 2022, see the analysis of fourth-order Gauss–Legendre scalar positivity. https://davidetorlo.it/files/publications/Torlo2021StabilityPatankar.pdf
4. B. A. Wade, A. Q. M. Khaliq, M. Siddique and M. Yousuf, “Smoothing with positivity-preserving Padé schemes for parabolic problems with nonsmooth data,” *Numerical Methods for Partial Differential Equations* 21 (2005), 553–573. https://doi.org/10.1002/num.20039
5. “Eight-state barrier for Markov positivity of the [2/2] Padé map,” accessible published mathematical research record. https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab
6. “Unconditional lattice positivity from backward-Euler-filtered Crank–Nicolson,” accessible published mathematical research record. https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-backward-euler-filtered-cn-lattice-positivity--1f6f56bd0eac
7. A. Itkin and R. Kazbek, “Diagonal Frog meets ADI: trading matrix exponentials for rational maps in the Fokker–Planck equation,” arXiv:2608.22703 (2026). https://arxiv.org/abs/2608.22703
