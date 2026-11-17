# A half-index Fibonacci reflection character for path Boolean complexes

## Finding

For each integer \(n\ge2\), let \(B_n\) be the Boolean complex of the \(n\)-vertex path \(P_n\), with its nontrivial diagram automorphism \(r\) reversing the vertices. Write \(F_0=0\), \(F_1=1\) and \(F_{j+2}=F_{j+1}+F_j\). The trace on the unique nonzero reduced rational homology group is

\[
t_n=\operatorname{tr}\!\left(r\mid\widetilde H_{n-1}(B_n;\mathbb Q)\right)=
\begin{cases}
(-1)^mF_m,&n=2m+1,\quad m\ge1,\\
1,&n=2,\\
(-1)^{m-1}F_{m-2},&n=2m,\quad m\ge2.
\end{cases}
\]

In particular, the complete rational \(C_2\)-module \(\widetilde H_{n-1}(B_n;\mathbb Q)\) has \(+1\) and \(-1\) eigenspace dimensions

\[
\frac{F_{n-1}+t_n}{2}\quad\text{and}\quad \frac{F_{n-1}-t_n}{2},
\]

respectively. For the **ordinary geometric quotient** (not a homotopy-orbit or stack quotient),

\[
\widetilde H_j(B_n/\langle r\rangle;\mathbb Q)=0\quad(j\ne n-1),\qquad
\dim_{\mathbb Q}\widetilde H_{n-1}(B_n/\langle r\rangle;\mathbb Q)
=\frac{F_{n-1}+t_n}{2}.
\]

The first traces for \(n=2,3,\ldots,12\) are \(1,-1,0,1,1,-2,-1,3,2,-5,-3\). The trace formula itself holds for all \(n\ge2\), not only this finite sample.

## Assumptions and scope

Label the path vertices \(1,\ldots,n\). An injective word is a string of distinct labels. Two injective words are equivalent if one can be obtained from the other by swaps of consecutive letters corresponding to **nonedges** of the path. A nonempty equivalence class on \(k\) letters represents one regular \((k-1)\)-cell of \(B_n\); its faces are induced by deletion of one letter. Use the increasing order of the underlying subset to orient each cell, and use augmented reduced cellular chains, where the empty word contributes in degree \(-1\).

The automorphism \(r(i)=n+1-i\) acts on all these cells. This is the standard Boolean cell complex of type \(A\) associated to a Coxeter path graph, **not** the unrestricted injective-word complex (which corresponds to a complete graph), nor the Coxeter complex. The established nonequivariant homotopy theorem gives \(B_n\simeq\bigvee^{F_{n-1}}S^{n-1}\); the new calculation is the explicit integral-valued *rational character trace* of the reflection and its quotient-rational-homology consequence.

## Proof

**1. Cellular model and signs.** A word commutation class with support \(S\subseteq[n]\) is determined by the relative order of the endpoints of each edge in the induced graph \(P_n[S]\). Equivalently it specifies an acyclic orientation of that induced graph. Since each induced component is a path, **every** edge orientation is acyclic. Hence cells on support \(S\) are in bijection with the \(2^{e(S)}\) orientations, where \(e(S)\) is the number of adjacent selected pairs. Deleting a vertex restricts the edge orientations. Reflection reverses the label order on a support of size \(k\), so its degree on each oriented cell carried to its reflected cell is \((-1)^{\lfloor k/2\rfloor}\). (This is the sign of the permutation reversing \(k\) positions.)

The reduced Lefschetz number of \(r\) is

\[
\widetilde L(r)=-1+
\sum_{\substack{S\ne\varnothing,\,rS=S}}
(-1)^{|S|-1+\lfloor |S|/2\rfloor}\,
\#\{\text{edge orientations of }P_n[S]\text{ fixed by }r\}.
\]

The leading \(-1\) is the augmented empty-cell term. A reflection-invariant orientation must reverse arrow directions on each mirrored edge; a central edge preserved setwise but reversed at its endpoints cannot occur in a fixed oriented graph.

**2. The half-path weighted sums.** For \(k\ge0\), put

\[
a_k=\sum_{T\subseteq[k]}(-1)^{|T|}2^{e(T)},\qquad
b_k=\sum_{\substack{T\subseteq[k]\\k\in T}}(-1)^{|T|}2^{e(T)}\quad(k\ge1),
\]

with \(a_0=1\). Here \(e(T)\) counts consecutive pairs in the smaller path. By splitting subsets according to inclusion of their last vertex,

\[
a_k=a_{k-1}+b_k,\qquad b_k=-a_{k-1}-b_{k-1}\quad(k\ge2),\]

with \(a_1=0\) and \(b_1=-1\). Hence \(a_k=a_{k-2}-a_{k-1}\) for \(k\ge2\), so

\[
a_k=(-1)^kF_{k-1}\quad(k\ge1),\qquad b_k=(-1)^kF_k\quad(k\ge1).
\]

The case \(a_0=1\) is retained separately.

**3. Even path.** If \(n=2m\), any invariant support consists of paired vertices about the middle, and cannot include both central vertices: that would force the central edge, whose orientation reverses. Thus invariant oriented cells correspond to nonempty \(T\subseteq[m-1]\), with \(2^{e(T)}\) choices of symmetric edge directions. Each such \(T\) has \(2|T|\) selected vertices, so its signed Lefschetz contribution is \(-(-1)^{|T|}2^{e(T)}\). Including the augmented empty cell gives \(\widetilde L(r)=-a_{m-1}\). The only reduced homology lies in degree \(2m-1\), hence \(\widetilde L(r)=-t_{2m}\) and \(t_{2m}=a_{m-1}\). This is \(1\) for \(m=1\), and \((-1)^{m-1}F_{m-2}\) for \(m\ge2\).

**4. Odd path.** If \(n=2m+1\), write a reflection-invariant support as mirrored pairs indexed by \(T\subseteq[m]\), optionally together with the central vertex. If the center is omitted, the augmented sum of signed contributions is \(-a_m\). If the center is present, its contributions sum to \(a_m+b_m\), because its two incident reflected edges contribute an additional binary orientation choice precisely when \(m\in T\). Thus \(\widetilde L(r)=b_m\). The top degree \(2m\) is even, so \(t_{2m+1}=b_m=(-1)^mF_m\).

**5. Rational quotient.** The previously established path Boolean-complex homotopy classification gives \(\widetilde H_{n-1}(B_n;\mathbb Q)\cong\mathbb Q^{F_{n-1}}\) and no other reduced groups. Since \(r^2=1\), its character is determined by dimension and trace; taking eigenspaces yields the displayed multiplicities. For a finite cellular action, subdividing equivariantly and averaging over the group identifies the rational homology of the ordinary orbit space with the invariant rational homology of the covering space. This establishes the quotient statement, without claiming an integral quotient classification.

## Verification

The standalone program `verify_boolean_path.py` enumerates all \(2^{e(S)}\) commutation classes for each nonempty \(S\subseteq[n]\), constructs actual signed cellular boundaries, and verifies \(\partial^2=0\) and \(r\partial=\partial r\). It independently computes exact fixed-cell Lefschetz traces for \(2\le n\le12\), and uses finite-field row reductions to check all homology ranks for \(2\le n\le8\) against the published Fibonacci ranks. `verify_output.txt` is the exact stdout from a successful fresh run (`VERIFY_OK`). Finite tests corroborate the identities; the recurrence proof covers all \(n\).

To reproduce with Python 3, from a folder containing the two auxiliary files run `python verify_boolean_path.py` and compare with `verify_output.txt`. No nonstandard Python dependencies are required.

## Relationship to prior work

Jonsson and Welker formulate commutation-class Boolean cell complexes and prove shellability; Ragnarsson and Tenner classify the homotopy type of Coxeter Boolean complexes and subsequently give explicit derangement-based homology generators and the path Fibonacci count. Those results determine the **total top-homology rank**, not its decomposition into reflection-invariant and reflection-anti-invariant parts. The present proof adds a signed fixed-cell enumeration and a half-index Fibonacci character. Complete-graph injective-word quotients and diagram reversals in other families of complexes do not imply this statement for path commutation classes. Relevant primary papers and their specific scope were compared; equivalently encoded character results outside indexed sources remain possible.

## Limitations

Only the diagram reversal of a path is treated. This is a rational representation theorem, not an integral module splitting, a torsion statement for the quotient, or an equivariant homeomorphism. The nonequivariant homotopy theorem is cited, while the new trace calculation and its recurrences are proved here. Novelty is assessed against the inspected literature and indexed research, not guaranteed against all unpublished or unindexed work. No independent mathematical audit has been performed.

## References

- J. Jonsson and V. Welker, *Complexes of injective words and their commutation classes*, Pacific Journal of Mathematics 243 (2009), 313–329; earliest preprint 2007-12-13. https://arxiv.org/abs/0712.2143 ; https://msp.org/pjm/2009/243-2/pjm-v243-n2-p07-s.pdf
- K. Ragnarsson and B. E. Tenner, *Homotopy type of the Boolean complex of a Coxeter system*, Advances in Mathematics 222 (2009), 409–430; preprint 2008-06-05. https://arxiv.org/abs/0806.0906
- K. Ragnarsson and B. E. Tenner, *Homology of the Boolean complex*, Journal of Algebraic Combinatorics 34 (2011), 617–639, especially §6.3, Corollary 6.12 (path Fibonacci multiplicities); preprint 2010-05-24. https://arxiv.org/abs/1005.4411 ; https://doi.org/10.1007/s10801-011-0285-5
