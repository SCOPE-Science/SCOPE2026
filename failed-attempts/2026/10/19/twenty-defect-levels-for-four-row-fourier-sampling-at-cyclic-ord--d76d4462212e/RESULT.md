# Twenty defect levels for four-row Fourier sampling at cyclic order twelve

## Finding
Let \(\zeta=e^{2\pi i/12}\) and let \(F=(\zeta^{rc})_{r,c\in\mathbb Z_{12}}\) be the unnormalized cyclic Fourier matrix. For each four-element subset \(R\subset\mathbb Z_{12}\), define its **four-column singularity count**
\[
d(R)=\#\{C\subset\mathbb Z_{12}:|C|=4,\ \det F[R,C]=0\}.
\]
Among the \(\binom{12}{4}=495\) row subsets, the complete distribution of \(d(R)\) is
\[
\begin{array}{c|rrrrrrrrrr}
d&0&3&15&27&39&51&63&66&69&72\\\hline
\#R&24&48&48&24&48&24&48&12&12&12
\end{array}
\]
\[
\begin{array}{c|rrrrrrrrrr}
d&90&99&105&171&207&255&270&303&351&414\\\hline
\#R&24&72&24&12&24&12&6&12&6&3.
\end{array}
\]
Thus there are **exactly twenty attainable defect levels**, and the number of ordered row/column pairs of singular four-by-four minors is exactly
\[
\boxed{40\,608\text{ out of }245\,025,\quad \frac{40\,608}{245\,025}=\frac{1504}{9075}.}
\]
There are precisely twenty-one orbits of four-element row sets under affine maps \(r\mapsto ar+b\), where \(a\in\{1,5,7,11\}\) and \(b\in\mathbb Z_{12}\). All orbit representatives, orbit sizes, and exact defect counts are listed in the proof.

There is a structural distinction not visible from uniform-distribution tests: the row sets \(R_1=\{0,1,2,4\}\) and \(R_2=\{0,1,3,5\}\) have identical **sorted residue-occupancy multisets modulo every proper divisor** of twelve, yet
\[
d(R_1)=15,\qquad d(R_2)=27.
\]
Consequently, the defect count cannot be determined solely from the unordered residue-class occupancy data at the divisors of twelve.

## Assumptions and scope
Every row set and column set has exactly four **distinct** indices in \(\mathbb Z_{12}\). Row/column pairs are ordered as pairs \((R,C)\), but the elements within each set are unordered. A minor is singular exactly when its complex determinant vanishes. The Fourier matrix is unnormalized; changing the sign in its exponential or multiplying its entries by nonzero row or column factors does not affect singularity. No extension of the census to other Fourier orders or to nonsquare minors is claimed.

The affine group here has forty-eight elements: four units multiplied by twelve translations. It need not act freely on row sets. A residue-occupancy multiset modulo a divisor \(m\) is the sorted vector of counts \(\big(\#\{r\in R:r\equiv j\pmod m\}\big)_{j=0}^{m-1}\), including zeros.

## Proof
**1. Affine invariance.** Translating \(R\) by \(b\) multiplies column \(c\) of the restricted matrix by the nonzero scalar \(\zeta^{bc}\). Multiplication of the row indices by a unit \(a\in\mathbb Z_{12}^{\times}\) replaces the column labels \(c\) by \(ac\), a permutation of all four-element column sets. Therefore \(d(aR+b)=d(R)\). Enumerating all \(495\) four-element row sets and their forty-eight affine images gives exactly the following twenty-one disjoint orbits. For each orbit the table lists its lexicographically least representative, its size, and its value of \(d\):

| Representative \(R\) | Orbit size | \(d(R)\) |
|---|---:|---:|
| \(\{0,1,2,3\}\) | 24 | 0 |
| \(\{0,1,2,5\}\) | 48 | 3 |
| \(\{0,1,2,4\}\) | 48 | 15 |
| \(\{0,1,3,5\}\) | 24 | 27 |
| \(\{0,1,2,6\}\) | 48 | 39 |
| \(\{0,1,3,4\}\) | 24 | 51 |
| \(\{0,1,3,7\}\) | 48 | 63 |
| \(\{0,1,2,7\}\) | 12 | 66 |
| \(\{0,1,5,6\}\) | 12 | 69 |
| \(\{0,1,3,10\}\) | 12 | 72 |
| \(\{0,1,3,6\}\) | 24 | 90 |
| \(\{0,1,3,9\}\) | 48 | 99 |
| \(\{0,1,4,5\}\) | 24 | 99 |
| \(\{0,1,4,7\}\) | 24 | 105 |
| \(\{0,1,4,9\}\) | 12 | 171 |
| \(\{0,1,4,8\}\) | 24 | 207 |
| \(\{0,2,4,6\}\) | 12 | 255 |
| \(\{0,1,6,7\}\) | 6 | 270 |
| \(\{0,2,4,8\}\) | 12 | 303 |
| \(\{0,2,6,8\}\) | 6 | 351 |
| \(\{0,3,6,9\}\) | 3 | 414 |

The orbit sizes sum to \(495\), and their representatives are inequivalent because the explicit affine-orbit sets are pairwise disjoint. Consequently, the table exhausts all four-row sets.

**2. Exact determinant decision.** The primitive twelfth root \(\zeta\) has minimal polynomial \(\Phi_{12}(z)=z^4-z^2+1\). Expand any four-by-four Fourier minor using the twenty-four terms of the Leibniz formula, and reduce it modulo \(\Phi_{12}\). Its result is a vector of four integers \((v_0,v_1,v_2,v_3)\) representing \(v_0+v_1\zeta+v_2\zeta^2+v_3\zeta^3\). Because the degree of \(\zeta\) over \(\mathbb Q\) is exactly four, the complex determinant vanishes if and only if all four coordinates vanish. Each power \(\zeta^e\), for \(0\leq e<12\), has coordinates in \(\{-1,0,1\}\), hence \(|v_j|\leq24\). The standalone checker explicitly implements all reductions and enumerates the \(495\) possible column sets for each representative. It gives the twenty-one counts in the table without a floating-point comparison.

**3. Second exact arithmetic certificate.** For independent zero decisions use the finite field \(\mathbb F_{61}\). The four elements \(21,29,32,40\) are distinct primitive twelfth roots in this field, and they are the four roots of \(\Phi_{12}\) there. Evaluate every four-by-four determinant independently by Gaussian elimination modulo \(61\) at all four roots. If all four values vanish, its degree-at-most-three reduced determinant polynomial has four distinct roots in \(\mathbb F_{61}\), so all its integer coefficients are divisible by \(61\). The preceding bound \(|v_j|\le24<61\) forces all coefficients to be zero. Conversely an identically zero cyclotomic determinant vanishes at all four roots. Thus the finite-field test is an **if-and-only-if exact certificate**, not a randomized residue check. Both implementations agree on every representative/column pair.

**4. Aggregation and residue boundary.** For each orbit, multiply its size by its representative's singular-column count. Adding gives \(40\,608\) ordered singular row/column pairs, while all pairs number \(495^2=245\,025\); division reduces the ratio to \(1504/9075\). The twenty defect levels follow by combining the two size contributions at level \(99\). For \(R_1\) and \(R_2\) above, the sorted occupancy vectors are \((1,3)\) modulo two, \((1,1,2)\) modulo three, \((0,1,1,2)\) modulo four, and \((0,0,1,1,1,1)\) modulo six. Yet their counts are \(15\) and \(27\), respectively. This proves the final structural conclusion.

## Verification
Run `python3 verify_fourier12.py` with Python 3 and no third-party packages. The checker constructs the full affine partition, enumerates each orbit representative against all \(495\) four-column choices, computes each determinant independently using exact cyclotomic coordinates and four finite-field Gaussian eliminations, and asserts agreement on all \(10\,395\) representative/column pairs. It then asserts all twenty-one orbit triples, the twenty-level distribution, the total of \(40\,608\), and the divisor-occupancy counterexample. The exact completed output is provided in `verification_output.txt`.

## Relationship to prior work
Caragea and Lee (arXiv:2409.09793, first public September 15, 2024) investigate **principal minors**, establish a nonsquarefree-order existence obstruction, and explicitly discuss the difficulty of four-by-four principal minors. This supplies the natural Fourier-minor question and is not a twenty-level incidence census for arbitrary row and column sets. Cabrelli, Molter and Negreira (arXiv:2404.02229, first public April 2, 2024) connect invertibility of Fourier **principal minors** to weaving bases, without enumerating the off-principal four-row defect distribution. Alexeev, Cahill and Mixon (arXiv:1110.3548) give full-spark criteria and divisor-uniformity obstructions, which are Boolean existence statements rather than exact defective-column counts.

A published order-twelve full-spark classification (record `2026/10/4/SCOPE-complete-full-spark-classification-for-the-order-12-dft--81a97859d04e`) identifies the twenty-four full-spark four-row sets but does not count bad four-column choices for the remaining row sets. A related all-modulus theorem (record `2026/10/4/SCOPE-exact-singular-minors-for-the-near-consecutive-four-row-harmonic--bb8a5601ae6d`) gives exactly fifteen singular choices for the single row pattern \(\{0,1,2,4\}\) in order twelve; that one orbit is included here and does not imply the other twenty orbit counts. A four-by-four incidence classification over \(\mathbb F_3^2\) concerns a nonisomorphic Fourier group and has different uniform statistics. The complete cyclic-order-twelve twenty-level incidence distribution and the residue-occupancy counterexample are not statements or consequences of these inspected sources.

## Limitations
This is an **exact finite-order classification** and does not prove a formula for arbitrary Fourier orders, classify the ranks below four of singular submatrices, or provide conditioning estimates for nonsingular minors. The proof relies on a fully specified exhaustive finite enumeration that is logically exhaustive only because its domains and exact determinant tests are explicit. An unindexed earlier numerical table or an equivalent matroid-invariant tabulation could affect priority; the literature comparison is a best-knowledge assessment, not an absolute uniqueness guarantee. No independent mathematical audit has been performed.

## References
1. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793 (first public 2024-09-15), https://arxiv.org/html/2409.09793v4.
2. C. Cabrelli, U. Molter and F. Negreira, *Weaving Riesz Bases*, arXiv:2404.02229 (first public 2024-04-02), https://arxiv.org/html/2404.02229v2.
3. B. Alexeev, J. Cahill and D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548, https://arxiv.org/abs/1110.3548.
4. *Complete full-spark classification for the order-\(12\) DFT*, published mathematical record `2026/10/4/SCOPE-complete-full-spark-classification-for-the-order-12-dft--81a97859d04e`.
5. *Exact singular minors for the near-consecutive four-row harmonic frame*, published mathematical record `2026/10/4/SCOPE-exact-singular-minors-for-the-near-consecutive-four-row-harmonic--bb8a5601ae6d`.
6. *The four-by-four Fourier-minor incidence of the ternary affine plane*, published mathematical record `2026/10/11/SCOPE-the-four-by-four-fourier-minor-incidence-of-the-ternary-affine-p--9f007d7c322e`.
