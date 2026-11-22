# The sharp two-tail-lag correlation energy for unitary Fourier modulations

## Finding

For every integer \(N\ge4\), every unitary \(N\)-by-\(N\) complex matrix \(U\), and every column \(u_j\), set
\[
\gamma_k(u_j)=\sum_{i=0}^{N-k-1}\overline{u_{ij}}u_{i+k,j},\qquad
S_N(U)=\sum_{j=0}^{N-1}\bigl(|\gamma_{N-2}(u_j)|^2+|\gamma_{N-1}(u_j)|^2\bigr).
\]
Then the exact optimum, independent of dimension, is
\[
\max_{U\in\mathrm U(N)}S_N(U)=\frac54.
\]
In contrast, the normalized inverse discrete Fourier transform \(V\) satisfies \(S_N(V)=5/N\), so \(V\) is optimal for this two-lag non-prefix objective exactly at \(N=4\). Each of the two lags separately has respective maximum \(1\) and \(1/2\), while the sharp joint maximum \(5/4\) incurs a strictly positive compatibility loss of \(1/4\).

**Complete equality classification.** After a permutation of columns, exactly four columns are supported on the four extreme rows, in the order \(0,1,N-2,N-1\). Multiplying those columns by arbitrary unit complex scalars, they can be written
\[
\frac12(1,a_j,b_j,a_jb_j)^{\mathsf T},\qquad 1\le j\le4,\quad |a_j|=|b_j|=1,
\]
with mutual orthogonality equivalent to
\[
(1+\overline{a_j}a_l)(1+\overline{b_j}b_l)=0\quad(j\ne l).
\]
Thus for each distinct pair, at least one of its two phase coordinates is antipodal. All remaining \(N-4\) columns are an arbitrary orthonormal basis on the interior rows \(2,\ldots,N-3\), with zero entries on the four extreme rows. A particular optimizer is the four-column Walsh block with \((a_j,b_j)=(1,1),(1,-1),(-1,1),(-1,-1)\), supplemented by an identity on interior coordinates.

## Assumptions and scope

Rows and columns are indexed from zero. The matrices are unitary, without flat-entry, Fourier-circulant, or phase-alphabet constraints. The selected set of positive aperiodic lags is exactly \(\{N-2,N-1\}\), not the prefix \(\{1,\ldots,r\}\). The restriction \(N\ge4\) ensures that the four extreme rows are distinct.

For the statistical consequence, let \(s_0,\ldots,s_{N-1}\) be independent complex symbols with \(\mathbb E s_i=0\), \(\mathbb E s_i^2=0\), \(\mathbb E|s_i|^2=1\), and \(\mathbb E|s_i|^4=\mu_4<2\), all sharing the same fourth moment. With \(y=Us\), define the one-sided expected squared aperiodic sidelobe \(\operatorname{ESL}_k(U)=\mathbb E|\gamma_k(y)|^2\). No assertion is made for \(\mu_4\ge2\), or for other lag sets.

## Proof

Fix a column \(u\) of \(U\) and put
\[
\begin{gathered}
p_0=|u_0|^2,\quad p_1=|u_1|^2,\quad p_2=|u_{N-2}|^2,\quad p_3=|u_{N-1}|^2,\\
A=p_0+p_3,\quad B=p_1+p_2,\quad s=A+B\le1,\\
z=\overline{u_0}u_{N-2},\quad w=\overline{u_1}u_{N-1}.
\end{gathered}
\]
The column contribution is \(q=|z+w|^2+p_0p_3\). An exact sum-of-nonnegative-terms identity is
\[
\begin{aligned}
\frac{s(7A+3B)}{16}-q
={}&2\bigl(|z||w|-\operatorname{Re}(z\overline w)\bigr)
+\bigl(\sqrt{p_0p_1}-\sqrt{p_2p_3}\bigr)^2\\
&+\frac{(p_0-p_3)^2}{4}+\frac{3(A-B)^2}{16}.
\end{aligned}

\]
To verify (1), first expand \(q=p_0p_2+p_1p_3+p_0p_3+2\operatorname{Re}(z\bar w)\). Then replace the cross term by \(2\sqrt{p_0p_1p_2p_3}\) plus the phase deficit, and expand the three displayed real squares. The resulting polynomial equality is checked independently by `checker.py` with rational arithmetic. The phase term is nonnegative by \(\operatorname{Re}(z\overline w)\le|z||w|\).

For column \(j\), augment the right-hand side of (1) by \((1-s_j)(7A_j+3B_j)/16\). Summing over all columns and using the four row-norm conditions from \(UU^*=I\) gives
\[
\sum_j A_j=\sum_j B_j=2,\qquad
\boxed{\frac54-S_N(U)=\sum_j\left[\frac{(1-s_j)(7A_j+3B_j)}{16}+\text{four nonnegative terms from (1)}\right]\ge0.}

\]
This establishes the global upper bound with no restriction on the other \(N-4\) rows. Equality in (2), for any column with \(s_j>0\), forces \(s_j=1\), \(A_j=B_j=1/2\), \(p_{0j}=p_{3j}=1/4\), and \(p_{1j}=p_{2j}=1/4\), together with \(z_j\overline{w_j}\in\mathbb R_{>0}\). Thus the four extreme entries are all nonzero with modulus \(1/2\), and their phase relation is \(u_{0j}u_{N-1,j}=u_{1j}u_{N-2,j}\). Since the squared norm of row zero is one, exactly four such columns exist. Orthogonality forces all other columns into the interior coordinate subspace. Removing each active column's first phase yields \((1,a_j,b_j,a_jb_j)/2\); their pairwise inner products give precisely the classification above. Conversely, those conditions yield a unitary direct sum, attain equality in every term of (2), and hence give \(S_N=5/4\).

For the normalized Fourier matrix, each column satisfies \(|\gamma_k(u_j)|=(N-k)/N\), hence \(S_N(V)=N((2/N)^2+(1/N)^2)=5/N\).

Finally, the fourth-moment expansion for a traceless aperiodic shift \(J_k\) and \(A=U^*J_kU\) gives
\[
\mathbb E|s^*As|^2=|\operatorname{tr}A|^2+\|A\|_F^2+(\mu_4-2)\sum_j|A_{jj}|^2,
\]
so \(\operatorname{ESL}_k(U)=(N-k)+(\mu_4-2)\sum_j|\gamma_k(u_j)|^2\). The two constant contributions sum to \(3\). Since \(\mu_4-2<0\), the sharp minimum is
\[
\min_U\bigl(\operatorname{ESL}_{N-2}(U)+\operatorname{ESL}_{N-1}(U)\bigr)
=3-(2-\mu_4)\frac54=\frac12+\frac54\mu_4.
\]
The Fourier benchmark is \(3-(2-\mu_4)5/N\). Their difference, Fourier minus optimum, equals \((2-\mu_4)(5/4-5/N)\), positive exactly when \(N>4\).

## Verification

`checker.py` (Python 3, standard library only) verifies the quartic polynomial identity exactly on a complete five-point grid in each of four real amplitude variables, which proves coefficientwise equality because the polynomial degree in each variable is at most four. It also constructs the four-column Walsh direct sum for \(4\le N\le24\), checks every column's rational orthonormality, confirms \(S_N=5/4\), and checks the exact Fourier benchmark \(5/N\). These finite checks are supplementary: the proof of the theorem for every \(N\) is (1)–(2), and the finite checks are not treated as an infinite certificate. To reproduce, run `python3 checker.py`.

## Relationship to prior work

Xiong, Liu, Liu, Jin and Zhang, *On the Optimality of OFDM for Aperiodic Ranging* (first posted October 2, 2026), derive the fourth-moment formula and solve the optimization at each single lag and over every positive **prefix** \(\{1,\ldots,r\}\); their Theorem 1, Proposition 1 and Appendices A, B, G, H and I were compared. Their single-lag optima give the two separate values \(1\) and \(1/2\), but do not determine their simultaneous tradeoff. Their prefix theorem does not directly apply to the two-tail, non-prefix set. Equation (2) and its complete equality characterization address that remaining comparison with a different extremizing unitary, which for \(N>4\) has four active columns rather than a flat full Fourier basis.

## Limitations

The result treats exactly the final two positive lags, with equal weights; it does not classify arbitrary lag subsets, weighted mixtures, or intermediate lag windows. It assumes unitary matrices and proper i.i.d. input symbols in the statistical interpretation. The original mathematical bound itself needs only unitarity. The equality family need not be unique under phase and column symmetries. Published coverage beyond the inspected sources, including unindexed equivalences, cannot be excluded by searches alone. No independently performed audit is claimed.

## References

1. Y. Xiong, F. Liu, Y.-F. Liu, S. Jin and J. Zhang, *On the Optimality of OFDM for Aperiodic Ranging*, arXiv:2610.02843, first public 2026-10-02. https://arxiv.org/abs/2610.02843. Especially Lemma 1, Theorem 1, Proposition 1 and Appendices A, B, G, H, I.
2. F. Liu et al., *CP-OFDM Achieves the Lowest Average Ranging Sidelobe under QAM/PSK Constellations*, prior unitary modulation and aperiodic full-energy result, referenced in item 1, section I-B.
