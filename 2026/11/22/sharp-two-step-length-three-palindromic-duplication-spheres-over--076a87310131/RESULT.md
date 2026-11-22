# Sharp two-step length-three palindromic duplication spheres over fixed ternary alphabets

## Finding
Let \(\Sigma\) be any alphabet of size \(q\ge3\), and let \(n\ge3\). A length-three palindromic duplication copies three consecutive symbols, reverses that copy, and places it immediately after the source block. The second duplication may copy symbols introduced by the first. Write \(D^2_3(x)\) for the set of words obtained from \(x\in\Sigma^n\) by **exactly two sequential** length-three palindromic duplications. Then
\[
\boxed{\max_{x\in\Sigma^n}|D^2_3(x)|=(n-2)(n+1)-\binom{\max\{n-4,0\}}2.}
\]
For \(n\ge4\), this is \((n^2+7n-24)/2\), and at \(n=3\) it is \(4\). An extremizer for every \(n\) and every \(q\ge3\) is the length-\(n\) prefix of the periodic ternary word \(012012012\cdots\). Its complete history-fiber structure is determined: the only collisions are the two orders of duplicating **disjoint original** three-symbol blocks; each such output has exactly two histories, and all other outputs have exactly one.

The significance is the **fixed three-letter alphabet**: in particular, the sharp bound holds for arbitrarily long sources when \(q=3\), rather than needing a source with \(n\) distinct letters.

## Assumptions and scope
Indices are zero-based. For a word \(x\) of length \(N\) and \(0\le i\le N-3\), let
\[
T_i(x)=x[0..i+2]\,\bigl(x[i..i+2]\bigr)^R\,x[i+3..N-1].
\]
Empty suffixes are permitted. Thus
\[
D^2_3(x)=\{T_j(T_i(x)):0\le i\le n-3,\ 0\le j\le n\}.
\]
All \((n-2)(n+1)\) ordered histories are allowed, including nested and overlapping duplications. The word is linear, not circular. There is no complement operation, no restriction on source content, and no asymptotic assumption. The alphabet symbols \(0,1,2\) are three distinct members of \(\Sigma\).

## Proof
**1. A universal upper bound.** There are \(H=(n-2)(n+1)\) ordered histories. If original length-three blocks begin at \(0\le a<b\le n-3\) with \(b-a\ge3\), duplicating them in either order produces the same descendant:
\[
T_{b+3}(T_a(x))=T_a(T_b(x)).
\]
The pairs of histories \((a,b+3)\) and \((b,a)\) are pairwise disjoint as \((a,b)\) varies: their relative second-minus-first displacement is respectively at least \(6\) and at most \(-3\). The number of forced pairs is
\[
P=\#\{(a,b):0\le a<b\le n-3,\ b-a\ge3\}
=\binom{\max\{n-4,0\}}2.
\]
Consequently, every sphere has at most \(H-P\) distinct outputs.

**2. A cyclic three-letter source and its signed-difference signature.** Take \(x_r=r\bmod3\) for \(0\le r<n\). To remove boundary bookkeeping, extend it to \(x_r=r\bmod3\) for every \(r\ge0\). Any finite legal history has the finite resulting word followed by the *same* original periodic tail, so two finite outputs agree if and only if their infinite extensions agree.

For the infinite output \(y\) of a history \((i,j)\), encode the successive differences \((y_{r+1}-y_r)\bmod3\) by the symbols \(+\) for \(1\), \(0\) for \(0\), and \(-\) for \(2\). Outside a finite interval the differences are all \(+\). Define its signature \((\ell,W)\) by taking \(\ell\) to be the first index where the difference is not \(+\), and \(W\) the string from that index through the last non-\(+\) difference, retaining all intermediate \(+\) symbols. Every output begins in symbol \(0\), so \((\ell,W)\) determines the entire infinite output.

Put \(d=j-i\). Directly substituting the reversed three-letter block into the periodic source yields the **complete** signature table below. In the last column \((+)^h\) denotes \(h\) consecutive plus signs; concatenation of the displayed strings is intended.

| Displacement | First defect \(\ell\) | Core \(W\) |
|---|---|---|
| \(d\le-1\) | \(i+d+2\) | `0--0` \((+)^{-d-1}\) `0--0` |
| \(d=0\) | \(i+2\) | `0-----0` |
| \(d=1\) | \(i+2\) | `000-0-0` |
| \(d=2\) | \(i+2\) | `0-0+0+0` |
| \(d=3\) | \(i+2\) | `0--0` |
| \(d=4\) | \(i+2\) | `0--000+0` |
| \(d=5\) | \(i+2\) | `0--0+0-0-` |
| \(d\ge6\) | \(i+2\) | `0--0` \((+)^{d-4}\) `0--0` |

Here is the finite case calculation underpinning the table. After the first operation the output, near its source, is
\[
\cdots x_{i+2}\;x_{i+2}x_{i+1}x_i\;x_{i+3}\cdots,
\]
where \(x_{r+3}=x_r\) and \(x_{r+1}-x_r\equiv1\pmod3\). Its difference word is all \(+\) except for the local string `0--0` starting at position \(i+2\). If \(d<0\), the second copied three-letter block lies entirely before the first insertion, and if \(d\ge6\), entirely after it; both cases give two copies of `0--0`, separated by exactly the number of \(+\) signs in the table. For \(0\le d\le5\), the second block intersects the inserted block or its boundary. Reversing those six possible length-three windows gives, respectively, the six explicit core strings in the table. Every case uses only \(x_{r+3}=x_r\) and the displayed first-step fragment, so no length-dependent assumption enters this calculation.

**3. Complete collision classification.** The six exceptional cores at \(d=0,1,2,3,4,5\) are pairwise distinct and distinct from every two-copy core. Within either generic family, the number of plus signs determines \(d\), and \(\ell\) then determines \(i\); hence histories are unique there. A generic negative displacement and a generic displacement at least six have the same core only when
\[
-d_--1=d_+-4=h\ge2,
\qquad d_-=-h-1,\quad d_+=h+4.
\]
If their first-defect indices agree, their starting positions obey \(i_+=\ell-2\) and \(i_-=\ell+h-1\). Write \(a=\ell-2\), \(b=\ell+h-1\). Then \(b-a=h+1\ge3\), and the two histories are precisely
\[
(i_+,j_+)=(a,b+3),\qquad(i_-,j_-)=(b,a).
\]
These are the forced disjoint-block commuting pairs already counted in Step 1. No third history can produce their signature, and no additional collision exists. Thus the chosen ternary word has exactly \(P\) doubleton history fibers and all remaining fibers singletons, giving \(|D^2_3(x)|=H-P\). Since the three symbols embed into every \(\Sigma\) with \(q\ge3\), the universal upper bound is sharp for all claimed alphabets. \(\square\)

## Verification
Run `python3 checker.py` using Python 3 with no external packages. The verifier implements palindromic duplication directly and independently constructs the signed-difference signature. It exhaustively checks all 29,511 ternary sources of lengths \(3\) through \(9\), separately checks binary maxima through length \(9\), verifies all history fibers on the prescribed periodic ternary source for \(47\) lengths up to \(128\), and tests \(14,190\) signed-difference signatures against the table. The terminal output is preserved in `checker_output.txt`. These are finite checks; the uniform proof consists of the universal pair count and the complete symbolic displacement classification above.

## Relationship to prior work
Zabokritskiy, *Coding for Multiple Reverse-Complement and Palindromic Duplications* (arXiv:2609.00779, first submitted September 1, 2026), Theorem 5.1, gives the same numerical maximum for **even** duplication lengths over all alphabets. Its disjoint-commutation bound is reused in Step 1, but its alternating-source argument does not apply to the odd length three. A separate published mathematical record entitled *Sharp exact-two palindromic-duplication spheres for odd block lengths over large alphabets* (November 8, 2026; identifier `c4b4c103-f5f1-4cb5-b20f-b97eb5828b89`) proves the odd-block maximum when \(q\ge n\), with pairwise distinct original letters. That hypothesis covers the ternary case only when \(n\le3\), whereas this theorem works for \(q=3\) at **every** \(n\), using only three periodic letters.

Lenz, Wachter-Zeh, and Yaakobi (arXiv:1707.00052) classify certain one-step palindromic duplication collisions and sphere sizes, not exact-two PAL3 spheres. Sun and Ge (arXiv:2602.01151) investigate coding constructions for disjoint long duplications and related settings; their theorems do not give this sharp fixed-alphabet two-step maximum. The present result concerns palindromic reversal, not odd-length reverse-complement duplication with a fixed-point-free involution. No assertion of a new *universal upper bound* is made: the new statement is that the existing sharp bound is **attained with only three symbols for length-three duplications**.

## Limitations
The theorem is for exactly two sequential palindromic duplications of **length three** and \(q\ge3\). It does not determine the binary PAL3 maximum in general, the maxima for odd lengths greater than three, the corresponding reverse-complement spheres, or optimal correcting-code sizes. It is not an independent validation. Historical priority is evaluated against the inspected literature and published mathematical records; an unindexed equivalent fixed-alphabet treatment remains possible.

## References
1. A. L. Zabokritskiy, *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779 (v1 September 1, 2026; see Theorem 5.1 in v4). https://arxiv.org/html/2609.00779v4
2. *Sharp exact-two palindromic-duplication spheres for odd block lengths over large alphabets*, mathematical research record dated November 8, 2026, identifier `c4b4c103-f5f1-4cb5-b20f-b97eb5828b89`.
3. A. Lenz, A. Wachter-Zeh, and E. Yaakobi, *Bounds on Codes Correcting Tandem and Palindromic Duplications*, arXiv:1707.00052 (June 30, 2017), Section 3.3. https://arxiv.org/abs/1707.00052
4. Y. Sun and G. Ge, *On the Palindromic/Reverse-Complement Duplication Correcting Codes*, arXiv:2602.01151 (February 1, 2026). https://arxiv.org/html/2602.01151v1
