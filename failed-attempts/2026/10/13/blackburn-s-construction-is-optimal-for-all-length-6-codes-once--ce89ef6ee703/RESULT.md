# Blackburn's construction is optimal for all length-\(6\) codes once \(q\ge10\)
## Finding
Let \(S(q,6)\) be the maximum cardinality of a \(q\)-ary non-overlapping code of length \(6\). For every integer \(q\ge10\),
\[
S(q,6)=\max_{1\le \ell<q}\ell^5(q-\ell).
\]
Thus Blackburn's \(k=5\) construction is optimal for every alphabet size \(q\ge10\).

## Assumptions and scope
A code \(C\subseteq\Sigma^6\) is non-overlapping if no nonempty proper prefix of any codeword is a suffix of any, not necessarily distinct, codeword. The alphabet has size \(q\).

Stanovnik, Moškon, and Mraz prove that \(S(q,n)\) is the optimum of the integer program
\[
\max \sum_{i=1}^{n-1}x_i y_{n-i},
\]
subject to
\[
x_1+y_1=q,\qquad
x_i+y_i=\sum_{j=1}^{i-1}x_jy_{i-j},
\]
with \(x_1,y_1>0\) and all other variables nonnegative integers. Their construction also realizes every feasible size vector by suitable set partitions. Blackburn's \(k=n-1\) construction gives the lower bound
\[
S(q,6)\ge \max_{1\le\ell<q}\ell^5(q-\ell).
\]

The claim concerns all \(q\ge10\). It does not classify maximum codes or their number, and it makes no new assertion for \(q<10\).

## Proof
By the left-right symmetry of the size recurrence, assume
\[
a=x_1\le y_1=b,\qquad a+b=q.
\]
Put
\[
p=\frac aq,\qquad 0<p\le\frac12.
\]
For the remaining recurrence levels write
\[
x_2=rab,\qquad
x_3=sT_3,\qquad
x_4=tT_4,
\]
where
\[
T_3=ay_2+x_2b,\qquad
T_4=ay_3+x_2y_2+x_3b
\]
and
\[
0\le r,s,t\le1.
\]
These parameters cover the continuous relaxation of every feasible integer solution.

Let
\[
T_5=ay_4+x_2y_3+x_3y_2+x_4b.
\]
For fixed earlier levels the last contribution is
\[
a y_5+b x_5,\qquad x_5+y_5=T_5.
\]
Since \(b\ge a\), it is maximized by \(x_5=T_5\). After dividing the resulting objective by \(q^6\), denote the polynomial in \(p,r,s,t\) by \(F\).

Two exact polynomial inequalities are certified in `certificate.json` and replayed from rational arithmetic in `verify.py`:
\[
F(p,r,s,t)\le p(1-p)^5
\quad\text{for }0\le p\le\frac15,
\]
and
\[
F(p,r,s,t)\le\frac{1024}{15625}
\quad\text{for }\frac15\le p\le\frac12.
\]
For the first inequality, after the affine substitution \(p=u/5\), all \(168\) tensor-product Bernstein coefficients of the difference are nonnegative. For the second, the box is split only at \(r,s,t=1/2\); on each of the eight subboxes, all \(168\) exact rational Bernstein coefficients of the difference are nonnegative. Since Bernstein basis functions are nonnegative and sum to one, these coefficient checks prove the inequalities on the complete continuous domains, not merely on a finite sample.

If \(p\le1/5\), then
\[
|C|\le q^6p(1-p)^5=a b^5,
\]
which is one of the values in \(\max_\ell \ell^5(q-\ell)\).

Now suppose \(p\ge1/5\). Write
\[
q=5k+r,\qquad 0\le r\le4.
\]
For \(q\ge10\), one has \(k\ge2\). Choosing
\[
q-\ell=k,\qquad \ell=4k+r
\]
in Blackburn's construction gives \(k(4k+r)^5\). Exact expansion shows
\[
15625\,k(4k+r)^5-1024(5k+r)^6\ge0
\]
for every \(k\ge2\) and \(0\le r\le4\): after substituting \(k=h+2\), every coefficient is nonnegative. Hence
\[
\max_\ell \ell^5(q-\ell)\ge \frac{1024}{15625}q^6.
\]
The second Bernstein bound therefore also gives
\[
|C|\le \max_\ell \ell^5(q-\ell).
\]

This proves the upper bound for every feasible solution of the exact integer program. Blackburn's construction supplies the matching lower bound, completing the proof.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier rebuilds the normalized objective from the recurrence using exact rational multivariate polynomial arithmetic. It converts each required difference to tensor-product Bernstein form. The small-\(p\) box has \(168\) nonnegative coefficients; the middle-\(p\) region is covered by eight boxes, each with \(168\) nonnegative coefficients.

It also checks the five residue-class polynomials used for the integer Blackburn split. As a separate finite stress test, it solves the reduced exact integer program for \(2\le q\le15\); in particular it independently confirms the theorem at \(q=10,\ldots,15\).

The proof for unbounded \(q\) is the exact rational Bernstein certificate plus the symbolic residue-class argument, not extrapolation from the finite stress test.

## Relationship to prior work
Blackburn conjectured that for each fixed \(n>2\), sufficiently large alphabets have a maximum non-overlapping code from his \(k=n-1\) construction. His paper proves optimality when \(n\) divides \(q\) and gives asymptotic constant-factor control, but not an eventual exact threshold for \(n=6\).

Stanovnik, Moškon, and Mraz formulate the exact size problem as the integer program used above. Their paper proves the full formula for length \(4\), computes selected finite parameter tables, and states that no simple formula for larger lengths was obtained. It also records Blackburn's conjecture as unresolved.

The present result settles the eventual exact formula for the next even length \(6\): every \(q\ge10\) is covered by the \(k=5\) construction. Targeted searches under non-overlapping, cross-bifix-free, length-six, \(S(q,6)\), and Blackburn-conjecture formulations did not locate a published theorem giving this all-\(q\ge10\) result.

A previous finite computation available for overlap checking determines several small length-six alphabet sizes, including \(q=7,8,9\); those finite values do not imply the unbounded theorem proved here.

## Limitations
The theorem does not classify the maximum codes or enumerate them. It does not address \(n\ne6\), and it does not assert a general threshold as a function of \(n\).

The Bernstein certificate is exact but computer-assisted. Its validity depends only on rational arithmetic and the elementary Bernstein positivity criterion; the complete verifier is included.

No new small-\(q\) value is claimed. The finite \(q\le15\) replay is supplementary evidence for the exact continuous proof.

## References
1. L. Stanovnik, M. Moškon, and M. Mraz, “In search of maximum non-overlapping codes,” arXiv:2307.12593v1, first public version 2023-07-24; Designs, Codes and Cryptography 92 (2024), 1299–1326, DOI 10.1007/s10623-023-01344-z.
2. S. R. Blackburn, “Non-overlapping codes,” arXiv:1303.1026; IEEE Transactions on Information Theory 61 (2015), 4890–4894, DOI 10.1109/TIT.2015.2456634.
