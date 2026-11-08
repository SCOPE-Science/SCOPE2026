# Parity-twisted equilibrium census for 0-or-3 public goods on prism networks

## Finding

In the homogeneous strict binary public-goods game with best-response pattern \(T_j=1\) precisely for \(j\in\{0,3\}\), let \(G_n=C_n\square K_2\) be the prism graph with \(n\ge3\) labeled rungs (and hence \(2n\) labeled agents). An agent chooses \(1\) if and only if either none or all three of their neighbors choose \(1\). Let \(N_n\) denote the number of pure Nash equilibrium action profiles.

Every equilibrium is either the all-active profile or has exactly one of the following three rung symbols at each position: \(0=(0,0)\), \(U=(1,0)\), \(D=(0,1)\). In the latter case the zero-rung positions partition the ring into gaps of lengths \(2\) and \(3\), and **the number of length-2 gaps must be even**. Conversely, every such cyclic gap arrangement with an even number of length-2 gaps admits exactly two complementary layer assignments and determines two equilibria.

Consequently, for all integers \(n\ge3\),

\[
N_n=1+2n\!\!\sum_{\substack{q,r\ge0,\ 2q+3r=n\\q\equiv0\pmod2}}
\frac{1}{q+r}\binom{q+r}{q}.
\]

The sum is empty when no admissible pair exists. In particular, \(N_3,N_4,\ldots,N_{12}=7,5,1,7,15,5,7,31,23,11\), and \(n=5\) is the **unique** value \(n\ge3\) for which all-active is the only equilibrium.

Writing \(S_n=N_n-1\), its exact ordinary generating function is

\[
\sum_{n\ge1}S_nz^n=
\frac{6z^3+4z^4-6z^6}{1-2z^3-z^4+z^6}.
\]

If \(\rho\approx1.324717957\) is the positive root of \(\rho^3-\rho-1=0\), then

\[
N_n\sim\rho^n,\qquad
\frac{N_n}{4^n}\sim\left(\frac{\rho}{4}\right)^n.
\]

The second statement is the exact exponential rarity of equilibrium among uniformly sampled binary profiles on these \(2n\)-agent networks.

## Assumptions and scope

The graph \(C_n\square K_2\) has vertices \((i,\ell)\) for \(i\in\mathbb Z/n\mathbb Z\), \(\ell\in\{0,1\}\), two horizontal neighbors \((i-1,\ell),(i+1,\ell)\), and one vertical neighbor \((i,1-\ell)\). The graph is simple and cubic for \(n\ge3\). All players have the same strict response rule \(T_0=T_3=1\), \(T_j=0\) at all other nonnegative integers. Each agent's response depends on their three *open* neighbors, not on their own current choice. Labeled vertices and labeled layers are distinguished; no quotient by rotations, reflections or layer exchange is taken. All \(2^{2n}=4^n\) action profiles have equal weight only when the probability statement is invoked.

## Proof

**1. Rung rigidity.** Let a rung have both agents active. Each of its two vertices has an active vertical neighbor, so to be best responding the other two neighbors must also be active; the alternative of zero active neighbors is impossible. Induction along the two rims forces all agents active. This profile is an equilibrium because every vertex has three active neighbors. Hence every other equilibrium uses only \(0,U,D\) rung symbols.

**2. Local constraints.** At a zero rung, each inactive vertex has an inactive vertical neighbor and must therefore have at least one active horizontal neighbor; because no rung is \((1,1)\), the two adjacent rungs are exactly \(U,D\) in some order. At a \(U\) rung the upper active vertex has an inactive vertical neighbor, so both its horizontal neighbors must be inactive in the upper layer; the adjacent rungs therefore lie in \(\{0,D\}\). The lower inactive vertex has an active vertical neighbor and cannot have two additional active horizontal neighbors, so at least one adjacent rung is \(0\). The analogous statement holds for a \(D\) rung. These conditions are also sufficient for all agents to best respond. They exclude adjacent zero rungs, force every nonzero run between successive zeros to have length one or two, and require the two nonzero symbols to be different in a run of length two. A configuration with no zero rung is impossible: it would alternate \(U,D\), making the inactive vertex of each rung have three active neighbors, contradicting best response.

**3. The parity obstruction.** Follow the cyclic zero rungs. A gap of total length \(2\), of the form \(0U0\) or \(0D0\), makes the first active symbol after the next zero *opposite* to the first active symbol after the current zero. A gap of length \(3\), \(0UD0\) or \(0DU0\), preserves that first symbol. Closure of the two possible layer assignments around the circle is therefore possible exactly when the number \(q\) of length-2 gaps is even. Once the first active symbol is chosen, every other symbol is forced; the two choices give distinct equilibria. In conjunction with step 1, this proves the structural classification.

**4. Exact count.** Let \(q\) and \(r\) be the numbers of gaps of length \(2\) and \(3\), so \(2q+3r=n\) and there are \(k=q+r>0\) zero rungs. On the vertex-labeled cycle, the number of length patterns is exactly \(\frac{n}{k}\binom{k}{q}\): choose one distinguished zero position in \(n\) ways and an ordered list of \(q\) length-2 and \(r\) length-3 gaps in \(\binom{k}{q}\) ways, then divide by the \(k\) choices of distinguished zero of each resulting arrangement. The even-\(q\) condition and the two layer assignments yield the stated sum; the separate all-active profile contributes one.

**5. Generating function, uniqueness and entropy.** For an ordinary uncolored cyclic composition using gaps of length \(2\) and \(3\), the coefficient generating function is \(-z\,\frac{d}{dz}\log(1-z^2-z^3)\). Weighting each length-2 gap by \(-1\) instead gives \(-z\,\frac{d}{dz}\log(1+z^2-z^3)\). Adding the two sums keeps twice the even-\(q\) arrangements and deletes the odd-\(q\) arrangements. Therefore

\[
\sum_{n\ge1}S_nz^n=-z\frac{d}{dz}\log\!\left[(1-z^2-z^3)(1+z^2-z^3)\right]
=\frac{6z^3+4z^4-6z^6}{1-2z^3-z^4+z^6}.
\]

The reciprocal denominator polynomial factors as

\[
x^6-2x^3-x^2+1=(x^3-x-1)(x^3+x-1).
\]

The equivalent six-state nonnegative transfer matrix on consecutive distinct rung symbols \((0,U),(0,D),(U,0),(U,D),(D,0),(D,U)\), using these states in row and column order, is

\[
B=\begin{pmatrix}
0&0&1&1&0&0\\
0&0&0&0&1&1\\
0&1&0&0&0&0\\
0&0&0&0&1&0\\
1&0&0&0&0&0\\
0&0&1&0&0&0
\end{pmatrix}.
\]

Indeed, its entries encode precisely the local allowed middle-rung configurations and \(S_n=\operatorname{tr}(B^n)\). Direct determinant expansion gives \(\det(xI-B)=x^6-2x^3-x^2+1\). This matrix is primitive: its directed graph is strongly connected and has directed cycles of lengths \(3\) and \(4\). Its positive Perron eigenvalue is \(\rho\), the unique positive real root of \(x^3-x-1\). Perron--Frobenius and the fact that the eigenvalue occurs once in the characteristic polynomial give \(S_n=\rho^n+o(\rho^n)\), and adding the single all-active equilibrium does not change the asymptotic. Equilibrium density follows on dividing by \(4^n\). Finally, an admissible pair exists exactly when \(n=4a+3b\) for some nonnegative integers \(a,b\) not both zero: set \(q=2a\), \(r=b\). Every \(n\ge6\), as well as \(3\) and \(4\), has this representation, whereas \(5\) does not. Thus \(N_n=1\) exactly for \(n=5\) among \(n\ge3\).

## Verification

The standalone, standard-library-only script `verify.py` evaluates the best-response condition independently on every one of \(4^n\) labeled action profiles for each \(3\le n\le9\), totaling 349,504 direct profiles. It independently implements the cyclic gap formula, a six-state exact transfer matrix, 100 power-trace comparisons, and checks the matrix identity \(B^6-2B^3-B^2+I=0\). Its execution prints `VERIFY_OK` after all assertions pass. The infinite statements follow from the argument above, not from finite experiments.

## Relationship to prior work

Klimm and Stahlberg's 2023 paper formalizes strict binary public-goods games with best-response patterns and proves NP-completeness for the class of picky patterns \(10^k10^*\), including the present \(10010^*\) pattern (Theorem 5.11); Gilboa's independently developed 2023 complexity classification covers all finite non-monotone patterns. Those are existence/complexity theorems for unrestricted graphs. They do not provide the prism-specific exact equilibrium census, parity-twisted rung classification, uniqueness at \(n=5\), or the exact exponential abundance law. The ordinary Perrin/plastic-constant recurrence for unrestricted compositions into lengths two and three is classical; the result claimed here is the *game-theoretic* correspondence and its additional even-gap constraint, not a new discovery of that recurrence. Related parity-response graph games differ here: the present degree-three response selects neighbor counts \(0\) and \(3\), not even neighbor counts \(0\) and \(2\).

## Limitations

This is a complete result only for the specified homogeneous rule and fixed cylindrical cubic graphs; it does not assert a tractable equilibrium-counting algorithm on arbitrary graphs. A limiting base inferred from a rational generating function is not a universal network entropy. Previously unindexed equivalent counts or reductions to existing graph enumerators could affect publication priority. Independent expert checking and independent validation have not been performed.

## References

1. M. Klimm and M. J. Stahlberg, *Complexity of equilibria in binary public goods games on undirected graphs*, arXiv:2301.11849 (first public version 2023-01-27), especially Sections 2 and 5, Theorem 5.11. https://arxiv.org/abs/2301.11849
2. M. Gilboa, *A Characterization of Complexity in Public Goods Games*, arXiv:2301.11580 (first public version 2023-01-27), especially Sections 1--4. https://arxiv.org/abs/2301.11580
