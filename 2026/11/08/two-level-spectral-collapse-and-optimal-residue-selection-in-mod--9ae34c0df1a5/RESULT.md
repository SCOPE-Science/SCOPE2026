# Two-level spectral collapse and optimal residue selection in modulo-three Walsh sampling

## Finding
Let \(n\ge5\) and equip the Boolean cube \(\{0,1\}^n\) with normalized counting measure. Let \(\mathcal H_1\) be the span of the constant Walsh character and all \(n\) one-coordinate Walsh characters. For \(r\in\{0,1,2\}\), let \(S_{n,r}=\{x:\operatorname{wt}(x)\equiv r\pmod3\}\), and let \(G_{n,r}\) be the Gram operator of restriction from \(\mathcal H_1\) to \(S_{n,r}\), with the inherited cube normalization.

Write \(M=2^n\) and \(k\equiv n-2r\pmod6\), choosing \(0\le k\le5\). Define the periodic integers
\[
(t_0,t_1,t_2,t_3,t_4,t_5)=(2,1,-1,-2,-1,1),\qquad
(u_0,u_1,u_2,u_3,u_4,u_5)=(0,1,1,0,-1,-1).
\]
The exact Gram matrix in the basis \(1,(-1)^{x_1},\ldots,(-1)^{x_n}\) is
\[
G_{n,r}=
\begin{pmatrix}
 a&b\mathbf1^{\mathsf T}\\
 b\mathbf1&(a-c)I_n+c\mathbf1\mathbf1^{\mathsf T}
\end{pmatrix},\qquad
 a=\frac{M+t_k}{3M},\quad b=\frac{u_k}{M},\quad c=-\frac{t_k}{M}.
\]
For the two **regular** residues, where \(k\in\{1,2,4,5\}\), the complete spectrum is
\[
\boxed{\frac{M+4t_k}{3M}\quad(n\text{ times}),\qquad
\frac{M+(1-3n)t_k}{3M}\quad(1\text{ time}).}
\]
For the unique **exceptional** residue, where \(k=0\) or \(k=3\), it is
\[
\boxed{\frac{M+4t_k}{3M}\quad(n-1\text{ times}),\qquad
\frac{M+t_k}{3M}\quad(1\text{ time}),\qquad
\frac{M+(4-3n)t_k}{3M}\quad(1\text{ time}).}
\]
All eigenvalues are strictly positive. In particular, all three residue classes yield injective sampling on \(\mathcal H_1\), and their optimal squared sampling bounds are the minimum and maximum of their displayed spectral levels.

Among the three choices of residue class, **precisely the two regular classes (tied) minimize the squared singular-value condition ratio**. The minimum and the exceptional ratio are, respectively,
\[
\boxed{
\begin{array}{c|cc}
&\rho_{\rm opt}&\rho_{\rm exceptional}\\ \hline
n\ \mathrm{even}&\dfrac{M+3n-1}{M-4}&\dfrac{M+8}{M-6n+8}\\[6pt]
n\ \mathrm{odd}&\dfrac{M+4}{M+1-3n}&\dfrac{M+6n-8}{M-8}
\end{array}}
\]
with \(\rho_{\rm opt}<\rho_{\rm exceptional}\) strictly. The optimal singular-value condition number thus satisfies
\[
\boxed{\kappa_{\rm opt}=\sqrt{\rho_{\rm opt}}=1+\frac{3(n+1)}{2^{n+1}}+O(n^2 4^{-n}).}
\]
No residue-class restriction is exactly tight in the stated range. In even dimensions the two condition-optimal classes also use strictly fewer samples than the exceptional class.

## Assumptions and scope
The integer \(n\) is at least five. The three spatial masks are complete Hamming-weight congruence classes, not isolated Hamming layers or arbitrary subsets. The Fourier band has complex dimension \(n+1\). The source inner product is \(2^{-n}\sum_x f(x)\overline{g(x)}\), and the sampled norm is \(2^{-n}\sum_{x\in S_{n,r}}|f(x)|^2\). The Gram eigenvalues are squared singular values with this normalization. The squared condition ratio \(\rho\) is the largest Gram eigenvalue divided by its smallest; the sampling condition number is \(\sqrt\rho\). The asymptotic claim keeps the modulus three fixed and sends \(n\to\infty\).

## Proof
**Roots-of-unity counts.** For an integer \(m\ge0\) and a residue \(s\), define \(N_m(s)=\sum_{j\equiv s\;(\mathrm{mod}\;3)}\binom mj\). Filtering \((1+z)^m\) by the three cube roots of unity gives
\[
N_m(s)=\frac{2^m+2\cos((m-2s)\pi/3)}3.
\]
The spatial density is \(a=N_n(r)/M=(M+t_k)/(3M)\). Fixing a single coordinate to zero or one shows that the correlation between the constant character and any one-coordinate Walsh character equals
\[
 b=\frac{N_{n-1}(r)-N_{n-1}(r-1)}M=\frac{u_k}M.
\]
Similarly, conditioning on two coordinates shows that the correlation between two distinct one-coordinate characters is
\[
 c=\frac{N_{n-2}(r)-2N_{n-2}(r-1)+N_{n-2}(r-2)}M=-\frac{t_k}M.
\]
The six entries of \(t_k\) and \(u_k\) follow by evaluating the displayed cosines. Diagonal character correlations all equal \(a\), proving the Gram matrix formula.

**Complete spectra.** For regular residues one has \(t_k^2=u_k^2=1\), hence \(b^2=c^2\). With \(v=(b/c,1,\ldots,1)^{\mathsf T}\), the Gram matrix is exactly \((a-c)I_{n+1}+cvv^{\mathsf T}\). Since \(\|v\|^2=n+1\), its two eigenvalues are \(a-c\) with multiplicity \(n\), and \(a+nc\) with multiplicity one. Substitution yields the regular formula. For the exceptional residue \(u_k=0\), so the constant character separates with eigenvalue \(a\). On the \(n\) coordinate characters, the sum-zero space has eigenvalue \(a-c\) with multiplicity \(n-1\), and the coordinate-sum direction has eigenvalue \(a+(n-1)c\). Substitution yields the exceptional formula. Since \(n\) is even precisely when the regular residues have \(t_k=-1\), and odd precisely when they have \(t_k=1\), the parity table follows.

**Positivity and sharp bounds.** The denominators \(3M\) are positive. For even \(n\ge6\), \(M-4>0\) and \(M-6n+8>0\); for odd \(n\ge5\), \(M+1-3n>0\) and \(M-8>0\). The remaining numerators are larger. Thus every Gram operator is positive definite. Its extreme eigenvalues give the exact sharp squared sampling bounds. Because \(c\ne0\), the Gram matrix is not a scalar multiple of the identity, so no class is tight.

**Unique choice up to the two-residue tie.** If \(n\) is even, comparing the two ratios by positive cross-multiplication gives
\[
 (M+8)(M-4)-(M+3n-1)(M-6n+8)
=3\big((n-1)M+6n^2-10n-8\big)>0.
\]
If \(n\) is odd, it gives
\[
 (M+6n-8)(M+1-3n)-(M+4)(M-8)
=3\big((n-1)M-6n^2+10n+8\big)>0.
\]
For the latter inequality at \(n=5\), the quantity in parentheses is \(36\). Its increment from \(n\) to \(n+1\) is \((n+1)2^n-12n+4>0\) for all \(n\ge5\), proving the required inequality (indeed for all subsequent integers). Therefore exactly the two regular residue classes minimize the condition ratio. The asymptotic formula follows from \(\rho_{\rm opt}=1+3(n+1)/M+O(n^2/M^2)\) and Taylor expansion of the positive square root. For even dimensions the regular masks have \((M-1)/3\) points, while the exceptional one has \((M+2)/3\), proving the stated sample-count comparison.

## Verification
The standalone pure-standard-library script `artifacts/verify.py` enumerates every mask and constructs its actual integer-valued Fourier Gram matrix in each of the eighteen cases \(5\le n\le10\), \(0\le r\le2\). It checks each matrix entry against the formula, independently tests polynomial annihilation by the predicted eigenvalues and the first two trace moments, and checks the root-of-unity count identities and strict optimality inequalities in all \(408\) cases \(5\le n\le140\), \(0\le r\le2\). Execute `python artifacts/verify.py` from the package root. The expected successful output is `MOD3_WALSH_SPECTRAL_VERIFY_PASS direct=18 exact=408`. Finite checks are supplementary; the algebraic proof establishes the all-dimension claim.

## Relationship to prior work
Rao (2021) treats Fourier transforms of restrictions to a **single** Boolean Hamming slice and proves a slice Fourier-coefficient relation and a Goldreich–Levin-type theorem, not the exact first-Walsh-band Gram spectra of unions of periodically separated slices. Cornelissen, Mande, Ozols, and de Wolf (2021) analyze the Hamming-weight-modulo-three function and its exact quantum query complexity; their focus is query lower/upper bounds, not the spatial sampling conditioning of the low-degree Walsh band. Existing published spectra for a single nonbinary Hamming shell or a Boolean Hamming **ball** use related permutation decompositions, but neither determines the two-level degeneracy or strictly optimal residue choice for these congruence-class masks. The roots-of-unity count itself is standard; the result is the complete, sharp spectral/conditioning and design classification for these masks.

## Limitations
The theorem is about the first Walsh band and three equal-cost, unweighted residue-class masks, not higher Fourier degrees or optimally selected arbitrary subsets. It does not establish noise robustness for nonlinear reconstruction. The restriction \(n\ge5\) matters: an exceptional residue at \(n=4\) is singular. Existing general association-scheme or coding-theory identities may implicitly specialize to the Gram calculation; the literature search does not establish worldwide priority. The checker is finite and is not an independent proof of the all-dimension inequalities.

## References
1. S. Rao, *The Fourier Transform of Restrictions of Functions on the Slice*, arXiv:2111.03213v1, first posted 2021-11-05. https://arxiv.org/abs/2111.03213
2. A. Cornelissen, N. S. Mande, M. Ozols, R. de Wolf, *Exact quantum query complexity of computing Hamming weight modulo powers of two and three*, arXiv:2112.14682v1, first posted 2021-12-29. https://arxiv.org/abs/2112.14682
3. *Exact q-ary Hamming-shell Fourier concentration and the arithmetic tightness criterion*, published research record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-q-ary-hamming-shell-fourier-concentration-and-the-arithmet--89a15e26e594
4. *Exact first-Walsh-band concentration spectra on Boolean Hamming balls*, published research record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-first-walsh-band-concentration-spectra-on-boolean-hamming--a2f5ddac5a0f
