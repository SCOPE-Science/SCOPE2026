# An antipodal matching reverses characteristic-five cubical wave clocks in small dimensions

## Finding

For every integer \(d\ge2\), let \(Q_d\) be the ordinary \(d\)-cube on the labelled vertex set \(\{0,1\}^d\). Let \(F_d\) be the graph on the **same** vertices formed by adjoining the perfect matching \(\{x,\bar x\}\) between antipodal vertices. Let \(A_G\) denote the loopless adjacency matrix of either graph over any finite field \(\mathbb F_q\) with \(q=5^f\), \(f\ge1\). The reversible two-time-level wave is
\[
 T_G(u,v)=(A_Gu-v,u),\qquad (u,v)\in\mathbb F_q^{2^d}\times\mathbb F_q^{2^d}.
\]

The exact orders of these permutations are:

| Dimension \(d\) | \(Q_d\) | \(F_d\) |
|:--:|--:|--:|
| \(2\) | \(20\) | \(30\) |
| \(3\) | \(30\) | \(12\) |
| \(4\) | \(60\) | \(60\) |
| \(5\) | \(60\) | \(30\) |
| \(d\ge6\) | \(60\) | \(60\) |

Thus adding just one antipodal edge per vertex increases the global clock at dimension two, decreases it at dimensions three and five, and leaves it unchanged at every other admissible dimension. These are exact global orders, attained by individual states; not merely upper bounds.

There is also a complete **labelled temporal-orbit census** for every dimension, time and field extension. For \(r\in\{0,1,2,3,4\}\), define
\[
 m_r^{Q}(d)=\sum_{\substack{0\le k\le d\\d-2k\equiv r\pmod5}}\binom dk,
 \qquad m_r^{F}(d)=\sum_{\substack{0\le k\le d\\d-2k+(-1)^k\equiv r\pmod5}}\binom dk.
\]
For either choice \(G\in\{Q,F\}\), abbreviate \(m_r=m_r^G(d)\) and define, for any positive integer \(t\),
\[
\begin{aligned}
 E_G(d,t)={}&2m_0\mathbf1_{4\mid t}+2m_1\mathbf1_{6\mid t}
 +m_2(1+\mathbf1_{5\mid t})\\
 &+m_3\mathbf1_{2\mid t}(1+\mathbf1_{5\mid t})
 +2m_4\mathbf1_{3\mid t}.
\end{aligned}
\]
Then the exact numbers of fixed labelled paired-row states, primitive-period states and primitive temporal orbits are, respectively,
\[
\begin{aligned}
 \#\operatorname{Fix}(T_G^t)&=q^{E_G(d,t)},\\
 \#\operatorname{Per}_\ell(T_G)&=\sum_{e\mid\ell}\mu(\ell/e)q^{E_G(d,e)},\\
 \#\operatorname{Orb}_\ell(T_G)&=\frac1\ell\sum_{e\mid\ell}\mu(\ell/e)q^{E_G(d,e)}.
\end{aligned}
\]
Here \(\mu\) is the ordinary Möbius function; \(\operatorname{Per}_\ell\) means *least* period exactly \(\ell\). Nonzero populations occur only at divisors of the respective orders in the table.

For either graph family, the proportion of paired-row states with least period sixty tends to one as \(d\to\infty\), with a quantitative bound
\[
 1-\frac{\#\operatorname{Per}_{60}(T_G)}{q^{2^{d+1}}}
 \le q^{-2m_0}+q^{-2(m_1+m_4)}+q^{-(m_2+m_3)}
 =O\!\left(q^{-\frac25 2^d+C\gamma^d}\right),\quad \gamma=2\cos(\pi/10)<2,
\]
for \(d\ge7\), where the \(m_r\) are those of the relevant graph. Here the constant \(C>0\) is absolute, and the equality is an upper-bound asymptotic scale. This shows that the small-dimensional nonmonotonicity disappears at the level of the global order, whereas maximal-period dominance emerges in high dimension.

## Assumptions and scope

Both graph families are finite, simple, undirected, unweighted and loopless. The ordinary cube has degree \(d\); \(F_d\) has degree \(d+1\) and \(2^d\) vertices. In particular, the symbol \(F_d\) means **antipodal matching augmentation**, not the graph formed by quotienting antipodal vertex pairs (which has half as many vertices). The restriction \(d\ge2\) avoids duplicating coordinate edges at dimension one. All vertex labels are retained, both time levels are independent, and spatial automorphisms are not factored out. Each field has characteristic exactly five and size \(5^f\). No assertion is made about other characteristics, nonlinear rules or a random update schedule.

## Proof

**1. Common character eigenbasis.** For \(S\subseteq\{1,\ldots,d\}\), let \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\), regarded as a vector over \(\mathbb F_q\). Orthogonality of Boolean characters and invertibility of \(2\) in characteristic five imply that the \(2^d\) vectors \(\chi_S\) form an eigenbasis. If \(|S|=k\), the sum of the coordinate-neighbor shifts acts by \(d-2k\), while the antipodal involution \(x\mapsto\bar x\) acts by \((-1)^k\). Therefore \(A_{Q_d}\) and \(A_{F_d}\) have, respectively, eigenvalues \(d-2k\) and \(d-2k+(-1)^k\), each contributed by \(\binom dk\) characters. Reduction modulo five gives exactly \(m_r^{Q}\) and \(m_r^{F}\).

**2. Universal two-dimensional wave blocks.** In the eigenmode with adjacency eigenvalue \(r\in\mathbb F_5\), the two-level update is
\[
 B_r=\begin{pmatrix}r&-1\\1&0\end{pmatrix},\qquad
 \det(XI-B_r)=X^2-rX+1.
\]
Its determinant is one, so every global state is periodic immediately. The complete block calculation in characteristic five is:

| \(r\) | Polynomial over \(\mathbb F_5\) | Exact order of \(B_r\) | \(\dim\ker(B_r^t-I)\) |
|:--:|:--|--:|:--|
| \(0\) | \(X^2+1\) | \(4\) | \(2\mathbf1_{4\mid t}\) |
| \(1\) | \(X^2-X+1\) | \(6\) | \(2\mathbf1_{6\mid t}\) |
| \(2\) | \((X-1)^2\) | \(5\) | \(1+\mathbf1_{5\mid t}\) |
| \(3\) | \((X+1)^2\) | \(10\) | \(\mathbf1_{2\mid t}(1+\mathbf1_{5\mid t})\) |
| \(4\) | \(X^2+X+1\) | \(3\) | \(2\mathbf1_{3\mid t}\) |

Indeed \(B_0^2=-I\); \(B_1^3=-I\); \(B_4^3=I\), with the stated smaller orders excluded by the companion matrices. At \(r=2\), \(B_2=I+N\) for a nonzero \(N\) satisfying \(N^2=0\), so \((I+N)^t=I+tN\); this has order five. At \(r=3\), \(B_3=-I+N\) with nonzero square-zero \(N\), so its odd powers have no fixed vectors and its even powers have a one-dimensional fixed space unless \(5\mid t\), when the entire block is fixed. The three separable rows have no partial fixed spaces. This proves the table without assuming diagonalizability of \(B_{\pm2}\).

**3. Global orders and their exceptional dimensions.** The exact order of \(T_G\) is the least common multiple of the orders in the block table for which \(m_r>0\). The residue sets of adjacency eigenvalues (ignoring multiplicity) are:

| \(d\) | Residues for \(Q_d\) | Residues for \(F_d\) |
|:--:|:--|:--|
| \(2\) | \(\{0,2,3\}\) | \(\{3,4\}\) |
| \(3\) | \(\{1,2,3,4\}\) | \(\{0,1,4\}\) |
| \(4\) | All five | \(\{0,1,2\}\) |
| \(5\) | All five | \(\{1,2,3,4\}\) |
| \(6\) | All five | \(\{0,2,3,4\}\) |
| \(d\ge7\) | All five | All five |

For \(Q_d\), five consecutive values \(d-2k\), \(0\le k\le4\), cover all residues as soon as \(d\ge4\). For \(F_d\), the eight consecutive indices \(k=0,\ldots,7\) give offsets \(1,2,2,3,3,4,4,0\pmod5\) relative to \(d\), so all five residues occur once \(d\ge7\); the smaller dimensions are checked directly from the given expression. Taking least common multiples now gives the displayed orders. Because each selected block occurs as an actual invariant direct summand, an initial state with nonzero components achieving the constituent block orders attains the lcm; sharpness needs no extrapolation from finite checks.

**4. Exact fixed populations and orbit inversion.** There are \(m_r\) independent copies of \(B_r\). Summing the last column of the block table, weighted by \(m_r\), proves the dimension \(E_G(d,t)\). Every \(h\)-dimensional linear subspace over \(\mathbb F_q\) has \(q^h\) elements. Finally, a state fixed by \(T_G^t\) has least period dividing \(t\), giving \(\#\operatorname{Fix}(T_G^t)=\sum_{\ell\mid t}\#\operatorname{Per}_\ell\); ordinary divisor Möbius inversion proves both population formulas.

**5. Maximal-period dominance.** For any \(d\ge7\), the global order is sixty. A state has a proper divisor of sixty as its least period exactly when it belongs to one of \(\operatorname{Fix}(T_G^{30})\), \(\operatorname{Fix}(T_G^{20})\), \(\operatorname{Fix}(T_G^{12})\). The block table shows that these spaces have codimensions, respectively, \(2m_0\), \(2(m_1+m_4)\), and \(m_2+m_3\) inside the \(2^{d+1}\)-dimensional state space. The union bound proves the displayed exact inequality. For \(Q_d\), each \(m_r\) is a binomial sum over one congruence class modulo five. For \(F_d\), each \(m_r\) is a binomial sum over two congruence classes modulo ten (one of each parity). Finite Fourier inversion of these binomial sums gives
\[
 m_r^G(d)=\frac{2^d}{5}+O\bigl((2\cos(\pi/10))^d\bigr)
\]
uniformly in \(r\), because every nontrivial tenth root of unity \(\omega\) obeys \(|1+\omega|\le2\cos(\pi/10)<2\). The claimed maximal-period density therefore tends to one at the stated scale.

## Verification

The included standalone Python 3 program `verify.py` independently builds both adjacency matrices from labelled binary vertices, forms the full wave matrices over \(\mathbb F_5\), computes exact ranks of \(T_G^t-I\), and compares the nullities to the above formula for all twelve divisors \(t\mid60\) and both graph families at dimensions two through five. It also checks the complete matrix orders and their sharpness via proper prime divisors, then verifies the claimed global-order table through dimension nineteen from the arithmetic formulas. The program has no external dependencies. Executing `python3 verify.py` produced 96 matching exact rank comparisons, eight matrix-order confirmations and 36 symbolic dimension-clock comparisons; captured output is embedded separately in `verification_output.txt`. The finite checks complement, and do not replace, the all-dimensional character-block proof.

## Relationship to prior work

The second-order reversible construction is classical, notably Vlasov (first public arXiv version 2013-11-18, §3). Linear cellular automata with memory are also discussed by Rowland and Yassawi (first public arXiv version 2012-09-26); their principal theorems characterize automatic sequence columns rather than finite folded-cube orbit populations. The adjacency character spectra of the folded cube and ordinary cube are explicitly established by Mirafzal (2023, Theorem 3.1 and Corollary 3.2). Those spectral formulas are **prior mathematical input, not a new theorem here**. The additional result is the characteristic-five wave block analysis, sharp nonmonotone antipodal clock response in dimensions two through five, and the all-dimensional primitive temporal census and density bound. A previous result on waves over characteristic two for cubes with one universal hub studies a different graph modification and field; its full text was inspected. Another previous result on mixed-arity Hamming waves studies characteristic two and different graph factors. Their stated results do not give the characteristic-five antipodal matching table. These comparisons do not establish absolute novelty relative to inaccessible or unindexed sources.

## Limitations

The formulas do not identify spatial-equivalence classes, nor treat characteristics other than five. The four exceptional dimensions are small; no claim is made that a generic graph-edge addition has the same effect. The two-dimensional block analysis relies crucially on the known adjacency character spectra and elementary finite-field linear algebra. The present mathematical review is not independent validation; priority against unseen equivalent formulations cannot be guaranteed.

## References

1. E. Rowland and R. Yassawi, *A characterization of p-automatic sequences as columns of linear cellular automata*, arXiv:1209.6008, first submitted 2012-09-26. https://arxiv.org/abs/1209.6008
2. A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297, first submitted 2013-11-18; see especially §3, Equation (2). https://arxiv.org/html/1311.4297v2
3. S. M. Mirafzal, *A note on the spectrum of the folded hypercube*, Acta Mathematica Universitatis Comenianae 92 (2023), 281–286; Theorem 3.1 and Corollary 3.2. https://www.iam.fmph.uniba.sk/amuc/ojs/index.php/amuc/article/view/1988 ; full-text HTML rendering: https://www.researchgate.net/publication/376263318_A_NOTE_ON_THE_SPECTRUM_OF_THE_FOLDED_HYPERCUBE
4. *A hub-induced period-eight parity transition for reversible waves on Boolean cubes* (2026), published research note, accessible full RESULT: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-hub-induced-period-eight-parity-transition-for-reversible-wave--f559fa00b785
5. *Twelve-step resonance and exact orbit census for mixed Hamming waves* (2026), published research note, accessible full RESULT: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-twelve-step-resonance-and-exact-orbit-census-for-mixed-hamming-w--ae5e876acfba
