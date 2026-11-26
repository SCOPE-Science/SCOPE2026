# Every minimum zero-forcing set of a binary hypercube is parity-balanced and frozen under token sliding

## Finding

For every integer \(d\ge 2\), let \(Q_d\) be the graph on the binary words \(\{0,1\}^d\), with edges joining words differing in one coordinate. Let \(E_d\) and \(O_d\) be its even- and odd-Hamming-weight classes. Every minimum **ordinary** zero-forcing set \(S\) satisfies the sharp parity constraint

\[
|S\cap E_d|=|S\cap O_d|=2^{d-2}.
\]

Consequently the token-sliding reconfiguration graph on minimum ordinary zero-forcing sets of \(Q_d\) is **edgeless** for every \(d\ge2\): moving a selected vertex across one edge, while keeping the number of vertices fixed, never produces another minimum zero-forcing set. This is sharp in dimension one, whose two optimal singleton sets have one legal slide between them. In dimensions at least two there are at least two optimal sets, so the edgeless graph is genuinely disconnected.

The proof also recovers the known value \(Z(Q_d)=2^{d-1}\), but neither that scalar equality nor existing finite counts of minimum sets are claimed as new.

## Assumptions and scope

A vertex in an initially colored set is blue; other vertices are white. At any stage, a blue vertex with exactly one white neighbor may change that neighbor to blue. A set is *ordinary zero forcing* if some finite sequence of these moves colors all vertices. The minimum cardinality is denoted \(Z(G)\). A *token slide* removes one vertex \(u\) from a minimum set and adds an unoccupied neighbor \(v\) with \(uv\in E(G)\), requiring the resulting set to be another minimum ordinary zero-forcing set. There are no intermediate additions or spare tokens.

The bipartition \(E_d,O_d\) is specified by Hamming-weight parity; each side contains \(2^{d-1}\) vertices. All matrices below are over the real numbers; their entries are exact integers. The claim holds for every integer \(d\ge2\) without a computational dimension cutoff. It does not concern positive-semidefinite, skew, or power domination forcing.

## Proof

**1. Kernel obstruction for ordinary forcing.** Let \(G\) be a graph and \(A\) a symmetric real matrix whose off-diagonal entries are nonzero exactly on the edges of \(G\). Restriction to an ordinary zero-forcing set \(S\) defines an injective map \(\ker A\longrightarrow\mathbb R^S\). Indeed, suppose \(Ax=0\) and \(x\) vanishes at all initial blue vertices. If a blue \(u\) forces its unique white neighbor \(v\), then all other neighbors of \(u\) have vanishing coordinates, and the equation \((Ax)_u=0\) reduces to \(A_{uv}x_v=0\), so \(x_v=0\). The same is true after every force; at termination \(x=0\). Thus, for any subspace \(W\subseteq\ker A\) whose vectors have support entirely inside a vertex class \(C\), restriction \(W\to\mathbb R^{S\cap C}\) is injective. In particular,

\[
|S\cap C|\ge\dim W.
\]

**2. An all-dimensional signed cube matrix with two large parity-supported kernels.** Write \(d=m+1\) with \(m\ge1\). For \(1\le j\le m\), define a signed coordinate-flip operator on functions on \(\{0,1\}^{m}\):

\[
(T_j f)(z)=(-1)^{z_1+\cdots+z_{j-1}}f(z\oplus e_j).
\]

Each \(T_j\) is a symmetric real matrix with zero diagonal, supported exactly on the \(j\)-th-direction cube edges, and satisfies \(T_j^2=I\). For \(i\ne j\), their sign rules give \(T_iT_j=-T_jT_i\): flipping the lower-index bit changes the sign of the higher-index operator once. Therefore all cross terms cancel in the square of any real linear combination of the \(T_j\).

Put \(a=4m-3\), \(c_1=5-4m\), and \(c_j=4\) for \(2\le j\le m\). These are nonzero integers for every \(m\ge1\), and

\[
c_1^2+\sum_{j=2}^m c_j^2=(5-4m)^2+16(m-1)=(4m-3)^2=a^2.
\]

Hence the symmetric matrix \(K=\sum_{j=1}^m c_jT_j\) has nonzero entries exactly on the edges of \(Q_m\), has zero diagonal, and satisfies \(K^2=a^2 I\).

Order the vertices of \(Q_d=K_2\square Q_m\) in the two layers of its first coordinate, and form

\[
A=\begin{pmatrix}K&aI\\aI&K\end{pmatrix}.
\]

All off-diagonal edge entries of \(A\) are nonzero and all nonedges have zero entries, with zero diagonal. Its kernel is exactly

\[
\ker A=\{(x,-Kx/a):x\in\mathbb R^{2^m}\},
\]

because both block equations hold by \(K^2=a^2I\), and the first equation determines the second block. Therefore \(\operatorname{rank}A=2^m=2^{d-1}\).

Reorder the same matrix by the two full-cube parity classes. Every cube edge crosses parity, so

\[
A=\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix},
\quad |E_d|=|O_d|=2^{d-1}.
\]

The rank of this block matrix is twice \(\operatorname{rank}B\), hence \(\operatorname{rank}B=2^{d-2}\). In particular the subspace of \(\ker A\) supported entirely on \(E_d\) has dimension \(\dim\ker B^{\mathsf T}=2^{d-2}\); the subspace supported entirely on \(O_d\) has dimension \(\dim\ker B=2^{d-2}\). Step 1 applied separately to these two subspaces proves **for every zero-forcing set \(S\), not only minimum sets**, that

\[
|S\cap E_d|\ge 2^{d-2},\qquad |S\cap O_d|\ge 2^{d-2}.
\]

**3. Optimality and rigidity.** Adding the bounds gives \(|S|\ge2^{d-1}\). Conversely an entire coordinate facet, consisting of all words with a fixed first bit, has \(2^{d-1}\) vertices, and each selected vertex has its opposite-facet counterpart as its sole unselected neighbor. Thus the whole other facet can be forced in one round and \(Z(Q_d)=2^{d-1}\). Equality in the sum of the two bounds forces each individual parity count to equal \(2^{d-2}\).

Any graph edge of \(Q_d\) has one even endpoint and one odd endpoint. Moving one token along an edge changes the parity count by one. It therefore violates the necessary equality and cannot result in another minimum zero-forcing set. The two opposite coordinate facets demonstrate distinct optimal configurations in every dimension \(d\ge2\). For \(d=1\), \(Q_1=K_2\) and its two minimum singleton sets are connected by one legal slide.

## Verification

The proof in the preceding section is symbolic and valid for unbounded \(d\). The two accompanying standalone programs are independent checks, not substitutes for this proof. With Python 3.8 or newer and no third-party packages, execute:

```sh
python3 verify_matrix.py
python3 verify_small.py
```

`verify_matrix.py` constructs the signed Clifford matrices in dimensions \(2\) through \(6\), checks every matrix entry and the exact integer identity \(K^2=a^2I\), and computes ranks modulo the prime \(1000003\). The modular rank computations cross-check the predicted parity-block and full-matrix ranks; the proof itself establishes the ranks over \(\mathbb R\) for all dimensions. `verify_small.py` independently enumerates ordinary zero forcing sets in dimensions \(2\), \(3\), and \(4\), confirms the exact optimum counts \(4,30,2360\), checks every optimum's parity count, and independently checks that no legal token slide exists. Their final output lines are `MATRIX_CERTIFICATE_PASS` and `ENUMERATION_CERTIFICATE_PASS`.

## Relationship to prior work

Geneson, Haas and Hogben formalized one-vertex-exchange reconfiguration graphs for zero-forcing sets (2020 preprint, later journal publication). Their framework allows exchanging any selected and unselected vertices, unlike the more restrictive adjacent-vertex token sliding studied here. Huang, Chang and Yeh and the subsequent hypercube literature establish the scalar value \(Z(Q_d)=2^{d-1}\); that value alone does not determine how many vertices an arbitrary minimum set must occupy in each parity class. Brimkov, Cameron and Grubbs study hypercube forts and minimum zero-forcing propagation times, not the all-dimensional balanced-parity invariant or its token-slide obstruction. Bong and collaborators study token sliding primarily for positive semidefinite and skew zero forcing, and give universal structural properties such as bipartiteness for sliding on bipartite graphs; that does not imply an edgeless graph for ordinary hypercube zero forcing.

A previously available exact result classifies the **unrestricted-exchange** graph on the \(2360\) minimum sets of \(Q_4\) as connected with diameter eight and \(22848\) edges. The present infinite-family theorem instead proves its **adjacency-constrained** subgraph has no edges at all, with a uniform structural reason across every dimension. No existing count of minimum sets or unrestricted-exchange metric is claimed as new.

## Limitations

The theorem concerns only ordinary minimum zero-forcing configurations on unweighted binary hypercubes and strictly one-token moves along original cube edges with no spare tokens. It does not assert that one cannot transform optimal sets by temporarily adding tokens, nor does it give the minimum extra buffer required for mobility. The proof uses a purpose-built real signed adjacency matrix; the finite rank and enumeration programs check only small dimensions and cannot independently verify the infinite statement. An equivalent parity-rigidity claim in uncatalogued literature remains possible; originality is based on comparisons with the listed available sources, not on the absence of search hits. No independent scientific audit is claimed.

## References

1. J. Geneson, R. Haas and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220, first submitted 2020-09-01; https://arxiv.org/abs/2009.00220.
2. H. Huang, G. J. Chang and H.-G. Yeh, *On minimum rank and zero forcing sets of a graph*, Linear Algebra and its Applications (2010), DOI:10.1016/j.laa.2010.01.001.
3. B. Brimkov, T. R. Cameron and O. Grubbs, *On the forts and related parameters of the hypercube graph*, arXiv:2507.10826 (2025); https://arxiv.org/abs/2507.10826.
4. N. Bong et al., *Reconfiguration of Minimum PSD Forcing Sets and Minimum Skew Forcing Sets*, arXiv:2501.03642 (2025); https://arxiv.org/abs/2501.03642.
5. *A self-centered, nonregular exchange graph for minimum zero forcing of the four-cube*, published mathematical finding (2026); https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-self-centered-nonregular-exchange-graph-for-minimum-zero-forci--4c5b7f9219b1.
