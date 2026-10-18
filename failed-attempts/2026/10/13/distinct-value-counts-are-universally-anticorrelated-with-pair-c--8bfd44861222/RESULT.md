# Distinct-value counts are universally anticorrelated with pair collisions

## Finding

Let
\[
X_1,\ldots,X_n
\]
be iid from a finite categorical distribution
\[
p=(p_1,\ldots,p_m),
\qquad
p_i\ge0,
\qquad
\sum_{i=1}^m p_i=1,
\]
with \(n\ge2\) and at least two positive masses.

Define the number of observed categories
\[
K_n=\#\{X_1,\ldots,X_n\},
\]
the number of matching sample pairs
\[
C_n=
\sum_{1\le a<b\le n}
\mathbf1\{X_a=X_b\},
\]
and the population pair-collision probability
\[
q_2=\sum_{i=1}^m p_i^2.
\]

Then
\[
\boxed{
\operatorname{Cov}(K_n,C_n)
=
\binom n2
\sum_{i=1}^m
p_i(1-p_i)^{n-2}
\bigl[p_i-(2-p_i)q_2\bigr].
}
\tag{1}
\]

Moreover,
\[
\boxed{
\operatorname{Cov}(K_n,C_n)<0
}
\tag{2}
\]
for every nondegenerate finite categorical law.

Thus the negative dependence is not a symmetry artifact of the classical uniform birthday model: it survives arbitrary heterogeneity of category probabilities.

For the uniform law on \(m\ge2\) categories,
\[
p_i=\frac1m,
\]
equation (1) reduces to
\[
\boxed{
\operatorname{Cov}(K_n,C_n)
=
-\frac{\binom n2}{m}
\left(1-\frac1m\right)^{n-1}.
}
\tag{3}
\]

There is also a sharp critical-scale consequence. If
\[
m\to\infty,
\qquad
\frac{n}{\sqrt m}\to c\in(0,\infty),
\]
then
\[
\boxed{
C_n-(n-K_n)\longrightarrow0
\quad\text{in }L^2
}
\tag{4}
\]
and consequently
\[
\boxed{
\operatorname{Corr}(K_n,C_n)\longrightarrow-1.
}
\tag{5}
\]

So at birthday scale, the pair-collision count and the number of occupied categories become asymptotically the same information with opposite sign after centering.

## Assumptions and scope

The exact covariance and sign theorem, equations (1)--(2), hold for every fixed finite categorical law with at least two positive masses and every integer \(n\ge2\).

Zero-probability categories may be deleted without changing the statement.

The critical-scale statements (4)--(5) are only asserted for the uniform law with the number \(m\) of categories tending to infinity and \(n/\sqrt m\) tending to a finite positive constant.

Here, \(C_n\) counts matching unordered pairs. This differs from the classical sequential occupancy collision count
\[
n-K_n,
\]
which counts repeat observations after their first occurrence. The distinction matters exactly when a category is sampled at least three times.

## Proof

For category \(i\), let
\[
I_i=\mathbf1\{\text{category }i\text{ appears among }X_1,\ldots,X_n\}.
\]
Then
\[
K_n=\sum_{i=1}^m I_i.
\]

For a fixed sample pair \(e=\{a,b\}\), write
\[
Y_e=\mathbf1\{X_a=X_b\}.
\]
Then
\[
C_n=\sum_e Y_e,
\qquad
\mathbb E Y_e=q_2.
\]

Fix \(i\) and \(e\). Conditional on the pair matching, either the common value is \(i\), with probability contribution \(p_i^2\), or it is some other category and category \(i\) appears among the remaining \(n-2\) observations. Hence
\[
\mathbb E[I_iY_e]
=
p_i^2
+
(q_2-p_i^2)
\bigl[1-(1-p_i)^{n-2}\bigr].
\]
Also,
\[
\mathbb E I_i=1-(1-p_i)^n.
\]
Subtracting
\[
\mathbb E I_i\,\mathbb E Y_e
\]
gives
\[
\operatorname{Cov}(I_i,Y_e)
=
p_i(1-p_i)^{n-2}
\bigl[p_i-(2-p_i)q_2\bigr].
\tag{6}
\]
Summing (6) over the \(m\) categories and the \(\binom n2\) sample pairs proves (1).

It remains to prove the universal sign.

Put
\[
r=n-2,
\qquad
w_i=p_i(2-p_i),
\qquad
f_i=\frac{p_i}{2-p_i},
\qquad
g_i=(1-p_i)^r.
\]
Let
\[
W=\sum_iw_i=2-q_2
\]
and let expectation \(\mathbb E_w\) refer to the probability weights \(w_i/W\).

The sum in (1), before multiplication by \(\binom n2\), is
\[
W\left(
\mathbb E_w[f g]
-
q_2\mathbb E_w[g]
\right).
\tag{7}
\]

As a function of \(p_i\), \(f_i\) is increasing while \(g_i\) is decreasing. Therefore the elementary weighted rearrangement inequality gives
\[
\operatorname{Cov}_w(f,g)\le0.
\]
Equivalently,
\[
\frac{\mathbb E_w[fg]}{\mathbb E_w[g]}
\le
\mathbb E_w[f].
\tag{8}
\]
But
\[
\mathbb E_w[f]
=
\frac{\sum_i p_i^2}{2-q_2}
=
\frac{q_2}{2-q_2}.
\tag{9}
\]
For a nondegenerate categorical law,
\[
0<q_2<1,
\]
and therefore
\[
\frac{q_2}{2-q_2}<q_2.
\tag{10}
\]
Combining (8)--(10) in (7) proves strict negativity.

For the uniform law,
\[
q_2=\frac1m,
\]
and substitution in (1) immediately gives (3).

For the critical-scale result, let \(N_i\) be the occupancy of category \(i\). The sequential repeat count is
\[
n-K_n=\sum_i(N_i-1)_+.
\]
The discrepancy between pair matches and repeats is
\[
C_n-(n-K_n)
=
\sum_i
\left[
\binom{N_i}{2}-(N_i-1)_+
\right]
=
\sum_i
\binom{N_i-1}{2}\mathbf1\{N_i\ge3\}.
\tag{11}
\]
It is nonnegative and bounded by the number \(T_n\) of colliding sample triples,
\[
T_n=
\sum_{1\le a<b<c\le n}
\mathbf1\{X_a=X_b=X_c\}.
\tag{12}
\]

Under the uniform law,
\[
\mathbb E T_n=\binom n3m^{-2}.
\]
For two distinct triples, their intersection can have zero, one, or two sample indices. The corresponding joint collision probabilities are respectively
\[
m^{-4},
\qquad
m^{-4},
\qquad
m^{-3}.
\]
The numbers of ordered triple pairs in these three cases are respectively
\[
O(n^6),
\qquad
O(n^5),
\qquad
O(n^4).
\]
Thus
\[
\mathbb E T_n^2
=
O\left(
\frac{n^3}{m^2}
+
\frac{n^4}{m^3}
+
\frac{n^5}{m^4}
+
\frac{n^6}{m^4}
\right).
\]
When \(n=O(\sqrt m)\), every term tends to zero. By (11)--(12),
\[
\mathbb E\left[C_n-(n-K_n)\right]^2
\le
\mathbb E T_n^2
\longrightarrow0,
\]
which proves (4).

Finally, in the uniform model the pair indicators in \(C_n\) are pairwise independent, including pairs that share one sample index. Hence
\[
\operatorname{Var}(C_n)
=
\binom n2
\frac1m
\left(1-\frac1m\right)
\longrightarrow
\frac{c^2}{2}.
\]
Together with (4), this implies
\[
\operatorname{Var}(n-K_n)\to\frac{c^2}{2}
\]
and
\[
\operatorname{Cov}(n-K_n,C_n)\to\frac{c^2}{2}.
\]
Since \(K_n=n-(n-K_n)\), equation (5) follows.

## Verification

The accompanying checker exhaustively enumerates iid samples for several nonuniform rational probability vectors and sample sizes. It computes the sample probability of every word exactly with rational arithmetic and compares the resulting covariance to equation (1).

The checker also verifies the weighted rearrangement proof algebraically on the same nonuniform profiles, checks the uniform specialization (3), and independently checks the exact variance of the uniform pair-collision count.

For several critical birthday scalings, a high-precision calculation evaluates the exact uniform covariance and variance formulas and confirms convergence of the correlation toward \(-1\).

The finite checks are supplementary. Equations (1)--(5) are proved analytically above.

## Relationship to prior work

Camarri and Pitman study birthday repeats for arbitrary discrete probability distributions, including unequal probabilities, and characterize repeat-time limits. Their object is the sequential repeat process rather than the finite-sample covariance between the number of distinct observed values and the number of matching pairs.

Chatterjee, Diaconis, and Meckes study Poisson approximation for the birthday problem. In the uniform model they explicitly distinguish the number of boxes with at least two balls from the number of matching pairs, and observe that the two coincide when there are no triple occupancies. Their analysis does not state equation (1), the heterogeneous sign theorem (2), or the exact covariance (3).

Hwang and Janson develop local limit theory for the number of occupied urns in finite and infinite occupancy schemes. Their full text treats the occupied-count marginal and does not treat the pair-collision covariance. Their paper lists \(60C05\) among its primary MSC classifications.

Arratia, Garibaldi, and Kilian define the classical sequential collision count exactly as the number of balls minus the number of occupied bins. That is the quantity \(n-K_n\) used in (4), not the pair-match count \(C_n\). Their collision-process embedding therefore complements rather than subsumes the exact mixed covariance in (1).

The present theorem links these two standard occupancy summaries at finite sample size and shows that their negative relation survives arbitrary category heterogeneity.

## Limitations

The sign theorem is proved here for finite categorical laws. Extending the exact formula to countably infinite support is plausible under direct summability arguments but is not claimed.

The asymptotic perfect anticorrelation in (5) is a uniform birthday-scale statement. No analogous \(-1\) limit is asserted for arbitrary triangular arrays of nonuniform probability vectors.

The covariance is a second-order dependence statement; it does not imply negative association between all increasing functions of \(K_n\) and \(C_n\).

The birthday and occupancy literature is extensive. The closest full sources were compared at the level of the actual statistics and implications, but an older equivalent covariance formula under different terminology remains a residual bibliographic risk.

## References

1. M. Camarri and J. Pitman, “Limit distributions and random trees derived from the birthday problem with unequal probabilities,” Berkeley Statistics Technical Report 523, first public 1998-06-01; *Electronic Journal of Probability* 5 (2000).
2. S. Chatterjee, P. Diaconis, and E. Meckes, “Exchangeable pairs and Poisson approximation,” arXiv:math/0411525, first public 2004-11-23; *Probability Surveys* 2 (2005), 64–106.
3. H.-K. Hwang and S. Janson, “Local limit theorems for finite and infinite urn models,” arXiv:math/0604397, first public 2006-04-18; *Annals of Probability* 36 (2008), 992–1022.
4. R. Arratia, S. Garibaldi, and J. Kilian, “Asymptotic distribution for the birthday problem with multiple coincidences, via an embedding of the collision process,” arXiv:1310.7055, first public 2013-10-26; *Random Structures & Algorithms* 48 (2016), 480–502.
