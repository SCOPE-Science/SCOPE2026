# Three-marker binary words: exact distinct Lyndon-factor distribution and limit law

## Finding

Let \(0<1\), and for a binary word \(w\) let \(L(w)\) denote the number of **distinct, nonempty contiguous factors** that are Lyndon words (each factor counted once even if it occurs repeatedly). This is not the number of blocks in the Chen–Fox–Lyndon factorization. For every \(a,b,c,d\in\mathbb Z_{\ge0}\), define
\[
w=0^a1\,0^b1\,0^c1\,0^d.
\]
Except for \(w=111\), where \(L(w)=1\), the complete pointwise formula is
\[
\boxed{L(w)=2+\max(a,b,c)+(a-b)_++(b-c)_+
 +(a-\max(b,c))_++\mathbf{1}_{\{c<b\le a\}},}
\]
where \(t_+=\max(0,t)\). The terminal zero gap \(d\) does not affect the value once the word contains a zero.

For \(k\ge0\), let \(A_{k,j}\) be the number of words with exactly three ones, \(k\) zeros, and \(L(w)=j\). Define \(G(z,u)=\sum_{k,j} A_{k,j}z^ku^j\). Then
\[
\boxed{G(z,u)=u-u^2+\frac{B(z,u)}{(1-z)(1-z^3u)},}
\]
where
\[
\begin{aligned}
B(z,u)={}&\frac{u^2}{1-zu^3}
+\frac{z^2u^5}{(1-z^2u^2)(1-zu^3)}
+\frac{z^2u^4}{(1-z^2u^2)(1-zu^3)}\\
&+\frac{zu^4}{(1-z^2u^2)(1-zu^2)}
+\frac{z^2u^3}{(1-z^2u)(1-zu^2)}\\
&+\frac{zu^3}{(1-z^2u^2)(1-zu)}
+\frac{z^3u^4}{(1-z^2u)(1-zu)}.
\end{aligned}
\]
The coefficients of this rational function give the **complete finite-length multiplicity distribution** for every length \(n=k+3\). In particular \(G(z,1)=(1-z)^{-4}\).

For \(W_n\) sampled uniformly from the \(\binom n3\) words of length \(n\) having exactly three ones,
\[
\frac{L(W_n)}n\ \xrightarrow{\mathrm d}\ X,
\qquad
\mathbb E X=\frac{19}{24},\quad
\operatorname{Var}(X)=\frac{563}{2880}>0.
\]
The full law \(X\), not just its moments, is specified as follows. Sample \(J\) uniformly from \(\{1,\ldots,6\}\), independently of \((T,U,V,D)\sim\operatorname{Dirichlet}(1,1,1,1)\). Conditional on \(J=j\), set \(X=T/3+\alpha_jU+\beta_jV\), where
\[
(\alpha_j,\beta_j)_{j=1}^6
=((1,3),(1,3),(1,2),(1/2,2),(1,1),(1/2,1)).
\]
This yields a nondegenerate continuous distribution with support \([0,3]\). The variance of \(L(W_n)/n\) converges to \(563/2880\), not to zero.

## Assumptions and scope

All words are finite, indexed as contiguous strings over the ordered alphabet \(0<1\); the weight is exactly three ones, with \(n\ge3\). A word is Lyndon if and only if it is lexicographically strictly smaller than every nonempty proper suffix. A factor is a contiguous substring, not a subsequence, and factors are counted by distinct values rather than by occurrences. The variables \(z\) and \(u\) are formal generating-function indeterminates. Convergence is as \(n\to\infty\) through positive integers.

## Proof

**1. Classify the Lyndon factors.** A binary Lyndon word longer than one letter must start in \(0\) and end in \(1\). Indeed, a word containing both symbols cannot begin in \(1\), while a word ending in \(0\) is lexicographically greater than the one-letter suffix \(0\). Hence a non-letter Lyndon factor contains exactly one, two or three of the three markers. The single-letter factors are \(1\), and also \(0\) unless \(w=111\).

Those with one marker are precisely \(0^i1\) for \(0\le i\le\max(a,b,c)\), giving \(\max(a,b,c)+1\) distinct factors.

A two-marker Lyndon factor must span the first two markers or the last two. Its form is \(0^i1\,0^j1\), which is Lyndon precisely for \(i>j\). The two spans respectively provide \((a-b)_+\) and \((b-c)_+\) distinct factors. They cannot duplicate one another: for unequal interior gaps their suffix patterns differ, while if \(b=c\), the second span has no eligible value of \(i\).

A three-marker candidate has form \(0^i1\,0^b1\,0^c1\), with \(1\le i\le a\). Suffixes starting with \(1\) are lexicographically larger. Of the suffixes starting in a zero run, the only potentially minimal ones start at the full runs \(0^b\) and \(0^c\), because a proper suffix beginning later in either run has fewer initial zeros and is larger. The candidate is smaller than \(0^c1\) exactly when \(i>c\). It is smaller than \(0^b1\,0^c1\) exactly when \(i>b\), or \(i=b>c\). The resulting count is \((a-\max(b,c))_++\mathbf{1}_{\{c<b\le a\}}\). Adding the disjoint factor types proves the pointwise formula and the \(111\) exception.

**2. Sum the complete distribution.** Partition nonnegative \((a,b,c)\) uniquely into the six (weak/strict) order chambers listed below. Every displayed \(t,x,y\) is a nonnegative integer. The third column is the number of zeros in the first three gaps; the fourth is \(L(w)\) before the \(111\) correction:

| Chamber | Parameterization | \(a+b+c\) | \(L(w)\) |
|---|---|---|---|
| \(a\ge b\ge c\) | \((t+x+y,t+x,t)\) | \(3t+2x+y\) | \(t+2x+3y+2+\mathbf{1}_{\{x>0\}}\) |
| \(a\ge c>b\) | \((t+1+x+y,t,t+1+x)\) | \(3t+2+2x+y\) | \(t+4+2x+3y\) |
| \(b>a\ge c\) | \((t+x,t+1+x+y,t)\) | \(3t+1+2x+y\) | \(t+4+2x+2y\) |
| \(b\ge c>a\) | \((t,t+1+x+y,t+1+x)\) | \(3t+2+2x+y\) | \(t+3+x+2y\) |
| \(c>a\ge b\) | \((t+x,t,t+1+x+y)\) | \(3t+1+2x+y\) | \(t+3+2x+y\) |
| \(c>b>a\) | \((t,t+1+x,t+2+x+y)\) | \(3t+3+2x+y\) | \(t+4+x+y\) |

The terminal gap \(d\) is arbitrary and contributes \((1-z)^{-1}\). Every chamber contributes a geometric product. The first chamber is split into \(x=0\) and \(x\ge1\), yielding the first two terms in \(B\); the other five chambers yield the remaining five. All terms have the shared factor \((1-z^3u)^{-1}\). The exceptional zero-free word \(111\) was provisionally counted as \(u^2\), and replacing that by \(u\) explains the correction \(u-u^2\). This proves the rational generating function. Substituting \(u=1\) simplifies it to \((1-z)^{-4}\), as must be true for weak compositions of the \(n-3\) zeros into four gaps.

**3. Derive the full limit law.** The uniformly selected four-gap vector \((a,b,c,d)/(n-3)\) converges to the uniform Dirichlet law on the three-dimensional simplex; each of the six strict orders of its first three coordinates has probability \(1/6\). Within a chamber, let \(t\) be the smallest of the first three gaps, \(x\) the difference from smallest to middle, and \(y\) the difference from middle to largest, in the chamber's parameterization. Up to bounded strict-order shifts, \(a+b+c+d=3t+2x+y+d\). Thus the rescaled vector \((3t,2x,y,d)/(n-3)\) converges conditionally to \(\operatorname{Dirichlet}(1,1,1,1)\). The six fourth-column formulas have linear leading parts giving the six \((\alpha_j,\beta_j)\) listed in the finding. Their bounded offsets disappear after division by \(n\), proving the distributional convergence.

For a Dirichlet \((1,1,1,1)\) vector, individual means are \(1/4\), diagonal second moments are \(1/10\), and off-diagonal second moments are \(1/20\). Averaging the six component means gives \(19/24\); averaging their second moments gives \(37/45\), hence variance \(37/45-(19/24)^2=563/2880\). Since \(0\le L(W_n)/n\le3+2/n\), all relevant powers are bounded, so first and second moments converge as stated. This finishes the proof.

## Verification

The standalone `verify_lyndon.py` constructs Lyndon factors directly from every binary word of weight three for lengths \(3\) through \(21\), independently expands the stated geometric-series expression, and checks equality of the exact distributions. It checks the generating function against a separate gap enumeration through length \(70\), and recomputes the limit moments using rational arithmetic. Run `python3 verify_lyndon.py` with Python 3 and no extra dependencies. Successful output ends in `VERIFY_OK`. These finite checks corroborate, but do not replace, the proof for every length.

## Relationship to prior work

Saari's *Lyndon Words and Fibonacci Numbers* (first publicly available July 17, 2012, arXiv:1207.4233) establishes general lower bounds for the number of distinct Lyndon factors of Lyndon words and results for Fibonacci words. Glen, Simpson and Smyth's *Counting Lyndon Factors* (first publicly available January 4, 2017, arXiv:1701.00928), particularly Sections 2 and 4, determines the unrestricted maximum and the average over all words on a fixed alphabet. Their Section 2 already implies the familiar ordered-block extremal behavior; no maximum-factor theorem is claimed here as new. Neither inspected text states the **complete fixed-three-one distribution**, the seven-term rational bivariate enumerator, or the conditioned limiting law. These statements are not consequences of a universal maximum or unrestricted average without additional fixed-composition analysis. The proposed contribution is the joint exact distribution and its limit law, not the definition of Lyndon factors or a general maximal-count theorem.

## Limitations

The factor count assumes three ones and \(0<1\); exchanging alphabet order changes what constitutes a Lyndon factor. The limiting variable is conditional on exact weight three, not the unbiased Bernoulli-word law. Literature searching and inspection cannot rule out uncatalogued equivalent specializations. No statement is made about fixed weights four or greater, nor about the number of Lyndon blocks in a Chen–Fox–Lyndon factorization. The finite verification is not itself a proof of the infinite formulas.

## References

1. K. Saari, *Lyndon Words and Fibonacci Numbers*, arXiv:1207.4233, version 1 posted July 17, 2012, https://arxiv.org/abs/1207.4233.
2. A. Glen, J. Simpson and W. F. Smyth, *Counting Lyndon Factors*, arXiv:1701.00928, version 1 posted January 4, 2017, https://arxiv.org/abs/1701.00928. Published in Electronic Journal of Combinatorics 24(3), P3.28 (2017), https://doi.org/10.37236/6915.
3. M. Lothaire, *Combinatorics on Words*, Addison–Wesley, 1983; standard suffix characterization of Lyndon words.
