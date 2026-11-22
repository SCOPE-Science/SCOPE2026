# Sharp multiplicative-orbit collapse for five-nondivisible three-central binomial coefficients

## Finding

Define the integral three-central binomial coefficients by
\[
(1-9z)^{-1/3}=\sum_{n\geq0}c(n,3)z^n,
\qquad c(0,3)=1.
\]
Let \(E=\{n\in\mathbb Z_{\geq0}:5\nmid c(n,3)\}\). For \(m\in\{2,3\}\), put \(E_m=\{n\in E:mn\in E\}\), and set
\[
A_2=\{0,1,3\},\qquad A_3=\{0,1,2\}.
\]
Then, **for both multipliers**,
\[
\boxed{E_m=\left\{\sum_{j\geq0}a_j25^j:
 a_j\in A_m,\quad a_j=0\text{ for all sufficiently large }j\right\}.}
\]
Consequently, for every integer \(r\geq0\),
\[
\boxed{\#(E_m\cap[0,25^r))=3^r.}
\]
Despite these infinitely large pair intersections, every *three-step geometric orbit* is excluded except the trivial one:
\[
\boxed{\{n\geq0:n,mn,m^2n\in E\}=\{0\}\quad(m=2,3).}
\]
Both statements also hold in the precise five-adic sense: if
\[
\Sigma=\left\{\sum_{i\geq0}a_i5^i\in\mathbb Z_5:
 a_{2j}\in\{0,1,2,3\},\ a_{2j+1}\in\{0,1\}\right\},
\]
then
\[
\Sigma\cap m^{-1}\Sigma
 =\left\{\sum_{j\geq0}a_j25^j\in\mathbb Z_5:a_j\in A_m\right\},
\qquad
\Sigma\cap m^{-1}\Sigma\cap m^{-2}\Sigma=\{0\}.
\]
Here \(m^{-1}\Sigma=\{x\in\mathbb Z_5:mx\in\Sigma\}\). The two pair intersections are uncountable, both of Hausdorff dimension \(\log_{25}3\) in the usual five-adic metric; the triple intersections have dimension zero. The collapse is sharp among integer ratios greater than one: the ratio \(4\) admits the nonzero orbit \(2,8,32\), and all three indices belong to \(E\).

## Assumptions and scope

The statement concerns integral coefficients \(c(n,3)\) at the fixed prime \(5\), both for ordinary nonnegative indices and for the explicitly defined five-adic digit-set extension. Nonnegative indices have finite base-five expansions; five-adic integers may have infinite expansions. No claim is made concerning the full five-adic interpolation of \(c(n,3)\) as a function on \(\mathbb Z_5\): only the index digit-set closure is used. The Hausdorff dimension uses \(|5|_5=1/5\).

## Proof

**1. Reduction to alternating digits.** The coefficient recurrence is
\[
(n+1)c(n+1,3)=3(3n+1)c(n,3).
\]
The prime-five unit criterion follows from the valuation formula of Straub–Amdeberhan–Moll, Theorem 3.2 and its specialization Theorem 3.5: if \(n=\sum a_i5^i\), then \(5\nmid c(n,3)\) exactly when \(a_{2j}\leq3\) and \(a_{2j+1}\leq1\) for every \(j\). To see the digit thresholds directly from the inverse-of-three description, note
\[
\frac13=1+\sum_{j\geq0}\left(5^{2j}+3\cdot5^{2j+1}\right)
\quad\text{in }\mathbb Z_5,
\]
so the inverse-of-three digit offsets are alternately \(1\) and \(3\). The no-carry inequalities are exactly \(a_{2j}+1<5\), \(a_{2j+1}+3<5\). This also defines \(\Sigma\) without referring to an interpolation of the coefficient function.

**2. Two-point structure.** Work from the least significant digit upward. At each even digit, the incoming multiplication carry is zero (initially so). For \(m=2\) the allowable even digit \(a\in\{0,1,2,3\}\) must produce an allowable even output \((2a)\bmod5\leq3\); thus \(a\in\{0,1,3\}\), and the outgoing carry is \(0,0,1\), respectively. At the following odd position \(b\in\{0,1\}\), the output digit is \(2b+c\), with \(c\in\{0,1\}\); requiring it at most one forces \(b=0\), and the outgoing carry becomes zero. The same argument for \(m=3\) gives allowed even digits \(a\in\{0,1,2\}\) with carries \(0,0,1\), and the odd output \(3b+c\leq1\) again forces \(b=0\) and resets the carry. These inductions work unchanged for infinite digit expansions. Hence the pair sets are precisely the independent base-25 digit choices stated above.

**3. Three-point obstruction.** Suppose a nonzero \(x\) belongs to \(\Sigma\cap m^{-1}\Sigma\), and choose the least \(j\) for which the base-25 digit \(a_j\) is nonzero. Lower input digits vanish, so the first two base-five digits of \(m^2x\) at positions \(2j,2j+1\) are exactly those of \(m^2a_j\). For \(m=2\), \(a_j\in\{1,3\}\): the products \(4\) and \(12=(22)_5\) violate the even-digit or odd-digit restriction, respectively. For \(m=3\), \(a_j\in\{1,2\}\): the products \(9=(14)_5\) and \(18=(33)_5\) also violate the even-digit or odd-digit restriction. Thus \(m^2x\notin\Sigma\). This proves both triple intersections are exactly \(\{0\}\). The same least-nonzero-digit argument applies to finite nonnegative indices.

**4. Cardinality, dimension, sharpness.** Each of the \(r\) independent base-25 positions has exactly three choices, yielding \(3^r\) indices below \(25^r\). For the five-adic closure the \(3^r\) level-\(r\) cylinder balls have radius \(25^{-r}\). Their upper bound gives dimension at most \(\log_{25}3\); the equidistributed Bernoulli measure on these cylinders yields the matching lower bound, since every smaller ball meets at most one cylinder at its relevant depth and its measure is bounded by a fixed constant times the radius to that exponent. The zero set has dimension zero. Finally, \(2=(2)_5\), \(8=(13)_5\), and \(32=(112)_5\) all satisfy the alternating digit restriction, proving existence of a positive orbit of length three for ratio four.

## Verification

The standalone `check.py` implements the exact recurrence-derived valuation identity
\[
\nu_5(c(n,3))-\nu_5(c(n-1,3))
=\nu_5(3n-2)-\nu_5(n)\quad(n\geq1).
\]
It independently tests the digit criterion against actual valuation computations, all pair languages and triple exclusions for \(0\leq n<5^6\), the finite pair counts at depths \(r=0,1,2,3\), the local transition table and the ratio-four witness. Run `python3 check.py`. Its successful output reports 281275 exact assertions. The unrestricted statements follow from the preceding digit-by-digit proof, not from finite testing.

## Relationship to prior work

The prime-five digit criterion is *not new*: it is a specialization of Straub, Amdeberhan and Moll (2008), Theorems 3.2 and 3.5. The new assertion is the evaluated pair/triple multiplicative-orbit law, including the exact base-25 languages and immediate collapse at the third orbit position. Abram and Lagarias (2013), and Abram, Bolshakov and Lagarias (2015), develop related finite-automaton and Hausdorff-dimension methods for intersections of multiplicative translates of the **three-adic** Cantor set, not this alternating-digit five-adic index set or the stated exact pair/triple classification. General p-adic path-set theory is relevant methodological context. The classification is verified by a direct carry argument, not by assuming any classification theorem from those sources.

## Limitations

The source digit characterization implies the result once the displayed specific carry analysis is performed; the scope of originality is the new evaluated multiplicative-intersection classification, not a new unit criterion or a new general path-set framework. The dimension is only for the index digit sets, not for coefficient-value images. No arbitrary multiplier, prime, or higher valuation is classified. A sufficiently broad unlocated general p-adic intersection result may contain this case; independent priority verification is outstanding.

## References

1. A. Straub, T. Amdeberhan and V. H. Moll, *The p-adic valuation of k-central binomial coefficients*, arXiv:0811.2028v1, submitted 13 November 2008, https://arxiv.org/html/0811.2028v1 (especially Theorems 3.2, 3.5 and 3.7).
2. W. Abram and J. C. Lagarias, *Intersections of multiplicative translates of 3-adic Cantor sets*, arXiv:1308.3133, first submitted 14 August 2013, https://arxiv.org/abs/1308.3133 (Sections 1–3, 5).
3. W. C. Abram, A. Bolshakov and J. C. Lagarias, *Intersections of multiplicative translates of 3-adic Cantor sets II: two infinite families*, arXiv:1508.05967, submitted 24 August 2015, https://arxiv.org/abs/1508.05967 (Sections 1–3, 6).
