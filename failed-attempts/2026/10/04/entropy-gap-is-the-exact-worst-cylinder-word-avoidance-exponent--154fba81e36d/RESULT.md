# Entropy gap is the exact worst-cylinder word-avoidance exponent in entropy-minimal bi-balanced shifts
## Finding
Let \(X\) be an irreducible entropy-minimal bi-balanced two-sided shift over a finite alphabet. Fix an admissible word \(v\in\mathcal B(X)\), and define
\[
D_n(v)=\{w\in\mathcal B_n(X):v\text{{ is not a subword of }}w\}.
\]
Let
\[
Y_v=\{x\in X:v\text{{ never occurs in }}x\}.
\]
Write \(h=h(X)\). If \(Y_v\neq\varnothing\), write \(h_v=h(Y_v)\) and \(\Delta_v=h-h_v>0\). If \(Y_v=\varnothing\), set \(h_v=-\infty\) and \(\Delta_v=+\infty\).

Choose a common balance constant \(c>0\) such that for every admissible word \(u\) and every \(n\ge 0\),
\[
|\mathcal F_n(u,X)|\ge c|\mathcal B_n(X)|,\qquad |\mathcal P_n(u,X)|\ge c|\mathcal B_n(X)|.
\]
Define the worst follower and predecessor avoidance fractions
\[
a_n^+(v)=\sup_{u\in\mathcal B(X)}\frac{|\mathcal F_n(u,X)\cap D_n(v)|}{|\mathcal F_n(u,X)|},
\]
\[
a_n^-(v)=\sup_{u\in\mathcal B(X)}\frac{|\mathcal P_n(u,X)\cap D_n(v)|}{|\mathcal P_n(u,X)|}.
\]
Then for both signs,
\[
\frac{|D_n(v)|}{|\mathcal B_n(X)|}\le a_n^\pm(v)\le \frac1c\frac{|D_n(v)|}{|\mathcal B_n(X)|}.
\]
Consequently, if \(Y_v\neq\varnothing\),
\[
\lim_{n\to\infty}-\frac1n\log a_n^\pm(v)=\Delta_v.
\]
If \(Y_v=\varnothing\), then \(D_n(v)=\varnothing\) for all sufficiently large \(n\), so \(a_n^\pm(v)=0\) eventually.

Bi-balancedness also supplies an invariant Gibbs measure \(\mu\) for the zero potential. If \(K\ge1\) is a Gibbs constant, so that
\[
K^{-1}e^{-m h}\le \mu([w]_0)\le K e^{-m h}
\]
for every \(w\in\mathcal B_m(X)\), define \(b_n^+(v)\) as the supremum, over all admissible cylinder histories \([u]_0\), of the conditional probability that the immediately following length-\(n\) block belongs to \(D_n(v)\). Define \(b_n^-(v)\) analogously for the immediately preceding block. Then
\[
K^{-1}|D_n(v)|e^{-nh}\le b_n^\pm(v)\le K^2|D_n(v)|e^{-nh}.
\]
Thus, whenever \(Y_v\neq\varnothing\),
\[
\lim_{n\to\infty}-\frac1n\log b_n^\pm(v)=\Delta_v,
\]
and the same eventual-vanishing statement holds when \(Y_v=\varnothing\).

This gives the exact exponential scale of the quantitative strengthening of the one-hit follower/predecessor lemma for entropy-minimal bi-balanced shifts: the cost of avoiding \(v\) is precisely the entropy gap to the survivor subshift.

## Assumptions and scope
The occurrence of \(v\) is tested wholly inside the length-\(n\) follower or predecessor block. An occurrence crossing the boundary between the conditioning word and the appended block is not counted. This convention is essential for the displayed cylinder decomposition.

The theorem assumes entropy minimality and bi-balancedness. Synchronization is not needed for the estimate itself. Therefore it applies in particular to synchronized bi-balanced shifts, because the motivating source proves those shifts entropy minimal. The measure statement uses an invariant zero-potential Gibbs measure, whose existence follows from bi-balancedness in the framework cited by that source.

No mixing rate, specification constant, finite-type presentation, or Markov property is assumed.

## Proof
Set \(D(v)=\bigcup_{n\ge0}D_n(v)\). It is factorial: every subword of a word avoiding \(v\) also avoids \(v\). The associated survivor shift is exactly \(Y_v=X(D(v))\). Since \(v\in\mathcal B(X)\), the survivor is a proper subshift whenever it is nonempty. Entropy minimality therefore gives \(h_v<h\).

For positive \(|D_n(v)|\), the counting sequence is submultiplicative. Indeed, a word of length \(m+n\) avoiding \(v\) is determined by its prefix of length \(m\) and suffix of length \(n\), and both pieces avoid \(v\). Hence
\[
|D_{m+n}(v)|\le |D_m(v)|\,|D_n(v)|.
\]
It follows that
\[
\lim_{n\to\infty}\frac1n\log |D_n(v)|=h(D(v))=h_v.
\]
Together with
\[
\lim_{n\to\infty}\frac1n\log|\mathcal B_n(X)|=h,
\]
this yields
\[
\lim_{n\to\infty}-\frac1n\log\frac{|D_n(v)|}{|\mathcal B_n(X)|}=h-h_v.
\]
If \(Y_v=\varnothing\) but arbitrarily long words in \(D(v)\) existed, factoriality and compactness would yield a bi-infinite point all of whose finite subwords avoid \(v\), a contradiction. Thus \(D_n(v)\) is eventually empty in this case.

For the follower estimate, the empty word \(\varepsilon\) is admissible and satisfies
\[
\mathcal F_n(\varepsilon,X)=\mathcal B_n(X).
\]
Therefore
\[
a_n^+(v)\ge\frac{|D_n(v)|}{|\mathcal B_n(X)|}.
\]
For an arbitrary \(u\), the numerator is at most \(|D_n(v)|\), while bi-balancedness gives \(|\mathcal F_n(u,X)|\ge c|\mathcal B_n(X)|\). Hence
\[
a_n^+(v)\le\frac1c\frac{|D_n(v)|}{|\mathcal B_n(X)|}.
\]
The predecessor argument is identical, using \(\mathcal P_n(\varepsilon,X)=\mathcal B_n(X)\). Multiplication by a fixed constant does not change the exponential rate, proving the first part.

For the Gibbs statement, let \(|u|=m\). Conditional on \([u]_0\), the event that the next length-\(n\) block avoids \(v\) is the disjoint union of the cylinders \([uw]_0\) over
\[
w\in\mathcal F_n(u,X)\cap D_n(v).
\]
The Gibbs bounds give
\[
\frac{\sum_w\mu([uw]_0)}{\mu([u]_0)}
\le K^2|D_n(v)|e^{-nh}.
\]
Taking the supremum over \(u\) proves the upper bound. Taking \(u=\varepsilon\) gives the global avoidance event, and the lower Gibbs bound on its disjoint length-\(n\) cylinders gives
\[
b_n^+(v)\ge K^{-1}|D_n(v)|e^{-nh}.
\]
For the past, use the cylinders \([wu]_{-n}\), shift invariance of \(\mu\), and the same Gibbs bounds. The logarithmic rate is again \(h-h_v\).

## Verification
The proof is analytic. The critical checks are: factoriality of the avoidance language; submultiplicativity of its word counts; equality of its entropy with the survivor-shift entropy; strict entropy loss from entropy minimality; use of the empty word for the matching lower bound; use of the uniform follower/predecessor balance constant for the upper bound; and the cylinder-by-cylinder Gibbs comparison for arbitrary conditioning words.

The empty-survivor case was checked separately: compactness forces eventual absence of avoiding words, so no finite-rate statement is incorrectly assigned to that case.

## Relationship to prior work
Hong and Kim, *Bi-balanced shifts and variable specification* (arXiv:2609.33476v1), prove that synchronized bi-balanced shifts are entropy minimal and, in Lemma 4.9, show qualitatively that for every fixed word \(v\), some common follower/predecessor length forces at least one extension containing \(v\). Their proof already introduces the factorial avoidance language and the strict entropy gap. The finding here is the sharp quantitative refinement: all worst follower/predecessor avoidance proportions are trapped within constant factors of the global avoidance proportion, so their exact exponent is the entropy gap; the same exponent holds uniformly for worst conditional avoidance under the invariant Gibbs measure.

For irreducible shifts of finite type with Parry measure, the global escape-rate identity as an entropy difference is already known in open-system literature, including Agarwal and Cheriyath's work on subshifts with holes and the Markov-measure extension by Agarwal, Cheriyath, and Tikekar. That known global identity is not claimed as new here. Davis, Haydn, and Yang prove equality of ordinary and return-conditioned escape rates when conditioning on the hole itself. Ramsey studies entropy perturbations after forbidding finitely many words, and Chandgotia, Marcus, Richey, and Wu give detailed finite-type single-pattern avoidance results. These works do not state the constant-factor worst-follower/predecessor sandwich or the arbitrary-cylinder Gibbs conditional exponent for the entropy-minimal bi-balanced setting.

## Limitations
The estimate concerns occurrences lying entirely inside the newly appended block; it does not count copies of \(v\) straddling the history/block boundary. It gives an exact exponential rate but no universal prefactor beyond the displayed balance/Gibbs constants. It does not prove synchronization from entropy minimality and bi-balancedness, does not establish a mixing rate, and does not provide a limit law for rescaled hitting times.

The literature search cannot exclude an unindexed folklore formulation of this short argument. The global entropy-gap escape identity is classical in important finite-type settings and is explicitly not part of the novelty claim.

## References
1. Soonjo Hong and Minkyu Kim, *Bi-balanced shifts and variable specification*, arXiv:2609.33476v1, 2026.
2. Nikita Agarwal and Haritha Cheriyath, *Subshifts of finite type with a hole*, arXiv:1905.11767.
3. Nikita Agarwal, Haritha Cheriyath, and Sharvari Neetin Tikekar, *On escape rate for shifts with Markov measure*, arXiv:2401.05118.
4. C. Davis, N. Haydn, and F. Yang, *Escape rate and conditional escape rate from a probabilistic point of view*, Annales Henri Poincare, 2021.
5. Nick Ramsey, *Entropy bounds for multi-word perturbations of subshifts*, Ergodic Theory and Dynamical Systems, 2024.
6. Nishant Chandgotia, Brian Marcus, Jacob Richey, and Chengyu Wu, *Shifts of finite type obtained by forbidding a single pattern*, arXiv:2409.09024.
