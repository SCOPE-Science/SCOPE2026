# Three-marker rigidity for substring-composition reconstruction

## Finding

For every integer \(n\geq 3\), consider a binary word \(w\in\{0,1\}^n\) containing exactly three ones. For \(j\in\{0,1,2,3\}\), define
\[
Q_j(w;t)=\sum_{\ell=1}^n c_{j,\ell}(w)t^\ell,
\qquad
c_{j,\ell}(w)=\#\{i:1\le i\le n-\ell+1,\ |w_i\cdots w_{i+\ell-1}|_1=j\}.
\]
Thus \(c_{j,\ell}\) counts contiguous factors *with multiplicity*, classified by their length and number of ones.

**Theorem.** If \(w,v\in\{0,1\}^n\) each contain exactly three ones and
\[
Q_j(w;t)=Q_j(v;t)\qquad(j\in\{0,2,3\}),
\]
then \(v=w\) or \(v=w^{\mathrm{rev}}\). Consequently, the full substring-composition multiset determines every binary word with three ones up to reversal, *even when all observations of factors with exactly one one are discarded*.

The exact number of distinct full substring-composition multisets of length-\(n\) weight-three binary words is
\[
R_3(n)=\frac12\left(\binom n3+\mathbf 1_{\{n\text{ odd}\}}\frac{n-1}{2}\right)\quad(n\ge3).
\]
The Hamming-weight threshold is sharp: the distinct nonreverse length-eight words `01001101` and `01101001`, each with four ones, have identical full substring-composition multisets. This particular witness was already exhibited by Acharya and collaborators; only the universal three-marker rigidity and its selective-channel strengthening are advanced as new here.

## Assumptions and scope

Words are linear and indexed, not cyclic. All nonempty *contiguous* factors are counted including repeated occurrences. The alphabet is exactly \(\{0,1\}\), and the theorem concerns exact Hamming weight three. The entire observation includes the length, which is also the unique length of the longest factor; the shorter retained observation is specifically the collection of the three polynomials \(Q_0,Q_2,Q_3\). Reversal is intrinsically unobservable. No noise, erasures within a retained channel, unknown alphabet relabeling, or scattered subsequences are asserted.

## Proof

Every weight-three word has a unique zero-gap representation
\[
w=0^a1\,0^b1\,0^c1\,0^d,
\qquad a,b,c,d\in\mathbb Z_{\ge0},\quad a+b+c+d=n-3.
\]
Write \(G_r(t)=1+t+\cdots+t^r\) for \(r\ge0\). Enumerating factors containing respectively zero, two, and three ones yields the exact polynomial identities
\[
Q_0(w;t)=\sum_{g\in\{a,b,c,d\}}\sum_{\ell=1}^{g}(g-\ell+1)t^\ell,
\]
\[
Q_2(w;t)=t^{b+2}G_a(t)G_c(t)+t^{c+2}G_b(t)G_d(t),
\qquad
Q_3(w;t)=t^{b+c+3}G_a(t)G_d(t).
\]
Here the braces in the first sum denote the four-element *multiset* of gaps. For instance, a factor containing the first two ones but not the third may extend by any of \(0,\ldots,a\) zeros to its left and any of \(0,\ldots,c\) zeros to its right, proving the first summand in \(Q_2\). Every factor containing all three ones may extend by \(0,\ldots,a\) zeros to its left and \(0,\ldots,d\) zeros to its right, proving the \(Q_3\) identity. All other identities follow by the same exhaustive factor classification.

First, let \(u_\ell=[t^\ell]Q_0(w;t)\) for positive integers \(\ell\), setting \(u_\ell=0\) above the degree. Since
\[
u_\ell=\sum_{g\in\{a,b,c,d\}}\max(0,g-\ell+1),
\qquad
u_\ell-2u_{\ell+1}+u_{\ell+2}=\#\{g\in\{a,b,c,d\}:g=\ell\},
\]
all positive gap multiplicities are determined. The number of zero gaps is four minus the total positive-gap multiplicity. Hence \(Q_0\) recovers the entire unordered multiset \(\{a,b,c,d\}\), including zeros.

Second, \(Q_3\) is never zero. Its least exponent is \(m=b+c+3\), and its greatest is \(n\). Removing the smallest power produces \(G_a(t)G_d(t)\), whose degree is \(a+d=n-m\) and whose value at \(t=1\) is \((a+1)(d+1)\). Consequently \(Q_3\) determines the unordered endpoint pair \(\{a,d\}\): its two entries are the roots of the quadratic with their known sum \(a+d\) and known product \((a+1)(d+1)-(a+d)-1=ad\). Subtracting this pair from the four-gap multiset determines the unordered internal pair \(\{b,c\}\).

It remains only to decide how the internal pair is oriented relative to the endpoint pair. Up to simultaneous reversal, there are at most two possibilities, \((a,b,c,d)\) and \((a,c,b,d)\), after fixing one orientation of the endpoint pair. Their difference in the second observation is
\[
\begin{aligned}
Q_2(a,b,c,d;t)-Q_2(a,c,b,d;t)
 &=\bigl(G_a(t)-G_d(t)\bigr)\bigl(t^{b+2}G_c(t)-t^{c+2}G_b(t)\bigr)\\
 &=\frac{t^2\bigl(t^{d+1}-t^{a+1}\bigr)\bigl(t^b-t^c\bigr)}{(1-t)^2}.
\end{aligned}
\]
This polynomial is nonzero precisely when \(a\ne d\) and \(b\ne c\), because the integral polynomial ring has no zero divisors. When either equality holds, the two proposed tuples already represent the same word or reversals of one another. Thus \(Q_2\) distinguishes every pair of genuinely distinct reversal classes. This completes reconstruction for every \(n\ge3\), including zero-length internal and endpoint gaps.

To count full multispectra, observe that the proven equivalence classes are exactly reversal orbits of the \(\binom n3\) weight-three words. A palindrome of weight three must have odd length, its central bit must be one, and exactly one of the \((n-1)/2\) mirror pairs must be occupied by ones. Hence the number of self-reversing words is \((n-1)/2\) for odd \(n\), and zero otherwise. Burnside's orbit formula yields \(R_3(n)\).

Finally, direct substring counting gives the same composition profile for the known weight-four witness pair `01001101` and `01101001`, which are not reversals. This proves sharpness in the allowed number of ones (though not any claim about larger alphabets).

## Verification

Run `python verify.py` using Python 3 and no third-party packages. The replayed checks are: exact \(Q_0,Q_2,Q_3\) identities for all 1,820 zero-gap quadruples of total gap size at most 12; independent complete substring enumeration of 17,550 indexed weight-three words of lengths 3 through 26, checking every fiber and the orbit formula; a 4,096-case independent test of the \(Q_2\) orientation criterion for gap entries 0 through 7; and full equality of the weight-four counterexample spectra. Successful execution prints `VERIFY_OK`. These calculations check the implementation and illustrate boundary cases; the polynomial and orbit arguments above are the all-length proof.

## Relationship to prior work

Acharya, Das, Milenkovic, Orlitsky and Pan developed substring-composition reconstruction and polynomial factorization methods, proved full reconstruction at specified blocklengths, and explicitly gave the length-eight four-one collision. That collision is prior work, not a new contribution. Their published results do not state universal fixed-weight-three reconstruction for all blocklengths, nor recovery from only the zero-, two- and three-one channels. Gupta and Mahdavifar use gap vectors and algebraic reconstruction algorithms for other code families; Ye and Elishco study partial observations, mostly prefix/suffix compositions and error-correcting constructions. Those general frameworks motivate the question but no inspected statement entails this particular all-length low-weight claim without a separate argument.

## Limitations

The uniqueness theorem applies only to exact weight-three binary words; reconstruction without knowing the word weight or from a partial selection of lengths is not established. The weight-four witness demonstrates that a direct universal extension is false. The example at weight four is published, and potential unindexed equivalent formulations of the three-marker theorem remain an originality risk. Independent validation has not been performed.

## References

- J. Acharya, H. Das, O. Milenkovic, A. Orlitsky and S. Pan, *String Reconstruction from Substring Compositions*, arXiv:1403.2439 (initial public version 2014-03-10), https://arxiv.org/abs/1403.2439; SIAM Journal on Discrete Mathematics 29 (2015), 1340–1371, https://doi.org/10.1137/140962486.
- U. Gupta and H. Mahdavifar, *A New Algebraic Approach for String Reconstruction from Substring Compositions*, arXiv:2201.09955 (2022), https://arxiv.org/abs/2201.09955.
- Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963 (2022), https://arxiv.org/html/2208.14963v2.
