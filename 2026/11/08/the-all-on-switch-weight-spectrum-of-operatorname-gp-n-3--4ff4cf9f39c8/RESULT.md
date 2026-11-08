# The all-on switch-weight spectrum of \(\operatorname{GP}(n,3)\)

## Finding

For every integer \(n\ge 7\), let \(G=\operatorname{GP}(n,3)\) have vertices \(u_i,v_i\) for \(i\in\mathbb Z/n\mathbb Z\) and edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\) (indices modulo \(n\)). A subset \(S\subseteq V(G)\) is **odd dominating** if \(|S\cap N_G[x]|\) is odd for every vertex \(x\), where \(N_G[x]\) is the closed neighborhood. Equivalently, pressing precisely the switches in \(S\) sends the all-on Lights Out configuration to all-off, with each press toggling its vertex and all adjacent vertices.

Define the all-on strategy-weight enumerator
\[
W_n(z)=\sum_{S:\ |S\cap N_G[x]|\equiv1\ (\mathrm{mod}\ 2)\ \forall x\in V(G)} z^{|S|}.
\]
Put \(g=\gcd(n,20)\). **Theorem:** \(W_n(z)=R_g(z^{n/g})\), where the six explicit polynomials are
\[
\begin{aligned}
R_1(t)&=2t,\\
R_2(t)&=4t^2,\\
R_4(t)&=4t^2+8t^4+4t^6,\\
R_5(t)&=10t^3+12t^5+10t^7,\\
R_{10}(t)&=10t^6+44t^{10}+10t^{14},\\
R_{20}(t)&=4t^{10}+10t^{12}+60t^{18}+108t^{20}\\
&\qquad+60t^{22}+10t^{28}+4t^{30}.
\end{aligned}
\]
The new step-three phenomenon is clearest when compared with step two. Under the same outer/inner vertex labels, **every** all-on strategy for \(\operatorname{GP}(n,2)\) is also a strategy for \(\operatorname{GP}(n,3)\). The strategy sets are equal when \(4\nmid n\), but the latter has **exactly four times** as many solutions when \(4\mid n\). For \(20\mid n\), the extra solutions contribute precisely
\[
4z^{n/2}+60z^{9n/10}+64z^n+60z^{11n/10}+4z^{3n/2}.
\]
This index-four enlargement at multiples of four, and its complete new weight profile, is the main addition beyond the already determined step-two case.

In particular, the smallest number of switches and the number of minimum strategies are
\[
\min |S|=\begin{cases}
 n/2,&4\mid n,\\
 3n/5,&4\nmid n\ \text{and}\ 5\mid n,\\
 n,&4\nmid n\ \text{and}\ 5\nmid n,
\end{cases}
\]
with respectively \(4\), \(10\), and \(2\) (for odd \(n\)) or \(4\) (for even \(n\)) minimizers. When \(20\mid n\), exactly \(256\) strategies exist and their seven possible sizes are \(n/2,3n/5,9n/10,n,11n/10,7n/5,3n/2\), with respective counts \(4,10,60,108,60,10,4\).

All minimum strategies have explicit periodic descriptions. If \(4\mid n\), they are exactly the four translates, for \(r\in\{0,1,2,3\}\), of
\[
\{u_{4j+r},v_{4j+r+2}:0\le j<n/4\}.
\]
If \(4\nmid n\) and \(5\mid n\), they are exactly the ten translates, for \(r\in\{0,1,2,3,4\}\), of the two types
\[
\begin{aligned}
&\{u_{5j+r},v_{5j+r+2},v_{5j+r+3}:0\le j<n/5\},\\
&\{u_{5j+r},u_{5j+r+2},v_{5j+r+1}:0\le j<n/5\}.
\end{aligned}
\]
For all other \(n\), both full rings are minimum strategies; for even \(n\), the two additional alternating outer/inner selections are also minimum.

## Assumptions and scope

All graphs here are finite, undirected, simple, and use the standard generalized Petersen convention with \(n\ge7\) and step three. Indices are interpreted modulo \(n\). Strategies are vertex subsets; order of presses and repeated presses are disregarded because repeated presses cancel modulo two. The result counts labelled vertex subsets, not orbits under graph automorphisms. The polynomials \(R_g\) count formal periodic binary solutions of length \(g\); for small \(g\) they are not asserted to be the Lights Out polynomials of a separate simple graph \(\operatorname{GP}(g,3)\).

## Proof

Write \(a_i\in\mathbb F_2\) and \(b_i\in\mathbb F_2\) for the indicators of whether \(u_i\) and \(v_i\) are pressed. The closed-neighborhood equations are exactly
\[
 a_{i-1}+a_i+a_{i+1}+b_i=1,
 \qquad
 a_i+b_{i-3}+b_i+b_{i+3}=1
 \quad (i\bmod n).
\]
The first gives \(b_i=1+a_{i-1}+a_i+a_{i+1}\). Substitution in the second, collecting terms over \(\mathbb F_2\), gives
\[
 a_{i-4}+a_{i-3}+a_{i-2}+a_{i-1}+a_{i+1}+a_{i+2}+a_{i+3}+a_{i+4}=0.
\tag{1}
\]
Conversely, every binary cyclic sequence satisfying (1), together with this uniquely determined \(b\), solves both closed-neighborhood equations.

Let \(T\) denote the cyclic shift \((Ta)_i=a_{i+1}\). Multiplying the Laurent-polynomial form of (1) by \(T^4\) yields \(P(T)a=0\), where
\[
P(t)=1+t+t^2+t^3+t^5+t^6+t^7+t^8
=(t+1)^4(t^4+t^3+t^2+t+1)
\quad\text{in }\mathbb F_2[t].
\]
Since
\[
t^{20}+1=(t^5+1)^4=(t+1)^4(t^4+t^3+t^2+t+1)^4,
\]
we have \(P(t)\mid(t^{20}+1)\). Therefore \((T^{20}+1)a=0\): **every solution is 20-periodic**. It is also \(n\)-periodic, so it is \(g=\gcd(n,20)\)-periodic. Conversely, any \(g\)-periodic solution of (1) repeats to a solution for order \(n\), with the uniquely determined \(b\). Thus no solutions are omitted or duplicated by passing to the six divisors \(g\mid20\).

The characteristic recurrence is reversible and has order eight. If \(a_0,\ldots,a_7\) are fixed, its forward rule is
\[
a_{i+8}=a_i+a_{i+1}+a_{i+2}+a_{i+3}+a_{i+5}+a_{i+6}+a_{i+7}
\quad\text{in }\mathbb F_2.
\]
There are exactly \(2^8=256\) possible initial words. The factorization above ensures each uniquely extends to a bi-infinite 20-periodic sequence. Filter each such sequence by the condition \(a_i=a_{i\bmod g}\), compute \(b_i=1+a_{i-1}+a_i+a_{i+1}\), and count \(\sum_{i=0}^{g-1}(a_i+b_i)\). The full exhaustive count, with no heuristic search or omitted cases, is:

| Period \(g\) | Weight \(w\) : number of periodic strategies |
|---|---|
| \(1\) | \(1:2\) |
| \(2\) | \(2:4\) |
| \(4\) | \(2:4,\ 4:8,\ 6:4\) |
| \(5\) | \(3:10,\ 5:12,\ 7:10\) |
| \(10\) | \(6:10,\ 10:44,\ 14:10\) |
| \(20\) | \(10:4,\ 12:10,\ 18:60,\ 20:108,\ 22:60,\ 28:10,\ 30:4\) |

For comparison, the identical elimination for \(\operatorname{GP}(n,2)\) produces the equation \(P_2(T)a=0\), where \(P_2(t)=(t+1)^2(t^4+t^3+t^2+t+1)\). Thus \(P_2\mid P\), so the step-two solution space embeds in the step-three space with exactly the same \(b_i\) formula. On cyclic length \(n\), the dimensions are the degrees of \(\gcd(P_2(t),t^n+1)\) and \(\gcd(P(t),t^n+1)\). The two gcds agree when \(4\nmid n\); when \(4\mid n\), the multiplicity of \(t+1\) increases by two. This gives equality of the two solution sets off multiples of four and an index-four containment on multiples of four. Subtracting the established step-two enumerator from the displayed step-three polynomials gives the five-term new weight profile above when \(20\mid n\).

The standalone verifier `periodic_check.py` contains the eight-bit loop and checks every entry of this finite certificate; `gauss_check.cpp` independently reconstructs and solves the original \(2n\)-variable system. A \(g\)-periodic pattern repeats \(n/g\) times in order \(n\), multiplying its weight by \(n/g\), proving all six enumerator identities. Reading off the least exponent and its coefficient proves the minimum and its multiplicity. Inspecting the minimal initial words in the same exhaustive count yields the stated two periodic types for the five-phase case and the four translates in the four-phase case. These words are also directly verified by substitution in the two neighborhood equations.

## Verification

Run `python3 periodic_check.py` and `g++ -O2 -std=c++17 gauss_check.cpp -o gauss_check && ./gauss_check` in a directory containing the two standalone files. The Python program enumerates all \(256\) reversible-recurrence words, checks the six tabulated weight distributions, and tests every order from \(7\) through \(400\). The independent C++ program constructs the original closed-neighborhood matrix, performs binary reduced-row-echelon elimination, enumerates the entire affine solution space, and checks every order from \(7\) through \(100\). It additionally tests all \(2^{2n}\) possible vertex subsets directly for \(7\le n\le10\). Both were run successfully from the packaged source files.

## Relationship to prior work

The 2007 study by Fu, Yang and Jiang determines **ordinary** domination of \(\operatorname{GP}(n,3)\), not closed-neighborhood parity or all strategy weights. Torrence and Torrence (2016) study Lights Out on generalized Petersen graphs, give general linear-algebraic facts and finite nullity tables, and propose solving strategies; their results do not provide this all-on weight enumerator. Karami (2022) determines feasible parameter matrices for **equitable two-colorings** of the same family; exact neighbor-color counts differ from a parity constraint at each vertex, and those existence results do not count all odd dominating sets. Wang and Zhang (2026) classify perfect codes in generalized Petersen graphs: their four-translates theorem *does* already cover the \(4\mid n\) optimal sets of size \(n/2\), so neither their existence nor their number is claimed as new here. The earlier step-two all-on enumeration has the *same* weight distributions at orders not divisible by four, and this agreement is fully acknowledged: the comparison above proves equality of the underlying solution sets there. The new contribution is the **index-four expansion for orders divisible by four**, its complete weight splitting (especially the mixed twenty-period case), and the explicit all-order classification for step three. The existence and fourfold count of four-phase perfect-code minima are already known.

## Limitations

The theorem covers only step-three generalized Petersen graphs. The six finite counts depend on a compact exhaustive binary certificate; the standalone programs expose the whole count rather than relying on uninspectable logs. The proof is not a result about arbitrary target Lights Out configurations or about graph-independent minimum odd domination. Historical priority is qualified: an equivalent unpublished or unindexed weight enumeration could exist, and no independent scholarly audit has been performed. The previously known four-phase perfect-code minimum is explicitly excluded from the originality claim.

## References

1. Fu Xueliang, Yang Yuansheng and Jiang Baoqi, *On the Domination Number of Generalized Petersen Graphs \(P(n,3)\)*, Ars Combinatoria **84** (2007), 373–383. https://combinatorialpress.com/article/ars/Volume%20084/volume-84-paper-32.pdf (published 2007-07-31).
2. Bruce Torrence and Robert Torrence, *An Iterative Strategy for Lights Out on Petersen Graphs*, Involve **9** (2016), 721–732. DOI: 10.2140/involve.2016.9.721.
3. Hamed Karami, *Perfect 2-colorings of the generalized Petersen graph \(GP(n,3)\)*, Electronic Journal of Graph Theory and Applications **10** (2022), 239–245. DOI: 10.5614/ejgta.2022.10.1.16.
4. Xiaomeng Wang and Junyang Zhang, *Classification of perfect and total perfect codes in generalized Petersen graphs*, arXiv:2603.20722v1 (2026-03-21), Theorem 1.1.
