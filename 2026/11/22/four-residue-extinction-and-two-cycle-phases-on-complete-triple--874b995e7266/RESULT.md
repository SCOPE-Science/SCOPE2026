# Four-residue extinction and two-cycle phases on complete triple-incidence graphs

## Finding

For every integer \(n\ge4\), form the bipartite incidence graph \(G_n\) between the \(n\) points of \([n]\) and all \(\binom n3\) unordered triples. Connect a point to a triple exactly when the point belongs to that triple. Give each graph vertex a state in a finite field \(\mathbb F_q\), where \(q=2^h\) and \(h\ge1\), and simultaneously replace its state by the sum of all open-neighbor states. Let \(F\) be the resulting linear map, \(m=\binom n3\), and \(N=n+m\).

Set \(d=n,n-1,0,1\) as \(n\equiv0,1,2,3\pmod4\), respectively. Then the complete Jordan form over \(\mathbb F_q\) is

\[
\boxed{F\sim J_2(1)^{\oplus d}\oplus J_3(0)^{\oplus(n-d)}\oplus J_1(0)^{\oplus(m-2n+d)}.}
\]

All the listed multiplicities are nonnegative for \(n\ge4\). Thus every trajectory becomes periodic within three updates, and the only eventual periods are one and two. There are exactly \(q^d\) fixed states, \((q^{2d}-q^d)/2\) primitive two-cycle orbits, and \(q^{2d}\) periodic states. Every fixed-state basin has \(q^{N-2d}\) initial configurations, and every two-cycle basin has \(2q^{N-2d}\) initial configurations.

If \(E_t\) denotes the number of initial states periodic by update \(t\), including states periodic initially, then the **exact full first-entry census** is specified by

\[
\boxed{(E_0,E_1,E_2,E_3)=(q^{2d},\ q^{m-n+2d},\ q^{m+d},\ q^{N}).}
\]

The number first becoming periodic *exactly* at update \(t\) is \(E_0\) for \(t=0\), and \(E_t-E_{t-1}\) for \(1\le t\le3\). In particular:

| \(n\bmod4\) | Recurrent dimension | Nilpotent size-three chains | Sharp maximum entry time | Long-term phase |
|---|---:|---:|---:|---|
| \(0\) | \(2n\) | \(0\) | \(0\) if \(n=4\), otherwise \(1\) | Exponentially many fixed and two-periodic states |
| \(1\) | \(2n-2\) | \(1\) | \(3\) | Fixed states and two-cycles, one terminal transient chain |
| \(2\) | \(0\) | \(n\) | \(3\) | Universal extinction |
| \(3\) | \(2\) | \(n-1\) | \(3\) | Only \(q^2\) periodic states |

For the two residue classes with \(n\equiv2,3\pmod4\), the fraction requiring the full third update is respectively \(1-q^{-n}\) and \(1-q^{-(n-1)}\). For \(n\equiv1\pmod4\) this fraction is \(1-q^{-1}\). Therefore almost every initial configuration needs three steps in the \(2\)- and \(3\)-residue classes, whereas the other classes have radically different recurrent dimensions.

## Assumptions and scope

The hypergraph contains **all** three-element subsets of \([n]\), without multiplicity; the incidence graph is undirected, simple, bipartite, and has no additional edges or self-loops. States lie in an arbitrary *finite characteristic-two field*, not merely the binary field. Updates are synchronous, unweighted and open-neighbor only. The first periodic-entry time of a state \(x\) is the least \(t\ge0\) for which \(F^t x\) lies on a temporal cycle; no transient is counted as periodic merely because its image repeats later. Every basin count concerns labelled configurations and counts all states whose eventual periodic orbit is the specified orbit.

Write \(B\in\mathbb F_q^{n\times m}\) for the point–triple incidence matrix, with column \(e_i+e_j+e_k\) for each triple. Relative to the two bipartition classes,

\[
F=\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix},\qquad Q=BB^{\mathsf T}.
\]

## Proof

**1. Full point rank.** For any distinct \(i,j\in[n]\), choose two other distinct points \(a,b\), available since \(n\ge4\). The incidence columns of \(\{i,a,b\}\) and \(\{j,a,b\}\) sum to \(e_i+e_j\) in characteristic two. Such pair sums span the even-coordinate-sum subspace of dimension \(n-1\). Any incidence column has three ones and thus odd coordinate sum, giving one further independent direction. Hence \(\operatorname{rank}B=n\). Consequently \(B\) is onto and \(B^{\mathsf T}\) is injective.

**2. The complete-triple intersection identity.** The diagonal entries of \(Q\) equal \(\binom{n-1}{2}\) modulo two, and the off-diagonal entries equal \(n-2\) modulo two. Writing \(I\) for the point identity and \(J\) for the all-ones point matrix, a direct four-residue calculation yields

\[
Q=\begin{cases}
I,&n\equiv0\pmod4,\\
I+J,&n\equiv1\pmod4,\\
0,&n\equiv2\pmod4,\\
J,&n\equiv3\pmod4.
\end{cases}
\]

In the two odd-order cases, \(J^2=nJ=J\); hence \(Q^2=Q\) in all four cases. Its rank is exactly \(d\) as specified above.

**3. Iterate ranks and the two temporal eigenvalues.** Since \(B\) is onto and \(B^{\mathsf T}\) injective,

\[
\begin{aligned}
\operatorname{rank}F&=2n,\\
\operatorname{rank}F^2&=n+d,\\
\operatorname{rank}F^3&=2d,\\
\operatorname{rank}F^4&=2d.
\end{aligned}
\]

For example \(F^2=\operatorname{diag}(Q,B^{\mathsf T}B)\), where \(B^{\mathsf T}B\) has rank \(n\). Also

\[
F^3=\begin{pmatrix}0&QB\\B^{\mathsf T}Q&0\end{pmatrix},\quad
F^5=\begin{pmatrix}0&Q^2B\\B^{\mathsf T}Q^2&0\end{pmatrix}=F^3.
\]

It follows that the recurring subspace \(R=\operatorname{im}F^3\) has dimension \(2d\), and \(F^2=I\) on \(R\). The complementary nilpotent Fitting summand \(Z=\ker F^3\) has dimension \(N-2d\) and nilpotency index at most three. On \(Z\), the ranks of the first and second powers are \(2(n-d)\) and \(n-d\). Thus there are exactly \(n-d\) size-three nilpotent chains, **no** size-two nilpotent chains, and \(N-2d-3(n-d)=m-2n+d\) size-one nilpotent chains.

**4. Fixed states and periodic Jordan blocks.** A fixed state \((u,w)\) must satisfy \(u=Bw\) and \(w=B^{\mathsf T}u\), or equivalently \(Qu=u\) and \(w=B^{\mathsf T}u\). Because \(Q\) is a projection of rank \(d\), the fixed-state space has dimension \(d\). Since the periodic space has dimension \(2d\), and the polynomial \((X+1)^2\) annihilates its restriction of \(F\), this periodic restriction has exactly \(d\) Jordan blocks of size two at eigenvalue one, with no size-one blocks there. The displayed full Jordan form follows. The Jordan count also proves that genuine two-cycles exist whenever \(d>0\).

**5. Entrance layers and basins.** By the unique splitting \(x=r+z\) with \(r\in R\), \(z\in Z\), the first periodic-entry time of \(x\) is exactly the least \(t\) with \(F^t z=0\). For \(t\in\{0,1,2,3\}\), the dimension of the choices for \(z\) in \(\ker(F^t|_Z)\) is \(\dim Z-\operatorname{rank}(F^t|_Z)\). Using the block ranks above gives dimensions \(0,m-n,m-n+(n-d),N-2d\) at times zero through three. Adding the \(2d\) arbitrary recurrent coordinates gives the asserted exponents \(2d,m-n+2d,m+d,N\).

Every recurrent state has exactly \(q^{N-2d}\) initial configurations with that recurrent Fitting component. Because the recurrent map is bijective, an orbit of length \(p\) therefore attracts exactly \(p q^{N-2d}\) initial configurations. The maximal entry times in the table follow from the explicit positive size-three block counts (or, for \(n\equiv0\), the positive count of size-one blocks when \(n\ge8\)); when \(n=4\), both counts vanish.

## Verification

Run the attached standard-library-only script `check_hypergraph_xor.py` using `python3 check_hypergraph_xor.py`. It builds the point–triple incidence graph independently from triples, computes ranks of the first five iterate matrices for every \(4\le n\le16\), and compares these with the predicted nilpotent and recurrent Jordan dimensions. It also directly enumerates all \(256\) binary configurations at \(n=4\) and all \(32768\) configurations at \(n=5\), checking exact entry times, fixed states and two-cycle populations; deterministic direct trajectories test all four residue classes through \(n=12\). The captured result is in `check_output.txt`. These finite tests do not prove the universal field- and order-quantified result; the proof above supplies that argument.

## Relationship to prior work

The binary subset inclusion matrix and its rank theory are classical: Ghorbani, Khosrovshahi, Maysoori and Mohammad-Noori analyze inclusion matrices and Smith forms, but not dynamics on their point–block incidence graphs. Moreno, Bollman and Aviño-Díaz discuss finite linear dynamical systems and their state diagrams generally, without the complete triple-incidence family or its parity-residue Jordan decomposition. Rowland and Yassawi study linear cellular automata through automatic sequences and symbolic factors, not these finite hypergraph incidence orbits.

Two closely related published finite network examples—the ordinary edge-subdivision of a complete graph and projective-plane point–line incidence graphs—have different underlying incidence matrices. The former has even-weight columns and rank \(n-1\), while the triple-incidence matrix here has odd-weight columns and full rank \(n\); the latter is square and symmetric as a design, while the complete triple system is usually highly rectangular. Neither prior graph-specific statement yields the four-residue table, the single versus multiple length-three chains, or the exact full entrance populations without a new incidence-square calculation.

## Limitations

The claim applies to the complete 3-uniform set system for \(n\ge4\), not to arbitrary 3-uniform hypergraphs, to incomplete block designs or to other uniformities. It requires characteristic two, simultaneous updates, and unweighted open neighborhoods. The universal proof is elementary algebra, but no assertion is made that the known inclusion-matrix rank theorem or generic linear Jordan theory is new. Reproducible finite checks are corroborative only. A mathematically equivalent family-specific classification might exist outside the searched and inspected literature; independent external validation has not been performed.

## References

1. O. Moreno, D. Bollman, M. A. Aviño-Díaz, *Finite Dynamical Systems, Linear Automata, and Finite Fields*, arXiv:math/0604534 (first public arXiv posting 2006-04-25), https://arxiv.org/html/math/0604534v1.
2. E. Ghorbani, G. B. Khosrovshahi, Ch. Maysoori, M. Mohammad-Noori, *Inclusion Matrices and Chains*, arXiv:0709.3144 (first public arXiv posting 2007-09-20), https://arxiv.org/abs/0709.3144.
3. E. Rowland, R. Yassawi, *A characterization of \(p\)-automatic sequences as columns of linear cellular automata*, arXiv:1209.6008 (first public arXiv posting 2012-09-26), https://arxiv.org/abs/1209.6008.
4. *Three-step extinction rigidity and parity-swapped cycles on subdivided cliques*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-three-step-extinction-rigidity-and-parity-swapped-cycles-on-subd--88cbaceccac4/RESULT.md.
5. *Exact parity-dependent orbit and extinction census on projective-plane incidence graphs*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-exact-parity-dependent-orbit-and-extinction-census-on-projective--578d68794cd5/RESULT.md.
