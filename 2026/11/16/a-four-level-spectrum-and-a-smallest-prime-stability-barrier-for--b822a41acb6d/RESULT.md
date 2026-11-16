# A four-level spectrum and a smallest-prime stability barrier for primitive semiprime Fourier sampling

## Finding

Let \(p<q\) be distinct primes, \(N=pq\), and \(\varphi=(p-1)(q-1)\). Define the \(\varphi\)-by-\(q\) Fourier sampling matrix
\[
 F_{a,j}=\varphi^{-1/2}\exp\!\left(\frac{2\pi i a j}{pq}\right),
 \qquad a\in(\mathbb Z/N\mathbb Z)^\times,\quad 0\le j<q.
\]
Thus the measurements are precisely the primitive Fourier frequencies, and the unknown signal occupies \(q\) consecutive time coordinates. Put \(q=pk+s\), so \(k\ge1\) and \(1\le s\le p-1\), and define
\[
 a_0=\frac{q}{q-1},\qquad
 u=a_0-\frac{p(k+1)}{\varphi},\qquad
 v=a_0-\frac{pk}{\varphi},\qquad
 w=a_0-\frac{q+p-2s}{\varphi}.
\]
The **complete multiset** of squared singular values of \(F\), including all multiplicities, is
\[
 \boxed{\operatorname{spec}(F^*F)
 =\{a_0^{[q-p+1]},\ u^{[s-1]},\ v^{[p-s-1]},\ w^{[1]}\}.}
\]
Here \(z^{[m]}\) means that \(z\) occurs with multiplicity \(m\); terms with multiplicity zero are omitted. These formulas remain valid if some values coincide.

For \(p=2\), \(F\) has rank \(q-1\), with precisely one zero singular value, and the nullspace is spanned by \(((-1)^j)_{j=0}^{q-1}\). For every odd \(p\), \(F\) has full column rank and the **sharp frame bounds** are
\[
 \boxed{\lambda_{\max}(F^*F)=\frac{q}{q-1},\quad
 \lambda_{\min}(F^*F)=\frac{p-2}{p-1}
 +\frac{\max\{s-2,0\}}{(p-1)(q-1)}.}
\]
Consequently, for every odd \(p\), uniformly in all larger primes \(q\),
\[
 \frac{p-2}{p-1}\|x\|_2^2\le\|Fx\|_2^2
 \le\frac{q}{q-1}\|x\|_2^2,
 \qquad x\in\mathbb C^q.
\]
The left bound is an equality for this individual pair precisely when \(q\bmod p\) is \(1\) or \(2\). The exact Euclidean condition number is the square root of the ratio of the displayed extremal eigenvalues. Along primes \(q\to\infty\) with fixed odd \(p\), it tends to \(\sqrt{(p-1)/(p-2)}\).

## Assumptions and scope

Both \(p\) and \(q\) are ordinary positive primes, with \(2\le p<q\). The Fourier matrix uses the counting Euclidean norm in its \(q\)-coordinate input and its \(\varphi\)-coordinate output, scaled by \(\varphi^{-1/2}\). Rows are all unit residue classes modulo \(pq\) without repetitions. Columns correspond to exactly the time sites \(0,1,\dots,q-1\); a common translate of these sites gives a unitarily equivalent matrix. We do not claim the same spectrum for arbitrary nonconsecutive time supports or for other composites.

## Proof

**1. Exact Gram kernel.** The Ramanujan-sum identity gives, for column indices \(i,j\),
\[
 (F^*F)_{ij}=\frac{c_{pq}(j-i)}{\varphi},\qquad
 c_{pq}(h)=c_p(h)c_q(h).
\]
For any prime \(\ell\), \(c_\ell(h)=\ell-1\) when \(\ell\mid h\) and \(c_\ell(h)=-1\) otherwise. Since \(|i-j|<q\), the only difference divisible by \(q\) is zero. Hence the diagonal Gram entries are one, distinct entries in the same residue class modulo \(p\) are \(-1/(q-1)\), and entries in different classes are \(1/\varphi\).

For \(0\le r<p\), let \(u_r\) be the indicator in \(\mathbb C^q\) of the coordinates congruent to \(r\bmod p\). The preceding three cases give the exact identity
\[
 \boxed{G=F^*F=a_0 I-\frac p\varphi\sum_{r=0}^{p-1}u_ru_r^*
 +\frac1\varphi\mathbf1\mathbf1^*.}\tag{1}
\]
Exactly \(s\) residue classes have size \(k+1\), and the other \(p-s\) have size \(k\).

**2. Eigenspaces.** Let \(y_r=u_r^*x\) be the class sums of \(x\in\mathbb C^q\). From (1),
\[
 \langle(G-a_0I)x,x\rangle
 =\frac{\left|\sum_r y_r\right|^2-p\sum_r|y_r|^2}{\varphi}\le0.
\]
Equality holds exactly when all \(p\) class sums coincide. All classes are nonempty. This equality subspace has dimension \(q-p+1\), giving the full top-eigenvalue multiplicity.

On the orthogonal complement of the within-class sum-zero vectors, take normalized class indicators \(e_r=u_r/\sqrt{m_r}\), where \(m_r=\|u_r\|_2^2\). In this orthonormal basis the residual \(p\)-dimensional operator is
\[
 M=a_0 I_p-\frac p\varphi\operatorname{diag}(m_0,\ldots,m_{p-1})
 +\frac1\varphi(\sqrt{m_r m_t})_{r,t}.
\]
Contrasts among the \(s\) large classes have eigenvalue \(u\), multiplicity \(s-1\). Contrasts among the \(p-s\) small classes have eigenvalue \(v\), multiplicity \(p-s-1\). The remaining two-dimensional operator has one eigenvalue \(a_0\), from the equal-class-sum condition. Its trace is \(2a_0-(q+p-2s)/\varphi\), so its second eigenvalue is exactly \(w\). Combining these with the \(q-p\) within-class sum-zero vectors proves the full multiset.

**3. Sharp extremal eigenvalues.** Since \(k\ge1\), direct subtraction gives
\[
 u<w<v<a_0\quad\text{whenever all four sectors are present},
 \qquad w-u=\frac{s}{\varphi},\quad v-w=\frac{p-s}{\varphi}.
\]
When \(s=1\), the \(u\)-sector has zero multiplicity and the least eigenvalue is \(w\); otherwise it is \(u\). Substituting \(pk=q-s\) yields
\[
 u=\frac{p-2}{p-1}+\frac{s-2}{\varphi},
 \qquad w=u+\frac{s}{\varphi}.
\]
The claimed least eigenvalue follows in both cases. It is positive for \(p\ge3\), while for \(p=2\) necessarily \(s=1\) and it vanishes. For \(p=2\), identity (1) simplifies to \(G=\frac q{q-1}I-\frac1{q-1}vv^*\), where \(v_j=(-1)^j\), giving the stated rank and nullspace. Finally, the uniform bound and the asymptotic condition number follow immediately from the exact eigenvalues, with \(1\le s<p\) held bounded as \(q\to\infty\).

## Verification

The accompanying `check_spectrum.py` computes the matrix directly from complex Fourier exponentials, separately computes its exact Ramanujan Gram kernel, and compares both with the **rational** four-level spectral formula. Run `python check_spectrum.py` from a directory with Python and NumPy installed. Its current run passed 465 assertions across 93 distinct-prime pairs \(p<q\), with \(p\le13\) and \(q\le67\). This is a finite check only; the proof above establishes the complete family.

## Relationship to prior work

Ushiroya's 2018 analysis gives the spectrum of the **full** Ramanujan circulant \((c_N(i-j))_{0\le i,j<N}\), with eigenvalues \(0\) and \(N\). Compressing a circulant to \(q\) consecutive coordinates is not a spectral restriction to its Fourier eigenspaces: it changes the spectrum. The present theorem computes that truncated primitive-row Fourier Gram spectrum for every distinct-prime product and gives its sharp lower bound.

Schlage-Puchta's 2021 determinant theorem treats a Ramanujan-sum matrix indexed by the **divisors** of \(N\); its indexing and invertibility question differ from this consecutive-coordinate frame problem. The publicly indexed result *Consecutive Fourier bands minimize primitive-row frame potential at every modulus* treats a Frobenius/frame-potential optimization for the same primitive-row sampling setting. The available abstract-level record does not establish the present four-level spectrum or the sharp lower Riesz bound; its full text was not accessible for direct comparison, so historical priority requires further verification.

## Limitations

The exact four-level statement is for a semiprime modulus and a consecutive block whose length is the **larger prime factor**, not an arbitrary length, sampling set, or modulus. The exceptional \(p=2\) rank loss is also consistent with there being only \(q-1\) primitive measurements for \(q\) unknowns. The number of numerical tests is finite and does not certify the theorem independently. The claimed literature comparison does not establish absolute priority, especially because one closely related publicly indexed full text could not be inspected.

## References

- N. Ushiroya, *Eigenvalues of Matrices whose Elements are Ramanujan Sums or Kloosterman Sums*, Journal of Integer Sequences **21** (2018), Article 18.2.6, published March 6, 2018. Full text: https://cs.uwaterloo.ca/journals/JIS/VOL21/Ushiroya/ushi3.pdf ; arXiv:1803.02970 (first posted March 8, 2018).
- J.-C. Schlage-Puchta, *A determinant involving Ramanujan sums and So's conjecture*, Archiv der Mathematik **117** (2021), 379–384, published July 17, 2021. https://doi.org/10.1007/s00013-021-01643-8
- *Consecutive Fourier bands minimize primitive-row frame potential at every modulus*, public research index entry, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-consecutive-fourier-bands-minimize-primitive-row-frame-potential--d824c1a982ba . Abstract-level comparison only; full text unavailable at inspection.
