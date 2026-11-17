# Exact Euclidean edge spectrum and a Dirichlet length-condensation law for Loday associahedra

## Finding
For every integer \(N\ge3\), let \(\mathcal A_N\) be Loday's canonical associahedron with \(N\) ordered leaves, embedded in \(\mathbb R^{N-1}\) with its ordinary, unrescaled Euclidean metric. Each edge has one canonical right-rotation description \(((A B) C)\to(A(B C))\). Write \(a,b,c\ge1\) for the numbers of leaves in its three designated subtrees and \(r=N-a-c\ge1\) for the total number of leaves in \(B\) and outside this rotation.

With \(C_j=\binom{2j}{j}/(j+1)\), the **complete two-parameter edge-multiplicity law** is
\[
M_N(a,c)=\frac12 C_{a-1}C_{c-1}\binom{2(N-a-c)}{N-a-c}
\qquad(a,c\ge1,\ a+c\le N-1).
\]
Every such edge has Euclidean length \(\sqrt2\,ac\); this local length formula itself was given by Loday and is not claimed as new. Consequently the number of edges of length \(\sqrt2\,q\), for any positive integer \(q\), is exactly
\[
\sum_{\substack{a,c\ge1,\ ac=q\\a+c\le N-1}}M_N(a,c).
\]
The **total length** of the complete one-skeleton is \(\sqrt2\,W_N\), where
\[
W_N=\frac12\left[(2N-3)\binom{2N-4}{N-2}-4^{N-2}\right],
\]
and the number of edges is \(E_N=(N-2)C_{N-1}/2\). Thus a uniformly sampled edge has mean Euclidean length \(\sim N/\sqrt2\), even though its length converges in distribution to a finite random variable.

More precisely, for a uniformly chosen unoriented edge, its uniquely oriented right rotation has outer leaf sizes \((A_N,C_N)\) satisfying
\[
(A_N,C_N)\ \Rightarrow\ (A,C),\quad
\Pr(A=j)=\Pr(C=j)=\frac{2C_{j-1}}{4^j},\quad j\ge1,
\]
where \(A,C\) are independent and have infinite means. In contrast, choose an edge with probability proportional to its *Euclidean length* and let \((A_N^*,C_N^*,R_N^*)\) denote its two outer leaf counts and the remaining count. Then
\[
\boxed{\left(\frac{A_N^*}{N},\frac{C_N^*}{N},\frac{R_N^*}{N}\right)
\Rightarrow\operatorname{Dirichlet}\left(\frac12,\frac12,\frac12\right).}
\]
In particular, almost all total one-skeleton length, in the limiting sense, belongs to edges whose two outer subtrees and complementary region each occupy positive fractions of the leaves, whereas a uniformly counted edge has outer sizes of bounded order in probability.

## Assumptions and scope
A rooted plane full binary tree has ordered leaves and every internal vertex has two children. For a tree \(T\) with \(N\) leaves, label its \(N-1\) internal vertices in infix order. If \(L_i(T)\) and \(R_i(T)\) are the numbers of leaves in the two child subtrees of its \(i\)-th internal vertex, put
\[
v(T)=(L_1(T)R_1(T),\ldots,L_{N-1}(T)R_{N-1}(T)),
\qquad \mathcal A_N=\operatorname{conv}\{v(T):T\text{ has }N\text{ leaves}\}.
\]
The ambient Euclidean norm restricts to the affine span of this polytope. Each rotation on an internal edge corresponds to exactly one undirected polytope edge, and its inverse rotation is not counted separately. The right-rotation orientation is a bookkeeping convention; every unoriented edge has exactly one representative of this form. The asymptotics send \(N\to\infty\) through integers; no assertion is made for alternative affine realizations or changes of Euclidean metric. Probabilistic weak convergence uses the usual topology on \(\mathbb N^2\) and on the closed two-simplex, respectively.

## Proof
**1. Local Euclidean metric (known input, independently reconstructed).** In the local rotation \(((A B) C)\to (A(B C))\), let the leaf sizes be \(a,b,c\). The two infix coordinates at the affected internal vertices change from \(ab,(a+b)c\) to \(a(b+c),bc\). Their differences are \(ac,-ac\); no other coordinate changes. Therefore the edge has Euclidean length \(\sqrt{(ac)^2+(-ac)^2}=\sqrt2\,ac\). The identification of rotations with polytope edges and this local length were already established in Loday's original work, especially Propositions 2.9 and Section 2.10; the novel work starts with counting the complete metric spectrum and deriving its two sampling limits.

**2. Exact marked-rotation enumeration.** Define the Catalan leaf-tree series
\[
T(z)=\sum_{m\ge1}C_{m-1}z^m=\frac{1-\sqrt{1-4z}}2,
\quad T(z)=z+T(z)^2.
\]
A rooted binary context with one distinguished substitution hole has series \(H(z)=1+2T(z)H(z)=(1-2T(z))^{-1}\), where the variable counts leaves outside the hole. A uniquely oriented rotation consists of the three ordered subtrees \(A,B,C\) grafted into such a context. Fixing the sizes of \(A,C\), and summing over the remaining subtree \(B\) and context, gives
\[
M_N(a,c)=C_{a-1}C_{c-1}[z^{N-a-c}]\frac{T(z)}{1-2T(z)}.
\]
Since
\[
\frac{T(z)}{1-2T(z)}=
\frac12\big((1-4z)^{-1/2}-1\big),
\]
the displayed binomial multiplicity follows. The substitution is bijective because a Tamari right rotation has a unique local site and ordered triple, and the surrounding binary context is uniquely recovered.

**3. Exact first length moment.** The standard Catalan count gives \(C_{N-1}\) vertices, each of degree \(N-2\). Dividing by two yields \(E_N=(N-2)C_{N-1}/2\). If \(W_N=\sum_e|e|/\sqrt2=\sum_{a,c}acM_N(a,c)\), the marked-tree decomposition yields
\[
\sum_{N\ge3}W_Nz^N
=\big(zT'(z)\big)^2\frac{T(z)}{1-2T(z)}
=\frac{z^2}2\big((1-4z)^{-3/2}-(1-4z)^{-1}\big).
\]
Here \([z^m](1-4z)^{-3/2}=(2m+1)\binom{2m}m\); extracting the coefficient of \(z^N\) gives the formula for \(W_N\). The central-binomial asymptotic \(\binom{2n}n\sim4^n/\sqrt{\pi n}\) yields
\[
E_N\sim\frac{4^N}{8\sqrt{\pi N}},\qquad
W_N\sim\frac{4^N\sqrt N}{16\sqrt\pi},\qquad
\frac{\sqrt2 W_N}{E_N}\sim\frac N{\sqrt2}.
\]

**4. Uniform-edge law.** For fixed positive \(a,c\) and \(N\to\infty\), dividing the exact multiplicity by \(E_N\) gives
\[
\frac{M_N(a,c)}{E_N}\longrightarrow
\frac{4C_{a-1}C_{c-1}}{4^{a+c}}
=p_ap_c,\quad p_j=\frac{2C_{j-1}}{4^j}.
\]
The Catalan generating-function identity \(\sum_{j\ge1}p_j=\tfrac12\sum_{k\ge0}C_k4^{-k}=1\) shows that this pointwise limit has total probability one. Thus it is a true weak limit on the discrete space, not merely a defective pointwise limit. As \(j\to\infty\), \(p_j\sim(2\sqrt\pi)^{-1}j^{-3/2}\), so the two limiting variables have infinite means. The continuous mapping theorem gives convergence of the uniformly sampled edge length to \(\sqrt2 AC\), a finite almost-sure random variable. The diverging finite means above show failure of uniform integrability.

**5. Length-biased macroscopic limit and boundary control.** A length-proportionately sampled edge with outer sizes \(a,c\) has exact mass \(acM_N(a,c)/W_N\). Put \(r=N-a-c\). On compact subsets of the strictly positive open simplex, Stirling's formula implies, uniformly for \((a/N,c/N,r/N)\to(u,v,w)\),
\[
\frac{acM_N(a,c)}{W_N}
=\frac{1+o(1)}{2\pi N^2\sqrt{uvw}}.
\]
The function \(f(u,v,w)=1/(2\pi\sqrt{uvw})\), for \(u,v,w>0\) and \(u+v+w=1\), integrates to one by the beta-integral identity \(\Gamma(1/2)^3/\Gamma(3/2)=2\pi\). It is exactly the \(\operatorname{Dirichlet}(1/2,1/2,1/2)\) density.

To rule out escape of probability toward a boundary, the standard central-binomial bounds and the exact formula give universal constants \(K,k>0\) such that, for every \(a,c,r\ge1\) with sum \(N\),
\[
acM_N(a,c)\le K\frac{4^N}{\sqrt{acr}},\qquad
W_N\ge k4^N\sqrt N
\]
for all sufficiently large \(N\). Moreover, \(\sum_{c=1}^{m-1}\big(c(m-c)\big)^{-1/2}\) is uniformly bounded in \(m\ge2\). Summing first over \(c+r=N-a\) and then \(a\le\varepsilon N\) gives
\[
\Pr(A_N^*/N\le\varepsilon)\le K'\sqrt\varepsilon,
\]
with identical bounds for \(C_N^*/N\) and \(R_N^*/N\), after adjusting constants. Hence the lattice Riemann sums converge on the full simplex, establishing the claimed Dirichlet limit with no unaccounted boundary mass. This completes all claims.

## Verification
Run `python3 LODAY_EDGE_CHECK.py` with Python 3; no third-party packages or external data are required. The program independently generates all full binary trees on \(3\le N\le8\) leaves, computes both endpoint coordinate vectors for every oriented local right rotation, compares the exact two-parameter multiplicities, checks vertex and edge counts, checks complete summed Euclidean lengths and maximal edge lengths. Successful output ends with `LODAY_EDGE_SPECTRUM_PASS`. Verified total normalized lengths for these leaf counts are \(1,7,38,187,874,3958\). These finite exact checks corroborate the finite formulas but do not replace the generating-function and analytic proofs of the all-dimensional and limiting assertions.

## Relationship to prior work
Loday's *Realization of the Stasheff polytope* (2002 preprint; 2004 publication) gives the binary-tree coordinates, the edge/rotation correspondence, the local \(\sqrt2\,ac\) length and the longest-edge length; none of those elementary facts is asserted as novel here. Pilaud, Santos and Ziegler's 2023 survey provides a modern primary exposition of that realization and the underlying normal-fan structure. Padrol, Palu, Pilaud and Plamondon (2023) study generalized associahedral realization cones, a different metric question. The sequence of summed normalized edge lengths \(1,7,38,187,\ldots\) coincides numerically with **OEIS A000531**, where it is associated with the algebraic degree of cyclic-polygon area. Its integer values or binomial expression are therefore **not** claimed to be a previously unknown numerical sequence. The contribution assessed here is the canonical-polytope metric interpretation, full two-parameter multiplicities, independent microscopic uniform-edge law, and length-weighted macroscopic Dirichlet limit, including the contrasting sampling regimes. No inspected source establishes that joint statement.

## Limitations
Historical originality is assessed against inspected primary texts, public mathematical databases and the checked accessible related claims; absence from these is not a proof of absolute priority. A prior unindexed result on marked Catalan rotations may imply the exact multiplicities or the Dirichlet law even without explicitly mentioning Euclidean associahedra. The normalizations apply only to Loday's fixed integer-coordinate Euclidean realization; other associahedral realizations can have different lengths. Finite tests cover only \(3\le N\le8\); all-dimensional validity rests on the analytic proof. No independent mathematical audit or external certification is asserted.

## References
- J.-L. Loday, *Realization of the Stasheff polytope*, arXiv:math/0212126v1 (first public 2002-12-09), especially Proposition 2.9 and Section 2.10, https://arxiv.org/pdf/math/0212126.
- V. Pilaud, F. Santos, G. M. Ziegler, *Celebrating Loday's Associahedron*, arXiv:2305.08471v1 (first public 2023-05-15), especially Sections 1.1–1.2, https://arxiv.org/html/2305.08471v1.
- A. Padrol, Y. Palu, V. Pilaud, P.-G. Plamondon, *Associahedra for finite-type cluster algebras and minimal relations between g-vectors*, Proc. London Math. Soc. 127 (2023), https://doi.org/10.1112/plms.12543.
- OEIS Foundation, *A000531*, https://oeis.org/A000531, and *A143019*, https://oeis.org/A143019, for the pre-existing numerical sequence in a different context.
