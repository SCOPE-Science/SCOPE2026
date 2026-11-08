# Globally and locally minimal defensive alliances of crown graphs

## Finding

For every integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M\) be the labelled crown graph with shores \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), where \(a_i b_j\) is an edge exactly when \(i\ne j\). A *defensive alliance* is a nonempty set \(S\) such that \(|N[v]\cap S|\ge |N(v)\setminus S|\) for every \(v\in S\). It is **locally minimal** when no single chosen vertex can be deleted while retaining an alliance, and **globally minimal** when no proper nonempty subset is an alliance; the latter must not be confused with a *global* (dominating) defensive alliance.

Put \(t=\lfloor(n-1)/2\rfloor\) and \(s=t+1\). Write \(X=\{i:a_i\in S\}\) and \(Y=\{j:b_j\in S\}\). Then all globally minimal defensive alliances are exactly the following two, disjoint classes:

1. \(|X|=|Y|=t\) and \(X\cap Y=\varnothing\).
2. \(|X|=|Y|=s\) and \(|X\cap Y|\ge3\).

All locally minimal defensive alliances are exactly the same first class together with the second class with the weaker bound \(|X\cap Y|\ge2\). In particular, **every locally but not globally minimal alliance has \(|X|=|Y|=s\) and \(|X\cap Y|=2\)**; such a set contains exactly two proper globally minimal alliances.

Let \(G_n(z)\) and \(L_n(z)\) enumerate globally and locally minimal defensive alliances, respectively, by selected-vertex cardinality. With the standard convention that out-of-range binomial coefficients are zero, define

\[
D_{n,k}=\binom nk\binom{n-k}{s-k}\binom{n-s}{s-k},\qquad C_n=\binom nt\binom{n-t}{t}.
\]

Then, for all \(n\ge3\), the two complete labelled cardinality polynomials are

\[
\boxed{G_n(z)=C_n z^{2t}+\left(\sum_{k=3}^{s}D_{n,k}\right)z^{2s}},\qquad
\boxed{L_n(z)=C_n z^{2t}+\left(\sum_{k=2}^{s}D_{n,k}\right)z^{2s}}.
\]

The exact number of locally minimal alliances that fail global minimality is \(D_{n,2}\). The smallest defensive alliance has cardinality \(2t\). The largest globally minimal alliance has cardinality \(2t\) for \(n=3,4\) and \(2s\) for \(n\ge5\); the largest locally minimal alliance has cardinality \(2s\) for every \(n\ge3\). Thus the two upper parameters agree for all \(n\ge5\) even though the locally and globally minimal families are different at every order. The only globally minimal cardinality at \(n=3,4\) is \(2\); at every \(n\ge5\) the global-minimal cardinalities are exactly \(2t\) and \(2t+2\).

## Assumptions and scope

Graphs are simple, finite and undirected. The deletion matching \(M=\{a_i b_i:1\le i\le n\}\) is fixed for labelled counting. The definition uses the closed-neighborhood allowance of one for the chosen vertex; the *strong* defensive-alliance inequality is a different condition and is not claimed here. Empty vertex sets are not defensive alliances. The theorem applies exactly to integer orders \(n\ge3\); \(\operatorname{Cr}_3\) is a six-cycle.

## Proof

Every vertex of \(\operatorname{Cr}_n\) has degree \(n-1\). The defining inequality is equivalent to \(2|N(v)\cap S|\ge n-2\), so a chosen vertex needs at least \(t=\lceil(n-2)/2\rceil\) selected neighbors. For a selected \(a_i\) that count is \(|Y|-\mathbf 1_{i\in Y}\); for a selected \(b_j\) it is \(|X|-\mathbf 1_{j\in X}\). Since \(t\ge1\), an alliance meets both shores. It follows that **the complete alliance feasibility criterion** is

\[
\bigl(|X|\ge s\ \text{and}\ |Y|\ge s\bigr)
\quad\text{or}\quad
\bigl(|X|\ge t,\ |Y|\ge t,\ X\cap Y=\varnothing\bigr).
\tag{1}
\]

Indeed, the first case supplies at least \(t\) neighbors even at matched selected indices, and in the second case each selected vertex has all members of the opposite selected shore as neighbors. Conversely, if one shore has exactly \(t\) selected vertices, the other shore must avoid its indices; otherwise a selected opposite-shore vertex has only \(t-1\) selected neighbors. If both shore sizes exceed \(t\), the first case applies.

We next derive local minimality directly from (1). If the sizes are unequal and the smaller is \(t\), then the sets are disjoint and one vertex can be deleted from the larger shore while retaining (1). If both sizes are at least \(s\) and one exceeds \(s\), deletion from that shore preserves the first case. Hence a locally minimal alliance has either sizes \((t,t)\) and disjoint shores, or sizes \((s,s)\). The former are locally minimal, since after deleting any vertex one shore has size below \(t\). For the latter, removing an \(a_i\) can leave an alliance only if the remaining \(t\) indices \(X\setminus\{i\}\) are disjoint from \(Y\), and similarly for removing \(b_j\). A permissible deletion exists if and only if \(|X\cap Y|\le1\). This proves the local classification.

A globally minimal alliance must be locally minimal. Every disjoint \((t,t)\) alliance is globally minimal because no alliance has fewer than \(t\) selected vertices on either shore. Consider a locally minimal \((s,s)\) alliance with intersection size \(k\ge2\). A proper defensive-alliance subset would have to satisfy the disjoint alternative in (1): it cannot satisfy the first alternative after any deletion, because both original shore sizes are exactly \(s\). To retain at least \(t=s-1\) vertices per shore, at most one index can be deleted from each shore. Such two deletions can eliminate every shared index precisely when \(k=2\); the two shared indices must be deleted one from the first shore and the other from the second, in either order. Thus \(k=2\) gives exactly two contained globally minimal \((t,t)\) alliances, whereas \(k\ge3\) permits no proper defensive-alliance subset at all. This proves global minimality and its distinction from local minimality.

For the first family, choose \(t\) indices for \(X\) and then \(t\) from the remaining \(n-t\) for \(Y\), producing \(C_n\) labelled alliances. For an \((s,s)\) pair with intersection size \(k\), choose its common \(k\) indices, then \(s-k\) exclusive indices on the first shore, and \(s-k\) exclusive indices on the second shore from the remaining \(n-s\); this gives \(D_{n,k}\). Summing over the respective intersection ranges proves the polynomials and the locally-only count. Since \(s=2\) for \(n=3,4\), there is no second globally minimal family; for \(n\ge5\), \(s\ge3\) and choosing \(X=Y\) of cardinality \(s\) constructs it. The two upper parameters and cardinality spectra follow, as does the minimum \(2t\).

## Verification

The standalone file `verify_crown_alliances.py` checks the original neighborhood inequality directly, without using criterion (1) to decide feasibility. For every labelled graph of the family with \(3\le n\le8\), it enumerates all \(2^{2n}\) vertex subsets; it independently tests one-vertex deletions for local minimality and strict subset containment for global minimality. It compares the resulting families with the two structural criteria and checks the closed coefficient formulas. Execute `python3 verify_crown_alliances.py` in the directory containing this document and the code. Finite verification is corroboration, not the unrestricted proof; all \(n\ge3\) are covered by the argument above.

## Relationship to prior work

Bazgan, Fernau and Tuza distinguish local and global minimality and study upper defensive alliances and computational complexity; their 2018 first-online article does not state the crown-graph labelled classification. Gaikwad and Maity's February 4, 2022 preprint studies complexity and neighborhood-diversity algorithms for globally minimal alliances, not the stated exact intersection structure or polynomial. Feng, Fernau and Mann's December 19, 2023 work studies enumeration and counting of minimal defensive alliances on general and selected graph classes. Its accessible abstract does not provide a crown-graph formula; its complete primary text could not be inspected here, leaving a specific priority risk. A September 23, 2026 preprint by Fernau and collaborators also concerns general minimal-alliance enumeration; the accessible abstract does not establish the present labelled formula, but its full text was likewise unavailable. No claim is made to originate the definitions, generic enumeration methods, or the small six-cycle case.

## Limitations

The formulas cover crown graphs and the ordinary (not strong) defensive-alliance condition only. They do not give a general-purpose algorithm for arbitrary graphs or enumerate alliances without the minimality requirement. Publication priority is provisional because some closely relevant enumeration literature could not be inspected in full. There has been no independent mathematical audit; the finite checker is not a proof for all orders.

## References

1. C. Bazgan, H. Fernau, Z. Tuza, *Aspects of upper defensive alliances*, Discrete Applied Mathematics 266 (2019), 111–120; first online June 30, 2018. DOI: 10.1016/j.dam.2018.05.061.
2. A. Gaikwad, S. Maity, *Globally Minimal Defensive Alliances: A Parameterized Perspective*, arXiv:2202.02010v1, February 4, 2022; later Discrete Applied Mathematics 385 (2026), 86–99.
3. Z. Feng, H. Fernau, K. Mann, *Enumerating Minimal Defensive Alliances*, arXiv:2312.11963v1, December 19, 2023; later Discrete Applied Mathematics 384 (2026), 309–325.
4. H. Fernau, K. Mann, A. Meier, H. Vollmer, *Parameterized Enumeration of Minimal Defensive Alliances*, arXiv:2609.27984, September 23, 2026.
