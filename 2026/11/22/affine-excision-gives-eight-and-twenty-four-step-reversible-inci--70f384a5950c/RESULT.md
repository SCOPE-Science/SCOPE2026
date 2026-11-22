# Affine excision gives eight- and twenty-four-step reversible incidence-wave clocks

## Finding
Let \(\mathcal A\) be **any** finite affine plane of order \(s\ge2\), not necessarily Desarguesian, with \(s^2\) points and \(s^2+s\) lines. Let \(B\) be its binary point-line incidence matrix, \(A=\left(\begin{smallmatrix}0&B\\B^{\mathsf T}&0\end{smallmatrix}\right)\) the binary adjacency of its Levi graph, \(N=2s^2+s\), and \(Q=2^f\) for any \(f\ge1\). The reversible two-level linear map on \(\mathbb F_Q^{2N}\) is
\[
T(u,v)=(Au+v,u).
\]
Every state is periodic from time zero. The **exact order** of \(T\) is \(8\) for even \(s\), and \(24\) for odd \(s\). In particular, these are sharp least temporal periods attained by individual states. This is a different parity law from the previously determined projective-plane incidence-wave orders \(12\) (even order) and \(6\) (odd order); deleting a line at infinity and its points can remove or introduce a factor of three in the global clock.

The complete fixed-time census and primitive temporal-orbit counts are as follows. Write \(b(t)=2^{\nu_2(t)}\), \(\rho=\operatorname{rank}_{\mathbb F_2}B\), and, for even \(s\),
\[
n_3=s+1,\qquad n_2=2\rho-2(s+1),\qquad n_1=2s^2+2s+1-4\rho.
\]
These are nonnegative integers. The number of labelled two-level states fixed by the \(t\)-th update is \(Q^{D_s(t)}\), for every integer \(t\ge1\), with
\[
D_s(t)=\begin{cases}
 n_1\min(b(t),2)+n_2\min(b(t),4)+n_3\min(b(t),6),&s\text{ even},\\
 \min(b(t),6)+(s-1)\min(b(t),2)
  +2(s^2-1)\mathbf1_{3\mid t}\min(b(t),2),&s\text{ odd}.
\end{cases}
\]
For every divisor \(d\) of the appropriate sharp order, the numbers of least-period-\(d\) states and temporal orbits are, respectively,
\[
P_d=\sum_{e\mid d}\mu(d/e)Q^{D_s(e)},\qquad C_d=P_d/d.
\]
All other least periods are impossible. The census determines \(\rho\) when \(s\) is even, since \(D_s(1)=N-2\rho\); for odd \(s\), \(\rho=s^2\) and \(D_s(1)=s\). Thus affine incidence rank is dynamically observable without identifying individual incidence codewords.

## Assumptions and scope
An affine plane of order \(s\) means a finite point-line incidence structure in which every two points lie on exactly one line, every line has \(s\) points, every point belongs to \(s+1\) lines, and the lines split into \(s+1\) parallel classes, each of size \(s\). Distinct parallel lines are disjoint, and distinct nonparallel lines intersect in exactly one point. Both abstract/non-Desarguesian and finite-field planes are included. Matrix entries are reduced modulo two, but the evolving state may lie over any finite extension \(\mathbb F_Q\) of \(\mathbb F_2\). Point labels, line labels, the two ordered time levels, and temporal phases are retained; no spatial or phase quotient is taken. All incidence ranks are over \(\mathbb F_2\), unchanged on extension to \(\mathbb F_Q\).

## Proof
**Step 1: Universal incidence identities.** Put \(P=s^2\), \(L=s^2+s\), and let \(J\) denote an all-ones matrix of the indicated size. Pairwise uniqueness of lines through points gives
\[
BB^{\mathsf T}=sI_P+J_P.
\]
Partition the line coordinates by their \(s+1\) parallel classes. The line-intersection Gram matrix has diagonal \(s\), zero off-diagonal within a parallel class, and one across distinct classes. In particular, when \(s\) is even,
\[
B^{\mathsf T}B=(J_{s+1}+I_{s+1})\otimes J_s
\]
over characteristic two, and this has rank \(s\), because \(J_{s+1}+I_{s+1}\) has rank \(s\) and \(J_s\) rank one. In all cases \(A=\left(\begin{smallmatrix}0&B\\B^{\mathsf T}&0\end{smallmatrix}\right)\) and \(\operatorname{rank}A=2\rho\).

**Step 2: Even plane order.** If \(s\) is even, then \(BB^{\mathsf T}=J_P\), and \(J_P^2=PJ_P=0\). Every line has an even number of points, so \(B^{\mathsf T}\mathbf1_P=0\). Consequently \(BB^{\mathsf T}B=J_PB=0\) and \(B^{\mathsf T}BB^{\mathsf T}=B^{\mathsf T}J_P=0\), hence \(A^3=0\). By Step 1,
\[
\operatorname{rank}A^2=\operatorname{rank}(BB^{\mathsf T})+\operatorname{rank}(B^{\mathsf T}B)=1+s.
\]
For a nilpotent matrix with index at most three, successive ranks determine its Jordan multiplicities: there are \(\operatorname{rank}A^2=s+1\) size-three blocks, \(\operatorname{rank}A-2\operatorname{rank}A^2=2\rho-2s-2\) size-two blocks, and \(N-2\operatorname{rank}A+\operatorname{rank}A^2=2s^2+2s+1-4\rho\) size-one blocks. These are \(n_3,n_2,n_1\). The positive size-three multiplicity forces the later period eight, not merely a divisor of eight.

**Step 3: Odd plane order.** If \(s\) is odd, \(BB^{\mathsf T}=I_P+J_P\), with \(P\) odd and \(J_P^2=J_P\); its rank is \(P-1\). The incidence matrix \(B\) has **full row rank** \(P\). Indeed if \(y^{\mathsf T}B=0\), then \((I_P+J_P)y=BB^{\mathsf T}y=0\), so \(y=c\mathbf1_P\). But \(B^{\mathsf T}\mathbf1_P=\mathbf1_L\), since every line contains the odd number \(s\) of points; therefore \(c=0\).

Let \(W=\ker(\mathbf1_P^{\mathsf T})\), of dimension \(P-1\). Since \((I_P+J_P)w=w\) for \(w\in W\), the paired subspace \(W\oplus B^{\mathsf T}W\) is \(A\)-invariant and \(A\) exchanges \((w,0)\) and \((0,B^{\mathsf T}w)\). It therefore consists of \(P-1\) adjacency Jordan blocks \(J_2(1)\). The complementary generalized zero eigenspace has dimension \(N-2(P-1)=s+2\). The two off-diagonal blocks of \(A^3\) are \((I_P+J_P)B\) and \(B^{\mathsf T}(I_P+J_P)\); each has rank \(P-1\) because \(B\) is surjective and \(B^{\mathsf T}\) injective. Thus \(\operatorname{rank}A^3=2(P-1)\). Since \(\operatorname{rank}A=2P\) and \(\operatorname{rank}A^2=(P-1)+P=2P-1\), the zero part has precisely one \(J_3(0)\) and \(s-1\) copies of \(J_1(0)\). Indeed, \(A^4\) has diagonal blocks \((I_P+J_P)^2=I_P+J_P\) and \(B^{\mathsf T}(I_P+J_P)B\), each of rank \(P-1\), since \(B\) is surjective and \(B^{\mathsf T}\) injective. Thus \(\operatorname{rank}A^4=2(P-1)=\operatorname{rank}A^3\), ruling out zero-primary blocks of length greater than three.

**Step 4: Transfer of adjacency blocks to wave blocks.** The inverse of \(T=\left(\begin{smallmatrix}A&I\\I&0\end{smallmatrix}\right)\) is \(\left(\begin{smallmatrix}0&I\\I&A\end{smallmatrix}\right)\), proving reversibility. A nilpotent adjacency block \(J_j(0)\), \(j=1,2,3\), produces one temporal Jordan block \(J_{2j}(1)\). To see this, the corresponding two-level characteristic polynomial is \((X^2+1)^j=(X+1)^{2j}\), and a fixed wave state has \(u=v\) with \(Au=0\). Its fixed space has dimension one for each single adjacency block, forcing a *single* temporal Jordan block of length \(2j\).

The adjacency block \(J_2(1)\) produces one cyclic temporal block \(\mathbb F_Q[X]/(X^2+X+1)^2\) of dimension four. Its characteristic polynomial is \((X^2+X+1)^2\). Writing \(h(X)=X^2+X+1\), the identity \(h(T)=(I+\operatorname{diag}(A,A))T\) shows that \(h(T)\) is nonzero, has square zero, and has kernel dimension two on that four-space; therefore the block is \(h^2\), not two blocks of \(h\). This remains true when \(h\) splits over a larger characteristic-two field.

Thus for even \(s\) there are \(n_j\) temporal \((X+1)^{2j}\) blocks for \(j=1,2,3\). For odd \(s\) the temporal decomposition is one \((X+1)^6\) block, \(s-1\) blocks \((X+1)^2\), and \(s^2-1\) blocks \(h(X)^2\). The stated decompositions and multiplicities are exact over the prime field and remain exact after scalar extension.

**Step 5: Time-fixed dimensions, periods, and rank recovery.** For a cyclic block \(\mathbb F_Q[X]/g(X)\), the dimension fixed by its \(t\)-th power is \(\deg\gcd(g(X),X^t-1)\). In characteristic two, \(X+1\) occurs in \(X^t-1\) with multiplicity \(b(t)\), and \(h(X)\) occurs exactly if \(3\mid t\), then also with multiplicity \(b(t)\). Summing over the temporal blocks gives \(D_s(t)\) as stated. In the even case at least one \((X+1)^6\) block has order eight, which is the largest block order. In the odd case the \((X+1)^6\) block has order eight, while each \(h(X)^2\) block has order six; since \(s\ge3\), both occur and their least common multiple is exactly twenty-four. Direct sums of a vector attaining each component order attain the full order. Möbius inversion over divisors now gives \(P_d\) and \(C_d\). Finally \(\dim\operatorname{Fix}T=\dim\ker A=N-2\rho\) always; for odd \(s\), \(\rho=P\), giving \(s\) as claimed.

## Verification
The included standalone integer-only programs `check_matrix.py` and `check_jordan.py` are executable with Python 3 and have no nonstandard dependencies. The first independently constructs incidence matrices of \(\mathrm{AG}(2,s)\) for \(s=2,3,4,5\), forms the complete binary wave matrix, and calculates actual nullities of \(T^t-I\) for each divisor of the claimed sharp global period. The second checks the point-line incidence ranks and the independently constructed adjacency-power ranks \(A^0,\ldots,A^4\); these are the structural invariants used in the proof. Both successfully completed; `matrix_results.txt` and `jordan_results.txt` contain their exact outputs. For \(s=4\) the construction uses the four-element field. The finite checks corroborate the argument but do not establish the theorem for all finite planes; Steps 1–5 do.

## Relationship to prior work
The reversible two-level update is a standard second-order cellular-automaton construction, including in Vlasov's 2013 paper, Section 3. Incidence designs and their binary codes are classical subjects; no priority is claimed for the affine-plane incidence identities or modular-rank notions. A published projective-plane wave classification gives exact orders \(6\) and \(12\) for the **square**, projective incidence matrices; those formulas do not apply to the rectangular affine incidence matrix, whose block structure and zero-primary components differ. Another published reversible-wave census for complete multipartite graphs also identifies order \(24\) on certain unrelated graphs, but the affine Levi graph is not complete multipartite, and the affine-plane Jordan multiplicities and rank-recovery law do not follow from that family theorem. The new assertion is the all-affine-plane temporal classification, including non-Desarguesian planes, and its rank-sensitive fixed-point data, not the construction of a reversible automaton itself.

## Limitations
The claimed clocks concern only characteristic-two finite fields and the specified two-level neighbor-sum update. For even plane order the individual fixed-state counts depend on \(\rho\), which the theorem does not evaluate for every possible non-Desarguesian plane; it gives an exact formula once that intrinsic incidence rank is known. The theorem does not classify the possible binary ranks of nonisomorphic affine planes, nor does identical temporal data imply isomorphism. Computational checks cover four Desarguesian examples; the universal conclusion rests on the incidence-axiom proof. Independent mathematical audit has not been performed, and unindexed historical overlap remains possible.

## References
- A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297, first submitted 2013-11-18, Section 3. https://arxiv.org/abs/1311.4297
- D. C. Clark, D. Jungnickel and V. D. Tonchev, *Exponential bounds on the number of designs with affine parameters*, first published online 2010-09-29, DOI 10.1002/jcd.20256. Background on affine incidence designs. https://doi.org/10.1002/jcd.20256
- M. Lavrauw, L. Storme and G. Van de Voorde, *On the code generated by the incidence matrix of points and hyperplanes in PG(n,q) and its dual*, arXiv:1201.3290, first submitted 2012-01-16. Background on modular incidence-code methods. https://arxiv.org/abs/1201.3290
- *The incidence-rank clock of reversible waves on finite projective planes*, published research record, complete result and proof. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-incidence-rank-clock-of-reversible-waves-on-finite-projectiv--fe075b4d8619/RESULT.md
- *Twenty-four-step resonances in reversible waves on complete multipartite graphs*, published research record, complete result and proof. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-twenty-four-step-resonances-in-reversible-waves-on-complete-mult--addc32219e63/RESULT.md
