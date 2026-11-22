# Lucas-law Walsh inertia of circular descent profiles

## Finding
For each integer \(n\geq3\), write \(S_n\) for the permutations of \([n]\) and define the *circular descent-position vector* \(d(\pi)\in\{0,1\}^{n}\) by
\[
d_i(\pi)={\bf1}\{\pi(i)>\pi(i+1)\},\qquad \pi(n+1)=\pi(1).
\]
The integer kernel \(a_n(x)=\#\{\pi\in S_n:d(\pi)=x\}\), on the Boolean group \(G_n=(\mathbb Z/2\mathbb Z)^n\), defines counting convolution \((T_nf)(x)=\sum_{y\in G_n}a_n(y)f(x\oplus y)\). For the Walsh character \(\chi_U(x)=(-1)^{\sum_{i\in U}x_i}\), let \(\lambda_n(U)=\sum_{\pi\in S_n}\chi_U(d(\pi))\).

**Theorem (complete Fourier support, signs and inertia).** The following hold simultaneously for every \(n\geq3\).

1. If \(U\subsetneq[n]\), decompose its marked positions on the cyclic index set into maximal nonempty circular intervals of lengths \(r_1,\ldots,r_b\). Let \(A_m(t)=\sum_{\sigma\in S_m}t^{\operatorname{des}(\sigma)}\) be the ordinary Eulerian polynomial. Then
\[
\lambda_n(U)=n!\prod_{j=1}^{b}\frac{A_{r_j+1}(-1)}{(r_j+1)!}.
\]
For \(U=\varnothing\), the empty product is \(1\). For the full character \(U=[n]\),
\[
\lambda_n([n])=-nA_{n-1}(-1).
\]
2. A proper \(U\) has a nonzero multiplier exactly when *every* circular marked run has even length. The full set has nonzero multiplier exactly when \(n\) is even. In every nonzero case \(|U|\) is even and
\[
\operatorname{sgn}\lambda_n(U)=(-1)^{|U|/2}.
\]
Thus the nonzero Walsh support is exactly the family of vertex subsets covered by a matching of the cyclic graph \(C_n\); the full set, when \(n\) is even, is covered by two distinct perfect matchings but is only one Walsh frequency.
3. Let \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\), \(L_n=F_{n-1}+F_{n+1}\), and \(\varepsilon_n={\bf1}\{2\mid n\}\). Define the integer six-periodic quantity \(q_n\) by \((q_0,q_1,q_2,q_3,q_4,q_5)=(2,1,-1,-2,-1,1)\), and set \(h_n=(-1)^{n/2}\) at even \(n\) and \(h_n=0\) at odd \(n\). The numbers of positive, negative and zero eigenvalues, including Walsh multiplicity, are precisely
\[
\begin{aligned}
N_+(T_n)&=\frac{L_n-\varepsilon_n+q_n-h_n}2,\\
N_-(T_n)&=\frac{L_n-\varepsilon_n-q_n+h_n}2,\\
N_0(T_n)&=2^n-L_n+\varepsilon_n.
\end{aligned}
\]
Hence the exact rank is \(L_n-\varepsilon_n\), and the recoverable Fourier fraction is asymptotic to \((\varphi/2)^n\), with \(\varphi=(1+\sqrt5)/2\).

## Assumptions and scope
All permutations have equal weight \(1\), coordinate positions on the circle are labelled, and the convolution is **unnormalized**. No claim concerns the distinct construction that records descent *values*, or the descent sets of permutations constrained to consist of one cycle in cycle notation. The result classifies every Walsh eigenvalue's vanishing and sign, and exactly counts each sign and the nullity. It does not claim the minimum nonzero multiplier magnitude or an endpoint-norm projection constant.

## Proof
**Local signed Eulerian factor.** Let \(U\neq[n]\). Cutting the circular index set immediately after any unmarked index produces disjoint runs of marked comparison edges. A run of \(r\) consecutive comparison edges involves \(r+1\) consecutive vertex positions; distinct runs involve disjoint position blocks even when separated by only one unmarked edge. For a uniformly random \(\pi\in S_n\), the relative orders of its values restricted to these disjoint position blocks are independent, and the relative order on a block of size \(r+1\) is uniform on \(S_{r+1}\). The expected signed descent weight on such a block is \(A_{r+1}(-1)/(r+1)!\). Multiplication of these independent expectations, followed by multiplication by \(n!\), proves the proper-set formula.

**Nonvanishing and sign of local factors.** The classical Eulerian exponential generating function, with \(A_0(t)=1\), specializes to
\[
\sum_{m\ge0}\frac{A_m(-1)}{m!}z^m=\frac{2}{1+e^{-2z}}=1+\tanh z.
\]
The even-degree coefficients other than the constant are zero. The odd-degree coefficient of degree \(2r+1\) is \((-1)^r E_{2r+1}/(2r+1)!\), where \(E_{2r+1}>0\) is the number of alternating permutations of length \(2r+1\); equivalently \(\tan z=\sum_{r\ge0}E_{2r+1}z^{2r+1}/(2r+1)!\). Thus \(A_m(-1)=0\) exactly for even positive \(m\), and \(A_{2r+1}(-1)=(-1)^rE_{2r+1}\). The proper-set statement follows, with product sign \((-1)^{(r_1+\cdots+r_b)/2}=(-1)^{|U|/2}\).

**Closed circular factor.** Rotate every one-line permutation so that its largest entry occurs at position \(n\). Its circular descents then consist of the single wrap-around descent from position \(n\), together with the ordinary descents of the first \(n-1\) entries. Every relative order of those entries gives exactly \(n\) circular rotations. Therefore \(\sum_{\pi\in S_n}t^{\operatorname{cdes}(\pi)}=ntA_{n-1}(t)\). Setting \(t=-1\) proves \(\lambda_n([n])=-nA_{n-1}(-1)\), nonzero precisely for even \(n\), with sign \((-1)^{n/2}\).

**Matching correspondence.** On the index cycle \(C_n\), a matching covers each of its vertices in disjoint adjacent pairs. If its covered set is proper, its maximal cyclic covered runs all have even length, and conversely each proper even-run set admits exactly one matching: beginning at each run endpoint, its vertices must be paired successively. If the covered set is the entire vertex cycle, it is possible only at even \(n\), and exactly two perfect matchings cover it. Consequently the nonzero Walsh frequencies correspond to matchings with only this one two-to-one collision.

Write \(M_n(t)=\sum_{r=0}^{\lfloor n/2\rfloor}m_{n,r}t^r\) for the matching generating polynomial of \(C_n\), where \(m_{n,r}\) counts its \(r\)-edge matchings. Choose binary edge indicators \(z_i\in\{0,1\}\) for a matching, requiring \(z_i z_{i+1}=0\) cyclically. The two-state matrix \(B(t)=\begin{pmatrix}1&t\\1&0\end{pmatrix}\) has entries \(B(t)_{a,b}=t^b\mathbf1\{ab=0\}\), so \(M_n(t)=\operatorname{tr}(B(t)^n)\). The characteristic equation is \(x^2-x-t=0\); if its roots are \(\alpha(t),\beta(t)\), then \(M_n(t)=\alpha(t)^n+\beta(t)^n\), with \(\alpha+\beta=1\) and \(\alpha\beta=-t\). Thus \(M_n(1)=L_n\) and \(M_n(-1)=2\cos(n\pi/3)=q_n\). The unique-mask generating polynomial is
\[
R_n(t)=M_n(t)-\varepsilon_nt^{n/2}.
\]
The coefficient of \(t^r\) counts nonzero Walsh frequencies of cardinality \(2r\), all of which have sign \((-1)^r\). Hence \(R_n(1)=N_++N_-\), \(R_n(-1)=N_+-N_-\), and \(N_0=2^n-R_n(1)\). Substituting the preceding evaluations gives the three displayed inertia formulas. Finally, \(L_n=\varphi^n+(-\varphi^{-1})^n\), proving the asserted asymptotic.

## Verification
The accompanying self-contained Python 3 file `verification.py` independently enumerates all permutations for \(3\le n\le9\), builds their circular-descent histograms and computes each complete Walsh transform. It checks every multiplier against the exact Eulerian formula, matches the nonzero character support against separately enumerated cycle matchings, and verifies rank, sign and inertia. It additionally verifies the odd/even Eulerian evaluations for every index through \(40\). The actual run produced `PASS: 2081 exact assertions, full permutation/FWHT for n=3..9`. These finite checks are supplementary; the argument above proves the all-order statement.

## Relationship to prior work
Foata and Schützenberger give the classical Eulerian generating function and signed Eulerian evaluations (1970 monograph; arXiv edition 2005). Petersen's 2006 dissertation, Chapter 1, Section 1.5, gives the circular Eulerian polynomial relation \(ntA_{n-1}(t)\) and develops the cyclic descent algebra of the symmetric group; its group-algebra multiplication is not the Boolean XOR convolution considered here. Elizalde (arXiv 0906.2795, first posted 2009) studies *one-cycle permutations* and their ordinary descents rather than the circular descent-position vectors of unrestricted permutations. Chang, Ma and Yeh (arXiv 0806.0433, first posted 2008) classify circular descent **values**, a different coordinate statistic. The earlier linear-position Walsh result yields a Fibonacci rank and a proper-run local factor on a path; it does not settle the full circular character or the two-perfect-matching collision that gives the exact cyclic inertia. The newly assessed statement is the global Boolean Fourier support, the sign law, and the full three-way inertia, not these classical input identities.

## Limitations
This is an exact algebraic result about counting convolution, not a statement that every circular descent word occurs. The operators have zero eigenvalues in all the stated dimensions. There is no assertion of an optimal nonzero inverse norm, endpoint projection norm, or an independent priority/correctness certification. The comparison is bounded by accessible and indexed literature; an unindexed earlier multivariate signed circular-descent theorem could potentially cover some of the spectral conclusions. Independent audit has not been performed.

## References
- D. Foata and M.-P. Schützenberger, *Théorie Géométrique des Polynômes Eulériens*, Lecture Notes in Mathematics 138 (1970), authorized arXiv edition `math/0508232`, first posted 2005-08-15. https://arxiv.org/abs/math/0508232
- T. K. Petersen, *Descents, Peaks, and P-partitions*, PhD dissertation, Brandeis University (May 2006), Chapter 1 §1.5. https://people.brandeis.edu/~gessel/homepage/students/petersenthesis.pdf
- H. Chang, J. Ma, and Y.-N. Yeh, *Enumerations of Permutations by Circular Descent Sets*, arXiv `0806.0433`, first posted 2008-06-05. https://arxiv.org/abs/0806.0433
- S. Elizalde, *Descent Sets of Cyclic Permutations*, arXiv `0906.2795`, first posted 2009-06-15. https://arxiv.org/abs/0906.2795
