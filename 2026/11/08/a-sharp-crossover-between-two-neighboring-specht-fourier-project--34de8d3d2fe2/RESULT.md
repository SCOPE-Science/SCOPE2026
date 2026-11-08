# A sharp crossover between two neighboring Specht Fourier projection norms

## Finding
For each integer \(n\ge4\), let \(G=S_n\). Write \(E_{\mathrm h}\) and \(E_{\mathrm t}\) for the real spaces of **all** matrix coefficients of the irreducible representations with respective Young shapes \((n-2,1,1)\) and \((n-2,2)\), considered as subspaces of \(C(G;\mathbb R)\) with its supremum norm. Let \(\Lambda_{\mathrm h}(n)\) and \(\Lambda_{\mathrm t}(n)\) be the minimum norms among real linear projections from \(C(G;\mathbb R)\) onto these respective subspaces. Then no equality occurs, and
\[
\Lambda_{\mathrm t}(n)>\Lambda_{\mathrm h}(n)
\quad\Longleftrightarrow\quad n=5\ \text{or}\ n\ge8.
\]
For \(n=4,6,7\), the reverse strict inequality holds. The underlying irreducible representation dimensions differ by **exactly one**: \(d_{\mathrm h}=(n-1)(n-2)/2\), \(d_{\mathrm t}=n(n-3)/2\), and \(d_{\mathrm h}-d_{\mathrm t}=1\).

In fact the strict macroscopic separation stabilizes:
\[
\lim_{n\to\infty}\frac{\Lambda_{\mathrm t}(n)-\Lambda_{\mathrm h}(n)}{d_{\mathrm t}}
=\delta,\qquad \frac1{40}<\delta<\frac1{38}.
\]
For independent \(K\sim\operatorname{Poisson}(1)\) and \(M\sim\operatorname{Poisson}(1/2)\), this constant is the explicitly convergent expectation difference
\[
\delta=\mathbb E\left|\frac{K(K-1)}2+M-K\right|
-\mathbb E\left|\frac{(K-1)(K-2)}2-M\right|
\approx0.02606751085.
\]
The final decimal is illustrative, not a certified interval; the stated rational bounds are rigorous.

## Assumptions and scope
The domain is the finite group \(S_n\) with uniform counting probability, \(n\ge4\). All functions and projections are real. A matrix-coefficient space contains the full \(d^2\)-dimensional irreducible isotypic block, not merely its central character line. A *relative* minimum projection norm is meant: the ambient space is \(C(S_n;\mathbb R)\). The two shapes are distinct and well-defined for every stated \(n\).

Let \(k(\sigma)\) and \(m(\sigma)\) count the cycles of lengths one and two of \(\sigma\in S_n\). Define the integer-valued character polynomials
\[
H(k,m)=\frac{(k-1)(k-2)}2-m,\qquad
T(k,m)=\frac{k(k-1)}2+m-k.
\]
The first formula uses an ordinary polynomial and is defined also at \(k=0\). Let \(q_0=1\) and, for \(r\ge1\),
\[
q_r=\frac1r\sum_{j=3}^{r}q_{r-j},
\]
with the empty sum zero. Equivalently, \(q_r\) is the number of permutations of \(r\) having no one- or two-cycles, divided by \(r!\). Set
\[
A_n=\sum_{\substack{k,m\ge0\\k+2m\le n}}
\frac{q_{n-k-2m}}{k!2^m m!}|H(k,m)|,
\qquad
B_n=\sum_{\substack{k,m\ge0\\k+2m\le n}}
\frac{q_{n-k-2m}}{k!2^m m!}|T(k,m)|.
\]
Both are exact rational numbers. The sharp projector norms are
\[
\Lambda_{\mathrm h}(n)=d_{\mathrm h}A_n,\qquad
\Lambda_{\mathrm t}(n)=d_{\mathrm t}B_n.
\]

## Proof
**Character identities.** Let \(V\) be the \((n-1)\)-dimensional standard representation of \(S_n\). Its character is \(k-1\), and that of \(V\) evaluated at \(\sigma^2\) is \(k+2m-1\). The exterior-square character is therefore
\[
\chi_{\wedge^2 V}(\sigma)
=\tfrac12\big((k-1)^2-(k+2m-1)\big)=H(k,m).
\]
The standard hook identity \(\wedge^2 V\cong S^{(n-2,1,1)}\) identifies it with the first target space. The permutation representation on unordered two-element subsets has character \(\binom{k}{2}+m\), counting fixed pairs and transposed pairs. Its irreducible decomposition is \(\mathbf1\oplus V\oplus S^{(n-2,2)}\), so subtracting the first two characters gives \(T(k,m)\). The hook-length formula, or these decompositions, gives the stated degrees.

**Minimum norms.** Every irreducible representation of \(S_n\) has an absolutely irreducible real model. Averaging any projection onto one of the two coefficient spaces over the commuting left and right translation actions yields another projection of no larger supremum-operator norm. By the irreducible, multiplicity-free \(S_n\times S_n\) decomposition of functions on \(S_n\), the unique projection commuting with both actions onto the selected coefficient block is its central Fourier projector. Its convolution kernel is \(d_\lambda\chi_\lambda(\sigma\tau^{-1})/n!\). Each evaluation row has \(\ell^1\) norm \(d_\lambda\mathbb E|\chi_\lambda|\), and a real sign choice of the corresponding row attains it. Hence this central projector minimizes the operator norm, with the two formulas above.

**Exact cycle counting.** The exponential generating function for permutations with all cycles of length at least three is
\[
\sum_{r\ge0}q_rz^r
=\exp\left(\sum_{j\ge3}\frac{z^j}{j}\right)
=\frac{e^{-z-z^2/2}}{1-z}.
\]
Differentiating proves the recurrence for \(q_r\). A permutation with \(k\) fixed points and \(m\) two-cycles and any remainder of cycles of length at least three has probability \(q_{n-k-2m}/(k!2^m m!)\). Summation gives \(A_n\) and \(B_n\).

**Finite degrees.** The exact rational values of \(d_{\mathrm t}B_n-d_{\mathrm h}A_n\) for \(4\le n\le29\) are in `finite_certificate.tsv`. Their signs are positive precisely for \(n=5\) and \(8\le n\le29\). In particular, the first seven gaps are
\[
\begin{array}{c|rrrrrrr}
n&4&5&6&7&8&9&10\\\hline
\Lambda_{\mathrm t}-\Lambda_{\mathrm h}
&-11/12&7/6&-49/60&-44/45&4313/20160&701/5040&18869/90720.
\end{array}
\]
The finite certificate is checked by exact rational arithmetic, using the above recurrence and an independent inclusion-exclusion formula for \(q_r\). The included checker additionally counts actual permutations through \(n=8\). This finite computation proves only the explicitly finite range.

**All remaining degrees and limit.** For \(f=|H|\) or \(|T|\), introduce the entire function
\[
F_f(z)=\sum_{k,m\ge0}\frac{f(k,m)z^{k+2m}}{k!2^m m!},
\quad W_f(z)=e^{-z-z^2/2}F_f(z),
\quad L_f=W_f(1).
\]
The coefficient identity \(\mathbb E_n f=[z^n]W_f(z)/(1-z)\) implies
\[
\mathbb E_n f-L_f=[z^n]\frac{W_f(z)-W_f(1)}{1-z}.
\]
The quotient has a removable singularity at one and is entire. Both character absolute values obey \(f(k,m)\le(k+2)^2+m\). On \(|z|=2\), Poisson summation bounds \(|F_f(z)|\le20e^4\) and \(|W_f(z)|\le20e^8\), while \(0\le L_f\le21/2\). Since \(e<68/25\) and \((68/25)^8<3000\), Cauchy's coefficient estimate gives the **uniform explicit error**
\[
|\mathbb E_n f-L_f|\le\frac{60011}{2^n}\qquad(n\ge0).
\]
This proves convergence to the two independent-Poisson expectations in the finding. A direct exact evaluation from the cycle formula at \(n=30\) gives
\[
B_{30}-A_{30}
=\frac{28810340840256302566019194639}
{1105220249217462744317952000000}.
\]
The exact rational inequalities verified in the checker are
\[
\frac1{40}< (B_{30}-A_{30})-\frac{120022}{2^{30}},
\qquad
(B_{30}-A_{30})+\frac{120022}{2^{30}}<\frac1{38}.
\]
Consequently \(1/40<\delta<1/38\). For every \(n\ge30\), the same error gives \(B_n-A_n>1/41\). By irreducible-character orthogonality, \(A_n\le(\mathbb E H^2)^{1/2}=1\). Hence
\[
\Lambda_{\mathrm t}(n)-\Lambda_{\mathrm h}(n)
=d_{\mathrm t}(B_n-A_n)-A_n
>\frac{n(n-3)}{82}-1>0,
\]
where the final inequality holds for \(n\ge30\). Together with the finite certificate this proves the exact crossover. Dividing the same identity by \(d_{\mathrm t}\) and letting \(n\to\infty\) proves the asymptotic limit.

## Verification
Run `python3 verify.py` in the same directory as `finite_certificate.tsv` with Python 3 standard library. The checker uses `fractions.Fraction` throughout, independently checks the cycle EGF by inclusion-exclusion, verifies both character second moments equal one, matches 26 exact finite gap certificates, enumerates every permutation for orders four through eight, and checks the rational inequalities needed for the infinite-dimensional Cauchy bound. Its finite cases alone do not establish the all-\(n\) claim; the analytic estimate in the proof closes the infinite range.

## Relationship to prior work
Hultman's 2013 character-statistics treatment explicitly records the hook character in terms of one- and two-cycle counts. Marin (2011) identifies hook modules with exterior powers of the standard representation. Regev and Zeilberger (2015) compare **sums of squares over whole collections** of two-row and hook shapes, a different statistic from the minimum \(L^\infty\) projection norms of these two individual coefficient spaces. Defant et al. (2022) give a broad averaging framework for projection constants, credited here for the minimality method. Existing precise projection results for the \((n-2,2)\) block supply one of the two comparison terms; that term and general Fourier projection principles are not claimed as new. The contribution here is the exact all-degree **comparison**, its irregular small-degree exceptions, and the positive limiting gap despite the irreducible dimensions differing by one.

## Limitations
The theorem compares only these two shapes, and only relative projection norms in real \(C(S_n)\). It does not assert a universal ordering among all irreducible characters of similar degrees, nor identify the absolute Banach-space projection constants under arbitrary embeddings. Numerical decimals are illustrative; the proof's certified asymptotic statement is the rational interval. The novelty search cannot exclude an unindexed equivalent comparison in older character-norm literature.

## References
- I. Marin, *Hooks generate the representation ring of the symmetric group*, arXiv:1112.3127v1, publicly posted 2011-12-14; see §1.
- A. Hultman, *Permutation statistics of products of random permutations*, arXiv:1301.0430v1, publicly posted 2013-01-03; see Lemmas 2.1–2.2 and §2.
- A. Regev and D. Zeilberger, *Surprising Relations Between Sums-Of-Squares of Characters of the Symmetric Group Over Two-Rowed Shapes and Over Hook Shapes*, arXiv:1510.07061v1, publicly posted 2015-10-23.
- A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Projection constants for spaces of multivariate polynomials*, arXiv:2208.06467v1, publicly posted 2022-08-12; §2.2 (Rudin averaging).
