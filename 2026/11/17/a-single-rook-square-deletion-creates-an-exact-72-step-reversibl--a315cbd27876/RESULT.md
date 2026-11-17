# A single rook-square deletion creates an exact 72-step reversible wave clock

## Finding
For positive integers \(m,n\) divisible by three, let \(G_{m,n}\) be the simple graph obtained from the rectangular rook graph \(K_m\square K_n\) by removing the vertex \((0,0)\) and all incident edges. Set \(q=3^f\) for an arbitrary integer \(f\ge1\), and let \(A\) be the adjacency matrix of \(G_{m,n}\) over \(\mathbb F_q\). Consider the invertible two-time-level evolution
\[
T(u,v)=(Au-v,u),\qquad (u,v)\in(\mathbb F_q^{mn-1})^2.
\]
Then **the exact order of the global time map is 72**, independent of either graph size or the field extension. Every state is periodic at time zero, and the only possible least positive periods are
\[
\boxed{1,2,6,8,18,24,72}.
\]
All seven occur for every allowed \(m,n,q\).

For an exact labelled census define
\[
h=m+n-4,\qquad j=(m-2)(n-2)+1,\qquad
a=h+j,\quad b=3h+2j,\quad c=4h+2j.
\]
The primitive-period **state populations** \(P_t\) (not orbit counts) are
\[
\begin{array}{c|l}
t&P_t\\\hline
1&1\\
2&q^a-1\\
6&q^b-q^a\\
18&q^c-q^b\\
8&(q^4-1)q^a\\
24&(q^4-1)(q^b-q^a)\\
72&(q^4-1)(q^c-q^b).
\end{array}
\]
All other primitive-period populations vanish, and exactly \(P_t/t\) distinct temporal orbits have period \(t\). In particular, a uniform initial state has exact maximal period with probability
\[
\boxed{\Pr(\mathrm{period}=72)=(1-q^{-4})(1-q^{-h}).}
\]
This probability tends to \(1-q^{-4}\) as both graph dimensions grow. The intact graph \(K_m\square K_n\), under the identical characteristic-three rule, has exact global order \(18\) when \(3\mid m,n\); deleting just one vertex therefore multiplies its global clock by four.

## Assumptions and scope
Both side lengths are multiples of three, hence at least three. The graph has \(mn-1\) individually labelled surviving cells. Two distinct cells are adjacent if and only if they share a row or column. The removed cell has no state or feedback; other rook edges remain unchanged. Field values are arbitrary elements of \(\mathbb F_q\), not binary opinions. Both time levels \(u,v\) are unrestricted; the minus sign is essential in odd characteristic. No quotient by graph automorphisms is taken.

## Proof
**1. Decomposition after deleting one cell.** Put \(M=m-1\) and \(N=n-1\). Both equal \(-1\) in characteristic three. Partition the remaining vertices into the \(N\) cells \(R=(0,j)\), the \(M\) cells \(C=(i,0)\), and the \(MN\) interior cells \(I=(i,j)\), where the nonzero indices run from one to \(N\) or \(M\). With arrays \(r,c,w\), the adjacency acts by
\[
\begin{aligned}
(Ar)_j&=\sum_{k\ne j}r_k+\sum_iw_{ij},\\
(Ac)_i&=\sum_{k\ne i}c_k+\sum_jw_{ij},\\
(Aw)_{ij}&=r_j+c_i+\sum_{k\ne i}w_{kj}+\sum_{\ell\ne j}w_{i\ell}.
\end{aligned}
\]
Since \(M,N\ne0\) in the field, each coordinate space splits as a constant line and a zero-sum subspace, of dimensions \(1,M-1\) and \(1,N-1\), respectively. All displayed maps respect the resulting constant/zero-sum tensor sectors.

**2. The three invariant sector types.** In the fully constant sector (one constant value on each of \(R,C,I\)), \(A\) is the three-by-three matrix
\[
Q=\begin{pmatrix}1&0&-1\\0&1&-1\\1&1&2\end{pmatrix}
\quad\text{over }\mathbb F_3.
\]
Its characteristic polynomial is \((X-1)(X^2+1)\) in \(\mathbb F_3[X]\), and these factors are coprime. Thus this sector consists of a one-dimensional eigenvalue-one block and one irreducible quadratic block. For a zero-sum row direction, the corresponding two-dimensional sector, coupling \(C\) to \(I\), has matrix
\[
B=\begin{pmatrix}-1&-1\\1&0\end{pmatrix}.
\]
The same block applies to a zero-sum column direction, coupling \(R\) to \(I\). The characteristic polynomial of \(B\) is \((X-1)^2\), and \(B\ne I\), so it is exactly one size-two Jordan block at eigenvalue one. Finally every tensor product of a row-zero-sum direction with a column-zero-sum direction belongs only to \(I\) and has scalar eigenvalue \(-2=1\). Consequently the full spatial adjacency module is
\[
\boxed{A\ \sim\ J_2(1)^{\oplus h}\oplus J_1(1)^{\oplus j}\oplus\mathbb F_3[X]/(X^2+1),}
\]
where \(h=(M-1)+(N-1)=m+n-4\) and \(j=(M-1)(N-1)+1\). The dimensions sum to \(2h+j+2=mn-1\). This similarity is defined over \(\mathbb F_3\) and therefore remains valid over every extension field.

**3. Temporal blocks.** For a spatial Jordan block \(J_s(1)\), the temporal companion \(T=\left(\begin{smallmatrix}A&-I\\I&0\end{smallmatrix}\right)\) has characteristic polynomial \((Z^2-Z+1)^s=(Z+1)^{2s}\) in characteristic three. Solving \(T(u,v)=-(u,v)\) gives \(v=-u\) and \((A-I)u=0\). Hence its \(-1\)-eigenspace is one-dimensional: the temporal block is exactly \(J_{2s}(-1)\). It has order \(2\cdot3^e\), where \(3^e\) is the smallest power of three at least \(2s\). In particular \(J_2(1)\) yields temporal order \(18\) and \(J_1(1)\) yields order \(6\).

On the two-dimensional spatial irreducible block \(X^2+1\), the temporal characteristic polynomial is
\[
\operatorname{Res}_X(X^2+1,Z^2-XZ+1)=Z^4+1.
\]
This is squarefree in characteristic three and all its roots satisfy \(Z^4=-1\) and \(Z^8=1\). Thus this four-dimensional temporal sector has **exact order eight** and every nonzero vector in it has least period eight. The three sector types are in direct sum, so the whole map has exact order \(\operatorname{lcm}(18,6,8)=72\). Invertibility follows directly from \(T^{-1}(u,v)=(v,Av-u)\), so there is no transient.

**4. Fixed spaces and primitive periods.** At any positive time \(t\), put \(w_t=3^{\nu_3(t)}\). A temporal block \(J_s(-1)\) contributes no fixed vectors except zero when \(t\) is odd, and for even \(t\) has fixed-space dimension \(\min(s,w_t)\). The temporal order-eight sector contributes four fixed dimensions exactly when \(8\mid t\), otherwise zero. Thus
\[
\dim\ker(T^t-I)=
\mathbf1_{2\mid t}\bigl[h\min(4,w_t)+j\min(2,w_t)\bigr]
+4\mathbf1_{8\mid t}.
\]
At \(t=1,2,6,18,8,24,72\), the resulting fixed populations are respectively
\[
1,\quad q^a,\quad q^b,\quad q^c,\quad q^{a+4},\quad q^{b+4},\quad q^{c+4}.
\]
Every divisor of \(72\) has the same fixed population as the greatest member of this list dividing it. Möbius inversion of \(|\operatorname{Fix}(T^t)|=\sum_{d\mid t}P_d\), or direct subtraction of the nested fixed spaces, gives the claimed seven primitive populations. Since \(h,j\ge2\), all six nonzero periods occur. Finally \(c+4=2(mn-1)\), proving the state total; dividing \(P_{72}\) by \(q^{c+4}\) gives the probability formula.

**5. Intact-graph comparison.** Without deleting the cell and still with \(3\mid m,n\), both clique all-ones matrices are nonzero square-zero operators. The intact adjacency \(J_m\otimes I+I\otimes J_n-2I\) has only spatial eigenvalue \(1\), with nilpotent Jordan lengths at most three and at least one length three. Its temporal companion therefore has exact order \(18\). The puncture produces a new quadratic spatial factor and hence order eight, raising the least common multiple to \(72\).

## Verification
The standalone standard-library `verify_punctured_rook.py` independently builds the literal vertex adjacency, forms the temporal matrix over \(\mathbb F_3\), computes exact modular ranks of \(T^t-I\), and checks all twelve divisors \(t\mid72\) across five board dimensions \((m,n)=(3,3),(3,6),(6,3),(3,9),(6,6)\): **60 exact kernel-dimension comparisons**, plus tests that the matrix has order precisely 72. Its actual captured output is included in `verify_punctured_rook.out`.

The separately implemented `verify_direct.cpp` instead evolves sampled vertex-level states using explicit rook-neighbor summation, without matrix rank operations. It checked **3,400 actual trajectories** on four punctured boards; each returned to its initial two-time state with a divisor of 72 in the permitted period set. Its captured output is included in `verify_direct.out`. Compile with `g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct` and run `./verify_direct`; run the Python verifier with `python3 verify_punctured_rook.py`. Both test sets are corroborative: the invariant-sector decomposition and companion polynomial calculation prove the infinite-family assertion.

As a sample, on the 8-vertex graph \(G_{3,3}\) over \(\mathbb F_3\), the exponents are \((a,b,c)=(4,10,12)\). The primitive state populations at periods \(1,2,6,8,18,24,72\) are obtained directly from the displayed formula and sum to \(3^{16}\).

## Relationship to prior work
Vlasov's reversible second-order automaton framework (arXiv:1311.4297, posted 2013-11-18) supplies the type of temporal update but does not state the punctured-rook wave clock or orbit formula. The published square-rook Smith-group study of Ducey, Gerhard and Watson (arXiv:1507.06583v1, posted 2015-07-23) addresses integral Smith invariants on intact graphs rather than time evolution after a vertex deletion. An existing all-rectangular characteristic-odd **intact** rook-graph Laplacian classification provides the unpunctured modular Jordan decomposition; the present punctured adjacency has an additional irreducible quadratic factor and is not a consequence of that intact similarity type. The most structurally similar known punctured-rook calculation treats **characteristic two first-order neighbor summation**, where the pertinent modular algebra and resulting dynamical periods are different; its full theorem and proof have been examined. A characteristic-three equal-alphabet Hamming wave classification covers the intact \(3\)-divisible square case, with temporal order 18, but not the punctured boards or the order-eight defect sector. Those comparisons isolate the deletion-induced exact order-72 phase and its primitive-state census.

## Limitations
The result concerns single-vertex deletion, characteristic three, and side lengths divisible by three. It does not classify other residues, multiple defects, nonlinear opinions, or spatially inequivalent temporal orbits. Finite rank and simulation checks are not substitutes for the all-size decomposition proof. The originality comparison includes publicly accessible research records and relevant primary papers, but cannot eliminate an unindexed historical equivalent; independent validation has not been performed.

## References
1. A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297v1 (first posted 2013-11-18), https://arxiv.org/abs/1311.4297.
2. J. E. Ducey, J. Gerhard, and N. Watson, *The Smith and Critical Groups of the Square Rook's Graph and its Complement*, arXiv:1507.06583v1 (first posted 2015-07-23), https://arxiv.org/abs/1507.06583.
3. R. Peeters, *On the p-Ranks of the Adjacency Matrices of Distance-Regular Graphs*, Journal of Algebraic Combinatorics 15 (2002), 127–149, DOI:10.1023/A:1013842904024. This treats intact Hamming-graph modular matrices.
