# Zero lower density for ternary elated numbers with an exponentially sparse-scale bound

## Finding
Let \(n=\sum_{i=0}^{\ell-1} a_i3^i\ge1\), \(a_{\ell-1}\in\{1,2\}\), and \(0\le a_i\le2\). Define the *ternary elated map*
\[E(n)=a_{\ell-1}\sum_{i=0}^{\ell-1}a_i^2.\]
A positive integer is *ternary elated* if some iterate of \(E\), including the zero-th, equals \(1\). Let \(A(X)\) denote the number of ternary elated positive integers at most \(X\).

For every integer \(r\ge3\) set \(B_r=3^r\), \(k_r=(3B_r-1)/2\), \(M_r=\lfloor k_r/20\rfloor\), \(X_r=3^{k_r}-1\). Then
\[ A(X_r)\le3^{k_r-M_r}+2\cdot3^{k_r}e^{-B_r/192}. \tag{1}\]
In particular,
\[\liminf_{X\to\infty}\frac{A(X)}{X}=0.\]
Thus if the natural density exists it must equal zero. The estimate is along the explicitly defined subsequence, not at all scales.

## Assumptions and scope
All integers are positive unless otherwise specified. The leading digit is the highest nonzero digit in the usual base-three expansion. The function is *leading-digit times the sum of digit squares*, not the ordinary happy-number map and not a digit sum of powers of the integer itself. The concentration step uses only independent uniform lower digits conditional on a fixed length and leading digit.

## Proof
**Parity obstruction.** Since \(3\equiv1\pmod2\) and \(a_i^2\equiv a_i\pmod2\), the digit-square sum \(S(n)=\sum_i a_i^2\) has \(S(n)\equiv n\pmod2\). Therefore \(E(n)\equiv a_{\ell-1}n\pmod2\). Every even integer remains even under iteration, and every integer with leading ternary digit \(2\) maps to an even integer. Consequently neither can be ternary elated. Moreover, if \(n\) starts with digit \(1\) and \(S(n)\) starts with digit \(2\), its second iterate is even and it is not elated.

**Concentration.** Fix \(r\ge3\), abbreviate \(B=B_r\), \(k=k_r\), \(M=M_r\), and consider a uniformly chosen \(\ell\)-digit ternary integer starting with \(1\), where \(k-M\le\ell\le k\). The lower \(\ell-1\) digits \(D_i\) are independent and uniform on \(\{0,1,2\}\); hence
\[S=1+\sum_{i=1}^{\ell-1}D_i^2,\qquad \mu_\ell=\mathbb ES=1+\frac53(\ell-1)=\frac{5\ell-2}{3}.\]
Because \(M\le k/20\), \(k=(3B-1)/2\), and \(B\ge27\),
\[\frac94B\le\mu_\ell\le\frac{11}4B.\tag{2}\]
Indeed the lower bound follows from \(\mu_\ell\ge(19/8)B-35/24\ge(9/4)B\), and the upper bound from \(\mu_\ell\le(5/2)B-3/2<(11/4)B\). Thus if \(|S-\mu_\ell|<B/4\), then \(2B<S<3B\); the leading ternary digit of \(S\) is \(2\), so the original integer is not ternary elated.

The variables \(D_i^2\) lie in \([0,4]\). Hoeffding's inequality and \(\ell-1<3B/2\) give
\[\Pr\{|S-\mu_\ell|\ge B/4\}\le2\exp\left(-\frac{B^2}{128(\ell-1)}\right)\le2e^{-B/192}.\tag{3}\]
There are fewer than \(3^{k-M}\) positive integers of ternary length below \(k-M\). All remaining potentially elated integers in \([1,3^k-1]\) have a leading digit \(1\) and length between \(k-M\) and \(k\). Applying (3) separately to each length and summing the counts gives at most \(2e^{-B/192}\sum_{\ell=k-M}^{k}3^{\ell-1}\le2\cdot3^k e^{-B/192}\) exceptional integers. Adding the shorter integers proves (1).

Finally \(k_r\to\infty\), \(M_r\to\infty\), and \(B_r\to\infty\), so division by \(X_r=3^{k_r}-1\) makes the right-hand side tend to zero. The density ratios are nonnegative, proving the stated lower limit. \(\square\)

## Verification
The independent standard-library checker `verify.py` verifies the parity obstruction on all \(1\le n\le10000\) and checks the exact rational mean interval (2) for every \(3\le r\le50\). It also evaluates sample numerical bounds. These finite tests do not establish the infinite theorem: that follows from the elementary inequalities and Hoeffding estimate (3). Run `python verify.py`; the expected output is provided in `verification_output.txt`.

## Relationship to prior work
Fox, Fox, Grundman, Lynn, Namoijam and Vanderschoot (2024) introduced the elated map, proved the leading-digit parity obstruction in their Lemma 3, and explicitly asked in Section 6 whether natural densities of elated numbers exist. Their finite cycle classification and arbitrarily long arithmetic progressions do not provide the concentration or subsequence-density result above. The present contribution combines the published parity obstruction with a probabilistic digit-square concentration argument to prove a new necessary conclusion for that density problem. This does not imply that the full density exists.

## Limitations
Only ternary elated numbers are treated. The conclusion is a zero **lower** asymptotic density, not zero upper density, not an actual density value unless existence is separately established, and not a proof that the set is globally sparse at every scale. The concentration estimate does not classify all elated integers or basins. Unindexed equivalent results remain possible.

## References
Fox, N. Bradley; Fox, Nathan H.; Grundman, Helen G.; Lynn, Rachel; Namoijam, Changningphaabi; Vanderschoot, Mary. *Elated Numbers*, arXiv:2409.09863v1, first public 2024-09-15, https://arxiv.org/abs/2409.09863 (particularly Lemma 3 and Section 6); open-access later version, https://link.springer.com/article/10.1007/s44007-025-00185-7.

Hoeffding, W. *Probability Inequalities for Sums of Bounded Random Variables*, Journal of the American Statistical Association 58 (1963), 13–30. Standard bounded-independent-variable inequality.
