# The complete nonzero adjacency spectrum of commuting primitive idempotents over finite fields

## Finding

Let \(q\) be any prime power and \(n\ge4\). The commuting graph \(\Gamma_{n,q}\) has as vertices the rank-one idempotent matrices in \(M_n(\mathbb F_q)\); distinct vertices are joined when they commute. Define
\[
 v=\frac{q^n-1}{q-1},\quad t=\frac{q^{n-1}-1}{q-1},\quad s=\frac{q^{n-2}-1}{q-1},\quad \gamma=q^{n-2},\quad \beta=q^{n-3},\quad k=\gamma t,\quad \alpha=q^{3(n-2)/2}.
\]
Then \(\Gamma_{n,q}\) has \(N=vq^{n-1}\) vertices, is \(k\)-regular, and its full real adjacency eigenvalue multiset is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
 k&1\\
 +\alpha&v-1\\
 -\alpha&v-1\\
 +\beta&\dfrac{q^3ts}{q+1}\\
 +\gamma&\dfrac{(q-2)tv}{2}\\
 -\gamma&\dfrac{q(q-1)tv}{2(q+1)}
\end{array}
\]
The \(+\gamma\) row has multiplicity zero when \(q=2\), and all other multiplicities are positive. These values are pairwise distinct for \(n\ge4\) except the absent row. In particular the adjacency matrix is always nonsingular. For odd \(n\) and nonsquare \(q\), the pair \(\pm\alpha\) is irrational and the graph is not integral.

## Assumptions and scope

All spectra are those of the simple, unweighted, undirected adjacency graph, with the identity/zero matrices excluded because neither is rank one. The result is uniform in the field characteristic. This claim concerns the rank-one-idempotent commuting graph, not the larger commuting graph on all noncentral matrices. The restriction \(n\ge4\) deliberately omits the projective-plane case \(n=3\), which has earlier antiflag association-scheme literature. Here projective points mean one-dimensional subspaces of \(\mathbb F_q^n\), while projective hyperplanes have vector-space dimension \(n-1\).

## Proof

**1. Matrix-to-antiflag identification.** Every rank-one idempotent has the unique form \(E=u\varphi\), with \(\varphi(u)=1\), specified by its image point \(p=\langle u\rangle\) and its kernel hyperplane \(H=\ker\varphi\); necessarily \(p\notin H\). Conversely every such nonincident pair gives a unique projection. For two distinct rank-one idempotents \(E,F\), commutativity implies \(EF=FE=0\): their images are invariant one-dimensional spaces, so if the product were nonzero, both idempotents would have the same image and commute only when identical. Thus for corresponding antiflags \((p,H),(r,K)\), adjacency means \(p\in K\) and \(r\in H\). There are \(v\) points and \(q^{n-1}\) hyperplanes avoiding a chosen point, giving \(N=vq^{n-1}\). Each neighbor of \((p,H)\) chooses \(r\in H\) (\(t\) choices) and then a hyperplane \(K\) containing \(p\) but avoiding \(r\) (\(\gamma\) choices), proving valency \(k=\gamma t\).

**2. Incidence factorization.** Let \(\mathcal D\) be all ordered pairs of distinct projective points. Define the rectangular real matrix \(U\), rows indexed by antiflags \((p,H)\) and columns by arcs \((a,r)\), by \(U_{(p,H),(a,r)}=1\) exactly if \(a=p\) and \(r\in H\). Let \(T\) transpose each directed arc. Then the graph adjacency operator is \(A=UTU^{\mathsf T}\). The matrix \(G=U^{\mathsf T}U\), restricted to arcs with a common first point \(p\), has entries
\[
G_{(p,r),(p,s)}=\begin{cases}\gamma,&r=s,\\0,&r\ne s\text{ and }p,r,s\text{ collinear},\\\beta,&p,r,s\text{ noncollinear} .\end{cases}
\]
This is because hyperplanes through one chosen point but not another number \(q^{n-2}\), and those through two independent points but not a third number \(q^{n-3}\). The nonzero eigenvalues of \(A\) coincide, including multiplicities, with those of \(TG\), by the \(AB/BA\) identity.

**3. Exhaustion of nonexceptional eigenvalues.** For an eigenvector \(x=(x_{pr})_{p\ne r}\) of \(TG\), set \(S_p=\sum_{r\ne p}x_{pr}\), and on each projective line \(\ell\) through \(p\) set \(L_{p\ell}=\sum_{r\in\ell\setminus\{p\}}x_{pr}\), \(d_{p\ell}=S_p-L_{p\ell}\), \(D_\ell=\sum_{p\in\ell}d_{p\ell}\). Writing \(\ell=pr\), the eigen-equation reads
\[
\lambda x_{pr}=\gamma x_{rp}+\beta d_{r\ell}.
\]
For \(\lambda\notin\{0,\beta,\gamma,-\gamma\}\), solve the paired equations and sum around each line:
\[
x_{pr}=\frac{\beta(\lambda d_{r\ell}+\gamma d_{p\ell})}{\lambda^2-\gamma^2},\quad
\lambda(\lambda-\beta)d_{p\ell}=(\lambda^2-\gamma^2)S_p-\beta\lambda D_\ell,
\quad D_\ell=\frac{\lambda-\gamma}{\lambda}\sum_{p\in\ell}S_p.
\]
There are exactly \(t\) lines through each point, and any two distinct points determine one line. Sum the last line identities over the lines through \(p\), and put \(J\) for the all-ones matrix on projective points. Elementary cancellation using \(\gamma=q\beta\) and \((q-1)t+1=q^{n-1}\) gives
\[
 \big(\lambda^2-\gamma^3\big)S=\beta(\lambda-\gamma)JS.
\]
If \(S=0\), the line equations force \(d=0\) and then \(x=0\), a contradiction. The operator \(J\) acts by zero on the mean-zero point-function space and by \(v\) on constants, so the only allowed nonexceptional eigenvalues are \(\pm\alpha=\pm\gamma^{3/2}\) and the two roots of \(\lambda^2-\gamma^3-\beta v(\lambda-\gamma)=0\), which factor as \((\lambda-\beta)(\lambda-k)=0\). For each of \(\pm\alpha\), the eigenspace therefore has dimension at most \(v-1\), and for \(k\) it has dimension at most one.

**4. Realization of the large eigenspaces.** For every real function \(f\) on projective points with \(\sum_p f(p)=0\), define functions on antiflags by \(F_1(p,H)=f(p)\) and \(F_2(p,H)=\sum_{r\in H}f(r)\). Direct incidence counting gives \(AF_1=\gamma F_2\) and \(AF_2=\gamma^2F_1\). Thus \(F_1\pm\gamma^{-1/2}F_2\) are eigenvectors with eigenvalues \(\pm\alpha\). They are nonzero and injective in \(f\): the incidence identities yield \(\lVert F_1\rVert^2=q^{n-1}\lVert f\rVert^2\), \(\lVert F_2\rVert^2=\gamma q^{n-1}\lVert f\rVert^2\), and \(\langle F_1,F_2\rangle=-\gamma\lVert f\rVert^2\), hence \(\lVert F_1\pm\gamma^{-1/2}F_2\rVert^2=2(q^{n-1}\mp\sqrt\gamma)\lVert f\rVert^2>0\). The valency eigenvalue \(k\) occurs once because the all-ones vector realizes it and the previous dimension bound applies.

**5. Remaining four multiplicities from exact moments.** Apart from \(k,\pm\alpha\), the only possible eigenvalues are \(0,\beta,\gamma,-\gamma\). The graph has no loops and its neighbor-induced graph is the antiflag graph of a hyperplane, hence every adjacent pair has exactly \(a=\beta s\) common neighbors. Consequently
\[
\operatorname{tr}(A^0)=N,\quad\operatorname{tr}(A)=0,\quad\operatorname{tr}(A^2)=Nk,\quad\operatorname{tr}(A^3)=Nka.
\]
Subtract the already determined contributions from \(k\) and the two \(\pm\alpha\) eigenspaces. The resulting nonsingular four-by-four Vandermonde system for eigenvalues \(0,\beta,\gamma,-\gamma\) has the unique solution
\[
m_0=0,\qquad m_\beta=\frac{q^3ts}{q+1},\qquad m_{+\gamma}=\frac{(q-2)tv}{2},\qquad m_{-\gamma}=\frac{q(q-1)tv}{2(q+1)}.
\]
This proves completeness, all multiplicities and nonsingularity; their integrality follows as eigenspace dimensions. The exceptional \(q=2\) zero-multiplicity row and irrationality assertion are immediate.

## Verification

The accompanying standalone Python 3/NumPy program builds the exact antiflag adjacency matrix directly from normalized projective vectors over prime fields, checks regularity, computes all eigenvalues numerically, and matches them against the symbolic formula with tolerance \(3\cdot10^{-7}\). Independent executions tested \((n,q)=(4,2),(4,3),(5,2)\), including \(1080\)-vertex and \(496\)-vertex graphs, with maximum absolute eigenvalue discrepancies under \(2\cdot10^{-13}\). These finite computations corroborate but do not replace the above proof for every prime power.

## Relationship to prior work

Cohen and Postma's arXiv preprint (publicly posted 20 October 2003), and Cohen–Cuypers–Gramlich's local-recognition paper, already define and study point-hyperplane antiflag graphs. In particular their graph identification and local-neighborhood recursion are prior results, not new claims. A previously published exact degree and adjacent common-neighbor formula for the primitive-idempotent graph is also explicitly credited. Faradzev's 1994 association-scheme work concerns projective planes and is a reason to omit \(n=3\). Pankov and Pasini (2026) analyze the four antiflag relations and their automorphism structures but their inspected statements do not give the full eigenvalue multiplicities above. The contribution claimed here is specifically the explicit complete adjacency spectrum of the commuting primitive-idempotent graph for \(n\ge4\), together with its nonvanishing and field-parity consequences.

## Limitations

No claim of historical uniqueness or independent certification is made. In particular a yet-unidentified general representation-theoretic or association-scheme spectrum theorem may imply this result, despite targeted searches. The Faradzev full text was not obtained; the excluded \(n=3\) case is not a novelty claim. The numerical checker covers only stated prime-field instances; the proof, not the experiments, addresses prime-power fields and all \(n\ge4\). The result says nothing about spectra of the entire noncentral-matrix commuting graph or any weighted variant.

## References

1. A. M. Cohen and E. J. Postma, *Covers of Point-Hyperplane Graphs*, arXiv:math/0310322, first posted 20 October 2003. https://arxiv.org/abs/math/0310322
2. A. M. Cohen, H. Cuypers and R. Gramlich, *Local Recognition of Non-Incident Point-Hyperplane Graphs*, Combinatorica (2005), DOI 10.1007/s00493-005-0016-4; open preprint https://www.mathematik.tu-darmstadt.de/media/mathematik/forschung/preprint/ps2pdf/2248.pdf
3. I. Faradzev, *Association schemes on the set of antiflags of a projective plane*, Discrete Mathematics, 1994. DOI 10.1016/0012-365X(92)00476-8 (full text not inspected).
4. M. Pankov and A. Pasini, *Four Relations on the Set of Point-Hyperplane Antiflags*, Electronic Journal of Combinatorics 33 (2026), #P3.38, DOI 10.37236/15331. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i3p38/pdf/
5. *Edge-regular primitive-idempotent graphs of finite full matrix rings*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-edge-regular-primitive-idempotent-graphs-of-finite-full-matrix-r--366b43eada10
