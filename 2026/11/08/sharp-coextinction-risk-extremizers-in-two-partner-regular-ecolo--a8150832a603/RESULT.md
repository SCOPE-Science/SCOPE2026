# Sharp coextinction-risk extremizers in two-partner regular ecological networks

## Finding
Let \(n\ge3\). Consider \(n\) habitat patches and \(n\) dependent species; each dependent species uses exactly two distinct patches and survives as long as at least one of its patches survives. Every patch supports exactly two dependent species, and no two species have identical partner pairs. Write \(G\) for the resulting simple \(2\)-regular graph on the habitat patches, with one edge per dependent species. Thus \(G\) is a disjoint union of cycles \(C_\ell\), \(\ell\ge3\).

After uniformly deleting exactly \(t\in\{0,\ldots,n\}\) distinct patches, write \(R_t(G)\) for the probability that **at least one** dependent species becomes extinct. Define the two cycle-partition networks
\[
G_-(n)=\begin{cases}kC_3,&n=3k,\\(k-1)C_3\sqcup C_4,&n=3k+1,\\(k-1)C_3\sqcup C_5,&n=3k+2,\end{cases}
\quad
G_+(n)=\begin{cases}kC_4,&n=4k,\\(k-1)C_4\sqcup C_5,&n=4k+1,\\(k-1)C_4\sqcup C_6,&n=4k+2,\\(k-1)C_4\sqcup C_7,&n=4k+3,\end{cases}
\]
with the evident single-cycle interpretations for \(n=3,4,5,6,7\) (particularly \(G_+(3)=C_3\)).

**Theorem.** For every such \(G\) and every \(t\),
\[
R_t(G_+(n))\le R_t(G)\le R_t(G_-(n)).
\]
Equivalently, the independent-set polynomials obey the **coefficientwise** inequalities
\[
I_{G_-(n)}(z)\preceq I_G(z)\preceq I_{G_+(n)}(z),\qquad
I_G(z)=\sum_{t=0}^n i_t(G)z^t.
\]
Each extremal polynomial is attained by only its displayed cycle partition, up to graph isomorphism. The same extremizers and strict class-wide uniqueness hold when habitat losses are independent with any common probability \(q\in(0,1)\). Equality at an individual fixed \(t\) need not characterize either extremizer.

For \(n=9\), deletion of \(t=3\) patches gives \(i_3(3C_3)=27\) and \(i_3(C_4\sqcup C_5)=30\), out of \(\binom93=84\) equally likely triples. The probabilities of at least one coextinction are respectively \(19/28\) and \(9/14\).

## Assumptions and scope
The claim concerns *one-step deterministic secondary losses*: a secondary species dies exactly when both of its partners are deleted. There are no feedback cascades, population dynamics, weighted interactions, repeated partner pairs, or unequal deletion probabilities. Species and patches have degree exactly two on their respective sides of the incidence network. The graph is allowed to be disconnected. Uniform deletion means every \(t\)-element subset of patches is equally likely. The Bernoulli model independently deletes every patch with probability \(q\). The graph-theoretic polynomial order \(A(z)\preceq B(z)\) means every corresponding coefficient of \(B-A\) is nonnegative.

## Proof
**1. Extinction event and independence polynomial.** A removed patch set avoids all secondary extinctions precisely when it contains no edge of \(G\), i.e., when it is an independent vertex set. Therefore
\[
R_t(G)=1-\frac{i_t(G)}{\binom nt},\qquad
\Pr_q(\text{no secondary extinction})=(1-q)^n I_G\!\left(\frac q{1-q}\right).
\]
The second identity follows by summing \(q^{|S|}(1-q)^{n-|S|}\) over independent deleted sets \(S\).

**2. A signed cycle-merge identity.** For \(\ell\ge3\), the independent-set polynomial of a cycle is
\[
I_{C_\ell}(z)=\sum_{j=0}^{\lfloor\ell/2\rfloor}\frac{\ell}{\ell-j}\binom{\ell-j}j z^j.
\]
Let \(u+v=1\) and \(uv=-z\). The standard two-state circular independent-set transfer gives \(I_{C_\ell}=u^\ell+v^\ell\). Set \(L_0=2\), \(L_1=1\), \(L_2=1+2z\), and \(L_j=I_{C_j}\) for \(j\ge3\). All these polynomials have strictly positive coefficients on their nonzero terms. For \(a,b\ge3\), direct expansion gives
\[
I_{C_a}I_{C_b}-I_{C_{a+b}}
=(uv)^{\min(a,b)}(u^{|a-b|}+v^{|a-b|})
=(-z)^{\min(a,b)}L_{|a-b|}(z).
\tag{1}
\]
In particular, **splitting** a cycle of length \(a+b\) into cycles of lengths \(a,b\) *strictly raises* its polynomial for even \(\min(a,b)\), and *strictly lowers* it for odd \(\min(a,b)\), coefficientwise.

**3. Universal coefficientwise minimum.** Whenever a component has length at least six, split it as \(C_3\sqcup C_{\ell-3}\). By (1) the independent-set polynomial strictly decreases coefficientwise. Repeating leaves only cycles of sizes 3, 4, or 5. The following additional replacements all strictly decrease it, as can be verified from the preceding cycle formula:
\[
\begin{array}{rcl}
I_{2C_4}-I_{C_3\sqcup C_5}&=&z^3(1+4z),\\
I_{C_4\sqcup C_5}-I_{3C_3}&=&z^3(3+10z),\\
I_{2C_5}-I_{2C_3\sqcup C_4}&=&z^3(2+7z).
\end{array}
\]
The replacements leave at most one cycle of length 4 or 5 and preserve the total vertex count, so the resulting decomposition is necessarily \(G_-(n)\). Finite termination follows since each preliminary split increases the number of components, and each exceptional replacement lowers the number of nontriangle components. Every changed decomposition strictly changes its polynomial for every positive \(z\), proving the minimum and class-wide uniqueness.

**4. Universal coefficientwise maximum.** Split every cycle of length at least eight as \(C_4\sqcup C_{\ell-4}\); by (1), this strictly raises the polynomial. For any component of length three that has another component, combine it with a second component of length 3, 4, 5, 6, or 7, then, when needed, split the merged cycle by fours. The five replacements are
\[
(3,3)\to(6),\ (3,4)\to(7),\ (3,5)\to(4,4),\ (3,6)\to(4,5),\ (3,7)\to(4,6),
\]
all strictly increasing coefficientwise by (1). For \(n>3\), there are now only 4-, 5-, 6-, and 7-cycles. Every pair of exceptional sizes (5, 6, 7) can be removed by these strictly increasing replacements:
\[
\begin{array}{rcl}
(5,5)&\to&(4,6),\\(5,6)&\to&(4,7),\\(5,7)&\to&(4,4,4),\\
(6,6)&\to&(4,4,4),\\(6,7)&\to&(4,4,5),\\(7,7)&\to&(4,4,6).
\end{array}
\]
The polynomial differences (new minus old) are, respectively,
\[
z^4(1+4z),\ z^4(1+4z),\ z^4(3+13z+8z^2),\ z^4(3+12z+4z^2),\ z^4(2+9z+6z^2),\ z^4(2+12z+19z^2+8z^3).
\]
All have nonnegative coefficients and are nonzero for \(z>0\). Each replacement reduces the number of exceptional components; the final decomposition has at most one exceptional cycle, necessarily \(G_+(n)\) by the total vertex-count residue modulo four. The case \(n=3\) is immediate. Hence the maximum and strict full-polynomial uniqueness hold.

**5. Fixed-count and independent loss.** Multiplying the polynomial inequalities by any independent-set polynomial preserves coefficientwise order because its coefficients are nonnegative. The preceding transformations therefore prove the global coefficientwise claim. Substitute the formulas from step 1 to reverse the order for \(R_t\). For independent deletion with \(0<q<1\), evaluate at strictly positive \(z=q/(1-q)\); every nontrivial transformation gives a strict inequality. This proves both loss models and the asserted uniqueness.

## Verification
The standalone `verify.py` uses only Python's standard library and exact integers. Running `python verify.py` checks 484 independent polynomial merge identities, the nine exceptional transformations, coefficientwise bounds and distinct full-polynomial optimizers for all 5,666 cycle partitions on 3 through 36 vertices, and direct enumeration of removed patch sets for every cycle partition through 11 vertices (25 distributions). It separately checks the nine-patch example. The proof above, not this finite enumeration, establishes the theorem for all \(n\).

## Relationship to prior work
The traditional topological coextinction convention of losing a dependent species only after all its partners disappear is explicitly discussed and employed by Evans, Pocock, and Memmott (2013) and Vieira and Almeida-Neto (2015); their ecological network studies address simulations and more general dependency models, not these exact regular-degree coefficientwise extremizers. Zhao (2009) proves the general pointwise activity upper bound for regular-graph independent-set polynomials; in the two-regular case it already covers the **pointwise upper bound** when \(n\) is divisible by four, although it does not provide this all-fixed-cardinality coefficientwise inequality or the exact residual cycle partitions. Galvin (2010) and Alexander and Mink (2013/2014) describe and partially resolve fixed-size independent-set extremality problems; Alexander and Mink treat \(t\le3\) and certain \(t=4\) cases. Sah, Sawhney, Stoner, and Zhao (2018) derive pointwise regular-graph bounds, including extremal divisible-order regimes, but not the complete coefficientwise residue classification stated here. A previous exact third-moment calculation for the same two-partner coextinction model addresses a different statistic: it does not entail sharp bounds on the full probability of avoiding *any* secondary extinction at every deletion count.

## Limitations
This result applies only to simple two-regular requirement graphs and uniform or iid patch loss. Other ecological models, heterogeneous susceptibility, directed dependencies, and cascades are not covered. At fixed small deletion counts, several graph shapes can tie; the uniqueness assertion concerns simultaneous all-coefficient or positive-activity extrema, not every \(t\) separately. The coefficientwise theorem is derived here by explicit constructive inequalities; novelty comparisons cannot exclude all unindexed graph-polynomial results or older classifications, and external independent review remains outstanding.

## References
- Y. Zhao, *The Number of Independent Sets in a Regular Graph* (2009), arXiv:0909.3354, https://arxiv.org/abs/0909.3354.
- D. Galvin, *An Upper Bound for the Number of Independent Sets in Regular Graphs* (2010), arXiv:1007.4811, https://arxiv.org/abs/1007.4811.
- J. Alexander and T. Mink, *A New Method for Enumerating Independent Sets of a Fixed Size in General Graphs* (2013 preprint; 2014 version), arXiv:1308.3242, https://arxiv.org/abs/1308.3242.
- A. Sah, M. Sawhney, D. Stoner and Y. Zhao, *The Number of Independent Sets in an Irregular Graph* (2018), arXiv:1805.04021, https://arxiv.org/abs/1805.04021.
- D. M. Evans, M. J. O. Pocock and J. Memmott, *The Robustness of a Network of Ecological Networks to Habitat Loss* (2013), *Ecology Letters*, DOI:10.1111/ele.12117, https://doi.org/10.1111/ele.12117.
- M. C. Vieira and M. Almeida-Neto, *A Simple Stochastic Model for Complex Coextinctions in Mutualistic Networks: Robustness Decreases with Connectance* (2015), *Ecology Letters*, DOI:10.1111/ele.12394, https://doi.org/10.1111/ele.12394.
