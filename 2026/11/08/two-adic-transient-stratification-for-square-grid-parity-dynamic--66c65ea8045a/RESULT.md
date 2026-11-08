# Two-adic transient stratification for square-grid parity dynamics

## Finding

Let \(n\ge 2\) and \(q=2^f\), where \(f\ge1\). On the open square grid \(P_n\square P_n\), update all vertex values in \(\mathbb F_q\) simultaneously by summing the four available nearest-neighbor values, with no self term and zero exterior boundary. Denote this linear map by \(B_n\), and define the **first periodic-entry time** \(T(x)\) as the smallest \(t\ge0\) for which \(B_n^t x\) belongs to a periodic orbit.

Factor \(n+1=hu\), where \(h=2^{\nu_2(n+1)}\) and \(u\) is odd. Over an algebraic closure, the **complete nilpotent zero-eigenvalue Jordan structure** of \(B_n\) is
\[
\begin{cases}
J_2(0)^{\oplus(u-1)},&h=1,\\[3pt]
J_1(0)\oplus J_h(0)^{\oplus(h-2)}\oplus J_{2h}(0)^{\oplus h(u-1)},&h\ge2.
\end{cases}
\]
All nonzero-eigenvalue primary components are invertible and hence periodic over the finite field. Put
\[
K=(h-1)^2+2h^2(u-1),\qquad R=n^2-K.
\]
For \(t\ge0\), define
\[
d_t=\begin{cases}
(u-1)\min(t,2),&h=1,\\[3pt]
\min(t,1)+(h-2)\min(t,h)+h(u-1)\min(t,2h),&h\ge2.
\end{cases}
\]
Then, **for every** integer \(t\ge0\),
\[
\#\{x:T(x)\le t\}=q^{R+d_t},\qquad
\#\{x:T(x)=t\}=q^{R+d_t}-q^{R+d_{t-1}}\quad(t\ge1).
\]
In particular, the zero-eigenvalue generalized eigenspace has dimension \(K\), exactly \(q^R\) configurations are periodic at time zero, and the sharp maximum entry time is
\[
T_{\max}=\begin{cases}
h,&u=1,\\
2h,&u>1.
\end{cases}
\]
(The case \(u=1\) and \(n\ge2\) forces \(h\ge4\).) When \(u>1\), the proportion requiring this maximum time is \(1-q^{-h(u-1)}\); when \(u=1\), it is \(1-q^{-(h-2)}\). Finally, the single-step nullity is universally
\[
\dim\ker B_n=n.
\]
This last identity is known from earlier square-grid adjacency nullity theory and is included as a consistency consequence, not claimed as a new discovery.

## Assumptions and scope

The graph has vertex set \(\{1,\ldots,n\}^2\), with an edge when exactly one coordinate changes by one. At a boundary vertex, sum only actual neighbors. A period may have arbitrary length on the invertible primary component; **no classification of those eventual primitive periods** is asserted. A vector is periodic under a finite-field linear operator exactly when its projection onto the zero-eigenvalue generalized eigenspace vanishes. The theorem applies to all finite fields of characteristic two; its nilpotent Jordan multiplicities are unchanged after passing to any such extension field.

## Proof

**1. Path polynomial and root multiplicities.** Let \(A_n\) be the open-path adjacency matrix. The basis vector at one endpoint is cyclic: successive vectors \(e_1,A_ne_1,\ldots,A_n^{n-1}e_1\) have successively new terminal coordinates equal to one. Thus the minimal and characteristic polynomials coincide. Writing \(p_0(z)=1\), \(p_1(z)=z\) and \(p_j(z)=z p_{j-1}(z)+p_{j-2}(z)\), a tridiagonal determinant expansion shows that both polynomials are \(p_n(z)\).

Let \(h=2^a\) and \(n+1=hu\) with \(u\) odd. By the characteristic-two Chebyshev identity (or by representing \(z=\alpha+\alpha^{-1}\)),
\[
p_n(z)=z^{h-1}p_{u-1}(z)^h.
\]
Since \(u-1\) is even, \(p_{u-1}(z)=g_u(z)^2\), with \(g_u\) monic of degree \((u-1)/2\). The polynomial \(g_u\) is squarefree, and \(g_u(0)\ne0\): the nonzero roots of \(p_{u-1}\) are exactly the distinct values \(\alpha+\alpha^{-1}\) as \(\alpha\) ranges over nonidentity \(u\)-th roots of unity, identified under inversion. Because \(u\) is odd, these roots of unity are distinct; \(\alpha+\alpha^{-1}\) has no further identifications except inversion, and \(p_{u-1}(0)=1\). Comparing degrees shows that each such root of \(p_{u-1}\) has multiplicity exactly two. Consequently
\[
p_n(z)=z^{h-1}g_u(z)^{2h}.
\]
There is a single path Jordan block of size \(h-1\) at eigenvalue zero when \(h\ge2\), and one block of size \(2h\) at each of the \((u-1)/2\) distinct nonzero roots of \(g_u\). When \(h=1\), the zero-root block is absent. This description remains true after scalar extension to an algebraic closure.

**2. Square-grid diagonal root sectors.** The update matrix is the Kronecker sum
\[
B_n=A_n\otimes I_n+I_n\otimes A_n.
\]
Over an algebraic closure, its path-root pair \((\lambda,\mu)\) has eigenvalue \(\lambda+\mu\). In characteristic two this is zero precisely when \(\lambda=\mu\). Every unequal-root sector is invertible, so only equal-root sectors contribute to transients. If the path Jordan block for \(\lambda\) has length \(e\), the equal-root sector is multiplication by \(x+y\) on
\[
\overline{\mathbb F}_q[x,y]/(x^e,y^e).
\]

**3. Two local Jordan calculations.** For \(e=2^b\), the change of variables \(z=x+y\) gives an isomorphism
\[
\overline{\mathbb F}_q[x,y]/(x^e,y^e)
\cong\overline{\mathbb F}_q[z,y]/(z^e,y^e),
\]
because \((z+y)^e=z^e+y^e\). Hence multiplication by \(z\) has exactly \(e\) Jordan blocks of length \(e\).

For \(e=h-1\) with \(h=2^a\ge2\), put \(S=\overline{\mathbb F}_q[x,y]/(x^{h-1},y^{h-1})\). Here \(z^h=x^h+y^h=0\). When \(h>2\), the \(h-2\) vectors
\[
z^{h-1},\quad z^{h-1}x,\quad\ldots,\quad z^{h-1}x^{h-3}
\]
are nonzero and independent: their total degrees are distinct, and each contains the surviving monomial \(x^{j+1}y^{h-2}\) for its respective index \(j\), because all binomial coefficients in \((x+y)^{h-1}\) are odd. Thus multiplication by \(z\) has at least \(h-2\) blocks of length \(h\). Their combined dimension is \(h(h-2)\), whereas \(\dim S=(h-1)^2=h(h-2)+1\). There is therefore exactly one additional block of length one. The same conclusion for \(h=2\) follows directly from \(S\cong\overline{\mathbb F}_q\).

**4. Assemble the Jordan blocks.** There are \((u-1)/2\) distinct nonzero path roots, each with block length \(2h\). Step 3 supplies \(2h\) grid blocks of size \(2h\) per nonzero root, hence \(h(u-1)\) such blocks in total. The zero path root, when present, contributes one block of size one and \(h-2\) blocks of size \(h\). This proves the asserted complete zero-eigenvalue Jordan form, including its boundary cases. Summing block lengths gives \(K\). Summing block counts gives \(n\), independently recovering the established square-grid nullity.

**5. Entry times and populations.** Fitting decomposition splits the state space as an invariant nilpotent sector of dimension \(K\) and an invariant invertible sector of dimension \(R\). Since the latter is a finite set on which the map acts bijectively, every vector in it is periodic. A vector enters a periodic orbit by time \(t\) if and only if the nilpotent projection is killed by \(B_n^t\). A Jordan block of length \(s\) contributes \(\min(t,s)\) to \(\dim\ker B_n^t\). Summing the blocks gives exactly \(d_t\), yielding \(q^{R+d_t}\) states entering by time \(t\) and the difference formula for exact entry time. The largest nilpotent block has length \(h\) when \(u=1\), and \(2h\) when \(u>1\); these are present in the stated ranges. The final nonzero entry layer is determined by the number of maximal-length blocks, giving both sharpness and the stated probability formulas.

For illustration: at \(n=5\), \(h=2\), \(u=3\), the nilpotent type is \(J_1(0)\oplus J_4(0)^{\oplus4}\), the periodic sector has dimension eight, and the cumulative entry populations are \(q^8,q^{13},q^{17},q^{21},q^{25}\) at times zero through four. At \(n=7\), \(h=8\), \(u=1\), the entire map is nilpotent, with type \(J_1(0)\oplus J_8(0)^{\oplus6}\), and the sharp extinction time is eight.

## Verification

The included Python 3 scripts use only the standard library. Run `python check_grid.py` to construct the exact binary adjacency operator independently for each square side \(2\le n\le18\) and compare all predicted nullities through two iterates past the sharp cutoff (121 comparisons). Run `python check_algebra.py` to verify the polynomial factorization and squarefreeness for \(2\le n\le129\) (384 checks) and the truncated two-variable multiplication ranks through \(h=16\) (68 checks). Both captured outputs end in `ALL PASS`. These finite tests corroborate the proof but do not replace the all-size arguments above.

## Relationship to prior work

The classical open-neighbor square-grid nullity \(\dim\ker B_n=n\) is already implied by the path-Chebyshev gcd formula; Yamagishi (2015, Theorem 1.1 and Corollary 4.1) explicitly recovers that result and identifies its earlier sources. Peters, Goldwasser and Young (2017), and Curtis, Earl, Livingston and Shader (2018), study invertibility and zero-eigenspace dimensions for Cartesian graph products. Boyles (2022) treats the **shifted** adjacency \(B_n+I\) in the Lights Out problem. None of these inspected statements gives the higher kernels \(\dim\ker B_n^t\), the complete zero-primary Jordan partition, or the exact entry-time census. The 2014 Glasby–Praeger–Xia modular Jordan-partition framework concerns general tensor products of Jordan blocks; its local algebra is compatible with the ingredients here but does not state the present all-side-length grid result. An earlier calculation treated the unmodified square grid only at side lengths \(2^a-1\), in connection with a one-corner feedback perturbation; that restricted uniform case is not asserted to be new here.

## Limitations

The theorem does not enumerate the primitive periods or distinct periodic cycles on the invertible sector, nor does it classify nonsquare rectangular grids. Its new content is the complete zero-primary Jordan structure and exact first-periodic-entry distribution for all square side lengths. Related older articles by Sutner (2000) and Hunziker–Machiavelo–Park (2004) could not be accessed in full during the comparison; their publicly available descriptions emphasize Chebyshev/divisibility or reversibility and do not resolve the historical-priority risk. No independent audit or external certification is claimed.

## References

- M. Yamagishi, *Periodic harmonic functions on lattices and Chebyshev polynomials*, Linear Algebra Appl. **476** (2015), 1–15, doi:10.1016/j.laa.2015.03.004. Author manuscript: https://nitech.repo.nii.ac.jp/record/6000/files/YamagishiMasakazu_2014_A1.pdf .
- T. Peters, J. Goldwasser, M. Young, *Lights Out! on Cartesian Products*, Electron. J. Linear Algebra **32** (2017), doi:10.13001/1081-3810.3483. https://journals.uwyo.edu/index.php/ela/article/view/1801 .
- B. Curtis, J. Earl, D. Livingston, B. Shader, *Resolution of Conjectures related to Lights Out! and Cartesian Products*, Electron. J. Linear Algebra **34** (2018), doi:10.13001/1081-3810.3722. https://journals.uwyo.edu/index.php/ela/article/view/1941 .
- W. Boyles, *Resolution to Sutner's Conjecture*, arXiv:2202.09878 (first public version 20 February 2022), https://arxiv.org/html/2202.09878v3 .
- S. P. Glasby, C. E. Praeger, B. Xia, *Decomposing modular tensor products, and periodicity of Jordan partitions*, arXiv:1401.2748 (first public version 13 January 2014), https://arxiv.org/abs/1401.2748 .
- K. Sutner, *σ-Automata and Chebyshev-Polynomials*, Theor. Comput. Sci. **230** (2000), 49–73, doi:10.1016/S0304-3975(97)00242-9 (full text not inspected).
- M. Hunziker, A. Machiavelo, J. Park, *Chebyshev polynomials over finite fields and reversibility of σ-automata on square grids*, Theor. Comput. Sci. **320** (2004), 465–483, doi:10.1016/j.tcs.2004.03.031 (full text not inspected).
