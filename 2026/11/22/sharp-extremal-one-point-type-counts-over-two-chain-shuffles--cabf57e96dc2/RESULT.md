# Sharp extremal one-point type counts over two-chain shuffles

## Finding

Let \(L\) be the countable Fraïssé-homogeneous structure whose age consists of finite strict partial orders with a distinguished linear extension. Let an individually named parameter structure consist of two mutually incomparable chains of positive lengths \(a,b\), interleaved arbitrarily in its distinguished linear order. Denote by \(T(w)\) the number of complete nonalgebraic singleton types over the parameters in \(L\), where the shuffle word \(w\) specifies the interleaving. Put

\[
n=a+b,\qquad m=\min\{a,b\},\qquad d=|a-b|,
\qquad
\varepsilon_d=\begin{cases}4&d\text{ even},\\1&d\text{ odd}.\end{cases}
\]

**Theorem.** For every \(a,b\ge1\), the exact extrema over every shuffle are

\[
\boxed{T_{\min}=\binom{n+3}{3}+ab,\qquad
T_{\max}=T_{\min}+\frac{m}{6}
\left(3d^2+6dm+4m^2-\varepsilon_d\right).}
\]

The only minimizing words are the two segregated words. To characterize every maximizer, rename the chains if necessary so that \(a\ge b\), call them \(A\) and \(B\), and put \(q_j\) equal to the number of \(A\)-vertices before the \(j\)-th \(B\)-vertex, for \(1\le j\le b\). Exactly the maximizing words satisfy

\[
\boxed{q_j\in\operatorname*{argmin}_{z\in\mathbb Z}
\left|z-\left(j+\frac{a-b-1}{2}\right)\right|
\quad (1\le j\le b).}
\]

There is exactly one maximizing word when \(d\) is odd, and exactly \(2^m\) maximizing words when \(d\) is even, considering the two chains to be prescribed components. If the components are not distinguished and \(a=b\), exchanging them identifies pairs of words. In the balanced case \(a=b=m\),

\[
T_{\max}-T_{\min}=\frac{2m(m^2-1)}3,
\qquad \lim_{m\to\infty}\frac{T_{\max}}{T_{\min}}=\frac32.
\]

## Assumptions and scope

The strict partial order \(\prec\) is an irreflexive transitive relation, and \(\triangleleft\) is a total order extending it. There are no predicates naming the two chains in the ambient language: the labels \(A,B\) are bookkeeping for two specified components of the finite base. All base vertices are named individually. The new vertex is required to be different from each parameter. Every consistent finite extension diagram is realized in the Fraïssé limit, and homogeneity makes its quantifier-free diagram equivalent to a complete singleton type over the named finite base. All counts are finite orbit/type counts, not probabilities on the underlying countable set.

## Proof

**1. Local count at an insertion gap.** At a gap after \(i\) vertices of chain \(A\) and \(j\) vertices of chain \(B\), let \(D_-\) be the set of named vertices below the new point and \(D_+\) those above it. Then \(D_-\) is an initial segment on each chain restricted to vertices before the gap, while \(D_+\) is a final segment on each chain restricted to vertices after the gap. Transitivity requires every element of \(D_-\) to precede every element of \(D_+\) in the old partial order. Thus both can be nonempty only when each lies in the **same** one of the two chains.

The diagrams with \(D_+=\varnothing\) number \((i+1)(j+1)\); those with \(D_-=\varnothing\) number \((a-i+1)(b-j+1)\); the doubly empty diagram was counted twice. The diagrams with both nonempty number \(i(a-i)+j(b-j)\). Hence the exact contribution of this gap is

\[
\begin{aligned}
G(i,j)&=(i+1)(j+1)+(a-i+1)(b-j+1)-1\\
&\quad+i(a-i)+j(b-j)\\
&=(a+1)(b+1)+(a-b)(i-j)-(i-j)^2.
\end{aligned}
\]

The cases are exhaustive and disjoint after correcting the doubly empty diagram, so this is a bijective count, not an asymptotic estimate.

**2. A nonnegative shuffle-defect identity.** Write the word as a monotone lattice path from \((0,0)\) to \((a,b)\). At time \(t\in\{0,\dots,n\}\), set \(d_t=i_t-j_t\). Then \(T(w)=\sum_{t=0}^n G(i_t,j_t)\). Let the \(B\)-steps occur at positions \(p_1<\cdots<p_b\), so that \(q_j=p_j-j\), with

\[
0\le q_1\le\cdots\le q_b\le a.
\]

To expand the sum, set \(B_t=|\{j:p_j\le t\}|\), so that \(d_t=t-2B_t\). The identities

\[
\sum_{t=0}^n B_t=\sum_{j=1}^b(n-p_j+1),\quad
\sum_{t=0}^n tB_t=\sum_{j=1}^b\sum_{t=p_j}^n t,
\quad
\sum_{t=0}^n B_t^2=\sum_{j=1}^b(2j-1)(n-p_j+1)
\]

follow by interchanging sums. Substitution and expansion give the exact identity

\[
\boxed{T(w)=\binom{n+3}{3}+ab
+2\sum_{j=1}^{b}q_j(a-q_j)
+2\sum_{1\le i<j\le b}(q_j-q_i).}\tag{1}
\]

Indeed, the constant is the value of the segregated word \(A^aB^b\), as also follows by summing the gap polynomial on that word. Every nonconstant term in (1) is nonnegative. Equality holds exactly when every \(q_j\) lies in \(\{0,a\}\) and all the \(q_j\)'s agree; this means \(B^bA^a\) or \(A^aB^b\). This proves the minimum and all its equality cases, including \(b=1\).

**3. Completing the square.** Define \(r_j=j+(a-b-1)/2\). Reorganizing (1) yields

\[
T(w)-T_{\min}=2\sum_{j=1}^b\left(r_j^2-(q_j-r_j)^2\right).
\tag{2}
\]

Assume \(a\ge b\). Then \(r_1\ge1/2\), \(r_b\le a\), and \(r_{j+1}=r_j+1\). Consequently, choosing each \(q_j\) independently to be any nearest integer to \(r_j\) always yields an admissible weakly increasing integer sequence in \([0,a]\). Every such sequence corresponds to a unique shuffle, and the strictly negative squares in (2) prove that **these and only these** shuffles maximize the count.

If \(a-b\) is odd, each \(r_j\) is integral and the choice is unique. If \(a-b\) is even, each \(r_j\) is a half-integer, and the two nearest choices at every \(j\) remain compatible with monotonicity; therefore there are exactly \(2^b\) maximizing words. Summing the squares in (2) gives

\[
T_{\max}-T_{\min}=\begin{cases}
\displaystyle\frac b6\big(3d^2+6db+4b^2-1\big),&d\text{ odd},\\[4pt]
\displaystyle\frac b6\big(3d^2+6db+4b^2-4\big),&d\text{ even}.
\end{cases}
\]

Swapping the names of the chains gives the formula with \(m=\min\{a,b\}\). The balanced case is immediate algebra, and its asymptotic ratio uses the leading cubic terms of the two extrema.

## Verification

The bundled `check.py` implements (a) direct ternary assignments of old-to-new comparisons with full transitivity checks, (b) the insertion-gap sum, and (c) the independent defect formula (1). Run `python3 check.py` using Python 3 without external dependencies. The recorded `check_output.txt` shows all 48,602 shuffles with \(1\le a,b\le8\) checked against both formulas, 240 small-shuffle direct ternary cross-checks with \(a+b\le7\), and the complete optimizer classification for those ranges. It also checks the balanced gap identity for \(1\le m<100\). These finite checks corroborate the explicit all-order proof; they do not replace it.

## Relationship to prior work

Dolinka and Mašulović classified countable homogeneous linearly ordered posets, including the Fraïssé limit of all finite such structures, and used its one-point extension property. That work establishes the ambient framework, but not the shuffle-dependent singleton-orbit extrema here. Corrêa and Szwarcfiter studied extensions of an order on a fixed ground set, rather than adding a new point to an ordered Fraïssé structure. de Sousa and Truss classified coloured homogeneous partial orders and studied shuffling of components, not the present extremal extension count. Earlier calculations of types over chains and antichains and over the **unordered** union of two chains do not determine the dependence on an added distinguished linear extension. The claim is the exact extremal count and optimizer classification, not novelty of the Fraïssé construction or of lattice-path shuffles themselves.

## Limitations

The theorem covers exactly two nonempty incomparable chains. It does not classify bases with three or more chains, arbitrary partial orders, tuple types of higher arity, or distributions among the nonextremal shuffles. The originality comparison is necessarily subject to historical-priority risk from unindexed or inaccessible equivalent treatments. No separate external mathematical audit is represented by the finite checks.

## References

1. I. Dolinka and D. Mašulović, *Countable homogeneous linearly ordered posets*, European Journal of Combinatorics 33 (2012), 1965–1973. https://doi.org/10.1016/j.ejc.2012.06.006 (first available online 2012-07-15).
2. R. C. Corrêa and J. L. Szwarcfiter, *On extensions, linear extensions, upsets and downsets of ordered sets*, Discrete Mathematics 295 (2005), 13–30. https://doi.org/10.1016/j.disc.2004.12.007.
3. S. Torrezao de Sousa and J. K. Truss, *Countable homogeneous coloured partial orders*, Dissertationes Mathematicae 455 (2008), 1–48. https://www.academia.edu/88684243/Countable_homogeneous_coloured_partial_orders.
