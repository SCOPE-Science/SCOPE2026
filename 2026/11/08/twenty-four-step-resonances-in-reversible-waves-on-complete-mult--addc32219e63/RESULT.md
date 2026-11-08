# Twenty-four-step resonances in reversible waves on complete multipartite graphs

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be a labelled simple complete multipartite graph with \(r\ge 2\) and \(n_i\ge1\), and let \(N=\sum_i n_i\). Over any finite field \(\mathbb F_q\) of characteristic two, \(q=2^f\), let \(A\) denote the adjacency operator (entry \(1\) for adjacent vertices, entry \(0\) otherwise). The reversible two-time-level wave is
\[
T(u,v)=(v,u+Av),\qquad (u,v)\in\mathbb F_q^N\times\mathbb F_q^N.
\]
Write \(p\) for the number of odd-sized parts and \(e=r-p\) for the number of even-sized parts. Define the integers
\[
\rho=r-(r\bmod2),\quad s=p-(p\bmod2),\quad
\delta=\mathbf1_{\{p\text{ odd},\ e>0\}},\quad
b_2=\mathbf1_{\{p>0\text{ and }p\text{ even}\}},
\]
\[
b_1=s-2b_2,\qquad a_3=\delta,\qquad
 a_2=\rho-s-2\delta,\qquad a_1=N-2\rho+s+\delta.
\]
These five numbers are nonnegative integers. In a rational canonical description over the prime field \(\mathbb F_2\), the wave operator has blocks
\[
\boxed{T\sim J_2(1)^{\oplus a_1}\oplus J_4(1)^{\oplus a_2}
\oplus J_6(1)^{\oplus a_3}
\oplus C_h^{\oplus b_1}\oplus C_{h^2}^{\oplus b_2}},
\qquad h(z)=z^2+z+1,
\]
where \(J_j(1)\) is a unipotent Jordan block of size \(j\), and \(C_g\) is the companion matrix of \(g\). This decomposition over \(\mathbb F_2\) remains a valid matrix similarity after extending scalars to \(\mathbb F_q\); the polynomial \(h\) may split over the larger field.

For each positive integer \(t\), let \(\nu_2(t)\) be the exponent of \(2\) in \(t\), and put \(w_t=2^{\nu_2(t)}\). Then the exact count of configurations fixed by time \(t\) is
\[
\boxed{
\#\operatorname{Fix}(T^t)=q^{D(t)},\quad
D(t)=\sum_{j=1}^3 a_j\min(w_t,2j)
+\mathbf1_{\{3\mid t\}}\bigl(2b_1+2b_2\min(w_t,2)\bigr).}
\]
Every state is periodic, and \(T^{24}=I\). The exact number of states of least period \(m\mid24\) and the number of distinct time-orbits of that period are, respectively,
\[
P_m=\sum_{d\mid m}\mu(m/d)q^{D(d)},\qquad C_m=P_m/m.
\]
All other least periods have zero states. The **sharp global period** (the order of \(T\), also attained as the least period of a state) is completely classified:

| Parities of part sizes | Sharp period |
|---|---:|
| No odd parts (\(p=0\)) | \(4\) |
| Exactly one odd part (\(p=1\)) | \(8\) |
| At least three odd parts, odd \(p\), with \(e\ge1\) | \(24\) |
| Positive even \(p\) with \(e\ge2\) | \(12\) |
| All remaining admissible cases | \(6\) |

For the smallest mixed-parity graph producing period \(24\), \(K_{1,1,1,2}\), there are exactly \(720\) configurations of least period \(24\), forming \(30\) time-orbits. The complete binary least-period population at periods \(1,2,3,4,6,8,12,24\) is, respectively, \(2,2,30,12,30,48,180,720\), summing to \(2^{10}\) states.

## Assumptions and scope

The graph has no self-loops and has all possible cross-part edges but no within-part edges. The two rows \(u,v\) are ordered; exchanging them is not used to identify states. Simultaneous addition and vertex-neighbor summation are in \(\mathbb F_q\), not in the integers or in real arithmetic. There are no inhomogeneous terms or external inputs. All formulas hold for every labelled choice of positive part sizes, including singleton parts, and for every extension degree \(f\ge1\). The global period is temporal, not a graph-theoretic cycle length. The polynomial \(h\) is irreducible over \(\mathbb F_2\), but not necessarily over \(\mathbb F_q\).

## Proof

**1. Factor the adjacency map.** Let \(\sigma:\mathbb F_q^N\to\mathbb F_q^r\) take a vector to its \(r\) partwise coordinate sums, and let \(E:\mathbb F_q^r\to\mathbb F_q^N\) copy each coordinate to its entire part. The former is surjective and the latter injective. Put \(K=I_r+\boldsymbol1\boldsymbol1^{\mathsf T}\) and \(D=\operatorname{diag}(n_1\bmod2,\ldots,n_r\bmod2)\). Since the diagonal of \(K\) is zero in characteristic two and all other entries are one, \(A=EK\sigma\) and \(\sigma E=D\). In particular, for every \(j\ge1\),
\[
A^j=E(KD)^{j-1}K\sigma.
\]
Thus \(\operatorname{rank}A=\operatorname{rank}K=\rho\), and higher ranks reduce to matrices of size \(r\).

**2. Extract the ranks and nonzero Jordan blocks.** Order the odd parts first. When \(p\) is even, direct multiplication gives
\[
KDK=\begin{pmatrix}I_p&\boldsymbol1_p\boldsymbol1_e^{\mathsf T}\\
\boldsymbol1_e\boldsymbol1_p^{\mathsf T}&0\end{pmatrix},
\]
which has rank \(p\). When \(p\) is odd, it gives
\[
KDK=\begin{pmatrix}I_p+\boldsymbol1_p\boldsymbol1_p^{\mathsf T}&0\\0&\boldsymbol1_e\boldsymbol1_e^{\mathsf T}\end{pmatrix},
\]
which has rank \(p-1+\mathbf1_{\{e>0\}}\). Zero-dimensional blocks are interpreted as empty. Consequently
\[
\operatorname{rank}A^2=s+\delta.
\]
On part-constant vectors \(y\), let \(\theta\) be the sum of entries at the odd parts. The next part values are \(\theta+y_i\) at odd parts and \(\theta\) at even parts. If \(p\) is even, the induced map \(H\) satisfies \(H^3=H\); if \(p\) is odd, it satisfies \(H^3=H^2\). Applying this after the first adjacency update shows, respectively, \(A^4=A^2\) and \(A^4=A^3\), with \(\operatorname{rank}A^3=s\) in both cases. (The last rank also follows directly by summing the odd-part values after two updates.) Thus \(A\) has no nilpotent Jordan blocks larger than size \(3\).

The nonzero Jordan blocks of \(A\) are the same as those of \(KD\). Its odd-by-odd corner is \(L=I_p+\boldsymbol1_p\boldsymbol1_p^{\mathsf T}\); its even-column corner vanishes. If \(p\) is odd, then \(L^2=L\) has rank \(p-1\), so there are exactly \(p-1\) simple eigenvalue-one blocks. If \(p>0\) is even, then \(L=I+J\) with nonzero \(J\) of rank one and \(J^2=0\), giving one eigenvalue-one block of size two and \(p-2\) simple blocks. If \(p=0\), there are none. This proves the counts \(b_1,b_2\), including all boundary cases.

The zero-eigenvalue Jordan-block counts follow from the successive rank losses. One size-three zero block occurs exactly when \(\operatorname{rank}A^2-\operatorname{rank}A^3=\delta=1\). The size-two zero count is \(\rho-(s+\delta)-\delta=a_2\), and dimension conservation gives \(a_1=N-2\rho+s+\delta\). Therefore
\[
A\sim J_1(0)^{\oplus a_1}\oplus J_2(0)^{\oplus a_2}
\oplus J_3(0)^{\oplus a_3}
\oplus J_1(1)^{\oplus b_1}\oplus J_2(1)^{\oplus b_2}.
\]
In particular all five block counts are nonnegative, because they are Jordan multiplicities.

**3. Transfer each block to the reversible wave.** On a subspace where \(A\) is one Jordan block \(J_j(\lambda)\), the wave acts by the block matrix \(\bigl(\begin{smallmatrix}0&I\\I&A\end{smallmatrix}\bigr)\) of size \(2j\). Its characteristic polynomial is \(\det(z^2I+zA+I)\). If \(\lambda=0\), this is \((z+1)^{2j}\), and a fixed wave state must satisfy \(u=v\) and \(Au=0\). Since \(\dim\ker J_j(0)=1\), this is exactly a single Jordan block \(J_{2j}(1)\).

For \(\lambda=1\), set \(h(z)=z^2+z+1\). The wave satisfies the matrix identity \(T^2+\operatorname{diag}(A,A)T+I=0\), so \(h(T)=\operatorname{diag}(I+A,I+A)T\). If \(A=J_j(1)\), the kernel of \(h(T)\) has dimension \(2\); together with characteristic polynomial \(h(z)^j\), this implies one companion block \(C_{h^j}\) for \(j=1,2\). This proves the asserted wave decomposition.

**4. Count fixed configurations and determine the sharp period.** In characteristic two the root of \(z^{t}-1\) at \(1\) has multiplicity \(w_t=2^{\nu_2(t)}\). The polynomial \(h(z)\) divides \(z^t-1\) exactly when \(3\mid t\), in which case it appears with multiplicity \(w_t\). On \(J_{2j}(1)\), the kernel of \(T^t-I\) therefore has dimension \(\min(w_t,2j)\); on \(C_{h^j}\) its dimension is \(2\mathbf1_{\{3\mid t\}}\min(w_t,j)\). Summation over the block multiplicities gives the stated \(D(t)\), and over \(\mathbb F_q\) the corresponding fixed space has cardinality \(q^{D(t)}\).

The largest orders of the permitted primary blocks are \(2,4,8,3,6\), respectively. Therefore every orbit divides \(\operatorname{lcm}(8,3)=24\). Each nonzero primary summand admits a vector attaining its maximal block order, and vectors from independent summands can be added, so the exact order of \(T\) is the least common multiple of the orders of the blocks actually present. Substituting the explicit multiplicities yields the five parity cases in the theorem. Finally, each state fixed by \(T^t\) has least period dividing \(t\), and Möbius inversion gives the exact primitive-state and orbit counts.

## Verification

The standalone Python programs `verify_binary.py` and `verify_field4.py` use only the Python standard library. The binary program reconstructs the graph and wave matrices from the part sizes; it checks the predicted adjacency-power ranks, kernel dimensions of all wave powers \(1\le t\le24\), and the identity \(T^{24}=I\) on \(2891\) distinct multipartite parameter choices (with two through six parts and at most fourteen vertices). It independently enumerates complete time-orbits of all binary states for another \(84\) small graph choices, comparing least-period populations with Möbius inversion. The second program directly iterates pairs of rows over \(\mathbb F_4\), represented additively by two-bit field elements, for \(11\) graph choices with at most four vertices. Direct output is stored in `binary_output.txt` and `field4_output.txt`. These are finite corroborations; Steps 1--4 are the proof for every admissible graph and field.

## Relationship to prior work

Toffoli and Margolus, *Cellular Automata Machines* (1987), Section 14.2, introduce reversible second-order updates from a local rule. Vlasov (2013), Section 3, develops that construction further. Neither inspected exposition provides exact temporal periods for the specific multipartite neighbor-sum wave.

The published *Sharp period-four census for complete multipartite parity automata* (2026) derives ranks of adjacency powers and exact orbits for the **first-order** maps \(x\mapsto Ax\) and \(x\mapsto (I+A)x\). Those adjacency ranks provide some inputs to Step 2 above, but its first-order period bound (four) is not a statement about the two-time-level wave; the latter has genuine period \(24\) on mixed-parity graphs, which cannot occur in either first-order system. The additional Jordan transfer and exact wave-period census are essential here. The other related classification of two-row waves on strongly regular graphs treats a more restricted graph family; the unequal-size example \(K_{1,1,1,2}\) is not strongly regular and cannot be deduced by its parameter formula. Kantic, Qureshi, Panario and Legl (2026) study general algebraic algorithms for cycles of linear finite dynamical systems, without this explicit graph-and-parity-specific classification.

## Limitations

The result applies to characteristic-two finite fields and simple, undirected complete multipartite graphs, with this precise unforced linear reversible update. It does not extend automatically to odd characteristic, nonbinary edge weights, or other graph families. The first-order adjacency-power ranks are related to published work, and the general second-order method is classical; the claim of novelty concerns the full **two-row** Jordan decomposition, exact orbit counts, and the sharp period-24 resonance. Accessible searches and inspected source sections cannot rule out earlier equivalent work in unindexed literature. Independent mathematical review has not been performed.

## References

1. T. Toffoli and N. Margolus, *Cellular Automata Machines: A New Environment for Modeling*, MIT Press, 22 April 1987, Section 14.2, DOI: 10.7551/mitpress/1763.001.0001. Author-hosted full book: https://people.csail.mit.edu/nhm/cam-book.pdf.
2. A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297v1, submitted 18 November 2013, Section 3. https://arxiv.org/abs/1311.4297.
3. *Sharp period-four census for complete multipartite parity automata* (2026), published mathematical research record, 11 October 2026, especially the finding and proof on adjacency-power ranks.
4. J. Kantic, C. Qureshi, D. Panario and F. Legl, *On the Dynamics of Linear Finite Dynamical Systems Over Galois Rings*, arXiv:2604.01548v1, 2 April 2026, Sections 2--4. https://arxiv.org/abs/2604.01548.
