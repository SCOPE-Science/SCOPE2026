# Exact Abelian-square diversity and conditional limit law for three-marker binary words

## Finding

A nonempty *Abelian square* is a contiguous word of the form \(uv\), with \(|u|=|v|\) and identical numbers of each letter in \(u\) and \(v\). Factors are counted **as distinct literal words**, not as occurrences or merely by their Parikh vectors.

Let \(a,b,c,d\) be arbitrary nonnegative integers and \(w=0^a1\,0^b1\,0^c1\,0^d\). Define the nonnegative lattice-band count
\[
H(A,B;g)=\sum_{\substack{-g\le \delta\le g\\ \delta\equiv g\pmod 2}}
\left[\min(A,B+\delta)-\max(0,\delta)+1\right]_+,
\qquad [x]_+=\max(0,x).
\]
Then the exact number \(S(w)\) of distinct nonempty Abelian-square factors is
\[
\boxed{S(w)=\left\lfloor\frac{\max(a,b,c,d)}2\right\rfloor
 +H(a,c;b)+H(b,d;c)-\mathbf1_{\{b=c\}}H(\min(a,b),\min(c,d);b).}
\tag{1}
\]
This includes every boundary case (zero gaps permitted), including \(S(111)=1\).

For \(T_m=\sum_{a+b+c+d=m}S(0^a1\,0^b1\,0^c1\,0^d)\), the ordinary generating function \(\sum_{m\ge0}T_mz^m\) is the following explicit rational function:
\[
\begin{aligned}
Z(z)&=\frac1{(1-z)^4}\sum_{j=1}^4(-1)^{j+1}\binom4j\frac{z^{2j}}{1-z^{2j}},\\
F(z)&=\frac{1+z^2}{(1-z)^3(1-z^2)^3},\\
U(z)&=\frac{1/(1-z^2)-2z/(1-z^3)+z^2/(1-z^4)}{(1-z)^2},\\
V(z)&=\frac{1/(1+z^2)+2z/(1-z^3)+z^2/(1+z^4)}{(1+z)^2},\\
O(z)&=\frac{U(z)+V(z)}{2(1-z)^2},\\
\boxed{\sum_{m\ge0}T_mz^m}&=Z(z)+2F(z)-O(z).
\end{aligned}
\tag{2}
\]
In particular, \((T_0,T_1,\ldots,T_7)=(1,4,21,54,124,234,423,702)\).

Define for nonnegative reals \(A,B,G\) the planar area
\[
J(A,B;G)=AB-\frac12\bigl[(A-G)_+^2+(B-G)_+^2-(A-B-G)_+^2-(B-A-G)_+^2\bigr].
\tag{3}
\]
If \(W_n\) is uniformly distributed among the \(\binom n3\) indexed binary words of length \(n\ge3\) having exactly three ones, and \(X=(X_0,X_1,X_2,X_3)\sim\mathrm{Dirichlet}(1,1,1,1)\), then
\[
\frac{S(W_n)}{n^2}\ \xrightarrow{\mathrm d}\
\mathcal L=\tfrac12\bigl[J(X_0,X_2;X_1)+J(X_1,X_3;X_2)\bigr],
\qquad \boxed{\mathbb E\mathcal L=\frac1{40}}.
\tag{4}
\]
The limiting variable is nonconstant, and boundedness implies convergence of first moments:
\[
\mathbb E S(W_n)=\frac{n^2}{40}+O(n).
\tag{5}
\]

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\); words are linear rather than circular; a factor is contiguous; distinct factors with the same Parikh vector are **not** identified. Every word in the family has exactly three symbols equal to \(1\). Gap parameters are integers \(a,b,c,d\ge0\) with \(n=a+b+c+d+3\). Formula (2) is a formal power-series identity; it requires no analytic convergence assumption. The random-word statement is for the uniform conditional distribution at fixed Hamming weight three, not an unrestricted Bernoulli word.

## Proof

**Complete factor classification.** Every Abelian square has the same number of ones in its two equal-length halves. Since \(w\) contains only three ones, an Abelian-square factor contains either zero or two ones. The all-zero squares are exactly \(00,0000,\ldots,0^{2\lfloor M/2\rfloor}\), where \(M=\max(a,b,c,d)\), contributing \(\lfloor M/2\rfloor\).

A two-one factor must use adjacent ones, since taking the first and third would include the second. Consider two adjacent ones separated by \(g\) zeros, with at most \(A\) zeros immediately available to the left and \(B\) immediately to the right. A distinct factor containing exactly these ones has the unique literal form \(0^u1\,0^g1\,0^v\), with \(0\le u\le A\), \(0\le v\le B\). Its total length is even and the two ones lie in different halves precisely when
\[
 u+v+g\equiv0\pmod2,\qquad |u-v|\le g.
\]
For the derivation, the first-one and second-one half-conditions yield \(u-v\le g+1\) and \(v-u\le g\), while parity makes \(u-v\equiv g\pmod2\), removing the extra endpoint. For each \(\delta=u-v\), the permitted integers \(u\) run from \(\max(0,\delta)\) to \(\min(A,B+\delta)\). This proves the expression for \(H\).

The first adjacent pair contributes \(H(a,c;b)\) and the second \(H(b,d;c)\). Their literal words can coincide only if the zero gap between their ones is equal, \(b=c\), and then the common words have \(u\le\min(a,b)\) and \(v\le\min(c,d)\). Inclusion-exclusion proves (1). Notice that this collision is a structural feature absent when the word has only two ones.

**Rational population sum.** The all-zero contribution is \(Z(z)\): use \(\lfloor M/2\rfloor=\sum_{j\ge1}\mathbf1_{M\ge2j}\) and subtract words with all four gaps below \(2j\). For one ordered adjacent pair, sum \(u,v\) first and the three freely extensible exterior gaps next. Because the allowed separating gap is \(g=|u-v|+2r\) for \(r\ge0\), the pair generating series is
\[
\frac1{(1-z)^3(1-z^2)}\sum_{u,v\ge0}z^{u+v+|u-v|}
=\frac{1+z^2}{(1-z)^3(1-z^2)^3}=F(z).
\]
For collisions, write the common separating gap as \(g=b=c\). It is necessary and sufficient that \(0\le u,v\le g\), \(u+v+g\) is even, and that \(a\ge u\), \(d\ge v\). The contribution is
\[
\frac1{(1-z)^2}\sum_{g\ge0}z^{2g}\sum_{u,v=0}^g
\mathbf1_{u+v+g\equiv0\ (\mathrm{mod}\ 2)}z^{u+v}.
\]
Applying the parity projector \(\frac12(1+(-1)^{u+v+g})\) and summing the two finite geometric sums gives exactly \(O(z)=(U(z)+V(z))/(2(1-z)^2)\). The two adjacent pairs contribute \(2F(z)\). This proves (2) as an identity of rational formal power series.

**Conditional limit law.** Uniform four-tuples of nonnegative integer gaps summing to \(n-3\), scaled by \(n\), converge weakly to the uniform three-simplex law \(\mathrm{Dirichlet}(1,1,1,1)\). For \(A,B,G\) of order \(n\), the lattice checkerboard count obeys
\[
H(A,B;G)=\tfrac12\,\mathrm{area}\{(u,v):0\le u\le A,\ 0\le v\le B,\ |u-v|\le G\}+O(n)
\]
uniformly over \(0\le A,B,G\le n\), by the elementary lattice-point boundary estimate for a convex polygon with boundedly many edges. Cutting two triangles off the rectangle gives area (3). The overlap subtraction is supported on \(b=c\), an event of probability \(O(1/n)\), so it vanishes in probability after division by \(n^2\). The all-zero term is \(O(n)\), proving the distributional limit.

To calculate its mean, with \(A,B,G\) three distinct coordinates of a uniform four-simplex composition, Dirichlet beta conditioning gives
\[
\mathbb E[AB]=\tfrac1{20},\quad
\mathbb E[(A-G)_+^2]=\tfrac1{20},\quad
\mathbb E[(A-B-G)_+^2]=\tfrac1{40}.
\]
For instance, \(A+G\sim\mathrm{Beta}(2,2)\), \(A/(A+G)\sim\mathrm{Beta}(1,1)\), independently, giving the middle identity. Similarly \(A+B+G\sim\mathrm{Beta}(3,1)\) and \(A/(A+B+G)\sim\mathrm{Beta}(1,2)\), giving the last. Thus \(\mathbb EJ(A,B;G)=\frac1{20}-\frac12(\frac2{20}-\frac2{40})=\frac1{40}\). Both adjacent-pair terms have this same expectation, and the factor \(\frac12\) in (4) yields \(\mathbb E\mathcal L=\frac1{40}\). The values at interior points \((1/10,2/10,3/10,4/10)\) and \((1/4,1/8,3/8,1/4)\) are respectively \(1/20\) and \(11/256\), proving nonconstancy. A deterministic bound \(0\le S(w)\le n^2\) gives uniform integrability. The rational generating function has a pole of order six and leading coefficient \(1/2\) at \(z=1\); coefficient extraction yields the refined \(O(n)\) mean error in (5).

## Verification

Run `python3 verify.py` in the same directory as this document. The standard-library checker compares the complete literal set of Abelian-square factors with (1) for every weight-three word through length \(26\), a total of \(17{,}550\) words. It independently expands the rational summands in (2) through zero-count degree \(22\) and compares with the aggregate gap formula; it also checks the rational Dirichlet first-moment computation. These are finite checks and do not establish the general identity on their own; the proof above supplies the infinite argument.

## Relationship to prior work

Richmond and Shallit count Abelian-square **words** at a given even length, rather than distinct Abelian-square factors inside a fixed sparse word. Kociumaka, Radoszewski, Rytter and Waleń establish quadratic unrestricted-alphabet-size growth and analyze bounded-run restrictions; their two-marker construction demonstrates quadratic abundance but does not give the four-gap identity (1), the conditional all-length series (2), or the expectation \(1/40\). Fici, Mignosi and Shallit investigate Abelian-square-rich infinite words, not this finite fixed-composition population. The general quadratic-order fact and constructions are **not claimed as new**.

## Limitations

The result is confined to binary words containing precisely three ones. It does not classify the maximizers of the Abelian-square count at each length, or provide an explicit closed-form density for the limit distribution. The same literal factor may occur multiple times but is counted once. The pointwise continuum limit is not asserted on the measure-zero hyperplane of exactly equal middle gaps, where overlap subtraction may persist at quadratic order. Historical equivalence with unindexed treatments cannot be excluded; independent review has not been performed.

## References

1. L. B. Richmond and J. Shallit, *Counting Abelian Squares*, arXiv:0807.5028 (first submitted 31 July 2008), https://arxiv.org/abs/0807.5028.
2. T. Kociumaka, J. Radoszewski, W. Rytter, T. Waleń, *Maximum Number of Distinct and Nonequivalent Nonstandard Squares in a Word*, Developments in Language Theory (2014), https://doi.org/10.1007/978-3-319-09698-8_19; arXiv:1604.02238.
3. G. Fici, F. Mignosi, J. Shallit, *Abelian-Square-Rich Words*, arXiv:1701.00948 (2017), https://arxiv.org/abs/1701.00948.
