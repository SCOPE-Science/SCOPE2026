# A zero-free Fourier law and sharp inverse bound for half-radius Lee balls on odd square tori

## Finding

Let \(N=2r+1\ge3\) be any odd integer. On \(G=(\mathbb Z/N\mathbb Z)^2\), take the Lee ball
\[
B_N=\{(x,y):d_N(x)+d_N(y)\le r\},\qquad d_N(x)=\min(\bar x,N-\bar x),
\]
where \(\bar x\in\{0,\ldots,N-1\}\). Let \(\zeta=e^{-2\pi i/N}\) and use the **unnormalized** Fourier convention
\[
\Lambda_N(k,\ell)=\sum_{(x,y)\in B_N}\zeta^{kx+\ell y},\qquad 0\le k,\ell<N.
\]
Then \(|B_N|=(N^2+1)/2\), \(\Lambda_N(0,0)=|B_N|\), and at every nonzero character
\[
\Lambda_N(k,\ell)=
\begin{cases}
\displaystyle\frac{(-1)^k}{\cos(\pi k/N)+\cos(\pi\ell/N)},&k+\ell\text{ even},\\[5pt]
\displaystyle\frac{(-1)^{k+1}}{\cos(\pi\ell/N)-\cos(\pi k/N)},&k+\ell\text{ odd}.
\end{cases}
\]
Both displayed denominators are nonzero in their stated domains. Hence all Fourier multipliers are nonzero. Moreover
\[
\min_{0\le k,\ell<N}|\Lambda_N(k,\ell)|=\frac{1}{2\cos(\pi/N)}
\]
and **the only minimizers** are the four characters
\[
(k,\ell)\in\{(1,1),(1,N-1),(N-1,1),(N-1,N-1)\}.
\]
Thus unnormalized convolution \(T_Nf=\mathbf1_{B_N}*f\) is invertible on the Hilbert space \(\ell^2(G)\), with exactly
\[
\|T_N^{-1}\|_{2\to2}=2\cos(\pi/N),\quad
\|T_N\|_{2\to2}=\frac{N^2+1}{2},\quad
\kappa_2(T_N)=(N^2+1)\cos(\pi/N).
\]
These equalities hold for every odd integer \(N\ge3\), whether prime or composite.

## Assumptions and scope

All elements of \(G\) use representatives \(0,\ldots,N-1\). The ball is defined by **cyclic**, not ordinary, coordinate distance. A Fourier multiplier is the sum over \(B_N\) without division by \(N^2\), and convolution uses counting measure: \((T_N f)(z)=\sum_{b\in B_N}f(z-b)\). The norm is induced by counting-measure \(\ell^2\), so Fourier characters diagonalize \(T_N\) without changing its singular values. The radius is specifically \(r=(N-1)/2\); no result is claimed for other radii or dimensions.

## Proof

**1. Rotated integer square.** The representative square \([-r,r]^2\subset\mathbb Z^2\) maps bijectively to \(G\). For any integer pair in that square, put \(u=x+y\) and \(v=x-y\). The identity \(|x|+|y|=\max(|u|,|v|)\) shows that \(B_N\) corresponds exactly to the pairs \(u,v\in[-r,r]\) having the same parity. Therefore it has \((N^2+1)/2\) points, and the Fourier transform, being real by inversion symmetry, is the parity-filtered geometric sum
\[
\Lambda_N(k,\ell)=\frac12\left[A(\alpha)A(\beta)+A(-\alpha)A(-\beta)\right],
\quad A(t)=\sum_{j=-r}^rt^j,
\quad \alpha=e^{-\pi i(k+\ell)/N},\quad\beta=e^{-\pi i(k-\ell)/N}.
\]
The equality follows because \(x=(u+v)/2\), \(y=(u-v)/2\) are integers precisely when \(u,v\) have the same parity.

**2. Evaluation of the geometric sums.** For \(t\ne1\),
\[
A(t)=t^{-r}\frac{1-t^N}{1-t},\qquad N=2r+1.
\]
If \(k+\ell\) is even and \((k,\ell)\ne(0,0)\), the product \(A(\alpha)A(\beta)\) vanishes. Indeed both \(\alpha^N\) and \(\beta^N\) equal one, and they cannot both equal one except at the origin. The product with minus signs has neither denominator zero, since \(-\alpha=-1\) or \(-\beta=-1\) would force an odd sum or a difference of magnitude \(N\). Simplifying yields
\[
\Lambda_N(k,\ell)=\frac{(-1)^k}{2\cos(\pi(k+\ell)/(2N))\cos(\pi(k-\ell)/(2N))}
=\frac{(-1)^k}{\cos(\pi k/N)+\cos(\pi\ell/N)}.
\]
If \(k+\ell\) is odd, \(A(-\alpha)A(-\beta)=0\): when one factor's base equals one the other factor vanishes. The other product is defined by ordinary geometric sums (neither \(\alpha\) nor \(\beta\) equals one), and hence
\[
\Lambda_N(k,\ell)=\frac{(-1)^{k+1}}{2\sin(\pi(k+\ell)/(2N))\sin(\pi(k-\ell)/(2N))}
=\frac{(-1)^{k+1}}{\cos(\pi\ell/N)-\cos(\pi k/N)}.
\]
These formulas also prove their denominators cannot be zero: equality of two cosine values would force \(k=\ell\), incompatible with odd sum, while opposite cosine values would force \(k+\ell=N\), incompatible with even sum. At the origin the original geometric sum directly gives \(\Lambda_N(0,0)=(N^2+1)/2\).

**3. Exact smallest multiplier and equality modes.** Put \(c=\cos(\pi/N)>0\). For any \(j\in\{1,\ldots,N-1\}\), \(|\cos(\pi j/N)|\le c\). Thus if neither frequency is zero, either denominator in step 2 has absolute value at most \(2c\), with equality only when both frequencies are in \(\{1,N-1\}\) and the cosine signs match the indicated sum or difference. If one frequency is zero and the other is nonzero even, the denominator has modulus \(1+\cos(\pi j/N)\le1+\cos(2\pi/N)=2c^2<2c\). If the nonzero frequency is odd, its denominator has modulus \(1-\cos(\pi j/N)\le1+\cos(2\pi/N)=2c^2<2c\), because \(j\le N-2\). Consequently every nontrivial Fourier coefficient has absolute value at least \(1/(2c)\), with equality at exactly the four listed modes. The origin has multiplier \((N^2+1)/2>1/(2c)\), so cannot be another minimizer.

**4. Operator conclusion.** The finite Fourier transform diagonalizes \(T_N\) with eigenvalues \(\Lambda_N(k,\ell)\). Since the character basis is orthogonal and all multipliers are nonzero, \(T_N\) is invertible and its inverse Hilbert-space norm is the reciprocal of the least modulus. The triangle inequality gives \(|\Lambda_N(k,\ell)|\le|B_N|\) with equality at the origin, yielding the stated largest singular value and condition number.

## Verification

`check_lee.py` independently builds the Boolean Lee-ball array and compares its two-dimensional numerical FFT against the closed formulas for the 50 odd orders \(N=3,5,\ldots,101\), covering 176,850 individual frequency comparisons. It checks the exact identity for ball cardinality, the four predicted minimizer indices, and the condition-number expression at numerical tolerance. Run `python check_lee.py` with NumPy. Finite floating-point experiments corroborate the computations but do not prove the universal assertion, which is supplied by the argument above.

## Relationship to prior work

Xiao and Zhou (2026) investigate Lee-ball lattice tilings using Q-polynomials and group-ring equations. Their abstract does not state the present square-torus, half-radius Fourier multiplier and exact inverse-conditioning classification; the full manuscript could not be inspected. Guo et al. (2026), whose substantive sections on the joint Lee metric and discrete rhombus error supports were inspected, motivate cyclic Lee balls in qudit error models but analyze stabilizer codes and error correction rather than the spectrum of the ball's unweighted convolution operator. Existing related indexed results include an exact positive-definite Turán mass for a *fixed radius-two* Lee ball on a finite torus, and arithmetic Fourier support for a *four-dimensional continuous* cross-polytope; neither implication yields the present all-odd-order inverse norm or its equality modes. The rotated-square and geometric-sum methods are elementary established tools, not claimed as new in isolation.

## Limitations

The result concerns the single critical radius \((N-1)/2\), dimension two, and the unweighted kernel. Its behavior under smaller radii, higher dimensions, unequal coordinate weights or non-Hilbert endpoint norms remains unproved. Literature checks cannot exclude older equivalent Fourier evaluations, notably via cyclic convolution or Lee-ball group-ring identities; the 2026 Xiao–Zhou primary full text was unavailable. Numerical verification uses floating-point FFT and is not an independent proof. The result has not undergone independent mathematical audit.

## References

1. Ang Xiao and Yue Zhou, *On the Lattice Tilings by Lee Balls: Q-Polynomials, Group-Ring Equations, and a Decision Algorithm*, arXiv:2610.19775, first posted 2026-10-14, https://arxiv.org/abs/2610.19775.
2. Jinkang Guo, Yiqiu Han, Aranya Chakraborty, Shubham P. Jain, Tianhao Liu, Victor V. Albert, and Andrew Lucas, *Quantum codes in the Lee metric*, arXiv:2610.04834, https://arxiv.org/abs/2610.04834; readable full-text mirror https://www.paperpeel.com/paper/2610.04834.
3. *Exact divisibility threshold for the Turán mass of a cyclic Lee two-ball*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-divisibility-threshold-for-the-tur-n-mass-of-a-cyclic-lee--6818c6c3e94b.
4. *Arithmetic Fourier support and three-level lattice coverage of the four-dimensional cross-polytope*, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-arithmetic-fourier-support-and-three-level-lattice-coverage-of-t--313db71ad1f7.
