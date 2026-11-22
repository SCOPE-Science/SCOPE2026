# Joint boundary counts of random interval orders and independent Rayleigh extremes

## Finding

For every integer \(n\ge1\), consider the precedence order on \(n\) randomly paired intervals. Write \(M_n\) and \(N_n\) for the number of minimal and maximal elements. For all integers \(0\le k,l\le n\), put \(c=2n-k-l\), \(z=n-k-l+h\), and define \((2n-1)!!=1\cdot3\cdots(2n-1)\). Their **complete exact joint survival law** is

\[
\Pr(M_n\ge k,N_n\ge l)=\frac{1}{(2n-1)!!}\sum_{h=\max(0,k+l-n)}^{\min(k,l)}\frac{k!\,l!\,c!}{h!\,(k-h)!\,(l-h)!\,2^z z!}.
\]

The marginal survival function is

\[
\Pr(M_n\ge k)=\Pr(N_n\ge k)=\prod_{j=0}^{k-1}\frac{2n-2j}{2n-j}.
\]

With \(Y_1,Y_2\) independent variables having \(\Pr(Y_i>x)=\exp(-x^2/4)\) for \(x\ge0\),

\[
(M_n/\sqrt n,N_n/\sqrt n)\ \xrightarrow{\mathrm d}\ (Y_1,Y_2).
\]

Moreover, \(\mathbb E[M_n]/\sqrt n\to\sqrt\pi\), \(\operatorname{Var}(M_n)/n\to4-\pi\), and \(\operatorname{Corr}(M_n,N_n)\to0\). The finite-size variables are not asserted independent.

## Assumptions and scope

For each \(n\), sample \(2n\) independent observations from any one atomless probability distribution on the real line, pair observations by their original labels into \(n\) intervals \(I_i=[L_i,R_i]\) (left and right endpoints ordered), and set \(I_i\prec I_j\) precisely when \(R_i<L_j\). An interval is minimal if no other interval precedes it, maximal if no other follows it. All formulas are distribution-free by invariance under strictly increasing transformations on the sampled support. Empty products equal one. When \(n=1\), \(M_n=N_n=1\). These are *precedence-poset* boundary elements, not inclusion-minimal or inclusion-maximal intervals.

## Proof

**Exact one-sided law.** Sorting all \(2n\) endpoints produces a uniform perfect matching of their ranks. Let \(T\) be the first right endpoint (first completed pair). An interval is minimal exactly if its left endpoint occurs at or before \(T\). Consequently \(M_n\ge k\) means the first \(k\) endpoint positions contain no complete pair. At the \((j+1)\)-st reveal, after \(j\) distinct pairs have opened, \(2n-2j\) of the \(2n-j\) possible as-yet-unseen endpoints are from new pairs. Their product yields the marginal formula. Reversing endpoint order yields the same law for \(N_n\).

**Bivariate finite law.** The event \(M_n\ge k,N_n\ge l\) forbids internally matched pairs within the first \(k\) endpoint positions \(A\) and within the last \(l\) positions \(B\). These blocks are disjoint because \(k+l\le2n\). There are \(c\) middle endpoints. If exactly \(h\) pairs join \(A\) to \(B\), then \(k-h\) pairs join \(A\) to the middle, \(l-h\) join \(B\) to the middle, and the \(2z\) remaining middle endpoints pair internally, where \(z=n-k-l+h\). Counting these choices gives \(k!l!c!/[h!(k-h)!(l-h)!2^z z!]\) perfect matchings. The feasible range of \(h\) is precisely the range displayed in the theorem. Divide by the total \((2n-1)!!\) matchings. Taking two successive finite differences of this survival function recovers each individual joint probability, so it specifies the full joint law.

**Joint scaling.** By the probability integral transform it suffices to take independent uniform endpoints on \([0,1]\). Let \(T_n=\min_i R_i\), and \(W_n=1-\max_i L_i\). When \(a,b\ge0\) and \(a+b\le1\), the events \(T_n>a\) and \(W_n>b\) forbid the disjoint endpoint squares \([0,a]^2\) and \([1-b,1]^2\). Thus

\[
\Pr(T_n>a,W_n>b)=(1-a^2-b^2)^n.
\]

It follows directly that \((\sqrt n T_n,\sqrt n W_n)\) converges jointly to independent variables with survival \(\exp(-x^2)\). Conditional on \(T_n=t\), the interval ending at \(t\) is minimal, and the other \(n-1\) intervals independently have their right endpoint greater than \(t\). Each has its left endpoint at most \(t\) with probability \(2t/(1+t)\). Therefore

\[
M_n\mid T_n=t\ \sim\ 1+\operatorname{Binomial}\!\left(n-1,\frac{2t}{1+t}\right).
\]

In particular, \(\mathbb E[(M_n-2nT_n)^2]=O(\sqrt n)\): the expected conditional variance is \(O(n\mathbb E T_n)=O(\sqrt n)\), while the conditional-mean discrepancy is bounded in absolute value by \(1+2T_n+2nT_n^2\), whose squared expectation is \(O(1)\). The requisite moment bounds follow from \(\Pr(T_n>t)=(1-t^2)^n\le e^{-nt^2}\). The reflected argument gives \(\mathbb E[(N_n-2nW_n)^2]=O(\sqrt n)\). Hence the scaled counts are jointly asymptotic to \((2\sqrt n T_n,2\sqrt nW_n)\), proving the independent Rayleigh limit.

Finally, the finite-product bound

\[
\Pr(M_n\ge k)\le\exp\!\left(-\frac{k(k-1)}{4n}\right)
\]

follows from \(\log(1-u)\le-u\). It gives uniformly bounded moments of every fixed order after scaling by \(\sqrt n\). The Rayleigh limit therefore also gives the stated first two moments and mixed moment, and positive limiting scaled variances yield vanishing correlation.

## Verification

The included standalone `checker.py` uses Python's exact rational arithmetic to enumerate all perfect matchings through seven intervals and compare their boundary-count joint survivals with the closed formula. It also performs further exact rational marginal/bivariate consistency checks for moderate sizes. Run `python checker.py` in a directory containing the extracted checker. An exhaustive finite check supports the counting identity but is not the proof of the all-size or limit statements; the arguments above provide those proofs.

## Relationship to prior work

Diaconis, Holmes and Janson develop graph limits and structural characteristics of random interval graphs. Iliopoulos treats the same paired-endpoint model and a range of degree and extremal graph observables. These are foundational for the model but do not, in the inspected portions, state this two-sided precedence-poset boundary joint law or independent-extreme limit. Justicz, Scheinerman and Winkler investigate disjoint interval families and globally intersecting intervals; their 1990 article's accessible abstract does not resolve this precise comparison, and its inaccessible full text is a residual priority risk. The statistic is not an interval-containment extremum and is not simply a component-count statistic.

## Limitations

The theorem has an analytic derivation and finite exact checks, not independent validation. An overlooked equivalent result in older interval-order literature cannot be excluded. The limiting independence does **not** imply independence for finite \(n\), nor does the theorem determine the unscaled covariance limit. The proof requires independently generated, identically distributed atomless endpoints; it does not cover atoms or dependent endpoint mechanisms.

## References

1. P. Diaconis, S. Holmes, S. Janson, *Interval graph limits*, arXiv:1102.2841 (first posted 2011-02-14), https://arxiv.org/abs/1102.2841.
2. L. Iliopoulos, *Random Interval Graphs*, arXiv:1507.06275 (first posted 2015-07-22), https://arxiv.org/abs/1507.06275.
3. J. Justicz, E. R. Scheinerman, P. M. Winkler, *Random Intervals*, American Mathematical Monthly 97 (1990), 881–889, https://doi.org/10.1080/00029890.1990.11995679 (abstract inspected; full text inaccessible).
4. E. R. Scheinerman, *Random interval graphs*, Combinatorica 8 (1988), 357–371, https://doi.org/10.1007/BF02189092 (relevant historical source; full text not fully verified).
