# Composition-refined enumeration and type laws for subsequence universality

## Finding

Fix a labeled alphabet \(\Sigma=\{1,\ldots,q\}\) with \(q\ge2\). For a finite word \(w\in\Sigma^*\), let \(\iota(w)\) be the largest integer \(k\ge0\) for which every word of length \(k\) over the **fixed ambient alphabet** \(\Sigma\) is a scattered subsequence of \(w\). Let \(\alpha_i(w)\) count the copies of letter \(i\), and let \(c_q(\boldsymbol\alpha,k)\) count words with composition \(\boldsymbol\alpha\in\mathbb N_0^q\) and index \(k\).

Write \(X_S=\sum_{i\in S}x_i\) for every \(S\subseteq[q]\), with \(X_\varnothing=0\). Define the following formal power series, which are explicit rational functions:

\[
A_q(\mathbf x)=\sum_{j=1}^q x_j\sum_{S\subseteq[q]\setminus\{j\}}
  \frac{(-1)^{q-1-|S|}}{1-X_S},\qquad
R_q(\mathbf x)=\sum_{\varnothing\ne T\subseteq[q]}
  \frac{(-1)^{|T|+1}}{1-X_{[q]\setminus T}}.
\]

**The complete composition-index law**, valid coefficientwise for all compositions and indices, is

\[
\boxed{\sum_{\boldsymbol\alpha\in\mathbb N_0^q}\sum_{k\ge0}
 c_q(\boldsymbol\alpha,k)\,\mathbf x^{\boldsymbol\alpha}u^k
  =\frac{R_q(\mathbf x)}{1-uA_q(\mathbf x)}.}
\]

For the binary alphabet, writing \(a\) for the number of zeros and \(b\) for the number of ones, the entire three-variable function reduces to

\[
\boxed{F_2(x,y,u)=\frac{1-xy}{(1-x)(1-y)-uxy(2-x-y)}.}
\]

For every \(a,b\ge0\), put \(m=\min(a,b)\) and \(M=\max(a,b)\). The exact number of words attaining the maximum possible index \(m\) is

\[
\boxed{c_2((a,b),m)=\sum_{j=0}^{m}\binom mj\binom{M-m+j}{j}.}
\]

The complete first moment on a binary fixed-composition class is

\[
\boxed{\sum_{w:\,\alpha_0(w)=a,\,\alpha_1(w)=b}\iota(w)
=\sum_{j=0}^{m-1}(a+b-2j)\binom{a+b-2j-2}{a-j-1},}
\]

where the sum is zero if \(m=0\). Thus dividing by \(\binom{a+b}{a}\) gives the exact expected index in the uniform binary type class.

There is also a **fixed-composition limit law** for every \(q\): if nonnegative integer compositions \(\boldsymbol\alpha^{(n)}\) have total length \(n\) and \(\alpha_i^{(n)}/n\to p_i>0\), then a uniformly chosen word \(W_n\) in that type class satisfies

\[
\boxed{\frac{\iota(W_n)}n\xrightarrow{\mathbb P}\frac1{\mu(\mathbf p)},\qquad
\mu(\mathbf p)=\sum_{\varnothing\ne S\subseteq[q]}
\frac{(-1)^{|S|+1}}{\sum_{i\in S}p_i}.}
\]

The normalized expected index converges to the same limit. For binary frequencies \((1-p,p)\), the limiting index density is \(p(1-p)/(1-p(1-p))\); for uniformly balanced \(q\)-letter frequencies, it is \(1/(qH_q)\), where \(H_q=\sum_{j=1}^q1/j\).

## Assumptions and scope

All enumeration formulas are identities of formal power series over the integers in the letter variables and \(u\); they require no analytic convergence. The alphabet is fixed even for words omitting some symbols, which then have index zero. The empty word is included and has index zero. In the limit theorem, \(q\) is fixed and every limiting frequency is strictly positive; no rate or central limit theorem is asserted.

## Proof

**1. Greedy arches and the index.** Scan a word left to right, ending a block at the first position where all \(q\) letters have appeared. Restart immediately and continue until no complete block remains. The result is a unique factorization \(w=a_1a_2\cdots a_kr\), with \(k\) shortest complete-alphabet blocks (arches) and a final suffix missing at least one letter. Any length-\(k\) target word embeds by taking its successive target letters from successive arches. Conversely, let \(t_j\) be the final letter of arch \(a_j\), which is the first occurrence of \(t_j\) inside that arch. Choose any letter \(t_{k+1}\) absent from \(r\). Greedy subsequence matching of \(t_1\cdots t_k t_{k+1}\) must use the final position of each arch to match \(t_j\), and then fails on the remainder. Thus \(\iota(w)=k\) exactly, including the case \(k=0\).

**2. Multivariate arch and remainder inventories.** If the final, previously unseen letter of one arch is \(j\), its prefix uses only letters other than \(j\), but must contain every one of them. Inclusion-exclusion over the required other letters gives precisely

\[
 x_j\sum_{S\subseteq[q]\setminus\{j\}}(-1)^{q-1-|S|}(1-X_S)^{-1}.
\]

Summing over \(j\) counts all arches and gives \(A_q\). The remainder is any word omitting at least one ambient letter; inclusion-exclusion over sets of omitted letters gives \(R_q\). Unique concatenation of \(k\) arches and one remainder has weight \(u^kA_q^kR_q\). Summation over \(k\ge0\) proves the first boxed identity, with no overcounting or boundary exclusions.

**3. Binary specializations.** Directly, \(A_2=xy\bigl((1-x)^{-1}+(1-y)^{-1}\bigr)\) and \(R_2=(1-xy)/((1-x)(1-y))\); substitution gives \(F_2\). The coefficient of \(u^m y^m\), for \(a\ge b=m\), is the formal series \(x^m(2-x)^m/(1-x)^{m+1}\). Expanding \((2-x)^m=(1+(1-x))^m\) as \((1+(1-x)^{-1})^m(1-x)^m\) yields the positive sum in the third box. Symmetry exchanges zeros and ones, and the composition bound \(\iota\le\min(a,b)\) follows since each arch contains both letters.

For the first moment, differentiate at \(u=1\) to obtain

\[
\left.\frac{\partial F_2}{\partial u}\right|_{u=1}
=\frac{xy(2-x-y)}{(1-x-y)^2(1-xy)}.
\]

Expand \((1-xy)^{-1}=\sum_{j\ge0}(xy)^j\) and use the binomial coefficients of \((1-x-y)^{-1}\) and \((1-x-y)^{-2}\). Their sum in the remaining bidegree is \((a+b-2j)\binom{a+b-2j-2}{a-j-1}\), establishing the fourth box.

**4. Fixed-type law of large numbers.** First take an infinite i.i.d. letter source with positive probabilities \(\mathbf p\). Its successive greedy arch lengths are independent and identically distributed coupon-collector completion times. Inclusion-exclusion gives their finite expectation \(\mu(\mathbf p)\): for integer \(t\ge0\), the chance an arch is incomplete at time \(t\) is \(\sum_{\varnothing\ne S}(-1)^{|S|+1}(1-\sum_{i\in S}p_i)^t\), and summing over \(t\) produces the displayed reciprocal sum. The renewal strong law gives \(\iota(W[1,n])/n\to1/\mu(\mathbf p)\).

Now fix an arbitrary sequence of type classes with frequencies converging to \(\mathbf p\). Generate an i.i.d. length-\(n\) word with probabilities \(\mathbf p^{(n)}=\boldsymbol\alpha^{(n)}/n\). Its realized counts differ from the required counts by a total \(\ell_1\) error \(O_{\mathbb P}(\sqrt n)\). Change exactly half that many letters, uniformly among positions with surplus symbols, to obtain the required type. The correction rule is equivariant under permutations of positions, so the corrected word is uniform in its type class. Changing one position can change the universality index by at most one: deleting that position destroys at most one block in any complete-arch decomposition, and both words have the same deletion. Hence the corrected and original indices differ by \(O_{\mathbb P}(\sqrt n)\). A uniform positive lower bound for the alphabet probabilities gives uniformly exponentially tailed arch lengths; the renewal law for the i.i.d. triangular array therefore yields the asserted convergence. Since \(0\le\iota(W_n)/n\le1/q\), convergence of its expectation follows by boundedness.

## Verification

Run `python3 verify.py` using only the Python standard library. It constructs exact integer coefficients for the independent multivariate arch and remainder inventories and compares them with exhaustive direct subsequence tests. Complete checks cover \(q=2\) through length \(13\), \(q=3\) through length \(8\), and \(q=4\) through length \(7\), totaling 48,069 finite words and 1,586 composition-index coefficient cells. The binary maximal-index and first-moment identities are also tested in every applicable cell. Finite checks corroborate the algebraic proof; they are not used as evidence of an infinite exhaustive census.

## Relationship to prior work

Barker and collaborators (2020) formalized scattered-factor universality and greedy-arch methods. Adamson (2023) gave length- and index-based counting, ranking, and unranking algorithms for universality, but no composition-refined enumerator or fixed-composition limit law in the inspected article. Fazekas, Huang and Mercaş (2026) study existential and universal indices within finer binary Parikh-matrix classes (which also fix an ordered-pair subsequence count), not the complete composition-index frequency distribution or its law of large numbers. The present theorem uses established arch factorization but provides an explicit letter-by-letter rational enumerator and exact type-class consequences. The unrestricted binary index series follows as the specialization \(x=y=z\), and is not claimed separately as new.

## Limitations

The limit theorem assumes every letter retains positive limiting frequency; it does not describe sparse types with vanishing frequencies. No asymptotic variance, central limit theorem, or uniqueness of equivalent published formulas is claimed. The formulas are mathematically checked in this work but have not received independent external audit.

## References

1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, first publicly posted 2020-03-10, https://arxiv.org/abs/2003.04629 .
2. D. Adamson, *Ranking and Unranking k-subsequence universal words*, first publicly posted 2023-04-10, https://arxiv.org/abs/2304.04583 .
3. S. Z. Fazekas, X. Huang, R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, first publicly posted 2026-10-05, https://arxiv.org/abs/2610.06717 .
