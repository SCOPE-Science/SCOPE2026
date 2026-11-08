# Sharp one-step opinion-gap inflation for five and six bounded-confidence agents

## Finding
For each integer \(n\ge2\), confidence radius \(\varepsilon>0\), and sorted initial real opinions \(x_1\le\cdots\le x_n\) satisfying \(x_{i+1}-x_i\le\varepsilon\), define the synchronous update
\[
H_{\varepsilon}(x)_i=\frac{1}{|N_i(x)|}\sum_{j\in N_i(x)}x_j,\qquad N_i(x)=\{j:|x_j-x_i|\le\varepsilon\}.
\]
The sharp normalized largest *one-step adjacent gap* is
\[
\Delta_n=\sup_x\frac{1}{\varepsilon}\max_{1\le i<n}\left(H_{\varepsilon}(x)_{i+1}-H_{\varepsilon}(x)_i\right).
\]
Its first five values are
\[
\boxed{(\Delta_2,\Delta_3,\Delta_4,\Delta_5,\Delta_6)=(0,\tfrac12,1,\tfrac54,\tfrac32).}
\]
The general *binary-boundary reduction* is also proved: on the closure of any initial connected-confidence-graph cell, any one-step adjacent-gap linear functional attains its maximum at gaps belonging to \(\{0,\varepsilon\}\), keeping that cell's neighbor pattern fixed. Thus a continuous extremum can be certified by finite exact arithmetic. For five and six agents, initially connected communities can first lose an influence link, and their maximum possible new adjacent gap is respectively \(25\%\) and \(50\%\) above the confidence radius.

## Assumptions and scope
There are exactly \(n\) equally weighted agents on the real opinion line; self-inclusion and all pairwise contacts at distance *at most* \(\varepsilon\) are mandatory. All agents update simultaneously by the ordinary arithmetic mean of the opinions in their inclusive confidence neighborhood. Agents may have coincident opinions. Initial connectivity means exactly that every consecutive sorted gap is at most \(\varepsilon\); no restrictions are placed on nonconsecutive distances. Only the first update is considered. By translation and positive rescaling, set \(x_1=0\), \(\varepsilon=1\), and \(g_i=x_{i+1}-x_i\in[0,1]\). The calculation uses no assumption about later dynamics or limiting clusters.

## Proof
**Binary-boundary lemma.** Fix any symmetric binary inclusion pattern \(P\) for the nonconsecutive agent pairs, while consecutive pairs are included. The closed feasibility polytope \(Q_P\subset[0,1]^{n-1}\) consists of the inequalities
\[
\sum_{k=i}^{j-1}g_k\le1\quad\text{if }\{i,j\}\text{ is included},\qquad
\sum_{k=i}^{j-1}g_k\ge1\quad\text{otherwise}.
\]
All inequality rows are signed interval indicators in the consecutive-gap coordinates, including the coordinate bounds. After changing individual row signs, every row is an interval of ones. This matrix is totally unimodular: for every subset of its columns, assigning alternating signs to the selected columns produces a sum in \(\{-1,0,1\}\) on every interval row; the Ghouila-Houri criterion (applied to the transpose) proves total unimodularity, and reversing row signs preserves it. Since all right sides are integers, every vertex of every nonempty \(Q_P\) is integral. As \(0\le g_i\le1\), every vertex has \(g_i\in\{0,1\}\).

Within a fixed pattern \(P\), the neighborhoods \(N_i\) are constant, so each updated opinion and each adjacent updated gap is a linear form in \(g\) (the common translation cancels). A linear maximum on the compact \(Q_P\) is therefore attained at one of these binary vertices. If a strict confidence cell exists, pick an actual point \(g^*\) in it. Each \(g\in Q_P\) is a limit as \(t\downarrow0\) of \((1-t)g+tg^*\), which respects all included constraints and makes every excluded distance strictly above one. Thus the closure of each nonempty strict cell equals \(Q_P\), even at ties. Including closed patterns that lack strict witnesses may overestimate the supremum, but never underestimates it. Consequently it suffices for an upper bound to enumerate every binary gap vector compatible with every weak cell pattern. This argument is valid for all finite \(n\).

**Exact finite extrema.** For \(n=2,3,4,5,6\), the program `verify.py` iterates all \(2^{(n-1)(n-2)/2}\) nonconsecutive contact patterns and all \(2^{n-1}\) binary gap vectors. It retains precisely the combinations obeying every included-distance inequality \(\le1\) and excluded-distance inequality \(\ge1\). For each retained combination it builds the stipulated inclusive neighbor sets, evaluates all updated means with `fractions.Fraction`, and maximizes the consecutive differences. Its exact outputs are:

| Agents | Nonempty weak patterns | Exact vertex-gap comparisons | Largest gap |
| ---: | ---: | ---: | ---: |
| 2 | 1 | 2 | \(0\) |
| 3 | 2 | 12 | \(1/2\) |
| 4 | 8 | 78 | \(1\) |
| 5 | 55 | 616 | \(5/4\) |
| 6 | 549 | 6150 | \(3/2\) |

This is exhaustive because the binary-boundary lemma reduces the complete continuum to exactly those finitely many vertices, not because an arbitrary grid approximates it. A weak pattern that is not physically realizable can only enlarge the enumerated candidate set; the exhibited sharp instances below ensure equality.

**Attainment.** At radius one, the five-agent opinion vector \((0,1,2,3,3)\) updates to \((1/2,1,9/4,8/3,8/3)\), so the gap between agents two and three is exactly \(5/4\). The six-agent vector \((0,0,1,2,3,3)\) updates to \((1/3,1/3,3/4,9/4,8/3,8/3)\), with gap \(3/2\) between agents three and four. Both initial confidence graphs are connected, proving sharpness for these sizes. The smaller exact extrema are also attained by the enumerated profiles. Multiplication of all opinions by \(\varepsilon\) proves the claims for any radius. Finally, updates preserve sorting: each confidence neighborhood is a contiguous interval of sorted indices, and both endpoints of that interval are nondecreasing with the agent index, so the uniform neighbor-index distribution shifts right in first-order stochastic order, making its mean opinion nondecreasing.

## Verification
Run `python3 verify.py` from the same directory. It performs only integer and exact rational arithmetic, checks all \(6858\) possible closed-cell vertex-gap comparisons across two through six agents, and independently updates all \(1364\) connected profiles on a four-level adjacent-gap grid. It also recomputes the two displayed extremal initial and updated vectors. An optimizer, tolerance, external dataset, or probabilistic sample is not used for the exhaustive bound. The checker proves a finite vertex maximum **in combination with** the preceding total-unimodularity and closure argument; a finite grid by itself would not prove an inequality over all real profiles.

## Relationship to prior work
Li (2021, Lemmas 2–5) derives a neighbor-overlap bound on updated distance, establishes connectivity preservation for at most four agents, and gives the five-agent profile exhibiting a gap \(5/4\). That five-agent witness is therefore **not claimed as new**. The present contribution is the universal binary-cell extremality mechanism and its exact sharp upper bounds at five and six agents; Li's general local bound allows \(4/3\) for the relevant five-agent neighborhood sizes and \(23/15\) for a feasible six-agent neighborhood pattern, so it does not by itself supply the sharp values. Hegarty and Wedin (2014) study equally spaced initial profiles and subsequent time evolution rather than this unrestricted one-step extremal optimization. Hegselmann (2023) analyzes changes in bounded-confidence trajectories as the radius varies, while Bernardo and collaborators (online 2023) survey network evolution and consensus; neither inspected treatment establishes the stated binary reduction or these exact unrestricted two-size extrema.

## Limitations
The bound concerns **one update**, not maximum separation at later times, eventual consensus probability, or a limit as the agent number grows. The binary extremizers for closed graph cells may require taking limits from a prescribed contact pattern; interpreting ties using a different contact rule can change the one-step average. No closed formula is asserted for \(n>6\). Originality is subject to the possibility of an unindexed equivalent or a result contained in literature not inspected in full. The verifier uses a finite exact certificate supported by a structural theorem, not an independent external verification.

## References
- H.-L. Li, *Probability of Consensus of Hegselmann–Krause Dynamics*, arXiv:2103.02756, first posted 2021-03-03, https://arxiv.org/abs/2103.02756.
- R. Hegselmann, *Bounded Confidence Revisited: What We Overlooked, Underestimated, and Got Wrong*, Journal of Artificial Societies and Social Simulation 26(4), 2023, published 2023-10-31, https://jasss.soc.surrey.ac.uk/26/4/11.html.
- P. Hegarty and E. Wedin, *The Hegselmann–Krause dynamics for equally spaced agents*, arXiv:1406.0819, first posted 2014-06-02, https://arxiv.org/abs/1406.0819.
- C. Bernardo, C. Altafini, A. Proskurnikov and F. Vasca, *Bounded confidence opinion dynamics: A survey*, Automatica 159 (2024), 111302, available online 2023-10-03, https://doi.org/10.1016/j.automatica.2023.111302.
