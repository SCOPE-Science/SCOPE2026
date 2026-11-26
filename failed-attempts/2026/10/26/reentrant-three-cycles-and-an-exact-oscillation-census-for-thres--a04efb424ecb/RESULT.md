# Reentrant three-cycles and an exact oscillation census for threshold-two cyclic competition

## Finding

Let \(K_{a,b}\) be a labelled loopless complete bipartite graph with \(a,b\ge1\). Give each vertex one of the colors \(0,1,2\). At each synchronous step, a vertex of color \(i\) changes to \(i+1\pmod3\) if **at least two** of its neighbours have color \(i+1\pmod3\); otherwise it remains at \(i\). Write \(F\) for this map.

For positive integers \(n\), define
\[
B_n=\sum_{u,v,w\ge2\atop u+v+w=n}\frac{n!}{u!v!w!},\qquad
C_n=\begin{cases}2^n-2n-2,&n\ge4,\\0,&n\le3,\end{cases}\qquad
I_n=\begin{cases}n!\binom3n,&1\le n\le3,\\0,&n\ge4.\end{cases}
\]
The number of labelled configurations of **primitive period three** is exactly
\[
R_3(a,b)=B_aB_b+B_aI_b+I_aB_b,
\]
and the number of configurations of **primitive period four** is
\[
R_4(a,b)=6C_aC_b.
\]
There are no primitive periods other than one, three and four. Every configuration enters its eventual periodic orbit within **three updates**, independently of \(a,b\), and
\[
F^{15}=F^3.
\]
The entry-time bound three is attained on \(K_{2,4}\). Hence the primitive-period-three existence condition is precisely: both shores have at least six vertices, **or** one shore has at least six and the other has size one, two or three. In particular, for every fixed \(b\ge6\), three-cycles occur when \(a\in\{1,2,3\}\) and when \(a\ge6\), but disappear completely for \(a\in\{4,5\}\). Primitive four-cycles exist exactly when \(a,b\ge4\).

The fixed configurations have an exact finite formula as well. For triples of nonnegative integers \(\mathbf u=(u_0,u_1,u_2)\) and \(\mathbf v=(v_0,v_1,v_2)\) summing to \(a\) and \(b\), respectively, let \(\mathcal F_{a,b}\) consist of those pairs satisfying, for every \(i\in\{0,1,2\}\) with subscripts modulo three,
\[
(u_i=0\ \text{or}\ v_{i+1}\le1)
\quad\text{and}\quad
(v_i=0\ \text{or}\ u_{i+1}\le1).
\]
Then
\[
R_1(a,b)=\sum_{(\mathbf u,\mathbf v)\in\mathcal F_{a,b}}
\binom a{u_0,u_1,u_2}\binom b{v_0,v_1,v_2}.
\]
Thus all recurrent configurations number \(R_1+R_3+R_4\), and the number of distinct orbits of periods three and four is \(R_3/3\) and \(R_4/4\), respectively.

As \(\min(a,b)\to\infty\), the proportion of recurrent configurations lying on primitive three-cycles tends to one.

## Assumptions and scope

The graph is simple and labelled, both shores are nonempty, and the update is simultaneous. Only neighbours in the opposite shore count; the vertex itself is not a neighbour. The contact threshold is exactly two and there are exactly three cyclic colors. All formulas concern configurations (not color-isomorphism classes); group labels and shore labels are distinguished. The source date given in metadata refers to the initial public posting of the selected historical dynamical reference, not a claim that the entire subject began then.

## Proof

**Finite exact quotient.** Let \(A_i\) and \(D_i\) be the counts of color \(i\) on the two shores. Set \(\sigma(n)=\min\{n,2\}\), and let \(s_i=\sigma(A_i)\), \(t_i=\sigma(D_i)\). For each shore, every vertex currently in a given color class makes exactly the same decision. Thus, if \(m_i=\mathbf1_{\{t_{i+1}=2\}}\), the next capped count on the first shore is
\[
s'_j=\sigma\left(\sum_{i=0}^2s_i\mathbf1_{\{j\equiv i+m_i\pmod3\}}\right),
\]
with the analogous rule interchanging the shores. This identity holds even if a capped count two represents an arbitrarily large actual class: no class splits, and saturation commutes with the addition of whole classes.

There are \(3^3-1=26\) possible nonempty capped triples per shore, hence exactly \(676\) ordered support pairs to check. To follow an *individual labelled vertex*, adjoin its shore and current color. The resulting tagged transition map has exactly \(2808\) realizable tagged states: a tag is included only if the corresponding capped color class is nonempty. Its transition uses the opposite shore's successor-color threshold indicator. This is a genuine closed finite quotient for every vertex of every configuration, independently of the actual multiplicities at least two.

**Exhaustive finite lemma.** Applying the finite transition rule to all \(2808\) tagged states gives eventual entry time at most three and tagged cycle length belonging to \(\{1,3,4\}\). Moreover, for each of the \(676\) support pairs, the least common multiple of the eventual tagged periods of *all occupied initial colors* is in \(\{1,3,4\}\), never twelve. The accompanying `verify.py` constructs every state from the displayed rule, follows every orbit until its first repetition, and asserts these two statements. This exhaustive finite computation is the complete proof of this finite lemma, not an extrapolation from sample sizes. It follows that every labelled configuration has entry time at most three and primitive period one, three or four, and therefore \(F^{15}=F^3\).

**Exact periodic-point extraction.** For a given pair of capped triples \((s,t)\), let \(\mathcal P_k\) be the set for which every originally occupied color class, on either shore, returns to its original color after \(k\) tagged updates. Because the capped transition determines every tagged color path, \(\mathcal P_k\) exactly characterizes configurations fixed by \(F^k\). Put \(E(z)=e^z-1-z\), and assign a capped triple \(s\) the exponential generating weight \(\prod_i W_{s_i}(x)\), where \(W_0(x)=1\), \(W_1(x)=x\), \(W_2(x)=E(x)\); use variable \(y\) for the other shore.

An exhaustive comparison of all \(676\) support pairs yields the following **exact polynomial identities** for the differences of their weighted indicator sums:
\[
\sum_{(s,t)\in\mathcal P_3\setminus\mathcal P_1}W_s(x)W_t(y)
=E(x)^3E(y)^3+E(x)^3\big((1+y)^3-1\big)+E(y)^3\big((1+x)^3-1\big),
\]
\[
\sum_{(s,t)\in\mathcal P_4\setminus\mathcal P_1}W_s(x)W_t(y)
=6E(x)^2E(y)^2.
\]
Here \(W_s(x)=\prod_i W_{s_i}(x)\). The script prints the seven monomials of the first identity and the single monomial of the second and checks both coefficient by coefficient. Their coefficient extraction \(a!b![x^ay^b]\) gives the displayed formulas: \(B_n=n![z^n]E(z)^3\), \(C_n=n![z^n]E(z)^2\), and \(I_n=n![z^n]((1+z)^3-1)\). Because the only possible periodic lengths are one, three and four, the two differences count precisely the indicated *primitive* periods. The fixed-point condition in the Finding is immediate from the literal update rule.

**Sharp boundary and limiting density.** The explicit configuration on \(K_{2,4}\) with first-shore color counts \((0,1,1)\) and second-shore counts \((2,0,2)\) first enters its fixed point after precisely three steps. A period-three witness has shore counts \((0,0,1)\) and \((2,2,2)\), and a period-four witness has counts \((0,2,2)\) and \((2,0,2)\). These are verified by the original vertex-level update, not only by the capped quotient. Positivity of \(B_n\), \(C_n\) and \(I_n\) establishes all existence cutoffs. Finally, \(B_n/3^n\to1\) by a union bound on color classes of sizes at most one. For \(a,b\ge6\), \(R_3=B_aB_b\), whereas \(R_4\le6\cdot2^{a+b}\) and \(R_1\le3^{a+b}-B_aB_b\): a configuration with every color represented at least twice on both shores cannot be fixed. Division by \(R_1+R_3+R_4\) proves the stated asymptotic proportion.

## Verification

The self-contained standard-library script `verify.py` exhausts all \(676\) capped pairs, all \(2808\) admissible tagged states, and the return conditions for periods one, two, three, four, six and twelve. The two polynomial identities are compared as exact integer-coefficient dictionaries. Independent direct vertex-level enumeration checks all initial configurations on \(K_{1,6}\), \(K_{2,4}\), \(K_{2,6}\), \(K_{3,6}\), \(K_{4,4}\), and \(K_{4,6}\), a total of \(94{,}770\) labelled initial states, as well as the three witnesses. The recorded `verification_output.txt` ends with `VERIFY_OK`. Run `python3 verify.py` in a directory containing this file and the verifier. The all-size proof uses the exhaustive, finite capped-and-tagged quotient; the vertex-level enumeration is an independent cross-check only.

## Relationship to prior work

Durrett and Griffeath (1993) investigate threshold-dependent cyclic excitable automata on integer lattices; Fisch, Gravner and Griffeath (1991) explicitly formulate successor-color threshold contact rules and examine lattice wave and fixation phenomena. Those results establish the physical and mathematical motivation, but the inspected material does not give the labelled complete-bipartite state census or the nonmonotone shore-size threshold. Bello and Sivakoff (2021) study threshold at least two on infinite regular trees and address stochastic fixation/fluctuation, not exact finite-graph recurrence. The earlier complete-bipartite count for **threshold one** has a different update rule: the presence of a single successor neighbor already causes advancement. In particular, its period-three count is a product of counts of colorings using all three colors, unlike the threshold-two formula with the sparse-shore terms and sizes four/five exclusion. A rewording, specialization or formal substitution of that earlier threshold-one theorem does not prove this theorem. Searches and access limitations are detailed in `AUDIT.json`.

## Limitations

The classification is specific to exactly three colors, contact threshold two and complete bipartite graphs. It does not establish a general theorem on arbitrary graphs, thresholds or numbers of colors. The novelty comparison was performed against accessible primary literature and an indexed research database, but cannot exclude unindexed equivalent work. Computed checks of a finite quotient are exhaustive because its state-space reduction is proved above; the direct enumeration of finitely many graph sizes would not by itself prove the infinite-family statement. No independent scientific audit has been conducted.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, initial public arXiv submission 1993-03-22, arXiv:patt-sol/9303002, https://arxiv.org/abs/patt-sol/9303002.
2. R. Fisch, J. Gravner and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing 1 (1991), 23–39, https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf.
3. J. Bello and D. Sivakoff, *Cyclic Cellular Automata and Greenberg–Hastings Models on Regular Trees*, arXiv:2108.06404, 2021, https://arxiv.org/abs/2108.06404.
4. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, 2016, https://arxiv.org/abs/1610.07320 (threshold-one comparison only).
