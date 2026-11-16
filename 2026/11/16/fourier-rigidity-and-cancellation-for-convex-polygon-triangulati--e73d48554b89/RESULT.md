# Fourier rigidity and cancellation for convex-polygon triangulations

## Finding

For every integer \(N\geq3\), label a convex \(N\)-gon by \(0,1,\ldots,N-1\) counterclockwise. Let \(E_N\) be its set of nonboundary diagonals, let \(\mathcal T_N\) be its triangulations, and identify each triangulation with the binary incidence vector of its diagonals in \(\mathbb F_2^{E_N}\). For any frequency \(b\in\mathbb F_2^{E_N}\), define the **unnormalized** Walsh coefficient
\[
W_N(b)=\sum_{T\in\mathcal T_N}(-1)^{\sum_{e\in E_N}b_e\mathbf 1_{e\in T}}.
\]
Let \(C_j=\binom{2j}{j}/(j+1)\) and let \(s_2(m)\) be the number of ones in the binary expansion of \(m\). The following three statements hold.

1. The explicit frequency \(b^{\mathrm{alt}}\), with \(b^{\mathrm{alt}}_{(i,j)}=1\) precisely for diagonals \(i<j\) whose **smaller** endpoint \(i\) is even, has coefficient
\[
W_N(b^{\mathrm{alt}})=\begin{cases}0,&N\text{ even},\\ C_{(N-3)/2},&N\text{ odd}.\end{cases}
\]
2. For **every odd** \(N\ge3\) and **every** binary frequency \(b\),
\[
W_N(b)\equiv C_{N-2}\pmod4.
\]
Consequently, if \(s_2(N-1)=1\), all coefficients are odd; if \(s_2(N-1)=2\), all coefficients are congruent to \(2\) modulo \(4\). In particular the triangulation-indicator convolution operator on \(\mathbb F_2^{E_N}\) is invertible for every odd \(N\) with \(s_2(N-1)\le2\), **including infinitely many cases where the number \(C_{N-2}\) of triangulations is even**. In the two-bit cases every Fourier multiplier has absolute value at least \(2\).
3. The first odd polygon with a zero Walsh coefficient has \(15\) vertices. One explicit zero frequency is obtained by taking \(b^{\mathrm{alt}}\) for \(N=15\) and toggling its coordinates corresponding to diagonals \((0,8)\) and \((2,6)\). Its coefficient is exactly zero.

The statements provide sufficient zero-free and singular families; no complete classification is claimed for odd \(N\) satisfying \(s_2(N-1)\ge3\).

## Assumptions and scope

All diagonal coordinates are binary and all triangulations have coefficient \(1\). Every boundary side is **excluded** from \(E_N\). The end-points of diagonals are ordered by their integer labels; this determines the stated alternating frequency, which is not asserted to be invariant under dihedral relabeling. A triangulation has exactly \(N-3\) diagonals. Fourier transforms and convolutions use counting measure and the unnormalized character convention above. Thus the eigenvalues of convolution by the indicator of \(\mathcal T_N\) are exactly \(W_N(b)\), for all \(b\in\mathbb F_2^{E_N}\).

## Proof

**Alternating-sign identity.** Put \(s_i=-1\) when \(i\) is even and \(s_i=1\) when \(i\) is odd. Temporarily assign weight \(s_i\) to **every** polygon edge \((i,j)\) with \(i<j\), including boundary sides. Let \(H(i,j)\) be the sum, over all triangulations of the consecutive-vertex subpolygon \(i,i+1,\ldots,j\), of the product of the weights of **all** its edges (the boundary counted once). For \(j=i+1\) put \(H(i,i+1)=s_i\). Decomposing at the triangle incident with \((i,j)\) gives, for \(j\ge i+2\),
\[
H(i,j)=s_i\sum_{k=i+1}^{j-1}H(i,k)H(k,j).
\]
This recurrence does not double-count any edge: the root edge is counted by \(s_i\), while the two child-root edges belong to different child subpolygons.

Write \(E_L=H(i,i+L)\) for even \(i\), and \(O_L=H(i,i+L)\) for odd \(i\). These depend only on the indicated parity and the distance. The base cases satisfy \(E_1=-1\), \(O_1=1\). Induction in the recurrence proves \(O_L=-E_L\) for all \(L\ge1\). Consequently
\[
E_L=-\sum_{t=1}^{L-1}(-1)^tE_tE_{L-t}\quad(L\ge2).
\]
Set \(U(z)=\sum_{L\ge1}E_Lz^L\). The recurrence is equivalent as a formal-power-series identity to
\[
U(z)=-z-U(-z)U(z),\qquad U(-z)=z-U(z)U(-z).
\]
Subtracting gives \(U(z)-U(-z)=-2z\), so \(E_L=0\) for every odd \(L\ge3\). If \(R(z)=(U(z)+U(-z))/2\), then \(R(z)^2+R(z)=z^2\) and \(R(0)=0\), whence
\[
R(z)=\frac{\sqrt{1+4z^2}-1}{2}=\sum_{m\ge1}(-1)^{m-1}C_{m-1}z^{2m}.
\]
It follows that \(E_{2m}=(-1)^{m-1}C_{m-1}\). The product of the weights on all boundary sides of the original \(N\)-gon is a constant \(B_N\in\{\pm1\}\), independent of its triangulation. Hence \(H(0,N-1)=B_NW_N(b^{\mathrm{alt}})\). For even \(N\), \(N-1\ge3\) is odd, giving zero. For odd \(N=2m+1\), the boundary product is \(B_N=(-1)^{m+1}\) and \(H(0,N-1)=E_{2m}=(-1)^{m-1}C_{m-1}\). Their quotient is \(C_{m-1}\). This proves statement 1.

**Uniform odd-polygon congruence.** Fix an odd \(N\) and a diagonal \(e=(i,j)\) with \(0\le i<j<N\). It divides the polygon into pieces with \(a+2\) and \(b+2\) vertices, where \(a=j-i-1\), \(b=N-j+i-1\), both at least \(1\), and \(a+b=N-2\) is odd. Exactly \(C_aC_b\) triangulations contain \(e\). The classical Catalan parity criterion says that \(C_k\) is odd precisely when \(k=2^h-1\) for some integer \(h\ge0\). For positive \(a,b\), both being Catalan-odd would force both indices odd, contradicting the oddness of \(a+b\). Thus **every diagonal belongs to an even number of triangulations**.

Let \(S\subseteq E_N\) be the negative diagonals of any frequency. Reducing the sign sum modulo \(4\) gives
\[
W_N(\mathbf1_S)\equiv C_{N-2}-2\sum_{T\in\mathcal T_N}|S\cap D(T)|\pmod4,
\]
where only the parity of each intersection size matters. Reversing the finite sums, \(\sum_T|S\cap D(T)|=\sum_{e\in S}C_{a(e)}C_{b(e)}\) is even. Therefore \(W_N(b)\equiv C_{N-2}\pmod4\), uniformly in \(b\). The standard Catalan valuation identity \(v_2(C_j)=s_2(j+1)-1\), applied to \(j=N-2\), gives the two zero-free cases. Convolution invertibility follows by character diagonalization; the asserted modulus-two spectral gap follows from nonzero integers congruent to \(2\) modulo \(4\).

**First odd singular example.** For \(N=15\), put \(S_0=\{(i,j)\in E_{15}:i\text{ even}\}\), \(e=(0,8)\), and \(f=(2,6)\). The alternating coefficient is \(W_{15}(\mathbf1_{S_0})=C_6=132\). The exact signed sums over triangulations containing respectively \(e\), \(f\), and both are \(50\), \(56\), and \(20\), with signs determined by \(S_0\). These three integers follow directly from the triangle-decomposition recurrence in `checker.py`, and can be checked by substituting a formal variable in the indicated edge weights. Toggling both signs therefore yields
\[
132-2(50)-2(56)+4(20)=0.
\]
All smaller odd lengths \(3,5,7,9,11,13\) have \(s_2(N-1)\le2\), and are zero-free by the preceding congruence. Thus \(15\) is the first odd singular case, as claimed.

## Verification

Run `python checker.py` using Python 3.9 or newer. The checker uses exact integers throughout, no dependencies, and no floating point. It independently enumerates triangulations for \(3\le N\le9\) and compares their signed sums with the interval recurrence at random frequencies; verifies the alternating identity through \(N=30\); checks the modulo-four congruence at random frequencies in odd lengths through \(N=31\); exhaustively computes all \(2^{14}\) coefficients for the heptagon; and verifies the explicit \(15\)-gon zero witness. The formal-power-series argument and Catalan parity/valuation identities, not the finite computation, establish the infinite claims.

## Relationship to prior work

The Catalan triangulation count and triangle-splitting recurrence are classical. Regev (arXiv:1208.3915, first version 2012-08-20) studies the distribution of diagonals parallel to a fixed edge; the full text's Theorems 2 and 4 address those direction-specific counts, not Walsh transforms for arbitrary independently signed diagonals. Postnikov and Sagan (arXiv:math/0601339, first version 2006-01-13), Theorem 1.1, gives the Catalan two-adic valuation used above. Their weighted-Catalan work treats Dyck-path height weights satisfying a divisibility condition, not the unrestricted diagonal sign system here. Reifegerste (arXiv:math/0305327, first version 2003-05-23), Theorem 1.1, proves a numerically analogous sign-balance for 321-avoiding permutations; it does not identify the polygon diagonal incidence frequency or give an all-frequency mod-four obstruction. A separate published study of correlations between diagonals in uniform polygon triangulations discusses compatible-family counts, which may supply an alternative path to the single-diagonal counting premise but does not, in its accessible summary, give the present Fourier classification. A previous Fourier theorem for noncrossing *perfect matchings* uses different supports and does not imply the polygon-triangulation statement.

## Limitations

For odd \(N\) with \(s_2(N-1)\ge3\), no uniform invertibility or singularity classification is asserted. The value \(15\) is only the **first odd** singular case; even polygons are already singular from \(N=4\). No full Walsh-magnitude distribution, exact nullity, or sharp inverse norm is established beyond the stated lower gaps. A bounded literature comparison cannot rule out a historical signed-triangulation identity under another parametrization or a consequence hidden in a comprehensive face-enumeration formula. The scientific proof and computations have not received independent audit.

## References

- A. Regev, *Enumerating triangulations by parallel diagonals*, arXiv:1208.3915 (2012-08-20), https://arxiv.org/abs/1208.3915 .
- A. Postnikov and B. E. Sagan, *What power of two divides a weighted Catalan number?*, arXiv:math/0601339 (2006-01-13), https://arxiv.org/abs/math/0601339 .
- A. Reifegerste, *Refined sign-balance on 321-avoiding permutations*, arXiv:math/0305327 (2003-05-23), https://arxiv.org/abs/math/0305327 .
