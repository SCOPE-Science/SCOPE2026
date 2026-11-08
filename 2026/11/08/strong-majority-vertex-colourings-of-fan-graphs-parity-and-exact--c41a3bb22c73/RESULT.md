# Strong-majority vertex colourings of fan graphs: parity and exact optimal counts

## Finding

Let \(F_n=K_1\vee P_n\) be the fan graph on a hub and an induced path of \(n\) vertices. For all integers \(n\ge2\), its strong-majority vertex-colouring number is
\[
\operatorname{Maj}(F_n)=\begin{cases}3,&n\text{ even},\\4,&n\text{ odd}.\end{cases}
\]
With three **named** available colours the number of strong-majority colourings for even \(n\) is exactly \(12\) if \(4\mid n\), and \(6\) if \(n\equiv2\pmod4\). All such colourings are classified by a period-four binary path condition. For odd \(n=2m+1\ge3\), the exact number of optimal colourings with four named colours is
\[
4\sum_{0\le a,b,c\le m}[X^aY^bZ^c]B_m(X,Y,Z)B_{m+1}(X,Y,Z),
\]
where \(B_r(X,Y,Z)=\sum_{i_1,\ldots,i_r\in\{1,2,3\},\ i_j\ne i_{j+1}}\prod_{j=1}^r X_{i_j}\) with \(X_1=X,X_2=Y,X_3=Z\); this is a finite explicit path-colouring polynomial. The first odd cases \(n=3,5,7,9\) have respectively \(24,192,912,4128\) optimal named colourings.

## Assumptions and scope

The simple graph \(F_n\) has hub \(h\), path vertices \(v_1,\ldots,v_n\), and edges \(hv_i\) for all \(i\), together with \(v_iv_{i+1}\) for \(1\le i<n\). A strong-majority vertex-colouring assigns colours (properness is not assumed) such that for each vertex \(v\), **each** colour appears on at most \(\lfloor\deg(v)/2\rfloor\) vertices of the *open* neighbourhood \(N(v)\). Its minimum palette size is \(\operatorname{Maj}\). Named palettes distinguish permutations of colours; an optimal colouring uses every colour in the minimum palette. We take \(n\ge2\) so all degrees are at least two. At \(n=1\), \(F_1=K_2\) has no strong-majority colouring because its vertices have degree one.

## Proof

**Hub-colour exclusion.** For \(n\ge3\), each internal path vertex \(v_i\) has degree three and neighbours \(h,v_{i-1},v_{i+1}\). The strong-majority condition forces these three neighbours to have pairwise distinct colours, regardless of palette size. Thus the colours of \(v_{i-1}\) and \(v_{i+1}\) differ and neither equals the hub colour. Each endpoint is a neighbour of an internal vertex, and each interior path vertex is a neighbour of some path vertex of degree at least two; hence no path vertex can have the hub colour. More directly, the endpoints' degree-two constraints force \(c(v_2)\ne c(h)\) and \(c(v_{n-1})\ne c(h)\), while the internal degree-three constraints exclude the hub colour on all the other path vertices. Consequently all path colours avoid \(c(h)\), and
\[
c(v_{i-1})\ne c(v_{i+1})\quad(2\le i\le n-1).
\]
The hub condition is simply that each path colour occurs at most \(\lfloor n/2\rfloor\) times. Conversely, these two requirements, together with avoidance of the hub colour, suffice for all open-neighbourhood constraints: each internal path vertex sees three distinct colours, each endpoint sees two distinct colours, and the hub is controlled by its frequency cap. For \(n=2\) the graph is \(K_3\), requiring three pairwise distinct colours, and the same characterization holds if the distance-two inequalities are vacuous.

**Lower bound.** At least three colours are needed at every internal degree-three path vertex when \(n\ge3\), and at \(n=2\) the triangle needs three. With only three available colours, hub avoidance leaves at most two colours for the \(n\) path vertices. If \(n\) is odd, the hub cannot have both frequencies bounded by \(\lfloor n/2\rfloor\), since twice that bound is \(n-1\). Thus odd fans require at least four colours.

**Even construction and unique form.** For \(n\ge4\) even, let the hub have colour \(0\) and let the path use colours \(1,2\). The distance-two constraint forces \(c(v_{i+2})\) to be the other of \(\{1,2\}\) from \(c(v_i)\), so the path is periodic with period four, completely determined by its first two colours. There are four binary starts \((1,1),(1,2),(2,1),(2,2)\). If \(4\mid n\), every start yields exactly \(n/2\) occurrences of each path colour. If \(n\equiv2\pmod4\), the two equal starts produce frequency imbalance two and violate the hub condition, whereas the two unequal starts are balanced. Multiplying by the three choices for the hub colour gives twelve or six named three-colourings, respectively. For \(n=2\), the three vertices form a triangle and have \(3!=6\) named proper (and strong-majority) three-colourings, consistent with the second formula. Hence \(\operatorname{Maj}(F_n)=3\) for even \(n\).

**Odd construction and exhaustive optimal census.** Let \(n=2m+1\ge3\) and assign the hub a fourth colour \(0\). Colour the path periodically \(1,2,3,1,2,3,\ldots\). Vertices two steps apart have different colours. Each of its three path colours occurs at most \(\lceil n/3\rceil\le m\), since \(n\ge3\) is odd; therefore the hub constraint holds. The lower bound shows \(\operatorname{Maj}(F_n)=4\). In any four-colour solution, hub avoidance reduces path colours to three choices. The distance-two conditions split into independent proper-colouring conditions on the odd-indexed path vertices (a path of \(m+1\) positions) and the even-indexed path vertices (a path of \(m\) positions). Thus their joint colour-multiplicity generating polynomial is exactly \(B_{m+1}B_m\). The hub cap requires every variable's exponent to be at most \(m\); summing the indicated coefficients and multiplying by four hub-colour choices gives the displayed exact optimal-colouring count. Since \(n=2m+1>2m\), no admissible path colouring uses fewer than three colours, so each counted assignment really uses all four named colours. This proves the classification and enumeration for all odd \(n\).

## Verification

Run `python3 artifacts/verify.py` from the root of the embedded package. The verifier independently constructs all open graph neighbourhoods and checks the formula and all named optimum counts for \(2\le n\le9\) by direct enumeration; it computes the coefficient-extraction formula via a separate path dynamic program through \(n=31\), and checks the explicit optimal constructions for all \(2\le n\le100\). These are finite checks supporting, not replacing, the unrestricted proof.

## Relationship to prior work

The vertex invariant was introduced in R. Kalinowski, M. Kamyczura, M. Pilśniak and M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828 (first submitted 22 May 2026). Their results on cycles, complete graphs and general upper bounds do not imply a complete fan classification or its optimal-colouring census. The strong-majority **edge** index (including its line-graph interpretations) is a distinct invariant. The previously studied majority C-colouring (where each vertex sees at least half its own colour) reverses the neighbourhood constraint and is also different. The fan graph is a canonical hub-and-path graph family; its exact period-four constraint is forced by the interaction of degree-three path vertices with the hub's degree-dependent cap. Full historical priority cannot be established solely from a finite search.

## Limitations

The result concerns nonproper strong-majority **vertex** colourings of fans only; it does not classify arbitrary apex joins, wheels or edge colourings. The odd-case enumeration is an explicit finite coefficient formula rather than a single hypergeometric closed form. This is a mathematical proof and reproducible same-source finite check, not independently certified research.

## References

1. R. Kalinowski, M. Kamyczura, M. Pilśniak, and M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828, first version 22 May 2026. https://arxiv.org/abs/2605.23828
2. W. Młotkowski and N. Obata, *Quadratic embedding constants of fan graphs and graph joins*, Linear Algebra and its Applications 709 (2025), 58–91, DOI 10.1016/j.laa.2025.01.001. This treats the same fan graph but a distinct distance-matrix invariant.
