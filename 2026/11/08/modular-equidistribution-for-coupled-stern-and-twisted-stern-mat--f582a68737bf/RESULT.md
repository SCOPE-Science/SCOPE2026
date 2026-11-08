# Modular equidistribution for coupled Stern and twisted-Stern matrices

## Finding
Let the Stern and twisted Stern sequences satisfy \(s(0)=t(0)=0\), \(s(1)=t(1)=1\), and, for every integer \(n\ge1\),
\[
s(2n)=s(n),\quad s(2n+1)=s(n)+s(n+1),
\]
\[
t(2n)=-t(n),\quad t(2n+1)=-t(n)-t(n+1).
\]
Set
\[
M_n=\begin{pmatrix}s(n)&s(n+1)\\t(n)&t(n+1)\end{pmatrix},\qquad
J=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
B_n=J^{\lfloor\log_2n\rfloor}M_n.
\]

**Theorem.** Fix any odd integer \(m\ge3\). Put
\[
G_m=m^3\prod_{p\mid m}(1-p^{-2}),\qquad
P_m=m^2\prod_{p\mid m}(1-p^{-2}).
\]
For every matrix \(A\) over \(\mathbb Z/m\mathbb Z\), the natural density of positive integers \(n\) with \(B_n\equiv A\pmod m\) exists and is
\[
\begin{cases}
G_m^{-1},&\det A\equiv-2\pmod m,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, for each pair \((a,b)\bmod m\), the natural density of \(n\ge1\) satisfying \((s(n),t(n))\equiv(a,b)\pmod m\) is
\[
\begin{cases}
P_m^{-1},&\gcd(a,b,m)=1,\\
0,&\gcd(a,b,m)>1.
\end{cases}
\]
For the unnormalized matrices \(M_n\), each \(A\) whose determinant is \(2\) or \(-2\) modulo \(m\) has lower and upper asymptotic frequencies respectively \(1/(3G_m)\) and \(2/(3G_m)\). Thus individual admissible raw matrices do not have natural densities, even though the normalized matrices and raw first-column pairs do.

## Assumptions and scope
All congruences are entrywise modulo a fixed odd integer \(m\ge3\). A primitive residue pair means one satisfying \(\gcd(a,b,m)=1\) for any integer representatives. A natural density is the limit of a counting function divided by \(N\), as \(N\to\infty\). Lower and upper asymptotic frequencies are the corresponding liminf and limsup. The theorem makes no claim for even moduli: the determinant is then not necessarily invertible.

## Proof
**1. An exact binary matrix recurrence.** Set
\[
U=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
V=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad
M_1=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]
The defining recurrences give, for every \(n\ge1\),
\[
M_{2n}=JM_nU,\qquad M_{2n+1}=JM_nV.
\]
Writing the binary digits of \(n\ge1\) as a leading \(1\) followed by \(r\) digits \(\epsilon_1,\ldots,\epsilon_r\), induction yields
\[
M_n=J^rM_1W_{\epsilon_1}\cdots W_{\epsilon_r},\qquad
B_n=M_1W_{\epsilon_1}\cdots W_{\epsilon_r},
\]
where \(W_0=U\) and \(W_1=V\). Hence \(\det M_n=-2(-1)^r\) (the determinant identity itself is due to Bacher) and \(\det B_n=-2\).

**2. Finite-group generation and aperiodicity.** Over \(R=\mathbb Z/m\mathbb Z\), the two elementary unipotent matrices \(U,V\) generate \(\operatorname{SL}_2(R)\). Indeed, for a local ring \(\mathbb Z/p^k\mathbb Z\), one entry of any unimodular first column is a unit; elementary row operations reduce the column to a standard basis vector, the permutation matrix \(UV^{-1}U\) swaps the entries up to sign, and elementary operations also generate every diagonal matrix of determinant one. The Chinese remainder theorem gives the assertion for \(R\). Positive products suffice because \(U^m=V^m=I\).

The right random walk with equal choices of \(U,V\) is irreducible on the finite group \(H=\operatorname{SL}_2(R)\). It is aperiodic when \(m\) is odd: the identity has a return word \(U^m\) of length \(m\) and a return word \((UV^{m-1}U)^4\) of length \(4(m+1)\), because \(UV^{-1}U\) has order four. Their lengths have greatest common divisor \(\gcd(m,4(m+1))=1\). Each transition is a permutation, so uniform counting measure on \(H\) is stationary. Finite irreducible aperiodic Markov-chain theory therefore provides constants \(C_m>0\), \(0<\rho_m<1\) such that, uniformly over starting states and target states,
\[
\left|\Pr(W_{\epsilon_1}\cdots W_{\epsilon_h}=g)-|H|^{-1}\right|
\le C_m\rho_m^h.
\]
The exact group order is
\[
|H|=m^3\prod_{p\mid m}(1-p^{-2})=G_m,
\]
by counting the primitive first columns and the \(m\) compatible second columns.

**3. From binary blocks to natural density.** In the complete block \(2^r\le n<2^{r+1}\), every binary suffix of length \(r\) occurs once. The preceding estimate gives, for each matrix \(A\) of determinant \(-2\),
\[
\#\{2^r\le n<2^{r+1}:B_n\equiv A\}
=2^r/G_m+O_m(2^r\rho_m^r).
\]
Other matrices never occur. For an arbitrary initial segment of the same block, the binary suffixes form a lexicographic interval. Partition it into at most one complete binary cylinder of each remaining suffix length \(h\), \(0\le h<r\). The same Markov bound, uniform from any prefixed state, gives a total discrepancy bounded by
\[
O_m\left(\sum_{h=0}^{r-1}(2\rho_m)^h\right)=o_m(2^r).
\]
The discrepancy from all earlier complete blocks is also \(o_m(2^r)\). Hence for every \(A\) of determinant \(-2\),
\[
\#\{1\le n\le N:B_n\equiv A\}=N/G_m+o_m(N).
\]
This proves the normalized matrix statement.

**4. Primitive joint residues and the unnormalized oscillation.** Since \(m\) is odd, \(-2\) is a unit in \(R\). A first column \((a,b)\) can occur in a determinant-\(-2\) matrix exactly when it is primitive. Such a column has precisely \(m\) compatible second columns, since a primitive pair can be completed to a basis and the determinant functional on the second column is surjective with kernel size \(m\). Thus the normalized first columns have frequency \(m/G_m=1/P_m\). On each binary block the unnormalized first column of \(M_n\) is obtained by changing the sign of the second coordinate when \(r\) is odd. This permutation of primitive columns preserves the same uniform count; the uniform prefix estimate proves the asserted natural density for \((s(n),t(n))\) without normalization.

For a specified raw matrix \(A\) with determinant \(-2\), the counts on blocks of even depth \(r\) are \(2^r/G_m+o_m(2^r)\); on odd-depth blocks the counts are exactly zero. The roles reverse when \(\det A\equiv2\). Along the endpoints \(N=2^{2k}\) and \(N=2^{2k+1}\), the frequencies therefore tend to \(1/(3G_m)\) and \(2/(3G_m)\) in one order or the other. The uniform \(o_m(2^r)\) prefix estimate shows that no intermediate position in a binary block can have a larger limiting limsup or smaller liminf: the limiting frequency within an active block interpolates monotonically toward \(1/G_m\), and within an inactive block decreases monotonically. Both endpoint bounds are attained, establishing the claimed liminf and limsup.

## Verification
Run the standalone exact-integer script `verify.py` under Python 3. It checks the binary recurrences and determinant identities, independently enumerates the \(U,V\) Cayley graph for the moduli \(3,5,7,9,11,15\), and compares normalized matrix supports and primitive-pair supports on complete binary blocks through depth \(16\). The script also checks that binary-word matrix products agree with direct sequence evaluation. The output includes coverage and discrepancy statistics; finite discrepancies, especially for modulus \(15\), are expected and are not asserted to vanish at any finite depth. The unrestricted proof uses finite-group mixing, not experimental extrapolation.

## Relationship to prior work
Bacher (2010) introduced the twisted Stern sequence, its coupled matrix, and the alternating determinant identity; those are not new here. Coons (2010) and Allouche (2012) established further identities and generating-function properties for the same sequences. Deshouillers and Schinzel (2019) proved uniform primitive-pair distribution of the *adjacent ordinary Stern values* \((s(n),s(n+1))\) modulo arbitrary moduli, and provided an automata argument. Their stated distribution does not give the joint pair \((s(n),t(n))\) or the entire normalized coupled matrix distribution. The general finite-state mixing method is classical; the contribution is the precise coupled modular distribution, its determinant normalization, and the explicit oscillation of raw matrix frequencies.

## Limitations
Only odd moduli are asserted; no result is claimed for arbitrary even moduli. The convergence constants depend on the modulus, with no uniform quantitative rate in growing moduli. No priority claim is made against literature not located by the documented searches. In particular, the general automata framework of Deshouillers and Schinzel may offer an alternative derivation after constructing and analyzing a suitable augmented automaton. No independent mathematical audit is claimed.

## References
- R. Bacher, *Twisting the Stern sequence*, arXiv:1005.5627v1 (first released 2010-05-31), https://arxiv.org/pdf/1005.5627.
- M. Coons, *On some conjectures concerning Stern's sequence and its twist*, arXiv:1008.0193 (2010), https://arxiv.org/pdf/1008.0193.
- J.-P. Allouche, *On the Stern sequence and its twisted version*, arXiv:1202.4171 (2012), https://arxiv.org/abs/1202.4171.
- J.-M. Deshouillers and A. Schinzel, *The modular distribution of Stern's sequence*, Banach Center Publications 118 (2019), doi:10.4064/bc118-3, https://impan.pl/shop/en/publication/transaction/download/product/113097.
