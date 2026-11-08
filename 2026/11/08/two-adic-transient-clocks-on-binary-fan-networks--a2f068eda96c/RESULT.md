# Two-adic transient clocks on binary fan networks

## Finding
Let \(F_n=K_1\vee P_n\) be the fan graph on a hub and \(n\ge2\) sequentially labelled path vertices. At each synchronous step, replace every vertex's value in a finite field \(\mathbb F_q\), where \(q\) is a power of two, by the sum of its open-neighbor values. Write \(B_n\) for this linear update and \(T(x)\) for the first time at which the trajectory of \(x\) reaches an eventual periodic orbit.

The entire zero-primary Jordan form of \(B_n\) has the following exact trichotomy:

1. For even \(n\), it consists of one nilpotent block of size \(1\).
2. For \(n\equiv1\pmod4\), it is empty: \(B_n\) is invertible.
3. For \(n\equiv3\pmod4\), put \(e=2^{\nu_2(n+1)}\ge4\). It consists of two nilpotent blocks of sizes \(e-3\) and \(1\), including two size-one blocks when \(e=4\).

All assertions hold for each \(q=2^a\), \(a\ge1\). Define \(d\) to be the dimension of the invertible Fitting component, and \(c(t)\) the nullity of the \(t\)-th power on the nilpotent component, with \(c(0)=0\). The explicit values are
\[
(d,c(t))=\begin{cases}
(n,\min(t,1)),&n\text{ even},\\
(n+1,0),&n\equiv1\pmod4,\\
(n-e+3,\min(t,e-3)+\min(t,1)),&n\equiv3\pmod4.
\end{cases}
\]
Consequently the *complete labelled first-entry census* is
\[
\#\{x:T(x)\le t\}=q^{d+c(t)}\quad(t\ge0),
\qquad
\#\{x:T(x)=t\}=q^d\big(q^{c(t)}-q^{c(t-1)}\big)\quad(t\ge1),
\]
with \(\#\{T=0\}=q^d\). The sharp maximum entry time is \(1\) for even \(n\), \(0\) for \(n\equiv1\pmod4\), and \(e-3\) for \(n\equiv3\pmod4\).

For the naturally resonant family \(n=2^s-1\), \(s\ge3\), the graph has diameter two, yet \(\max_xT(x)=n-2\). Exactly \(1-1/q\) of all \(q^{n+1}\) labelled configurations attain this maximum. In addition, its recurrent subspace has dimension two, its recurrent update is one unipotent Jordan block of size two, and it has exactly \(q\) fixed configurations and \((q^2-q)/2\) primitive period-two orbits. In the binary case there are exactly two fixed states and one primitive two-cycle; exactly half of all initial states take the full \(n-2\) transient.

## Assumptions and scope
There are \(n+1\) *distinct* labelled vertices, no self-loops and no boundary wraparound. The path vertices are \(1,\ldots,n\), with edges between consecutive path vertices; the hub is adjacent to every path vertex. Each update is simultaneous and uses states from the preceding time only, and all additions are in the specified finite field. The first periodic-entry time \(T(x)\) is the minimal nonnegative integer \(t\) for which \(B_n^t x\) is on a periodic orbit. Recurrent orbits of periods other than one and two can occur away from the resonant subfamily; this finding does not classify their lengths.

## Proof
**Step 1 (the characteristic polynomial from matchings).** For any loopless undirected graph with adjacency matrix \(A\) in characteristic two, \(\det(zI-A)\) is its ordinary matching polynomial reduced modulo two: terms in the determinant expansion containing a permutation cycle of length at least three cancel in reversal pairs. Fixed points contribute \(z\), and transpositions contribute graph edges. Denote by \(f_j(z)\) the resulting polynomial for the path on \(j\) vertices. Then \(f_0=1\), \(f_1=z\), and \(f_j=zf_{j-1}+f_{j-2}\) for \(j\ge2\).

Reflecting a path on \(2k+1\) vertices pairs all its nonreflection-invariant matchings. A reflection-invariant matching must leave the central vertex unmatched and choose the same matching on both \(k\)-vertex halves. Thus
\[f_{2k+1}(z)=z f_k(z)^2.\]
For a matching in the fan, either the hub is unmatched, contributing \(zf_n\), or it is matched to some path vertex \(i\), contributing \(f_{i-1}f_{n-i}\). Reflecting the path pairs the latter terms when \(n\) is even, and leaves exactly the central term \(f_k^2\) when \(n=2k+1\). It follows that
\[
\chi_{B_n}(z)=\begin{cases}
z f_n(z),&n\text{ even},\\
(z+1)^2 f_k(z)^2,&n=2k+1.
\end{cases}
\]
The formula identifies the nonzero eigenvalue contributions, but *by itself does not determine the sizes of nilpotent Jordan blocks*.

**Step 2 (zero multiplicity).** The recurrence gives \(f_j(0)=1\) when \(j\) is even. Repeatedly applying \(f_{2k+1}=zf_k^2\) shows that for odd \(j\) the order of vanishing at zero is exactly \(2^{\nu_2(j+1)}-1\). Hence for even \(n\) the zero eigenvalue has algebraic multiplicity one. For \(n\equiv1\pmod4\), \(k=(n-1)/2\) is even and the characteristic polynomial has nonzero constant term. For \(n\equiv3\pmod4\), the algebraic multiplicity of zero is
\[2\big(2^{\nu_2((n+1)/2)}-1\big)=2^{\nu_2(n+1)}-2=e-2.\]

**Step 3 (geometric multiplicity and a length-one block).** Let \(C\) be the adjacency matrix of the path, \(\mathbf1\) its all-one column vector, and \(h\) the hub coordinate. Then
\[B_n(h,x)=(\mathbf1^{\mathsf T}x,\ h\mathbf1+Cx).\]
For odd \(n\), the path kernel is exactly one-dimensional, spanned by \(w=(1,0,1,0,\ldots,1)\); the boundary recurrence \(x_{i-1}+x_{i+1}=0\) proves this directly. When \(n=4r+3\), \(\mathbf1^{\mathsf T}w=0\). Define \(a_i=1\) precisely for \(i\equiv2,3\pmod4\) and zero otherwise. Direct inspection of both endpoints and all interior vertices yields \(Ca=\mathbf1\) and \(\mathbf1^{\mathsf T}a=2(r+1)=0\) in characteristic two. Thus \((0,w)\) and \((1,a)\) lie in \(\ker B_n\), and every kernel vector is their linear combination. The zero-primary component consequently has exactly two Jordan blocks.

The matrix \(B_n\) is symmetric. The kernel vector \(v=(1,a)\) satisfies \(v^{\mathsf T}v=1+\mathbf1^{\mathsf T}a=1\). If \(v\) belonged to \(\operatorname{im}B_n\), say \(v=B_ny\), symmetry and \(B_nv=0\) would imply \(v^{\mathsf T}v=(B_nv)^{\mathsf T}y=0\), a contradiction. A kernel vector outside the image witnesses a nilpotent Jordan block of size one. Since there are exactly two blocks and their total dimension is \(e-2\), the second block has size \(e-3\). When \(n\) is even, algebraic multiplicity one already forces one size-one nilpotent block. Invertibility in the remaining case was proved in Step 2.

**Step 4 (count and sharpness).** Finite-dimensional Fitting decomposition splits the state space into the invertible part of dimension \(d\) and the nilpotent part, with the blocks just proved. A state is periodic exactly when its nilpotent coordinate is zero; it has entered the periodic set by time \(t\) exactly when that coordinate belongs to \(\ker N^t\). A nilpotent Jordan block of length \(\ell\) contributes \(\min(t,\ell)\) to this kernel dimension. Counting field-valued coordinates proves both first-entry formulas. The last nonempty layer is nonempty because the largest Jordan block is attained by a basis vector at its end, proving every claimed sharp bound.

**Step 5 (the diameter-two linear clock).** For \(n=2^s-1\), repeated use of the reflection identity yields \(f_n(z)=z^n\) and \(f_{(n-1)/2}(z)=z^{(n-1)/2}\), hence
\[\chi_{B_n}(z)=z^{n-1}(z+1)^2.\]
Thus the invertible component has dimension two. The path matrix \(C+I\) is invertible because its determinant is \(f_n(1)=1\). Every fixed vector of \(B_n\) must satisfy \((C+I)x=h\mathbf1\), so each hub value determines at most one fixed vector. Since the characteristic polynomial contains \((z+1)^2\), at least one nonzero fixed vector exists; therefore the fixed space has exactly dimension one. The invertible two-dimensional part must be a single \(2\)-by-\(2\) Jordan block at eigenvalue one, giving the stated fixed points and two-cycles. For \(s\ge3\), the nilpotent blocks have lengths \(n-2\) and \(1\), so the last layer adds exactly one free field coordinate. Its fraction is \(1-q^{-1}\). Since every path vertex has distance one from the hub, the fan's diameter is two for \(n\ge3\).

## Verification
Standalone pure-Python scripts in `checks/matrix_certificate.py` and `checks/labelled_evolution.py` verify the statement without external packages. The matrix checker independently computes characteristic polynomials from the polynomial determinant expansion for \(2\le n\le14\), compares all zero-power nullities for \(2\le n\le96\), and confirms the special eigenvalue-one eigenspace for \(n=3,7,15,31,63\). The separate labelled-state simulator evolves every one of the \(8184\) binary configurations across \(2\le n\le11\), and checks the exact first-entry distribution and the special period census for \(n=7\). A captured successful output is included. These computations corroborate the symbolic proof rather than replacing it.

## Relationship to prior work
Wolfram (1983) and Martin, Odlyzko and Wolfram (1984) study additive cellular automata, notably Rule 90 on periodic rings, with algebraic methods for transients and periodic states. Thomas, Stevens and Lettieri (2006) derive path and ring polynomial techniques for Rule 90 and Rule 150; their general use of minimal polynomials is accepted here, not asserted new. These models have no universal hub, and their formulas do not by themselves supply the zero-primary Jordan partition of the coupled fan update. Cardoso, Gomes and Pinheiro (2022) give a general spectral theory for graph joins; such characteristic-polynomial machinery could imply the polynomial identity above, which is not asserted to be the new contribution. The *newly assessed statement* is the exact characteristic-two nilpotent Jordan classification and full entry-time census, particularly the diameter-two family with an \(n-2\) transient affecting a proportion \(1-q^{-1}\) of states. A known wheel-graph neighbor-parity classification is not being extended by implication: the wheel has a closing rim edge and has a different primary Jordan pattern; ordinary path and fan chip-firing results likewise do not cover this update.

## Limitations
There is no claim of a classification of all *nonzero* primary components or all possible recurrent periods for general \(n\), except for the resonant \(n=2^s-1\) family. The characteristic-polynomial step is an elementary reduction of known matching methods; mathematical value rests on the Jordan structure, exact entry census and diameter-two resonance. An unindexed equivalent result or a deeper application of published graph-join formulas could affect originality; those possibilities require outside priority review. The algebraic proofs, not the finite checks, supply the infinite-family conclusion.

## References
1. S. Wolfram, “Statistical mechanics of cellular automata,” *Reviews of Modern Physics* 55 (1983), 601–644, published July 1, 1983. DOI: 10.1103/RevModPhys.55.601.
2. O. Martin, A. M. Odlyzko and S. Wolfram, “Algebraic properties of cellular automata,” *Communications in Mathematical Physics* 93 (1984), 219–258. DOI: 10.1007/BF01223745. Author-hosted open text: https://content.wolfram.com/sw-publications/2020/07/algebraic-properties-cellular-automata.pdf.
3. D. M. Thomas, J. G. Stevens and S. Lettieri, “Characteristic and minimal polynomials of linear cellular automata,” *Rocky Mountain Journal of Mathematics* 36 (2006), 1077–1092. DOI: 10.1216/rmjm/1181069447.
4. D. M. Cardoso, H. Gomes and S. J. Pinheiro, “The H-join of arbitrary families of graphs — the universal adjacency spectrum,” *Linear Algebra and its Applications* (2022). DOI: 10.1016/j.laa.2022.04.015.
