# The unique noise-optimal universal three-point Fourier sampling orbit on the 25-cycle

## Finding

For the unnormalized cyclic Fourier matrix
\[
F_{25}=\bigl(e^{2\pi i rc/25}\bigr)_{r,c\in\mathbb Z_{25}},
\]
choose three distinct sample positions \(R\) before the three-frequency support \(C\) is specified. For a given support, the restricted Fourier matrix maps its three amplitudes to the three samples. The worst squared lower sampling bound over supports is
\[
\gamma(R)=\min_{C\subset\mathbb Z_{25},\ |C|=3}
\lambda_{\min}\bigl(F_{25}[R,C]F_{25}[R,C]^*\bigr).
\]

**Theorem.** Exactly 1,250 of the \(\binom{25}{3}=2300\) sampling triples have \(\gamma(R)>0\). Under affine transformations \(R\mapsto aR+b\), \(a\in(\mathbb Z_{25})^\times\), they form three orbits of sizes 250, 500 and 500, represented by \(\{0,1,2\}\), \(\{0,1,3\}\) and \(\{0,1,4\}\). **The complete set of 500 global maximizers** is the orbit of the nonconsecutive triple \(\{0,1,4\}\). In each of the three representatives, the *only* worst three-frequency sets are the 25 translates of \(\{0,1,2\}\). For any affine image of a representative, transport these column triples by the inverse multiplier in the same affine action.

Writing \(\gamma_k=\gamma(\{0,1,k\})\), exact rational interval certificates give
\[
\begin{aligned}
0.00044&<\gamma_2<0.00050,\\
0.0017&<\gamma_3<0.0018,\\
0.0039&<\gamma_4<0.0040.
\end{aligned}
\]
The exact algebraic values are the smallest eigenvalues of the explicit matrices
\[
H_k=\left(\sum_{c=0}^2\zeta^{(r_i-r_j)c}\right)_{i,j=0}^{2},\qquad
(r_0,r_1,r_2)=(0,1,k),\quad \zeta=e^{2\pi i/25},
\]
for \(k=2,3,4\). Approximate values \(0.000451096647871\), \(0.001778104926513\), \(0.003950281493420\) are diagnostics, *not* proof inputs.

The complete affine row-orbit table is:

| Representative | Number of row triples | Universal? |
|---|---:|---|
| \(\{0,1,2\}\) | 250 | yes |
| \(\{0,1,3\}\) | 500 | yes |
| \(\{0,1,4\}\) | 500 | yes; uniquely best orbit |
| \(\{0,1,5\}\) | 500 | no |
| \(\{0,1,10\}\) | 500 | no |
| \(\{0,5,10\}\) | 50 | no |

## Assumptions and scope

All indices are residues modulo 25; frequency and sampling sets are *unordered* sets of cardinality three, with no repetitions. The Fourier matrix is **unnormalized**: every matrix entry has absolute value one, so row-Gram diagonal entries are three. The least eigenvalue is of the Hermitian three-by-three row Gram matrix; no additional factor of 25 or 3 is inserted. The objective asks for invertibility on **each fixed support** and maximizes the worst squared singular value across supports. With the support supplied for amplitude recovery, the worst Euclidean noise amplification of a universal design is \(\gamma(R)^{-1/2}\). The claim is for order 25 only, with no inference to larger prime squares.

Universal invertibility does not identify an unknown support from three samples. For a universal design, two different three-frequency supports each map their amplitude space onto \(\mathbb C^3\). A generic sample vector therefore has distinct preimages with exactly those two supports; amplitudes need not vanish, since a zero amplitude for either inverse map confines the sample vector to a proper hyperplane.

## Proof

**1. Universality and the six affine classes.** The prime-power full-spark characterization [1, Theorem 9] says that three rows of the Fourier matrix of order 25 are full spark if and only if their residue populations modulo 5 differ by at most one. For three rows this is equivalent to three distinct residues modulo 5. If two rows agree modulo 5, the column set \(\{0,5,10\}\) gives identical corresponding rows, proving nonuniversality directly. The checker `certify.py` enumerates all \(\binom{25}{3}=2300\) triples and all affine transformations (20 unit multipliers and 25 translations). Exact integer set operations yield precisely the six disjoint affine orbits and their cardinalities in the table. A row transformation \(r\mapsto ar+b\) sends \(F_{25}[R,C]\) to a column-phase multiple of \(F_{25}[R,aC]\), so it preserves all singular values after relabelling columns.

**2. Reduce 2,300 column sets to 92 classes.** For fixed rows, replacing \(C\) by \(C+t\) multiplies each row by a unit complex number and does not alter singular values. The 2,300 three-frequency sets comprise exactly 92 translation orbits, all of length 25. The checker constructs these orbits exhaustively from the integer triples. One class is the 25 consecutive triples \(\{t,t+1,t+2\}\). For each universal representative \(\{0,1,k\}\), the Gram for this class is \(H_k\) above.

**3. Rationally enclose the entire Fourier table.** The exact checker uses Machin's identity
\[
\pi=16\arctan(1/5)-4\arctan(1/239)
\]
with 40 alternating Taylor terms in each arctangent. Its stated alternating-series remainder is below \(10^{-50}\). For angles reduced to absolute value at most \(24\pi/25\), 20 Taylor terms each for sine and cosine have errors less than \(10^{-18}\). Rounding both rational components to denominator \(D=10^9\) yields an explicitly checked Gaussian-integer approximation to every \(\zeta^j\) with complex error **strictly below \(1/D\)**. Hence every off-diagonal Gram entry is approximated within \(3/D\). The Gram matrices have identical exact diagonals, so the Hermitian spectral perturbation is less than \(6/D\), smaller than the certificate guard band \(\varepsilon=10^{-6}\).

**4. Exactly certify every least eigenvalue comparison.** `certify.py` computes three leading principal minors of \(D(\widetilde H-tI)\) using Gaussian-integer addition, multiplication, and squaring, for all \(k=2,3,4\) and all 92 column translation representatives. Sylvester's criterion certifies positivity of \(\widetilde H-(t+\varepsilon)I\) at every one of the 91 **nonconsecutive** column classes, for respective thresholds \(t=1/1000,1/250,1/100\). In the consecutive class, it computes a negative determinant of \(\widetilde H-(t-\varepsilon)I\), certifying a strictly smaller eigenvalue. The \(6/D\) perturbation bound transfers these strict inequalities to the actual complex Gram matrices. This proves that the **only** minimizers among columns are the 25 consecutive sets for each representative. Repeating exact rational tests at the lower-plus-\(\varepsilon\) and upper-minus-\(\varepsilon\) endpoints establishes the three displayed disjoint intervals. The group-orbit reduction then proves the global maximum is reached exactly by the 500 affine images of \(\{0,1,4\}\).

The `certify.py` executable uses only the Python standard library and makes no floating-point decisions. Every assertion must pass; its emitted `certify_output.txt` records the exhaustive class counts and determinant bounds. The independent `independent_check.py` numerically constructs all 6,900 Fourier restrictions for the three universal representatives using a separately implemented complex Gram eigensolver and independently finds exactly 25 minimizing columns in each case. Its floating-point calculations are diagnostic and not a substitute for the rational certificate.

## Verification

From the extracted package, run `python3 certify.py`, then `python3 independent_check.py` with NumPy installed. The complete integer certificate checks 6 row orbits, 92 translated column classes per universal representative, 273 nonconsecutive threshold tests, and all critical interval endpoints. It proves the eigenvalue order by exact integer signs and rigorous approximation bounds; the separate double-precision computation confirms diagnostics. Program source and the recorded outputs are included. The exact proof uses a known full-spark classification [1] plus a finite, exhaustive certificate for this fixed dimension.

## Relationship to prior work

Alexeev–Cahill–Mixon [1, Theorem 9 and its proof] characterize the **positive-versus-zero** full-spark condition on prime-power Fourier matrices. Their discussion distinguishes the need for conditioning but does not supply this minimax solution. Osgood–Siripuram–Wu [2, Theorem 4] characterize universal sampling patterns; Appendix A studies condition-number difficulties for *consecutive* samples with an illustrative lower bound. This exact comparison across **all** sampling rows at modulus 25, including strict improvement by a nonconsecutive orbit and the complete list of worst spectral supports, is not implied by those results. A published computational rank classification at other cyclic orders likewise does not determine these least eigenvalues. Searches for equivalent singular-value and noise-stability formulations did not identify a covering result, but unindexed or implicit prior calculations remain possible.

## Limitations

The result is deliberately finite and exactly at cyclic order 25; it gives no closed formula for arbitrary prime-square orders, and no claim of a universal all-moduli optimality pattern. Numerical eigenvalue decimals are illustrative; strict inequalities rest on the embedded integer/rational certificate and its explicit approximation analysis. The polynomial full-spark theorem is cited rather than reproved here. These checks and the accompanying scientific review are not an independent audit, and historical priority cannot be proved by absence of a search hit.

## References

[1] B. Alexeev, J. Cahill, and D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548, first publicly posted 2011-10-17, especially Theorem 9, https://arxiv.org/pdf/1110.3548 .

[2] B. Osgood, A. Siripuram, and W. Wu, *Discrete Sampling and Interpolation: Universal Sampling Sets for Discrete Bandlimited Spaces*, arXiv:1204.0992, first publicly posted 2012-04-04, especially Theorem 4 and Appendix A, https://arxiv.org/pdf/1204.0992 .
