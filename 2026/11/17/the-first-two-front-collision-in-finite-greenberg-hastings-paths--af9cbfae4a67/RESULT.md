# The first two-front collision in finite Greenberg–Hastings paths

## Finding

For each integer \(n\ge 5\), put \(q=n-1\) and let \(F\) be the synchronous \(q\)-state, threshold-one Greenberg–Hastings cellular automaton on the open path with labelled sites \(0,1,\ldots,n-1\). Define \(\tau(a)\) as the first update at which the state is all zero. Then the sharp extinction time is \(2n-3\).

Let \(r(a)\) count initially refractory sites (states \(2,\ldots,q-1\)), and let \(e(a)\) count initially excited sites (state \(1\)). Every state of maximal extinction time has either one or two initially excited sites. Their complete bivariate enumerator is

\[
\boxed{\sum_{\tau(a)=2n-3}z^{r(a)}u^{e(a)-1}=2\prod_{j=0}^{n-4}(1+jz)\left[(1+(n-3)z)^2+(n-3)zu\right].}
\]

In particular, exactly \(2((n-1)!-(n-3)!)\) labelled states have the maximum extinction time, with \(2(n-2)^2(n-3)!\) having exactly one initial excitation and \(2(n-3)(n-3)!\) having exactly two. The terminal-shell deficit relative to two independent, unopposed maximal propagation fronts, whose combined count would be \(2(n-1)!\), is exactly \(2(n-3)!\). The relative deficit is \(1/((n-1)(n-2))\).

## Assumptions and scope

All states are labelled \(a=(a_0,\ldots,a_{n-1})\in\{0,1,\ldots,q-1\}^n\), with \(n\ge5\), \(q=n-1\ge4\), and free (nonperiodic) path boundaries. At each update a nonzero state \(c\) becomes \((c+1)\bmod q\). A zero becomes one exactly when at least one existing path neighbor equals one; otherwise it remains zero. All sites update simultaneously. There is no self-neighbor and no coupling beyond adjacent sites. The reported clock counts complete updates, with initially resting state assigned \(\tau=0\). Each initially excited site has color exactly one, not any nonzero color.

The bivariate exponent of \(u\) is \(e(a)-1\), which is nonnegative on the terminal shell by the proof. The result does not assert the full distribution of smaller extinction times, nor cover periodic boundaries, graphs with extra edges, thresholds other than one, or fixed \(q\) as \(n\) grows.

## Proof

**1. No excitation beyond path distance.** Suppose a site is excited (state one) at time \(t>0\). It was resting and had an excited neighbor at time \(t-1\). Trace such an excited predecessor backwards, iteratively. This trace cannot immediately reverse direction: a site excited at time \(s\) is in state two at time \(s+1\), so it cannot be resting at that time and re-excited at \(s+2\). On a path every nonbacktracking walk is simple. Thus a trace of length \(t\) visits \(t+1\) distinct sites, forcing \(t\le n-1\). After its final excitation each vertex takes at most \(q-1\) further updates to become zero. Consequently \(\tau(a)\le(n-1)+(q-1)=2n-3\). The initialization \((1,0,\ldots,0)\) generates an undisturbed wave across the path and attains equality.

**2. Extreme directions.** Equality means an excitation occurs at time \(n-1\), whose ancestry must visit all \(n\) sites without backtracking. Its source and target are the two opposite endpoints. Consider a right-going terminal wave. Necessarily \(a_0=1\), and site \(i\) is excited at time \(i\), for each \(1\le i\le n-1\). At every intermediate site \(1\le i\le n-2\), this is its first excitation; the far endpoint may also have been excited at time zero. In particular, \(a_1=0\).

For \(1\le i\le n-2\), an initially excited site cannot become resting before its required excitement at time \(i\), since \(q-1=n-2>i-1\). Initial refractory color \(c\ge2\) becomes zero by time \(i-1\) precisely when \(q-c\le i-1\). Hence the permitted initial values at site \(i\) are exactly

\[
\{0\}\cup\{q-i+1,\ldots,q-1\},\qquad 1\le i\le n-2,
\]

with \(i-1\) refractory choices. At the target site \(i=n-1\), *every* initial color has become zero by time \(n-2=q-1\) provided that no earlier collision excites it. In particular, a second excitation initially at the far endpoint is newly possible at this critical length.

**3. Exactly one obstruction.** If the far endpoint initially has color one and its neighbor \(n-2\) initially has color zero, then that neighbor is excited at time one by the left-going front. Because it remains nonzero at the update when the right-going front requires a fresh excitation there, the right-going front is blocked. Conversely, when the far endpoint is not initially excited, or when its neighbor is initially refractory, no other initial excitation competes with the right-moving front; induction on the sites shows that the front reaches each consecutive site at its designated time. Thus the preceding local conditions are both necessary and sufficient, subject to excluding exactly the collision pattern

\[a_{n-1}=1,\qquad a_{n-2}=0.\]

No initial configuration can realize both extreme orientations: the right-going condition requires \(a_1=0\), the left-going one requires \(a_{n-2}=0\), and when both endpoints start excited the collision condition blocks either attempted full traverse. Reflection exchanges the two disjoint orientation classes.

**4. Exact enumerator.** For one orientation, sites \(1,\ldots,n-3\) contribute \(\prod_{j=0}^{n-4}(1+jz)\). The penultimate site contributes \(1+(n-3)z\). The far endpoint contributes \(1+(n-3)z+u\) (zero, one of its \(n-3\) refractory colors, or an initially excited color). The excluded collision class contributes \(u\prod_{j=0}^{n-4}(1+jz)\). Subtraction, followed by doubling for reflection, gives the displayed polynomial:

\[
2\prod_{j=0}^{n-4}(1+jz)\left[(1+(n-3)z)^2+(n-3)zu\right].
\]

Setting \(z=u=1\) gives the terminal-shell count. The constant and linear coefficients in \(u\) give respectively the one- and two-excitation populations. No higher power occurs.

## Verification

The standalone programs `verify_exhaustive.cpp` and `verify_structural.py` implement the synchronous dynamics by independent algorithms. The C++ program exhaustively evolves every labelled initial configuration for \(4\le n\le8\), \(q=n-1\), including all \(7^8=5,764,801\) configurations at \(n=8\). It confirms the maximum count, one- and two-excitation counts, and the upper bound without assuming the proposed local characterization. The independent Python program exhaustively checks the complete bivariate coefficient table and the collision exclusion predicate for \(4\le n\le7\). Their outputs are included in `checks/exhaustive.txt` and `checks/structural.txt`.

The \(n=4\) run is a boundary check outside the stated \(n\ge5\) result. Neither finite computation establishes the infinitely many cases: the proof above does that. Verification commands, relative to this package directory, are `g++ -std=c++17 -O3 -Wall -Wextra verify_exhaustive.cpp -o verify_exhaustive && ./verify_exhaustive` and `python3 verify_structural.py`.

## Relationship to prior work

Fisch and Gravner's *One-dimensional Deterministic Greenberg–Hastings Models* (1995), Section 5, defines percolating paths of lengths at most \(q\), describes wave collisions, and derives infinite-line survival properties. Its percolating-path color choices directly account for the unopposed initial segment in the present proof. The new result concerns the **first length beyond that percolating-path definition**, namely an open path of length \(q+1\), and quantifies the precise competing-front exclusion, including its refractory and second-source refinements. It does not claim the unopposed percolating-path product as new.

Durrett and Griffeath (public preprint dated 22 March 1993) give general background on excitable cellular automata and asymptotic spatial dynamics. The separately indexed result *A square-root law for maximal extinction times in three-state excitation on finite paths* handles a fixed three-state model as the path length varies; that result does not cover the present family \(q=n-1\ge4\), although the method of studying terminal extinction layers is shared. This comparison is based on the published summary of that latter result, not a full-text exclusion claim.

## Limitations

Only the critical color/path relation \(q=n-1\ge4\) is classified, not the next collision thresholds. The factorial formulas for unopposed fronts are already suggested by older percolating-path analysis; novelty is claimed only for the quantified first interference correction and its full two-source/refractory polynomial. Historical priority remains conditional on source discovery, especially earlier finite-interval treatments; no independent mathematical audit has been performed. The finite calculations establish only the enumerated small instances, not the general theorem.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, public preprint 22 March 1993, https://arxiv.org/abs/patt-sol/9303002.
2. R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, *Complex Systems* **9** (1995), 329–348, especially Section 5, https://content.wolfram.com/sites/13/2018/02/09-5-1.pdf.
3. *A square-root law for maximal extinction times in three-state excitation on finite paths*, published mathematical note (2026); consulted as a title and summary, not in full text.
