# Three-way source forcing for discounted hitting domination on balanced tripartite graphs

## Finding

Let \(m\ge4\), \(0<\lambda<1\), and let \(G=K_{m,m,m}\) be the labelled complete tripartite graph. A nonempty source set \(S\subseteq V(G)\) has discounted hitting support \(h_v^S=\mathbb E_v[\lambda^{T_S}]\), where the walk is simple random walk and \(T_S\) is its first hitting time of \(S\). Sources have support \(1\). For \(0<\tau\le1\), write \(\delta_{\lambda,\tau}(G)\) for the minimum cardinality of \(S\) such that every vertex has support at least \(\tau\).

Set \(A=m(1-\lambda)+\lambda\),
\[
D=4m^2-\lambda^3(m-1)(m-2)-\lambda^2(3m^2-6m+2),
\qquad E=m(2-\lambda-\lambda^2)+3\lambda^2.
\]
Define
\[
\eta_{111}=\frac{\lambda}{A},\qquad
\eta_{210}=\frac{\lambda\bigl(2\lambda^2(m-1)+\lambda(5m-2)+2m\bigr)}{D},\qquad
\eta_{300}=\frac{3\lambda^2}{E},\qquad
b_m(\lambda)=\max\{\eta_{210},\eta_{300}\}.
\]
Then \(b_m(\lambda)<\eta_{111}\). For the entire nonempty interval
\[
\boxed{b_m(\lambda)<\tau\le\eta_{111}},
\]
\(\delta_{\lambda,\tau}(K_{m,m,m})=3\), and **every** minimum feasible source set contains exactly one vertex from each of the three parts. Thus exactly \(m^3\) labelled minimum source sets exist, and no source set of cardinality at most two is feasible. This three-way-forcing assertion is sharp at the part-size boundary: on \(K_{3,3,3}\) a three-source set contained in one complete part has worst support \(\lambda/(2-\lambda)>\lambda/(3-2\lambda)\), the worst support of a balanced triple, for every \(0<\lambda<1\).

More generally, for \(r\ge2\) and arbitrary positive part sizes \(n_1,\ldots,n_r\), a finite exact profile formula below gives the *full cardinality polynomial* of all discounted-hitting-feasible sets, not just the minimum. The three-way forcing theorem is its nontrivial uniform consequence.

## Assumptions and scope

All graphs are finite, simple, connected and unweighted; the random walk chooses a neighbor uniformly. The discount is homogeneous, \(0<\lambda<1\), and thresholds satisfy \(0<\tau\le1\). The three-way theorem assumes three equally sized parts and \(m\ge4\); no claim is made for other tripartite sizes or other numbers of parts. Vertices are labelled when counting source sets.

For a complete multipartite graph with \(N=\sum_i n_i\) vertices, write \(s_i=|S\cap V_i|\) and \(u_i=n_i-s_i\), where \(0\le s_i\le n_i\), \(s=\sum_i s_i>0\), and \(d_i=N-n_i>0\). Each unselected vertex in part \(i\) has the same support \(h_i\). A part with \(u_i=0\) imposes no support constraint because all its vertices are selected.

## Proof

**1. Exact multipartite profile reduction.** Let \(B=s+\sum_j u_j h_j\) be the sum of all vertex supports. The discounted harmonic equation at an unselected vertex in part \(i\) is
\[
h_i=\frac{\lambda}{d_i}\bigl(B-s_i-u_i h_i\bigr).
\]
Consequently
\[
h_i=\frac{\lambda(B-s_i)}{d_i+\lambda u_i},\qquad
 a_i=\frac{\lambda u_i}{d_i+\lambda u_i},\qquad
 B=\frac{\sum_i s_i(1-a_i)}{1-\sum_i a_i}.
\]
The expression for \(B\) follows by substituting the first equation in its definition. Its denominator is positive: \(a_i\le\lambda n_i/(N-n_i+\lambda n_i)<n_i/N\), so \(\sum_i a_i<1\). The identical formulas may be used for a fully selected part as an algebraic convenience, but its formal \(h_i\) is not a vertex constraint.

This is an exact reduction of the unique discounted equilibrium, not an asymptotic approximation. Every set with the same profile has identical feasibility. Therefore the complete cardinality enumerator is
\[
\boxed{
 \mathcal H_{G;\lambda,\tau}(z)=
 \sum_{\substack{0\le s_i\le n_i\\\sum_i s_i>0}}
 \mathbf1\left\{\forall i\text{ with }u_i>0:\;
 \frac{\lambda(B(\mathbf s)-s_i)}{d_i+\lambda u_i}\ge\tau\right\}
 \prod_{i=1}^r\binom{n_i}{s_i}\,z^{\sum_i s_i}.
 }
\]
Its lowest nonzero degree equals \(\delta_{\lambda,\tau}(G)\). The profile summation takes at most \(\prod_i(n_i+1)\) rational evaluations for rational input parameters, and does not imply a polynomial-time algorithm when the number of parts varies.

**2. All three-source profiles.** For \(K_{m,m,m}\) with \(m\ge4\), every three-source profile is, up to permuting parts, \((1,1,1)\), \((2,1,0)\), or \((3,0,0)\). Every part has an unselected vertex. The preceding formulas give a common unselected support \(\eta_{111}\) for the balanced profile.

For fixed total support \(B\), the function
\[
f(t)=\frac{\lambda(B-t)}{2m+\lambda(m-t)}
\]
is strictly decreasing for \(0\le t\le3\), since its derivative has the sign of \(\lambda B-(2+\lambda)m\), which is negative as \(B\le3m\) and \(0<\lambda<1\). Thus the worst support in either unbalanced profile occurs at a non-source in the part containing the most sources. Direct substitution of \((2,1,0)\) and \((3,0,0)\) into the profile formula gives \(\eta_{210}\) and \(\eta_{300}\) respectively.

**3. Both unbalanced profiles are strictly worse.** All three denominators \(A,D,E\) are strictly positive: \(A>0\), \(E>0\), and, for \(m\ge4\), the two subtracted terms in \(D\) are nonnegative and increase with \(\lambda\), so
\[
 D>4m^2-(m-1)(m-2)-(3m^2-6m+2)=9m-4>0.
\]
Simple exact subtraction gives
\[
\eta_{111}-\eta_{210}=
\frac{\lambda m(1-\lambda)\bigl(m(2-\lambda-\lambda^2)+\lambda^2\bigr)}{AD}>0
\]
and
\[
\eta_{111}-\eta_{300}=
\frac{2\lambda m(1-\lambda)^2}{AE}>0.
\]
This proves \(b_m(\lambda)<\eta_{111}\), with a nonempty forcing interval for every allowed \(m,\lambda\).

**4. Exact optimizer count and lower cardinalities.** Fix \(b_m(\lambda)<\tau\le\eta_{111}\). Every balanced triple is feasible; all other three-source profiles fail. Discounted hitting support is monotone under source-set inclusion because \(T_{S'}\le T_S\) for \(S\subseteq S'\), so \(h_v^{S'}\ge h_v^S\). Any source set with one or two vertices can be extended, without introducing a new occupied part, to an unbalanced three-source set (there are at least four vertices per part). Since every such extension fails, its smaller subset also fails. Thus the minimum size is three. There are exactly \(m\) independent choices in each of three labelled parts, giving \(m^3\) optimizers.

**5. Sharp boundary at part size three.** For \(m=3\), selecting all vertices of one part leaves two identical unselected parts. The equilibrium for each non-source is \(h=\lambda(1+h)/2\), so \(h=\lambda/(2-\lambda)\). The balanced triple instead has worst support \(\lambda/(3-2\lambda)\), strictly less because \(3-2\lambda>2-\lambda\) for \(\lambda<1\). Hence balanced triples cannot be the unique optimal three-source configurations on \(K_{3,3,3}\) in an interval ending at their own support.

## Verification

The standalone `verify.py` uses only Python's standard library. It checks the full multipartite cardinality polynomial against independently solved rational vertex-level Dirichlet systems for 27 small complete multipartite instances, including instances with fully selected parts. It independently solves the vertex-level system for each of the three three-source profiles at 54 distinct pairs \((m,\lambda)\), namely \(4\le m\le12\) and six rational discounts, giving 162 exact solutions. It checks both symbolic difference identities by exact rational substitution, all three-source profile possibilities, and the \(m=3\) boundary. Its final line is `VERIFY_OK`. These finite checks corroborate, but do not replace, the proof for all real \(\lambda\) and all integer \(m\ge4\).

As an explicit test, at \(m=4\), \(\lambda=1/2\), the balanced profile has minimum support \(1/5\), the \((2,1,0)\) profile has \(37/227\), and the \((3,0,0)\) profile has \(3/23\). At \(\tau=1/6\), exactly 64 three-source sets meet the floor, with one selected vertex in each part; no smaller set works.

## Relationship to prior work

Allagan, Pereyra and Massey (arXiv:2609.31535v1, first public September 25, 2026) introduced discounted hitting domination, proved monotonicity and submodularity of the discounted support, developed general complexity results and exact methods for spiders, and computed examples on complete graphs and stars. Those theorems do not supply the three-source phase on balanced tripartite graphs. An earlier exact calculation restricted to complete *bipartite* graphs determines two-part profiles but does not mathematically imply the three-way forcing assertion here: the third nonempty part changes both degrees and the list of possible optimal profiles. The reduction to multipartite profiles above is given explicitly so that this non-implication can be independently checked. Earlier group hitting probability literature provides general evaluation methods for a fixed source set, not this parameter-uniform classification of every minimum threshold-feasible source set.

## Limitations

The forcing law does not extend unchanged to \(m=3\). The proof does not classify arbitrary unequal tripartite graphs, determine all threshold phases, or provide polynomial-time computation for an unbounded number of multipartite parts. The novelty comparison is based on accessible primary and mathematical research records, not a proof of historical priority. No independent mathematical audit has been performed.

## References

1. J. D. Allagan, K. Pereyra and W. A. Massey, *Discounted Hitting Domination on Graphs with Submodularity, Complexity and Exact Algorithms*, arXiv:2609.31535v1 (September 25, 2026), https://arxiv.org/abs/2609.31535.
2. S. Guo et al., *Efficient Algorithms for Group Hitting Probability Queries on Large Graphs*, IEEE Transactions on Knowledge and Data Engineering (2024), DOI:10.1109/TKDE.2023.3349164. (Background on fixed-set hitting probabilities, not the uniform-floor classification.)
