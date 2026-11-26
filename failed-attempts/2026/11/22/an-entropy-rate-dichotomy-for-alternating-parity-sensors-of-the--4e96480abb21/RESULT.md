# An entropy-rate dichotomy for alternating parity sensors of the doubling map

## Finding

Let \(T(x)=2x\bmod 1\) on \([0,1)\), with Lebesgue-distributed initial state. For every pair of **nonzero** polynomials \(p,q\in\mathbb F_2[s]\), use their coefficients to define finite binary-digit parity observables \(B_p,B_q\) as in the next section. Consider two ways to alternate the observations, corresponding to the two sampling protocols in Tsuneda (2024):

\[
U_{2k}=B_p(T^{2k}x),\quad U_{2k+1}=B_q(T^{2k+1}x),
\]
\[
V_{2k}=B_p(T^kx),\quad V_{2k+1}=B_q(T^kx),\qquad k\ge0.
\]

Write \(p(s)=p_e(s^2)+s p_o(s^2)\) and \(q(s)=q_e(s^2)+s q_o(s^2)\), and define the polynomial
\[
\Delta(z)=p_e(z)q_e(z)+z p_o(z)q_o(z)\in\mathbb F_2[z].
\]
Here addition and multiplication in the formula for \(\Delta\) are over \(\mathbb F_2\). With \(H_2\) denoting joint Shannon entropy in bits, the **complete entropy-rate classification** is:

1. If \(\Delta\ne0\), every finite block of \(U\) consists of independent fair bits. In particular, \(H_2(U_0,\ldots,U_{2N-1})=2N\) for every \(N\ge1\).
2. If \(\Delta=0\), then \(H_2(U_0,\ldots,U_{2N-1})=N+O_{p,q}(1)\); equivalently, the entropy rate of \(U\) is exactly \(1/2\) bit per reported bit. The exceptional condition is the finite polynomial identity \(p(s)q(s)=s r(s)^2\) for some nonzero \(r\in\mathbb F_2[s]\).
3. For **every** such nonzero pair \(p,q\), \(H_2(V_0,\ldots,V_{2N-1})=N+O_{p,q}(1)\). The entropy rate of the second protocol is always \(1/2\) bit per reported bit, regardless of its pairwise correlations.

The entropy gap cannot be diagnosed from pairwise correlations alone. For example, \(p(s)=1+s\) and \(q(s)=1+s^2\) in the second protocol give **pairwise independent fair** reported bits, but for every \(N\ge1\)
\[
H_2(V_0,\ldots,V_{2N-1})=N+1,
\qquad V_{2k+1}=V_{2k}\oplus V_{2k+2}.
\]
The first protocol also admits pairwise-independent examples of entropy rate \(1/2\), namely \(p(s)=1+s\) and \(q(s)=s+s^2+s^3+s^4\). Here \(H_2(U_0,\ldots,U_{2N-1})=N+2\) for \(N\ge2\), and \(U_1=U_2\oplus U_4\).

## Assumptions and scope

Take the canonical binary expansion \(x=\sum_{j\ge0}\xi_j(x)2^{-(j+1)}\) on \([0,1)\), choosing the terminating expansion at dyadic rationals. Under Lebesgue measure, its digits \(\xi_j\) are independent fair bits, and \(\xi_j(T^kx)=\xi_{j+k}(x)\). If \(p(s)=\sum_{j=0}^d p_j s^j\) with coefficients in \(\mathbb F_2\), set \(B_p(x)=\bigoplus_{j:p_j=1}\xi_j(x)\). Both sensors are finite and nonzero; the result is not asserted for arbitrary measurable binary functions or for non-Lebesgue initial distributions. The probabilities and entropies refer to the exact real-valued doubling map, not its finite-precision implementations. The schedules are known, deterministic and two-periodic. We consider Shannon entropy of the indicated observed finite blocks, not topological entropy of the underlying map.

## Proof

**Coding into linear forms.** Every parity observation is a linear functional on independent \(\mathbb F_2\)-valued input digits. The vector of any finite collection of such forms is uniform on the image of its coefficient matrix. Hence its joint entropy in bits is exactly the row rank over \(\mathbb F_2\). Representing the form at time \(k\) by a polynomial, \(B_p(T^kx)\) has coefficient polynomial \(s^kp(s)\). Different finite shifts \(s^kp(s)\) of a fixed nonzero polynomial are linearly independent: a finite relation would give \(a(s)p(s)=0\) in the integral domain \(\mathbb F_2[s]\), hence \(a=0\).

**Protocol \(U\).** Put \(z=s^2\). The module \(\mathbb F_2[s]\) is free over \(\mathbb F_2[z]\) with basis \(1,s\). The coefficient polynomials of the even outputs are \(z^kp(s)\); those of the odd outputs are \(z^k s q(s)\). Thus the two generators, in basis coordinates, are
\[
(p_e,p_o),\qquad (zq_o,q_e).
\]
Their determinant in characteristic two is exactly \(\Delta=p_e q_e+z p_o q_o\). If \(\Delta\ne0\), the two generators are independent over the fraction field \(\mathbb F_2(z)\). Consequently all polynomial translates of the two generators are \(\mathbb F_2\)-independent, proving the exact \(2N\)-bit entropy statement for every block.

If \(\Delta=0\), the generators are dependent over \(\mathbb F_2(z)\). Clearing denominators gives nonzero polynomials \(a(z),b(z)\) with \(a(z)p(s)+b(z)sq(s)=0\). Necessarily both are nonzero, because \(p,q\ne0\). Let \(d=\max(\deg a,\deg b)\). For \(N>d\), multiplying this identity by \(z^k\), \(0\le k<N-d\), gives \(N-d\) independent linear relations among the first \(2N\) output coefficient polynomials. Their independence follows because distinct polynomial multiples of the nonzero relation pair \((a,b)\) are independent. The first \(N\) even rows remain independent, so
\[
N\le H_2(U_0,\ldots,U_{2N-1})\le N+d.
\]
This proves rate \(1/2\). Finally \(p(s)q(s)\) has even-power part \(p_e q_e+z p_o q_o=\Delta\). Therefore \(\Delta=0\) exactly when the product has only odd powers; over \(\mathbb F_2\) this means it equals \(s r(s)^2\).

**Protocol \(V\).** The first \(2N\) coefficient polynomials are \(s^kp(s),s^kq(s)\) for \(0\le k<N\). The \(N\) translates of \(p\) are independent. The two generators are always dependent over \(\mathbb F_2(s)\), and the explicit relation
\[
\frac{q(s)}{g(s)}p(s)+\frac{p(s)}{g(s)}q(s)=0,\qquad g=\gcd(p,q),
\]
has polynomial coefficients. Its \(N-O_{p,q}(1)\) independent shifts lie within the first block of output rows. Hence the rank lies between \(N\) and \(N+O_{p,q}(1)\), establishing the universal half-rate.

**Sharp pairwise-independence witnesses.** For the second protocol choose \(p=1+s\), \(q=1+s^2\), and put \(E_k=\xi_k\oplus\xi_{k+1}\). The variables \(E_k\) are independent fair bits by the nonzero-shift argument. Directly, \(V_{2k}=E_k\) and \(V_{2k+1}=E_k\oplus E_{k+1}\). Every two distinct output coordinate forms are unequal and nonzero, hence are independent fair bits. A block of \(2N\) outputs contains exactly the information in \(E_0,\ldots,E_N\), so its entropy is \(N+1\); the stated XOR relation is deterministic. For the first protocol choose \(p=1+s\), \(q=s+s^2+s^3+s^4\), and \(E_k=\xi_{2k}\oplus\xi_{2k+1}\). Again the \(E_k\) are independent fair bits, and now \(U_{2k}=E_k\), \(U_{2k+1}=E_{k+1}\oplus E_{k+2}\). Distinct output forms are nonzero and unequal. The first \(2N\) outputs determine precisely \(E_0,\ldots,E_{N+1}\) when \(N\ge2\), giving entropy \(N+2\) and the asserted three-coordinate relation. This completes the proof.

## Verification

The attached standalone Python checker uses integer bitsets for \(\mathbb F_2\)-polynomials and exact Gaussian elimination for ranks. It tests all \(31^2=961\) ordered pairs of nonzero polynomials of degree at most four at block sizes \(2N\) for \(N=3,6,12\), verifies the determinant/odd-product criterion, and checks both pairwise-independent examples and their exact finite-block ranks through \(N=19\). Its result is `PASS: 961 nonzero pairs checked at three block lengths; full= 889 half= 72 ; exact example blocks N=1..19`. These are finite consistency checks only; the unbounded claims are proved by the polynomial-module argument above.

## Relationship to prior work

Tsuneda (2024) formulates the two alternation protocols and derives their autocorrelation functions (its equations (13)–(22)). The entropy rates and the polynomial criterion here are not consequences of pairwise-correlation data alone. Tsuneda (2019) studies individual Bernoulli-map Walsh sensors and establishes independent streams and their pairwise orthogonality, whereas this finding classifies the entropy of an interlaced stream. Tsuneda (2021) studies autocorrelations of multi-bit outputs formed from several chaotic binary streams, not this full parity-filter entropy classification. The proof uses standard binary polynomial algebra; possible equivalence to a general polyphase-filter rank theorem is a residual publication-priority risk.

## Limitations

This is an exact statement for Lebesgue-typical binary coding and **finite parity sensors**. It does not classify nonlinear Boolean sensors, biased input measures, finite-word implementations, or security properties. The universal half-rate for the second protocol is in part an information-capacity restriction; the additional content is sharp achievability for every nonzero parity sensor and the explicit pairwise-independent degeneracies. The originality comparison is limited to inspected primary sources and relevant indexed descriptions; no claim of exhaustive priority or independent verification is made.

## References

1. A. Tsuneda, "Auto-Correlation Functions of Chaotic Binary Sequences Obtained by Alternating Two Binary Functions," *Dynamics* **4** (2024), 272–286, https://doi.org/10.3390/dynamics4020016 (first public date verified: 2024-04-16).
2. A. Tsuneda, "Orthogonal Chaotic Binary Sequences Based on Bernoulli Map and Walsh Functions," *Entropy* **21** (2019), 930, https://doi.org/10.3390/e21100930.
3. A. Tsuneda, "Various Auto-Correlation Functions of m-Bit Random Numbers Generated from Chaotic Binary Sequences," *Entropy* **23** (2021), 1295, https://doi.org/10.3390/e23101295.
