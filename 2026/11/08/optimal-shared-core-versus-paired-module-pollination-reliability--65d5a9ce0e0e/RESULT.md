# Optimal shared-core versus paired-module pollination reliability at a sharp extinction threshold

## Finding

**Theorem (global optimal three-plant network with fixed plant degree and pollinator richness).** Let integers \(s\ge1\) and \(d\ge 2s\) be given, and put \(m=3d-2s\). Consider any simple bipartite incidence network with three named plant species and exactly \(m\) pollinator species. Every plant must be linked to exactly \(d\) different pollinators, and every pollinator must have at least one plant partner. Each pollinator independently becomes unavailable with the same probability \(q\in(0,1)\). A plant is called *supported* when at least one of its partners remains available, and \(R\) is the probability that **all three plants are supported**.

Two network families, unique up to relabeling within each guild, exhaust the global maximizers of \(R\):

- **Paired-module network \(B\):** two plants share exactly \(2s\) pollinators, have \(d-2s\) additional private pollinators each, and the third plant has \(d\) private pollinators. There are no other links or overlaps.
- **Common-core network \(H\):** all three plants share exactly \(s\) pollinators, and each plant has another \(d-s\) private pollinators. There are no other links or overlaps.

The optimal topology changes at the exact threshold
\[
q_c=2^{-1/s}.
\]
For \(0<q<q_c\), \(B\) is the unique maximizing isomorphism type; for \(q_c<q<1\), \(H\) is the unique maximizing isomorphism type; at \(q=q_c\), exactly these two isomorphism types maximize \(R\). The exact objective gap is
\[
R_B(q)-R_H(q)=q^{2d-2s}(1-q^s)(1-2q^s).
\]
The individual plant-support probabilities, expected number of supported plants, and probability that at least one plant is supported are identical for every admissible network: respectively \(1-q^d\), \(3(1-q^d)\), and \(1-q^m\). Thus the sharp reversal is invisible to these first-order and regional-presence summaries.

In the smallest member \((d,s,m)=(2,1,4)\), the common-core graph has neighborhoods \(\{0,1\},\{0,2\},\{0,3\}\), whereas the paired-module graph has neighborhoods \(\{0,1\},\{0,1\},\{2,3\}\). The crossover is \(q_c=1/2\). At \(q=1/4\), the paired-module and common-core joint reliabilities are \(225/256\) and \(219/256\), respectively; at \(q=3/4\), they are \(49/256\) and \(67/256\), respectively.

## Assumptions and scope

The pollinator set has size exactly \(m\), and all pollinators are used. Each plant neighborhood \(A_1,A_2,A_3\) has cardinality \(d\); neighborhoods may coincide. The bipartite graph need not be connected. Pollinator losses are independent and identically distributed; the plant-support rule is binary and instantaneous, without population dynamics, interaction weights, compensation, or cascading plant-to-pollinator feedback. The theorem applies to every integer pair \((d,s)\) in the stated range and every real \(q\in(0,1)\).

## Proof

**Step 1 (exact reliability).** Let \(A_1,A_2,A_3\) be the plant neighborhoods, with \(|A_i|=d\) and \(|A_1\cup A_2\cup A_3|=m\). The event that plant \(i\) is unsupported is exactly the event that all pollinators in \(A_i\) fail. Inclusion-exclusion therefore gives
\[
R=1-3q^d+\sum_{1\le i<j\le3}q^{2d-|A_i\cap A_j|}-q^m.
\]
Write \(t=|A_1\cap A_2\cap A_3|\), and let \(b_{ij}\) count pollinators occurring in exactly neighborhoods \(A_i\) and \(A_j\). Counting duplicated incidences gives
\[
2t+b_{12}+b_{13}+b_{23}=3d-m=2s.
\]
Thus \(0\le t\le s\), and, with \(r=1/q>1\), maximizing \(R\) is equivalent to maximizing
\[
\sum_{i<j}r^{t+b_{ij}}
\quad\text{subject to}\quad b_{12}+b_{13}+b_{23}=2(s-t).
\]

**Step 2 (pair-overlap concentration).** For nonnegative integers with fixed sum \(B\), the strict convexity of \(r^x\) gives
\[
r^{b_{12}}+r^{b_{13}}+r^{b_{23}}\le r^B+2.
\]
For \(B>0\), equality holds exactly when all of \(B\) occurs in one of the three coordinates. This follows by repeatedly transferring one unit from a smaller positive coordinate to a larger one; each transfer strictly increases the sum. Consequently
\[
\sum_{i<j}r^{t+b_{ij}}\le f(t):=r^{2s-t}+2r^t.
\]

**Step 3 (triple-overlap endpoints).** The real function \(f\) satisfies
\[
f''(t)=(\log r)^2\bigl(r^{2s-t}+2r^t\bigr)>0
\]
throughout \([0,s]\). Hence its maximum on that interval lies only at \(t=0\) or \(t=s\), with every interior value strictly smaller than the larger endpoint. At \(t=0\), equality in Step 2 forces one pair-only overlap of size \(2s\) and no other overlaps, which is precisely \(B\). At \(t=s\), the duplication budget forces \(b_{12}=b_{13}=b_{23}=0\), which is precisely \(H\). Both endpoints are feasible because \(d\ge2s\). The private-part sizes in \(B\) are \(d-2s,d-2s,d\); those in \(H\) are \(d-s,d-s,d-s\). This proves global optimality and all equality conditions.

**Step 4 (exact threshold).** Direct inclusion-exclusion gives
\[
\begin{aligned}
R_H&=1-3q^d+3q^{2d-s}-q^{3d-2s},\\
R_B&=1-3q^d+q^{2d-2s}+2q^{2d}-q^{3d-2s}.
\end{aligned}
\]
Subtracting and factoring yields
\[
R_B-R_H=q^{2d-2s}(1-q^s)(1-2q^s).
\]
For \(q\in(0,1)\), the first two factors are strictly positive, so the sign is determined by \(1-2q^s\). This gives the sharp crossover and, with the preceding strictness, the exhaustive maximizer classification.

**Step 5 (statistics that do not distinguish networks).** Each plant has exactly \(d\) partners, hence support probability \(1-q^d\), and linearity gives expected supported count \(3(1-q^d)\). Because all \(m\) pollinators have at least one plant partner, at least one plant is supported exactly when at least one pollinator survives, of probability \(1-q^m\).

## Verification

The standalone \`verify.py\` independently constructs the endpoint networks, computes reliability both from inclusion-exclusion and by enumeration of all pollinator failure states, and compares the exact gap for five integer parameter pairs and five rational failure probabilities. It also exhaustively evaluates every ordered triple of \(d\)-element pollinator neighborhoods whose union contains all \(m\) pollinators at \((d,s,m)=(2,1,4),(3,1,7),(4,2,8)\), using exact integer numerators at three rational probabilities each. These exhaustive checks cover \(114\), \(5{,}670\), and \(87{,}570\) labeled neighborhood triples, respectively. The checker reports \(87\) passing assertions. The proof, not the finite checks, establishes the universal claim.

Run with \`python3 verify.py\` using Python's standard library. No external data are needed.

## Relationship to prior work

Bascompte and collaborators (2003) document nested architectures in plant–animal mutualistic networks. Memmott, Waser, and Price (2004; first online 6 December 2004) use the binary rule that a plant is lost when every pollinator partner has been removed, and examine empirical extinction sequences. Bane, Pocock, and James (2018) analyze how network structure and model choices affect knockout-extinction robustness across observed networks, predominantly through extinction-order robustness summaries. The current result concerns a different, explicit endpoint: probability that **every** plant retains a partner after independent Bernoulli pollinator loss, globally optimized over all admissible networks at fixed plant degree and pollinator richness. The inspected sources do not give this three-plant extremal phase diagram. General set-system reliability and biased hitting-set literature may contain equivalent transformations; historical priority is not independently certified.

## Limitations

The model allows disconnected networks; its paired-module optimum is disconnected. Requiring a connected network, fixing pollinator-side degree sequences, introducing correlated losses, unequal pollinator vulnerabilities, weighted interaction efficacy, or dynamic coextinction may change the answer. The theorem supplies no field-based ecological management recommendation. The proof is analytical and reproducible, but prior-art completeness and independent mathematical review remain open.

## References

1. Bascompte, J., Jordano, P., Melián, C. J., and Olesen, J. M. (2003). The nested assembly of plant–animal mutualistic networks. *PNAS* 100, 9383–9387. First published online 24 July 2003. https://doi.org/10.1073/pnas.1633576100
2. Memmott, J., Waser, N. M., and Price, M. V. (2004). Tolerance of pollination networks to species extinctions. *Proceedings of the Royal Society B* 271, 2605–2611. First published online 6 December 2004. https://doi.org/10.1098/rspb.2004.2909
3. Bane, M. S., Pocock, M. J. O., and James, R. (2018). Effects of model choice, network structure, and interaction strengths on knockout extinction models of ecological robustness. *Ecology and Evolution* 8, 10794–10804. https://doi.org/10.1002/ece3.4529
4. Fishburn, P. C., Frankl, P., Freed, D., Lagarias, J. C., and Odlyzko, A. M. (1986). Probabilities for intersecting systems and random subsets of finite sets. *SIAM Journal on Algebraic and Discrete Methods* 7, 73–79. https://doi.org/10.1137/0607009
