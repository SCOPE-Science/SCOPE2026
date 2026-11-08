# Mod-three reversibility and a two-adic transient census for neighbor-sum dynamics on ladder graphs

## Finding

For every integer \(n\ge2\) and every finite field \(\mathbb F_q\) of characteristic two, let \(L_n=P_n\square K_2\) be the ordinary \(n\)-rung ladder, and let \(F\) simultaneously replace each vertex value by the sum of its open neighbors' values. For an initial configuration \(x\in\mathbb F_q^{2n}\), define its first periodic-entry time
\[
T(x)=\min\{t\ge0:F^t(x)\text{ belongs to a periodic orbit of }F\}.
\]
Set
\[
m(n)=\begin{cases}0,&3\nmid(n+1),\\ 2^{\nu_2(n+1)+1},&3\mid(n+1).\end{cases}
\]
Then the complete zero-primary Jordan partition of \(F\) is empty when \(m(n)=0\) and consists of **exactly two blocks of size \(m(n)\)** otherwise. Thus \(F\) is a permutation of the entire state space precisely when \(n\not\equiv2\pmod3\), and its maximum first periodic-entry time is \(m(n)\) when \(n\equiv2\pmod3\).

For \(m=m(n)>0\), the complete first-entry census is
\[
\#\{x:T(x)=0\}=q^{2n-2m},\qquad
\#\{x:T(x)=t\}=q^{2n-2m}\bigl(q^{2t}-q^{2t-2}\bigr)\quad(1\le t\le m),
\]
and no later entry is possible. In particular, \(1-q^{-2}\) of all configurations require the **maximum** \(m\) updates. When \(m=0\), every one of the \(q^{2n}\) configurations is initially periodic.

For the infinite subfamily \(n=3\cdot2^k-1\), \(k\ge1\), the maximum entrance time is \(2^{k+1}\); hence it is unbounded on width-two, degree-at-most-three grids. Along this family its ratio to graph diameter tends to \(2/3\).

## Assumptions and scope

The graph is simple with open-neighbor updates and **open** path ends, not a cylindrical ladder or a closed-neighborhood parity rule. The two rows each have exactly \(n\) vertices, and the rung joining corresponding positions is present. All updates are synchronous. The field size \(q\) is an arbitrary power of two; the proof does not assume binary states alone. The statement concerns transient **entry times**, the zero-primary Jordan structure and reversibility; it does not classify the individual cycle lengths of the invertible component.

## Proof

**1. A cyclic path operator.** Let \(S_n\) denote the \(n\times n\) adjacency matrix of the open path over \(\mathbb F_q\), and write \(p_n(z)=\det(zI-S_n)\). Expanding the tridiagonal determinant at one end gives
\[
p_0=1,\qquad p_1=z,\qquad p_n=z p_{n-1}+p_{n-2}\quad(n\ge2).
\]
The vectors \(e_1,S_ne_1,\dots,S_n^{n-1}e_1\) form a basis: the coefficient of \(e_{j+1}\) in \(S_n^j e_1\) is one, and all coefficients beyond \(e_{j+1}\) vanish. Consequently, \(S_n\) is cyclic (its minimal polynomial equals \(p_n\)), including after extending scalars to an algebraic closure.

**2. Exact multiplicity of the eigenvalue one.** In characteristic two, the recurrence implies the identity of rational functions
\[
p_n(w+w^{-1})=\frac{w^{n+1}+w^{-(n+1)}}{w+w^{-1}}.
\]
At \(z=1\), the solutions of \(w+w^{-1}=1\) are the two primitive cubic roots \(\omega,\omega^2\) in an algebraic closure. The substitution \(w\mapsto w+w^{-1}\) has nonzero derivative \(1+w^{-2}\) at either root, so it preserves local orders of vanishing. The numerator equals \(w^{-(n+1)}(w^{n+1}+1)^2\). It vanishes at \(\omega\) if and only if \(3\mid n+1\). In that case, write \(n+1=2^s h\) with \(h\) odd. Because \(3\mid h\), the factor \(w^h+1\) has a simple zero at \(\omega\), and
\[
w^{n+1}+1=(w^h+1)^{2^s}.
\]
Since the denominator equals one at \(z=1\), the multiplicity of \(z=1\) in \(p_n\) is exactly \(2^{s+1}\); otherwise it is zero.

**3. Ladder conjugacy and the two equal Jordan blocks.** In row coordinates \((x,y)\), the ladder operator is
\[
A_n=\begin{pmatrix}S_n&I\\I&S_n\end{pmatrix}.
\]
Introduce \(u=x+y\), \(v=x\), and let \(C=S_n+I\). The transformed update is
\[
(u,v)\longmapsto(Cu,\,u+Cv).
\]
Since \(S_n\) is cyclic, the generalized zero-eigenspace of \(C\), if nonzero, is one nilpotent Jordan block of length \(m=2^{s+1}\); on its complementary invariant subspace \(C\) is invertible. The displayed ladder operator is invertible on two copies of that complement.

On the zero-primary part identify the path block with multiplication by \(t\) on \(R=\mathbb F_q[t]/(t^m)\). The ladder map on \(R\oplus R\) becomes multiplication by \(t+\varepsilon\) on \(R[\varepsilon]/(\varepsilon^2)\), using \(u+\varepsilon v\). Since \(m\) is a power of two and \(m\ge2\), putting \(z=t+\varepsilon\) yields
\[
\mathbb F_q[t,\varepsilon]/(t^m,\varepsilon^2)
\cong\mathbb F_q[z,\varepsilon]/(z^m,\varepsilon^2).
\]
Indeed \((z+\varepsilon)^m=z^m+\varepsilon^m=z^m\). As a module for multiplication by \(z\), the right-hand side is precisely two copies of \(\mathbb F_q[z]/(z^m)\). Therefore the **entire** zero-primary partition of \(A_n\) is \((m,m)\), with no unaccounted zero blocks. If \(3\nmid n+1\), \(A_n\) is invertible.

**4. First-entry counts.** The Fitting decomposition of \(A_n\) consists of an invertible component of dimension \(d=2n-2m\) and the two nilpotent blocks. Over a finite field, every state in the invertible component is periodic, while a nonzero nilpotent component cannot lie in any periodic orbit. Thus \(T(x)\) is exactly the time required to kill its nilpotent component. The kernel of the \(t\)-th power on the nilpotent component has dimension \(2\min(t,m)\), giving \(q^{d+2t}\) states with \(T\le t\) for \(0\le t\le m\). Taking successive differences proves the displayed counts, including the fraction \(1-q^{-2}\) at \(t=m\). Taking \(n=3\cdot2^k-1\) gives \(m=2^{k+1}\), and the ladder diameter is \(n\), establishing the last conclusion.

## Verification

Run `python verify_linear.py` for an adjacency-matrix calculation independent of the polynomial proof. It constructs the actual \(2n\)-vertex ladder graph and checks \(\dim\ker(A_n^t)=2\min(t,m(n))\) at 525 selected pairs with \(2\le n\le84\), including before, at and after the claimed nilpotent cutoff. The program uses integer bit masks and exact row reduction over \(\mathbb F_2\). Its result is recorded in `linear_check.txt`.

Run `python verify_labelled.py` for independently constructed adjacency lists and direct enumeration of the eventual cycle and first entry of every binary state at \(2\le n\le6\). The verified total is 5,456 labelled initial states, including all 1,024 states for the four-step case \(n=5\). Its result is recorded in `labelled_check.txt`.

The checks are finite corroboration. The conclusions for every \(n\) and every characteristic-two finite field follow from the proof above. Extension from \(\mathbb F_2\) to \(\mathbb F_q\) is valid because the entire matrix and cyclicity argument use entries in the prime field, while the Fitting-space counts depend only on \(q\).

## Relationship to prior work

Martin, Odlyzko and Wolfram developed the algebraic analysis of finite additive cellular automata. Thomas, Stevens and Lettieri analyzed minimal and characteristic polynomials for Rule 90, explicitly including the one-row null-boundary path matrix. Those methods and the path recurrence are established tools, not claimed as novel. Rowland and Yassawi studied linear cellular automata with memory and automatic spacetime columns; their results address a different infinite-lattice question.

The present statement adds the precise **two-row ladder** zero-primary Jordan partition, the mod-three reversibility boundary and the all-time entrance-count formulas. Li and Wu's earlier work on interlace polynomials of ladder graphs is relevant to binary graph ranks, but an accessible full manuscript was not obtained; its abstract discusses interlace polynomial coefficients and ranks of tridiagonal matrices, not a full dynamical entrance-time classification. The general possibility of a previously unlocated equivalent result remains.

## Limitations

No statement is made about the complete primitive-period spectrum on the recurrent component. The individual nonzero eigenvalues of the path map can produce much longer eventual periods; the bound \(m(n)\) concerns only the number of updates **before** reaching periodicity. The precise earliest public dates of several historical journal articles are not established by their later uploads or indexing dates; the dated preprint anchor in the references is used for the source-age classification.

## References

1. O. C. Martin, A. M. Odlyzko and S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics **93** (1984), 219–258, DOI: `10.1007/BF01223745`.
2. D. M. Thomas, J. G. Stevens and S. Lettieri, *Characteristic and Minimal Polynomials of Linear Cellular Automata*, Rocky Mountain Journal of Mathematics **36** (2006), 1077–1092, DOI: `10.1216/rmjm/1181069447`.
3. E. Rowland and R. Yassawi, *A Characterization of \(p\)-Automatic Sequences as Columns of Linear Cellular Automata*, arXiv:`1209.6008`, first submitted 2012-09-26, https://arxiv.org/abs/1209.6008.
4. A. Li and Q. Wu, *Interlace Polynomials of Ladder Graphs*, Journal of Combinatorics, Information and System Sciences **35** (2010), 261–273.
