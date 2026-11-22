# Macroscopic jumps in the optimal donor position of an interrupted flower sequence

## Finding
Consider an inflorescence with \(n\ge 2\) sequentially visited flowers. Exactly one flower at position \(j\) is assigned pollen-donor function; all others have receptive female function. An arriving pollinator carries an initially unit-sized foreign-pollen load. It continues from one flower to the next with probability \(q\), and each receptive flower removes a fraction \(1-r\) of the pollen currently carried, where \(0<q,r<1\). If the donor flower is reached, the imported load is replaced by one unit of donor pollen; subsequent female flowers remove the same fraction \(1-r\). The objective is the expected amount of foreign pollen deposited on this inflorescence, multiplied by a fixed weight \(w>0\), plus the expected donor pollen remaining when the visitor leaves.

The objective at donor position \(j\) is exactly
\[
F_{n,j}(q)=\frac{w(1-r)+(1-q)q^{j-1}-w(1-r)(qr)^{j-1}+(1-r)q^n r^{n-j}}{1-qr}.
\]
Its adjacent difference has the explicit sign factor
\[
F_{n,j+1}-F_{n,j}=\frac{q^{j-1}}{1-qr}G_{n,q}(j),\qquad
G_{n,q}(j)=w(1-r)(1-qr)r^{j-1}-(1-q)^2+q^2(1-r)^2(qr)^{n-j-1}.
\]
For every \(n\), the real-variable function \(G_{n,q}(x)\) is strictly convex. In particular, if \(G_{n,q}(J)<0\) at an integer \(1\le J<n\), then **every globally optimal donor position belongs to** \(\{1,\ldots,J\}\cup\{n\}\).

**Macroscopic-jump theorem.** Fix any \(0<r<1\) and \(w>0\). Define \(K=4/|\log r|\), \(J_n=\lceil K\log n\rceil\), \(q_{-,n}=1-2\log n/n\), and \(q_{+,n}=1-(\log n)/(2n)\). For all sufficiently large integers \(n\) there exists
\[
q_n\in(q_{-,n},q_{+,n})
\]
such that the terminal position \(n\) ties for the global maximum with at least one position \(j_n\le J_n\), while every intermediate position \(J_n<j<n\) is strictly suboptimal. Consequently the two simultaneous optimal positions are separated by at least \(n-O(\log n)\) flowers and \(1-q_n=\Theta(\log n/n)\). The claim is **existence of at least one crossover**, not uniqueness of the crossover for all parameters.

A finite exact-arithmetic witness needs only ten flowers: at \(n=10\), \(r=1/2\), and \(w=1\), there is a value \(q_*\in(0.791094,0.791095)\) where positions \(4\) and \(10\) are both globally optimal and every other position is strictly inferior. Numerically, \(q_*\approx0.791094121152316\) and the tied objective is \(0.9483520055\).

## Assumptions and scope
The pollinator starts at position \(1\), visits positions in increasing order without skips or returns, and stops after each flower before \(n\) independently with probability \(1-q\); departure after the last flower is mandatory. Let \(L\) denote the number of visited flowers, with \(\Pr(L=\ell)=(1-q)q^{\ell-1}\) for \(1\le\ell<n\) and \(\Pr(L=n)=q^{n-1}\). All female flowers remove a fixed fraction \(1-r\) of whichever pollen load is carried. Replacement of incoming pollen at the one donor flower is assumed complete. Only deposited **foreign** pollen counts for the female part of the objective. Only unspent **local donor** pollen on departure counts for the male part. Each quantity is in units of its respective initial pollen load, and the weight \(w\) expresses their chosen relative value. Pollen cannot be replenished elsewhere on the same flower sequence. The analysis is a theoretical finite-sequence benchmark; it does not model selfing, pollen competition, variation between flowers, plant reproductive ESS, or habitat-dependent pollinator behavior.

## Proof
**1. Formula from the random path.** A female flower at \(i<j\) receives \((1-r)r^{i-1}\) units of imported pollen if it is visited, which occurs with probability \(q^{i-1}\). Consequently the expected imported-pollen receipt is
\[
C_{n,j}=(1-r)\sum_{i=1}^{j-1}(qr)^{i-1}
=\frac{(1-r)(1-(qr)^{j-1})}{1-qr}.
\]
If the pollinator leaves at length \(\ell\) after reaching the donor, it carries \(r^{\ell-j}\) units of local pollen. Summing over possible departure lengths gives
\[
E_{n,j}=(1-q)\,q^{j-1}\sum_{h=0}^{n-j-1}(qr)^h+q^{n-1}r^{n-j}
=\frac{(1-q)q^{j-1}+(1-r)q^nr^{n-j}}{1-qr}.
\]
Empty sums are zero, so the expressions also cover \(j=1\) and \(j=n\). The claim follows from \(F_{n,j}=wC_{n,j}+E_{n,j}\). Subtracting the two neighboring closed forms produces the displayed difference formula, including the factor \(G_{n,q}(j)\).

**2. Shape and candidate reduction.** For real \(x\), the two nonconstant terms of \(G_{n,q}(x)\) are positive multiples of \(e^{(x-1)\log r}\) and \(e^{(n-x-1)\log(qr)}\). Both have strictly positive second derivatives, hence \(G_{n,q}\) is strictly convex. If \(G_{n,q}(J)<0\), its signs at the integer points after \(J\) can only pass from negative to positive, never from positive back to negative. Thus the finite sequence of objective values past position \(J\) first weakly decreases and then weakly increases, with no local maximum in its interior; moreover \(F_{n,J+1}<F_{n,J}\). The largest score after \(J\), if any, is therefore attained at \(n\), establishing the candidate reduction. In particular, intermediate scores at a tie of \(n\) and the early maximum are strictly below their maximum (strict negativity at \(J\), and strict convexity excluding a constant stretch).

**3. A uniform gap in the relevant visitation window.** For fixed \(r,w\), let \(J=J_n\) and take any \(q\in[q_{-,n},q_{+,n}]\). For large \(n\), \(J<n\), \(q\in(0,1)\), and \(1-q\ge (\log n)/(2n)\). Since \(r^{J-1}\le r^{-1}n^{-4}\) and \((qr)^{n-J-1}\le r^{n-J-1}\), uniformly in the window
\[
G_{n,q}(J)\le w(1-r)r^{-1}n^{-4}+(1-r)^2r^{n-J-1}-\frac{(\log n)^2}{4n^2}<0
\]
for all sufficiently large \(n\). Thus every candidate global maximizer throughout the entire window is either at most \(J\) or exactly \(n\).

**4. An early winner at the lower endpoint.** Write \(B(q)=w(1-r)/(1-qr)\). At \(q=q_{-,n}\), the definition of \(F\) implies
\[
F_{n,J}-B(q)=\frac{(1-q)q^{J-1}-w(1-r)(qr)^{J-1}+(1-r)q^nr^{n-J}}{1-qr}.
\]
Here \(q^{J-1}\to1\), \((qr)^{J-1}=O(n^{-4})\), and \(1-q=2\log n/n\). The right-hand side is therefore positive and of order \((\log n)/n\). But \(F_{n,n}-B(q)=q^{n-1}-w(1-r)(qr)^{n-1}/(1-qr)\le q^{n-1}=O(n^{-2})\), using \((1-2\log n/n)^{n-1}\le e^{-2(n-1)\log n/n}\). Hence \(F_{n,J}>F_{n,n}\) at the lower endpoint for large \(n\).

**5. The terminal winner at the upper endpoint.** At \(q=q_{+,n}\), \(q^{n-1}=n^{-1/2}(1+o(1))\) and \(1-q=(\log n)/(2n)\). For all \(j<n\), the closed expression gives the uniform bound
\[
F_{n,j}-B(q)\le\frac{(1-q)+(1-r)q^nr}{1-qr},
\]
whereas
\[
F_{n,n}-B(q)=q^{n-1}-\frac{w(1-r)(qr)^{n-1}}{1-qr}.
\]
Subtracting the first from the second and factoring the leading term gives a lower bound
\[
q^{n-1}\left(1-\frac{q r(1-r)}{1-qr}\right)
-\frac{1-q}{1-qr}-\frac{w(1-r)(qr)^{n-1}}{1-qr}.
\]
The parenthesis tends to \(1-r>0\). The positive leading term is of order \(n^{-1/2}\), which dominates the terms of order \((\log n)/n\) and exponential order \(r^{n-1}\). Therefore \(F_{n,n}>F_{n,j}\) for **every** \(j<n\) at the upper endpoint for all sufficiently large \(n\).

**6. Continuity forces a nonlocal tie.** Define the continuous function
\[
H_n(q)=F_{n,n}(q)-\max_{1\le j\le J_n}F_{n,j}(q)
\]
on the closed visitation window. Parts 4 and 5 show \(H_n(q_{-,n})<0<H_n(q_{+,n})\). The intermediate value theorem supplies an interior zero \(q_n\). Part 3 restricts global maximizers to the early block or position \(n\), so at this zero at least one early position ties with \(n\), and every intervening position is inferior. Since \(J_n=O(\log n)\), the separation is at least \(n-O(\log n)\). The definition of the window gives the stated \(\Theta\)-order for \(1-q_n\). No assertion that the crossing is unique is needed.

**7. Exact ten-flower witness.** Set \(n=10,r=1/2,w=1\) and evaluate the closed rational expressions at \(q_-=791094/10^6\) and \(q_+=791095/10^6\). Exact rational arithmetic verifies \(F_{10,10}(q_-)<F_{10,4}(q_-)\), the reverse inequality at \(q_+\), and that \(F_{10,4}(q_-)-F_{10,j}(q_-)>400\cdot10^{-6}\) for every \(j\notin\{4,10\}\). Each derivative \(|F'_{10,j}|\) is bounded by \(155\) on \([0,1]\), by differentiating the finite visitation probability expansion and bounding each term by its positive coefficient. Thus each difference \(F_{10,4}-F_{10,j}\) changes by less than \(310\cdot10^{-6}<400\cdot10^{-6}\) on that interval. By continuity some root of \(F_{10,10}-F_{10,4}\) in the bracket therefore has \(4\) and \(10\) as the only maximizing positions.

## Verification
A standard-library Python program in `verify.py` enumerates all possible pollinator visit lengths with exact rational arithmetic, checks the closed forms and adjacent differences against direct enumeration for \(2\le n\le13\) on explicit grids of \(q,r,w\), and checks the strict rational inequalities needed for the ten-flower witness. It also performs supplementary numerical sanity tests in longer sequences. Replaying the program produced **17,658 successful assertions**. This finite computation is not a proof of the infinite macroscopic-jump theorem; parts 3–6 provide the uniform analytic proof.

## Relationship to prior work
Floral sexual segregation, ascending visitors, and pollen discounting are established biological phenomena. Kudo, Maeda and Narita (2001) measured position-dependent floral sex allocation and reproductive success in *Corydalis ambigua*. Jersáková and Johnson (2007) studied pollen export and geitonogamy in protandrous orchids with generally upward-moving pollinators. Harder, Jordan, Gross and Routley (2004) reviewed the pollination function of inflorescences and explained why terminal male flowers can reduce pollen discounting, while the present weighted objective makes terminal placement suboptimal in some persistence regimes. Devaux, Lepers and Porcher (2014) reviewed how visitor behavior constrains plant mating systems. These works provide biological context but do not, in the portions examined, establish the present exact objective, the strict-convexity candidate reduction, or the \(n-O(\log n)\) donor-position tie theorem. Brunet and Charlesworth (1995) treated sexual allocation across sequentially flowering plants; its accessible abstract is closely relevant, but the full paper could not be examined, leaving a priority risk. The finding is not a claim to have discovered protandry, pollen carryover, or positional sex allocation.

## Limitations
The reproductive objective is a deliberately weighted linear proxy, not a mechanistic seed-set or paternity model. Total load replacement at the donor is idealized; the pollinator's continuation probability does not react to nectar, age, sex or position. The main theorem is asymptotic; it supplies no universal finite threshold on \(n\) and does not assert a unique critical \(q\) or rule out other distant ties. Finite arithmetic checks do not establish the asymptotic theorem. Historical novelty is provisional pending comparison with inaccessible older full text and with broader sequential-allocation theory. No direct field-design or species-level fitness conclusions follow.

## References
- Brunet, J. and Charlesworth, D. (1995). Floral sex allocation in sequentially blooming plants. *Evolution* 49:70–79. https://doi.org/10.1111/j.1558-5646.1995.tb05959.x (abstract inspected; full text unavailable).
- Kudo, G., Maeda, T. and Narita, K. (2001). Variation in floral sex allocation and reproductive success within inflorescences of *Corydalis ambigua*. *Journal of Ecology*. https://doi.org/10.1046/j.1365-2745.2001.00512.x (full accessible HTML inspected).
- Jersáková, J. and Johnson, S. D. (2007). Protandry promotes male pollination success in a moth-pollinated orchid. *Functional Ecology* 21:496–504. https://doi.org/10.1111/j.1365-2435.2007.01256.x (full accessible HTML inspected).
- Harder, L. D., Jordan, C. Y., Gross, W. E. and Routley, M. B. (2004). Beyond floricentrism: The pollination function of inflorescences. *Plant Species Biology* 19:137–148. https://doi.org/10.1111/j.1442-1984.2004.00110.x (full accessible HTML inspected).
- Devaux, C., Lepers, C. and Porcher, E. (2014). Constraints imposed by pollinator behaviour on the ecology and evolution of plant mating systems. *Journal of Evolutionary Biology*. https://doi.org/10.1111/jeb.12380 (full accessible HTML inspected).
- Harder, L. D., Barrett, S. C. H. and Cole, W. W. (2000). The mating consequences of sexual segregation within inflorescences of flowering plants. *Proceedings of the Royal Society B*. https://doi.org/10.1098/rspb.2000.1002 (abstract inspected; complete paper not inspected).
