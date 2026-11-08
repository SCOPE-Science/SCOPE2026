# Adjacency codes of finite chain-ring zero-divisor graphs: uniform dimension, hull and weight-one spectrum

## Finding
Let \(R\) be a finite commutative chain ring with maximal ideal \(\mathfrak m=(\pi)\), residue field of order \(q=p^f\), and nilpotency index \(\ell\ge3\). Let \(\Gamma(R)\) be the **simple** zero-divisor graph on all nonzero nonunits; distinct vertices \(x,y\) are joined if and only if \(xy=0\). Its adjacency matrix \(A\) is regarded over the prime field \(\mathbb F_p\). The adjacency code is \(C=\operatorname{rowsp}_{\mathbb F_p}(A)\).

For a nonzero nonunit \(x\), define its valuation \(\nu(x)\) by \(x\in\mathfrak m^{\nu(x)}\setminus\mathfrak m^{\nu(x)+1}\), with \(1\le\nu(x)\le\ell-1\). Partition the graph vertices into
\[
 L=\{x:1\le\nu(x)<\lceil\ell/2\rceil\},\qquad
 H=\{x:\lceil\ell/2\rceil\le\nu(x)\le\ell-1\}.
\]
The sets have sizes \(|L|=q^{\ell-1}-q^{\lfloor\ell/2\rfloor}\) and \(|H|=q^{\lfloor\ell/2\rfloor}-1\). Order coordinates as \((L,H)\). Write \(B\) for the \(|L|\)-by-\(|H|\) matrix \(B_{uv}=\mathbf1_{\nu(u)+\nu(v)\ge\ell}\), and \(\mathbf1_L\) for the all-ones vector on \(L\).

**Theorem (complete rowspace, dual, hull, and weight-one spectrum).** For every such ring, without a restriction on characteristic or a requirement that the ring contain a coefficient field,
\[
\boxed{C=\{(t\mathbf1_L-By,y):t\in\mathbb F_p,\ y\in\mathbb F_p^H\}},
\qquad
\boxed{C^\perp=\{(z,B^Tz):z\in\mathbb F_p^L,\ \textstyle\sum_{u\in L}z_u=0\}}.
\]
Thus
\[
\boxed{C:[q^{\ell-1}-1,\ q^{\lfloor\ell/2\rfloor},\ 1]_p},\qquad
\boxed{C^\perp:[q^{\ell-1}-1,\ q^{\ell-1}-q^{\lfloor\ell/2\rfloor}-1,\ 2]_p},
\]
and
\[
\boxed{C\cap C^\perp=\mathbb F_p(\mathbf1_L,0_H)}.
\]
A coordinate unit vector \(e_v\) belongs to \(C\) exactly if \(v\) is a nonzero socle vertex (valuation \(\ell-1\)), or if \(\ell\) is even and \(\nu(v)=\ell/2\). Consequently the exact number of nonzero weight-one codewords is
\[
\boxed{A_1(C)=(p-1)(q-1)\bigl(1+\mathbf1_{2\mid\ell}\,q^{\ell/2-1}\bigr)},
\]
where the second term is understood to be zero for odd \(\ell\). The formulas depend on \(R\) only through \(q\) and \(\ell\).

## Assumptions and scope
A finite commutative chain ring means a unital finite commutative ring whose ideals form a chain; its unique maximal ideal has a generator \(\pi\). Its residue field has size \(q=p^f\). The coefficient field of the code is the **prime field** \(\mathbb F_p\), not necessarily the residue field. The adjacency matrix has zero diagonal even when a vertex squares to zero. The theorem concerns the row space of this adjacency matrix, not its vertex-edge incidence or Laplacian code. Nilpotency length is \(\ell\ge3\); the omitted length-two case is a clique with different formulas.

## Proof
**1. Graph structure and modular incidence identities.** Every nonzero nonunit is a unit times \(\pi^i\) for exactly one \(i\in\{1,\ldots,\ell-1\}\); two such elements have zero product precisely when their valuations sum to at least \(\ell\). The \(i\)-th valuation layer has size \((q-1)q^{\ell-i-1}\), and \(|\mathfrak m^i|=q^{\ell-i}\). The low set \(L\) is independent and the high set \(H\) is a clique. Hence the adjacency matrix has block form
\[
A=\begin{pmatrix}0&B\\ B^T&J_H-I_H\end{pmatrix}.
\]
For each low vertex \(u\) with valuation \(i\), the number of its high neighbors is exactly \(q^i-1\), so the row sum of \(B\) equals \(-1\) in \(\mathbb F_p\). For any two low vertices of valuations \(i,j\), their common high neighbors are exactly the nonzero elements of \(\mathfrak m^{\ell-\min(i,j)}\), numbering \(q^{\min(i,j)}-1\equiv-1\pmod p\). Therefore
\[
B\mathbf1_H=-\mathbf1_L,\qquad BB^T=-J_L,
\qquad |H|=q^{\lfloor\ell/2\rfloor}-1\equiv-1\pmod p.
\]
These hold for \(p=2\) as well.

**2. Complete kernel and rank.** Suppose \(A(z,y)^T=0\) for \(z\in\mathbb F_p^L\), \(y\in\mathbb F_p^H\); put \(s=\sum_L z_u\) and \(T=\sum_H y_v\). The high block equation reads \(B^Tz+T\mathbf1_H-y=0\), or \(y=B^Tz+T\mathbf1_H\). Summing yields \(T=-s+|H|T=-s-T\), hence \(2T=-s\). The low block equation and the identities above give \(0=By=-(s+T)\mathbf1_L\), so \(T=-s\). Substitution in \(2T=-s\) gives \(s=T=0\) over every field. Thus \(y=B^Tz\) with \(\sum_Lz=0\). Conversely these conditions give both block equations: \(By=-s\mathbf1_L=0\), while \(\sum_H B^Tz=-s=0\). This proves the stated kernel. Because \(|L|\ge2\), its dimension is \(|L|-1\), and the rank of \(A\) is \(|H|+1=q^{\lfloor\ell/2\rfloor}\).

**3. Complete row space.** Symmetry of \(A\) gives \(C=(\ker A)^\perp\). A vector \((c_L,c_H)\) is perpendicular to every \((z,B^Tz)\) with \(\sum_Lz=0\) precisely when \(c_L+Bc_H\) lies in the one-dimensional orthogonal complement of the low-coordinate sum-zero space. Thus \(c_L=t\mathbf1_L-Bc_H\). Writing \(y=c_H\) gives the claimed parametrization and its uniqueness.

**4. Hull.** Every coordinate of \(By\) on the low valuation layer \(i\) depends only on \(i\), so every low part of a codeword is constant on each low layer. Every such layer has size \((q-1)q^{\ell-i-1}\), divisible by \(p\) because \(i\le\lceil\ell/2\rceil-1\) and \(\ell\ge3\). Therefore, for any two codewords \(c(t,y)\) and \(c(t',y')\), their standard dot product reduces to \(y\cdot y'\). As \(y'\) ranges over all of \(\mathbb F_p^H\), a codeword is orthogonal to the whole code if and only if \(y=0\). This gives precisely \(\mathbb F_p(\mathbf1_L,0_H)\) as the Euclidean hull.

**5. Both minimum distances and the exact weight-one spectrum.** A socle vertex \(v\) has valuation \(\ell-1\); its column in \(B\) is \(\mathbf1_L\). Setting \(t=1\) and \(y=e_v\) gives the codeword \((0_L,e_v)\), proving \(d(C)=1\). For the dual, any nonzero \(z\) with \(\sum_Lz=0\) has at least two nonzero positions, and its full codeword contains \(z\); hence \(d(C^\perp)\ge2\). Choose two distinct low vertices in the valuation-one layer and set \(z=e_u-e_v\). They have identical rows in \(B\), so \(B^Tz=0\); thus the dual contains a word of weight two.

For an arbitrary high vertex \(v\), the singleton word \((0_L,e_v)\) belongs to \(C\) exactly when \(Be_v\) is constant on \(L\). Its entries are zero on the low layers with \(i+\nu(v)<\ell\) and one otherwise. It is all one exactly when \(\nu(v)=\ell-1\), and it is all zero exactly when \(\ell\) is even and \(\nu(v)=\ell/2\). No other high vertex has a constant column. A singleton supported in \(L\) cannot lie in \(C\), because its high part zero would force the low part to be constant on the whole of \(L\), which has at least two vertices. There are \(q-1\) socle vertices and, for even \(\ell\), \((q-1)q^{\ell/2-1}\) middle-layer vertices. Each gives \(p-1\) scalar multiples, proving the formula for \(A_1(C)\). The dual dimension and both complete code-parameter triples follow.

## Verification
The included standalone program `verify_adjacency.py` builds quotient rings \(\mathbb F_q[u]/(u^\ell)\) by explicit coefficient multiplication and constructs their simple zero-divisor graphs by testing every distinct vertex pair; it does not use the valuation shortcut to set adjacency. It compares independent modular row reductions with the theorem's dimension and one-dimensional hull, checks both stated code/kernel constructions on generators, and enumerates every possible weight-one coordinate. It covers \(q=2\) for \(3\le\ell\le8\), \(q=3\) for \(3\le\ell\le6\), and \(q=4,5\) for \(3\le\ell\le4\), for fourteen configurations. The direct check of \(\mathbb F_4\) uses its irreducible quadratic polynomial.

Run `python verify_adjacency.py` with Python 3 and NumPy installed. The included `verification_output.txt` records each configuration and concludes `VERIFY_OK configurations=14 direct_ring_multiplication=yes rank_hull_code_dual_weight_one_checks=yes`. These checks cover finitely many equal-characteristic rings; the proof covers all finite commutative chain rings, including mixed-characteristic rings.

For example, \(R=\mathbb F_3[u]/(u^4)\) produces a ternary adjacency code of parameters \([26,9,1]_3\), a dual code \([26,17,2]_3\), and a one-dimensional hull; exactly sixteen nonzero words have weight one, supported on eight high-valuation coordinates.

## Relationship to prior work
Sarkar, Hansda and Maji, *Graph-Based Linear Codes Associated with the Finite Ring* \(\mathbb F_p[x]/\langle x^4\rangle\), arXiv:2610.08480 (October 6, 2026), examine the single nilpotency-index-four family for odd primes. Their Theorems 4.6 and 4.7 already give the dimension and hull formula in that special case, and are acknowledged here. Their Theorem 4.6 reports minimum distance two for the adjacency code. The explicit coordinate-unit construction above establishes minimum distance **one** for its stated simple adjacency graph: the proposed code differs in that coordinate-level assertion. Their conclusion proposes general nilpotency indices at least five as further work. The present result gives the full rowspace, dual, hull, and first weight-enumerator coefficient uniformly for every length at least three, all residue prime powers and all finite commutative chain rings.

The earlier spectral paper arXiv:2609.22909 by the same authors considers real graph spectra and dynamics for index four; it does not determine modular adjacency-code rowspaces for arbitrary lengths. Earlier zero-divisor graph and incidence-code results do not imply the prime-field adjacency rowspace and hull formulas merely from their graph descriptions. A general fixed-adjacency modular linear-algebra result under different terminology could still affect historical priority.

## Limitations
The theorem is about the **simple** zero-divisor graph on **nonzero nonunits**, over the **prime field**. It does not state the full weight enumerator, larger minimum-distance performance, Laplacian or incidence codes, or a classification of arbitrary non-chain local rings. The \(\ell=2\) case is excluded. Finite checker runs are illustrations, not exhaustive proof of infinitely many rings. Historical priority has not undergone independent audit. The scientific distinction from the previously reported minimum-distance-two parameter is exact for the graph and code specified here.

## References
1. A. Sarkar, K. Hansda, and M. Maji, *Graph-Based Linear Codes Associated with the Finite Ring* \(\mathbb F_p[x]/\langle x^4\rangle\), arXiv:2610.08480, first posted 2026-10-06, especially Theorems 4.6–4.7 and conclusion. https://arxiv.org/abs/2610.08480
2. A. Sarkar, K. Hansda, and M. Maji, *Spectral Characterization and Network Systems Dynamics of Zero-Divisor Topologies over* \(\mathbb F_p[x]/\langle x^4\rangle\), arXiv:2609.22909, first posted 2026-09-19. https://arxiv.org/abs/2609.22909
3. D. F. Anderson and P. S. Livingston, *The zero-divisor graph of a commutative ring*, Journal of Algebra 217 (1999), 434–447; cited as the simple graph convention in Reference 1.
