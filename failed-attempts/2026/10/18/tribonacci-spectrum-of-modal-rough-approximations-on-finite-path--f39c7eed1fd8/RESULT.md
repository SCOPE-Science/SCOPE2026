# Tribonacci spectrum of modal rough approximations on finite path frames

## Finding

For every integer \(n\geq 1\), let \(P_n=\{1,\ldots,n\}\) carry the reflexive symmetric relation \(R_n\) given by \(iR_nj\) if and only if \(|i-j|\leq1\). On a Boolean valuation \(X\subseteq P_n\), define the modal necessity and possibility sets
\[
L(X)=\{i:R_n(i)\subseteq X\},\qquad U(X)=\{i:R_n(i)\cap X\neq\varnothing\}.
\]
Write \(a_n\) for the number of *distinct ordered pairs* \((L(X),U(X))\) as \(X\) ranges over all subsets of \(P_n\); pairs are not identified under path reversal. Set \(a_0=1\) only as an empty-word convention. Then
\[
(a_0,a_1,a_2,a_3,a_4,a_5,a_6,a_7,\ldots)
=(1,2,3,7,13,23,43,79,\ldots),
\]
and for every \(n\geq5\),
\[
a_n=a_{n-1}+a_{n-2}+a_{n-3},\qquad
\sum_{n\geq0}a_nz^n=\frac{1+z+z^3+z^4}{1-z-z^2-z^3}.
\]
In particular, if \(\alpha\) is the unique positive root of \(\alpha^3=\alpha^2+\alpha+1\), then
\[
a_n\sim C\alpha^n,\qquad \alpha=1.839286755\ldots,
\]
where, with \(r=1/\alpha\),
\[
C=\frac{1+r+r^3+r^4}{r(1+2r+3r^2)}=1.108072623\ldots.
\]
Thus the number of observable two-modal rough-set profiles has exact exponential growth strictly below the number \(2^n\) of underlying valuations.

## Assumptions and scope

This concerns precisely the nontransitive tolerance relation consisting of loops and the edges of a *labelled undirected path*. The input is an arbitrary crisp subset \(X\). The two output coordinates are computed from the same input; counting the possible lower sets and upper sets separately would answer a different question. All \(n\geq1\) are covered. The auxiliary \(n=0\) is a combinatorial convention and not a new nonempty frame. No statements are made about all graphs, cyclic graphs, equivalence relations, or probability distributions of the fibers.

## Proof

**1. A local three-symbol transducer.** Let \(x_1,\ldots,x_n\in\{0,1\}\) be the characteristic bits of \(X\), and set \(x_0=x_1\), \(x_{n+1}=x_n\) to implement the two endpoints. At position \(i\), the ordered truth-values of \((\Box p,\Diamond p)\) are exactly \((0,0)\), \((0,1)\), or \((1,1)\). Encode them respectively by symbols `0`, `1`, `2`. The output symbol is `0` when \((x_{i-1},x_i,x_{i+1})=(0,0,0)\), `2` when that triple is \((1,1,1)\), and `1` otherwise. Distinct output words are exactly distinct approximation pairs.

**2. Determinization.** The four possible ordered bit-pairs, denoted `00`, `01`, `10`, `11`, are indexed by `0`, `1`, `2`, `3`. A nondeterministic transition from `(a,b)` to `(b,c)` emits the symbol determined by `(a,b,c)`. The allowed initial state set is \(\{00,11\}\), since \(x_0=x_1\). After all output symbols have been read, a word is accepted if any surviving bit-pair is `00` or `11`, implementing \(x_{n+1}=x_n\). Subset determinization from the initial set produces exactly the following twelve reachable states. In the `pairs` column, digits denote their pair indices; `-` is the empty set. Columns `0`, `1`, `2` give the unique next state on the indicated output symbol.

| state | pairs | 0 | 1 | 2 | accepting |
|---:|:---:|---:|---:|---:|:---:|
| 0 | `03` | 1 | 2 | 3 | yes |
| 1 | `0` | 1 | 4 | 5 | yes |
| 2 | `12` | 5 | 6 | 5 | no |
| 3 | `3` | 5 | 7 | 3 | yes |
| 4 | `1` | 5 | 8 | 5 | no |
| 5 | `-` | 5 | 5 | 5 | no |
| 6 | `0123` | 1 | 6 | 3 | yes |
| 7 | `2` | 5 | 9 | 5 | no |
| 8 | `23` | 5 | 10 | 3 | yes |
| 9 | `01` | 1 | 11 | 5 | yes |
| 10 | `012` | 1 | 6 | 5 | yes |
| 11 | `123` | 5 | 6 | 3 | yes |

The initial state is `0`. The table can be checked directly by applying the eight elementary binary-triple transitions, so this is an exact automaton for *all* word lengths, not an extrapolation from short lengths.

**3. An algebraic generating-function certificate.** Let \(G_i(z)\) be the ordinary generating series of accepted output suffixes starting from deterministic state \(i\). If \(\delta(i,b)\) is the transition in the table and \(e_i\) its zero-one accepting indicator, the twelve equations are
\[
G_i(z)=e_i+z\sum_{b=0}^2 G_{\delta(i,b)}(z).
\]
They have a unique solution in formal power series, as all constant terms are fixed. Put \(D(z)=1-z-z^2-z^3\) and \(P_i(z)=D(z)G_i(z)\). The complete algebraic certificate is
\[
\begin{aligned}
P_0&=1+z+z^3+z^4,\\
P_1&=P_3=1,\\
P_2&=z(1+z)^2,\\
P_4&=P_7=z(1+z),\\
P_5&=0,\\
P_6&=(1+z)^2,\\
P_8&=P_9=1+z,\\
P_{10}&=P_{11}=1+z+z^2.
\end{aligned}
\]
For every row of the displayed transition table, direct polynomial substitution verifies
\[
P_i(z)=D(z)e_i+z\sum_{b=0}^2P_{\delta(i,b)}(z).
\]
Consequently these are the exact solutions to the formal-series equations. The initial series is \(G_0(z)=P_0(z)/D(z)\), giving the claimed rational generating function and its coefficient recurrence from index \(5\) onward. The initial coefficients are read directly from this rational function.

**4. Exponential growth.** The denominator has a unique zero \(r\in(0,1)\), satisfying \(r+r^2+r^3=1\). No other root lies on or inside \(|z|=r\), since equality in \(|z+z^2+z^3|\leq |z|+|z|^2+|z|^3\) would require the three nonzero terms to have the same positive direction, forcing \(z=r\). The pole is simple. The residue calculation gives the stated \(C\) and \(\alpha=r^{-1}<2\), proving the asymptotic and the strict exponential loss of distinct modal profiles relative to raw valuations.

## Verification

The standalone `verify.py` builds the subset automaton from the eight local bit transitions, checks every displayed transition and accepting status, and verifies all twelve polynomial certificate identities exactly using integer polynomial arithmetic. Independently, it enumerates each Boolean valuation on path sizes \(1\) through \(15\) and directly constructs the distinct lower/upper pairs. The two routes agree, and the program returns `VERIFY_OK`. These enumerations corroborate the universal generating-function proof; finite enumeration alone is not the basis for the all-size claim.

## Relationship to prior work

Doherty and Szałas (first publicly available 2021-12-29) provide the general relation-based definition of rough approximation pairs, including tolerance spaces, with dual universal/existential neighborhood semantics. The present statement determines the *joint image cardinality* of these operators for every finite reflexive path frame, an enumerative question not supplied by that framework. Chiaselotti, Ciucci, Gentile and Infusino (2015) analyze path and cycle graphs as preclusivity spaces and give formulas for the resulting closure/open sets and for the **complement-of-adjacency similarity** operators. Their similarity relation is not the reflexive adjacency tolerance \(R_n\) used here; their results do not give the above exact joint-output census. Järvinen, Kovács and Radeleczki's 2018/2019 work concerns pairs with lower approximation from a compatible equivalence and upper approximation from a tolerance, another distinct operator pairing. A similar Tribonacci recurrence can also arise in unrelated forbidden-pattern/dissociation counting, but matching recurrences do not identify the counted structures.

## Limitations

This is a self-contained mathematical proof with an ordinary finite-state/checker verification, not an external formal proof or independent audit. The theorem does not count input multiplicities of each approximation pair, does not enumerate pair spectra for arbitrary graphs, and does not claim novelty of the generic finite-state method or Tribonacci numbers. Equivalent formulations in work on finite-state image languages or rough-set approximation spectra remain an originality risk; a search cannot prove exhaustive absence.

## References

1. P. Doherty and A. Szałas, *A landscape and implementation framework for probabilistic rough sets using ProbLog*, Information Sciences **593** (2022), 546–576; publicly available online 2021-12-29. DOI: `10.1016/j.ins.2021.12.062`.
2. G. Chiaselotti, D. Ciucci, T. Gentile and F. Infusino, *Preclusivity and Simple Graphs: The n-cycle and n-path Cases*, RSFDGrC 2015, Lecture Notes in Computer Science **9437**, 138–148. DOI: `10.1007/978-3-319-25783-9_13`.
3. J. Järvinen, L. Kovács and S. Radeleczki, *Defining rough sets using tolerances compatible with an equivalence*, Information Sciences **496** (2019), 264–283; arXiv first posted 2018-11-21. DOI: `10.1016/j.ins.2019.05.030`.
