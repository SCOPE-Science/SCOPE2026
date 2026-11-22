# Sharp block-universality threshold for integer parts of irrational polynomials

## Finding

Let \(d\ge1\) and \(m\ge2\) be integers, and let
\[
P(X)=\alpha X^d+\sum_{h=0}^{d-1}\beta_hX^h,
\qquad \alpha\in\mathbb R\setminus\mathbb Q,
\quad \beta_h\in\mathbb R.
\]
For \(n\ge0\) put \(a_n=\lfloor P(n)\rfloor\pmod m\), represented by a letter in \(\{0,\ldots,m-1\}\). Every block of length \(d\) has limiting frequency \(m^{-d}\). The precise number of length-\(d+1\) blocks that occur is
\[
\boxed{\ m^d\min\{m,2^d\}\ }.
\]
Every occurring block has strictly positive natural frequency, so **all** length-\(d+1\) blocks occur if and only if \(m\le 2^d\). These statements hold independently of the lower coefficients of \(P\).

Here is the complete frequency formula. Put
\[
 w_i=(-1)^{d-1-i}\binom di,\quad v_i=\binom di\ (0\le i<d),
 \quad s=2^{d-1}-1,\quad \theta=d!\alpha,
\]
and define the piecewise-polynomial cumulative distribution function
\[
 H_d(z)=\frac{1}{d!\prod_{i=0}^{d-1}v_i}
 \sum_{J\subseteq\{0,\ldots,d-1\}}
 (-1)^{|J|}\left(z-\sum_{i\in J}v_i\right)_+^d,
 \quad y_+=\max\{y,0\}.
\]
For any prescribed letters \(A_0,\ldots,A_d\), set
\[
 r\equiv A_d-\sum_{i=0}^{d-1}w_iA_i\pmod m.
\]
Then the frequency of that block is exactly
\[
\boxed{
 \frac1{m^d}\sum_{\substack{j\in\mathbb Z\\j\equiv r\pmod m}}
 \left[H_d(j+1-\theta+s)-H_d(j-\theta+s)\right].
}
\]
Only \(2^d\) consecutive integers \(j\) can make a nonzero contribution. More explicitly, if \(q=\lfloor\theta\rfloor\), the contributions are strictly positive exactly for
\[
 q-(2^{d-1}-1)\le j\le q+2^{d-1}.
\]
Thus the formula is finite, and its dependence on the polynomial is only through \(d!\alpha\) modulo \(m\).

## Assumptions and scope

The leading coefficient is irrational; all lower coefficients are arbitrary real numbers. The result concerns natural frequencies along the nonnegative integers and fixed modulus \(m\). It neither asserts uniform finite-prefix discrepancy bounds nor extends the threshold to rational leading coefficients. The theorem includes degree one (the familiar two-increment phenomenon) as well as all higher degrees.

## Proof

**1. Joint equidistribution of the first \(d\) values.** Fix a nonzero integer vector \(\mathbf h=(h_0,\ldots,h_{d-1})\). The Vandermonde matrix at \(0,1,\ldots,d-1\) is invertible, hence there exists a least \(s\in\{0,\ldots,d-1\}\) such that \(\sum_{i=0}^{d-1}h_i i^s\ne0\), and all lower moments vanish. The coefficient of \(n^{d-s}\) in
\[
 \sum_{i=0}^{d-1}h_iP(n+i)
\]
is \(\alpha\binom ds\sum_i h_i i^s\); the lower-degree terms of \(P\) have degree at most \(d-1-s\) after these moment cancellations. This coefficient is irrational, and \(d-s\ge1\). By Weyl's polynomial equidistribution theorem, the displayed sum divided by \(m\) is uniformly distributed modulo one. Weyl's criterion for vectors therefore makes
\[
 (P(n),P(n+1),\ldots,P(n+d-1))\pmod m
\]
uniformly distributed on \([0,m)^d\). In particular, the first \(d\) residue letters are uniform, and conditional on any prescribed such letters, the fractional parts \(x_i=\{P(n+i)\}\) range uniformly over \([0,1)^d\). Boundaries have zero frequency.

**2. Finite differences force the last letter.** The exact degree-\(d\) finite-difference identity gives
\[
 P(n+d)=\theta+\sum_{i=0}^{d-1}w_iP(n+i).
\]
On separating integer and fractional parts, the last residue is the residue of
\[
 \sum_{i=0}^{d-1}w_iA_i+J,\qquad
 J=\left\lfloor\theta+\sum_{i=0}^{d-1}w_ix_i\right\rfloor.
\]
There are \(2^{d-1}-1\) units of negative weights, and all absolute weights add up to \(2^d-1\). Reflecting each negatively weighted uniform variable replaces the inner sum in \(J\) by
\[
 -s+T,\qquad T=\sum_{i=0}^{d-1}v_iU_i,
\]
where the \(U_i\) are independent uniform variables on \([0,1)\). The distribution of \(T\) has full, strictly positive density in \((0,2^d-1)\). Inclusion-exclusion on the defining rectangular box gives its cumulative distribution \(H_d\) as above.

**3. Exact support and frequency.** Writing \(\theta=q+t\), where \(0<t<1\), yields
\[
 J=q-s+\lfloor t+T\rfloor.
\]
Since \(T\) has full support from zero to \(2^d-1\), the integer \(\lfloor t+T\rfloor\) has exactly the values \(0,1,\ldots,2^d-1\), each with positive probability. Consequently \(J\) has the \(2^d\) successive values claimed. For any first \(d\) letters, precisely \(\min(m,2^d)\) last letters are possible modulo \(m\), and all have positive frequency. There are \(m^d\) uniformly occurring first blocks, so the total support has cardinality \(m^d\min(m,2^d)\). The probability that \(J=j\) is \(H_d(j+1-\theta+s)-H_d(j-\theta+s)\); summing over \(j\) in the required residue class and multiplying by \(m^{-d}\) establishes the frequency formula. Positivity and Weyl equidistribution ensure every permitted block really occurs infinitely often. This proves the theorem.

## Verification

The accompanying standard-library `check.py` constructs the inclusion-exclusion distribution independently, checks its normalization and strictly positive \(2^d\)-element correction support for degrees one through five, verifies all residue-extension counts for six moduli, and checks 198,385 exact-arithmetic sample/normalization conditions against the resulting probabilities. Samples use exact integer square roots for \(\lfloor\sqrt2\,n^d\rfloor\) and, for degrees at least two, a rational lower-order perturbation; degree one uses a constant perturbation only. Simulations are diagnostics: the infinite statements are established by the proof, not numerical sampling.

## Relationship to prior work

Javaheri's *A note on polynomial sequences modulo integers* (first publicly posted June 29, 2018; Theorem 5) characterizes one-point modular equidistribution of integer parts of real polynomials. This theorem sharpens that setting by classifying every consecutive block of the first length beyond the equidistributed range, including its exact support and all frequencies. Adamczewski and Konieczny's *Bracket words* (first posted March 21, 2022; Theorem 7.1) gives existence of block frequencies for the much broader generalized-polynomial class; its general existence result does not directly provide the stated sharp threshold or the weighted-box formula. The degree-one two-increment behavior is classical and is not claimed as a new special case.

## Limitations

The analysis is qualitative in its convergence rate and does not classify block lengths greater than \(d+1\). The proof assumes irrationality of the leading coefficient, rather than merely any irrational nonconstant coefficient. Equivalent formulations in unindexed or classical generalized-polynomial literature remain a bibliographic originality risk. No independent audit has been performed.

## References

1. M. Javaheri, *A note on polynomial sequences modulo integers*, *Journal of Integer Sequences* **22** (2019), Article 19.1.1; original arXiv version posted 2018-06-29, [arXiv:1806.11359](https://arxiv.org/abs/1806.11359); [published full text](https://cs.uwaterloo.ca/journals/JIS/VOL22/Javaheri/java4.pdf).
2. B. Adamczewski and J. Konieczny, *Bracket words: a generalisation of Sturmian words arising from generalised polynomials*, first arXiv posting 2022-03-21, [arXiv:2203.10814](https://arxiv.org/abs/2203.10814), Theorem 7.1.
3. H. Weyl, *Über die Gleichverteilung von Zahlen mod. Eins*, *Math. Ann.* **77** (1916), 313–352 (classical polynomial equidistribution criterion).
