# Fourier support and sharp recovery of primitive words over finite abelian alphabets

## Finding
Let \(H\) be any finite abelian group with \(q=|H|\ge 2\), and let \(n\ge2\). A *primitive word* is a position-labelled word in \(G=H^n\) whose least cyclic rotation period is exactly \(n\). Define \(r=\operatorname{rad}(n)\), the product of the distinct primes dividing \(n\), and \(m=n/r\). Let \(f\colon G\to\{0,1\}\) indicate the primitive words.

For a divisor \(d\mid n\), put \(U_d=\{x\in G:x_{j+d}=x_j\text{ for all }j\}\) (cyclic indices). Its annihilator \(C_d=U_d^\perp\subseteq\widehat G\) consists exactly of tuples \(\chi=(\chi_0,\ldots,\chi_{n-1})\) for which
\[
\prod_{j\equiv a\pmod d}\chi_j=1_{\widehat H}\qquad(0\le a<d).
\]
Here the product of characters is taken in \(\widehat H\). Use the **unnormalized** transform \(\widehat f(\chi)=\sum_{x\in G}f(x)\overline{\chi(x)}\). For every frequency,
\[
\boxed{\widehat f(\chi)=\sum_{e\mid r}\mu(r/e)q^{me}\,\mathbf 1_{C_{me}}(\chi).}
\]
Moreover the transform vanishes **exactly** outside \(C_m\); there is no cancellation at any frequency in \(C_m\). Thus the counting convolution \(T_fh(x)=\sum_{y\in G}f(x-y)h(y)\) has
\[
\boxed{\operatorname{rank}T_f=q^{n-m},\qquad \operatorname{nullity}T_f=q^n-q^{n-m}.}
\]
Its smallest positive singular value is **exactly** \(q^m\), while the largest is \(P_q(n)=\sum_{e\mid r}\mu(r/e)q^{me}\), the number of primitive labelled words. Consequently its inverse on the orthogonal complement of the kernel has sharp operator norm \(q^{-m}\) and sharp condition number \(P_q(n)/q^m\). The image is precisely the functions invariant under translation by every period-\(m\) word. The complete translation stabilizer of \(f\) is precisely \(U_m\).

In particular, if \(n\) is squarefree then \(m=1\) and the only Fourier zeros are those enforced by constant-word translation symmetry. If \(n\) is not squarefree, additional hidden period-\(m\) translation symmetries reduce the Fourier rank.

## Assumptions and scope
All words are **position-labelled**; this is not the indicator of one representative from each necklace orbit. \(H\) may be cyclic, noncyclic, or composite-order, but must be finite and abelian. The convolution is on the additive group \(G=H^n\), not on the cyclic group of position rotations. Parameters range over every integer \(n\ge2\) and every finite abelian \(H\) with \(q\ge2\); no assumption of prime-power order is made. Fourier normalization is unnormalized, so the singular values are the absolute values of the displayed multipliers.

## Proof
**1. Period-lattice Möbius inversion.** Every word has a unique smallest rotation period dividing \(n\). The identity
\[
 f=\sum_{d\mid n}\mu(n/d)\mathbf1_{U_d}
\]
therefore holds pointwise, by summing \(\mu(n/d)\) over the divisors of \(n\) that are multiples of the smallest period. The Möbius coefficient is nonzero exactly for \(d=me\), \(e\mid r\), giving the asserted finite expansion.

**2. Character orthogonality.** The subgroup \(U_d\cong H^d\) has order \(q^d\). Orthogonality gives \(\sum_{x\in U_d}\overline{\chi(x)}=q^d\) if \(\chi\in C_d\), and zero otherwise, proving the coefficient formula. For \(d\mid d'\mid n\), \(U_d\subseteq U_{d'}\), hence \(C_{d'}\subseteq C_d\). Every term in the expansion is therefore supported in \(C_m\).

**3. Exact noncancellation.** Fix \(\chi\in C_m\), and let \(d_*\) be the greatest divisor \(d=me\) of \(n\) with \(e\mid r\) and \(\chi\in C_d\). At least \(d=m\) is eligible. Its term has coefficient \(\pm q^{d_*}\), and every other surviving term has exponent a **distinct positive integer** less than \(d_*\). Their total absolute magnitude is at most \(\sum_{j=0}^{d_*-1}q^j<q^{d_*}\), because \(q\ge2\). Therefore \(\widehat f(\chi)\ne0\). Since \(|C_m|=|G|/|U_m|=q^{n-m}\), this proves support, rank, and nullity.

**4. Sharp smallest multiplier.** The expansion contains only powers \(q^d\) with \(d\ge m\), so every multiplier is an integer divisible by \(q^m\). The smallest nonzero magnitude is at least \(q^m\). For each prime \(p\mid r\), the relative index of \(C_{mp}\) in \(C_m\) is \(q^{m(p-1)}\). The union of these proper subgroups does not exhaust \(C_m\), since
\[
\sum_{p\mid r}\frac{|C_{mp}|}{|C_m|}=\sum_{p\mid r}q^{-m(p-1)}\le\sum_{p\text{ prime}}2^{-(p-1)}\le1-2^{-3}<1.
\]
(The last inequality omits exponent three, because four is not prime.) Choose \(\chi\in C_m\) outside that union. For every \(e>1\) dividing \(r\), some prime \(p\mid e\) implies \(C_{me}\subseteq C_{mp}\); hence precisely the \(e=1\) term survives. Its magnitude is \(q^m\), proving sharpness.

**5. Largest multiplier, operator range and stabilizer.** By the triangle inequality \(|\widehat f(\chi)|\le\sum_x f(x)=P_q(n)\), with equality at the trivial character. Fourier diagonalization of convolution gives the singular values, inverse norm, and condition number. The space of functions invariant under translation by \(U_m\) is exactly the Fourier subspace supported on \(C_m\), which equals \(\operatorname{im}T_f\). Finally, a translation \(u\in G\) fixes \(f\) exactly when \(\chi(u)=1\) for every \(\chi\in\operatorname{supp}\widehat f=C_m\). Finite duality identifies this annihilator with \(U_m\), proving the complete stabilizer classification.

## Verification
The included `check_binary.py` constructs the full-period indicator directly from rotation tests and computes its integer Walsh transform by an independent butterfly recursion for all \(2\le n\le15\). It checks the Möbius coefficient formula at every frequency, the complete support, rank, and sharp extreme multipliers. The included `check_palettes.py` independently performs exact tensor-character transforms in the cyclotomic integer rings \(\mathbb Z[\omega_3]\) and \(\mathbb Z[i]\), and a separate tensor transform on the Klein four-group, using direct rotation tests. It checks every frequency for cyclic orders three and four and the Klein four-group through lengths seven and six, respectively. Neither checker uses floating-point Fourier values. These finite tests are checks of the statements and code, **not** substitutes for the all-length proof above.

Illustrative values for \(q=2\):

| \(n\) | \(m=n/\operatorname{rad}(n)\) | Primitive words | Rank | Least positive multiplier |
|---:|---:|---:|---:|---:|
| 4 | 2 | 12 | 4 | 4 |
| 6 | 1 | 54 | 32 | 2 |
| 8 | 4 | 240 | 16 | 16 |
| 9 | 3 | 504 | 64 | 8 |
| 12 | 2 | 4020 | 1024 | 4 |
| 15 | 1 | 32730 | 16384 | 2 |

## Relationship to prior work
The period lattice, primitive-necklace counts, and Möbius inversion are classical; they are not claimed as new. Kopparty–Kumar–Saks (2015) develops indexing methods for necklaces and primitive fundamental periods and uses Möbius inversion (Section 2.2). Álvarez–Becher–Ferrari–Yuhjtman (2016) studies perfect necklaces and positional statistical tests, a different word subfamily and sampling question. Klapper–Goresky–Washington (2000) studies classical one-dimensional Fourier coefficients of an **individual periodic binary sequence** in relation to 2-adic span, not the Boolean-group Fourier transform of the incidence function of **all** primitive words. The contribution assessed here is the combined exact all-frequency support, maximal translation stabilizer, rank, and sharp positive multiplier bound for every finite abelian alphabet and length. Searches found no matching statement; this does not certify historical uniqueness.

## Limitations
No assertion concerns nonabelian alphabets, a single necklace representative per rotation orbit, or a Fourier transform along the position index of one word. The result uses the full uniform unweighted indicator; arbitrary weights on primitive words generally destroy the translation symmetry and spectrum. Historical novelty may be affected by unindexed folklore derivations or Fourier formulations of necklace counting not available in the inspected materials. The exact formula needs no external computation to establish the infinite conclusion, but the independent programs only cover the finite specified ranges.

## References
1. Swastik Kopparty, Mrinal Kumar, and Michael Saks, *Efficient indexing of necklaces and irreducible polynomials over finite fields*, arXiv:1504.00572, first posted 2015-04-02, especially Sections 1, 2.2 and 3. https://arxiv.org/abs/1504.00572
2. Nicolás Álvarez, Verónica Becher, Pablo A. Ferrari, and Sergio A. Yuhjtman, *Perfect Necklaces*, arXiv:1601.07975, first posted 2016-01-29. https://arxiv.org/abs/1601.07975
3. Andrew Klapper, Mark Goresky, and Lawrence Washington, *Fourier Transforms and the 2-adic Span of Periodic Binary Sequences*, IEEE Transactions on Information Theory 46 (2000), 687–691. Author abstract: https://www.cs.engr.uky.edu/~klapper/abs/fourier.html
