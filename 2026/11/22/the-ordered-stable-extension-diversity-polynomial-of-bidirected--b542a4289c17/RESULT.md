# The ordered stable-extension diversity polynomial of bidirected paths

## Finding

Let \(F_n\) be the symmetric Dung argumentation framework whose underlying undirected graph is the labelled path on \(n\) vertices, including the empty path \(F_0\). Write \(\operatorname{Stab}(F_n)\) for its stable extensions. Define the ordered-pair distance polynomial
\[
P_n(z)=\sum_{(S,T)\in\operatorname{Stab}(F_n)^2}z^{|S\triangle T|}.
\]
Its **complete distance distribution**, simultaneously for every \(n\ge0\), is the rational series
\[
\boxed{\sum_{n\ge0}P_n(z)x^n=\frac{N(x,z)}{D(x,z)},}
\]
where
\[
\begin{aligned}
N(x,z)={}&1+x-xz+x^2-x^2z+2x^2z^2\\
&-x^3z-x^3z^2+x^4z^2-x^5z^2,\\
D(x,z)={}&1-xz-x^2-x^3+x^3z-x^3z^2\\
&+x^4z-x^5z^2+x^6z^2.
\end{aligned}
\]
For every \(n\ge2\), the largest possible distance is \(n\), attained by exactly **two ordered pairs**. Distance one never occurs between distinct stable extensions. In particular, \(P_n(z)\) has coefficient \(2\) at \(z^n\) for \(n\ge2\), and coefficient zero at \(z\) for every \(n\).

If \(S,T\) are sampled independently and uniformly from \(\operatorname{Stab}(F_n)\), then, writing \(\lambda>1\) for the unique positive root of \(\lambda^3=\lambda+1\),
\[
\boxed{\mathbb E|S\triangle T|=\frac{2(\lambda+1)(\lambda+2)}{(2\lambda+3)^2}\,n+O(1)
=0.484333938347657\ldots\, n+O(1).}
\]
Thus the exact enumerator also determines the limiting mean disagreement fraction.

## Assumptions and scope

The attack graph contains two reciprocal directed attacks for every neighboring pair, with no loops, chords, or additional attacks. A stable extension is conflict-free and attacks every argument outside itself. Distances count arguments belonging to exactly one of two extensions; ordered pairs and equal pairs are included. The unique stable extension of the empty graph is the empty set, so \(P_0(z)=1\). In the one-vertex case, \(P_1(z)=1\). The theorem does not concern complete extensions, one-way directed paths, or general argumentation frameworks.

## Proof

**1. Stable sets become maximal independent sets.** In any symmetric irreflexive attack graph, conflict-freeness is ordinary independence, and attacking each vertex outside a set is ordinary domination. Thus the stable extensions of \(F_n\) are precisely its maximal independent sets. A membership word \(b_1\cdots b_n\in\{0,1\}^n\) is such a set if and only if
\[
 b_jb_{j+1}=0\quad(1\le j<n),\qquad
 b_{j-1}\lor b_j\lor b_{j+1}=1\quad(1\le j\le n),
\]
where the fictitious boundary bits \(b_0=b_{n+1}=0\). These conditions encode independence and domination, including both endpoints.

**2. A six-state automaton counts pairs.** For two candidate membership words, collect both membership bits at position \(j\) into a column \(v_j\in\{00,01,10,11\}\). A state consists of consecutive columns \((u,v)\) satisfying \(u\mathbin{\&}v=00\) bitwise; there are nine states. The next state \((v,w)\) is permitted precisely when \(u_i\lor v_i\lor w_i=1\) for each of the two membership coordinates. Give this transition the weight \(z^{v_1\oplus v_2}\). Swapping the two membership coordinates is an automorphism of the weighted state graph. Its six state orbits, in order, are
\[
 (00,00),\quad \{(00,01),(00,10)\},\quad(00,11),\quad
 \{(01,00),(10,00)\},\quad\{(01,10),(10,01)\},\quad(11,00).
\]
The equitable quotient transition matrix, initial row recording the possible first columns after a left fictitious column \(00\), and terminal column imposing the right fictitious column \(00\), are
\[
Q(z)=\begin{pmatrix}
0&0&1&0&0&0\\
0&0&0&0&z&0\\
0&0&0&0&0&1\\
0&1&1&0&0&0\\
0&0&0&z&z&0\\
1&2&1&0&0&0
\end{pmatrix},\quad
\alpha=(1,2,1,0,0,0),\quad
\beta=(1,0,0,1,0,1)^{\mathsf T}.
\]
In particular, for every \(n\ge1\), \(P_n(z)=\alpha Q(z)^n\beta\). Every path pair is counted once, since the left and right virtual columns force precisely the endpoint domination conditions and each transition weights the symmetric-difference indicator of exactly one real column. The factor \(2\) in the last row of \(Q\) and the two initial orbit sizes are genuine multiplicities, not symmetries of labelled arguments.

**3. Exact rational generating function.** Formal summation gives
\[
\sum_{n\ge0}P_n(z)x^n=1+x\alpha Q(z)(I-xQ(z))^{-1}\beta.
\]
Direct exact polynomial matrix arithmetic gives \(\det(I-xQ(z))=D(x,z)\). Multiplication by this determinant and expansion of the adjugate gives exactly \(N(x,z)\), displayed above. Alternatively, the six-term Cayley–Hamilton recurrence from \(D\), together with the initial coefficients
\[
P_0(z)=1,\quad P_1(z)=1,\quad P_2(z)=2+2z^2,\quad P_3(z)=2+2z^3,\quad P_4(z)=3+4z^2+2z^4,\quad P_5(z)=4+4z^2+4z^3+2z^4+2z^5,
\]
uniquely determines the numerator; the standalone checker reproduces these finite polynomial arithmetic steps directly and checks 43 further coefficients. This proves the identity in the ring of formal power series, for all orders.

**4. The maximum and missing first distance.** The two alternating parity sets are both independent and dominating for every \(n\ge2\). Their ordered pair in either order disagrees at all \(n\) positions. Conversely, full disagreement forces two complementary zero–one membership words. Since both are independent, adjacent vertices must be assigned to opposite sets. Connectivity of the path forces exactly the two alternating assignments, proving both sharpness and multiplicity. Two distinct inclusion-maximal independent sets cannot differ at just one vertex, since this would make one properly contain the other; hence the distance-one coefficient vanishes.

**5. Typical disagreement.** At \(z=1\),
\[
D(x,1)=(x^3-x-1)(x^3-x^2+2x-1).
\]
The unique pole of smallest modulus is the simple positive root \(r=\lambda^{-2}\) of the second cubic; the other roots have strictly larger modulus. The numerator does not vanish at this root (also follows from the ordinary positive maximal-independent-set growth). The analytic root \(r(z)\) solving \(D(r(z),z)=0\) remains uniquely dominant for real \(z\) near one, giving
\[
 P_n(z)=C(z)r(z)^{-n}(1+O(\theta^n))
\]
locally uniformly, for analytic \(C(1)\ne0\) and some \(0<\theta<1\). Taking the derivative of \(\log P_n(z)\) at \(z=1\), and using \(P'_n(1)/P_n(1)=\mathbb E|S\triangle T|\), gives
\[
\mathbb E|S\triangle T|=
\frac{D_z(r,1)}{rD_x(r,1)}\,n+O(1).
\]
Substitute \(r=\lambda^{-2}\), reduce with \(\lambda^3=\lambda+1\), and simplify to the stated algebraic coefficient. The root separation can be checked directly from the two displayed cubics: the first has a real root \(\lambda>1\) and conjugates of modulus \(\lambda^{-1/2}>r\); the second has root \(r\) and conjugates of modulus \(r^{-1/2}>r\).

## Verification

Run `python3 check.py` using only the Python 3 standard library. It independently enumerates all maximal independent sets of paths through order 16, forms the complete ordered-pair Hamming-distance polynomials (17 orders, 17,206 ordered pairs), and compares them coefficientwise to the quotient transfer and the rational recurrence. It computes \(\det(I-xQ)\) exactly by permutation expansion and checks the transfer against 43 coefficients of the claimed rational function. The expected marker begins `VERIFY_OK exact determinant and 43 generating coefficients`. Every count is an integer computed directly. These finite checks supplement, but do not replace, the formal transfer proof and singularity argument. For example,
\[
P_8(z)=9+14z^2+12z^3+10z^4+20z^5+6z^6+8z^7+2z^8.
\]

## Relationship to prior work

Fichte, Hecher, Mahmood and Wang [1] introduce extension diversity and analyze pairwise symmetric-difference notions on general argumentation frameworks. The theorem here gives the **entire all-distance ordered-pair distribution for every bidirected path**, not just maximum distance or a complexity bound. Jahari and Alikhani [2] provide the independent-domination polynomial of a path, counting one maximal independent set by its cardinality; that polynomial does not record intersections or distances between two such sets. The existing Walsh-transform classification [3] concerns zero/nonzero frequencies of the maximal-independent-set indicator of paths. While the complete Walsh transform could indirectly recover a pair-distance distribution, its all-frequency values and the present rational enumerator do not follow from that nonvanishing classification. An earlier cycle result [4] enumerates individual complete extensions by size on bidirected **cycles**, not ordered pairs of stable extensions on paths. A separate three-viewpoint result [5] concerns directed degree-one graph components, not the bidirected path case (whose internal vertices have indegree two and outdegree two). Those comparisons isolate the present exact rational bivariate count and mean-disagreement law.

## Limitations

The statement is for labelled bidirected paths and **stable** extensions only; even cycle analogues, general trees, and complete extensions need other boundary rules. A finite-state derivation is elementary and does not establish absolute historical priority; earlier one-dimensional hard-core or domination-model transfer matrices might implicitly contain the same two-replica generating function. The singularity analysis controls the first moment up to bounded error, not an explicit central-limit theorem. Code checks finite lengths only. Independent mathematical or priority validation has not been performed.

## References

[1] J. K. Fichte, M. Hecher, Y. Mahmood and Z. Wang, *Diversity of Extensions in Abstract Argumentation*, first public 2026-05-13, arXiv:2605.13332. https://arxiv.org/abs/2605.13332

[2] S. Jahari and S. Alikhani, *On the Independent Domination Polynomial of a Graph*, arXiv:1808.07369 (2018). https://arxiv.org/abs/1808.07369

[3] *Period-seven Walsh invertibility of maximal-independent-set path kernels* (2026-11-16), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-period-seven-walsh-invertibility-of-maximal-independent-set-path--294497a01d79

[4] *Cyclic-gap classification and exact complete-extension polynomial of bidirected argumentation cycles* (2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-cyclic-gap-classification-and-exact-complete-extension-polynomia--3d211752e469

[5] *Exact three-viewpoint stable-extension diversity for degree-one argumentation graphs* (2026-10-26), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-three-viewpoint-stable-extension-diversity-for-degree-one--507cf5e0d7fc
