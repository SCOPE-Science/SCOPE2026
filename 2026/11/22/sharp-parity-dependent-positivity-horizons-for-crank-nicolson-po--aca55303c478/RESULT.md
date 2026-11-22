# Sharp parity-dependent positivity horizons for Crank–Nicolson powers on stars

## Finding
Let \(m\ge2\) be an integer, let \(L_m\) be the unweighted Laplacian of the star \(K_{1,m}\), and let \(h>0\). With \(C_m(h)=(I+hL_m/2)^{-1}(I-hL_m/2)\), every off-diagonal entry of \(C_m(h)^k\) is **strictly positive** for all integers \(k\ge1\). For even \(k\), the entire matrix is strictly positive for every finite \(h>0\). For odd \(k\), it is entrywise nonnegative **if and only if**
\[
0<h\le H_{m,k}=\frac{2(1+m^{-1/k})}{(m+1)(1-m^{-1/k})}.
\]
At equality, the hub diagonal alone is zero; beyond the threshold, it alone is negative. In particular, after exactly two equal large steps the completed map is strictly positive although the intermediate one-step map is not. The sharp odd-power horizons grow strictly with odd \(k\), with \(H_{m,k}=4k/((m+1)\log m)+O_m(1)\) as \(k\to\infty\).

## Assumptions and scope
The star has vertices \(0,1,\ldots,m\), hub \(0\), unit conductances on \(\{0,i\}\), and no other edges. Powers are taken of the **same** fixed-step completed Crank–Nicolson matrix, in exact arithmetic; the displayed positivity refers to the final product, not each intermediate step. The update is symmetric and has unit row sums, but a negative entry is possible for an odd power. Strict positivity is asserted for finite \(h>0\), not uniformly as \(h\to\infty\). Integers \(m\ge2\) and \(k\ge1\) are arbitrary.

## Proof
Let \(J_m\) be the all-ones matrix on the leaves and let \(P_0=J_{m+1}/(m+1)\). Define the leaf-difference projection \(P_1=\operatorname{diag}(0,I_m-J_m/m)\) and \(P_2=I-P_0-P_1\). These are mutually orthogonal projectors, and the star Laplacian is \(L_m=P_1+(m+1)P_2\). Put
\[
a=\frac{2-h}{2+h},\qquad b=\frac{2-(m+1)h}{2+(m+1)h}.
\]
Then \(-1<b<a<1\), and exact spectral calculus gives \(C_m(h)^k=P_0+a^kP_1+b^kP_2\). The four entry types are
\[
\begin{aligned}
(C^k)_{00}&=\frac{1+mb^k}{m+1},\\
(C^k)_{0i}&=\frac{1-b^k}{m+1},\\
(C^k)_{ii}&=\frac{m+(m^2-1)a^k+b^k}{m(m+1)},\\
(C^k)_{ij}&=\frac{m-(m+1)a^k+b^k}{m(m+1)}\quad(i\ne j,\ i,j\ge1).
\end{aligned}
\]
The hub–leaf terms are strictly positive because \(|b|<1\). For the leaf–leaf off-diagonals use the following scalar fact, valid for **every** integer \(k\ge1\):
\[
F_k(z)=\frac{1-[(1-z)/(1+z)]^k}{z}\quad\text{is strictly decreasing for }z>0.
\]
For \(0<z<1\), the function \(f(z)=((1-z)/(1+z))^k\) is strictly convex, since \(f''(z)=4k((1-z)/(1+z))^{k-2}(k-z)/(1+z)^4>0\); hence the secant slope \((1-f(z))/z\) strictly decreases. For \(z>1\), set \(t=(z-1)/(z+1)\). If \(k\) is even, \((1-t^k)/z\) strictly decreases. If \(k\) is odd, the expression is \((1+t^k)/z\); indeed,
\[
z\frac{d(t^k)}{dz}=\frac{k}{2}(1-t^2)t^{k-1}\le k(1-t)t^{k-1}\le1-t^k<1+t^k,
\]
so its derivative is strictly negative. Continuity at \(z=1\) completes the lemma. Apply it at \(z=h/2\) and \((m+1)z\):
\[
(m+1)(1-a^k)>1-b^k,
\]
which is exactly the strict positivity of the leaf–leaf off-diagonal.

For even \(k\), both \(a^k\) and \(b^k\) are nonnegative, so the two displayed diagonal entries are positive. For odd \(k\), the leaf diagonal exceeds the hub diagonal by
\[
(C^k)_{ii}-(C^k)_{00}=\frac{m-1}{m}(a^k-b^k)>0.
\]
Thus the hub diagonal alone controls nonnegativity. As \(h\) increases, \(b\) decreases strictly from \(1\) to \(-1\), and odd powers preserve that order. Consequently \(1+mb^k\) crosses zero exactly once, at \(b=-m^{-1/k}\). Solving for \(h\) gives the displayed \(H_{m,k}\). At the unique boundary all other entries are positive. Since \(m^{-1/k}\) strictly increases with \(k\), the threshold strictly increases. Writing \(m^{-1/k}=e^{-(\log m)/k}\) gives \(H_{m,k}=(2/(m+1))\coth((\log m)/(2k))=4k/((m+1)\log m)+O_m(1/k)\), which proves the weaker displayed \(O_m(1)\) estimate.

The conclusion is genuinely graph-specific. On the four-vertex path with unit edge conductances, direct exact inversion at \(h=30\) gives \((C(30)^2)_{01}=-5111040/250937281<0\).

## Verification
The accompanying standalone `verify.py` independently inverts rational Crank–Nicolson matrices on stars with two through eight leaves and computes their first nine powers. Seven exact rational timesteps are tested for each star size, verifying all four spectral entry formulas and strict off-diagonal positivity against exact matrix products. It also computes and confirms the four-vertex-path counterexample using rational arithmetic. The checker reports `VERIFY_OK 33958`. The infinite-family claims, strict inequalities and threshold uniqueness are established by the displayed proof rather than finite tests.

## Relationship to prior work
The Cayley transform and its connection with positivity classes of matrices are classical (Fallat–Tsatsomeros 2002). Absolute monotonicity and positivity constraints for rational Runge–Kutta maps are also well developed (Lóczi–Ketcheson 2013). Existing exact work on reversible Markov generators determines the **one-step** nonnegativity criterion, and weighted-star Crank–Nicolson work specializes this to hub-controlled one-step thresholds. A stronger general result for continuous spectral filters on unweighted complete multipartite graphs **already implies** unconditional nonnegativity of **even powers** here, since their scalar multiplier is nonnegative and the required divided difference decreases. We do not claim the even-power positivity consequence independently as new. The distinguishing assertion is the **complete parity-sensitive, all-odd-power sharp threshold**, strict off-diagonal statements and isolation of the sole possible negative entry. A prior exact power classification for **directed cycles** does not imply the undirected-star classification: different generators, multiplicities and transition signs occur. No unrestricted-graph claim is made.

## Limitations
This is a narrow unweighted star result; unequal conductances and arbitrary trees are not classified. The counterexample on a unit four-path shows unconditional even-power positivity is not automatic on trees. The completed even-power map may be stochastic despite invalid intermediate odd iterates; it is not an SSP or stagewise-positivity guarantee. For very large steps, the even-power map tends to the identity, so unconditional positivity does not imply stiff damping or high accuracy. The link with existing complete-multipartite spectral-filter results limits the independently new part of the parity classification. Equivalent statements in older matrix-function or graph-filter literature remain a bibliographic risk. No independent scientific validation is asserted.

## References
1. S. M. Fallat and M. J. Tsatsomeros, *On the Cayley transform of positivity classes of matrices*, Electronic Journal of Linear Algebra 9 (September 2002), pp. 190–196, https://journals.uwyo.edu/index.php/ela/article/download/173/173/173.
2. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651v1, submitted March 26, 2013, https://arxiv.org/abs/1303.6651.
3. *An exact positivity criterion on complete multipartite diffusion graphs*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-an-exact-positivity-criterion-on-complete-multipartite-diffusion--690509e7de2b.
4. *Sharp positivity horizon and homogenization extremum for weighted-star Crank–Nicolson steps*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-positivity-horizon-and-homogenization-extremum-for-weighte--2ba13f6aa0a6.
5. *Two-step positivity and a three-state parity exception for cyclic Crank–Nicolson*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-two-step-positivity-and-a-three-state-parity-exception-for-cycli--5dc6def72908.
