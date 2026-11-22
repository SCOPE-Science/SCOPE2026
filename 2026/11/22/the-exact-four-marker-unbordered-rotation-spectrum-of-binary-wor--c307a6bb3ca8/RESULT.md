# The exact four-marker unbordered-rotation spectrum of binary words

## Finding

For every integer \(n\ge4\), consider the \(\binom n4\) indexed binary words of length \(n\) having exactly four occurrences of `1`. A rotation is *unbordered* if no nonempty proper prefix is also a suffix. Write \(u(w)\) for the number of unbordered rotations, counting starting positions (not just distinct words). Then \(u(w)\) belongs exactly to the set \(\{0,2,3,4\}\) as \(n\) varies; in particular, one unbordered rotation is impossible.

Let \(C_j(n)\) be the number of such indexed words with \(u(w)=j\), and define
\[
G_j(z)=\sum_{s\ge0}\frac{4C_j(s+4)}{s+4}z^s,\qquad D(z)=\prod_{h=1}^4(1-z^h).
\]
All four generating functions are **exactly** \(G_j(z)=P_j(z)/D(z)\), where
\[
\begin{aligned}
P_0(z)&=1-z+z^2-2z^3+z^4-z^5+z^6,\\
P_2(z)&=4z+4z^2-8z^4-8z^5+8z^6,\\
P_3(z)&=8z^3+8z^4+8z^5-24z^6,\\
P_4(z)&=4z^4+4z^5+16z^6.
\end{aligned}
\]
In particular, \(G_0(z)=(1-z^2)^{-2}\), so \(C_0(n)=\binom{n/2}{2}\) for even \(n\) and \(C_0(n)=0\) for odd \(n\). As \(n\to\infty\),
\[
C_2(n)=\frac{n^3}{16}+O(n^2),\quad C_3(n)=\frac{n^3}{4}+O(n^2),\quad C_4(n)=\binom n4-O(n^3).
\]
Thus a uniformly sampled weight-four binary word has four unbordered rotations with probability tending to one.

## Assumptions and scope

The alphabet is the labeled binary alphabet \(\{0,1\}\). The length is any integer \(n\ge4\). Every word is indexed, not quotiented by rotation, reversal, or complement. A word's \(n\) cyclic starting positions are tested separately, including when its least period is smaller than \(n\). A border must be nonempty and strictly shorter than the word. Cyclic zeros between successive ones are encoded by \(g=(a,b,c,d)\in\mathbb Z_{\ge0}^4\), with \(a+b+c+d=n-4\), and rotation of the gap tuple does not change \(u(w)\).

The explicit **gap law** is
\[
\begin{aligned}
u(g)={}&\sum_{i=0}^3[\,g_i\ne g_{i+1}\,]
-2[\,a=c<\min(b,d)\,]\\
&-2[\,b=d<\min(a,c)\,]
-2[\,a=c,\ b=d,\ a\ne b\,],
\end{aligned}
\]
where \(g_4=g_0\) and square brackets denote indicator functions. The extra terms expose the first nonlocal opposite-gap obstruction beyond the local adjacent-gap rule for three ones.

## Proof

**1. Characterize every possibly unbordered rotation.** A rotation beginning and ending with the same symbol has a one-letter border. The other starting positions occur only at a `1` immediately before a zero run and at the first zero of a nonempty run; these are at most eight starts, associated with the four cyclic gap choices. For the cyclic word written as
\(W=1\,0^a1\,0^b1\,0^c1\,0^d\), its `1`-initial rotation is unbordered precisely when
\[
a<d\quad\text{and}\quad\neg(a=c\text{ and }b\ge d).
\]
Indeed, if \(a\ge d\), the suffix \(1\,0^d\) is a proper prefix, including \(d=0\). If \(a<d\), any common nonempty prefix-suffix must start at one of the other three `1` positions: the last is already excluded, the second would force \(a=b=c\ge d\), and the third matches precisely for \(a=c\) and \(b\ge d\). No other suffix can match, since every common border must begin at `1`.

The companion zero-initial candidate is
\(V=0^a1\,0^b1\,0^c1\,0^d1\) (only defined for \(a>0\)). It is unbordered precisely when
\[
a>d\quad\text{and}\quad\neg(b=d\text{ and }c\ge a).
\]
If \(a\le d\), the suffix \(0^a1\) is a border; once \(a>d\), suffixes ending at the final `1` and beginning earlier can match only when \(b=d\) and \(c\ge a\). Any suffix beginning farther back would force the contradictory inequalities \(d\ge a\). These arguments include zero-length intervening runs and periodic words.

**2. Four-gap formula.** For each of the four cyclic permutations \((a,b,c,d)\) of \(g\), add the indicators of the two mutually exclusive tests above. The leading terms count strict inequalities \(a<d\) and \(a>d\), hence \(\sum[g_i\ne g_{i+1}]\). Pairing equal-opposite-gap exceptions gives precisely the three subtractions in the displayed gap law. The formula also proves that \(u\) depends only on the relative weak ordering of the four gaps.

**3. Exact rational enumeration by 75 weak orders.** An ordered weak order of the four labeled gaps is a surjection \(r:\{0,1,2,3\}\to\{0,\dots,k-1\}\) for \(1\le k\le4\). There are \(\sum_{k=1}^4 k!S(4,k)=75\) such patterns. If \(m_t\) is the number of gaps of rank \(t\), every nonnegative quadruple realizing this pattern is uniquely determined by an initial nonnegative height and \(k-1\) strictly positive increments. Its weight series is
\[
\frac{z^{\sum_{t=0}^{k-1}t m_t}}{\prod_{t=0}^{k-1}(1-z^{m_t+\dots+m_{k-1}})}.
\]
Every factor in its denominator occurs in \(D(z)\), since the suffix sums are distinct integers from one to four. Allocate each pattern to its value of \(u\) from Step 2, multiply each contribution by the missing factors of \(D(z)\), and add the resulting integer polynomials. The exhaustive 75-case integer computation in `verify_rational.py` gives, exactly and without floating-point arithmetic, the four numerators \(P_0,P_2,P_3,P_4\) displayed above. The case counts are 3, 16, 24, and 32, respectively, and the numerator sum equals \(D(z)/(1-z)^4\). This finite algebraic certificate covers all nonnegative quadruples because weak-order patterns partition them without omission or duplication.

**4. Transfer to indexed words.** For \(n=s+4\), choosing an indexed word with four ones and distinguishing one of those ones produces \(4C_j(n)\) objects. Choosing a location among \(n\) indices for the distinguished one and an ordered quadruple of zero gaps with sum \(s\) produces the same objects, so \(4C_j(n)=n[z^s]G_j(z)\). This proves every formula. Cancellation yields the stated \(G_0\). Laurent expansions at \(z=1\), with all other poles of smaller order, give the asymptotic estimates. Finally, the coefficient data show witnesses for all four values: \(n=4\) for zero, \(n=5\) for two, \(n=7\) for three, and \(n=8\) for four.

## Verification

Run `python3 verify_rational.py` for the 75-pattern exact polynomial identity and partition check. Run `python3 verify_words.py` for an independent direct comparison against all nonempty proper prefix-suffix pairs of each indexed weight-four word for every \(4\le n\le20\); it also checks 2401 larger-gap test tuples and agrees with all exact generating-function coefficients through that range. At \(n=8\), the distribution \((C_0,C_2,C_3,C_4)\) is \((6,24,32,8)\); at \(n=20\), it is \((45,500,1240,3060)\). Exhaustive finite tests corroborate but do not replace Steps 1–4, which prove the identities for every length.

## Relationship to prior work

Harju and Nowotka introduced the border-correlation function and proved general restrictions on unbordered conjugates. Holub and Müller characterize binary words with exactly two unbordered conjugates. These results concern arbitrary composition or one specific fiber; they do not state the complete four-one profile \(C_j(n)\), its all-length rational generating functions, or the opposite-gap correction. The general maximum over all binary compositions recorded in OEIS A321162 is not a fixed-composition spectrum. Related three-one gap classifications have a local adjacent-gap form, but the displayed four-one law has two-opposite-gap effects. The contribution claimed here is the complete four-one enumeration, not the general notion of a border, a conjugate, or weak-order rational enumeration.

## Limitations

The result is limited to exactly four occurrences of one labeled symbol, and is an enumerative theorem, not a reconstruction or coding-capacity bound. Originality was checked against accessible literature and indexed related mathematical statements, but an uncatalogued equivalent historical computation may exist. No external independent mathematical audit has been performed. The algebraic certificate is elementary and finite; no claim is made for higher fixed weights.

## References

- T. Harju and D. Nowotka, *Border correlation of binary words*, Journal of Combinatorial Theory A 108 (2004), 331–341, DOI: https://doi.org/10.1016/j.jcta.2004.07.009 (technical-report version, 2003).
- Š. Holub and M. Müller, *Fully bordered words*, arXiv:1504.02222v1, first public version April 9, 2015, https://arxiv.org/abs/1504.02222.
- OEIS A321162, *Maximum number of unbordered conjugates for a binary word of length n*, https://oeis.org/A321162.
