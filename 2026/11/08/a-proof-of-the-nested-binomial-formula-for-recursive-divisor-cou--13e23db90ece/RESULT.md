# A proof of the nested-binomial formula for recursive divisor counts

## Finding

The finite nested-binomial formula posed as Conjecture 1 in T. M. A. Fink, *Number of ordered factorizations and recursive divisors*, is valid for **every** positive integer. Explicitly, let \(n=\prod_{j=1}^{w}p_j^{a_j}>1\) have distinct primes \(p_j\), positive integer exponents \(a_j\), and \(w\ge1\). Define the recursive-divisor function by \(\kappa_0(1)=1\) and, for \(n>1\),

\[
\kappa_0(n)=1+\sum_{d\mid n,\ d<n}\kappa_0(d).
\]

With \(I_k=i_1+\cdots+i_k\), the conjectured formula is precisely

\[
\boxed{\displaystyle
\kappa_0(n)=2^{a_w}
\sum_{i_1=0}^{a_1}\cdots\sum_{i_{w-1}=0}^{a_{w-1}}
\prod_{k=1}^{w-1}\binom{a_k}{i_k}\binom{a_{k+1}+I_k}{a_{k+1}}.}
\]

For \(w=1\), the sums and product are empty, with value \(1\), so the formula says \(\kappa_0(p^a)=2^a\). For \(n=1\), retain the definition \(\kappa_0(1)=1\) separately. Any ordering of the distinct primes gives the same value.

## Assumptions and scope

All statements are exact integer identities. There are no unproved analytic convergence assumptions: all generating functions below are formal power series over \(\mathbb Q\), and all their denominators have constant coefficient \(1\). The prime factors are arbitrary and the exponent tuple is finite. The argument also works for exponent tuples containing zeros, which is needed when extracting coefficients.

## Proof

**1. The divisor recurrence gives a multivariate generating function.** Fix \(w\) distinct primes and put \(h(\boldsymbol a)=\kappa_0(\prod_jp_j^{a_j})\) for \(\boldsymbol a=(a_1,\ldots,a_w)\in\mathbb Z_{\ge0}^{w}\). For every tuple, including the zero tuple, the recursive definition is equivalent to

\[
2h(\boldsymbol a)=1+\sum_{\boldsymbol 0\le\boldsymbol b\le\boldsymbol a}h(\boldsymbol b).
\]

Indeed, the summation on the right is the sum over all divisors, including the number itself. Let

\[
H_w(\boldsymbol x)=\sum_{\boldsymbol a\ge\boldsymbol0}
h(\boldsymbol a)\prod_{j=1}^w x_j^{a_j}.
\]

Multiplying the recurrence by the corresponding monomial and summing coefficientwise gives

\[
2H_w=\prod_{j=1}^{w}(1-x_j)^{-1}
+H_w\prod_{j=1}^{w}(1-x_j)^{-1}.
\]

Hence

\[
\boxed{H_w(\boldsymbol x)=
\frac{1}{2\prod_{j=1}^{w}(1-x_j)-1}.}\tag{1}
\]

**2. Use the symmetric form of the conjectured sum.** For each exponent tuple \(\boldsymbol a\), set \(I_0=0\), \(I_j=i_1+\cdots+i_j\), and define

\[
S_w(\boldsymbol a)=
\sum_{i_1=0}^{a_1}\cdots\sum_{i_w=0}^{a_w}
\prod_{j=1}^{w}
\binom{a_j}{i_j}\binom{a_j+I_{j-1}}{a_j}.
\tag{2}
\]

The last index \(i_w\) appears only in \(\binom{a_w}{i_w}\), and its sum is \(2^{a_w}\). The initial factor \(\binom{a_1}{a_1}=1\). Therefore (2) is **exactly** the displayed conjectured formula.

**3. Evaluate its generating function by eliminating the indices backwards.** Work in \(\mathbb Q[[x_1,\ldots,x_w]]\). Put

\[
D_{w+1}=1,\qquad
D_j=(1-x_j)D_{j+1}-x_j
\quad (j=w,w-1,\ldots,1).
\tag{3}
\]

For any nonnegative integer \(J\), any indeterminate \(x\), and any formal power series \(D\) with constant term \(1\), the binomial theorem and the negative-binomial identity give

\[
\begin{aligned}
&\sum_{a\ge0}\sum_{i=0}^{a}
\binom{a}{i}\binom{a+J}{a}x^aD^{-(J+i+1)}\\
&=D^{-(J+1)}\sum_{a\ge0}
\binom{a+J}{a}[x(1+D^{-1})]^a\\
&=[(1-x)D-x]^{-(J+1)}.
\end{aligned}
\tag{4}
\]

Formula (4) is legitimate coefficientwise: for each prescribed monomial in the \(x_j\), only finitely many terms contribute. Apply (4) for \(j=w\) with \(J=I_{w-1}\) and \(D=D_{w+1}=1\): the \(a_w,i_w\) sums in the generating function of (2) collapse to \(D_w^{-(I_{w-1}+1)}\). Continue from \(j=w-1\) to \(j=1\). After the \(a_j,i_j\) sums are eliminated, the remaining factor is \(D_j^{-(I_{j-1}+1)}\). At the final step \(I_0=0\), so

\[
\sum_{\boldsymbol a\ge\boldsymbol0}
S_w(\boldsymbol a)\prod_jx_j^{a_j}=D_1^{-1}.
\tag{5}
\]

The recurrence (3) telescopes explicitly: descending induction starting from \(D_{w+1}=1\) yields

\[
D_j=2\prod_{k=j}^w(1-x_k)-1.
\tag{6}
\]

Combining (5) and (6) makes the generating function of the finite nested sum identical to (1). Coefficient extraction proves \(S_w(\boldsymbol a)=h(\boldsymbol a)\) for **all** nonnegative tuples. Summing its last binomial index establishes Conjecture 1, as claimed. \(\square\)

## Verification

The standalone file `check_fink_conjecture.py` compares three separately coded finite definitions: the proper-divisor recurrence on exponent vectors, the conjectured nested finite sum, and the polynomial coefficient recurrence following from (1). It checks 764 positive-exponent tuples of widths one through six, plus six empty or zero-exponent controls. The saved `check_output.txt` reports their exact agreement. These computations are diagnostic only; the infinite statement follows from the formal-series proof.

To reproduce, run `python3 check_fink_conjecture.py` in a directory containing the script. It requires only the Python standard library.

## Relationship to prior work

Fink's preprint of 31 July 2023 (arXiv:2307.16691), §2 Conjecture 1 and §5, states this exact finite formula and checks it numerically up to \(10^5\), explicitly asking for a proof. The publicly accessible updated manuscript still labels it Conjecture 1. Its Theorems 1 and 2 give other, proved expressions for the **same arithmetic function**; the contribution here is a proof of their conjectured **specific positive finite expansion**, not a discovery of the arithmetic function or of its existing numerical values. The earlier paper arXiv:2307.09140 establishes related Dirichlet-series identities, and OEIS A067824 records the recursion and sequence. None of these inspected sources proves the finite nested-binomial transformation. MacMahon's alternating sum, cited in Fink, is a different representation and is not treated here as an independently verified proof of the conjecture.

## Limitations

This result concerns \(\kappa_0\), not the \(\kappa_x\) family for arbitrary parameters. It does not imply new asymptotic estimates for the ordered-factorization function, nor does it establish independent novelty against every unindexed manuscript. It makes no independent-audit or formal-machine-certification claim. Computational tests cover only finite tuples; all unbounded quantifiers rely on the displayed proof.

## References

1. T. M. A. Fink, *Number of ordered factorizations and recursive divisors*, arXiv:2307.16691, first version 31 July 2023, especially Conjecture 1 and discussion; open manuscript: https://arxiv.org/abs/2307.16691; later full manuscript: https://lims.ac.uk/documents/paper-number-of-ordered-factorizations-and-recursive-divisors.pdf.
2. T. M. A. Fink, *Properties of the recursive divisor function and the number of ordered factorizations*, arXiv:2307.09140, 18 July 2023, https://arxiv.org/abs/2307.09140.
3. OEIS Foundation, A067824, recursive divisor counts, https://oeis.org/A067824.
4. P. A. MacMahon, *Memoir on the theory of the compositions of numbers* (1893), historical alternating-sum result as cited and displayed in reference 1; the original article was not independently inspected.
