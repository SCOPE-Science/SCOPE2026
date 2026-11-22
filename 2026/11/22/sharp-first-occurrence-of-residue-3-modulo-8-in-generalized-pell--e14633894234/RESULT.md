# Sharp first occurrence of residue \(3\) modulo \(8\) in generalized Pell sequences

## Finding
For the impulse-initialized \(k\)-generalized Pell sequence, the *first* index whose value is congruent to \(3\) modulo \(8\) is completely determined. Write
\[
T(k)=\min\{n\ge1:P_n^{(k)}\equiv3\pmod8\},
\]
with \(T(k)=\infty\) if the set is empty. Then \(T(2)=\infty\), and
\[
(T(3),T(4),\ldots,T(13))=(11,10,12,13,24,17,15,16,18,19,35).
\]
For every \(k\ge14\), the sharp offsets are
\[
\begin{array}{c|rrrrrr}
k\bmod6&0&1&2&3&4&5\\\hline
T(k)-k&7&16&9&6&6&7
\end{array}.
\]
Thus the obstruction interval has a six-class stable phase, with genuine exceptional delays at \(k=3\), \(k=7\), and \(k=13\).

## Assumptions and scope
For every integer \(k\ge2\), set \(P_j^{(k)}=0\) for \(j\le0\), \(P_1^{(k)}=1\), and
\[
P_n^{(k)}=2P_{n-1}^{(k)}+\sum_{j=2}^{k}P_{n-j}^{(k)} \quad(n\ge2).
\]
The congruence modulus is exactly \(8\), and \(T(k)\) is the least *positive* index, not the period or an eventual occurrence index. The two-parameter statement is for all integer \(k\ge2\), without numerical upper bound. No assertion about prime or composite status of the recurrence terms is needed.

## Proof
**1. A two-term correction before the second feedback.** In the ring of formal integer power series define
\[
B(z)=1-3z+z^2,\quad A(z)=\frac{z(1-z)}{B(z)},\quad E(z)=\frac{z(1-z)}{B(z)^2}.
\]
Summing the recurrence gives the exact identity
\[
G_k(z):=\sum_{n\ge1}P_n^{(k)}z^n=\frac{z(1-z)}{B(z)+z^{k+1}}.
\]
Formal geometric expansion (no analytic convergence required) yields
\[
G_k(z)=A(z)-z^{k+1}E(z)+\frac{z^{2k+2}z(1-z)}{B(z)^3}\left(1+\frac{z^{k+1}}{B(z)}\right)^{-1}.
\]
The last summand has valuation \(2k+3\). Writing \(a_n=[z^n]A(z)\) and \(e_t=[z^t]E(z)\), with \(e_t=0\) when \(t<0\), we therefore have the **exact integer** identity
\[
P_n^{(k)}=a_n-e_{n-k-1}\qquad(1\le n\le2k+2).
\]
Here \(a_n=F_{2n-1}\), where \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\). Since the odd Fibonacci subsequence obeys \(a_{n+2}=3a_{n+1}-a_n\), its residues modulo \(8\) repeat with period six:
\[
(a_1,\ldots,a_6)\equiv(1,2,5,5,2,1)\pmod8.
\]
In particular \(a_n\not\equiv3\pmod8\) for every \(n\). So \(T(k)\ge k+2\) for all \(k\), except that the classical case has no occurrence at all.

**2. Compute the first correction, uniformly.** Put \(C(z)=1/B(z)=\sum_{t\ge0}c_tz^t\). Its coefficients satisfy \(c_0=1,c_1=3,c_t=3c_{t-1}-c_{t-2}\). Since \(E(z)=A(z)C(z)\), finite convolution shows
\[
(e_0,e_1,\ldots,e_{15})\equiv(0,1,5,3,1,2,6,1,7,1,1,4,4,1,1,7)\pmod8.
\]
These coefficients can also be obtained by dividing the polynomial \(z(1-z)\) by \(B(z)^2\) recursively. For \(1\le s\le16\), and whenever \(k+s\le2k+2\),
\[
P_{k+s}^{(k)}\equiv a_{k+s}-e_{s-1}\pmod8.
\]
The following rows record the complete sixteen-term residue lists for \(s=1,\ldots,16\). The row label is \(k\bmod6\):

| \(k\bmod6\) | Values at \(k+1,\ldots,k+16\) modulo \(8\) | First \(s\) with residue \(3\) |
|---|---|---:|
| 0 | 1,1,0,2,1,7,3,1,6,4,1,5,5,1,4,6 | 7 |
| 1 | 2,4,0,7,0,7,4,4,6,1,0,5,6,4,4,3 | 16 |
| 2 | 5,4,5,6,0,0,7,4,3,0,0,6,1,4,1,2 | 9 |
| 3 | 5,1,4,6,1,3,7,1,2,0,1,1,1,1,0,2 | 6 |
| 4 | 2,0,4,7,4,3,4,0,2,1,4,1,6,0,0,3 | 6 |
| 5 | 1,0,5,2,4,0,3,0,3,4,4,6,5,0,1,6 | 7 |

For all \(k\ge14\), \(k+16\le2k+2\), so these sixteen entries are **exactly** the required segment. The previous paragraph excludes all earlier indices through \(k+1\). Reading the first \(3\) in each row proves all six infinite families.

**3. Finite exceptional orders.** Directly iterate the stated recurrence modulo \(8\) for the eleven orders \(3\le k\le13\), stopping on the first residue \(3\). The resulting first indices, in increasing order of \(k\), are
\[
11,10,12,13,24,17,15,16,18,19,35.
\]
This is a bounded, exhaustive computation: every term from index one up to and including the listed first index is checked with integer modular arithmetic in `checker.py`. The recurrence and initialization uniquely determine each term, so this suffices as a finite proof. At \(k=2\), the eight-term repeating Pell residue cycle from indices \(0\) through \(7\) is \((0,1,2,5,4,5,6,1)\), returning to its starting state after eight steps and never containing \(3\). This completes the classification.

**4. Consequence for odd-exponent Wagstaff-type shapes.** If \(m\ge3\) is any odd integer, then \((2^m+1)/3\) is an integer and \(3(2^m+1)/3\equiv1\pmod8\). The inverse of \(3\) modulo \(8\) is \(3\), so the quotient is always congruent to \(3\) modulo \(8\). Every term before \(T(k)\) avoids that residue, proving the stated exclusion. It does not imply an equality at \(T(k)\), or any later index.

## Verification
The standalone Python 3 script `checker.py` uses only the standard library. Run `python3 checker.py`. It independently computes all \(k\)-Pell residues through the predicted first index for every \(2\le k\le2000\), checks all eleven finite exceptional orders, and reconstructs the six sixteen-entry rows from the convolution of \(A(z)\) and \(1/B(z)\). These tests are not substituted for the formal generating-series proof for unbounded \(k\); they check arithmetic and transcription. The finite exceptional orders have no omitted indices in the checker.

## Relationship to prior work
Kaggwa, *On Wagstaff primes in the \(k\)-Pell number sequence* (first public preprint October 31, 2026), proves that no \(k\)-Pell number is a Wagstaff prime. Its Proposition 3.1 excludes residue \(3\) modulo \(8\) through index \(k+1\), its Remark 3.1 notes that the classical Pell recurrence never attains the residue, and it observes without determining the least index that the residue occurs for every \(k\ge3\). The new conclusion is **only** the sharp least-index function \(T(k)\) for all \(k\) and its six-phase formula, not an improvement to the already-proved global Wagstaff-prime nonexistence theorem. The published modular period of the classical Pell sequence and broad Fibonacci periodicity are background, not claimed as new. Other \(k\)-Pell papers on common terms and exponential shapes do not in the inspected material supply this parameter-uniform first-index cutoff.

## Limitations
This is a sharp local congruence boundary, not a classification of the full modular period or complete residue image, nor a full Diophantine exclusion for arbitrary composite odd exponents. The infinite-family proof uses only the coefficient range before the second feedback correction and cannot be extrapolated unchanged to later indices. Finite checks through \(k=2000\) are corroboration, not exhaustive evidence for all \(k\). Novelty comparisons are conditional on accessible primary literature and indexed records; independent review remains outstanding.

## References
1. Prosper Kaggwa, *On Wagstaff primes in the \(k\)-Pell number sequence*, arXiv:2611.01170v1, publicly submitted 2026-10-31. https://arxiv.org/pdf/2611.01170
2. B. V. Normenyo, S. E. Rihane and A. Togbé, *Common terms of \(k\)-Pell numbers and Padovan or Perrin numbers*, *Arabian Journal of Mathematics*, published online 2022-11-28. https://link.springer.com/article/10.1007/s40065-022-00407-8
