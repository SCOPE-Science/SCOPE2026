# A two-label correction formula for global Roman weight polynomials of wheel graphs

## Finding

For each integer \(n\ge 3\), let \(W_{n+1}=K_1\vee C_n\), with rim vertices \(0,\ldots,n-1\) and hub \(h\). A global Roman dominating function is a labeling \(f:V(W_{n+1})\to\{0,1,2\}\) in which every zero-labeled vertex has a two-labeled neighbor in the wheel and also a two-labeled neighbor in its complement. Let
\[
\mathcal G_n(x,y)=\sum_{f\text{ global Roman}}x^{\sum_v f(v)}y^{|\{i\in C_n:f(i)=2\}|}.
\]
The second variable records the number of rim vertices labeled two; a hub label of two contributes to the weight but not to the exponent of \(y\).

The complete, all-weights and all-rim-two-count polynomial \(\mathcal G_n\) has the following exact formula. Define \(T\) as the nine-by-nine matrix indexed by ordered pairs \((a,b)\in\{0,1,2\}^2\), with
\[
T_{(a,b),(b',c)}=\begin{cases}x^b y^{\mathbf1_{\{b=2\}}},& b=b'\text{ and }(b\ne0\text{ or }a=2\text{ or }c=2),\\0,&\text{otherwise},\end{cases}
\]
and put \(R_n(x,y)=\operatorname{tr}(T^n)\). For each two-element subset \(S\subseteq\{0,\ldots,n-1\}\), let \(U_S\) be the nonmembers of \(S\) adjacent on the rim to at least one member of \(S\), let \(X_S\) be those adjacent to exactly one member, and let \(B_S=U_S\setminus X_S\) (adjacent to both). Put \(F_{n,q}(x)=x^{n-2-q}(1+x)^q\) for \(0\le q\le n-2\). Define
\[
\begin{aligned}
A_n(x,y)={}&R_n(x,y)+ny\bigl(x^{n+1}-x^{n-1}(1+x)^2\bigr)\\
&+x^4y^2\sum_{|S|=2}\bigl(F_{n,|X_S|}(x)-F_{n,|U_S|}(x)\bigr),\\
B_n(x,y)={}&x^n+nx^4y(1+x)^{n-3}\\
&+x^4y^2\sum_{|S|=2}x^{|B_S|}(1+x)^{n-2-|B_S|}\\
&+(1+x+x^2y)^n-(1+x)^n\\
&-nx^2y(1+x)^{n-1}-\binom n2x^4y^2(1+x)^{n-2}.
\end{aligned}
\]
Then
\[
\boxed{\mathcal G_n(x,y)=xA_n(x,y)+x^2B_n(x,y)}.
\]
Although the expression contains subtractions, it is an identity in \(\mathbb Z[x,y]\) whose coefficients are nonnegative counts.

The minimum-weight counts (a refinement, not the first determination of the minimum weight itself) are
\[
(\gamma_{gR}(W_{n+1}),\#\mathrm{argmin})=\begin{cases}
(4,1),&n=3,\\(5,5),&n=4,\\(6,21),&n=5,\\(5,3),&n=6,\\(6,28),&n=7,\\(6,\binom n2),&n\ge8.
\end{cases}
\]
For every \(n\ge8\), all minimum labelings have hub label two and are exactly: (i) one rim label two, both neighboring rim vertices labeled one, every other rim vertex zero; or (ii) two rim labels two at cyclic distance different from two, every other rim vertex zero. There are respectively \(n\) and \(\binom n2-n\) such labelings.

## Assumptions and scope

Graphs are finite, simple and undirected; the rim is a *labeled* cycle on \(n\ge3\) vertices. All labels are from \(\{0,1,2\}\); this is global Roman domination, not signed Roman domination or total Roman domination. The generating polynomial counts individual labeled functions, not equivalence classes under graph automorphisms.

## Proof

Because the hub is isolated in the complement of a wheel, a global Roman labeling must assign the hub a positive value, either one or two. Split the sum accordingly, with rim enumerators \(A_n\) (hub one) and \(B_n\) (hub two).

First, \(R_n=\operatorname{tr}(T^n)\) is exactly the ordinary Roman labeling polynomial of the rim cycle: a closed length-\(n\) walk through pair-states encodes one cyclic word \(f(0),\ldots,f(n-1)\), and the edge weight inserts the middle label precisely when the middle zero has a neighboring two. Every cyclic word has exactly one such state walk with fixed labeled starting vertex (there is no division by \(n\)).

Write \(S=\{i:f(i)=2\}\) for the rim-two support. For a rim zero to be dominated in the wheel complement it must have a rim two outside its *closed* rim neighborhood; the hub never helps because it is universal in the wheel. When \(|S|\ge3\), at most two members of \(S\) can be rim neighbors of a zero, so its complement domination is automatic. Thus hub-one labelings with at least three rim twos are exactly the ordinary cycle Roman labelings. If \(|S|=0\), every rim vertex must be one and this is again counted correctly by \(R_n\). For \(|S|=1\), no rim zero can be complement-dominated, so the only \(n\) valid rim words have one two and all other entries one, of weight \(n+1\). The cycle Roman polynomial would have counted \(nyx^{n-1}(1+x)^2\): the chosen two, its two neighboring positions free in \(\{0,1\}\), and every other rim vertex one. Replacing this term gives the one-two correction in \(A_n\).

For \(|S|=2\), ordinary cycle Roman domination permits zero only in \(U_S\), while the additional complement condition permits zero only in \(X_S\), since a vertex adjacent to both selected twos lacks a complement-two neighbor. All remaining nonmembers of \(S\) must be one, and allowed positions may independently be zero or one. Thus the exact replacement in \(R_n\) is \(x^4y^2F_{n,|U_S|}\) by \(x^4y^2F_{n,|X_S|}\), for every \(S\), proving \(A_n\).

When the hub is labeled two, every rim zero already has a wheel-two neighbor. The only constraint is complement domination. For \(|S|=0\), there are no rim zeros and the rim contribution is \(x^n\). For \(|S|=1\), the two rim neighbors of the selected two must be one, and the remaining \(n-3\) positions are independently zero or one, giving \(nx^4y(1+x)^{n-3}\). For \(|S|=2\), a nonmember can be zero precisely when it is not adjacent to both selected twos. This gives \(x^4y^2x^{|B_S|}(1+x)^{n-2-|B_S|}\) for each \(S\). For \(|S|\ge3\), every zero is complement-dominated automatically, so all assignments with at least three rim twos qualify; subtracting the zero-, one-, and two-two terms from \((1+x+x^2y)^n\) gives the final line of \(B_n\). Multiplication by \(x\) or \(x^2\) accounts for the hub label and completes the polynomial identity.

For the minimum classification, note that a hub-one labeling with exactly two rim twos has weight at least \(1+4+(n-2-|X_S|)\ge n-1\), since \(|X_S|\le4\). With zero or one rim two it has weight \(n+1\) or \(n+2\), and with at least three it has weight at least seven. Hence for \(n\ge8\), hub one cannot achieve weight six. With hub two, zero rim twos has weight \(n+2\); one rim two forces two neighboring ones and has minimum weight six; two rim twos have minimum weight six exactly when \(B_S\) is empty; three or more rim twos have weight at least eight. For \(n\ge8\), precisely the \(n\) distance-two pairs of rim vertices have a common rim neighbor, so \(B_S=\varnothing\) for exactly \(\binom n2-n\) pairs. This proves the all-order minimum and multiplicity.

The five smaller rim orders reduce to the same exhaustive, explicit two-support categories: at \(n=3\), only the all-one hub-one labeling has weight four; at \(n=4\), the all-one labeling and four adjacent two-supports with hub one have weight five; at \(n=5\), weight-six minima consist of one all-one hub-one labeling, ten hub-one two-supports, five hub-two one-supports, and five hub-two adjacent two-supports; at \(n=6\), three antipodal two-supports with hub one yield weight five; at \(n=7\), seven rim-two one-supports and fourteen eligible two-supports with hub two, plus seven hub-one two-supports at distance three, yield 28 weight-six minima. Direct substitution into \(A_n,B_n\) checks each boundary case.

## Verification

The accompanying standalone `verify.py` independently enumerates all \(3^n\) rim assignments with hub label one or two for each \(3\le n\le9\); checks every coefficient of the complete bivariate formula against these counts; separately reconstructs the nine-state transfer trace and evaluates it at two integer variable pairs. The independent `verify_minima.cpp` exhaustively enumerates the two hub labels for \(3\le n\le12\) and checks each scalar minimum and count. Both are finite corroboration; the exact all-order result follows from the case arguments above.

Run `python3 verify.py` and `g++ -O3 -std=c++17 verify_minima.cpp -o verify_minima && ./verify_minima`. No external dependencies beyond Python 3 and a C++17 compiler are required.

## Relationship to prior work

Global Roman domination was introduced and investigated by Pushpam and Sampath in 2016, including known scalar values on wheels according to later literature. The exact scalar \(\gamma_{gR}(W_{n+1})\) is therefore **not claimed as new**. Reddy, Das, Kare and Reddy (2026) analyze the complexity of global Roman domination, including a linear-time algorithm on cographs, but do not give this two-variable, all-weight wheel census or the wheel optimizer classification. Ordinary Roman polynomial formulas, global Roman minimization algorithms, and signed-Roman wheel results cannot directly imply the simultaneous wheel/complement full enumerator; the extra complement constraints are responsible for the one- and two-rim-two corrections. No accessible source inspected gave the stated bivariate wheel identity or the all-order exact minimum multiplicity. Source accessibility and historical priority are limited as noted below.

## Limitations

The claim concerns wheel graphs and the exact definition of global Roman domination only. It does not prove a general polynomial formula for arbitrary universal-vertex graphs. Full text of the 2016 foundational wheel-value study could not be inspected through accessible lawful routes; an unindexed prior enumerator remains a specific historical-priority risk. This is a mathematical proof with independent finite computational corroboration, not external or independent scholarly certification.

## References

1. S. B. Reddy, A. K. Das, A. S. Kare and I. V. Reddy, *On the complexity of global Roman domination problem in graphs*, arXiv:2601.09167v1, first public 2026-01-14. https://arxiv.org/html/2601.09167v1
2. P. R. L. Pushpam and P. Sampath, *Global Roman domination in graphs*, Discrete Applied Mathematics **200** (2016), 176–185. https://doi.org/10.1016/j.dam.2015.07.014
3. G. Hao, Y. Wu and H. Jiang, *The relationship between global Roman domination number and Roman domination number of graphs*, Journal of Shandong University (Natural Science) **60** (2025), 52–56. https://doi.org/10.6040/j.issn.1671-9352.0.2023.301
