# A sharp three-habitat reversal of optimal founder placement under migration

## Finding

**Theorem (sharp three-patch founder-site switch).** Consider a continuous-time, density-independent branching population on an undirected path of habitats \(1-2-3\). Individuals at site \(i\) produce one additional individual at the same site at a shared per-capita birth rate \(b\), die at rate \(d_i=b-r_i\), and move to an adjacent site at rate \(m\) per incident edge. Suppose
\[
0<r_3<r_1<r_2<b,\qquad 2r_1>r_2+r_3,\qquad m>0.
\]
Let \(p_i(m)\) be the probability of indefinite population survival from one individual initially placed at site \(i\). Define
\[
t=\frac{r_1}{b},\quad z=\frac{r_3+\sqrt{r_3^2+4r_1(r_2-r_1)}}{2b},\quad
m_*=\frac{(r_2-r_1)t}{t-z}.
\]
Then \(0<z<t\), \(m_*>0\), and the strictly best founder site switches *exactly once*:
\[
\begin{array}{ll}
0<m<m_*: &p_2(m)>p_1(m)>p_3(m),\\
m=m_*: &p_1(m)=p_2(m)=t>p_3(m)=z,\\
m>m_*: &p_1(m)>p_2(m)>p_3(m).
\end{array}
\]
No such strict ranking reversal is possible in a connected one- or two-habitat population with common birth rate, positive net growth at every habitat, and symmetric migration. Thus three habitats are the sharp minimum within this population model.

**Exact example.** For \(b=10\) and \((r_1,r_2,r_3)=(6,8,1)\), the mortality rates are \((4,2,9)\) and the unique switch is \(m_*=6\). At the switch \((p_1,p_2,p_3)=(3/5,3/5,2/5)\). With little movement, habitat 2 (the highest local growth) is best, while sufficiently fast movement favors habitat 1 (the endpoint further from the poorest habitat).

## Assumptions and scope

There is one initial founder; every individual moves, gives birth, and dies independently. Birth yields a parent and one additional individual at the same site. There are no carrying-capacity effects, interactions, density feedback, immigration after initial release, environmental fluctuations, or habitat-specific birth rates. Habitat connectivity is precisely the path \(1-2-3\); each undirected corridor has symmetric, per-capita migration rate \(m\). The local net growth values are strictly positive and strictly below \(b\); hence all death rates are positive.

Population survival means nonextinction for all times. It is distinct from finite-horizon establishment, expected abundance, total person-time, and deterministic spectral growth. The result is an exact theoretical result about the initial placement of one founder, not an empirical prescription for reintroduction.

## Proof

**1. Backward equations and unique positive solution.** First-event conditioning for the independent branching system gives the survival equations
\[
F_i(p;m):=r_ip_i-bp_i^2+m\sum_{j\sim i}(p_j-p_i)=0.\tag{1}
\]
Indeed, a birth at rate \(b\) replaces the initial survival probability \(p_i\) by \(1-(1-p_i)^2\), death replaces it by zero, and a move to \(j\) replaces it by \(p_j\).

Let \(r_-:=\min_i r_i\) and \(r_+:=\max_i r_i\). Couple the total population size to ordinary birth-death processes with common birth rate \(b\) and respective death rates \(b-r_-\) and \(b-r_+\). Their one-founder survival probabilities bound the spatial process, giving
\[
0<r_-/b\le p_i(m)\le r_+/b<1.\tag{2}
\]
The extinction probability vector satisfies (1), so a positive solution exists. It is unique among strictly positive solutions: if \(u,v>0\) both solve (1), let \(c=\max_i u_i/v_i>1\) and choose an index where \(u_i=cv_i\). Then
\[
0=F_i(u;m)-cF_i(v;m)
=-b(c^2-c)v_i^2+m\sum_{j\sim i}(u_j-cv_j)<0,
\]
a contradiction. Interchanging \(u,v\) eliminates all nonidentical positive solutions. These uniform bounds and uniqueness also imply continuity of \(p(m)\) in \(m>0\) by compactness and passage to the limit in (1).

**2. The only possible equality of founder sites 1 and 2.** If \(p_1=p_2=t'>0\), the endpoint equation at site 1 forces \(t'=r_1/b=t\). Write \(p_3=z'\). The center equation then yields
\[
m(z'-t)=(r_1-r_2)t.\tag{3}
\]
Thus \(z'<t\). The site 3 equation and (3) imply
\[
b(z')^2-r_3z'+(r_1-r_2)t=0.\tag{4}
\]
Its constant coefficient is negative; consequently it has exactly one positive root, namely the displayed \(z\). Furthermore
\[
bt^2-r_3t+(r_1-r_2)t=t(2r_1-r_2-r_3)>0,
\]
so its positive root lies strictly below \(t\). Equation (3) then forces the unique crossing parameter \(m=m_*\). Conversely, \((t,t,z)\) satisfies all three equations at \(m_*\); by the positive-solution uniqueness it is the actual survival vector. There can be no other crossing of sites 1 and 2.

**3. Ordering on each side.** As \(m\downarrow0\), any limit of the uniformly positive solutions in (1) must satisfy \(p_i(r_i-bp_i)=0\), so \(p_i\to r_i/b\) for each \(i\). Hence \(p_2>p_1\) at sufficiently small positive migration.

As \(m\to\infty\), the endpoint equations and the bounds (2) yield \(p_1-p_2\to0\) and \(p_2-p_3\to0\). Summing (1) cancels all movement terms, so the common limit must equal
\[
\bar p=\frac{r_1+r_2+r_3}{3b}>0.
\]
Our strict hypothesis \(2r_1>r_2+r_3\) means \(\bar p<r_1/b\). Therefore at sufficiently large migration the site-1 equation gives
\[
m(p_1-p_2)=p_1(r_1-bp_1)>0.
\]
Continuity and the single equality at \(m_*\) establish the exact sign pattern for \(p_2-p_1\).

For every positive migration rate, sites 1 and 3 cannot tie: if \(p_1=p_3=s>0\), subtract their endpoint equations in (1) to get \((r_1-r_3)s=0\), impossible. Their small-migration order thus persists: \(p_1>p_3\). Sites 2 and 3 cannot tie either: \(p_2=p_3=s\) forces \(s=r_3/b\) from the site-3 endpoint, while the site-2 equation would give \((r_2-r_3)s+m(p_1-s)=0\), contrary to \(p_1>p_3=s\). Hence \(p_2>p_3\) for all \(m>0\), establishing the whole displayed ordering.

**4. Sharpness with respect to habitat count.** With one site there is no placement choice. With two connected sites and common birth rate \(b\), their survival equations remain (1). If \(p_1=p_2=t>0\), all migration terms vanish, so \(t=r_1/b=r_2/b\). If the two net growth rates differ, no tie or ranking reversal can occur by continuity; if equal, symmetry gives equality for every migration rate and again no strict reversal. Thus a connected two-site model cannot have this effect. The three-site construction establishes sharpness.

For the exact example, the quadratic (4) becomes \(10z^2-z-6/5=0\), with positive root \(z=2/5\). Then \(m_*=(8-6)(3/5)/(3/5-2/5)=6\), verifying the claimed exact crossing.

## Verification

The standalone script `founder_check.py` verifies polynomial identities with exact rational/symbolic arithmetic, the exact witness and crossing, 120 finite migration comparisons, and a family of parameters satisfying the open hypotheses on both sides of the predicted crossing. It can be run with Python 3, SymPy, NumPy, and SciPy via `python founder_check.py`. The full all-parameter theorem depends on the proof above, not on numerical samples. The script is an additional consistency test, not an independent proof or external certification.

## Relationship to prior work

Bansaye and Lambert, *Past, growth and persistence of source-sink metapopulations* (first available November 10, 2011, arXiv:1111.2535), study stochastic source-sink populations and decouple demographic and dispersal effects. Their persistence criteria, long-run growth, and ancestral habitat frequency results motivate the model, but the inspected manuscript does not establish a founder-site survival-probability ranking switch at a unique migration rate.

Hautphenne, Latouche, and Nguyen, *Extinction probabilities of branching processes with countably infinitely many types* (arXiv:1211.4129), develop general extinction-vector iteration methods, emphasizing countably many types rather than a sharp ordering classification on the three-site path. Hautphenne, Latouche, and Remiche, *Algorithmic Approach to the Extinction Probability of Branching Processes* (2011), is a related general algorithmic reference; its complete primary text was not accessed. The present contribution is the explicit single-crossing formula and sharp habitat-count boundary, not the standard backward equations or uniqueness technique.

## Limitations

The exact theorem concerns the density-independent branching model, shared birth rate, strictly positive local net growth, symmetric migration, and a three-habitat path. Habitat-specific birth rates, immigration, nonlinear density dependence, correlated demographic events, finite time, and general graphs are not classified here. The result establishes an exact mathematical ordering and does not quantify ecological field risk. Literature priority is provisional: an equivalent older theorem in branching-process or population-placement literature cannot be ruled out by the inspected sources alone; a 2011 algorithm paper was available only in abstract/preview.

## References

- Bansaye, V., and Lambert, A. (2011). *Past, growth and persistence of source-sink metapopulations*. arXiv:1111.2535, first version November 10, 2011. https://arxiv.org/abs/1111.2535
- Hautphenne, S., Latouche, G., and Nguyen, G. (2012). *Extinction probabilities of branching processes with countably infinitely many types*. arXiv:1211.4129, first version November 17, 2012. https://arxiv.org/abs/1211.4129
- Hautphenne, S., Latouche, G., and Remiche, M.-A. (2011). *Algorithmic Approach to the Extinction Probability of Branching Processes*. Methodology and Computing in Applied Probability. https://doi.org/10.1007/s11009-009-9141-7
