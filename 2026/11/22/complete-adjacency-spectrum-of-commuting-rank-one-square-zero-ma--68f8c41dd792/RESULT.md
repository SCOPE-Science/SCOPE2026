# Complete adjacency spectrum of commuting rank-one square-zero matrices over finite fields

## Finding
Let \(q\) be a prime power, let \(n\ge4\), and form the *simple* graph \(\Gamma_{n,q}\) on **all actual nonzero** rank-one square-zero matrices in \(M_n(\mathbb F_q)\): distinct matrices are adjacent exactly when they commute. Put
\[
[m]_q=\frac{q^m-1}{q-1},\quad v=[n]_q,\quad t=[n-1]_q,\quad s=[n-2]_q,\quad Q=q^{n-3},\quad F=vt,\quad k=t+(t-1)s.
\]
The graph has \((q-1)F\) vertices and degree \((q-1)k-1\). Its **complete real adjacency spectrum, with multiplicity and with equal numerical values combined**, is the following multiset:

| Adjacency eigenvalue | Multiplicity |
| :--- | ---: |
| \((q-1)k-1\) | \(1\) |
| \((q-1)(q^{n-2}+s q^{(n-2)/2})-1\) | \(v-1\) |
| \((q-1)(q^{n-2}-s q^{(n-2)/2})-1\) | \(v-1\) |
| \((q-1)q^{n-2}-1\) | \(a=\dfrac{q^2[n-3]_q[n]_q}{q+1}\) |
| \(-(q-1)q^{n-3}-1\) | \(b=\dfrac{q^3[n-2]_q[n-1]_q}{q+1}\) |
| \(-1\) | \((q-2)F\) |

In particular, the adjacency matrix is nonsingular for all \(n\ge4\) and all prime powers \(q\), despite the scalar-copy contribution at eigenvalue \(-1\). The eigenvalue list remains valid at \(n=3\), with \(a=0\); the main claim concerns the genuinely higher-dimensional range.

## Assumptions and scope
The field includes characteristic two. Here \(\operatorname{rank}A=1\), \(A\ne0\), and \(A^2=0\) are simultaneous vertex conditions; scalar multiples are **distinct** vertices when their scalars differ. Adjacency has no loops. Eigenvalues are those of the ordinary real symmetric \(0\)-\(1\) adjacency matrix, not of a normalized walk or of an association-scheme quotient. When numerical eigenvalues coincide in a small parameter case (for instance \(q=2,n=4\)), their multiplicities are added. For \(q=2\), the \(-1\)-multiplicity in the last line is zero. The displayed \(a,b\) are nonnegative integers as established by the spectral decomposition.

## Proof
**1. Algebra-to-flag identification.** Write a nonzero rank-one square-zero matrix as \(A=u\varphi\), where \(u\in\mathbb F_q^n\setminus0\), \(\varphi\in(\mathbb F_q^n)^*\setminus0\), and \(\varphi(u)=0\). Its image point \(P=\langle u\rangle\) belongs to its kernel hyperplane \(H=\ker\varphi\). Each incident point–hyperplane flag \((P,H)\) has exactly \(q-1\) matrices. For another such \(B=w\psi\), one has \(AB=\varphi(w)u\psi\) and \(BA=\psi(u)w\varphi\). Equality of nonzero products would imply equal image and kernel for \(A,B\), hence scalar proportionality and then \(AB=0\), a contradiction. Thus commuting is equivalent to both products vanishing, namely \(P\subseteq K\) and \(R\subseteq H\) for flags \((P,H),(R,K)\).

**2. The loop-retaining flag operator.** Let \(\mathcal F\) be the \(F=vt\) incident flags. Define the symmetric \(F\times F\) integer matrix
\[
B_{(P,H),(R,K)}={\bf1}_{P\subseteq K}{\bf1}_{R\subseteq H}.
\]
In particular \(B\) has diagonal entries one and constant row sum \(k=t+(t-1)s\). Choose an arbitrary order on the scalar copies. The adjacency matrix of \(\Gamma_{n,q}\) is a permutation similarity of \(B\otimes J_{q-1}-I_{(q-1)F}\), where \(J_j\) denotes the all-ones matrix. It therefore suffices to diagonalize \(B\).

**3. A full invariant point–hyperplane sector.** Let \(\mathcal U\subseteq\mathbb R^{\mathcal F}\) consist of functions \(f(P,H)=\alpha(P)+\beta(H)\). Because the incidence bipartite graph is connected, \(\dim\mathcal U=2v-1\). Write \(M\) for its \(v\times v\) point–hyperplane incidence matrix. Then
\[
MM^{\mathsf T}=(t-s)I_v+sJ_v,\qquad t-s=q^{n-2}.
\]
On functions of points alone, \(B\alpha(P,H)=q^{n-2}\alpha(P)+s\sum_{R\subseteq H}\alpha(R)\). Dually, on hyperplane functions \(B\beta(P,H)=q^{n-2}\beta(H)+s\sum_{K\supseteq P}\beta(K)\). The constant function has eigenvalue \(k\); on the two coupled zero-sum incidence modules the eigenvalues are \(q^{n-2}\pm s q^{(n-2)/2}\), each of multiplicity \(v-1\). Thus all of \(\mathcal U\) is diagonalized.

**4. Explicit quadratic identity on the orthogonal sector.** Put \(h=[n-3]_q\). For flags \(i=(P,H)\) and \(j=(R,K)\), a direct count of intermediate incident flags gives
\[
\begin{split}
\bigl(B^2-(q-1)QB-qQ^2I\bigr)_{ij}
={}&sh+Q\bigl({\bf1}_{P\subseteq K}+{\bf1}_{R\subseteq H}\bigr)\\
&+(s-1)Q\,{\bf1}_{P=R}+(t-s)h\,{\bf1}_{H=K}.
\end{split}
\tag{1}
\]
Here is a complete case derivation. In \(B^2_{ij}\), the intermediate point \(S\) lies in \(H\cap K\), and its intermediate hyperplane must contain \(\langle P,R,S\rangle\). If \(P=R\), the intersection includes \(P\); counting its \(t\) or \(s\) points gives respectively \(t[n-2]_q+q^{n-2}\) if \(H=K\), and \(s[n-2]_q+q^{n-2}\) otherwise. If \(P\ne R\), put \(L=\langle P,R\rangle\). For \(H=K\), the count is \(th+(q+1)Q\). For \(H\ne K\), the intersection \(L\cap H\cap K\) has respectively \(q+1\), one or zero projective points as both, exactly one or neither cross-incidence holds; hence the count is \(sh+(q+1)Q\), \(sh+Q\) or \(sh\). Subtracting the two specified matrix terms gives (1), including its diagonal. Every term on the right of (1), acting on an arbitrary function of \((R,K)\), produces a function of \(P\) alone or of \(H\) alone. Thus (1) maps into \(\mathcal U\). Since \(B\) is symmetric and preserves \(\mathcal U\), on \(\mathcal U^\perp\) the operator satisfies
\[
(B-q^{n-2}I)(B+QI)=0.
\]
All its real eigenvalues there are therefore \(q^{n-2}\) or \(-Q\), with multiplicities \(a,b\).

**5. Exact residual multiplicities.** The dimensions and diagonal of \(B\) yield
\[
a+b=F-2v+1,\quad
q^{n-2}a-Qb=F-k-2(v-1)q^{n-2}.
\]
Solving and substituting the projective-point counts gives
\[
a=\frac{q^2[n-3]_q[n]_q}{q+1},\qquad b=\frac{q^3[n-2]_q[n-1]_q}{q+1}.
\]
The \(q-1\) scalar copies transform every eigenvalue \(\lambda\) of \(B\) into \((q-1)\lambda-1\); the scalar-copy orthogonal directions contribute \(-1\) with multiplicity \((q-2)F\). This proves the table and its dimension sum.

**6. Nonsingularity.** For \(n\ge4\), \(s>q^{(n-2)/2}\), hence \(q^{n-2}-s q^{(n-2)/2}<0\); the other nontrivial positive eigenvalues of \(B\) are at least \(q^{n-2}\). Therefore none of the transformed eigenvalues equals zero, since \((q-1)q^{n-2}>1\). The extra eigenvalue \(-1\) is also nonzero.

## Verification
The included `checker.py` independently constructs projective points and hyperplanes over prime fields and \(\mathbb F_4\), builds the exact incidence matrix, verifies the operator identity (1) entrywise with integer arithmetic, and compares the complete predicted spectrum with real-symmetric diagonalization. For \((q,n)=(2,3),(3,3)\), it additionally checks all flag-pair adjacencies via ordinary matrix multiplication of the represented rank-one nilpotents. Tested parameter pairs: \((2,3),(3,3),(4,3),(2,4),(3,4),(2,5)\). All tests passed; maximum absolute numerical eigenvalue discrepancy was below \(10^{-12}\). See `checker_output.txt`. These finite computations are not the proof of the general result; steps 1–6 are.

## Relationship to prior work
Dolinar, Kuzma and Oblak (arXiv:1009.5543, publicly submitted 2010-09-28) study distances and rank-one matrices in commuting graphs of matrix algebras, not a finite-field rank-one square-zero adjacency eigenvalue census. Related published work on the same finite-field rank-one nilpotent graph determines maximal cliques, their polynomial, diameter and common-neighbor distinctions (see references below); their results identify the underlying flag graph but contain no global eigenvalue/multiplicity calculation. Boroja, Kokol Bukovšek and Stopar (arXiv:2602.07467) describe the three-by-three compressed commuting graph over prime fields, including its point-line flag component; the main claim here concerns every dimension \(n\ge4\). De Beule, Mattheus and Metsch (arXiv:2007.01104) calculate spectra of *oppositeness* relations in flag buildings, not the present *mutual cross-incidence* relation (which includes same-point and same-hyperplane flags). The general Iwahori–Hecke/association-scheme literature remains a potential source of implicit prior coverage; the proof is elementary and self-contained but independent historical-priority validation has not occurred.

## Limitations
The spectrum covers the induced graph of **rank-one** nonzero square-zero matrices, not arbitrary nilpotent matrices or the whole matrix commuting graph. The results concern finite fields, not arbitrary finite rings. The spectrum may have coincident entries, so the table denotes a multiset. The literature checks distinguish explicit stronger statements from new calculations but cannot exclude every historical representation-theoretic reformulation. No independent validation has been performed.

## References
- G. Dolinar, B. Kuzma, P. Oblak, *On maximal distances in a commuting graph*, arXiv:1009.5543 (first public 2010-09-28), https://arxiv.org/abs/1009.5543.
- J. De Beule, S. Mattheus, K. Metsch, *An algebraic approach to Erdős–Ko–Rado sets of flags in spherical buildings*, arXiv:2007.01104, https://arxiv.org/abs/2007.01104.
- I.-V. Boroja, D. Kokol Bukovšek, N. Stopar, *Unital compressed commuting graph of \(3\times3\) matrices over a finite prime field*, arXiv:2602.07467, https://arxiv.org/abs/2602.07467.
- *Projective geometry and clique spectra of rank-one nilpotent commuting graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-projective-geometry-and-clique-spectra-of-rank-one-nilpotent-com--00e8b0fff4f8.
- *Rank-one nilpotent commuting graphs acquire a second geometric edge class in dimension four*, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-rank-one-nilpotent-commuting-graphs-acquire-a-second-geometric-e--31b2442abb5e.
- *Maximal cliques of the rank-one nilpotent commuting graph over finite fields*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-maximal-cliques-of-the-rank-one-nilpotent-commuting-graph-over-f--449d5040be68.
