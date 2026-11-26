# Sharp parity-dependent positivity horizons for Crank–Nicolson powers on stars

## Finding

Let \(m\ge2\), let \(L_m\) be the unweighted Laplacian of the star \(K_{1,m}\), and put \(C_m(h)=(I+hL_m/2)^{-1}(I-hL_m/2)\), for \(h>0\). For every integer \(k\ge1\), all off-diagonal entries of \(C_m(h)^k\) are strictly positive. For even \(k\), all entries are strictly positive for every finite \(h>0\). For odd \(k\), the matrix is entrywise nonnegative if and only if
\[
0<h\le H_{m,k}=\frac{2(1+m^{-1/k})}{(m+1)(1-m^{-1/k})}.
\]
At \(H_{m,k}\) the hub diagonal alone vanishes. For \(h>H_{m,k}\) the hub diagonal is negative. The common leaf diagonal vanishes at a second, strictly larger unique threshold \(D_{m,k}\), characterized by
\[
m+(m^2-1)\left(\frac{2-D_{m,k}}{2+D_{m,k}}\right)^k
+\left(\frac{2-(m+1)D_{m,k}}{2+(m+1)D_{m,k}}\right)^k=0.
\]
Thus the hub diagonal is the only negative entry exactly for \(H_{m,k}<h\le D_{m,k}\), and every diagonal is negative for \(h>D_{m,k}\). For example, at \((m,k,h)=(2,1,6)\) the diagonal entries are \(-1/5,-1/20,-1/20\). Two equal steps always have a strictly positive completed map, even when the intermediate map has negative diagonal entries. The odd-power horizons \(H_{m,k}\) increase strictly with odd \(k\) and are \(4k/((m+1)\log m)+O_m(k^{-1})\).

## Assumptions and scope

The vertices are \(0,1,\ldots,m\), with hub \(0\) and unit conductances on \(\{0,i\}\). All powers use the same timestep and concern the final map in exact arithmetic, not an intermediate diffusion iterate. The matrix is symmetric and has row sums one. Strict positivity at even powers is not uniform as \(h\to\infty\).

## Proof

Let \(J_d\) be the \(d\)-by-\(d\) all-ones matrix. The mutually orthogonal projectors onto the constants, the leaf-difference subspace, and the remaining hub–leaf mode are respectively
\[
P_0=\frac{J_{m+1}}{m+1},\qquad P_1=\operatorname{diag}(0,I_m-J_m/m),\qquad P_2=I-P_0-P_1.
\]
The star Laplacian is \(L_m=P_1+(m+1)P_2\). Write
\[
a=\frac{2-h}{2+h},\qquad b=\frac{2-(m+1)h}{2+(m+1)h}.
\]
Then \(-1<b<a<1\) and \(E=C_m(h)^k=P_0+a^kP_1+b^kP_2\). In particular, for distinct leaves \(i,j\),
\[
\begin{aligned}
E_{00}&=\tfrac{1+mb^k}{m+1},& E_{0i}&=\tfrac{1-b^k}{m+1},\\
E_{ii}&=\tfrac{m+(m^2-1)a^k+b^k}{m(m+1)},& E_{ij}&=\tfrac{m-(m+1)a^k+b^k}{m(m+1)}.
\end{aligned}
\]
The hub–leaf entries are strictly positive since \(|b|<1\). For the leaf–leaf off-diagonal entries, set \(F_k(z)=[1-((1-z)/(1+z))^k]/z\) for \(z>0\). It is strictly decreasing: for \(0<z<1\) the function \(f(z)=((1-z)/(1+z))^k\) is strictly convex, with
\[
f''(z)=4k\left(\frac{1-z}{1+z}\right)^{k-2}\frac{k-z}{(1+z)^4}>0.
\]
Consequently the negated secant slope \((f(0)-f(z))/z\) strictly decreases. For \(z>1\), set \(t=(z-1)/(z+1)\in(0,1)\). For even \(k\), the positive numerator \(1-t^k\) decreases and the denominator increases. For odd \(k\),
\[
z\frac{d(t^k)}{dz}=\frac{k}{2}(1-t^2)t^{k-1}\le k(1-t)t^{k-1}\le 1-t^k<1+t^k,
\]
where the middle inequality follows by summing the geometric series \(1+t+\cdots+t^{k-1}\). Therefore \((1+t^k)/z\) strictly decreases. Continuity at \(1\) joins the two intervals. Applying this at \(z=h/2\) and \(z=(m+1)h/2\) gives \((m+1)(1-a^k)>1-b^k\), so \(E_{ij}>0\).

For even \(k\), each diagonal entry is positive by the entry formulas. For odd \(k\), the difference between the leaf and hub diagonals is
\[
E_{ii}-E_{00}=\frac{m-1}{m}(a^k-b^k)>0.
\]
The hub diagonal strictly decreases until its unique zero at \(b=-m^{-1/k}\), which gives \(H_{m,k}\); hence this threshold determines the first loss of entrywise nonnegativity. The leaf diagonal strictly decreases since it is a positive-weight sum of the strictly decreasing odd powers \(a^k,b^k\) and a constant. Its limits at \(0^+\) and \(+\infty\) are \(1\) and \((1-m)/(m+1)<0\), respectively. Its unique zero is therefore at \(D_{m,k}\), and the diagonal difference above gives \(D_{m,k}>H_{m,k}\). This proves the full sign classification. Also \(m^{-1/k}\) increases strictly with \(k\), and \(H_{m,k}=2\coth((\log m)/(2k))/(m+1)\), which gives the stated large-\(k\) expansion.

For contrast, even powers are not always entrywise positive on arbitrary unweighted trees. For the four-vertex path ordered along its edges, exact inversion and squaring at \(h=30\) gives \((C(30)^2)_{01}=-5111040/250937281\).

## Verification

Run `python3 verify.py` for finite checks with exact rational matrix arithmetic. The checker forms the update by direct Gauss–Jordan inversion, multiplies powers and compares all entries with the spectral formulas. It tests two exact hub thresholds, brackets the leaf threshold in the three-vertex one-step example, and checks the four-vertex-path counterexample. These tests do not prove the all-parameter statement; the divided-difference inequality, diagonal comparison and monotone crossings supply that proof.

## Relationship to prior work

The general entry formulas for spectral filters on complete multipartite graphs specialize to the four star entries above. The associated universal positivity criterion applies to the even Crank–Nicolson powers, so that case is not claimed as new. It requires nonnegative scalar multipliers and does not itself classify the odd powers, for which the scalar multiplier can be negative even when the matrix is strictly positive. Existing weighted-star results give the one-step threshold, including \(H_{m,1}=2/(m-1)\), and directed-cycle results consider a different generator. The distinguishing calculation here is the strict divided-difference bound also in the signed region for odd powers and the resulting exact nonnegativity horizon and change of diagonal sign pattern for repeated odd powers on an unweighted star.

## Limitations

No conclusion is claimed here for power positivity on stars of arbitrary conductance, for general trees, for finite-precision arithmetic or for stagewise positivity, accuracy or stiff damping. At fixed even \(k\), the large-step limit is the identity, so entrywise strict positivity of the finite completed map does not yield a positive uniform bound. Bibliographic comparison is not a claim of historical priority.

## References

1. S. M. Fallat and M. J. Tsatsomeros, *On the Cayley transform of positivity classes of matrices*, Electronic Journal of Linear Algebra **9** (2002), 190–196. https://journals.uwyo.edu/index.php/ela/article/download/173/173/173
2. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*. https://arxiv.org/abs/1303.6651
3. *An exact positivity criterion on complete multipartite diffusion graphs*. https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-an-exact-positivity-criterion-on-complete-multipartite-diffusion--690509e7de2b/RESULT.md
4. *Sharp positivity horizon and homogenization extremum for weighted-star Crank–Nicolson steps*. https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-sharp-positivity-horizon-and-homogenization-extremum-for-weighte--2ba13f6aa0a6/RESULT.md
5. *Two-step positivity and a three-state parity exception for cyclic Crank–Nicolson*. https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-two-step-positivity-and-a-three-state-parity-exception-for-cycli--5dc6def72908/RESULT.md
