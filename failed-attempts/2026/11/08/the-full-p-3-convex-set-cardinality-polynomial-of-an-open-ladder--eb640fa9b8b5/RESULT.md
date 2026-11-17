# The full \(P_3\)-convex-set cardinality polynomial of an open ladder

## Finding

Let \(L_n=P_2\square P_n\) be the labelled open ladder with \(n\ge1\) columns, two rows, and all horizontal rail and vertical rung edges. A vertex set \(S\) is \(P_3\)-convex if every vertex outside \(S\) has at most one neighbor in \(S\). Define the size enumerator

\[P_n(z)=\sum_{S\subseteq V(L_n)\,\colon\, S\text{ is }P_3\text{-convex}}z^{|S|}.\]

The entire bivariate ordinary generating function is

\[\boxed{\sum_{n\ge1} P_n(z)t^{n-1}=\frac{N(t,z)}{D(t,z)}}\]

with

\[\begin{aligned}
N(t,z)={}&(1+z)^2+(z-3z^3)t+(z+z^2-3z^3)t^2\\
&-3z^3t^3-z^3t^4,\\
D(t,z)={}&1-(1+z+z^2)t+(z^2+z^3)t^2\\
&-(z+z^2)t^3+2z^3t^4+z^3t^5.
\end{aligned}\]

Thus every cardinality coefficient of every ladder is determined exactly. In particular, the order-five polynomial recurrence

\[\begin{aligned}
P_n(z)={}&(1+z+z^2)P_{n-1}(z)-(z^2+z^3)P_{n-2}(z)\\
&+(z+z^2)P_{n-3}(z)-2z^3P_{n-4}(z)-z^3P_{n-5}(z)
\end{aligned}\]

holds for every integer \(n\ge6\), with initial values

\[\begin{aligned}
P_1(z)={}&1+2z+z^2,\\
P_2(z)={}&1+4z+4z^2+z^4,\\
P_3(z)={}&1+6z+9z^2+2z^3+2z^4+z^6,\\
P_4(z)={}&1+8z+18z^2+12z^3+6z^4+2z^6+z^8,\\
P_5(z)={}&1+10z+31z^2+36z^3+21z^4+6z^5+5z^6+2z^8+z^{10}.
\end{aligned}\]

## Assumptions and scope

The graphs are finite, simple and undirected. Every vertex is distinguished by its column and row; sets are not quotiented by graph automorphisms. The convention \(n=1\) gives a single edge and is included to make the boundary-conditioned generating function uniform. The coefficient of \(z^k\) counts exactly the \(k\)-element convex subsets, for all \(0\le k\le2n\). No random process or percolation limit is assumed.

## Proof

Index the two rows by \(r=0,1\), and write each column membership as a bit mask \(b\in\{0,1,2,3\}\). Put \(b_r\in\{0,1\}\) for its bit at row \(r\), and \(|b|=b_0+b_1\). For three successive column masks \(a,b,c\), let \(\phi(a,b,c)=1\) if, for both \(r=0,1\),

\[b_r=0\quad\Longrightarrow\quad a_r+b_{1-r}+c_r\le1,\]

and put \(\phi=0\) otherwise. This is precisely the convexity requirement at the middle column: the outside vertex has neighbors on the same rung and on the two adjacent rails. At the two ends use a virtual all-zero column. Accordingly, a mask word \(b_1,\ldots,b_n\) is valid exactly when \(\phi(b_{i-1},b_i,b_{i+1})=1\) for all \(i\), with \(b_0=b_{n+1}=0\).

Construct the sixteen-state transfer matrix \(M(z)\), indexed by ordered mask pairs \((a,b)\), via

\[M(z)_{(a,b),(b',c)}=\mathbf1_{b'=b}\,\phi(a,b,c)z^{|c|}.\]

Set \(v_{(a,b)}=\mathbf1_{a=0}z^{|b|}\) and \(u_{(a,b)}=\phi(a,b,0)\). Each word is assigned weight \(z\) once for each selected vertex, hence

\[P_n(z)=v M(z)^{n-1}u\qquad(n\ge1).\]

Swapping the two rows acts simultaneously on both masks and commutes with \(M\). Both \(v\) and \(u\) are invariant. The sixteen pair states therefore reduce to ten row-swap orbits \(\mathcal O\). Let \(B(z)\) be the ten-by-ten quotient whose entry from orbit \(I\) to orbit \(J\) is the sum of the \(M\)-transition weights from any representative of \(I\) to all states in \(J\). This is independent of the representative. Let \(\bar v_I=\sum_{s\in I}v_s\) and \(\bar u_I=u_s\) for any \(s\in I\). Then

\[P_n(z)=\bar v B(z)^{n-1}\bar u.\]

A finite exact determinant calculation gives

\[\det(I_{10}-tB(z))=D(t,z).\]

This is an identity in \(\mathbb Z[t,z]\); the entire quotient is explicitly defined above, so the calculation is reproducible without an unstated matrix. The supplied verifier certifies this identity over \(\mathbb Z\) by Bareiss determinants on a rectangular interpolation grid: each side has degree at most ten in \(t\) and at most twenty in \(z\), and it checks equality at eleven distinct values of \(t\) and twenty-one distinct values of \(z\). The elementary polynomial interpolation theorem makes this a complete finite exact certificate, not a probabilistic test.

By the adjugate identity, \(\bar v(I-tB)^{-1}\bar u\) has denominator dividing \(D(t,z)\) and numerator of \(t\)-degree at most nine. Exact transfer iteration supplies the first ten polynomial coefficients in \(t\); direct multiplication by \(D\) yields precisely the displayed \(N\) at orders zero through four and zero at orders five through nine. Since the numerator degree bound is nine, this proves the rational identity for every \(n\ge1\). Equating coefficients proves the claimed recurrence and the initial values.

## Verification

Run `python3 artifacts/verify.py` using Python 3.8 or newer. The script rebuilds the row-swap orbits from the four masks and checks all 231 exact integer determinant equalities needed for the polynomial identity; it independently verifies the ten coefficient-polynomial identities, reproduces the unweighted initial sequence, and exhaustively tests all \(2^{2n}\) vertex subsets for \(1\le n\le8\) directly against the original vertex-neighborhood definition. The script prints `VERIFY_OK` only after these tests pass. Each determinant computation uses exact fraction-free integer elimination, and each size coefficient uses integer polynomial arithmetic. No floating-point result, stochastic sampling, black-box external database, or fitted recurrence enters the proof.

## Relationship to prior work

Dourado, Grippo, Lin and Protti (2026) study counting \(P_3\)-convex sets, prove general hardness and obtain efficient methods for trees and threshold graphs. Their accessible complete 2026 preprint does not give the present exact size-resolved ladder polynomial. The unweighted specialization \(P_n(1)\) for \(n\ge2\) is **already known** as OEIS A231376, compiled by R. H. Hardin in 2013; the fifth-order scalar recurrence and scalar generating function are also recorded there, including a 2018 contribution by Colin Barker. Neither this existing scalar sequence nor its scalar generating function implies the coefficients of \(P_n(z)\) for \(z\ne1\). Indeed, arbitrary different cardinality distributions can share the same sum. The assessed contribution is the fully refined two-variable generating function with a short polynomial-coefficient recurrence, not its pre-existing scalar shadow. Closed configurations under two-neighbor bootstrap percolation are the same objects under another name.

## Limitations

This result applies to width-two *open* ladders, not to cyclic ladders, wider strips, or arbitrary grids. The unweighted count and its scalar recurrence were published earlier and are not claimed as new. A precise size-dependent generating function may also exist in unindexed literature; source comparison provides best-knowledge originality, not historical uniqueness. No independent mathematical audit has been performed.

## References

- M. C. Dourado, L. N. Grippo, M. C. Lin, and F. Protti, *Counting P3-convex sets in graphs*, arXiv:2603.04706v1, first posted 2026-03-05, https://arxiv.org/html/2603.04706v1 .
- R. H. Hardin, *Number of n X 2 0..1 arrays with no element less than a strict majority of its horizontal and vertical neighbors*, OEIS A231376, original 2013; scalar recurrence and generating function recorded at https://oeis.org/A231376 .
- R. H. Hardin, two-dimensional count table, OEIS A231382, original 2013, https://oeis.org/A231382 .
- M. Przykucki, *Maximal percolation time in hypercubes*, Electronic Journal of Combinatorics 19(2) (2012), P41, for the correspondence of closed configurations to two-neighbor bootstrap percolation, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v19i2p41/pdf/ .
