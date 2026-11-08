# Clustering high-transmission contacts increases mean outbreak size on every cycle, while variance can reverse

## Finding

Place two contacts of transmission probability \(p\) and all other contacts of probability \(q\) around a cycle \(C_n\), where \(n\ge4\) and \(0<q<p<1\). Infect one vertex chosen uniformly at random, and let \(K\) be the size of its connected component after independent bond retention. If \(\mu_d=\mathbb E[K]\) when the two high-probability contacts have shorter cyclic edge separation \(d\), then for every integer \(1\le d<\lfloor n/2\rfloor\),

\[
\mu_d-\mu_{d+1}=\frac{2(p-q)^2}{n}\sum_{k=d+1}^{n-d-1}q^{k-2}>0.
\]

Thus adjacent high-transmission contacts uniquely maximize expected outbreak size up to rotation and reflection, and maximally separated contacts minimize it. The classification is strict for all specified real parameters and all cycle orders, not merely for sampled cases.

On the smallest nontrivial cycle \(C_4\), compare adjacent contacts \(A=(p,p,q,q)\) and alternating contacts \(B=(p,q,p,q)\). Let \(V_A=\operatorname{Var}(K_A)\) and \(V_B=\operatorname{Var}(K_B)\). The exact moment differences are

\[
\mu_A-\mu_B=\frac{(p-q)^2}{2},\qquad
\mathbb E[K_A^2]-\mathbb E[K_B^2]=3(p-q)^2,
\]
\[
V_A-V_B=(p-q)^2\left(3-\frac{\mu_A+\mu_B}{2}\right),
\]
where
\[
\mu_B=1+p+q+2pq+p^2q+pq^2-3p^2q^2,
\quad\mu_A=\mu_B+\frac{(p-q)^2}{2}.
\]

Write \(q_L=1-2/\sqrt7\) and let \(q_U\) be the unique root in \((0,1)\) of
\[
3q_U^4-2q_U^3-2q_U^2-2q_U+2=0.
\]
Numerically \(q_L\approx0.244071054\) and \(q_U\approx0.609294410\). The variance classification is complete:

- If \(0<q\le q_L\), then \(V_A>V_B\) for every \(q<p<1\).
- If \(q_L<q<q_U\), there is one and only one \(p_*(q)\in(q,1)\) such that \(V_A>V_B\) below it, \(V_A=V_B\) at it, and \(V_A<V_B\) above it.
- If \(q_U\le q<1\), then \(V_A<V_B\) for every \(q<p<1\).

This proves a mean–variance decoupling: moving the two stronger contacts together always increases mean outbreak size, but the direction of the variance change depends sharply on transmission strengths.

## Assumptions and scope

The cycle has \(n\ge4\) distinct vertices and \(n\) independent undirected Bernoulli bonds. Two distinct edges retain with probability \(p\); the others retain with probability \(q\). The index source is uniform on the vertices, independent of the bonds. Once bonds are sampled, the infected set is its open-edge connected component. This is an independent-transmissibility percolation/Reed–Frost final-size model; it does **not** assert the same law for an SIR process in which a common random infectious period correlates transmissions from a vertex.

The shorter cyclic edge distance of the two special edges is \(d\in\{1,\dots,\lfloor n/2\rfloor\}\). An optimal arrangement is unique only among these distance classes: rotations, reflections, and swaps of indistinguishable edges produce equivalent assignments.

## Proof

**1. Exact susceptibility identity.** Label edges modulo \(n\), with retention probabilities \(r_i\). For vertices \(u\ne v\), there are precisely two edge-disjoint arcs between them. If the products of their edge-retention probabilities are \(P_{uv}^{(1)}\) and \(P_{uv}^{(2)}\), then inclusion–exclusion gives
\[
\mathbb P(u\leftrightarrow v)=P_{uv}^{(1)}+P_{uv}^{(2)}-R,
\qquad R=\prod_{i=0}^{n-1}r_i.
\]
A uniform index vertex belongs to a component of expected size
\[
\mathbb E[K]=1+\frac2n\sum_{u<v}\mathbb P(u\leftrightarrow v)
=1+\frac2n\left[\sum_{k=1}^{n-1}\sum_{i=0}^{n-1}\prod_{j=0}^{k-1}r_{i+j}-\binom n2R\right].
\]
The double sum lists both arcs of every unordered vertex pair exactly once each.

**2. Moving the two strong edges apart.** Set \(\delta=p-q>0\), and place the two special edges at labels \(0\) and \(d\), so \(r_i=q+\delta\mathbf1_{\{i=0\text{ or }i=d\}}\). Expand each interval product. For any interval length \(k\), the constant term \(q^k\), and the total linear coefficient \(2k\delta q^{k-1}\), are independent of \(d\). The quadratic coefficient is \(\delta^2q^{k-2}C_k(d)\), where \(C_k(d)\) counts cyclic length-\(k\) edge intervals containing both distinguished edges. For \(2\le k\le n-1\),
\[
C_k(d)=(k-d)_++(k-n+d)_+,\qquad(x)_+=\max\{x,0\}.
\]
For \(1\le d<\lfloor n/2\rfloor\),
\[
C_k(d)-C_k(d+1)=
\begin{cases}1,&d+1\le k\le n-d-1,\\0,&\text{otherwise}.\end{cases}
\]
Also \(R=p^2q^{n-2}\) is placement-independent. Subtraction in step 1 yields the claimed formula. Its summation interval is nonempty and all its summands are positive. Strict monotonicity in integer \(d\) proves both global extremizers and all equality cases.

**3. Two-edge configurations on the four-cycle.** On \(C_4\), the two arrangements have the same multiset of independent bond probabilities, hence the same law for the *number* of open bonds. If that count is \(0,1,3,4\), component sizes (and thus the conditional first and second moments for a uniformly sampled index vertex) do not depend on which bonds are open. With exactly two open bonds, adjacent open bonds give components of sizes \(3,1\), hence
\[
(\mathbb E[K\mid\text{configuration}],\mathbb E[K^2\mid\text{configuration}])=(5/2,7),
\]
whereas opposite open bonds give component sizes \(2,2\), hence \((2,4)\). The probability of exactly two *adjacent* open bonds under placement \(A\) minus that under placement \(B\) is
\[
p^2(1-q)^2+q^2(1-p)^2-2pq(1-p)(1-q)=(p-q)^2.
\]
The changes in first and second moments are therefore \((p-q)^2/2\) and \(3(p-q)^2\), respectively. Direct inclusion–exclusion of connected pairs (or the step-1 formula with \(n=4\)) gives the displayed expression for \(\mu_B\). Subtracting the squares of means proves the variance identity.

**4. Exhaustive variance sign diagram.** Let
\[
F(p,q)=12p^2q^2-4p^2q-p^2-4pq^2-6pq-4p-q^2-4q+8.
\]
The step-3 variance identity equivalently gives \(V_A-V_B=(p-q)^2F(p,q)/4\). For fixed \(0<q<1\), the function \(F(p,q)\) is strictly decreasing in \(p\in[q,1]\), because its derivative is affine in \(p\) and negative at both endpoints \(p=0\) and \(p=1\):
\[
\partial_pF(0,q)=-4q^2-6q-4<0,\qquad
\partial_pF(1,q)=20q^2-14q-6=2(q-1)(10q+3)<0.
\]
Its endpoint values are
\[
F(1,q)=7q^2-14q+3,
\qquad F(q,q)=4[3-\mu(q,q)],
\]
where \(\mu(t,t)=1+2t+2t^2+2t^3-3t^4\) is the homogeneous four-cycle mean outbreak size. Coupling each bond to a single uniform random variable shows that \(\mu(t,t)\) rises strictly from \(1\) to \(4\) as \(t\) runs from \(0\) to \(1\). Hence \(F(q,q)\) has exactly one zero \(q_U\), given by the stated polynomial. Likewise \(F(1,q)\) has exactly one zero on \((0,1)\), namely \(q_L\). Since \(q_L<q_U\), monotonicity and the intermediate value theorem give precisely the three cases and the unique interior crossover. Equality on the open parameter domain occurs only on this crossover curve.

## Verification

The standalone `verify.py` evaluates all \(2^n\) independent-bond configurations, finds connected-component sizes using a disjoint-set procedure, and computes \(\mathbb E[K]\) and \(\mathbb E[K^2]\) from \(\sum_j |C_j|^2/n\) and \(\sum_j |C_j|^3/n\) in exact rational arithmetic. It separately expands the two four-cycle moment polynomials as bivariate polynomials and checks the exact coefficient identities. It also enumerates \(4\le n\le10\) for three rational probability pairs and all allowed adjacent-separation comparisons, and checks the strict-sign examples. Execute `python verify.py` with a standard Python 3 interpreter. It reports `PASS 67 exact checks`.

For instance, at \((p,q)=(3/4,1/4)\), the adjacent and alternating means are \(661/256\) and \(629/256\), and \(V_A-V_B=123/1024>0\). At \((9/10,3/4)\), their means are \(6013/1600\) and \(1199/320\), while \(V_A-V_B=-2709/160000<0\). These computations corroborate, but do not establish, the universal real-parameter assertions, which follow from the displayed proof.

## Relationship to prior work

Moore and Newman (1999/2000) analyze percolation representations of epidemics on small-world networks, including homogeneous local bonds. Their model motivates uniform-index outbreak size but does not give a finite fixed-cycle placement inequality for two heterogeneous bonds. Moore and Newman (2000) subsequently derive mean and variance of cluster sizes in the small-world limit; these are not the location-dependent finite-cycle moments here. Allard and collaborators (2008/2009) allow heterogeneity in occupation probabilities on multitype random networks; that ensemble treatment does not imply the specific strict finite-cycle rearrangement or the four-cycle variance switching diagram. Kenah and Robins (2006/2007) explain why correlated transmission from random infectious periods breaks a naive bond-percolation equivalence. Volz and collaborators (2011) analyze heterogeneous, clustered contact structures at a network-ensemble level, rather than the present fixed two-edge arrangement.

## Limitations

The claim is about independently retained undirected edges and a uniformly random initial case; no result is asserted for unequal seed priors, dependence between edges, arbitrary graphs, random-infectious-period SIR, or the variance ordering on larger cycles. The two-edge placement problem has an exact solution for the mean at all \(n\), and an exact variance phase diagram only at \(n=4\). An exhaustive historical-priority claim is not made: related work on rearrangement inequalities for finite reliability networks may cover the result under different terminology, and independent literature audit remains necessary.

## References

1. C. Moore and M. E. J. Newman, *Epidemics and percolation in small-world networks*, first public preprint 1999-11-30, arXiv:cond-mat/9911492, https://arxiv.org/abs/cond-mat/9911492.
2. C. Moore and M. E. J. Newman, *Exact solution of site and bond percolation on small-world networks*, first public preprint 2000-01-26, arXiv:cond-mat/0001393, https://arxiv.org/abs/cond-mat/0001393.
3. E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, first public preprint 2006-10-30, arXiv:q-bio/0610057, https://arxiv.org/abs/q-bio/0610057; open-access full text https://pmc.ncbi.nlm.nih.gov/articles/PMC2215389/.
4. A. Allard, P.-A. Noël, L. J. Dubé, and B. Pourbohloul, *Heterogeneous bond percolation on multitype networks with an application to epidemic dynamics*, first public preprint 2008-11-14, arXiv:0811.2349, https://arxiv.org/abs/0811.2349.
5. E. Volz and collaborators, *Effects of Heterogeneous and Clustered Contact Patterns on Infectious Disease Dynamics*, 2011, https://www.bio.utexas.edu/research/meyers/_docs/publications/VolzPLoSCB11.pdf.
