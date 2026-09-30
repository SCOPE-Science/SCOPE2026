# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** For \(A,B\in\mathcal S_4\), Schatten Hölder places every quartic
word used in the proof in \(\mathcal S_1\), so the trace expansions and
cyclic permutations are valid. Under \(AB=BA\), direct expansion gives
\[
\operatorname{Tr}([A^*,A][B^*,B])
=
\operatorname{Tr}([A^*,B]^*[A^*,B]).
\]
Applying this pairwise yields the stated Gram identity. Consequently, if the
sum of the self-commutators is zero, its squared Hilbert--Schmidt norm is a
sum of nonnegative squared Hilbert--Schmidt norms of all cross-commutators,
forcing each one to vanish.

For the sum-hyponormal corollary, \(\mathcal S_2\)-membership makes each
self-commutator trace class. Positivity of their sum together with trace
zero forces the sum to vanish, after which the Schatten-four identity
applies. The conclusion is therefore stronger than coordinatewise
normality: the tuple is doubly commuting.

## Originality

**PASS, to the best of our knowledge.** The motivating source,
arXiv:2609.19287v1, explicitly asks whether every sum-normal tuple is normal
(Question 1.3(ii)) and states near the end that a nonnormal sum-normal tuple
is still unknown. It records only the trace-class observation that
sum-hyponormality then implies sum-normality; it does not state a
Schatten-four or Hilbert--Schmidt result.

The comparison included exact and synonymous searches around products of
self-commutators, cross-commutators, Hilbert--Schmidt/Schatten conditions,
and sum-normality. Curto--Jian (1994) establish a different matricial
identity tied to Taylor invertibility. Misra--Pramanick--Sinha (2022)
study the determinant of the block commutator matrix and associated trace
inequalities. Neither located statement gives the pair trace identity or
the resulting exact energy formula.

A residual bibliographic risk remains: literature on Hilbert modules,
essential normality, and Schatten-class cross-commutators is broad, and an
equivalent special case of the pair identity may have appeared in a
different language. Accordingly, the originality claim is limited to the
full theorem package and its application to the newly posed sum-normal
question, rather than claiming that every algebraic ingredient is
historically new.

## Value

**PASS.** The result gives an exact quantitative identity rather than only a
qualitative sufficient condition:
\[
\left\|\sum_j[T_j^*,T_j]\right\|_2^2
=
\sum_{j,k}\|[T_j^*,T_k]\|_2^2.
\]
It answers the new general sum-normal question on a large classical
operator ideal, shows the matrix of squared cross-commutator norms is
positive semidefinite, and upgrades the source paper's trace-class
observation to a Hilbert--Schmidt sum-hyponormal normality theorem.

## Limitations

The \(\mathcal S_4\) hypothesis is not claimed optimal. The result does not
settle arbitrary compact sum-normal or sum-hyponormal tuples, and it gives
no counterexamples or classification outside the stated Schatten classes.
Independent audit has not been performed.
