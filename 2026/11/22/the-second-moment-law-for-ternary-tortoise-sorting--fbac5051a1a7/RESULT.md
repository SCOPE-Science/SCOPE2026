# The second-moment law for ternary tortoise sorting

## Finding

Let \(\Sigma=\{0,1,2\}\) with the natural letter order, and let \(\tau\) be the one-pass Defant--Kravitz *tortoise* map on finite words. Define the fertility of an output \(v\in\Sigma^n\) by
\[
F_n(v)=\#\{w\in\Sigma^n:\tau(w)=v\},
\]
and its squared-fertility sum by \(S_n=\sum_{v\in\Sigma^n}F_n(v)^2\). Then for **every** \(n\ge0\), including the empty word,
\[
\boxed{\sum_{n\ge0}S_nz^n=\frac{1-8z+32z^2-68z^3+83z^4-60z^5+24z^6}{(1-z)^2(1-2z)^2(1-5z+7z^2-5z^3)}.}
\]
The initial values are \(1,3,15,71,301,1175,4347,15547,54421,187855\) for \(0\le n\le9\). There is a unique real \(\lambda>3\) satisfying \(\lambda^3-5\lambda^2+7\lambda-5=0\), namely \(\lambda=3.359304085971776\ldots\), and a positive constant \(K=3.630021251101213\ldots\) for which \(S_n\sim K\lambda^n\).

For independently uniform input words \(X_n,X_n'\in\Sigma^n\), the collision probability of their images is \(\Pr(\tau(X_n)=\tau(X_n'))=S_n/9^n\). Thus the order-two Rényi entropy, with base-two logarithms, has the all-length asymptotic law
\[
H_2(\tau(X_n))=n\log_2(9/\lambda)-\log_2 K+o(1),
\]
and the exact entropy rate is \(\log_2(9/\lambda)=1.421762606445352\ldots\) bits per input symbol.

## Assumptions and scope

Words are finite strings over the **fixed ordered three-symbol alphabet**, repetitions allowed. Every input length \(n\) is included, and the source is uniform over all \(3^n\) words, not a fixed-composition ensemble. The map is defined recursively: if the maximum letter \(m\) occurs \(r\) times and \(w=w_0m w_1m\cdots m w_r\), with all \(w_j\) avoiding \(m\), then
\[
\tau(w)=\tau(w_0)\tau(w_1)m\tau(w_2)m\cdots\tau(w_r)m,
\]
with \(\tau(\varepsilon)=\varepsilon\) and the same recursion on the lower alphabet. If \(r=0\), use the smaller alphabet. This is one application of the tortoise operator, not iterated sorting. A positional preimage is counted once for each *distinct input word*, not for each algorithmic execution.

## Proof

**1. Binary fertilities.** Write \(f(u)=\#\{x\in\{0,1\}^{|u|}:\tau(x)=u\}\). For an input with \(r\) ones, each of the \(r+1\) intervening zero runs is fixed by \(\tau\), so the output has the form \(0^{a_0+a_1}1\,0^{a_2}1\cdots0^{a_r}1\). Consequently, for \(u\in\{0,1\}^*\),
\[
f(u)=\begin{cases}1,&u=0^h\ \text{for some }h\ge0,\\h+1,&u\text{ ends in }1\text{ and begins with exactly }h\text{ zeros},\\0,&\text{otherwise.}\end{cases}
\]
The cases are disjoint; the empty word has fertility one. Let \(B_2(z)=\sum_u f(u)^2z^{|u|}\). The all-zero words contribute \((1-z)^{-1}\), and the words ending in one are counted by a leading zero block and an arbitrary nonempty suffix ending in one. Thus
\[
B_2(z)=\frac1{1-z}+\frac z{1-2z}\sum_{h\ge0}(h+1)^2z^h
=\frac{1-2z+3z^2}{(1-z)^2(1-2z)}.
\]

**2. Two initial binary subwords.** For binary \(u\), put \(c(u)=\sum_{u=xy}f(x)f(y)\), over all \(|u|+1\) splits. We claim the exact formula
\[
c(u)=\begin{cases}
 h+1,&u=0^h,\\
 h+1,&u\text{ has a }1\text{ and ends in }0,\text{ with }h\text{ initial zeros},\\
 (h+1)(L+(h+2)/2),&u=0^hq,\ q\text{ begins and ends in }1,\ |q|=L.
\end{cases}
\]
For \(0^h\) every split contributes one. If the word has a one and ends in zero, only the split just after the last one can contribute; its left factor has fertility \(h+1\) and the remaining zero suffix has fertility one. For an ending-one word, the splits inside the leading zero block contribute \((h+1)(h+2)/2\). Every other contributing split ends immediately after a one of \(q\). Its left fertility is \(h+1\), while the right fertility is one plus the length of the immediately following zero run. The sum of these right fertilities is exactly \(L\), since \(q\) starts and ends with one. This proves the formula even for \(h=0\), \(L=1\), and empty suffixes.

To square-sum, partition binary words into all-zero, ending-zero with at least one one, and ending-one. The first two contributions are
\[
\frac{1+z}{(1-z)^3},\qquad \frac{z^2(1+z)}{(1-z)^3(1-2z)}.
\]
For ending-one words \(0^hq\), \(q\) begins and ends in one, and the number of such \(q\) of length \(L\) is \(1\) at \(L=1\) and \(2^{L-2}\) at \(L\ge2\). Summing the square of \((h+1)(L+(h+2)/2)\) over \(h,L\) by geometric series and their first two derivatives gives
\[
\frac{2z(2-z)(1+2z)}{(1-z)(1-2z)^3}.
\]
The sum of these three disjoint contributions is
\[
C_2(z):=\sum_{u\in\{0,1\}^*}c(u)^2z^{|u|}
=\frac{1+z+6z^2}{(1-z)(1-2z)^3}.
\]
This computation requires no assumption on the number or arrangement of ones.

**3. Ternary fibers.** If an output \(v\) contains no two, its fertility is \(f(v)\), because the number of maximal letters cannot change. If it contains at least one two, a nonempty fiber forces it to end in two. Write the unique decomposition \(v=u2v_2 2\cdots v_r2\) into binary blocks. The recursion in the assumptions shows that the first binary block is the concatenation of the sorted images of **two independently chosen** binary inputs, giving exactly \(c(u)\) possible ordered input pairs. Each subsequent binary block \(v_j\) has \(f(v_j)\) preimages. Therefore
\[
F(v)=c(u)\prod_{j=2}^{r}f(v_j).
\]
This formula also handles \(r=1\), where the product is empty and equals one. Summing the squares over words, the prefix \(u\) contributes \(C_2(z)\), each obligatory two contributes \(z\), and any additional two and binary block contributes \(zB_2(z)\). Hence
\[
S(z)=B_2(z)+\frac{zC_2(z)}{1-zB_2(z)}.
\]
Substituting the rational expressions above and simplifying yields the displayed formula. Since both derivations count actual preimages, there is no overcount of outputs across different positions of the maximal letter.

**4. Singularities and entropy.** Put \(Q(z)=1-5z+7z^2-5z^3\). Its derivative \(-5+14z-15z^2\) is negative for all real \(z\). Therefore \(Q\) has exactly one real root \(r=0.297680702433558\ldots\) in \((0,1/2)\). The other two roots are conjugates whose modulus is \((5r)^{-1/2}>r\), by Vieta's product relation; the remaining denominator poles at \(1/2\) and \(1\) also lie farther away. Since \(S=B_2+zC_2/(1-zB_2)\), and \(B_2,C_2\) have positive values at \(r\), the pole at \(r\) is simple and nonremovable. Writing \(N(z)\) for the displayed numerator, its coefficient is
\[
K=-\frac{N(r)}{r(1-r)^2(1-2r)^2Q'(r)}>0,
\qquad \lambda=r^{-1}.
\]
Consequently \(S_n\sim K\lambda^n\). For independent uniform inputs, there are \(9^n\) ordered input pairs, so their image-collision probability is \(S_n/9^n\). The formula for the order-two Rényi entropy follows by taking a base-two negative logarithm.

## Verification

Run `python3 verification/exhaustive.py` and `python3 verification/series.py` from the package root, using only the Python standard library. The first script implements both a recursive maximum-letter map and an independent literal stack algorithm; over all lengths \(0\) through \(9\), it checks the images of \(29{,}524\) input words, every output's predicted fertility, and the first ten second moments. The second enumerates all \(8{,}191\) binary words of lengths \(0\) through \(12\), independently verifies the binary formulas, and checks the rational coefficient identities through degree \(80\). Recorded console outputs are provided. Those finite tests are consistency checks; the all-length conclusion follows from the proof, not from extrapolation of enumeration.

## Relationship to prior work

Defant and Kravitz introduced the tortoise recursion and general fertility analysis in *Stack-sorting for Words* (2018). Campbell and Rampersad (first public release April 28, 2026) study subwords under stack-sorting equivalence, including binary tortoise equivalence classes and automatic sequences. Neither inspected treatment supplies the sum of **squared preimage fertilities over all ternary outputs**, its rational generating function, or the resulting Rényi entropy rate. General per-output fertility information does not alone provide an evaluated global second moment; this result explicitly performs the weighted aggregation. Prior enumeration of the ternary *support* of outputs is likewise weaker because it discards positive fiber sizes. No novelty is claimed for the operator or its binary preimage recursion.

## Limitations

The theorem treats exactly one tortoise pass, the uniformly sampled full ternary word space and order-two Rényi entropy. It does not determine Shannon entropy, higher Rényi orders, fixed-composition fiber statistics, arbitrary alphabet sizes or iterated sorting. Existing literature could contain an equivalent global second-moment calculation under a different terminology; the cited comparisons do not prove exhaustive priority.

## References

1. Colin Defant and Noah Kravitz, *Stack-sorting for Words*, arXiv:1809.09158, first public September 24, 2018. https://arxiv.org/abs/1809.09158
2. John M. Campbell and Narad Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811, first public April 28, 2026. https://arxiv.org/abs/2604.25811
