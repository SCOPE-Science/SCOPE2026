# Exact finite-size propagation time of probabilistic zero forcing on sunlet graphs

## Finding

Let \(S_n\) be the **sunlet** or \(n\)-Sun graph, obtained from the cycle \(C_n\) by adjoining one private leaf to each cycle vertex. For each integer \(n\ge5\), consider the synchronous probabilistic zero-forcing process defined below and let \(\operatorname{ept}(S_n)\) be the minimum mean number of rounds to color all vertices blue from a single initially blue vertex. Then

\[
\boxed{\operatorname{ept}(S_n)=\frac{11n}{16}+\frac{4437}{3344}
+\frac{1323}{6688}\left(-\frac29\right)^{n-2}
-\frac{147}{608}\left(-\frac25\right)^{n-2}.}
\]

For every such \(n\), starting from a cycle vertex is strictly better than starting from a leaf. Their mean-propagation-time gap (leaf minus cycle) is precisely

\[
\boxed{\frac{41}{152}-\frac{27}{608}\left(-\frac29\right)^{n-2}
+\frac{147}{608}\left(-\frac25\right)^{n-2}>0.}
\]

For \(n\ge6\) the exact increment is

\[
\operatorname{ept}(S_n)-\operatorname{ept}(S_{n-1})
=\frac{11}{16}-\frac{1617}{6688}\left(-\frac29\right)^{n-3}
+\frac{1029}{3040}\left(-\frac25\right)^{n-3}.
\]

In particular,

\[
\boxed{\lim_{n\to\infty}
\bigl(\operatorname{ept}(S_n)-\operatorname{ept}(S_{n-1})\bigr)=\frac{11}{16}.}
\]

This proves the sun-graph limiting-increment conjecture of Chan, Curl, Geneson, Hogben, Liu, Odegard and Ross (2019 preprint, Conjecture 2.7; 2020 journal version, Conjecture 2.8), and gives the previously conjectured limit with explicit alternating geometric convergence.

## Assumptions and scope

All graphs are finite and simple. In a round, every blue vertex \(v\) independently attempts to color each of its white neighbors \(w\) blue with probability

\[
\Pr(v\longrightarrow w\mid B)=\frac{|N[v]\cap B|}{\deg(v)},
\]

where \(B\) is the blue set at the start of the round and \(N[v]\) is the closed neighborhood. Attempts use the same pre-round blue set and are independent. Blue vertices never revert. Time zero has exactly one blue vertex; the propagation time counts subsequent synchronous rounds until all \(2n\) vertices are blue. Since all cycle vertices are symmetric, as are all leaves, the minimum over initial vertices reduces to two cases.

The result applies to every integer \(n\ge5\), without an asymptotic approximation or independence assumption between neighboring cycle fronts beyond that given by the force-attempt rule.

## Proof

**1. Reduction to two moving fronts.** Once two or more cycle vertices have become blue, the blue cycle vertices form a contiguous cyclic interval. Write \(m\) for the number of remaining white cycle vertices. For \(m\ge2\), only the two endpoints of the blue interval can turn further cycle vertices blue. Interior leaf colors are irrelevant to this event: an interior cycle vertex has both cycle neighbors blue and forces its leaf, if white, with probability one in the next round. Let \(a_m,b_m,c_m\) be the expected further rounds until all cycle vertices are blue, according as zero, one, or two leaves attached to the *two endpoint cycle vertices* are blue. Define \(a_0=b_0=c_0=0\).

At an endpoint with a white leaf, its adjacent white cycle vertex and its leaf are each independently forced with probability \(2/3\). Thus its behavior in one round is: cycle advance with probability \(2/3\); no advance but leaf turns blue with probability \(2/9\); neither with probability \(1/9\). At an endpoint whose leaf is blue, the next cycle vertex is forced surely. Whenever an endpoint advances, its newly exposed endpoint leaf is white.

When \(m=1\), both endpoints target the same last white cycle vertex. If either endpoint has a blue leaf, this vertex turns blue surely, hence \(b_1=c_1=1\). With neither endpoint leaf blue, both cycle attempts fail with probability \(1/9\); conditioned on these failures, endpoint-leaf forces remain independent. Consequently

\[
 a_1=1+\frac{1}{81}a_1+\frac{4}{81}b_1+\frac{4}{81}c_1
 =\frac{89}{80}.
\]

For \(m\ge2\), the distinct target cycle vertices permit the following exact first-step recurrences, incorporating the self-transition in the first one:

\[
\begin{aligned}
 b_m&=1+\frac19a_{m-1}+\frac29b_{m-1}+\frac23a_{m-2},\\
 c_m&=1+a_{m-2},\\
 \frac{80}{81}a_m&=1+\frac4{81}(b_m+c_m)
 +\frac4{27}a_{m-1}+\frac8{27}b_{m-1}+\frac49a_{m-2}.
\end{aligned}
\]

Every term represents disjoint simultaneous outcomes of the two boundary force attempts; these recurrences uniquely determine the expectations, since the coefficient \(80/81\) is nonzero and the other terms are known at earlier stages (or are \(b_m,c_m\), already computed).

**2. Solve the frontier recurrences.** Define the formal power series \(A(z)=\sum_{m\ge0}a_mz^m\), \(B(z)=\sum_{m\ge0}b_mz^m\), and \(C(z)=\sum_{m\ge0}c_mz^m\). Summing the recurrences with their boundary values yields

\[
\begin{aligned}
 B&=\frac{z}{1-z}+\frac z9 A+\frac{2z}9 B+\frac{2z^2}3 A,\\
 C&=\frac{z}{1-z}+z^2 A,\\
 \frac{80}{81}\left(A-\frac{89z}{80}\right)
 &=\frac{z^2}{1-z}+\frac4{81}(B+C-2z)
 +\frac{4z}{27}A+\frac{8z}{27}B+\frac{4z^2}{9}A.
\end{aligned}
\]

Solving this linear rational system, or substituting directly in all three identities, gives the unique formal-power-series solution

\[
\begin{aligned}
 A(z)&=\frac{z(46z+801)}{16(1-z)^2(2z+5)(2z+9)},\\
 B(z)&=\frac{z(150z^2-23z+720)}{16(1-z)^2(2z+5)(2z+9)},\\
 C(z)&=\frac{-z(18z^3-417z^2+272z-720)}{16(1-z)^2(2z+5)(2z+9)}.
\end{aligned}
\]

These are identities of rational functions, not numerical fits; all denominator constant terms are nonzero, so their Taylor coefficients are uniquely determined.

**3. Initial cycle vertex.** Let \(u_n\) be the expected additional rounds until all cycle vertices are blue given exactly one initially blue cycle vertex and its leaf white. Let \(h_n\) denote the corresponding expectation if this leaf is already blue. For \(n\ge5\), the initial core vertex independently attempts its two white cycle neighbors and its own leaf, each with probability \(1/3\); with the leaf blue it forces each cycle neighbor with probability \(2/3\). Exact first-step conditioning gives

\[
\begin{aligned}
 u_n&=1+\frac8{27}u_n+\frac4{27}h_n
 +\frac8{27}a_{n-2}+\frac4{27}b_{n-2}+\frac19a_{n-3},\\
 h_n&=1+\frac19h_n+\frac49b_{n-2}+\frac49a_{n-3}.
\end{aligned}
\]

Solving,

\[
 u_n=\frac{63}{38}+\frac{8a_{n-2}+6b_{n-2}+5a_{n-3}}{19},
 \qquad h_n=\frac98+\frac{b_{n-2}+a_{n-3}}2.
\]

When the last white cycle vertex turns blue, its own leaf remains white because updates are synchronous and no white cycle vertex can force its leaf in that same round. In the *following* round every remaining white leaf is forced deterministically, since its cycle parent then has both cycle neighbors blue. Thus the full-graph expectation from a cycle vertex is exactly \(u_n+1\), and from a leaf is exactly \(h_n+2\) (one initial deterministic leaf-to-cycle round plus one final leaf-clearing round).

**4. Extract coefficients and compare starts.** From the preceding expressions,

\[
\begin{aligned}
 \frac8{19}A(z)+\frac6{19}B(z)+\frac{5z}{19}A(z)
 &=\frac{11}{16(1-z)^2}-\frac{269}{418(1-z)}\\
 &\quad-\frac{735}{608(2z+5)}+\frac{11907}{6688(2z+9)}.
\end{aligned}
\]

Taking the coefficient of \(z^{n-2}\) and adding \(1+63/38=101/38\) yields the displayed exact formula for \(\operatorname{ept}(S_n)\) when the initial vertex is on the cycle. Similarly, coefficient extraction for \(h_n+2-(u_n+1)\) yields

\[
(h_n+2)-(u_n+1)=\frac{41}{152}-\frac{27}{608}\left(-\frac29\right)^{n-2}
 +\frac{147}{608}\left(-\frac25\right)^{n-2}.
\]

For \(n\ge5\), its absolute oscillating correction is bounded by

\[
\frac{27}{608}\left(\frac29\right)^3
+\frac{147}{608}\left(\frac25\right)^3
<\frac{41}{152},
\]

so cycle start is the unique optimal **vertex orbit**, with every cycle vertex optimal and every leaf strictly worse. Subtracting consecutive exact formulas gives the increment expression, whose two geometric terms tend to zero. This proves the theorem for all \(n\ge5\).

## Verification

The standalone standard-library script `verify_sun.py` replays the rational frontier recurrences through index \(110\), verifies the stated exact expectation and starting-orbit formulas through size \(109\), and independently solves the **uncompressed** \(2n\)-vertex blue-subset Markov chain using exact rational arithmetic for \(n=5,6\). It reports **653 exact equalities and six separate comparisons** to the source's displayed decimal values. For example the direct full-state calculations give \(\operatorname{ept}(S_5)=1225469/256500\) and \(\operatorname{ept}(S_6)=251448607/46170000\), matching the closed forms and the source's numerical table. The algebraic rational-function identities and geometric convergence above, not the finite script runs, establish the all-size theorem. Run with `python3 verify_sun.py`.

## Relationship to prior work

Chan, Curl, Geneson, Hogben, Liu, Odegard and Ross (arXiv version first public 2019-06-25; 2020 journal version) give a general Markov-chain method, a finite-state sun-graph transition table and numerical propagation-time values through order \(45\). They explicitly conjecture that successive means tend to \(11/16\) (preprint Conjecture 2.7; journal Conjecture 2.8). Their general exact matrix formula does not itself evaluate the complete sun-graph family in closed form or prove that limit. The result here solves their boundary recurrences to a rational generating function, determines exact all-size means, and proves optimality of cycle-vertex initialization.

Geneson and Hogben (2018) derive exact propagation times for paths and cycles without pendant leaves, not the sunlets. Narayanan and Sun (2019) and Jelassi, Portier and Sarkar (2025) derive bounds for wider graph classes, which do not imply this exact sunlet formula. The same limiting increment, when simply stated numerically, was already conjectured in the 2019 source and is not represented here as an original conjecture or an originally discovered numerical value.

## Limitations

The result is for the specific synchronous independent-attempt probabilistic zero-forcing convention and exactly one initially blue vertex on \(S_n\), with \(n\ge5\). It does not provide an entire propagation-time distribution, cover arbitrary graphs or modified forcing probabilities, or classify multi-vertex seed sets. The independent full-state verification is finite; the all-size assertion rests on the detailed analytic recurrence proof. Literature checks cannot establish exclusive historical priority, and independent mathematical validation has not been performed.

## References

1. Yu Chan, Emelie Curl, Jesse Geneson, Leslie Hogben, Kevin Liu, Issac Odegard and Michael S. Ross. *Using Markov chains to determine expected propagation time for probabilistic zero forcing*. arXiv:1906.11083, first submitted June 25, 2019, https://arxiv.org/abs/1906.11083 ; *Electronic Journal of Linear Algebra* **36** (2020), 318–333, https://emis.de/ft/34759 . See the sun-graph transition table and limiting-increment conjecture.
2. Jesse Geneson and Leslie Hogben. *Propagation time for probabilistic zero forcing*. arXiv:1812.10476, first submitted December 24, 2018, https://arxiv.org/abs/1812.10476 .
3. Shyam Narayanan and Alec Sun. *Bounds on expected propagation time of probabilistic zero forcing*. arXiv:1909.04482, first submitted September 10, 2019, https://arxiv.org/abs/1909.04482 .
4. Mehdi Jelassi, Julien Portier and Rik Sarkar. *Tight bounds for expected propagation time of probabilistic zero forcing*. arXiv:2512.01429, first submitted December 1, 2025, https://arxiv.org/abs/2512.01429 .
