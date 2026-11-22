# The one-quarter exponent law for uniformly sampled \(\lambda\)-orbits in unitriangular radical braces

## Finding
Fix a prime power \(q\ge2\). Let \(J_n=\operatorname{NT}_n(\mathbb F_q)\) be the associative nilpotent algebra of strictly upper-triangular \(n\times n\) matrices. Give it the radical two-sided brace operations \(A+B\) and \(A\circ B=A+B+AB\). Its circle group acts on the additive group through \(\lambda_A(B)=B+AB\). Choose **one orbit uniformly from the finite orbit set** \(J_n/(1+J_n)\), and denote it by \(\mathcal U_n\); this differs from choosing a uniformly random point of \(J_n\).

For any representative \(B\in\mathcal U_n\), let \(R_n=\operatorname{rank}_{\mathbb F_q}B\) and \(L_n=\log_q|\mathcal U_n|\). These are independent of the representative. Put \(\Delta_n=L_n-\binom{R_n}{2}\). For every fixed prime power \(q\), there is a finite constant \(C_q\) such that for **every** integer \(n\ge2\),
\[
\boxed{\Delta_n\ge0,\qquad
\mathbb E|R_n-n/2|\le C_q,\qquad
\mathbb E\Delta_n\le C_q,\qquad
\mathbb E|L_n-n^2/8|\le C_q n.}
\]
Consequently \(R_n/n\to1/2\) and \(L_n/n^2\to1/8\) in \(L^1\) as \(n\to\infty\), with \(q\) fixed. The leading exponent is one quarter of the known \(1/2\) limit when **points** rather than distinct orbits are sampled uniformly; this is a substantial orbit-size bias.

A useful exact structural refinement underlies the assertion. For each subset \(S=\{m_1<\cdots<m_k\}\subseteq\{1,\ldots,n-1\}\), there are exactly
\[
w_{n,q}(S)=\prod_{i=1}^k(q^{m_i-i+1}-1)
\]
\(\lambda\)-orbits with suffix-rank increment set \(S\). Each has matrix rank \(k\) and orbit exponent
\[
L(S)=\sum_{i=1}^k(n-1-m_i)=\binom{k}{2}+\delta(S),\qquad
\delta(S)=\sum_{i=1}^k(n-k+i-1-m_i)\ge0.
\]
The displayed exact census is a *proof device* consistent with earlier finite transfer formulas. The assessed new claim is the uniform-in-dimension concentration under **equal-orbit sampling** and its separation from the uniform-point law, not first discovery of the finite enumeration.

## Assumptions and scope
All matrix ranks are over the finite field \(\mathbb F_q\); all operations are ordinary matrix operations. The action is by the **full** unitriangular group \(1+J_n\), not conjugation, right multiplication, or a double action. Since \(1+A\) is invertible, each orbit preserves the rank of \(B\), and the size is a power of \(q\). The random orbit is distributed uniformly over distinct orbits. No assumption on the characteristic is required. The constants may depend on \(q\); no limit in which \(q\) grows with \(n\) is asserted. For \(n=2\), every orbit is a singleton and the inequalities hold on enlarging the constant.

## Proof
**1. The full orbit and its row-rank exponent.** For each fixed \(B\),
\[\Lambda(B)=\{(I+A)B:A\in J_n\}=B+J_nB.\]
The \(i\)-th row of \(AB\) is an arbitrary linear combination of the rows of \(B\) below it, and the choices for different \(i\) are independent. Let \(B^{(m)}\) denote the lower-right \(m\times m\) principal suffix of \(B\), with \(B^{(1)}=0\). Thus
\[L(B)=\dim_{\mathbb F_q}(J_nB)=\sum_{m=1}^{n-1}\operatorname{rank}(B^{(m)}).\]
The suffix rank sequence is orbit-invariant, because the bottom-right suffix of \((I+A)B\) is obtained by applying an invertible upper-unitriangular matrix to the corresponding suffix of \(B\).

**2. A positive formula for the rank-increment profile.** Build \(B\) by adjoining a new top row to its lower-right suffix, from size \(1\) through \(n\). At the step adjoining \(m\) freely chosen entries, suppose the current suffix has rank \(r\). The new row belongs to its row span for exactly \(q^r\) choices, keeping rank \(r\), and increases the rank for exactly \(q^m-q^r\) choices, making rank \(r+1\). The orbit exponent increases by \(r\) in either case. Dividing each matrix population by its orbit size, the corresponding **numbers of orbits** are multiplied by \(1\) (no rank increase) or \(q^{m-r}-1\) (rank increase). These transitions are exact because ranks and the entire suffix-rank path are constant along orbits.

Record the steps at which rank increases as \(S=\{m_1<\cdots<m_k\}\). Immediately before stage \(m_i\), rank is \(i-1\). The orbit count is therefore \(w_{n,q}(S)\) as stated, and its orbit exponent equals the sum of all previous ranks. Each increase at stage \(m_i\) contributes to exactly \(n-1-m_i\) later stages, hence \(L(S)=\sum_i(n-1-m_i)\). Since \(m_i\le n-k+i-1\), subtraction from the latest possible \(k\) stages yields \(L(S)=\binom{k}{2}+\delta(S)\) with \(\delta(S)\ge0\). The rank of the final matrix is exactly \(k\). Thus \(\Delta_n=\delta(S)\) is a nonnegative intrinsic invariant of its orbit.

**3. Partition domination.** There is one subset with \(k\) increments at the latest possible stages \(n-k,n-k+1,\ldots,n-1\), whose orbit multiplicity is \((q^{n-k}-1)^k\). More generally, the shifts
\[a_i=n-k+i-1-m_i\quad(1\le i\le k)\]
form a weakly decreasing nonnegative sequence (a partition), fit into the rectangle of height \(k\) and width \(n-1-k\), and sum to \(\delta(S)\). Writing \(p(d)\) for the ordinary partition number, there are at most \(p(d)\) increment sets of given \((k,\delta=d)\). Furthermore,
\[
w_{n,q}(S)\le q^{\sum_i(m_i-i+1)}=q^{k(n-k)-\delta(S)}.
\]
For fixed \(q\), both constants
\[P_q=\sum_{d\ge0}p(d)q^{-d}=\prod_{j\ge1}(1-q^{-j})^{-1},\qquad
Q_q=\sum_{d\ge0}d\,p(d)q^{-d}\]
are finite. This follows from convergence of the Euler partition product and its first derivative at the interior point \(1/q<1\). Consequently, for every \(n,k\),
\[
\sum_{|S|=k}w_{n,q}(S)\le P_q q^{k(n-k)},\qquad
\sum_{|S|=k}\delta(S)w_{n,q}(S)\le Q_q q^{k(n-k)}.
\]

**4. Normalization and concentration.** Set \(k_0=\lfloor n/2\rfloor\) and \(D=\lfloor n^2/4\rfloor=k_0(n-k_0)\). The latest-stage increment pattern with \(k_0\) increases already contributes
\[
(q^{n-k_0}-1)^{k_0}=q^D(1-q^{-(n-k_0)})^{k_0}\ge\tfrac12 q^D
\]
orbits. The last inequality follows from \((1-t)^k\ge1-kt\) and \(k_0q^{-(n-k_0)}\le1/2\) for \(n\ge2\), \(q\ge2\). Therefore the total orbit count \(K_{n,q}\) obeys \(K_{n,q}\ge\tfrac12q^D\).

For any integer \(k\) between zero and \(n-1\),
\[q^{k(n-k)-D}\le q^{1/4}\,q^{-(k-n/2)^2}.\]
The Gaussian lattice sums \(\sup_{a\in[0,1]}\sum_{j\in\mathbb Z}q^{-(j+a)^2}\) and their first absolute moments are finite. Dividing the bounds in Step 3 by \(K_{n,q}\), and summing over \(k\), gives constants independent of \(n\) satisfying
\[
\mathbb E|R_n-n/2|\le C_q,\qquad
\mathbb E\Delta_n\le C_q.
\]
Finally, \(L_n=\binom{R_n}{2}+\Delta_n\), and for \(0\le R_n\le n-1\),
\[
\left|\binom{R_n}{2}-\frac{n^2}{8}\right|
\le\frac{3n}{4}|R_n-n/2|+\frac n2.
\]
Taking expectations proves \(\mathbb E|L_n-n^2/8|\le C_qn\), and dividing by \(n\) or \(n^2\) yields the claimed \(L^1\) limits. This is an infinite-dimensional analytic argument, not an extrapolation from finite enumeration.

## Verification
The standalone standard-library program `verify_orbit_sampling.py` independently enumerates actual full \(\lambda\)-orbits via all group actions for \((q,n)=(2,2),(2,3),(3,3),(5,3),(2,4),(3,4),(2,5)\), comparing every pair of matrix rank and orbit exponent with the rank-increment subset formula. It also checks a separate matrix-by-matrix recurrence for all \(q\in\{2,3,4,5,7\}\) and \(2\le n\le15\), and prints exact finite moment examples. A finite checker cannot certify the all-dimensions estimate; that follows from Steps 3 and 4. No Lean proof or independent expert audit is claimed.

For example, over \(\mathbb F_2\), \(n=5\) has \(158\) distinct \(\lambda\)-orbits and equal-orbit mean exponent \(2\), while \(n=10\) has \(162700898\) distinct orbits and mean exponent approximately \(11.388095\). The infinite-dimensional limit, not either small example, is the assessed result.

## Relationship to prior work
Properzi and Van Antwerpen [1] introduced common-divisor graphs of \(\lambda\)-orbits and their general numerical invariants; their work does not provide a uniform-random-*orbit* large-dimension law for the present family. Yan [2, §3.1] describes the relevant upper-unitriangular left matrix actions by row operations. These actions and their elementary orbit descriptions are established mathematics and are not claimed as new. Existing exact finite multiplicity transfers for this same brace family already determine each orbit-size coefficient and have been used to establish the **uniform-point** asymptotic \(L_n/n^2\to1/2\). The present claim deliberately does not repackage those coefficients as a novel enumeration: the new assertion is the quantitative **uniform-orbit** distributional bound, including the bounded partition defect and the \(1/8\) exponent law.

The \(q\)-Stirling literature [3] and the naturally-labelled-poset enumeration [4] supply well-known equivalent unrefined total orbit counts (at \(q=2\), OEIS A135922 [5]) and related rank layers (OEIS A139382 [6]); these are credited. Neither of their inspected statements provides a \(\lambda\)-orbit-size \(L^1\) concentration law under the equal-orbit measure. Such unrefined counts alone cannot yield the new two-invariant concentration without further analysis. The key new step is the partition-deficit domination of *individual orbit classes*, not an arithmetic restatement of the total-count formula. A broader unlocated earlier left-orbit asymptotic remains a historical-priority risk.

## Limitations
The result is for fixed \(q\) and grows only the matrix dimension. It does not provide a sharp limiting law on the scale \(n\), nor a uniform estimate when \(q\) varies. It makes no claim about conjugacy or coadjoint orbits, other radical braces, or a new exact orbit-size census. The previously known finite distribution and ordinary \(q\)-Stirling identities are essential neighboring results. Historical originality is assessed against the named inspected sources, not certified by an independent literature audit.

## References
[1] S. Properzi and A. Van Antwerpen, *Common divisor graphs for skew braces*, first public arXiv posting 2023-06-21, arXiv:2306.12415, https://arxiv.org/abs/2306.12415 .

[2] N. Yan, *Representations of finite unipotent linear groups by the method of clusters*, arXiv:1004.2674 (2010), especially §3.1, https://arxiv.org/abs/1004.2674 .

[3] Y. Cai, R. Ehrenborg and M. A. Readdy, *q-Stirling Identities Revisited*, Electronic Journal of Combinatorics 25(1), P1.37 (2018), https://doi.org/10.37236/6829 .

[4] D. Bevan, G.-S. Cheon and S. Kitaev, *On naturally labelled posets and permutations avoiding 12–34*, arXiv preprint 2023, arXiv:2311.08023, §2, https://arxiv.org/abs/2311.08023 .

[5] OEIS A135922, *Inverse binomial transform of the Galois numbers*, https://oeis.org/A135922 .

[6] OEIS A139382, *A Stirling-number-type triangle*, https://oeis.org/A139382 .
