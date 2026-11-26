# Exact weight-resolved \(2\)-binomial spectra of the Cantor word at triadic lengths

## Finding

Let \(C=c_0c_1\cdots\) be the binary Cantor word, the fixed point beginning with \(1\) of \(\mu(1)=101\), \(\mu(0)=000\). For every integer \(k\geq0\), let \(n=3^k\), \(m=2^k\), and let \(b_C^{(2)}(n)\) be the number of equivalence classes of length-\(n\) contiguous factors under equality of all *scattered* subsequence counts of lengths at most two.

The following is an **exact arithmetic description of every class at every triadic length**. For \(0\leq j<m\), write the binary digits of \(j\) as \(\varepsilon_r(j)\in\{0,1\}\), and set
\[
 p_j=2\sum_{r=0}^{k-1}\varepsilon_r(j)3^r,\qquad U_w=\sum_{j=0}^{w-1}p_j\quad(1\leq w<m).
\]
For each \(1\leq w<m\), put \(a_w=p_{w-1}+1\), \(d_w=p_w\), and define
\[
 A_w=\{U_w+w(n-t):t\in\mathbb Z,\ a_w\leq t\leq d_w\},\qquad
 B_w=\{w(n-1)-s:s\in A_w\}.
\]
The complete \(2\)-binomial equivalence-class spectrum consists of the two endpoint profiles \((0,0)\) and \((m,m(n-1)/2)\), and exactly the profiles \((w,s)\) for \(1\leq w<m\) and \(s\in A_w\cup B_w\). Here the second coordinate is the sum of zero-based positions occupied by ones in the factor. The endpoint profile with weight \(m\) has an integer second coordinate because the Cantor block is palindromic.

Consequently, if
\[
 h_w=n+1+\frac{2U_w}{w},\qquad
 I_w=\begin{cases}
 0,&h_w\notin\mathbb Z,\\
 \max\bigl\{0,\ \min(d_w,h_w-a_w)-\max(a_w,h_w-d_w)+1\bigr\},&h_w\in\mathbb Z,
 \end{cases}
\]
then the number of classes of weight \(w\) is precisely
\[
 2\bigl(3^{\nu_2(w)}+1\bigr)-I_w\qquad(1\leq w<m),
\]
and the total satisfies the **exact formula for every integer \(k\geq0\)**
\[
 \boxed{b_C^{(2)}(3^k)=2\cdot3^k-\sum_{w=1}^{2^k-1}I_w.}
\]
It involves only explicit finite arithmetic on the binary digits of indices below \(2^k\), not enumeration of all length-\(3^k\) factors. The sum is empty when \(k=0\).

For example, direct exact evaluation gives the values \(2,5,17,50,154,466,1402,4210,12634,37906,113722,341170\) at levels \(k=0,1,\ldots,11\). These finite evaluations are not used to justify the theorem for arbitrary \(k\).

## Assumptions and scope

The Cantor word is indexed from zero; its ones occur exactly at indices whose base-three expansions use only digits zero and two. A *factor* is contiguous; a *scattered subsequence* retains order but need not occupy consecutive positions. Two factors of equal length are \(2\)-binomial equivalent if the counts of each of \(0,1,00,01,10,11\) as scattered subsequences agree. This statement concerns precisely lengths \(3^k\) and all integers \(k\geq0\); it asserts neither an arbitrary-length formula nor the simpler closed expression suggested by its initial values.

The displayed descriptions of \(A_w\), \(B_w\), and \(I_w\) are finite formulas, not recurrences dependent on the infinite word. In particular the summands \(U_w\) can be evaluated without enumerating \(p_0,\dots,p_{w-1}\) using
\[
 U_w=2\sum_{r=0}^{k-1}3^r\left(2^r\left\lfloor\frac{w}{2^{r+1}}\right\rfloor+\max\{0,(w\bmod2^{r+1})-2^r\}\right).
\]

## Proof

**1. Finite-block factor covering.** Put \(D_k=\mu^k(1)\), \(Z_k=0^{3^k}\). Since \(C=\mu^k(C)\), it is a concatenation of length-\(n\) blocks \(D_k\) and \(Z_k\), whose adjacency pattern is the original Cantor word. The only adjacent symbol pairs in \(C\) are \(00\), \(01\), and \(10\), and all three occur. A length-\(n\) factor meets at most two adjacent aligned length-\(n\) blocks. In a \(00\) pair it is all zero, in a \(01\) pair it is \(0^{n-t}\operatorname{pref}_t(D_k)\), and in a \(10\) pair it is \(\operatorname{suff}_t(D_k)0^{n-t}\), for some integer \(0\leq t\leq n\). Conversely, each such cut occurs because the three pairs occur. The word \(D_k\) is palindromic: both images \(101\) and \(000\) are palindromes, and reversing the image of a palindrome preserves it. Therefore the two nonzero-bearing families are reversals of each other.

**2. Classifying the fixed-weight cuts.** The ones of \(D_k\) are at the positions \(p_j\): each iteration replaces a one at \(p\) by ones at \(3p\) and \(3p+2\), yielding the base-three digits \(0,2\). In increasing order these indices are obtained by replacing the binary digits of \(j\) by twice those digits in base three. Their number is \(m\). For each \(1\leq w<m\), the prefix of length \(t\) has exactly \(w\) ones if and only if \(p_{w-1}+1\leq t\leq p_w\). Within this interval the sum of original positions of these ones is \(U_w\), so the padded prefix has position sum \(U_w+w(n-t)\). Its reverse has sum \(w(n-1)-[U_w+w(n-t)]\). Therefore the complete profile set for weight \(w\) is exactly \(A_w\cup B_w\). A factor has weight zero only when it is all zero, giving one class. Weight \(m\) requires the entire \(D_k\), giving the other endpoint class.

**3. Why two statistics suffice.** Let \(W\) be the number of ones in an arbitrary binary word of length \(n\), and let \(S\) be the sum of their zero-based positions. The scattered \(01\) count is \(S-\binom{W}{2}\): a one at position \(j\), the \(i\)-th one starting at \(i=0\), has \(j-i\) preceding zeros. Counts of \(00\) and \(11\) are \(\binom{n-W}{2}\) and \(\binom W2\), and the scattered \(10\) count equals \(W(n-W)\) minus the \(01\) count. Thus equality of all scattered counts of lengths one and two is equivalent, at fixed \(n\), to equality of \((W,S)\). The profile enumeration above is therefore exactly the \(2\)-binomial class enumeration.

**4. Counting overlaps.** For weight \(w\), consecutive values of \(U_w+w(n-t)\) differ by \(w\), so \(|A_w|=|B_w|=p_w-p_{w-1}\). A profile belongs to both precisely when some integers \(t,t'\in[a_w,d_w]\) satisfy
\[
 U_w+w(n-t)=w(n-1)-U_w-w(n-t').
\]
After rearranging, \(t+t'=h_w\). If \(h_w\) is not an integer, there are no solutions. If it is, admissible \(t\) lie in the intersection of integer intervals \([a_w,d_w]\) and \([h_w-d_w,h_w-a_w]\); its cardinality is exactly \(I_w\) as displayed. Hence the class count of this weight is \(2(p_w-p_{w-1})-I_w\).

**5. Explicit gaps and total.** Let \(r=\nu_2(w)\). When adding one to the binary expansion of \(w-1\), exactly \(r\) trailing ones turn to zero and bit \(r\) turns to one. Consequently,
\[
 p_w-p_{w-1}=2\cdot3^r-2\sum_{j=0}^{r-1}3^j=3^r+1.
\]
Summing \(p_w-p_{w-1}\) over \(1\leq w<m\) telescopes to \(p_{m-1}-p_0=n-1\). The two endpoint classes together with all intermediate weight classes therefore yield \(2+2(n-1)-\sum I_w=2n-\sum I_w\). This establishes both the full weight-resolved profile and the total for all \(k\geq0\). The floor-and-remainder expression for \(U_w\) follows by counting, separately for each bit position \(r\), the numbers \(0\leq j<w\) having bit \(r\) equal to one. \(\square\)

## Verification

The accompanying standalone Python program `verify.py` evaluates the integer formulas, without floating-point arithmetic, for all levels \(0\leq k\leq11\). It also independently constructs the entire prefix/reversal factor families and compares **sets** of \((W,S)\) profiles against a rolling direct scan of the generated Cantor-word prefix, at every level \(0\leq k\leq7\). The executed program returned `VERIFY_OK`. Run `python3 verify.py` in the directory containing the script.

The proof, especially finite-block completeness and the \(01\)-count identity, applies to all \(k\); the finite checks neither establish nor substitute for infinite validity.

## Relationship to prior work

Rigo and Salimov introduced binomial complexity as a refinement of ordinary abelian equivalence, and computed it for Sturmian and Parikh-constant morphic words (2013, extended 2015). The Cantor substitution is **not** Parikh-constant: its images contain respectively two and zero ones. Their general binary bounds do not supply the exact Cantor triadic-weight profile.

Chen, Lü, and Wu (2017) studied the **contiguous** \(k\)-abelian complexity of the same Cantor word and proved regularity properties. The present scattered-subsequence equivalence is distinct: the count of contiguous adjacent pairs does not determine the weighted sum of one positions. As a concrete check, the length-27 Cantor factors `000101000000000101000101000` and `001010000000001010001010000` have the same one-count, first and last symbol, and number of adjacent \(11\) occurrences, yet their position sums are different (84 and 78). Thus the published contiguous-spectrum results do not immediately determine the present spectrum.

## Limitations

The cardinality formula is an **explicit digit-arithmetic sum with \(2^k-1\) terms**, not a proved elementary closed expression without summation. The observed numerical pattern in the first twelve levels is not asserted to continue. No assertion is made for lengths not of the form \(3^k\). The originality comparison covers the identified primary literature and searchable records; an unindexed equivalent computation or a different stronger theorem could still exist. No independent scientific audit has been performed.

## References

1. M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, WORDS 2013, LNCS 8079, 217–228; public full-text preprint at https://orbi.uliege.be/handle/2268/149313 (available 2013-05-27).
2. M. Rigo and P. Salimov, *Another generalization of abelian equivalence: binomial complexity of infinite words*, Theoretical Computer Science 601 (2015), 47–57; https://orbi.uliege.be/bitstream/2268/178703/1/binomial_TCS_final.pdf .
3. J. Chen, X. Lü, and W. Wu, *On the k-abelian complexity of the Cantor sequence*, arXiv:1703.04063 (first posted 2017-03-12); https://arxiv.org/pdf/1703.04063 .
