# Exact sixth Fourier moments of finite middle-thirds Cantor spectra

## Finding

For each integer \(k\ge 0\), let
\[
A_k=\left\{\sum_{j=0}^{k-1}\varepsilon_j3^j:\varepsilon_j\in\{0,1\}\right\},\qquad
r_k(t)=\#\{(a,b,c)\in A_k^3:a+b+c=t\}.
\]
The ordered six-variable additive energy
\[
E_k=\sum_{t\in\mathbb Z}r_k(t)^2
=\#\{(a,b,c,d,e,f)\in A_k^6:a+b+c=d+e+f\}
\]
has the **exact all-level** recurrence and rational generating function
\[
E_0=1,\quad E_1=20,\quad E_{k+2}=26E_{k+1}-90E_k\ (k\ge0),
\qquad \sum_{k\ge0}E_kz^k=\frac{1-6z}{1-26z+90z^2}.
\]
Writing \(\lambda_\pm=13\pm\sqrt{79}\), the closed form is
\[
E_k=\frac{7+\sqrt{79}}{2\sqrt{79}}\lambda_+^k
+\frac{\sqrt{79}-7}{2\sqrt{79}}\lambda_-^k.
\]
The complete triple sumset is an integer interval,
\[
A_k+A_k+A_k=\{0,1,\ldots,3(3^k-1)/2\}.
\]
Nevertheless, with \(S_k=(3^{k+1}-1)/2\) its number of represented integers, the exact collision excess over uniformly distributed ordered triples grows at the sharp rate
\[
\frac{S_k E_k}{64^k}\sim
\frac{3(7+\sqrt{79})}{4\sqrt{79}}
\left(\frac{3(13+\sqrt{79})}{64}\right)^k,
\quad \frac{3(13+\sqrt{79})}{64}>1.
\]
Equivalently, the same \(E_k\) is the complete sixth Fourier moment
\[
E_k=\int_0^1\left|\sum_{a\in A_k}\exp(2\pi ia\theta)\right|^6d\theta.
\]
Scaling \(A_k\) by two gives the standard finite stages of the classical middle-thirds Cantor set; the six-variable equality counts are invariant under this scaling.

## Assumptions and scope

All variables are integers and the triples and sextuples are **ordered**. The empty-digit case \(k=0\) is included, with \(A_0=\{0\}\). Energy is for equality of ordinary integer sums, not congruence modulo \(3^k\); using the latter would change the answer. The Fourier integral uses normalized Lebesgue measure on the unit circle. No asymptotic result is substituted for an exact finite-level identity.

## Proof

**1. Carry identity.** For each sextuple write the signed column difference at ternary position \(j\) as
\[
d_j=\varepsilon_{1,j}+\varepsilon_{2,j}+\varepsilon_{3,j}-\varepsilon_{4,j}-\varepsilon_{5,j}-\varepsilon_{6,j}.
\]
It ranges over \(-3,\ldots,3\); its exact multiplicity is
\(w(d)=\binom6{3+d}\), by the coefficient identity \((1+x)^3(1+x^{-1})^3=x^{-3}(1+x)^6\). An equality \(\sum_{j=0}^{k-1}3^j d_j=0\) is equivalent to a sequence of integer carries \(c_0=c_k=0\) satisfying
\[
d_j=3c_{j+1}-c_j\quad (0\le j<k).
\]
For necessity, the vanished total sum implies that each lower-position partial sum is divisible by the corresponding power of three; the successive division produces these carries. Conversely, telescoping the displayed identity gives the total equality. From \(c_0=0\) and \(|d_j|\le3\), integrality of \(c_{j+1}=(c_j+d_j)/3\) inductively confines every carry to \(\{-1,0,1\}\). Thus no other carry states are omitted.

**2. Exact transfer matrix.** Order carry states as \(-1,0,1\). The number of permissible sextuple columns from state \(c\) to state \(c'\) is \(w(3c'-c)\), with zero weight outside \([-3,3]\). This gives
\[
T=\begin{pmatrix}6&15&0\\1&20&1\\0&15&6\end{pmatrix},
\qquad E_k=(T^k)_{0,0},
\]
where the matrix subscript \(0\) refers to the *middle* carry state. Reflection of the six bits exchanges the \(+1\) and \(-1\) carry states. Let \(u_k\) count partial sextuples ending in carry zero and \(v_k\) the count ending in each one of the two nonzero carry states. Starting with \((u_0,v_0)=(1,0)\), matrix multiplication yields
\[
\begin{pmatrix}u_{k+1}\\v_{k+1}\end{pmatrix}
=\begin{pmatrix}20&30\\1&6\end{pmatrix}
\begin{pmatrix}u_k\\v_k\end{pmatrix}.
\]
Here \(E_k=u_k\), since equality requires the final carry to vanish. This two-state matrix has trace \(26\) and determinant \(90\). Cayley--Hamilton gives the stated second-order recurrence, with \(E_0=1\), \(E_1=20\). Solving the recurrence gives the generating function and two-root closed form; both coefficients in the latter are positive.

**3. Complete interval of sums.** The sets satisfy \(A_{k+1}=A_k\cup(3^k+A_k)\). Writing \(B_k=A_k+A_k+A_k\) yields
\(B_{k+1}=\bigcup_{j=0}^3(j3^k+B_k)\).
The base \(B_0=\{0\}\) consists of one interval. If \(B_k=[0,3(3^k-1)/2]\cap\mathbb Z\), the four translated intervals are adjacent or overlap because \(3(3^k-1)/2\ge3^k-1\) for all \(k\ge0\). Their union is exactly the claimed interval for \(k+1\). This proves \(S_k=(3^{k+1}-1)/2\).

**4. Exact collision excess.** The ordered triple total is \(\sum_t r_k(t)=|A_k|^3=8^k\). Cauchy--Schwarz gives the uniform-support benchmark \(E_k\ge64^k/S_k\). Since \(0<\lambda_-<\lambda_+\) and the leading root coefficient is nonzero, the exact closed form implies \(E_k\sim (7+\sqrt{79})\lambda_+^k/(2\sqrt{79})\). Inserting \(S_k=(3^{k+1}-1)/2\) proves the displayed sharp equivalent. The inequality \(3\lambda_+>64\) follows from \(3\sqrt{79}>25\). Finally, orthogonality of integer characters on \([0,1]\) gives the Fourier identity by expanding the sixth power and integrating; a frequency survives exactly when the two three-term sums agree.

## Verification

A standalone Python program `CHECK.py` directly enumerates each finite set and independently constructs the ordered triple-sum histogram through \(k=8\). It checks equality of the direct squared histogram and the two-state carry recurrence, the complete interval of sums, initial coefficients and higher recurrence values. The first energies are \(1,20,430,9380,205180,4490480,98286280,2151300080,47088036880\). These finite computations test the proof but do not replace its all-\(k\) carry argument.

## Relationship to prior work

Hare and Sidorov (2022), arXiv:2210.07671, study the arithmetic and uniqueness of twofold sums of deleted-digit Cantor sets, with primary MSC2020 11A63. Their results motivate asking about multiplicities of higher sums but do not give this ordinary-integer finite-level sixfold collision count. Lau and Ngai (2000) derive the \(L^q\)-spectrum of the continuous *threefold* standard Cantor convolution, including at \(q=2\), via more general finite-type transfer methods; thus multifractal nonuniformity and its scaling exponent have substantial prior foundations and are not being claimed as new in themselves. Their displayed theorem is an asymptotic moment-spectrum characterization rather than the exact sequence \(E_k\) at all integer digit depths. In particular, their tabulated \(q=2\) spectral polynomial \(45z^2-832z+2048=0\) is transformed **exactly** into \(\lambda^2-26\lambda+90=0\) by \(z=64/\lambda\). Thus the leading spectral root and correlation-dimension exponent are already contained in their work and are not claimed as new; only the complete finite-depth collision identity, including its initial data, rational generating function and sharp leading multiplicative constant, is distinguished here. Fong, Hare and Johnstone (2011), and Hare, Hare and Shen (2019), study local dimensions and spectra of these convolutions, not the finite exact count above. Other published finite energy problems for different base/digit systems and Fourier extremal problems do not imply this exact sequence by parameter substitution. The exact discrete six-tuple formula is the specific proposed contribution; priority against unindexed or implicitly equivalent finite-type identities remains a limitation.

## Limitations

No new general theorem about all Cantor digit sets, all higher-fold convolutions, or general \(L^q\) spectra is asserted. The result counts a single canonical family at every finite level, not arbitrary deleted-digit systems. The all-level recurrence is proved without numerical extrapolation. The connection to known multifractal exponents may be derivable from established theory; only the explicit finite-level enumeration and closed rational generating function are distinguished here. No independent verification is asserted.

## References

1. K. G. Hare and N. Sidorov, *The Minkowski sum of linear Cantor sets*, arXiv:2210.07671, first posted 2022-10-14, https://arxiv.org/abs/2210.07671 .
2. K.-S. Lau and S.-M. Ngai, *Second-order self-similar identities and multifractal decompositions*, Indiana University Mathematics Journal 49 (2000), 925--972, https://scispace.com/pdf/second-order-self-similar-identities-and-multifractal-71znxgov33.pdf .
3. V. P.-W. Fong, K. E. Hare and D. L. Johnstone, *Multifractal analysis for convolutions of overlapping Cantor measures*, Asian Journal of Mathematics 15 (2011), 53--70, https://intlpress.com/api/bgcloud-front/resource/pdf/volume/1806252759957606402-1806252759957606402-3120dba1d7ba4f2d24c3ed500d07c498.pdf .
4. K. E. Hare, K. G. Hare and W. Shen, *The \(L^q\)-spectrum for a class of self-similar measures with overlap*, arXiv:1909.08941, https://arxiv.org/abs/1909.08941 .
