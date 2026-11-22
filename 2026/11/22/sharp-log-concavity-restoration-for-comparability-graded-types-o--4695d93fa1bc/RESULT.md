# Sharp log-concavity restoration for comparability-graded types over equal-chain posets

## Finding

Let \(\mathcal P\) be the countable homogeneous universal strict partial order. For positive integers \(a,k\), take an individually named induced finite subposet \(A\) consisting of \(k\) mutually incomparable chains, each of length \(a\). Let \(c_j(a,k)\) be the number of complete nonalgebraic singleton types over \(A\) in which the new element is comparable with exactly \(j\) named elements, and put \(C_{a,k}(z)=\sum_j c_j(a,k)z^j\). Define \(U_a(z)=1+z+\cdots+z^a\).

The polynomial and its full coefficient-shape classification are
\[
 C_{a,k}(z)=2U_a(z)^k-1+k\sum_{j=2}^{a}(j-1)z^j,
\]
\[
 \boxed{\ (c_0(a,k),\ldots,c_{ak}(a,k))\text{ is log-concave}\quad\Longleftrightarrow\quad
 a\leq2\ \text{or}\ k=1\ \text{or}\ k\geq5\ \text{or}\ (a,k)=(3,4).\ }
\]
All coefficients on the support are positive. The complete classification is not asserted for nonidentical chains.

Thus, even though the grade polynomial contains an additive correction absent from the usual convolution theorem, **five equal chains always suffice for log-concavity, uniformly in their length**. Four chains do not suffice: at length four the grade-five defect equals \(-336\). The only nontrivial exception among two, three or four copies with length at least three is four copies of length three, which are log-concave.

## Assumptions and scope

The language has one irreflexive transitive binary relation, and \(A\) is pointwise named. Types are complete one-variable types not equal to a parameter. Homogeneity and universality of \(\mathcal P\) identify these types with finite induced one-point extensions. Log-concavity means \(c_j^2\ge c_{j-1}c_{j+1}\) at every internal grade with support \(0,1,\ldots,ak\). The formula and classification concern **positive integer** lengths and numbers of components.

## Proof

**1. Classification of extensions.** Let \(L\) be the named elements strictly below the new point and \(R\) those strictly above it. They must respectively be a down-set and an up-set, and every element of \(L\) must be below every element of \(R\). Conversely these conditions define a finite one-point extension and hence one nonalgebraic type. When \(L=\varnothing\) or \(R=\varnothing\), the contribution is \(2U_a(z)^k-1\). If both are nonempty, all comparable named elements lie on the **same** chain; a nonempty lower prefix of length \(p\) and upper suffix of length \(q\) are possible exactly when \(p,q\ge1\) and \(p+q\le a\). For grade \(j\) this gives \(j-1\) choices per chain, proving the displayed polynomial.

**2. The interior coefficients.** Write \(B_j=\binom{k+j-1}{j}\). For \(1\le j\le a\), the grade coefficients are
\[
 c_0=1,\qquad c_j=\beta_j:=2B_j+k(j-1).
\]
The binomial ratio identities \(B_{j-1}=B_jj/(k+j-1)\) and \(B_{j+1}=B_j(k+j)/(j+1)\) yield, for \(k\ge2\) and \(j\ge2\),
\[
 \beta_j^2-\beta_{j-1}\beta_{j+1}
 = k^2+\frac{2(k-1)B_j}{(j+1)(j+k-1)}
 \left(2B_j-k\bigl(j(k-4)-2k+2\bigr)\right).
\]
For \(2\le k\le4\), the parenthesis is positive. For \(k\ge5\), it is positive at \(j=2\) because the expression in its inner square brackets is \(-6\). At \(j\ge3\), \(B_j/j\) is nondecreasing, since \(j(k-2)\ge1\), and
\[
 \frac{B_j}{j}\ge\frac{B_3}{3}=\frac{k(k+1)(k+2)}{18}
 \ge\frac{k(k-4)}{2};
\]
indeed \((k+1)(k+2)-9(k-4)=k^2-6k+38>0\). Therefore \(2B_j\ge kj(k-4)\), making the parenthesis positive. The remaining first inequality is \(c_1^2-c_0c_2=4k^2-k(k+2)\ge0\) when \(a\ge2\). When \(a=1\), the polynomial is \(2(1+z)^k-1\) and is log-concave directly.

**3. Only one possible exceptional grade.** Let \(b_j=[z^j]U_a(z)^k\). The sequence \((b_j)\) is log-concave: \((1,\ldots,1)\) is log-concave and nonnegative log-concave sequences without internal zeros are closed under convolution (e.g. by multiplying their totally positive order-two Toeplitz matrices and applying Cauchy--Binet). All grades at least \(a+1\) have \(c_j=2b_j\); for \(j=a\), comparison with the fully untruncated \(\beta_{a+1}\) makes the log-concavity inequality strictly easier than in step 2. Thus the sole possible failure is at grade \(j=a+1\). For \(a\ge2\), with \(B=\binom{a+k}{k-1}\), the first two truncated coefficients are
\[
 b_{a+1}=B-k,\qquad b_{a+2}=B\frac{a+k+1}{a+2}-k^2,
\]
while \(b_a=B(a+1)/(a+k)\). Consequently its exact defect is
\[
 \begin{split}
 \Delta_{a,k}&:=c_{a+1}^2-c_ac_{a+2}\\
 &=\frac{2B}{(a+2)(a+k)}\bigl(2(k-1)B-k f_a(k)\bigr)
 +2k^2\bigl(k(a-1)+2\bigr),\\
 f_a(k)&=a^3+4a^2+ak^2-3ak+7a-k^2+3k.
 \end{split}
\]

**4. The sharp cutoff.** For \(k=2,3,4\), direct substitution gives, respectively,
\[
 \begin{array}{ll}
 \Delta_{a,2}=-4a(a-2),\\
 \Delta_{a,3}=-3a^3-10a^2+43a-6,\\
 \Delta_{a,4}=-(3a^4+16a^3+39a^2-370a+72)/3.
 \end{array}
\]
The first is negative precisely at \(a\ge3\). The second equals \(16\) at \(a=2\) and is negative for \(a\ge3\), as seen by writing \(a=3+y\). The third equals \(112\) at \(a=2\), \(4\) at \(a=3\), and is negative for \(a\ge4\), as seen by writing \(a=4+y\). These statements use only \(a\ge2\); the case \(a=1\) was settled above.

For \(k\ge5\), it suffices to establish \(2(k-1)\binom{a+k}{k-1}\ge kf_a(k)\). At \(k=5\) the difference is
\[
 \frac{a^4-a^3+11a^2-101a+270}{3}>0\quad (a\ge2),
\]
which follows on putting \(a=2+y\), as the numerator becomes \(y^4+7y^3+29y^2-37y+120\), and \(29y^2-37y+120>0\) for every real \(y\).

Assume the inequality for \(k\). The ratio of consecutive binomial factors is \(\binom{a+k+1}{k}/\binom{a+k}{k-1}=(a+k+1)/k\). Thus the induction step follows if
\[
 k(a+k+1)f_a(k)-(k^2-1)f_a(k+1)\ge0.
\]
Expanding gives
\[
 k^2(a-1)\bigl(k(a-1)-3a\bigr)
 +k(a^4+5a^3+11a^2+6a+1)+a^3+4a^2+5a+2.
\]
The first summand is nonnegative for \(a\ge3,k\ge5\), and also for \(a=2,k\ge6\); the single remaining pair \((a,k)=(2,5)\) makes the entire expression strictly positive directly. Hence the sufficient inequality holds for all \(a\ge2,k\ge5\), and the defect is positive. For \(k=1\), the coefficients are \(1,2,\ldots,a+1\), which are log-concave. Together these cases prove the classification.

## Verification

The included standalone `verify.py` uses exact integer arithmetic. It compares the polynomial formula to a separate exhaustive ternary relation-state enumeration for every \((a,k)\) with \(ak\le9\), compares the complete log-concavity classification for \(1\le a\le150\), \(1\le k\le25\), and checks the key induction bound over an additional finite grid. It prints `VERIFY_OK` on success. The infinite statement rests on the proof above, not on finite testing.

## Relationship to prior work

The countable generic partial order and its one-point extension realization are classical (Droste--Kuske; Pach et al.). Standard closure of log-concavity under convolution is classical (Brenti; Stanley). A previously recorded type-spectrum result for arbitrary disjoint unions of chains gives the general generating polynomial and classifies **two-chain** coefficient shapes. Neither that polynomial identity nor a conventional convolution theorem directly supplies the all-length five-component threshold: the additive two-sided correction can destroy log-concavity for two, three and four copies. The new theorem is the all-size equal-chain shape classification, not the underlying extension count or general convolution lemma.

## Limitations

This is an exact statement for equal-length chain components only. It does not classify nonuniform chain-size vectors or the finer bivariate predecessor/successor grading. Its historical originality assessment is provisional; mathematical independent audit has not been performed. The standard convolution lemma is cited and its elementary Toeplitz justification is indicated; the displayed boundary algebra is independently testable.

## References

1. M. Droste and D. Kuske, *On random relational structures*, Journal of Combinatorial Theory A **102** (2003), 241--254; lawful preliminary full text at https://eiche.theoinf.tu-ilmenau.de/kuske/Publications/random.pdf .
2. P. P. Pach, M. Pinsker, G. Pluhár, A. Pongrácz, and C. Szabó, *Reducts of the random partial order*, arXiv:1111.7109, first submitted 2011-11-30; https://arxiv.org/abs/1111.7109 .
3. F. Brenti, *Unimodal, Log-Concave and Pólya Frequency Sequences in Combinatorics*, Memoirs AMS **81** (1989), no. 413, https://doi.org/10.1090/memo/0413 .
4. R. Stanley, *Log-concave and unimodal sequences in algebra, combinatorics, and geometry*, Ann. New York Acad. Sci. **576** (1989), 500--535, https://doi.org/10.1111/j.1749-6632.1989.tb16434.x .
