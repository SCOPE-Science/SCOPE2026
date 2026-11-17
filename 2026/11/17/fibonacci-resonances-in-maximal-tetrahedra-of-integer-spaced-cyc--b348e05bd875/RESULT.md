# Fibonacci resonances in maximal tetrahedra of integer-spaced cyclic three-polytopes

## Finding

For each integer \(N\ge3\), let \(C_N\subset\mathbb R^3\) be the convex hull of the \(N+1\) points \(v(t)=(t,t^2,t^3)\), \(t=0,1,\ldots,N\), with ordinary Euclidean three-volume. Define
\[
q=\left\lfloor\frac{N}{\sqrt5}\right\rfloor,\quad
\varepsilon_y=(N-y)\bmod2\in\{0,1\},\quad
H_N(y)=\frac{Ny}{16}\big((N-y)^2-\varepsilon_y\big)\big((N+y)^2-\varepsilon_y\big).
\]
For \(1\le y\le N-2\), the quantity \(H_N(y)\) is an integer. The greatest volume of **any** tetrahedron contained in \(C_N\) is exactly
\[
\boxed{\mathcal V_N=\frac16\max_{y\in\{q,q+1\}\cap[1,N-2]}H_N(y)}.
\]
This gives a constant-time, entirely exact evaluation after computing \(q\) with integer square root. Every maximizing **vertex-supported** tetrahedron is of the form
\[
\operatorname{conv}\{v(0),v(x),v(x+y),v(N)\},\quad
x\in\left\{\left\lfloor\frac{N-y}{2}\right\rfloor,\left\lceil\frac{N-y}{2}\right\rceil\right\},
\]
where \(y\) is any maximizer in the displayed two-element candidate set. In particular the complete vertex-supported equality classification is determined by a one-dimensional threshold. For \(q+1\le N-2\), put
\[
T_N(q)=\begin{cases}
5q^2+8q+4,&N-q\text{ even},\\
5q^2+2q+1,&N-q\text{ odd}.
\end{cases}
\]
The maximizing \(y\)-value is \(q\) if \(N^2<T_N(q)\), it is \(q+1\) if \(N^2>T_N(q)\), and **both** values occur exactly when \(N^2=T_N(q)\). For \(N=3\), only \(q\) is admissible.

The tie case occurs **if and only if** \(N=F_{2m+1}\) for some integer \(m\ge2\), where \(F_j\) is the Fibonacci sequence normalized by \(F_0=0,F_1=1\). The first ties are at \(N=5,13,34,89,233,610\). At each tie there are exactly three maximizing vertex-supported tetrahedra: one symmetric under reversal of the parameter grid and two exchanged by reversal. Outside this sparse family there are one or two vertex-supported maximizers, according as \(N-y\) is even or odd for the unique optimal \(y\).

## Assumptions and scope

The vertices are embedded in the *specified* Euclidean moment-curve realization \(v(t)=(t,t^2,t^3)\), not an arbitrary affine realization of the same combinatorial cyclic polytope. The integer-grid parameter \(N\) ranges over all integers at least three. The theorem classifies **all** maximizing tetrahedra drawn from the enumerated vertices; for tetrahedra with vertices at arbitrary points of the body it determines only the maximal volume, not the complete nonvertex equality locus. No assertion about other parameter grids, higher-dimensional cyclic polytopes, or affine-invariant optimal volume ratios is made.

## Proof

**1. Vandermonde volume and endpoint rigidity.** For four distinct integers \(0\le t_0<t_1<t_2<t_3\le N\), the oriented simplex determinant with homogeneous vertex rows \((1,t,t^2,t^3)\) is the classical Vandermonde product. Thus
\[
6\operatorname{Vol}_3\big(\operatorname{conv}\{v(t_0),v(t_1),v(t_2),v(t_3)\}\big)
=\prod_{0\le i<j\le3}(t_j-t_i)>0.
\]
Replacing \(t_0\) by zero strictly increases all three factors containing \(t_0\), unless \(t_0=0\). Replacing \(t_3\) by \(N\) strictly increases all three factors containing \(t_3\), unless \(t_3=N\). Hence all vertex-tetrahedron maximizers contain \(v(0),v(N)\).

**2. Two-variable reduction and reflection.** Write the successive positive integer gaps as \(x=t_1\), \(y=t_2-t_1\), \(z=N-t_2\), so \(x+y+z=N\). The six-factor determinant becomes
\[
D_N(x,y,z)=Nxyz(x+y)(y+z)=Ny\,xz\big(xz+Ny\big).
\]
For fixed \(y\), its right-hand side increases strictly with \(p=xz>0\). With \(x+z=N-y\), the largest integer product occurs exactly at the two balanced choices \(x,z=\lfloor(N-y)/2\rfloor,\lceil(N-y)/2\rceil\), including one choice if these coincide. Because \(4xz=(N-y)^2-\varepsilon_y\) and \(4(xz+Ny)=(N+y)^2-\varepsilon_y\), the maximum fixed-gap determinant is precisely \(H_N(y)\).

**3. The two-candidate theorem.** Direct multiplication shows that for \(1\le y\le N-3\),
\[
H_N(y+1)-H_N(y)=\frac N{16}\big(N^2-(y+\delta_y)^2\big)\big(N^2-T_N(y)\big),
\]
where \(\delta_y=0\) when \(N-y\) is even, \(\delta_y=1\) otherwise, and \(T_N(y)\) has the same parity-dependent definition as above with \(q\) replaced by \(y\). The first parenthesis is strictly positive throughout the admissible range. The parity-dependent threshold is strictly increasing: consecutive increments are either \(4y+4\) or \(16y+16\), according to parity. Set \(\alpha=N/\sqrt5\) and \(q=\lfloor\alpha\rfloor\). For \(y\le q-1\),
\[
T_N(y)\le5y^2+8y+4\le5(\alpha-1)^2+8(\alpha-1)+4=N^2-2\alpha+1<N^2.
\]
The final inequality holds because \(\alpha\ge3/\sqrt5>1/2\). For \(y\ge q+1\),
\[
T_N(y)\ge5y^2+2y+1>5\alpha^2=N^2.
\]
Therefore \(H_N(y)\) strictly increases up to \(q\), and strictly decreases after \(q+1\), leaving at most \(q,q+1\) as candidates. Their exact comparison proves the stated threshold; in the boundary case \(N=3\) the admissible range has only \(y=1=q\). This establishes the full all-integer maximum and the characterization of its maximizing vertex quadruples.

**4. Tie equation.** If \(H_N(q+1)=H_N(q)\) with both gaps legal, then \(N^2=T_N(q)\). In the even case, write \(u=5q+4\); in the odd case write \(u=5q+1\). Either equation rearranges to
\[
\boxed{u^2-5N^2=-4},\qquad u>0,\ N\ge3.
\]
Conversely, any positive integer solution of this Pell-type equation with \(N\ge3\) gives one of the two threshold equations: modulo five, \(u\equiv1\) or \(4\), leading to the respective representations \(u=5q+1\) or \(u=5q+4\). Comparison of \(u/5\) with \(N/\sqrt5\), together with the displayed equation and the congruence parity, identifies this \(q\) with \(\lfloor N/\sqrt5\rfloor\) and matches the necessary parity of \(N-q\). Equivalently these last two facts follow directly from the odd-index Fibonacci–Lucas recurrences below.

**5. Complete Pell solutions.** Recall the Lucas numbers \(L_0=2,L_1=1\), \(L_{j+2}=L_{j+1}+L_j\). The identity \(L_j^2-5F_j^2=4(-1)^j\) provides the positive solutions \((u,N)=(L_{2m+1},F_{2m+1})\). Conversely, for a positive solution with \(N\ge2\), \(u,N\) have the same parity, and the descent
\[
(u,N)\mapsto\left(\frac{3u-5N}{2},\frac{3N-u}{2}\right)
\]
yields another positive integer solution of the same equation with strictly smaller \(N\), down to \((1,1)\) through \((4,2)\). (Positivity follows from \(\sqrt{5N^2-4}<3N\) and \(3\sqrt{5N^2-4}>5N\) for \(N\ge2\).) The inverse descent generates exactly \((L_{2m+1},F_{2m+1})\), so there are no others. For odd indices at least five, \(L_{2m+1}\equiv1\pmod5\) when \(m\) is even and \(4\pmod5\) when \(m\) is odd; the Fibonacci recurrences then show \(q=(L_{2m+1}-1)/5\) with \(N-q\) odd, or \(q=(L_{2m+1}-4)/5\) with \(N-q\) even, respectively. This proves that every such positive Pell solution really gives a tie. When the parity flips between \(y=q\) and \(q+1\), one balanced pair \((x,z)\) is equal and the other yields two mirror choices. Consequently each tie has exactly three vertex-supported maximizers; elsewhere there is one or two according to the unique balanced pair.

**6. From vertices to the entire body.** The unsigned determinant \(6\operatorname{Vol}_3(p_0,p_1,p_2,p_3)=\lvert\det(p_1-p_0,p_2-p_0,p_3-p_0)\rvert\) is convex separately in each point \(p_i\). Because \(C_N\) is the convex hull of its vertices, replacing each point of any contained tetrahedron in turn by some vertex cannot decrease the volume. Thus the largest tetrahedron anywhere in \(C_N\) has the already-computed vertex-supported volume \(\mathcal V_N\). This argument does *not* exclude nonvertex equality configurations.

## Verification

The standalone file `checker.py` uses Python integer arithmetic. It enumerates every vertex quadruple for all \(N=3,\ldots,59\), compares the exact Vandermonde maxima and complete optimizer sets to the theorem, and checks signed homogeneous determinants separately. For \(N=3,\ldots,10000\), it also checks the exact two-candidate threshold against all admissible one-variable gap choices and independently compares the tie indices to the odd-index Fibonacci sequence. The result is:

`CYCLIC_FEKETE_PASS full_n=4..60 full_quadruples=5949147 1d_N=3..10000 ties=5,13,34,89,233,610,1597,4181 exact_determinants=PASS`

These finite experiments corroborate, but do not supply, the unrestricted all-integer proof above. Reproduce with `python checker.py` using the Python standard library.

## Relationship to prior work

The classical Fekete-point problem maximizes a Vandermonde product over a compact set; see Dubickas and Pritsker for its definitions and weighted, continuous-domain treatments [1]. Karvonen, Särkkä, and Tanaka analyze approximate Fekete points for truncated kernel matrices and Gaussian-kernel interpolation over continuous domains [2]. The canonical moment-curve construction of a cyclic polytope is also documented by the Polyhedra package of Macaulay2 [3]. The present problem fixes **four nodes on a finite integer line** and seeks a sharp Euclidean three-dimensional volume together with all discrete equality configurations. Those prior constructions and weighted/continuous statements do not themselves yield the exact two-gap threshold or the Fibonacci–Lucas tie classification. Historical priority is provisional: related classical finite-node extremal-design or interpolation literature may use a different terminology.

## Limitations

The sparse Fibonacci-resonance classification depends on the equally spaced integer moment-curve realization. Different affine realizations preserve relative vertex-supported volume ratios but can distort absolute Euclidean volumes by a determinant factor; arbitrary nonlinear parameter grids need not preserve the same maximizers. The classification of optimal tetrahedra with nonvertex corners is not supplied. Literature inspection establishes no claim of exhaustive historical priority; independent mathematical validation has not been performed.

## References

[1] A. Dubickas and I. Pritsker, *Weighted Fekete points on the real line and the unit circle*, first public preprint 2019-02-22, arXiv:1902.08348v1, https://arxiv.org/html/1902.08348v1 . See Section 1 for Vandermonde/Fekete definitions and Theorems 1.1–1.2 for weighted settings.

[2] T. Karvonen, S. Särkkä, and K. Tanaka, *Kernel-based interpolation at approximate Fekete points*, first public preprint 2019-12-16, arXiv:1912.07316v1, https://arxiv.org/html/1912.07316v3 . See Sections 2.2 and 4.1 on kernel determinant optimization and Gaussian interpolation.

[3] Macaulay2 Polyhedra documentation, *cyclicPolytope*, https://macaulay2.com/doc/Macaulay2-1.26.05/share/doc/Macaulay2/Polyhedra/html/_cyclic__Polytope.html .
