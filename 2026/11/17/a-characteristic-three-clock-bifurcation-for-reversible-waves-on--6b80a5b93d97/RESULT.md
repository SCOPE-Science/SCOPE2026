# A characteristic-three clock bifurcation for reversible waves on projective-plane incidence graphs

## Finding
Let \(\Pi\) be any finite projective plane of order \(s\ge2\) with \(3\nmid s\), not necessarily Desarguesian. Put \(v=s^2+s+1\). Let \(A\) be the adjacency matrix of its point-line incidence graph, taken over \(\mathbb F_Q\) with \(Q=3^f\), \(f\ge1\). On pairs of labelled vertex configurations define the reversible second-order wave
\[
T(u,w)=(Au-w,u),\qquad (u,w)\in\mathbb F_Q^{2v}\times\mathbb F_Q^{2v}.
\]
Every state is periodic from its first time. The exact order of the entire permutation \(T\), and every fixed-point count, depend only on the plane order modulo three:

**Order \(s\equiv2\pmod3\):** the exact global order is eight, and for each integer \(t\ge1\),
\[
E_s(t)=4\mathbf1_{4\mid t}+4(v-1)\mathbf1_{8\mid t}.
\]
Only primitive temporal periods \(1,4,8\) occur; all three occur. The zero state is the unique fixed state, \(Q^4-1\) states have least period four, and \(Q^{4v}-Q^4\) have least period eight.

**Order \(s\equiv1\pmod3\):** the exact global order is eighteen. Write \(h=3^{\nu_3(t)}\), and put
\[
H_s(t)=\min(4,h)+(v-2)\min(2,h),\qquad
E_s(t)=(1+\mathbf1_{2\mid t})H_s(t).
\]
Precisely the primitive periods \(1,2,3,6,9,18\) occur, and every one occurs.

In both cases the number of states fixed by the \(t\)-th iterate is exactly
\[
\#\operatorname{Fix}(T^t)=Q^{E_s(t)}.
\]
For any positive integer \(d\), the population of labelled states of least period \(d\), and the number of distinct temporal orbits of that length, are respectively
\[
P_d=\sum_{e\mid d}\mu(d/e)Q^{E_s(e)},\qquad O_d=P_d/d.
\]
No spatial symmetry or temporal phase is quotiented from the state populations. The formula is valid for every finite projective plane of the stated order, including nonisomorphic planes with the same order, and every finite extension of \(\mathbb F_3\).

## Assumptions and scope
A finite projective plane of order \(s\) has \(v=s^2+s+1\) points and equally many lines, with each point on \(s+1\) lines and each pair of distinct points on exactly one common line; the dual statements hold. The point-line incidence graph has \(2v\) distinguishable vertices. Each dynamic state is an ordered pair of complete vertex-label vectors of length \(2v\), so its total vector-space dimension is \(4v\). The field size \(Q\), plane order \(s\), and time \(t\) are distinct parameters. Subtraction of the previous state is essential, since addition gives a different rule in odd characteristic. No assertion is made here for \(3\mid s\).

## Proof
**1. Incidence identity and reversibility.** Let \(B\) be the point-line incidence matrix, and \(J\) the all-ones \(v\)-square matrix, all entries reduced to characteristic three. Directly counting the common incident lines of distinct points and dualizing gives
\[
BB^{\mathsf T}=B^{\mathsf T}B=sI+J,
\quad B\mathbf1=B^{\mathsf T}\mathbf1=(s+1)\mathbf1.
\]
The graph adjacency is \(A=\left(\begin{smallmatrix}0&B\\B^{\mathsf T}&0\end{smallmatrix}\right)\). The wave transfer is \(T=\left(\begin{smallmatrix}A&-I\\I&0\end{smallmatrix}\right)\), with inverse \(T^{-1}(u,w)=(w,Aw-u)\). Thus every state is immediately periodic over a finite field. Writing \(S=\operatorname{diag}(A,A)\) on the two time rows, direct block multiplication gives
\[
T+T^{-1}=S,\qquad T^2-ST+I=0.
\]

**2. The nonresonant plane order \(s\equiv2\pmod3\).** Here \(v\equiv1\pmod3\), so each point/line space is the direct sum of the constant line \(U=\langle\mathbf1\rangle\) and the zero-sum hyperplane \(W=\ker(\mathbf1^{\mathsf T})\). Both \(B\) and \(B^{\mathsf T}\) kill \(U\) and preserve \(W\). On \(W\), the identity \(BB^{\mathsf T}=-I+J\) becomes \(BB^{\mathsf T}=-I\), and similarly for the other shore. Hence \(A=0\) on the two-dimensional sum of constant-shore spaces, while \(A^2=-I\) on the complementary \(2(v-1)\)-dimensional subspace.

Each of these spatial summands lifts to two time rows. On the four-dimensional lift of the constant-shore space, \(T^2=-I\); every nonzero vector there has least period four. On the \(4(v-1)\)-dimensional lift of \(W\oplus W\), squaring \(T+T^{-1}=S\) and using \(S^2=-I\) gives \(T^4=-I\), hence every nonzero vector there has least period eight. The only vector of period one is zero. The direct sum yields all three least-period populations and the displayed exact nullity \(E_s(t)\). Since the complementary space is nonzero, the global order is exactly eight.

**3. The resonant plane order \(s\equiv1\pmod3\).** Now \(v\equiv0\pmod3\), so \(J^2=vJ=0\) although \(J\ne0\). The incidence identity becomes \(BB^{\mathsf T}=I+J\), so \(B\) is invertible and
\[
A^2=I+\operatorname{diag}(J,J),\qquad (A^2-I)^2=0.
\]
The spatial characteristic polynomial is
\[
\det(yI-A)=\det((y^2-1)I-J)=(y^2-1)^v.
\]
For each \(\lambda\in\{1,-1\}\), solving \(A(p,\ell)=\lambda(p,\ell)\) yields \(Jp=0\), \(\ell=\lambda B^{\mathsf T}p\), so the \(\lambda\)-eigenspace of \(A\) has dimension \(v-1\). Since its algebraic multiplicity is \(v\), and no spatial Jordan block has length greater than two, the Jordan partition at each \(\lambda\) is exactly one size-two block and \(v-2\) size-one blocks.

On the two-time-row lift of a single spatial Jordan block of size \(k\in\{1,2\}\) at \(\lambda\), the temporal characteristic polynomial is \((x^2-\lambda x+1)^k=(x+\lambda)^{2k}\) in characteristic three. Solving \(T(u,w)=-\lambda(u,w)\) shows that its temporal eigenspace has the same dimension (one) as the spatial eigenspace of the original block. Hence its entire temporal Jordan form is **one block of size \(2k\)** at eigenvalue \(-\lambda\), not several smaller blocks. Therefore at each temporal eigenvalue \(1\) and \(-1\), the wave has exactly one Jordan block of size four and \(v-2\) of size two.

In characteristic three, \(x^t-1\) has multiplicity \(h=3^{\nu_3(t)}\) at \(x=1\), and also at \(x=-1\) exactly when \(t\) is even. A Jordan block of size \(k\) contributes \(\min(k,h)\) fixed dimensions at an applicable eigenvalue. Summing the stated partitions gives \(E_s(t)\) exactly. A size-four block at eigenvalue \(-1\) has least-order exponent eighteen, and one at eigenvalue \(1\) has exponent nine. Size-two blocks supply periods three and six; ordinary eigenvectors supply periods one and two. All six claimed primitive periods therefore occur, and the global order is exactly eighteen.

**4. Orbit inversion.** Each reversible finite-state map is a permutation, and \(\#\operatorname{Fix}(T^t)=\sum_{d\mid t}P_d\). Möbius inversion yields the formula above. Dividing by \(d\) counts temporal cycles of primitive length \(d\). No finite enumeration is used to establish the unrestricted statement. \(\square\)

## Verification
Two standalone programs accompany this result. `check_wave.py` builds the explicit projective planes of orders \(2,4,5\) in finite-field coordinates, constructs their wave transfer matrices over \(\mathbb F_3\), and performs exact modular Gaussian elimination at the decisive time indices; it also checks the exact global order. For plane orders \(2\) and \(5\), the observed fixed dimensions at times \(1,4,8\) are \((0,4,4v)\). For order \(4\), the dimensions at times \(1,2,3,6,9,18\) are \((20,40,41,82,42,84)\). These match the formulas.

`check_direct.py` independently constructs the same graphs using affine coordinate charts and a separate finite-field multiplication table, and simulates individual neighbor sums with previous-state subtraction. Across \(804\) deterministic test configurations on orders \(2,4,5\), all least periods divide the predicted global order, and the predicted maximal period is attained in each order. The included output files record the actual runs. Both programs are ordinary finite checks; the argument above, rather than finite tests, establishes the theorem for every permitted finite projective plane.

## Relationship to prior work
Reversible second-order cellular automata are established, not new. Macfarlane (2004) treats linear reversible one-dimensional rules over characteristic two; Vlasov (2013, Section 3) presents the general previous-state-subtraction construction on arbitrary cell spaces. Neither source's inspected material supplies the projective-plane characteristic-three period or orbit counts.

A published characteristic-two classification for reversible waves on the **same** family of projective-plane incidence graphs gives orders six and twelve and an orbit formula depending on binary incidence rank. That statement does **not** imply the present characteristic-three 8-versus-18 bifurcation: the odd-characteristic inverse uses subtraction, and the rank, eigenvalues, and Jordan blocks of the incidence operator change. A published characteristic-three classification on complete bipartite graphs likewise gives periods eight or twelve, but those graphs have a rank-two spatial operator, unlike the projective-plane incidence graph with its large invertible or \(-I\) component. Its result therefore does not cover this theorem. The counted common-incidence identity is classical; the asserted contribution is the all-plane, nondefining-characteristic temporal classification and its exact orbit populations.

## Limitations
The theorem excludes orders divisible by three: in that case the incidence rank in characteristic three may carry additional information not determined by the order alone. The statement does not classify distinct projective planes or their automorphism groups, spatially quotient periodic states, or claim generality for other characteristics or nonlinear updates. Historical priority has been investigated but not independently confirmed; Macfarlane's full article was not available in the inspected form (the dated abstract was inspected). Independent external mathematical validation has not been performed.

## References
- A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A 37 (2004), DOI:10.1088/0305-4470/37/45/006, published 2004-10-28. https://doi.org/10.1088/0305-4470/37/45/006
- A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297, first submitted 2013-11-18, especially Sections 2–3. https://arxiv.org/abs/1311.4297
- *The incidence-rank clock of reversible waves on finite projective planes*, published research record `fe075b4d8619`, 2026-11-08, especially proof and assumptions.
- *Mod-three resonance trichotomy for reversible waves on complete bipartite graphs*, published research record `167b2c8980f2`, 2026-11-08, especially proof and assumptions.
- M. Lavrauw, L. Storme, and G. Van de Voorde, *On the code generated by the incidence matrix of points and hyperplanes in PG(n,q) and its dual*, arXiv:1201.3290, 2012-01-16 (related incidence-code context, not a dynamical result). https://arxiv.org/abs/1201.3290
