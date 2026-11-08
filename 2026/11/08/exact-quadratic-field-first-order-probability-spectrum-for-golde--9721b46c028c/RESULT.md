# Exact quadratic-field first-order probability spectrum for golden-mean words

## Finding

Let \(\mathcal G_n\) consist of the binary words of length \(n\) containing no two consecutive \(1\)'s. Equip \(\mathcal G_n\) with the uniform probability measure, and interpret first-order sentences over the finite linear order of positions with a unary predicate \(P\) marking the \(1\)'s. Write \(\varphi=(1+\sqrt5)/2\).

**Theorem.** Every first-order sentence \(\Theta\) has a limiting probability on \(\mathcal G_n\), and the set of all such limits is exactly

\[
\left\{\lim_{n\to\infty}\Pr_{w\in\mathcal G_n}(w\models\Theta):\Theta\in\mathrm{FO}[<,P]\right\}
=\mathbb Q(\sqrt5)\cap[0,1].
\]

More precisely, for each \(\alpha=a+b\varphi\in(0,1)\) with \(a,b\in\mathbb Q\), choose any sufficiently large integer \(m\ge1\) so that

\[
r_0=a+b\frac{F_{m+2}}{F_{m+1}},\qquad
r_1=a+b\frac{F_{m+1}}{F_m}
\]

belong to \([0,1]\), where \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\). There is an explicit first-order sentence that observes the \(m\)-th bit and then performs a rational-valued first-occurrence test on successive zero-runs to implement the conditional acceptance probabilities \(r_0\) and \(r_1\). Its limiting probability is exactly \(\alpha\). The endpoints \(0\) and \(1\) are given by contradictory and tautological sentences.

In particular the spectrum is countable and dense but is not restricted to rational probabilities: \(1/(3\varphi)=(\varphi-1)/3\) is realized using \(m=2\) and the rational conditional probabilities \(1/6\) and \(1/3\).

## Assumptions and scope

The language contains equality, the ordinary strict linear order \(<\), and one unary color predicate \(P\); successor is definable from \(<\). No addition, modular predicates, extra named positions, random truth values, or second-order quantifiers are assumed. The length \(n\) goes through all positive integers. The base words are sampled uniformly *conditional on avoidance of the adjacent factor* \(11\), not under the independent Bernoulli distribution on all binary words. The first-order sentence may depend on the prescribed limiting probability but never on \(n\).

The classification belongs to logical limiting probabilities. It is not a classification of all arbitrary regular sublanguages, for which periodicity can obstruct a full-length limit.

## Proof

**1. Fibonacci counts and the limiting source.** The number of admissible words of length \(n\) is \(F_{n+2}\). If an admissible prefix \(u\) has length \(j\ge1\), the number of completions to length \(n\) is \(F_{n-j+2}\) when its last bit is \(0\), and \(F_{n-j+1}\) when its last bit is \(1\). Therefore, as \(n\to\infty\),

\[
\Pr(\text{prefix }u)\longrightarrow
\begin{cases}\varphi^{-j},&u\text{ ends in }0,\\
\varphi^{-(j+1)},&u\text{ ends in }1.
\end{cases}
\]

The consistent limiting prefix law is a Markov chain: from a \(0\), the probabilities of following with \(0\) and \(1\) are \(\varphi^{-1}\) and \(\varphi^{-2}\), and from a \(1\) the next symbol is \(0\) with probability one. After every occurrence of \(1\), the numbers \(G_i\ge1\) of zeros before the following occurrences of \(1\) are independent with

\[\Pr(G_i=t)=\varphi^{-(t+1)},\qquad t=1,2,\ldots.\]

These statements follow from the displayed prefix formula and the Markov property, not from any independence assumption about the original finite uniform words.

**2. A first-order rational lottery.** Fix integers \(0\le p\le q\) with \(q\ge1\). Choose \(k\) so that \(k!\ge q\), and select \(q\) distinct permutations \(\pi_1,\ldots,\pi_q\) of \(\{1,\ldots,k\}\). In the gap alphabet of positive integers consider the \(q\) patterns

\[W_i=(k+1,\pi_i(1),\ldots,\pi_i(k)).\]

Every pattern has the same strictly positive probability, as the gap law is independent and every pattern uses precisely the same multiset. No proper suffix of any \(W_i\) can equal a prefix of any \(W_j\), because the sentinel \(k+1\) occurs in a pattern only at its first coordinate. For an occurrence beginning at index \(t\), any earlier complete occurrence which overlaps it is impossible; the event that there is no earlier occurrence consequently depends only on gaps strictly before \(t\). It follows, by factoring independent probabilities, that the first occurrence among the \(q\) patterns is uniformly distributed among their \(q\) labels. Some such occurrence exists almost surely: inspecting disjoint blocks of \(k+1\) gaps gives independent trials of fixed positive success probability.

The same test is first-order definable on the finite binary word. A gap of any fixed length is specified by a pair of consecutive \(P\)-positions and finitely many successor steps; a fixed sequence of consecutive gaps is specified by finitely many existentially quantified positions. One can assert that a matching occurrence has no earlier matching occurrence, and that its label belongs to \(\{1,\ldots,p\}\). This uses only \(<\), \(P\), and a finite formula. Applied after the first \(1\) at or beyond any fixed prefix boundary, its asymptotic acceptance probability is \(p/q\), independent of the preceding fixed prefix. To justify the finite-to-infinite passage, first restrict to the first \(T\) gaps and cap the positions at which those gaps finish by a fixed \(H\), producing a finite-cylinder event. Send \(n\to\infty\) for fixed \(T,H\), then \(H\to\infty\), then \(T\to\infty\). Geometric gap tails and the almost-sure occurrence of a marker make the discarded probability tend to zero.

**3. Realizing the entire quadratic field interval.** There are \(F_{m+1}\) admissible \(m\)-bit prefixes ending in \(0\) and \(F_m\) ending in \(1\). By Step 1, the limiting probabilities of these two classes are

\[w_0=F_{m+1}\varphi^{-m},\qquad w_1=F_m\varphi^{-(m+1)},\qquad w_0+w_1=1.\]

Given \(\alpha=a+b\varphi\in(0,1)\), the rational numbers \(r_0,r_1\) displayed in the Finding both converge to \(\alpha\) as \(m\to\infty\). Hence some finite \(m\) places both strictly between \(0\) and \(1\). Choose a rational lottery from Step 2 for each \(r_i\), applied only after the first post-prefix \(1\). A first-order disjunction branches on the last bit of the fixed \(m\)-prefix; independence of subsequent renewal gaps gives limiting acceptance probability \(w_0r_0+w_1r_1\). Fibonacci identities yield

\[
w_0r_0+w_1r_1
=a+b\bigl(F_{m+2}\varphi^{-m}+F_{m+1}\varphi^{-(m+1)}\bigr)
=a+b\varphi=\alpha.\]

The first \(m\) positions and the first post-prefix \(1\) are first-order definable for fixed \(m\). The conditional lotteries are therefore components of one fixed finite first-order sentence, and \(\alpha\) is attained.

**4. Convergence and the field upper bound.** A language of finite words definable in \(\mathrm{FO}[<,P]\) is regular and has a finite aperiodic syntactic monoid (the classical star-free/aperiodic characterization). Take its deterministic monoid automaton and form the product with the two-state automaton recognizing avoidance of \(11\). The latter has adjacency matrix

\[A=\begin{pmatrix}1&1\\1&0\end{pmatrix},\]

with Perron eigenvalue \(\varphi\) and strictly positive right eigenvector \((\varphi,1)\).

Consider any strongly connected component \(D\) of the product whose spectral radius is \(\varphi\). Lifting the displayed Perron vector to its states gives \(A_Dv\le\varphi v\). A strictly positive Perron left eigenvector of \(A_D\) forces equality coordinatewise; thus **every legal outgoing transition from every state of \(D\) remains in \(D\)**. Such a component contains a state whose base last-letter state is \(0\). Repeatedly reading \(0\) keeps the product in \(D\) and, by aperiodicity of the finite monoid, eventually fixes its automaton state. Hence \(D\) has a length-one loop and is primitive. Also, because it is closed under legal transitions, a path cannot traverse two different components of spectral radius \(\varphi\).

All other components have spectral radii strictly below \(\varphi\). Standard finite-matrix Perron expansion, with no chain of dominant components and with every dominant component primitive, consequently gives for the number \(a_n\) of accepted admissible words

\[a_n=c\varphi^n+o(\varphi^n),\qquad c\ge0.\]

Because \(\sum_{n\ge0}a_nz^n\) is a rational function with rational coefficients and \(a_n/\varphi^n\to c\), Abel's theorem gives

\[c=\lim_{z\uparrow1/\varphi}(1-\varphi z)\sum_{n\ge0}a_nz^n\in\mathbb Q(\varphi).\]

Finally \(F_{n+2}/\varphi^n\to\varphi^2/\sqrt5\), so the satisfaction probability converges to \(c\sqrt5/\varphi^2\in\mathbb Q(\sqrt5)\cap[0,1]\). Combined with Step 3, this proves the theorem.

## Verification

Run `python3 checker.py` using the accompanying standard-library-only script. It checks the Fibonacci word counts and last-symbol classes by exhaustive enumeration for lengths through \(16\); verifies symbolic field mixing and rational conditional probabilities for selected exact quadratic-field targets; and directly enumerates the two-way marker race for lengths \(10\) through \(22\), and the six-way race for lengths \(19\) through \(23\). The expected output is `FIBONACCI_SPECTRUM_FINITE_CHECKS_OK`. These tests validate finite consequences of the construction but are not a proof of the asymptotic theorem. The infinite argument is in Steps 1–4.

## Relationship to prior work

Markström and Räty (first publicly submitted October 15, 2026) establish first-order/monadic logical regular-language correspondences and prove convergence for small permutation classes; their automaton product spectral-radius lemma is relevant to the convergence mechanism here. Their result does not state the golden-mean word spectrum or its universal rational renewal selector. Falgas-Ravry, Markström, Räty and Skerman (October 25, 2026) show density of first-order limits for exponentially growing small permutation classes, not an exact quadratic-field spectrum for a constrained word language. Sin'ya (2015) studies zero-one densities of ordinary regular languages; the present ensemble is instead uniformly conditioned on no adjacent \(1\)'s, and the result specifies all intermediate values, including irrational ones.

The classical Fibonacci enumeration, star-free characterization, Perron–Frobenius theorem and rational generating-function fact are used as inputs, not claimed as new. The new object-specific classification is the equality of the entire set of limits with the quadratic-field interval, with an explicit first-order fair-lottery construction and an upper-bound argument for this conditional model.

## Limitations

The limit spectrum is asserted only for \(\mathrm{FO}[<,P]\) and the uniform golden-mean word ensemble. It need not hold for all regular conditions, monadic second-order sentences, other conditioning subshifts, or different distributions. The rational selector is asymptotically fair; the proof does not assert a fixed finite-length success probability for every lottery. Historical priority remains subject to further comparison with older general results on aperiodic languages and Markov-source densities; no independent mathematical audit is claimed.

## References

1. K. Markström and E. Räty, *Logical isomorphism and logical limit laws for small permutation classes and regular languages*, arXiv:2610.22218, first submitted 2026-10-15; especially the automaton lemmas in Section 5 and logical limit discussion.
2. V. Falgas-Ravry, K. Markström, E. Räty and F. Skerman, *On first-order limiting probabilities for small permutation classes*, arXiv:2610.34328, first submitted 2026-10-25; Theorems 1.1 and 1.4.
3. R. Sin'ya, *Zero-One Law for Regular Languages and Semigroups with Zero*, arXiv:1505.03343, 2015.
4. R. McNaughton and S. Papert, *Counter-Free Automata*, MIT Press, 1971 (classical aperiodicity characterization).
5. P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009 (rational generating functions and Perron asymptotics).
