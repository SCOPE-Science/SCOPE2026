# Exact cone-transfer law for fastest symmetric Markov mixing

## Finding

For a finite simple graph \(H\) with \(m\ge2\) vertices, put \(C(H)=K_1\vee H\), the graph obtained by adding a vertex joined to every vertex of \(H\). For any graph \(F\), let \(\rho(F)\) be the minimum second-largest eigenvalue modulus (SLEM) among all real symmetric, nonnegative, row-stochastic matrices supported on \(F\), allowing nonnegative diagonal holding probabilities. Then
\[
 \rho(C(H))\le\frac{m-1}{m}\rho(H).
\]
**Equality holds whenever \(H\) is vertex-transitive**, with no edge-transitivity or connectedness assumption:
\[
 \boxed{\rho(K_1\vee H)=\left(1-\frac1m\right)\rho(H).}
\]
For any noncomplete vertex-transitive \(H\), each fastest-mixing matrix \(Q\) on \(H\) gives an optimal matrix on the cone,
\[
 P_* =\begin{pmatrix}0&\frac1m\mathbf 1^T\\
               \frac1m\mathbf1&\frac{m-1}{m}Q\end{pmatrix}.
\]
If \(H=K_m\), both sides of the equality are zero; the uniform matrix on \(K_{m+1}\) is optimal instead. The vertex-transitive hypothesis is substantive: when \(H=P_4\), the cone admits a chain with SLEM \((1+\sqrt{281})/40\), strictly less than \((3/4)\rho(P_4)=3\sqrt2/8\).

## Assumptions and scope

Graphs are finite, undirected, simple, labelled when a matrix is written, and may be disconnected. A permissible matrix \(Q\) on \(m\) vertices satisfies \(Q=Q^T\), \(Q\mathbf 1=\mathbf1\), \(Q_{ij}\ge0\), and \(Q_{ij}=0\) whenever \(i\ne j\) are nonadjacent. All diagonal entries are permitted. Let \(J_m=\mathbf1\mathbf1^T/m\), and define \(\rho(Q)=\|Q-J_m\|_2\), which equals the largest **absolute** eigenvalue of the restriction to \(\mathbf1^\perp\). Define \(\rho(H)=\min_Q\rho(Q)\); the minimum exists by compactness. The cone has \(m+1\) vertices. No assumption that graph edges carry equal weights is imposed.

## Proof

**1. A nonedge spectral obstruction.** Suppose \(H\) is not complete, and choose distinct nonadjacent \(i,j\). For a permissible \(Q\), put \(M=Q-J_m\) and \(u_i=e_i-\mathbf1/m\), \(u_j=e_j-\mathbf1/m\). Since \(M\mathbf1=0\),
\[
 |u_i^TMu_j|=|M_{ij}|=\frac1m,
 \qquad \|u_i\|_2\|u_j\|_2=\frac{m-1}{m}.
\]
The operator-norm inequality gives \(\rho(Q)=\|M\|_2\ge1/(m-1)\). Thus for every noncomplete \(H\),
\[
 \rho(H)\ge\frac1{m-1}.
\]
This bound is attained for the four-cycle: equal edge transitions of \(1/3\) give nontrivial eigenvalues \(1/3,1/3,-1/3\).

**2. Universal construction.** Let \(Q\) minimize \(\rho(H)\), and assume \(H\) noncomplete. The displayed \(P_*\) is symmetric, nonnegative and stochastic; its hub row has \(m\) entries \(1/m\), and every outer row has hub entry \(1/m\) and an outer block of row sum \((m-1)/m\). On the two-dimensional space spanned by the hub coordinate and the constant outer coordinate, it has eigenvalues \(1\) and \(-1/m\). On the orthogonal subspace \(\{0\}\oplus\mathbf1_m^\perp\), its eigenvalues are \((m-1)/m\) times those of \(Q\) on \(\mathbf1_m^\perp\). Therefore
\[
 \rho(P_*)=\max\left\{\frac1m,\frac{m-1}{m}\rho(H)\right\}
 =\frac{m-1}{m}\rho(H),
\]
where the last equality uses Step 1. If \(H\) is complete, then \(C(H)\) is complete and the uniform transition matrix gives both sides equal to zero. This proves the universal upper bound.

**3. Optimality for vertex-transitive bases.** Suppose \(H\) is vertex-transitive, and let \(P\) be any permissible symmetric stochastic matrix on \(C(H)\). Average \(P\) over the automorphism group of \(H\), acting on the outer vertices and fixing the hub. The averaged matrix \(\bar P\) remains permissible, and by convexity and orthogonal invariance of \(\|P-J_{m+1}\|_2\), it has SLEM no larger than \(P\). Vertex transitivity makes every hub-to-outer entry equal to some \(b\), with \(0\le b\le1/m\). Consequently the outer block of \(\bar P\) equals \((1-b)Q_b\) for a permissible symmetric stochastic \(Q_b\) on \(H\), since \(1-b>0\). The hub-constant two-dimensional block has eigenvalues \(1\) and \(1-(m+1)b\); the remaining eigenvalues are \((1-b)\) times the eigenvalues of \(Q_b\) on \(\mathbf1_m^\perp\). Hence
\[
 \rho(P)\ge\rho(\bar P)
 \ge(1-b)\rho(Q_b)
 \ge\left(1-\frac1m\right)\rho(H).
\]
Combining this lower bound with Step 2 proves equality. If \(H\) is disconnected, \(\rho(H)=1\) because every permissible chain preserves its connected components; the same proof applies.

**4. Sharp limit of the symmetry conclusion.** For the four-vertex path, reflection averaging reduces a permissible chain to weights \(a,b,a\) on its three edges with \(a,b\ge0\) and \(a+b\le1\). The odd-reflection spectral block has largest eigenvalue \(1-a-b+\sqrt{a^2+b^2}\), which is at least \(1-(a+b)+(a+b)/\sqrt2\ge1/\sqrt2\). The choice \(a=b=1/2\) has nontrivial eigenvalues \(\sqrt2/2,0,-\sqrt2/2\); therefore \(\rho(P_4)=\sqrt2/2\).

The following permissible matrix on \(K_1\vee P_4\), with hub indexed last, is symmetric and stochastic:
\[
 R=\begin{pmatrix}
 3/10&3/10&0&0&2/5\\
 3/10&1/5&9/20&0&1/20\\
 0&9/20&1/5&3/10&1/20\\
 0&0&3/10&3/10&2/5\\
 2/5&1/20&1/20&2/5&1/10
 \end{pmatrix}.
\]
The characteristic polynomial of \(R-J_5\) is
\[
 x(40x^2-2x-7)(200x^2-10x-33)/8000.
\]
Thus \(\rho(R)=(1+\sqrt{281})/40<1/2<3\sqrt2/8\). So the equality law cannot be asserted for all nonsymmetric cores, despite the universal upper bound.

## Verification

The attached standard-library Python script `verify.py` uses exact rational arithmetic. It checks the complete spectral trace identity
\[
 \operatorname{tr}(P^k)=1+[1-(m+1)b]^k+(1-b)^k\bigl(\operatorname{tr}(Q^k)-1\bigr)
\]
for representative vertex-transitive bases and multiple rational hub weights, checks stochasticity and nonnegativity, computes the exact characteristic polynomial of \(R-J_5\), and checks the four-cycle nonedge-bound example. It reports `VERIFY_OK exact_rational_checks= 895`. These finite calculations corroborate but are not a substitute for the unrestricted proof in Steps 1–4. Reproduce using `python3 verify.py` in a directory containing this file.

## Relationship to prior work

Boyd, Diaconis and Xiao formulate fastest symmetric mixing as spectral-norm convex optimization. Boyd, Diaconis, Parrilo and Xiao prove symmetry reduction and, in Section 5.3.3 of their 2007 preprint, explicitly derive the wheel formula \(\rho(K_1\vee C_m)=(1-1/m)\rho(C_m)\). **The wheel result and the circle-core specialization of this finding are known, not claimed as new.** Boyd, Diaconis, Sun and Xiao give the exact fastest path chain used as a comparison. The new statement assessed here is the general transfer identity for every vertex-transitive base, including bases with several internal edge orbits and possibly disconnected bases, the universal upper bound without transitivity, and the explicit sharp boundary example. The primary papers examined do not state the general identity or this necessity example. The exact implication comparison and residual literature risks are recorded in `AUDIT.json`.

## Limitations

The result concerns **symmetric uniform-stationary** chains with allowed holding, not arbitrary reversible stationary measures, nonreversible chains, prescribed edge lower bounds, or mixing times with finite-state total-variation constants. Equality is guaranteed for vertex-transitive bases but is not characterized for every nontransitive base. The formula reduces the cone optimization to \(\rho(H)\); it does not by itself compute unknown base optima. Unindexed theses or specialist publications could contain equivalent general cone reductions. Independent audit has not been performed.

## References

1. S. Boyd, P. Diaconis, and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46(4), 667–689 (2004), DOI `10.1137/S0036144503423264`; lawful full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (first posted 2007-09-06), especially Sections 2, 3 and 5.3.3; https://arxiv.org/pdf/0709.0955.
3. S. Boyd, P. Diaconis, J. Sun, and L. Xiao, *Fastest Mixing Markov Chain on a Path*, American Mathematical Monthly 113(1), 70–74 (2006); https://web.stanford.edu/~boyd/papers/pdf/fmmc_path.pdf.
