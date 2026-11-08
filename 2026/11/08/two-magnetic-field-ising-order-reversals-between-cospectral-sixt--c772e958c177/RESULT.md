# Two magnetic-field Ising-order reversals between cospectral sixteen-spin graphs

## Finding

Let \(R=K_4\square K_4\) be the square rook graph, and let \(S\) be the Shrikhande graph. These are nonisomorphic strongly regular graphs with the same parameters \((16,6,2,2)\) and adjacency spectrum. For each graph \(G\), define its **field-resolved cut polynomial** by
\[
P_G(z,q)=\sum_{U\subseteq V(G)}z^{|U|}q^{|\delta_G(U)|},
\]
where \(\delta_G(U)\) consists of the edges with exactly one endpoint in \(U\). The following polynomial identity holds in \(\mathbb Z[z,q]\):
\[
\boxed{P_R(z,q)-P_S(z,q)=8q^{12}z^4(q^2-1)^6\bigl(z^8-4q^6z^6+6q^8z^4-4q^6z^2+1\bigr).}
\]

For every \(q>1\), put
\[
s_\pm(q)=2q^6\pm\sqrt{4q^{12}-6q^8+2}.
\]
Then \(2<s_-(q)<s_+(q)\). For \(0<z\le1\), define \(s=z^2+z^{-2}\). The exact sign order is
\[
\begin{array}{ll}
P_R(z,q)>P_S(z,q),&2\le s<s_-\ \text{or}\ s>s_+,\\
P_R(z,q)<P_S(z,q),&s_-<s<s_+,\\
P_R(z,q)=P_S(z,q),&s=s_-\ \text{or}\ s=s_+.
\end{array}
\]
For every \(0<q<1\), in contrast, \(P_R(z,q)>P_S(z,q)\) for every \(z>0\); for \(q=1\), the polynomials coincide.

For the antiferromagnetic Ising Hamiltonian
\[
\mathcal H_G(\sigma)=J\sum_{uv\in E(G)}\sigma_u\sigma_v-h\sum_{v\in V(G)}\sigma_v,
\quad J>0,\quad\sigma_v\in\{-1,+1\},
\]
write \(\beta>0\) for inverse temperature and \(Z_G(\beta,J,h)\) for the partition function. At every positive temperature there are **exactly two distinct positive magnetic fields** at which \(Z_R=Z_S\), namely
\[
\boxed{h_\pm(\beta,J)=\frac{1}{4\beta}\operatorname{arcosh}\!\left(\frac{s_\pm(e^{2\beta J})}{2}\right).}
\]
The rook partition function is larger for \(0\le h<h_-\) and \(h>h_+\), and the Shrikhande partition function is larger for \(h_-<h<h_+\). Finally,
\[
\lim_{\beta\to\infty}h_-(\beta,J)=J,
\qquad \lim_{\beta\to\infty}h_+(\beta,J)=3J.
\]
All comparisons are strict off the stated crossings. Spin reversal gives the corresponding result for negative fields.

## Assumptions and scope

Both graphs have labeled vertex set \(\{(a,b):a,b\in\mathbb Z/4\mathbb Z\}\). For \(R\), distinct vertices are adjacent exactly when they agree in one coordinate. For \(S\), vertices are adjacent when their coordinate difference lies in \(\{\pm(1,0),\pm(0,1),\pm(1,1)\}\). Each graph has exactly \(48\) undirected edges and degree \(6\). The cut polynomials are ordinary polynomials; the algebraic identity holds for arbitrary complex substitutions, although the sign statements require positive real arguments. We make no infinite-volume, thermodynamic-limit, or magnetic criticality claim: these are exact **finite-graph** comparisons, with the zero-temperature field limits stated above.

For the physical model, if \(U\) is the set of down spins, then \(|U|\) determines the magnetization and \(|\delta_G(U)|\) determines the interaction energy, giving exactly
\[
Z_G(\beta,J,h)=e^{-48\beta J+16\beta h}\,P_G(e^{-2\beta h},e^{2\beta J}).
\]
The multiplicative prefactor does not depend on which graph is used.

## Proof

**1. Exact finite polynomial identity.** If \(k=|U|\) and \(e_G(U)\) is the number of edges internal to \(U\), regularity gives
\[
|\delta_G(U)|=6k-2e_G(U).
\]
Thus the coefficient of \(z^kq^c\) is an integer count of subsets \(U\) with these two statistics. Partition the sixteen vertices into four coordinate rows, each with four positions. There are exactly \(16^4=65536\) choices of the four row masks. The cut count can be calculated without graph-isomorphism software:

- For \(R\), each row with \(r\) selected sites contributes \(r(4-r)\) horizontal cut edges, and each column with \(t\) selected sites contributes \(t(4-t)\) vertical cut edges.
- For \(S\), with row masks \(m_a\) and bit functions \(b_a(j)\in\{0,1\}\), the cut size is the sum, over \(a,j\in\mathbb Z/4\mathbb Z\), of the three XORs \(b_a(j)\oplus b_a(j+1)\), \(b_a(j)\oplus b_{a+1}(j)\), and \(b_a(j)\oplus b_{a+1}(j+1)\). These correspond to disjoint edge families of sizes sixteen, sixteen, and sixteen.

An exact enumeration of these explicitly listed row masks gives, setting \(D_k(q)=[z^k](P_R-P_S)\),
\[
D_k(q)=\begin{cases}
8q^{12}(1-q^2)^6,&k=4,12,\\
-32q^{18}(1-q^2)^6,&k=6,10,\\
48q^{20}(1-q^2)^6,&k=8,\\
0,&\text{all other }0\le k\le16.
\end{cases}
\]
These seventeen coefficient identities yield the displayed factorization by collecting powers of \(z\). The attached standard-library script `verify.py` provides a completely specified finite certificate: it evaluates the row formulas, independently counts via adjacency masks and an edge-increment recurrence, compares all integer coefficients, and checks every term of the stated factor. Both enumerations run through *all* sixteen-spin configurations. No partial sampling or numerical approximation enters the polynomial identity.

**2. Exact sign classification.** The parenthetical factor can be written as
\[
z^4 g_q(s),\qquad s=z^2+z^{-2}\ge2,\qquad
g_q(s)=s^2-4q^6s+6q^8-2.
\]
Because \((q^2-1)^6\ge0\), the sign away from \(q=1\) is the sign of \(g_q(s)\). If \(0<q<1\), \(g_q\) is strictly increasing for \(s\ge2\), while
\[
g_q(2)=2(q^2-1)^2(3q^4+2q^2+1)>0.
\]
If \(q>1\), the vertex of this quadratic is at \(s_0=2q^6>2\), where
\[
g_q(s_0)=-2(q^4-1)^2(2q^4+1)<0.
\]
Together with \(g_q(2)>0\) and positive leading coefficient, this proves that the two distinct roots \(s_-\), \(s_+\) both exceed \(2\), and that the three sign intervals have the asserted order.

**3. Magnetic-field crossings and low-temperature limits.** For nonnegative field \(h\), substitute \(q=e^{2\beta J}>1\) and \(z=e^{-2\beta h}\). Then \(s=2\cosh(4\beta h)\) increases strictly from \(2\) to infinity as \(h\) runs from zero to infinity. The two roots therefore give exactly the two fields above. As \(q\to\infty\), direct expansion yields \(s_-(q)\sim\tfrac32q^2\) and \(s_+(q)\sim4q^6\). Since \(\operatorname{arcosh}(x)\sim\log(2x)\) for \(x\to\infty\), the crossing fields tend to \(J\) and \(3J\), respectively. Spin reversal makes the partition functions even in \(h\).

## Verification

Run `python3 verify.py` from the package directory. It uses only the Python standard library and checks two independent encodings of both graphs, all \(65536\) subsets on each graph, the degree-six graph identity, subset-count normalizations \(\binom{16}{k}\), all \(35\) nonzero coefficient differences, and the previously known zero-field specialization as a consistency test. The certificate is finite and exhaustive; its scope is exactly the two sixteen-vertex graphs in the theorem. The inequalities and asymptotics follow analytically from the factored polynomial, not from floating-point experiments.

## Relationship to prior work

The cut-polynomial representation is standard in the two-spin Ising model. Galanis–Štefankovič–Vigoda study antiferromagnetic partition functions and approximation complexity on bounded-degree graphs; Chelkak–Cimasoni–Kassel give zero-field combinatorial formulations on graph surfaces; and Peters–Regts study complex-field zero locations. None of the primary material examined for these works contains a field-dependent comparison of this specific cospectral pair. The preexisting zero-field identity
\[
P_R(1,q)-P_S(1,q)=16q^{12}(q^2-1)^8(3q^4+2q^2+1)
\]
is reproduced by setting \(z=1\) and is **not claimed as new**. A prior full-field rook-graph phase diagram likewise does not determine the Shrikhande polynomial or the two finite-temperature crossing fields. Previously tabulated graph parameters and independence complexes cannot supply the joint cut-by-cardinality coefficients without additional computation.

## Limitations

The statement is specific to two labeled sixteen-vertex graphs, not a classification of arbitrary strongly regular graphs. It does not claim that these finite-system crossings are singular thermodynamic phase transitions. Although checked literature and available records did not reveal the two-variable factorization or sign reversals, an unindexed graph-polynomial table or a different normalization of a two-spin partition function might contain an equivalent identity. The self-review is not an independent scientific audit. Numerical verification is unnecessary for the analytic sign classification; the exact finite coefficient certificate is indispensable for the specialized polynomial identity.

## References

1. A. Galanis, D. Štefankovič, and E. Vigoda, *Inapproximability of the Partition Function for the Antiferromagnetic Ising and Hard-Core Models*, arXiv:1203.2226 (first public version 2012-03-10), https://arxiv.org/abs/1203.2226 .
2. D. Chelkak, D. Cimasoni, and A. Kassel, *Revisiting the combinatorics of the 2D Ising model*, arXiv:1507.08242 (first public version 2015-07-29), https://arxiv.org/abs/1507.08242 .
3. H. Peters and G. Regts, *Location of zeros for the partition function of the Ising model on bounded degree graphs*, Journal of the London Mathematical Society (online 2019-11-05), https://doi.org/10.1112/jlms.12286 .
4. Graph reference for the Shrikhande graph and the rook graph: https://jaanos.github.io/tables/graphs/Shrikhande.html .
