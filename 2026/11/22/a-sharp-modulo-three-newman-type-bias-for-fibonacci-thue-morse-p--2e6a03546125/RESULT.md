# A sharp modulo-three Newman-type bias for Fibonacci–Thue–Morse parity

## Finding

Let \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). Every nonnegative integer has a unique Zeckendorf expansion
\[
n=\sum_{j\ge1}\varepsilon_jF_{j+1},\qquad \varepsilon_j\in\{0,1\},\quad\varepsilon_j\varepsilon_{j+1}=0.
\]
Write \(s_F(n)=\sum_j\varepsilon_j\). For integers \(L\ge0\) and \(r\in\{0,1,2\}\), define the signed residue imbalance
\[
D_L(r)=\sum_{\substack{0\le n<F_{L+2}\\n\equiv r\pmod3}}(-1)^{s_F(n)}.
\]
Thus \(D_L(r)\) is exactly the number of integers with an even number of Zeckendorf summands minus the number with an odd number, restricted to residue \(r\pmod3\) and the Fibonacci cutoff \(F_{L+2}\).

Set \(q_0=3\), \(q_1=23\), and \(q_{t+2}=8q_{t+1}-q_t\) for every \(t\ge0\). Define \(b_t=0,-1,1\) according as \(t\equiv0,1,2\pmod3\). Then, **for every integer \(t\ge0\)**,
\[
\boxed{D_{8t+7}(0)=\frac{2q_t+b_t}{3},\qquad
D_{8t+7}(1)=D_{8t+7}(2)=\frac{b_t-q_t}{3}.}
\]
In particular, the even-Zeckendorf-weight count strictly exceeds the odd-weight count for multiples of three, whereas the opposite inequality holds in both other residue classes, at every indicated cutoff. Their total signed imbalance is just \(b_t\in\{-1,0,1\}\).

Let \(\lambda=4+\sqrt{15}\), \(\varphi=(1+\sqrt5)/2\), and
\[
\alpha=\frac{11+3\sqrt{15}}{2\sqrt{15}},\qquad
\beta=\frac{\log(4+\sqrt{15})}{8\log\varphi}=0.5360001982\ldots.
\]
Then \(q_t=\alpha\lambda^t+(3-\alpha)\lambda^{-t}\), whence
\[
D_{8t+7}(0)=\frac{2\alpha}{3}\lambda^t+O(1),\qquad
D_{8t+7}(1)=D_{8t+7}(2)=-\frac{\alpha}{3}\lambda^t+O(1).
\]
For each \(r\in\{0,1,2\}\) and every integer \(L\ge0\), \(D_L(r)=O(F_{L+2}^{\beta})\), with an implied constant independent of \(L\) and \(r\). The exponent \(\beta\) is optimal on the Fibonacci-cutoff family, already for residue zero along \(L=8t+7\). The result asserts no uniform optimal discrepancy exponent for arbitrary non-Fibonacci cutoffs.

## Assumptions and scope

Indices are nonnegative integers; all sums and signs are over exact ordinary integers. The cutoff is the half-open interval \([0,F_{L+2})\), not \([0,F_{L+2}]\). For a length-\(L\) digit word, position \(j\in\{1,\dots,L\}\) has weight \(F_{j+1}\), and adjacent occupied positions are forbidden. Every such word corresponds bijectively to exactly one index in \([0,F_{L+2})\): this is the canonical Zeckendorf representation, and the greatest represented index is \(F_{L+2}-1\). The claim is about the parity of the *number* of summands, not the parity of the Fibonacci summand indices and not the ordinary binary digit sum.

## Proof

Let \(\omega=e^{2\pi i/3}\), so \(\omega^2+\omega+1=0\). In the ring \(\mathbb Z[z]/(z^3-1)\), use the signed finite-word polynomial
\[
Q_L(z)=\sum_{\substack{\varepsilon\in\{0,1\}^{L}\\\varepsilon_j\varepsilon_{j+1}=0}}
(-1)^{\sum_j\varepsilon_j}z^{\sum_j\varepsilon_jF_{j+1}}.
\]
A last-digit decomposition yields \(Q_{-1}(z)=Q_0(z)=1\) and
\[
Q_L(z)=Q_{L-1}(z)-z^{F_{L+1}}Q_{L-2}(z),\qquad L\ge1.
\]
By the Zeckendorf bijection, the coefficient of \(z^r\) after reduction modulo \(z^3-1\) is \(D_L(r)\).

**Exact cubic-root transfer.** Set
\[
T_j=\begin{pmatrix}1&-\omega^{F_{j+1}}\\1&0\end{pmatrix}.
\]
Then \((Q_j(\omega),Q_{j-1}(\omega))^{\mathsf T}=T_j(Q_{j-1}(\omega),Q_{j-2}(\omega))^{\mathsf T}\). The residues \(F_{j+1}\pmod3\) have period eight; during one period they are \(1,2,0,2,2,1,0,1\). Direct multiplication in \(\mathbb Z[\omega]\), using only \(\omega^2=-1-\omega\), gives
\[
M=T_8T_7\cdots T_1=
\begin{pmatrix}8+\omega&-1-3\omega\\3+\omega&-\omega\end{pmatrix},
\qquad\operatorname{tr}M=8,\quad\det M=1.
\]
Thus \(M^2-8M+I=0\). Since the eight transfer matrices repeat, their products over successive eight-step blocks are identical. Every sequence \(Q_{8t+j}(\omega)\) at a fixed phase \(j\in\{0,\dots,7\}\) consequently obeys the recurrence with characteristic polynomial \(X^2-8X+1\). At phase seven, direct application of the displayed recurrence gives \(Q_7(\omega)=3\) and \(Q_{15}(\omega)=23\). Hence
\[
Q_{8t+7}(\omega)=q_t\in\mathbb Z,
\]
where \(q_t\) is exactly the integer sequence in the finding. Its characteristic roots are \(4\pm\sqrt{15}\), proving the closed form and \(q_t\ge3\) for all \(t\ge0\).

**Root-one cancellation.** At \(z=1\), the same recurrence reads \(Q_L(1)=Q_{L-1}(1)-Q_{L-2}(1)\), with initial values \(Q_0(1)=1\), \(Q_1(1)=0\). Hence \(Q_L(1)\), as \(L\) advances through nonnegative integers, repeats \(1,0,-1,-1,0,1\) with period six. Since \(8t+7\equiv2t+1\pmod6\), \(Q_{8t+7}(1)=b_t\).

**Fourier inversion.** The three residue coefficients are real integers and satisfy
\[
D_L(r)=\frac13\bigl(Q_L(1)+\omega^{-r}Q_L(\omega)
+\omega^{-2r}Q_L(\omega^2)\bigr).
\]
At phase \(8t+7\), both \(Q_L(\omega)\) and its conjugate \(Q_L(\omega^2)\) equal the real number \(q_t\). Because \(\omega+\omega^2=-1\), the two displayed exact residue formulas follow. Since \(q_t\ge3\) and \(|b_t|\le1\), the claimed strict signs follow for every \(t\ge0\).

**Optimal exponent on Fibonacci cutoffs.** The eigenvalues of \(M\) are \(\lambda\) and \(\lambda^{-1}\), distinct and real. Any \(L=8t+j\), \(0\le j<8\), has transfer product consisting of \(M^t\) followed by at most seven fixed matrices. Therefore \(|Q_L(\omega)|=O(\lambda^t)\), uniformly over all phases \(j\). The root-one values are bounded by one, so Fourier inversion yields \(|D_L(r)|=O(\lambda^{L/8})\). Binet's Fibonacci formula gives \(F_{L+2}=\Theta(\varphi^L)\), proving \(D_L(r)=O(F_{L+2}^{\beta})\). At \(L=8t+7\), the coefficient \(2\alpha/3\) is strictly positive, proving the exponent cannot be decreased along Fibonacci cutoffs. This completes the proof.

## Verification

The standalone \(\texttt{verify.py}\) uses exact arithmetic in \(\mathbb Z[\omega]\) to reconstruct the transfer matrix, its trace and determinant, and its Cayley–Hamilton identity; it checks recurrence values at many phases. Independently, a three-residue signed-digit dynamic program is compared with direct greedy Zeckendorf enumeration for \(0\le L\le19\). Additional dynamic-program comparisons test every residue formula on lengths up to \(L=91\). A successful execution reports \(29{,}575\) finite exact comparisons. These tests check transcription and finite boundary cases; the general theorem follows from the symbolic proof above, not from finite testing.

Run with a standard Python 3 interpreter: \(\texttt{python3 verify.py}\). No external Python packages, datasets or network services are needed.

## Relationship to prior work

The Fibonacci–Thue–Morse parity word is classical; see Ferrand (2007), OEIS A095076, and Shallit (2022). Shallit proves complexity statements for this same word, not the exact three-progression signed sums above. Drmota, Müllner and Spiegelhofer (2017) treat Möbius orthogonality rather than a sharp congruence-conditioned exponent. Drmota and Steiner (2002) investigate Zeckendorf digit sums on polynomial subsequences with central limit laws; their main distribution theorems do not specify these exact signed frequencies. Popoli and Stipulanti (2024) give pseudorandomness/correlation properties of related morphic sequences rather than the present root-of-unity eight-step transfer calculation. The 1969 Newman phenomenon and its extensions concern the *binary* Thue–Morse digit sum, which has different numeration weights and therefore does not imply this Fibonacci analogue. Exact residue-class comparison is essential: cancellation without conditioning and a sublinear error bound by themselves do not yield the formulas or sharp exponent here.

## Limitations

The exact closed residue formulas are established at the specified phase \(L\equiv7\pmod8\); an exponent upper bound is proved at all Fibonacci cutoffs. No analogous all-cutoff exact formulas or estimates for other moduli are asserted. The evidence of priority is limited to the identified and inspected literature; an equivalent in an unindexed source is not ruled out. The result has not received independent mathematical review.

## References

1. Jeffrey Shallit, *Note on a Fibonacci Parity Sequence*, initial arXiv publication 20 March 2022, https://arxiv.org/abs/2203.10504.
2. Emmanuel Ferrand, *An analogue of the Thue–Morse sequence*, Electronic Journal of Combinatorics 14 (2007), R30, https://doi.org/10.37236/948.
3. Michael Drmota, Clemens Müllner, Lukas Spiegelhofer, *Möbius orthogonality for the Zeckendorf sum-of-digits function*, arXiv:1706.09680, https://arxiv.org/abs/1706.09680.
4. Michael Drmota, Wolfgang Steiner, *The Zeckendorf expansion of polynomial sequences*, Journal de Théorie des Nombres de Bordeaux 14 (2002), 439–475, https://www.numdam.org/item/JTNB_2002__14_2_439_0/.
5. Pierre Popoli, Manon Stipulanti, *On the pseudorandomness of Parry–Bertrand automatic sequences*, initial arXiv publication 26 August 2024, https://arxiv.org/abs/2408.14059.
6. OEIS Foundation, A095076, *Parity of 1-fibits in Zeckendorf expansion*, https://oeis.org/A095076.
7. Donald J. Newman, *On the number of binary digits in a multiple of three*, Proceedings of the American Mathematical Society 21 (1969), 719–721, https://doi.org/10.2307/2036455.
