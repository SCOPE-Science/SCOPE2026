# The second-moment law for ternary tortoise sorting

## Finding

Let \(\Sigma=\{0,1,2\}\) with the natural letter order, and let \(\tau\) be the one-pass Defant–Kravitz *tortoise* map on finite words. Define \(F_n(v)=\#\{w\in\Sigma^n:\tau(w)=v\}\) and \(S_n=\sum_{v\in\Sigma^n}F_n(v)^2\). Then for every \(n\ge 0\), including the empty word,
\[
\sum_{n\ge0} S_nz^n=\frac{1-8z+32z^2-68z^3+83z^4-60z^5+24z^6}{(1-z)^2(1-2z)^2(1-5z+7z^2-5z^3)}.
\]
The initial values for \(0\le n\le9\) are \(1,3,15,71,301,1175,4347,15547,54421,187855\). There is a unique real \(\lambda>3\) satisfying \(\lambda^3-5\lambda^2+7\lambda-5=0\), namely \(\lambda=3.359304085971776\ldots\), and \(S_n\sim K\lambda^n\), where \(K=3.630021251101213\ldots>0\).

For independently uniform words \(X_n,X_n'\in\Sigma^n\), the probability that their images coincide is \(S_n/9^n\). Thus the order-two Rényi entropy, in bits, satisfies
\[
H_2(\tau(X_n))=n\log_2(9/\lambda)-\log_2 K+o(1),
\qquad \log_2(9/\lambda)=1.421762606445352\ldots.
\]

## Assumptions and scope

Words are finite strings over the fixed ordered three-symbol alphabet, repetitions allowed, with no conditioning on composition. If the maximum letter \(m\) occurs \(r\) times and \(w=w_0m w_1m\cdots m w_r\), with all \(w_j\) avoiding \(m\), the recursion is
\[
\tau(w)=\tau(w_0)\tau(w_1)m\tau(w_2)m\cdots\tau(w_r)m,
\qquad \tau(\varepsilon)=\varepsilon.
\]
Batches of inputs are not sorted iteratively: each word undergoes one pass. Preimages are counted as distinct input words.

## Proof

**1. Binary fertilities.** Let \(f(u)=\#\{x\in\{0,1\}^{|u|}:\tau(x)=u\}\). If a binary input has \(r\ge1\) ones, each of its \(r+1\) intervening zero runs is fixed by \(\tau\), so its output has the form \(0^{a_0+a_1}1\,0^{a_2}1\cdots0^{a_r}1\). Thus
\[
 f(u)=\begin{cases}1,&u=0^h\quad(h\ge0),\\ h+1,&u\text{ ends in }1\text{ and begins with exactly }h\text{ zeros},\\ 0,&\text{otherwise.}\end{cases}
\]
In the second case \(u=0^h q\), with \(q\) beginning and ending with \(1\). Such suffixes have generating function \(A(z)=z+z^2/(1-2z)=z(1-z)/(1-2z)\): length one contributes \(z\), and at length at least two only the interior is free. Hence
\[
B_2(z):=\sum_{u\in\{0,1\}^*} f(u)^2 z^{|u|}
=\frac{1}{1-z}+A(z)\sum_{h\ge0}(h+1)^2z^h
=\frac{1-2z+3z^2}{(1-z)^2(1-2z)}.
\]

**2. The first binary block.** For a binary word \(u\), put \(c(u)=\sum_{u=xy} f(x)f(y)\) over all splits, including empty factors. The exact values are
\[
c(u)=\begin{cases}
h+1,&u=0^h,\\
h+1,&u\text{ has a }1\text{ and ends in }0,\text{ with }h\text{ initial zeros},\\
(h+1)(L+(h+2)/2),&u=0^h q,\quad q\text{ begins and ends in }1,\quad |q|=L.
\end{cases}
\]
For \(0^h\) every split contributes one. If the word has a one and ends in zero, only the split just after the last one can contribute. For an ending-one word the splits up to and including the end of the initial zero run contribute \((h+1)(h+2)/2\). Other nonzero splits follow a one of \(q\); their left fertilities equal \(h+1\), and their right fertilities equal one plus the length of the immediately following zero run. The sum of the latter fertilities equals \(L\), including the terminal split with empty right factor.

The squared values from all-zero words and from words ending in zero with at least one one contribute respectively
\[
\frac{1+z}{(1-z)^3},\qquad \frac{z^2(1+z)}{(1-z)^3(1-2z)}.
\]
For the second contribution, remove the \(h\) initial zeros and the mandatory first one and last zero; the middle is an arbitrary binary word. For the ending-one case let \(D=z\,d/dz\), \(H=1/(1-z)\). The sum over \(h,L\) of the squared value is
\[
((D+1)^2H)(D^2A)+((D+1)^2(D+2)H)(DA)
+\tfrac14((D+1)^2(D+2)^2H)A
=\frac{2z(2-z)(1+2z)}{(1-z)(1-2z)^3}.
\]
Here powers of \(D\) multiply the corresponding coefficients by powers of their indices, encoding \((h+1)^2(L+(h+2)/2)^2\). Adding the three contributions gives
\[
C_2(z):=\sum_{u\in\{0,1\}^*} c(u)^2 z^{|u|}=\frac{1+z+6z^2}{(1-z)(1-2z)^3}.
\]

**3. Ternary fibers.** An output containing no two has binary fertility \(f\). If an output has at least one two but does not end in two, it has fertility zero. Otherwise it decomposes uniquely as \(v=u2v_2 2\cdots v_r2\) with binary blocks (including empty ones). The first binary block is the concatenation of the images of two ordered binary input blocks, giving \(c(u)\) choices. Each subsequent block has \(f(v_j)\) preimages. The resulting input words are distinct, since they recover their own ordered blocks on splitting at the twos. Thus \(F(v)=c(u)\prod_{j=2}^r f(v_j)\), also when \(r=1\). Squaring and summing, with each two contributing length one, gives
\[
S(z)= B_2(z)+\frac{zC_2(z)}{1-zB_2(z)}.
\]
Substitution gives the displayed generating function.

**4. Singularities and entropy.** Write \(Q(z)=1-5z+7z^2-5z^3\), and \(N(z)\) for the displayed numerator. The derivative \(-5+14z-15z^2\) is strictly negative on the real axis. The unique real root \(r=0.297680702433558\ldots\) is between zero and \(1/3\); the other roots are conjugates of modulus \((5r)^{-1/2}>r\) by Vieta's formula. The denominator factors at \(1/2\) and \(1\) cannot affect dominance. At \(r\), \(1-rB_2(r)=0\) and \(rC_2(r)>0\), so \(S(z)\) has a simple pole there, with coefficient of \((1-z/r)^{-1}\) equal to
\[
K=-\frac{N(r)}{r(1-r)^2(1-2r)^2Q'(r)}>0.
\]
Positivity also follows from \((1-zB_2(z))'|_{z=r}=-B_2(r)-rB_2'(r)<0\). Thus \(S_n\sim Kr^{-n}\), with \(\lambda=r^{-1}\). There are \(9^n\) equally likely ordered input pairs, so the collision probability is \(S_n/9^n\). Taking its negative base-two logarithm yields the asserted entropy law.

## Verification

Run `python3 verification/exhaustive.py` and `python3 verification/series.py` from the package root, using the Python standard library. The first script compares recursive and stack maps on all 29,524 input words through length nine and checks every output's predicted fertility and the first ten second moments. The second checks the binary formulas on all 8,191 binary words through length twelve and checks the rational coefficient computations through degree eighty. Their outputs are supplied. Those finite checks are consistency evidence, not the basis of the all-length conclusion.

## Relationship to prior work

Defant and Kravitz introduced the tortoise recursion and general fertility analysis in *Stack-sorting for Words* (2018). Campbell and Rampersad study subwords under stack-sorting equivalence, including binary tortoise equivalence classes and automatic sequences. No novelty is claimed for the operator or the binary recursion. The quantity evaluated here is a global, weighted aggregation of ternary fibers, not per-output fertility or a count of the output support. Its growth constant measures the concentration of the ternary output distribution under uniform sampling.

## Limitations

The theorem treats one pass, the uniformly sampled full ternary word space and order-two Rényi entropy. It does not determine Shannon entropy, higher Rényi orders, fixed-composition fiber statistics, arbitrary alphabet sizes or iterated sorting. The literature comparison is not an exhaustive proof of priority.

## References

1. Colin Defant and Noah Kravitz, *Stack-sorting for Words*, arXiv:1809.09158. https://arxiv.org/abs/1809.09158
2. John M. Campbell and Narad Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811. https://arxiv.org/abs/2604.25811
