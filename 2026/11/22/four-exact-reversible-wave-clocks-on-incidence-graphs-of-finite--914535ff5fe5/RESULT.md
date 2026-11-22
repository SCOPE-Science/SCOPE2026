# Four exact reversible-wave clocks on incidence graphs of finite partial geometries

## Finding
Let \(\mathcal G\) be any finite partial geometry \(pg(s,t,\alpha)\), with \(s,t,\alpha\ge1\), every line incident with \(s+1\) points, every point with \(t+1\) lines, distinct points on at most one common line, and exactly \(\alpha\) connecting flags for every nonincident point-line pair. Write \(B\) for its binary point-line incidence matrix, \(A=\begin{psmallmatrix}0&B\\B^{\mathsf T}&0\end{psmallmatrix}\), and \(N=|P|+|L|\). On two labelled time layers over any finite field \(\mathbb F_Q\), \(Q=2^f\), define \(T(u,w)=(Au+w,u)\) for \(u,w\in\mathbb F_Q^N\).

Every state is periodic from time zero. **The exact global temporal period** is
\[
L=\begin{cases}
6,&\alpha\text{ even and }s\equiv t\pmod 2,\\
8,&\alpha\text{ even and }s\not\equiv t\pmod 2,\\
8,&\alpha,s,t\text{ all odd},\\
12,&\alpha\text{ odd, }s,t\text{ even, and }\mathcal G\text{ a projective plane},\\
24,&\alpha\text{ odd, at least one of }s,t\text{ even, and }\mathcal G\text{ not a projective plane}.
\end{cases}
\]
The projective-plane exception in the fourth line can be recognized without naming the geometry: among the odd-\(\alpha\), even-\(s,t\) cases, it occurs **if and only if** \(A^2=\operatorname{diag}(J_{|P|},J_{|L|})\) over characteristic two. This characterizes the case of a projective plane of even order.

There is also an exact **all-iterate fixed-state and primitive-orbit formula** using only six short binary kernel calculations. For \(0\le r\le5\), put \(d_r=\dim\ker A^r\), with \(d_0=0\), \(d_5=d_4\). Put \(e_0=0\), \(e_r=\dim\ker(A+I)^r\) for \(r=1,2\). Define
\[
 a_j=2d_j-d_{j-1}-d_{j+1}\quad(1\le j\le4),\qquad
 b_1=2e_1-e_2,\quad b_2=e_2-e_1.
\]
These are nonnegative integers. For \(k\ge1\), with \(h=2^{\nu_2(k)}\), define
\[
 E(k)=\sum_{j=1}^{4}a_j\min(2j,h)+2\mathbf1_{3\mid k}\sum_{j=1}^{2}b_j\min(j,h).
\]
Then
\[
|\operatorname{Fix}(T^k)|=Q^{E(k)},\qquad
\#\{\text{states of least period }k\}=\sum_{d\mid k}\mu(k/d)Q^{E(d)}.
\]
The number of primitive temporal orbits is the last expression divided by \(k\). In particular, it vanishes unless \(k\mid L\). These are orbit counts on labelled states, with no quotient by graph symmetry.

## Assumptions and scope
The incidence structure is a *realized* finite partial geometry, not merely a feasible parameter tuple or a pseudo-geometric strongly regular graph. Both shores have more vertices than a single incident neighborhood: \(|P|=(s+1)(st+\alpha)/\alpha>s+1\) and \(|L|=(t+1)(st+\alpha)/\alpha>t+1\). The two time layers are distinguished. The field extension degree \(f\ge1\) is arbitrary. All ranks and kernel dimensions may be computed over \(\mathbb F_2\), since the binary matrix has identical rank over every extension \(\mathbb F_Q\). The exceptional plane has order \(s=t\ge2\) even; the projective plane of order one is excluded by its odd order and belongs to the first branch when treated as a partial geometry. The temporal-period statement is about the global permutation order, not a claim that every allowed divisor occurs as a least period.

## Proof
**1. A universal cubic incidence identity.** Write \(v=|P|\), \(b=|L|\), and \(K=\begin{psmallmatrix}0&J_{v\times b}\\J_{b\times v}&0\end{psmallmatrix}\). Counting incidence paths of length three from a point to a line gives \((BB^{\mathsf T}B)_{p\ell}=s+t+1\) when \(p\in\ell\), and \(\alpha\) otherwise. Thus in characteristic two,
\[
 A^3=cA+aK,\quad c\equiv s+t+1-\alpha\pmod2,\quad a\equiv\alpha\pmod2.
\]
Row and column regularity also give
\[
 AK=KA=\operatorname{diag}((t+1)J_v,(s+1)J_b),\qquad A^2K=dK,\quad d\equiv(s+1)(t+1)\pmod2.
\]
All identities are consequences of the partial-geometry axioms, without transitivity, classical coordinates or Desarguesian assumptions.

**2. Reversible-wave primary-block transfer.** Over characteristic two, \(T^{-1}(u,w)=(w,u+Aw)\), proving immediate periodicity. For any one adjacency Jordan block \(J_j(0)\), the two-layer temporal characteristic polynomial is \((X+1)^{2j}\), and \(\dim\ker(T+I)=\dim\ker J_j(0)=1\). Hence it produces one temporal \((X+1)^{2j}\)-block, of order \(2^{\lceil\log_2(2j)\rceil}\). For an adjacency \(J_j(1)\), the temporal polynomial is \((X^2+X+1)^j\); the identity \(T^2+T+I=T\operatorname{diag}(A+I,A+I)\) gives a two-dimensional kernel for this polynomial. Thus it produces one temporal \((X^2+X+1)^j\)-block over \(\mathbb F_2\), of order \(3\cdot2^{\lceil\log_2 j\rceil}\). Scalar extension preserves the kernel dimensions and order even if the quadratic splits. The cubic identity below shows that only adjacency eigenvalues zero and one occur, with zero Jordan lengths at most four and one lengths at most two.

**3. Even \(\alpha\).** Here \(A^3=cA\). If \(s,t\) have opposite parity then \(c=0\), so \(A^3=0\), but \(A^2\ne0\): any two points on one line produce a nonzero off-diagonal entry of \(BB^{\mathsf T}\). Hence a length-three zero block exists and \(L=8\). If \(s,t\) have the same parity then \(c=1\), giving \(A^3=A\). Therefore \(T^6=I\), as follows from \(T+T^{-1}=\operatorname{diag}(A,A)\) and the characteristic-two identity \(T^3+T^{-3}=\operatorname{diag}(A^3+A,A^3+A)\). But \(T^2\ne I\) since \(A\ne0\), while \(T^3\ne I\) since its top-left block equals \(A\ne I\). Thus \(L=6\).

**4. Odd \(\alpha\) with both \(s,t\) odd.** The identities give \(c=d=0\), \(A^3=K\ne0\), and \(A^4=AK=0\). The longest zero Jordan block has length exactly four and there is no one-primary subspace; therefore \(L=8\).

**5. Odd \(\alpha\) with mixed parity.** Here \(c=1,d=0\), so \(A^3=A+K\) and \(A^5=A^3\). Consequently its zero blocks have length at most three and its one blocks at most two. Since \(AK\ne0\), the identity \(A^4+A^2=AK\ne0\) shows a zero block of length three exists: the displayed operator vanishes on every one-primary block and equals \(A^2\) on the zero-primary component. Some one-primary block also exists, since otherwise \(A^3=0\) would force \(A=K\), contradicting the presence of nonincident point-line pairs. The temporal order is therefore \(\operatorname{lcm}(8,3)=24\).

**6. Odd \(\alpha\) with both \(s,t\) even.** Here \(c=0,d=1\), so \(A^3=K\ne0\), \(A^4=AK=\operatorname{diag}(J_v,J_b)\), and \(A^5=A^3\). A one-primary component exists because \(A^3\ne0\). The length-three zero blocks exist exactly when \(A^4+A^2\ne0\), yielding \(L=24\). Otherwise \(A^2=\operatorname{diag}(J_v,J_b)\). As \(s+1,t+1\) are odd, its diagonal entries are one, and off-diagonal entries express unique common lines or points. This equality is equivalent to every two points sharing a line and every two lines sharing a point, hence the incidence structure is a finite projective plane (necessarily \(s=t\) of even order). Conversely every such projective plane satisfies the equality. In that case zero blocks have size at most two; a length-two zero block exists because the sum of two distinct point basis vectors is annihilated by \(A^2\) but not by \(A\) (distinct points have distinct incident-line neighborhoods). The two constant shore vectors are exchanged by \(A\), giving a length-two one block. Their wave components have respective orders four and six, so the exact global period is \(\operatorname{lcm}(4,6)=12\). This proves the exceptional branch and all period cases.

**7. Every fixed-state and primitive-orbit population.** The two polynomial identities imply the adjacency zero-primary blocks have sizes at most four and the one-primary blocks sizes at most two. The differences \(d_j-d_{j-1}\) count zero blocks of length at least \(j\); second differences therefore give the \(a_j\). Analogously, \(e_1\) counts one-primary blocks and \(e_2-e_1\) counts those of length two, giving \(b_1,b_2\). The temporal transfer in step 2 yields a \((X+1)^{2j}\)-block for each zero block and a \((X^2+X+1)^j\)-block for each one block. In \(X^k-1\), the first linear factor occurs with multiplicity \(2^{\nu_2(k)}\), while the quadratic factor occurs with the same multiplicity exactly when \(3\mid k\). Taking polynomial gcd dimensions proves \(E(k)\), including all normalization factors. Möbius inversion gives the least-period and temporal-orbit formula, completing the proof.

## Verification
Running `python3 verify_partial_geometry.py` constructs thirteen incidences by three independently specified families (prime-order affine nets, prime-order projective planes and symplectic generalized quadrangles), plus the three-point triangle geometry; checks line sizes, point degrees, pair uniqueness, and **every antiflag**; verifies the cubic identity; finds actual temporal orders by binary matrix multiplication; and compares the predicted formula against exact nullities of \(T^k+I\) at every \(1\le k\le24\), giving 312 exact fixed-space comparisons. A second program, `python3 verify_small_orbits.py`, directly iterates every labelled state (without matrix powers) on the six-vertex triangle incidence graph and eight-vertex grid incidence graph, respectively 4,096 and 65,536 states, checking the complete primitive period distributions. Captured outputs are included. These finite computations corroborate the proof, and are not asserted to enumerate all partial geometries.

## Relationship to prior work
Bose introduced partial geometries and their incidence axioms in 1963; the cubic identity follows by the standard antiflag count and is not claimed as new. Vlasov's 2013 discussion gives the general reversible second-order cellular-automaton construction. A published projective-plane incidence-wave classification gives the exact six/twelve dichotomy and a rank-resolved orbit formula for that special family. Existing generalized-quadrangle wave work treats \(\alpha=1\); the new classification establishes a unified theorem for arbitrary realized \(\alpha\), including Bruck nets, mixed-parity partial geometries and intermediate geometric families. A wave classification on strongly regular graphs does not dominate this result: the graph used here is the *bipartite incidence graph*, not the strongly regular **point-collinearity graph** of a partial geometry. The new content is the four-branch exact global period law with its uniquely characterized even-projective exception, together with a uniform short-rank formula for all primitive temporal populations.

## Limitations
The result concerns only characteristic two, the stated reversible two-layer rule and incidence graphs of realized partial geometries; it does not assert existence of every parameter parity combination, classify which incidence ranks occur, or determine orbit equivalence under incidence automorphisms. Its proof uses finite-dimensional linear algebra and does not apply to nonlinear excitable dynamics. Historical-priority searches cannot exclude an unindexed equivalent treatment. No independent mathematical audit or peer review has been performed.

## References
1. R. C. Bose, *Strongly regular graphs, partial geometries and partially balanced designs*, Pacific J. Math. 13 (1963), 389–419, DOI:10.2140/pjm.1963.13.389; https://msp.org/pjm/1963/13-2/pjm-v13-n2-p04-p.pdf (first issue dated April 1963; a day of first public release is not asserted).
2. A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297v1, publicly submitted 2013-11-18; https://arxiv.org/abs/1311.4297 .
3. *The incidence-rank clock of reversible waves on finite projective planes*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-incidence-rank-clock-of-reversible-waves-on-finite-projectiv--fe075b4d8619 .
4. *Three universal wave periods and spectrally invisible orbit counts on strongly regular graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-universal-wave-periods-and-spectrally-invisible-orbit-coun--6be21916ed4f .
