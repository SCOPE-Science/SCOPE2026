# A sharp local response law for three-distance cycle type spectra

## Finding

Let \(\mathbb U_3\) be the countable universal homogeneous metric space whose positive distances are \(1,2,3\). For each integer \(n\ge 7\), define a pointwise named parameter metric \(A_n\) on \(\mathbb Z/n\mathbb Z\) by
\[
d_n(i,j)=\min\bigl\{\operatorname{dist}_{C_n}(i,j),3\bigr\}.
\]
Write \(\Theta_n(x,y,z)\) for the polynomial enumerating complete nonalgebraic one-point types over \(A_n\), assigning monomial \(x^{a}y^{b}z^{c}\) to a type in which the new point is at distances \(1,2,3\) from exactly \(a,b,c\) named points, respectively. Then for all \(n\ge7\),
\[
\boxed{\begin{aligned}
\Theta_n(x,y,z)={}&(y+z)^n+nxy^2(y+z)^{n-3}\\
&+nx^2y^2(y+z)^{n-4}
+nx^2y^3(y+z)^{n-5}
+nx^3y^2(y+z)^{n-5}.
\end{aligned}}
\]
In particular the exact total number of such types is
\[
\boxed{\Theta_n(1,1,1)=(n+4)2^{n-2}.}
\]

A single long-distance relaxation has a sharp local response. Replace just \(d_n(0,3)=d_n(3,0)=3\) by \(2\), leaving all other distances unchanged, and call the new metric \(A'_n\). The replacement is metric for every \(n\ge7\). Its nonalgebraic one-point type polynomial satisfies
\[
\boxed{\Theta'_n-\Theta_n=
 x^2y^2(x+y)^2(y+z)^{n-6}+\mathbf1_{\{n=7\}}x^3y^4.}
\]
Thus the gain is exactly \(2^{n-4}\) types for every \(n\ge8\), with a single extra type at the sharp seven-vertex boundary: the gain at \(n=7\) is \(9\), not \(8\). The factorization describes every new type, not just their total number.

## Assumptions and scope

All new-point distances are strictly positive and lie in \(\{1,2,3\}\); the named points remain distinct. All types are complete nonalgebraic singleton types over a pointwise named finite metric base in \(\mathbb U_3\). The variable \(x\) records the number of distance-one coordinates, \(y\) distance-two coordinates, and \(z\) distance-three coordinates. The polynomial identities are in \(\mathbb Z[x,y,z]\), for integer \(n\ge7\); the stabilized single-pair factorization has its exceptional term only at \(n=7\).

More generally, for a finite connected simple graph \(G=(V,E)\), give \(V\) the metric \(\min\{\operatorname{dist}_G,3\}\). Let \(G^2\) join pairs at graph distance at most two; let \(N_G(S)\) denote the open graph neighborhood of \(S\), with vertices of \(S\) excluded. Then
\[
\tag{1}
\Theta_G(x,y,z)=\sum_{S:\,S\text{ a clique in }G^2}
 x^{|S|} y^{|N_G(S)|}(y+z)^{|V|-|S|-|N_G(S)|},
\]
including the empty clique. This representation underlies both cycle identities. It is not asserted that this formula classifies arbitrary metric bases: it applies to the particular truncated graph-metric subclass.

## Proof

**Step 1: complete types and local conditions.** A nonalgebraic one-point type over a finite metric base \(A\) corresponds bijectively to a function \(f:A\to\{1,2,3\}\) satisfying the Katětov inequalities \(\lvert f(a)-f(b)\rvert\le d(a,b)\le f(a)+f(b)\) for all old pairs. The age of \(\mathbb U_3\) contains every such finite metric extension, so each valid vector is realized; homogeneity makes the vector a complete type. Every vector admits infinitely many distinct realizations (indeed the type-orbit is infinite). For an old distance of \(1\), the only prohibited pair is \((1,3)\) or its reversal. Old distance \(2\) places no restriction. Old distance \(3\) prohibits exactly \((1,1)\).

**Step 2: a clique-neighborhood identity.** For a truncated graph metric, fix \(S=f^{-1}(1)\). No two points of \(S\) may lie at graph distance at least three, so \(S\) is a clique of \(G^2\). Every neighbor of \(S\) outside \(S\) must receive value \(2\), because a distance-one old pair cannot receive \((1,3)\). Every remaining vertex may independently receive \(2\) or \(3\): these states produce no other forbidden pairs. Conversely, every such assignment meets all Katětov inequalities. Weighting and summing over \(S\) proves (1).

**Step 3: cycle clique classification.** For \(n\ge7\), the cliques of \(C_n^2\) are exactly: one empty clique; \(n\) singletons; \(n\) adjacent pairs; \(n\) pairs of cyclic distance two; and \(n\) triples of consecutive vertices. There is no larger clique. To see this, rotate a nonempty clique to include \(0\). Its remaining vertices lie in \(\{-2,-1,1,2\}\) modulo \(n\). Compatible pairs among these four give either a consecutive triple with \(0\), or a two-point set; for \(n=7\), inspection of cyclic differences gives the same list. Their external neighborhoods have respective sizes \(0,2,2,3,2\). Insert these sizes into (1) to obtain the stated multivariate formula and its scalar specialization. The formula is also an immediate proof that at most three named points may be at new distance one when \(n\ge7\).

**Step 4: shortening one distance.** Replacing \(d_n(0,3)=3\) by \(2\) leaves a metric. In triangles not involving both \(0,3\), nothing changes. In a triangle involving both, the original sum on the other two sides is at least \(3\), hence at least \(2\); and \(\lvert d_n(0,t)-d_n(3,t)\rvert\le2\) for every third vertex \(t\), as is immediate from the capped cycle distance. Thus the triangle inequalities persist.

The only admissibility constraint removed is the prohibition against assigning \(1\) simultaneously to positions \(0\) and \(3\). For \(n\ge8\), a new type must have \(\{0,3\}\subseteq S\). Any further member of \(S\) must be within cyclic distance two of both, so belongs to \(\{1,2\}\). All four choices \(S=\{0,3\}\cup J\), \(J\subseteq\{1,2\}\), are permitted. For \(J\) of size \(j\), the external neighborhood of \(S\) has \(4-j\) vertices and there remain \(n-6\) free \(\{2,3\}\)-vertices. The four weighted contributions sum to
\[
\sum_{j=0}^{2}\binom2j x^{2+j}y^{4-j}(y+z)^{n-6}
=x^2y^2(x+y)^2(y+z)^{n-6}.
\]
For \(n=7\), the common cyclic distance-two neighborhood of \(0,3\) also contains \(5\). It cannot coexist in \(S\) with \(1\) or \(2\). Hence the sole extra new pattern is \(S=\{0,3,5\}\), with all four other old points forced to distance two, contributing \(x^3y^4\). This proves the exact defect formula, the sharp boundary, and the scalar gains.

## Verification

The standalone Python program `artifacts/verify.py` uses only the standard library. It directly tests every distance vector in \(\{1,2,3\}^{n}\) for each cycle size \(4\le n\le11\), independently evaluates the clique-neighborhood formula, and checks the full trivariate coefficient dictionary. For every \(7\le n\le11\), it independently checks that the shortened array is a metric and directly computes the full polynomial difference against the asserted local-response identity. It also enumerates all connected **labeled** graphs of orders at most five (\(772\) graphs) and compares the general clique formula with direct Katětov-vector enumeration. This is a finite reproducibility check, not an all-order proof: the all-order argument is Steps 1–4.

Invoke `python3 artifacts/verify.py` from the directory containing this document. Expected final output: `VERIFY_OK`. The exact recorded checks appear in `artifacts/verification_output.txt`.

## Relationship to prior work

The complete Katětov inequality and universal homogeneous metric extension theory are established by Sauer's public 2010 and 2011 preprints. The first supplies the local three-distance extension rule; neither inspected statement enumerates the three-distance truncated cycle family or the effect of a single distance decrement. A related published study, *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space*, establishes a different full trivariate polynomial on parameter metrics assigning only distances \(1\) and \(2\). That paper's graph-metric slice has no distance-three constraint, while the present theorem exploits that constraint to localize distance-one positions and to measure a single distance-three-to-two perturbation. Thus its graph-homomorphism representation and bounds do not cover either the cycle formula or the pair-defect factorization, though the general Katětov criterion is shared and credited.

Relevant source and claim-level searches included the published-finding corpus (truncated-cycle type spectra; Katětov distance decrements; square-graph clique profiles) and general literature on finite-distance Urysohn spaces, Katětov functions and metric extensions. No explicit covering claim was identified. The possibility of equivalent unindexed enumerations remains a historical-priority risk; neither a failed search nor these comparisons proves global novelty.

## Limitations

The theorem is for cyclic graph shortest-path distances capped at three, with one specified pair lowered from three to two. It does not classify general three-distance metric bases, arbitrary families of modified distances, other distance alphabets, or higher-arity types. Only finitely many instances were checked computationally; the all-order conclusions rest on the written combinatorial proof. Historical originality is based on the accessible literature and searches, not independently certified.

## References

1. N. W. Sauer, *Vertex partitions of metric spaces with finite distance sets*, arXiv:1010.4212 (first posted 2010-10-20), especially Section 2, the Katětov inequalities and extension theorem. https://arxiv.org/abs/1010.4212
2. N. W. Sauer, *Distance sets of universal and Urysohn metric spaces*, arXiv:1107.4794 (first posted 2011-07-24), especially Section 2 and Theorem 1. https://arxiv.org/abs/1107.4794
3. *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space*, published scientific result (2026), RESULT.md. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-widom-rowlinson-partition-functions-as-1-type-polynomials-of-the--ec80747a5989
