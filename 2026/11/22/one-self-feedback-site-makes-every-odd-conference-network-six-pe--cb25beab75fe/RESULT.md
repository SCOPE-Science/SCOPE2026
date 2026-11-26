# One self-feedback site makes every odd conference network six-periodic

## Finding

Let \(G\) be any finite nontrivial conference strongly regular graph with \(v\equiv5\pmod8\) vertices and parameters
\[
\left(v,\frac{v-1}{2},\frac{v-5}{4},\frac{v-1}{4}\right).
\]
Fix any vertex \(s\), let \(A\) be the ordinary loopless adjacency matrix, and let \(e\) be the coordinate vector of \(s\). Over any finite field \(\mathbb F_Q\) of characteristic two, with \(Q=2^f\) and \(f\ge1\), consider synchronous neighbor-sum dynamics on labelled configurations \(x\in\mathbb F_Q^v\). Introduce exactly one local self-input by setting \(B=A+ee^{\mathsf T}\).

**Theorem.** The modified evolution is bijective, has exact global order six, and every initial configuration is periodic from time zero. Its only possible least periods are \(1\), \(3\), and \(6\). The exact numbers of *configurations* with those least periods are
\[
\boxed{P_1=Q,\qquad P_3=Q^{v-2}-Q,\qquad P_6=Q^v-Q^{v-2}.}
\]
The corresponding numbers of labelled primitive temporal orbits are
\[
\boxed{C_1=Q,\qquad C_3=\frac{Q^{v-2}-Q}{3},\qquad C_6=\frac{Q^v-Q^{v-2}}6.}
\]
All three populations are nonzero. In sharp contrast, the unmodified evolution \(x\mapsto Ax\) is noninvertible: it has the unique fixed configuration zero, \(Q^{v-1}-1\) immediate period-three configurations, and \(Q^v-Q^{v-1}\) configurations taking exactly one update to become periodic; \(A^4=A\). Thus one self-feedback input eliminates the one-step transient sector and produces primitive period-six orbits. This compares the two population distributions; it does not assign period six to every formerly transient configuration.

## Assumptions and scope

All graphs are simple, loopless and undirected before the stated local change. The strongly regular parameters impose \(0<(v-1)/2<v-1\), so the network is neither empty nor complete; \(v\ge5\). The set of all admissible graphs is quantified, not only Paley graphs. In particular, a Paley graph over the graph-vertex field of prime-power order \(v\equiv5\pmod8\) is an example; the *state* field \(\mathbb F_Q\) is a separate field of characteristic two. All sums are in the state field. The symbol \(J\) denotes the all-one matrix and \(\mathbf1\) the all-one column. Temporal orbits are counted without quotienting by graph automorphisms.

## Proof

**1. Conference parameters give a universal quadratic identity.** Write \(k=(v-1)/2\), \(\lambda=(v-5)/4\), and \(\mu=(v-1)/4\). Because \(v\equiv5\pmod8\), the degree \(k\) and \(\lambda\) are even, whereas \(\mu\) is odd. The standard common-neighbor identity
\[
A^2=kI+\lambda A+\mu(J-I-A)
\]
therefore becomes, in characteristic two,
\[
A^2=A+I+J,\qquad A\mathbf1=0,\qquad AJ=JA=0.
\]
As \(v\) is odd, \(J^2=J\). These identities depend only on the conference parameters.

**2. A rank-two square-zero obstruction.** Put \(u=Ae\), \(w=\mathbf1+e\), and \(E=ee^{\mathsf T}\). The distinguished vertex has no self-loop, so \(e^{\mathsf T}u=0\). Since \(u\) contains exactly \(k\) ones and \(w\) contains \(v-1\) ones, both even, their ordinary bilinear products satisfy
\[
u^{\mathsf T}u=w^{\mathsf T}w=u^{\mathsf T}w=0.
\]
The vectors \(u,w\) are independent because \(0<k<v-1\) and their supports differ. Expanding \(B=A+E\), noting \(E^2=E\), yields
\[
B^2+B+I=J+ue^{\mathsf T}+eu^{\mathsf T}.
\]
From the quadratic identity,
\[
(B+I)\mathbf1=w,\qquad (B+I)e=u,\qquad (B+I)u=w.
\]
Consequently
\[
\boxed{B^3+I=ww^{\mathsf T}+uu^{\mathsf T}=:N.}
\]
The map \(N\) has image \(U=\operatorname{span}\{w,u\}\) and rank two, because both pairs of vectors are linearly independent. The displayed bilinear products give \(N^2=0\). Hence
\[
B^6=(I+N)^2=I.
\]
This already proves bijectivity, immediate periodicity, and the absence of any period not dividing six. Further, \(N\ne0\), so \(B^3\ne I\).

**3. Exactly which short periods occur?** On the \(B\)-invariant plane \(U\),
\[
Bw=u,\qquad Bu=w+u.
\]
The matrix of \(B|_U\) in the ordered basis \((w,u)\) is \(\begin{psmallmatrix}0&1\\1&1\end{psmallmatrix}\), whose polynomial is \(t^2+t+1\). Thus it has order three and no eigenvector of eigenvalue one. The global order is exactly six: it divides six and is divisible by both three (from \(U\)) and two (since \(B^3\ne I\)).

For a fixed configuration \(Bx=x\), the equation \((B^2+B+I)x=x\) shows \(x\in\operatorname{span}\{\mathbf1,e,u\}\). Since
\[
B\mathbf1=e,\qquad Be=e+u,\qquad Bu=\mathbf1+e+u,
\]
solving the three coefficients gives
\[
\operatorname{Fix}(B)=\operatorname{span}\{\mathbf1+u\},\qquad \dim\ker(B+I)=1.
\]
There can be no least-period-two states. Indeed, suppose \(B^2x=x\) and put \(y=(B+I)x\). Then \((B+I)y=0\). The identity \(Nx=(B^3+I)x=(B+I)x=y\) shows \(y\in U\). However, \(B+I\) is invertible on \(U\), because its restriction has no eigenvalue one. Thus \(y=0\), or \(Bx=x\). Therefore \(\ker(B^2+I)=\ker(B+I)\).

Because \(N=B^3+I\) has rank two, \(\dim\operatorname{Fix}(B^3)=v-2\). In a finite \(Q\)-element field, these fixed spaces have respective sizes \(Q\), \(Q\), and \(Q^{v-2}\) at powers one, two, and three. Inclusion–exclusion over the divisors of six now yields \(P_1=Q\), \(P_3=Q^{v-2}-Q\), and \(P_6=Q^v-Q^{v-2}\). Division by the respective least periods gives the primitive temporal-orbit counts. The counts are integral because the entire state set is partitioned into actual cycles.

**4. Comparison with no feedback.** Let \(H=\ker\mathbf1^{\mathsf T}\) have dimension \(v-1\). Since \(v\) is odd, the ambient space splits as \(\langle\mathbf1\rangle\oplus H\). The operator \(A\) is zero on the constant line, and on \(H\) the equality \(J=0\) gives \(A^2+A+I=0\), hence \(A^3=I\). The polynomial \(t^2+t+1\) has no root one in characteristic two, so no nonzero vector of \(H\) is fixed, and every such vector has least period three. In the full space, vectors of \(H\) are periodic immediately; vectors outside \(H\) lose their constant component after one update, and no earlier. This proves every unmodified population stated above and \(A^4=A\).

## Verification

The included standard-library programs `check_matrix.py` and `check_states.py` implement separate direct checks of the update. The first constructs prime-order Paley adjacency matrices and tests matrix powers and ranks of \(B^3+I\), \(B+I\), \(B^2+I\) and \(A\) at prime orders \(5,13,29,37,53,61,101\). The second directly traces all \(8{,}224\) binary configurations on the Paley graphs of order five and thirteen, separately under the modified and unmodified dynamics. The console outputs in `verification_run.txt` report the predicted ranks, period counts and transient counts. These finite tests are corroboration; the proof establishes the theorem for all admissible graphs and characteristic-two finite extension fields.

## Relationship to prior work

Haemers, Peeters and van Rijckevorsel (1999), Proposition 3.1 and Section 4.3, show that for these conference parameters the binary adjacency code has dimension \(v-1\), using \(A^2=A+I+J\); their result supplies the unperturbed matrix structure, but does not state the dynamics after inserting one diagonal feedback entry, or the resulting temporal orbit census. Lim and Praeger (2006) establish the structural Paley graph setting and automorphisms, not the local-feedback dynamics. The one-site feedback result for Boolean hypercubes [4] treats a different adjacency identity over the binary field and includes least period two in odd dimension. The characteristic-two facet-feedback result [5] also has least periods one, three and six, but uses feedback on every vertex of a cube facet and has different populations. Reversible *second-order* waves on strongly regular graphs [6] use pairs of successive configurations and do not imply the present *first-order* update. The additional input here is the rank-two nilpotent identity for \(B^3+I\), which gives the population classification for the stated conference parameters.

## Limitations

The theorem assumes precisely the conference parameter class with \(v\equiv5\pmod8\) and one self-input; it does not classify multiple feedback sites, other parameter congruences, odd-characteristic state fields, or nonlinear rules. The proof relies only on the parameter identity, not graph vertex transitivity. Historical priority is assessed by best-knowledge comparison and cannot exclude unindexed equivalent work.

## References

1. W. H. Haemers, M. J. P. Peeters and J. M. van Rijckevorsel, *Binary Codes of Strongly Regular Graphs*, Designs, Codes and Cryptography 17 (1999), 187–209, especially Proposition 3.1 and Section 4.3. https://pure.uvt.nl/ws/files/327256/fulltext.pdf
2. T. K. Lim and C. E. Praeger, *On generalised Paley graphs and their automorphism groups*, arXiv:math/0605252v1, first posted 2006-05-10. https://arxiv.org/abs/math/0605252
3. A. N. Elsawy, *Paley Graphs and Their Generalizations*, arXiv:1203.1818v1, first posted 2012-03-07. https://arxiv.org/abs/1203.1818
4. One-site feedback on Boolean cubes. https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-a-one-site-feedback-defect-creates-periods-three-and-six-on-bool--a9a2b0b84ed9
5. Facet feedback on Boolean cubes. https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-facet-feedback-converts-cube-parity-dynamics-into-a-universal-si--8779035d2a61
6. Reversible waves on strongly regular graphs. https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-three-universal-wave-periods-and-spectrally-invisible-orbit-coun--6be21916ed4f
