# Exact entrance-time census and parity law for majority dynamics on triangular books

## Finding
For every integer \(n\ge2\), let \(B_n=K_2\vee\overline{K_n}=K_{1,1,n}\) be the triangular book with two adjacent hubs and \(n\) independent vertices each adjacent to both hubs. Give every vertex a binary state. At each integer time, update simultaneously to the strict majority state among its *open* neighbors, retaining its old state if the votes tie.

Let \(E_{p,t}(n)\) be the number of labelled initial configurations whose eventual *least* period is \(p\) and whose **first periodic-entry time** is exactly \(t\) (that is, the least \(t\ge0\) at which the complete state is periodic). Set \(C_n=\binom{n}{\lfloor n/2\rfloor}\). Then every orbit has period one or two by time two, and the complete entrance-time census is

\[
\begin{array}{c|ccccc}
 &E_{1,0}&E_{2,0}&E_{1,1}&E_{2,1}&E_{1,2}\\\hline
 n\ \mathrm{even} &2&2+2C_n&2^n+C_n+2&2^n-C_n-2&2^{n+1}-2C_n-4\\
 n\ \mathrm{odd},\ n\ge3 &2&2&2^n+2C_n+2&2^n-2C_n-2&2^{n+1}-4
\end{array}
\]

All other \(E_{p,t}(n)\) vanish. Hence the full basin of genuine period two has the **different parity laws**
\[
E_{2,0}(n)+E_{2,1}(n)=
\begin{cases}
2^n+C_n,&n\text{ even},\\
2^n-2C_n,&n\text{ odd},\ n\ge3.
\end{cases}
\]
Under independent unbiased initial bits, the probability of *eventual* primitive two-periodicity tends to \(1/4\) along both parities, whereas the probability of *immediate* primitive two-periodicity is asymptotic to \(\frac12\sqrt{2/(\pi n)}\) for even \(n\), and exactly \(2^{-n-1}\) for odd \(n\ge3\). Thus the immediate-cycle contrast does not persist at the level of the full basin. The first-periodic-entry bound two is attained for all \(n\ge3\), and for \(n=2\) the bound is one.

## Assumptions and scope
All vertices are labelled. The two hub states are \(a,b\in\{0,1\}\); the \(n\) independent vertices (pages) have an arbitrary labelled binary word \(w\in\{0,1\}^n\). Let \(s=\sum_{i=1}^n w_i\). The count of words with a given \(s\) is \(\binom ns\). A state on the period-two orbit is counted as one configuration; the two configurations of each orbit are counted separately. First periodic-entry time is measured in whole synchronous updates from time zero. No random graph, asynchronous update, or alternative tie convention is considered. The boundary \(n=1\) is excluded because the triangular book degenerates to a triangle and has a different recurrent census.

## Proof
**1. Exact quotient update without loss of fibres.** A page vertex has precisely the two hubs as neighbors. If \(a=b\), all page states become \(a\) in one step; if \(a\ne b\), each page sees a tie and retains its own state. The hub degree is \(n+1\). If \(\phi_n(x,r)\) is one when \(2r>n+1\), zero when \(2r<n+1\), and \(x\) on equality, the entire update is
\[
 a'=\phi_n(a,b+s),\qquad b'=\phi_n(b,a+s),\qquad
 w'=\begin{cases}(a,\ldots,a),&a=b,\\w,&a\ne b.\end{cases}
\]
Thus its count-preserving weighted quotient is \((a,b,s)\mapsto(a',b',s')\) with \(s'=na\) when \(a=b\), and \(s'=s\) otherwise; each initial triple carries weight \(\binom ns\). Once a page word has been homogenized, every future state is determined by the quotient.

**2. Exhaustive hub cases.** If \(n=2k\) is even, the two new hub bits are
\[
 (a',b')=\begin{cases}(0,0),&0\le s\le k-1,\\(b,a),&s=k,\\(1,1),&k+1\le s\le 2k.
\end{cases}
\]
If \(n=2k+1\ge3\) is odd, they are
\[
(a',b')=\begin{cases}
(0,0),&0\le s\le k-1,\\
(1,1),&s=k\ \text{and}\ (a,b)=(1,1),\\
(0,0),&s=k\ \text{and}\ (a,b)\ne(1,1),\\
(0,0),&s=k+1\ \text{and}\ (a,b)=(0,0),\\
(1,1),&s=k+1\ \text{and}\ (a,b)\ne(0,0),\\
(1,1),&k+2\le s\le2k+1.
\end{cases}
\]
These cases, with the page rule, show directly that the only fixed states are the two unanimous states, and that no state has first periodic-entry time exceeding two: outside the central layers, after one update the hubs agree, hence on the next update the pages are homogeneous; the only resulting nonfixed pair is the alternating state \((a,b,w)=(0,0,1^n)\leftrightarrow(1,1,0^n)\). On the central layers, an opposite-hub state either alternates there immediately (the even case) or its hubs agree after one update and the next state becomes unanimous (the odd case). An equal-hub central state becomes unanimous in one update. The two homogeneous states just displayed do alternate for every \(n\ge2\).

**3. Immediate two-periodic states and their nonperiodic predecessors.** For even \(n=2k\), the central states \(s=k\) with \(a\ne b\) swap their hubs at each time while pages stay unchanged, yielding \(2\binom nk\) immediate period-two states. The homogeneous alternating pair adds two. Thus \(E_{2,0}=2+2C_n\). For odd \(n=2k+1\ge3\) no central opposite-hub state oscillates, leaving only the homogeneous alternating pair, so \(E_{2,0}=2\).

If \(n\) is even, the nonperiodic states entering that alternating pair after exactly one update are precisely the equal-hub states with \((a,b)=(0,0),s>k\), or with \((a,b)=(1,1),s<k\), excluding the two states already on the pair. Their number is \(2^n-C_n-2\). If \(n\) is odd, replace the strict inequalities by \(s\ge k+2\) and \(s\le k-1\) respectively. The two symmetric binomial tails then give \(2^n-2C_n-2\). No other state can enter a nonfixed recurrent orbit, and no such entry occurs at time two. This proves both period-two columns and the basin formulas.

**4. Fixed-state entrance distribution.** In the even case, the central equal-hub states contribute \(2C_n\) states that become fixed after one update. Away from the central layer, aligned hubs \(a=b=0\) on the lower side and \(a=b=1\) on the upper side contribute together \(2^n-C_n\). There are four additional opposite-hub configurations with \(s=0\) or \(s=n\), which become unanimous in one step, and the two initial unanimous states must be subtracted. Hence \(E_{1,1}=2C_n+(2^n-C_n)+4-2=2^n+C_n+2\).

In the odd case the equal-hub configurations in both central layers \(s=k,k+1\) contribute \(4C_n\), and the aligned-hub exterior tails contribute \(2^n-2C_n\); again the four opposite-hub extreme states contribute and the two initially fixed states are removed. Hence \(E_{1,1}=2^n+2C_n+2\). Finally all \(2^{n+2}\) states lie in one of the disjoint classes already enumerated, and all states become periodic by time two, so subtraction gives \(E_{1,2}=2^{n+1}-2C_n-4\) in the even case and \(E_{1,2}=2^{n+1}-4\) in the odd case. The other entries are zero. For \(n=2\) the resulting \(E_{1,2}\) is zero; for every \(n\ge3\) it is positive, proving sharpness.

**5. Random-initial-state consequences.** There are \(4\cdot2^n\) equally likely labelled initial configurations. Dividing the two basin formulas by this total, and using \(C_n/2^n\sim\sqrt{2/(\pi n)}\), yields the claimed common \(1/4\) limit. Dividing \(E_{2,0}\) yields the respective polynomial and exponential immediate-cycle laws. There is no inference from finite enumeration in any part of this proof.

## Verification
The standalone program `verify_direct.py` simulates each of the \(131{,}056\) labelled initial configurations for every \(2\le n\le14\), independently identifies its eventual least period and first periodic-entry time, and compares each count with all five displayed formulas. The separate `verify_weighted.py` implements the quotient-state dynamics and exact binomial weighting for every \(2\le n\le120\). Both completed successfully; the actual captured outputs are embedded as `direct_output.txt` and `weighted_output.txt`. Run from an extraction of this package using `python verify_direct.py` and `python verify_weighted.py`. These finite checks confirm concrete cases; the general proof is the quotient case analysis above.

## Relationship to prior work
General synchronous threshold-network results guarantee eventual fixed points or two-cycles but do not supply a labelled initial-state entrance-time census. Kuhlman–Mortveit–Murrugarra–Kumar analyze more general bi-threshold systems and construct examples over trees and cycles, with a principal focus on recurrent periods, not these triangular-book basin cardinalities. Benjamini–Chan–O'Donnell–Tamuz–Tan study convergence and disagreement on infinite transitive and random graphs, not exact basins of this finite split graph. The immediate two-cycle population in this theorem is an elementary special case of general complete-split periodic-state counting; **the finding here is the complete entrance-time distribution and its asymptotic eventual-versus-immediate contrast**, which is not determined by the periodic-state count or a stabilization-time upper bound alone.

## Limitations
The result covers exactly the triangular book \(K_{1,1,n}\), not all split graphs. It uses binary strict open-neighbor majority and retention on ties. It proves the exact entrance distribution, without claiming independent verification, publication priority, or a universal phase transition for other graph families. Related formulas could occur under different terminology; an older foundational threshold paper was available only in abstract form, so literature priority is not certified.

## References
1. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra, and V. S. A. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974, first posted 2011-08-15. https://arxiv.org/abs/1108.2974
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486, first posted 2014-05-11. https://arxiv.org/abs/1405.2486
3. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. DOI:10.1016/0012-365X(80)90121-1. Only bibliographic abstract was accessible for this comparison.
