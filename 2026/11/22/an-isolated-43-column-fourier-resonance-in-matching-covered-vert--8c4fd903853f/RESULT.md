# An isolated 43-column Fourier resonance in matching-covered vertex sets

## Finding
For each integer \(n\ge1\), consider the complete bipartite graph \(K_{3,n}\) with three labelled left vertices and \(n\) labelled right vertices. Every matching, including the empty matching, supplies one copy of its binary **covered-vertex incidence vector** in \(G_n=\mathbb F_2^{n+3}\). Let \(\mu_n:G_n\to\mathbb N\) count those copies, and let \(T_nf=\mu_n*f\) be unnormalized convolution. Unlike edge-incidence matchings, distinct matchings may contribute to the same covered-vertex vector; multiplicity is essential.

Then
\[
\boxed{T_n\text{ is singular if and only if }n\in\{1,43\}.}
\]
At \(n=1\), its nullity is \(6\). At \(n=43\), its complete zero set consists of Walsh frequencies selecting \(1\) left vertex and \(16\) right vertices, or selecting \(2\) left vertices and \(27\) right vertices. Thus
\[
\boxed{\operatorname{nullity}(T_{43})=6\binom{43}{16}=1,591,092,895,308},\qquad
\boxed{\operatorname{rank}(T_{43})=68,777,651,282,356}.\]
The smallest surviving multiplier magnitude at \(n=43\) is exactly \(2\), and the largest is \(79,594\). Therefore the sharp \(\ell^2\) condition number on the recoverable Fourier subspace is \(39,797\) and the Moore--Penrose pseudoinverse norm is \(1/2\).

## Assumptions and scope
A matching is an arbitrary set of disjoint edges; the empty matching is included. Its covered vertices consist of the endpoints of its chosen edges. The measure \(\mu_n\) counts matchings, not just distinct vertex subsets, and the transform is unnormalized:
\[
W_n(\xi)=\sum_{M\text{ matching in }K_{3,n}}(-1)^{\langle\xi,\mathbf1_{V(M)}\rangle}.
\]
All operators act on counting-measure \(\ell^2(G_n)\), and rank and nullity refer to their full finite-dimensional real or complex linear extensions. Frequencies may be summarized by \(a\), the number of selected vertices on the three-vertex shore, and \(b\), the number on the other shore, where \(0\le a\le3\) and \(0\le b\le n\). The character convention selects a negative sign at each selected vertex.

## Proof
**1. Exact transform.** For integers \(0\le r\le m\), define the elementary sign sum
\[
K_k(r;m)=\sum_{j=\max(0,k-m+r)}^{\min(k,r)}(-1)^j\binom rj\binom{m-r}{k-j},\qquad K_0(r;m)=1.
\]
It is the degree-\(k\) elementary symmetric function of \(m\) signs, of which \(r\) are negative. A size-\(k\) matching chooses \(k\) vertices on each shore and a bijection between the two chosen vertex sets, giving exactly \(k!\) matchings with a given pair of endpoint sets. Consequently,
\[
\boxed{W_n(a,b)=\sum_{k=0}^{\min(3,n)}k!\,K_k(a;3)K_k(b;n).}\tag{1}
\]
In particular this expression does not count edge-incidence Walsh frequencies: it has one sign factor for each *covered vertex*.

**2. Reduction to two cubics.** Let \(x=n-2b\), which satisfies \(|x|\le n\) and \(x\equiv n\pmod2\). The first elementary sign sums on the right shore are \(1\), \(x\), \((x^2-n)/2\), and \((x^3-(3n-2)x)/6\); terms above degree \(n\) vanish automatically. Substituting into (1), for left sign count \(a=0\), yields
\[
W_n(0,b)=x^3+3x^2+(5-3n)x+1-3n
=(x+1)^3+2(x+1)-2-3n(x+1).\tag{2}
\]
For \(a=1\), the left elementary sign sums are \(1,1,-1,-1\), so
\[
W_n(1,b)=(3x+1)n+1-x-x^2-x^3.\tag{3}
\]
Negating **all** vertex signs leaves every matching sign unchanged, since each matched edge has exactly two endpoints. This proves the exact symmetry
\[
W_n(a,b)=W_n(3-a,n-b),\tag{4}
\]
reducing all possible zero multipliers to the two preceding cases.

**3. No zeros in the first case.** Set \(y=x+1\) in (2). If a zero existed with \(y=0\), the value would be \(-2\), a contradiction. For \(y\ne0\), the equality \(3ny=y^3+2y-2\) implies the integer \(y\) divides \(2\). The four possibilities \(y=-2,-1,1,2\) give respective would-be values
\[
n=\frac73,\quad\frac53,\quad\frac13,\quad\frac53,
\]
none an integer. Thus every multiplier with \(a=0\), and by (4) every multiplier with \(a=3\), is nonzero at every \(n\ge1\).

**4. Exact Diophantine resonance in the second case.** Equation (3) can vanish only if
\[
(3x+1)n=x^3+x^2+x-1.\tag{5}
\]
Let \(t=3x+1\). The integer \(t\) is nonzero, coprime to \(27\), and \(t\equiv1\pmod3\). Direct polynomial reduction gives
\[
27(x^3+x^2+x-1)\equiv-34\pmod t.
\]
Thus \(t\mid34\). Of the eight positive and negative divisors of \(34\), precisely \(1,-2,-17,34\) are congruent to \(1\) modulo three. Substitution in (5) gives exactly
\[
(x,n)=(0,-1),\quad(-1,1),\quad(-6,11),\quad(11,43).
\]
The first pair has a negative graph size, while the third violates \(x\equiv n\pmod2\). The two admissible cases therefore are exactly \((x,n)=(-1,1)\) and \((11,43)\), with \(b=(n-x)/2=1\) and \(16\) respectively. Symmetry (4) gives the remaining zeros at \((a,b)=(2,0)\) for \(n=1\), and \((2,27)\) for \(n=43\). These are all zeros by steps 2–3.

**5. Nullities and sharp spectral gap.** The characters on \(G_n\) diagonalize counting convolution. There are \(\binom3a\binom nb\) frequencies with a given pair \((a,b)\), so the just-proved zero classification yields nullity \(3+3=6\) at \(n=1\), and \(3\binom{43}{16}+3\binom{43}{27}=6\binom{43}{16}\) at \(n=43\). The latter rank is \(2^{46}\) minus that nullity. For \(n=43\), the total matching count is
\[
\sum_{k=0}^3\binom3k\binom{43}k k!=43^3+2\cdot43+1=79,594.
\]
Every sign is one modulo two, hence all multipliers are even. But at \(a=0\) and \(b=22\), equation (2) has \(x=-1\) and value \(-2\); the smallest nonzero magnitude is therefore \(2\). The trivial character realizes the full count \(79,594\), which bounds all absolute multipliers by the triangle inequality. The Fourier diagonalization gives both the sharp condition number and pseudoinverse norm stated above.

## Verification
The standalone Python 3 file `verify.py` uses only the standard library. It independently enumerates all matchings by row recursion and directly sums character phases for all \(2^{n+3}\) characters at each \(1\le n\le7\). It compares these against both (1) and (2)–(4), checks all character-weight classes up to \(n=160\), tests exact Parseval sums at eleven sizes, and replays the finite divisibility certificates and the 43-column nullity and multiplier extrema. Its execution produces `MATCHED_VERTEX_K3N_EXACT_PASS 54381`. These finite tests check the implementation and endpoint arithmetic; the Diophantine argument in the proof establishes the all-order statement.

## Relationship to prior work
The vertex-activity matching generating polynomial is classical. In particular, Wagner's 2004/2008 treatments furnish general weighted matching and degree-constrained-subgraph polynomial constructions. Their general zero-free regions require positivity or half-plane restrictions on activities and do not classify the special mixed \(\pm1\) vertex assignments in (3), where the isolated 43-column cancellation occurs. The new claim is not the definition of this classical polynomial: it is the **complete integer sign-specialization zero locus and resulting Fourier rank classification**.

A public result titled *Complete Walsh singularity and sharp spectral gap for all matchings of \(K_{3,n}\)* concerns the edge-incidence transform on \(\mathbb F_2^{3n}\), with independently assignable signs to all edges. The present characters are induced by products of vertex signs \(z_{ij}=u_iv_j\), a restricted subfamily of edge characters, and the operator lives instead on \(\mathbb F_2^{n+3}\) with multiplicities. The earlier criterion (singular at all odd column counts for the full edge-character space) does not identify the exact induced zero locus, which here is confined to one odd column count above one. A separate public two-edge-only matching result omits all other matching sizes and does not imply (3). An equivalent older signed-rook specialization may exist and historical priority is not independently certified.

## Limitations
The theorem does not classify edge-incidence Fourier multipliers, arbitrary bipartite graphs, larger fixed left shores, or the sharp inverse condition number for every invertible \(n\). It concerns a multiplicity-weighted measure, not the unweighted set of realizable covered-vertex subsets. All-size correctness follows from the proof rather than the finite checker. The claim is not independently audited; its historical-priority comparison is bounded to the inspected sources and indexed records.

## References
1. D. G. Wagner, *Enumeration of spanning subgraphs with degree constraints*, arXiv:math/0412059v1, first submitted 2004-12-02, https://arxiv.org/abs/math/0412059.
2. D. G. Wagner, *Weighted enumeration of spanning subgraphs with degree constraints*, arXiv:0803.1659v1, first submitted 2008-03-11, https://arxiv.org/abs/0803.1659.
3. *Complete Walsh singularity and sharp spectral gap for all matchings of \(K_{3,n}\)*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-complete-walsh-singularity-and-sharp-spectral-gap-for-all-matchi--5bf177d89df5.
4. *Exact zero-free residues and sharp Fourier norms for two-edge matchings in \(K_{3,n}\)*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-zero-free-residues-and-sharp-fourier-norms-for-two-edge-ma--9046021fcb99.
