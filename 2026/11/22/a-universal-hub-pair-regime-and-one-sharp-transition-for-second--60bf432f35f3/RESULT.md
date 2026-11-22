# A universal hub-pair regime and one sharp transition for second-order coherence on weighted quadrilateral books

## Finding

Let \(B_m(t)\) be the graph of \(m\) four-cycles sharing one edge, with two common hubs \(h_0,h_1\), \(m\) pairs of peripheral vertices \(u_i,v_i\), and conductances \(1\) on the hub edge and every hub-to-peripheral edge, and \(t>0\) on the \(m\) peripheral rung edges \(u_iv_i\). Let \(m\ge2\). For exactly two perfectly pinned leaders \(S\), let \(F=V\setminus S\) and minimize
\[
J_2(S)=\operatorname{tr}\bigl(L_{FF}(S)^{-2}\bigr),
\]
where \(L_{FF}(S)\) is the follower principal submatrix of the **full weighted Laplacian**. Then:

1. For every integer \(m\ge3\) and every \(t>0\), the unique minimizing leader set is \(\{h_0,h_1\}\), and the exact minimum is
\[
J_2^*(m,t)=\frac{2m(2t^2+2t+1)}{(2t+1)^2}.
\]
2. For \(m=2\), define \(\tau\) as the unique positive zero of
\[
q(t)=54t^4+126t^3+37t^2-48t-23.
\]
The unique minimizer for \(0<t<\tau\) is the two hubs. For \(t>\tau\), the only minimizers are the two sets \(\{u_1,v_2\}\) and \(\{v_1,u_2\}\), with one peripheral leader on each side and different rungs. At \(t=\tau\), all three listed sets and no others minimize. Numerically \(\tau\approx0.62270087273621\), with \(3/5<\tau<7/10\). For \(m=2\), their objective-value difference is exactly
\[
J_2(\{u_1,v_2\})-J_2(\{h_0,h_1\})=
-\frac{2q(t)}{(2t+1)^2(4t+3)^2}.
\]

In particular, the weighted infinite family has a single two-rung transition but **no hub-abandonment transition for any larger book**, independent of the rung conductance. At \(m=3,t=1\), the squared-inverse objective selects the two hubs, whereas the established first-inverse-power objective selects a hub and a peripheral on the opposite side: the optimal placements for the two coherence orders differ.

## Assumptions and scope

The vertices are \(h_0,h_1,u_1,v_1,\ldots,u_m,v_m\). Edges are \(h_0h_1\), \(h_0u_i\), \(h_1v_i\) of unit conductance, and \(u_iv_i\) of conductance \(t\), with no other edges. The two pinned vertices are held exactly, not attached to finite-gain feedback; therefore the grounded matrix retains the original weighted degree diagonals, including contributions from edges to leaders. Every \(t\) is a strictly positive real number, not just an integer or rational. Each follower principal Laplacian is positive definite because the underlying graph is connected and \(S\ne\varnothing\). Leader sets are unordered and distinct.

## Proof

The automorphism group permutes the \(m\) rungs and interchanges the two hub layers simultaneously. Hence exactly six pair types cover every candidate: HH (both hubs), HS (hub and a peripheral adjacent to that hub), HO (hub and a peripheral on the opposite layer), LLs (two peripherals in distinct rungs on the same layer), LLc (the two peripherals of one rung), LLd (two peripherals in different rungs and opposite layers). The names refer to *leader locations*.

Here is an exact rational formula for each orbit's cost, suitable for independently reconstructing the comparisons. Retain \(k\in\{0,1,2\}\) unpinned hubs, let \(H\) be their principal block with diagonals \(m+1\) and off-diagonal \(-1\) if both hubs remain. For each surviving leaf column, use the principal submatrix \(D_i\) of
\[
D_0=\begin{pmatrix}1+t&-t\\-t&1+t\end{pmatrix}
\]
restricted to its unpinned peripherals, and let \(B_i\) have a \(1\) at the corresponding incidence with an unpinned hub (and \(0\) otherwise). For a removed pair of peripherals, the block is empty. Put
\[
M_r=\sum_i B_i^{\mathsf T}D_i^{-r}B_i\quad(r=1,2,3),\qquad
X=(H-M_1)^{-1},\qquad T_2=\sum_i\operatorname{tr}(D_i^{-2}).
\]
When \(k=0\), take \(J_2=T_2\). Otherwise the block inverse formula gives **exactly**
\[
J_2=\operatorname{tr}(X^2)+2\operatorname{tr}(X^2M_2)+T_2+
2\operatorname{tr}(XM_3)+\operatorname{tr}(XM_2XM_2). \tag{1}
\]
Indeed, the grounded inverse is the block matrix with upper left block \(X\), upper right block \(XB^{\mathsf T}D^{-1}\), and lower right block \(D^{-1}+D^{-1}BXB^{\mathsf T}D^{-1}\); squaring and taking the trace yields (1). Each \(D_i\) is positive definite. The Schur complement \(H-M_1\) is positive definite, as is the grounded Laplacian, so no singular division occurs.

The six types correspond, respectively, to the following lists of surviving hub indices and rung-column multiplicities, where \(11\) retains both peripherals, \(10\) the top alone, \(01\) the bottom alone, and \(00\) neither:

| Type | Surviving hub indices | Rung multiplicities |
|---|---|---|
| HH | none | \(m\) of \(11\) |
| HS | bottom hub | \(m-1\) of \(11\), one \(01\) |
| HO | bottom hub | \(m-1\) of \(11\), one \(10\) |
| LLs | both hubs | \(m-2\) of \(11\), two \(01\) |
| LLc | both hubs | \(m-1\) of \(11\), one \(00\) |
| LLd | both hubs | \(m-2\) of \(11\), one \(01\), one \(10\) |

These conventions yield all six exact rational expressions directly from (1), without any numerical approximation. For \(m\ge3\), let \(a=m-3\ge0\), and for each type \(T\ne\mathrm{HH}\), write the exact rational difference from (1) in reduced factored form \(J_2(T)-J_2(\mathrm{HH})=N_T(m,t)/Q_T(m,t)\). Every denominator \(Q_T\) is a product of positive powers of polynomials with nonnegative coefficients and positive constant terms. The complete integer polynomial expansion of \(N_T(a+3,t)\) has **strictly positive** coefficients in every nonzero monomial. In type order HS, HO, LLs, LLc, LLd, the numbers of nonzero monomials are exactly \(21,21,32,22,32\), with respective minimum coefficients \(1,1,1,4,4\). The standalone symbolic checker derives these polynomials from (1) and verifies every coefficient (rather than checking finitely many values of \(m\) or \(t\)). Thus all other five leader types are strictly worse for every \(m\ge3,t>0\).

For \(m=2\), exact substitution into (1) gives the stated HH–LLd difference. The polynomial \(q\) has exactly one sign change in its descending coefficients; by Descartes' rule it has at most one positive zero. Since \(q(3/5)<0<q(7/10)\), it has precisely one. To exclude all other four types, the numerators of HS–LLd, LLs–LLd, and LLc–LLd have all strictly positive coefficients (and positive denominators), hence those three never win. For HO, compare against HH on \(0<t\le3/5\) and against LLd on \(t\ge3/5\). The numerator of HO–HH after \(t=3z/[5(1+z)]\), multiplied by \([5(1+z)]^6\), has, in descending powers of \(z\), the strictly positive coefficients
\[
788929,\ 3717300,\ 6412500,\ 5489750,\ 2544375,\ 618750,\ 62500.
\]
The numerator of HO–LLd after \(t=z+3/5\) also has all nine coefficients strictly positive; both denominators have positive coefficients. Therefore HO cannot be optimal anywhere. This completes the exhaustive classification, with all ties as stated.

## Verification

The standalone \(\texttt{checker.py}\) uses exact SymPy rational algebra to construct the six orbit costs from the Schur formula, checks positive denominators and all claimed all-parameter coefficient certificates, verifies the quartic threshold and its uniqueness, and checks both complementary HO domains. It then constructs the entire grounded Laplacian **independently**, enumerates every unordered leader pair for \(m=2,\ldots,8\) and several positive rational and floating rung conductances, and compares its spectral inverse-square cost against the orbit formula and the predicted minimizers. The check is a useful independent finite diagnostic; the symbolic polynomial identities, not its finite samples, provide the all-size and all-\(t\) argument. Run with `python checker.py` using Python, SymPy and NumPy.

## Relationship to prior work

Earlier leader-selection theory treats grounded inverse trace and network coherence, but that objective is not interchangeable with its squared-inverse analogue. An earlier first-order classification on the same unweighted quadrilateral-book graph finds an opposite-layer hub–peripheral optimizer at three rungs, whereas the present second-order theorem selects the hub pair at three rungs for *all* positive rung conductances. Chen, Li and Sun's full study of book-graph coherence computes ungrounded first-order Laplacian spectral sums as a function of graph size, not optimal two-leader squared-inverse placement. General second-order coherence studies motivate the spectral objective, but do not imply the stated exact weighted-book optimizer classification. Similar names or the existence of a six-orbit first-order reduction alone do not establish the squared-inverse polynomial signs.

## Limitations

The result applies to exactly two perfect leaders, equal unit hub and spoke conductances, and one common strictly positive rung conductance; it does not classify finite-gain pinning, heterogeneous rung conductances, or three or more leaders. The symbolic certificate has been checked with a computer-algebra system, not with an independent proof assistant; the proof above identifies the finite coefficient comparisons whose exact output can be reproduced from the included code. Literature and record searches cannot establish absolute priority. An accessible first-order record on the same graph was recoverable by its statement, but its complete manuscript was not available for all-section comparison; an undiscovered equivalent second-order result remains possible.

## References

- S. Patterson and B. Bamieh, *Consensus and Coherence in Fractal Networks* (public preprint 9 October 2013), https://arxiv.org/abs/1310.2592 . Discusses Laplacian inverse-power coherence, not the present perfect-leader classification.
- A. Clark, L. Bushnell and R. Poovendran, *A Supermodular Optimization Framework for Leader Selection under Link Noise in Linear Multi-Agent Systems* (public preprint 4 August 2012), https://arxiv.org/abs/1208.0946 . General first-order leader selection, not the stated inverse-square weighted-book optimum.
- J. Chen, Y. Li and W. Sun, *Network Coherence in a Family of Book Graphs*, Frontiers in Physics **8**, 583603 (16 October 2020), https://doi.org/10.3389/fphy.2020.583603 . Studies ungrounded first-order coherence of the same book-graph family.
- An earlier public result, *A three-stage two-leader transition on quadrilateral book graphs* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-three-stage-two-leader-transition-on-quadrilateral-book-graphs--3b37aec41c1b . Reported first-order leader placement, contrasted with the squared-inverse objective here; only its indexed statement was accessible for detailed comparison.
