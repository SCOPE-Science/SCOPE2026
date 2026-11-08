# A sharp border spectrum and limit law for two-marker binary words

## Finding

For every integer \(n\ge 2\), let \(\mathcal W_n\) be the set of binary words of length \(n\) with exactly two occurrences of \(1\). Let \(L(w)\) denote the length of a longest *proper* border, namely a prefix also equal to a suffix, with \(L(w)=0\) when no nonempty proper border exists. The central structural characterization is

\[
L(0^a1\,0^b1\,0^c)=
\begin{cases}
a+c+1,&b\ge\max(a,c),\\
\min(a,c),&b<\max(a,c),
\end{cases}
\quad a,b,c\in\mathbb Z_{\ge0}.
\]

This yields the **complete finite-length border spectrum**. For integers \(0\le t<n\), write \(N_n(t)=\#\{w\in\mathcal W_n:L(w)=t\}\) and put \(m=n-2\). Define

\[
A_n(t)=\begin{cases}
\max\bigl(0,\min(t-1,n-t-1)-\max(0,2t-n)+1\bigr),&t\ge1,\\
0,&t=0,
\end{cases}
\]

and

\[
D_n(t)=\begin{cases}
2\left\lceil\dfrac{m-t}{2}\right\rceil,&0\le3t\le m,\\
2(m-2t)+1,&3t>m\ \text{and}\ 2t\le m,\\
0,&\text{otherwise}.
\end{cases}
\]

Then \(N_n(t)=A_n(t)+D_n(t)\). In particular,

\[
\max_{w\in\mathcal W_n}L(w)=\left\lfloor\frac{2n-1}{3}\right\rfloor.
\]

There is also a compact rational bivariate generating function. With

\[
H(z,u)=\sum_{m\ge0}z^m\!\sum_{a+b+c=m}u^{L(0^a1\,0^b1\,0^c)},
\]

one has \(H(z,u)=H_1(z,u)+H_2(z,u)\), where

\[
H_1(z,u)=\frac{u(1+z^2u)}{(1-z)(1-z^2u)(1-z^3u^2)}
\]

and

\[
\begin{aligned}
H_2(z,u)={}&\frac{2}{1-z}\left(\frac{z}{(1-z)(1-z^2u)}-\frac{z^2}{(1-z^2)(1-z^3u)}\right)\\
&+\frac{1}{1-z}\left(\frac{z^2u}{1-z^2u}-\frac{z^3u}{1-z^3u}\right).
\end{aligned}
\]

If \(W_n\) is uniform on \(\mathcal W_n\), the scaled longest-border length converges in distribution to an absolutely continuous random variable \(Z\):

\[
\frac{L(W_n)}{n}\ \xrightarrow{\ d\ }\ Z,
\qquad
f_Z(x)=\begin{cases}
2,&0\le x\le\frac13,\\
4-6x,&\frac13<x\le\frac23,\\
0,&\text{otherwise}.
\end{cases}
\]

(The values of a density at individual endpoints are immaterial.) More sharply, the local limit is uniform for all integers \(0\le t<n\):

\[
\sup_{0\le t<n}\left|n\,\Pr(L(W_n)=t)-f_Z(t/n)\right|=O(1/n).
\]

Its cumulative distribution is \(F_Z(x)=0\) for \(x<0\), \(F_Z(x)=2x\) for \(0\le x\le1/3\), \(F_Z(x)=4x-3x^2-1/3\) for \(1/3\le x\le2/3\), and \(F_Z(x)=1\) thereafter. The first two moments and variance are

\[
\mathbb E Z=\frac7{27},\qquad \mathbb E Z^2=\frac5{54},\qquad\operatorname{Var}(Z)=\frac{37}{1458}.
\]

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), the word is linear (not circular), and positions are labeled. Exactly two letters are \(1\); the remaining \(n-2\) letters are \(0\). A border is an *exact* prefix-suffix equality, not an Abelian equality. Empty borders contribute length zero; the whole word is not a proper border. Every displayed finite formula is valid at \(n=2\), including consecutive ones and zero-length outer gaps. The limit uses the uniform distribution on all \(\binom n2\) indexed two-one words, not the uniform distribution on necklaces or on gap triples modulo reversal.

## Proof

**1. Complete classification of border types.** Write \(w=0^a1\,0^b1\,0^c\) and \(n=a+b+c+2\). A border with no ones is \(0^t\), with longest such length \(\min(a,c)\). A proper border cannot contain both ones: the internal distance between the first letter of the word and its two marked positions is different in the proper suffix by the positive suffix start offset, so equal two-one prefixes and suffixes would force that offset to be zero. If a border contains one one, its prefix occurrence must contain the first marker and its suffix occurrence the second marker. Equality of the marker offsets forces its length to be \(t=a+c+1\). The prefix excludes the second marker precisely when \(c\le b\), and the suffix excludes the first precisely when \(a\le b\). Thus this one-marker border exists exactly when \(b\ge\max(a,c)\). Its length strictly exceeds \(\min(a,c)\), proving the structural formula.

**2. Finite spectrum.** In the one-marker-border case, \(t=a+c+1\) and \(b=n-t-1\); the admissible value of \(a\) lies in the integer interval \([\max(0,2t-n),\min(t-1,n-t-1)]\). Its cardinality is \(A_n(t)\). In the complementary case, \(t=\min(a,c)\). If \(a<c\), set \(a=t\) and let \(c\) range from \(\max(t+1,\lfloor(m-t)/2\rfloor+1)\) to \(m-t\), because \(b=m-t-c<c\). The case \(c<a\) contributes equally. The diagonal \(a=c=t\) contributes one additional word exactly when \(0\le m-2t<t\). Simplifying these three disjoint cases gives \(D_n(t)\). This proves the exact spectrum and \(\sum_tN_n(t)=\binom n2\). The one-marker case has \(A_n(t)>0\) up to \(\lfloor(2n-1)/3\rfloor\); the zero-only case has \(t\le\lfloor(n-2)/2\rfloor\). The sharp maximum follows.

**3. Generating function.** In the first case, sum the weight \(z^{a+b+c}u^{a+c+1}\) over \(b\ge\max(a,c)\). Summing the geometric tail in \(b\) yields

\[
\frac{u}{1-z}\sum_{a,c\ge0}(zu)^{a+c}z^{\max(a,c)}
=\frac{u(1+z^2u)}{(1-z)(1-z^2u)(1-z^3u^2)}.
\]

For the second case separate \(a<c\), \(c<a\), and \(a=c\). In either off-diagonal case write \(a=t,c=t+d\), \(d\ge1\), and sum over \(0\le b<t+d\). The total off-diagonal contribution is

\[
\frac2{1-z}\left[\frac{z}{(1-z)(1-z^2u)}-\frac{z^2}{(1-z^2)(1-z^3u)}\right].
\]

On the diagonal \(a=c=t\ge1\), sum \(0\le b<t\) to obtain

\[
\frac1{1-z}\left[\frac{z^2u}{1-z^2u}-\frac{z^3u}{1-z^3u}\right].
\]

This proves \(H_1+H_2\). As a check, \(H(z,1)=(1-z)^{-3}\), the generating series for all ordered zero-gap triples.

**4. Uniform scaling limit.** Directly from the exact piecewise integer counts and their floors, for all integers \(0\le t<n\),

\[
N_n(t)=\frac n2f_Z(t/n)+O(1),
\]

with a single absolute error bound independent of \(n,t\). Indeed, before the transition \(t\approx n/3\) the sum of the two case counts is \(n+O(1)\), between \(n/3\) and \(2n/3\) it is \(2n-3t+O(1)\), and thereafter it is zero. Dividing by \(\binom n2\) proves the uniform local limit. Summing these cell probabilities proves weak convergence, with uniform \(O(1/n)\) error for the distribution functions. Integrating \(x f_Z(x)\) and \(x^2f_Z(x)\) over its two intervals yields the stated rational moments and variance.

## Verification

Run `python3 verify.py` from a directory containing the supplied standalone script. It uses only the Python standard library. It computes longest proper borders independently through the KMP prefix function for **all 121,485** two-one words of lengths \(2\) through \(90\), checks the gap characterization, exact distributions, and maxima, independently expands the rational bivariate series through zero-degree \(35\), and checks exact rational moments and selected larger lengths. Its successful output begins with `VERIFY_OK`. The verifier confirms many finite instances; the unlimited claims rely on the four mathematical proof steps above.

## Relationship to prior work

Holub and Shallit, *Periods and borders of random words*, arXiv:1509.05240v1 (first public posting 2015-09-17), analyze maximum border lengths and least periods under *unrestricted*, fixed-alphabet uniform sampling. They obtain bounded limiting mean border length, about \(1.64116\) for a binary alphabet, and general recurrence schemes. The full text, including Sections 2–6, does not evaluate the fixed-weight-two border spectrum, its rational bivariate series, or its macroscopic limit law. Here the fixed-weight sampling gives a qualitatively different linear scale and a piecewise density. The general period-border duality is classical and is not claimed as new.

Harju and Nowotka, *Border Correlation of Binary Words*, TUCS Technical Report 546 (2003), study which cyclic conjugates are bordered and properties of the resulting boolean correlation word; their questions do not resolve exact longest-border lengths in a uniformly sampled fixed-content linear family. Abelian-border enumerations concern equality of symbol counts, not the exact borders studied here. General algorithms for calculating a border are also not the novel contribution. No claim is made about higher Hamming weights or arbitrary probability measures.

## Limitations

Novelty is assessed against the inspected primary literature and searchable mathematical records; an unindexed equivalent specialization may exist. The calculation does not imply a new unrestricted-word border law or a theorem for a positive marker density. No independent expert validation has been performed. Numeric checks only cover the specified finite ranges, not the infinite theorem.

## References

- Š. Holub and J. Shallit, *Periods and borders of random words*, arXiv:1509.05240v1 (2015-09-17), https://arxiv.org/html/1509.05240v1 ; STACS 2016, LIPIcs 47, Article 44. MSC2020: 68R15 (as recorded on arXiv).
- T. Harju and D. Nowotka, *Border Correlation of Binary Words*, TUCS Technical Report 546 (August 2003), https://citeseerx.ist.psu.edu/document?doi=912065a268d68bfb1e44494181f636a0c491d9c2&repid=rep1&type=pdf ; journal version, J. Combin. Theory Ser. A 108 (2004), 331–341.
- M. Christodoulakis, M. Christou, M. Crochemore, C. S. Iliopoulos, *Abelian borders in binary words*, Discrete Applied Mathematics 171 (2014), 141–146, https://doi.org/10.1016/j.dam.2014.02.012 (conceptually related but with a different equality notion).
