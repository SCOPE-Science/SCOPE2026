# Exact three-state Potts field diagram on the Grötzsch graph

## Finding

The three-state nearest-neighbor Potts antiferromagnet with a single preferred spin value on the eleven-vertex Grötzsch graph has **eight open-field ground-state regimes and seven coexistence fields**. With the normalization in the next section, put \(x=h/J\). The ground-state energy for every real field is

\[
\frac{E_0(h)}{J}=\min\{4,\ 1-2x,\ 1-5x,\ 2-6x,\ 4-7x,\ 7-8x,\ 15-10x,\ 20-11x\}.
\]

As \(x\) increases through the complement of the seven critical values \(-3/2,0,1,2,3,4,5\), the respective favored-spin occupancies are exactly \(0,2,5,6,7,8,10,11\). All minimum-energy configurations at a noncritical field have the same occupancy, and the counts for those eight regimes are, respectively, \(10,30,80,60,40,40,2,1\).

At the seven critical fields the *total* numbers of ground configurations (with three spin labels distinct) are:

| \(h/J\) | \(-3/2\) | \(0\) | \(1\) | \(2\) | \(3\) | \(4\) | \(5\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Multiplicity | 40 | 660 | 140 | 100 | 80 | 62 | 3 |

At zero field there is precisely one monochromatic (frustrated) edge in every ground configuration. Of the 660 configurations, the defect lies on a pentagon edge in 210, a shadow-to-pentagon edge in 300, and an apex-to-shadow edge in 150. Equivalently, every edge of these three respective orbits supports 42, 30 and 30 ground configurations.

## Assumptions and scope

Let \(G=\mu(C_5)\) be the Grötzsch graph with vertices \(v_i,u_i\) for \(i\in\mathbb Z/5\mathbb Z\) and a vertex \(w\). Its twenty edges are exactly \(v_iv_{i+1}\), \(u_iv_{i-1}\), \(u_iv_{i+1}\), and \(u_iw\), taking each indicated edge for each \(i\). This is the smallest triangle-free four-chromatic graph.

Each vertex receives a spin \(\sigma\in\{0,1,2\}\). The three labels are distinct. The antiferromagnetic coupling satisfies \(J>0\), and \(h\in\mathbb R\) is a uniform longitudinal field favoring label 0. The Hamiltonian is

\[
H_{J,h}(\sigma)=J\sum_{\{p,q\}\in E(G)}\mathbf1_{\sigma_p=\sigma_q}-h\sum_{p\in V(G)}\mathbf1_{\sigma_p=0}.
\]

Energy is unshifted: each equal-color bond costs \(J\), while each vertex carrying label zero contributes \(-h\). The result is strictly zero-temperature and finite-graph; no thermodynamic-limit phase transition is asserted.

## Proof

Define the two integer statistics \(f(\sigma)=\sum_{pq\in E}\mathbf1_{\sigma_p=\sigma_q}\) and \(k(\sigma)=\sum_p\mathbf1_{\sigma_p=0}\). For each \(k\in\{0,\ldots,11\}\), let \(m_k=\min_{\sigma:k(\sigma)=k}f(\sigma)\), and let \(c_k\) count the configurations attaining this minimum.

There is an exact six-spin factorization of the complete counting polynomial \(P(z,t)=\sum_\sigma z^{k(\sigma)}t^{f(\sigma)}\). Write \(a=\sigma_w\), \(c_i=\sigma_{v_i}\), with indices modulo five. Conditional on \(a,c_0,\ldots,c_4\), the five shadow spins are independent in this polynomial, giving

\[
P(z,t)=\sum_{a,c_0,\ldots,c_4\in\{0,1,2\}}
z^{\mathbf1_{a=0}+\sum_i\mathbf1_{c_i=0}}
t^{\sum_i\mathbf1_{c_i=c_{i+1}}}
\prod_{i=0}^{4}\left(\sum_{b=0}^{2}
z^{\mathbf1_{b=0}}
t^{\mathbf1_{b=a}+\mathbf1_{b=c_{i-1}}+\mathbf1_{b=c_{i+1}}}\right).
\]

The factorization is an identity term by term: the prefactor counts the pentagon bonds and occupied apex/pentagon vertices, and the local factors count all ten shadow-to-pentagon bonds, five apex-to-shadow bonds and all shadow-spin occupancies. It sums exactly \(3^6=729\) assignments of the retained six spins; expansion of its five three-term factors accounts for every one of the \(3^{11}=177147\) complete configurations.

Exact nonnegative-integer coefficient extraction gives the full lower boundary and multiplicities:

| \(k\) | \(m_k\) | \(c_k\) |
|---:|---:|---:|
| 0 | 4 | 10 |
| 1 | 3 | 160 |
| 2 | 1 | 30 |
| 3 | 1 | 240 |
| 4 | 1 | 310 |
| 5 | 1 | 80 |
| 6 | 2 | 60 |
| 7 | 4 | 40 |
| 8 | 7 | 40 |
| 9 | 11 | 20 |
| 10 | 15 | 2 |
| 11 | 20 | 1 |

This table is not a sample: the displayed polynomial is a complete finite sum, and the attached exact-arithmetic verifier evaluates every coefficient by two separately organized computations. Its nonnegative coefficients show that for each occupancy no configuration can have fewer frustrated bonds than the displayed \(m_k\); each positive \(c_k\) certifies attainability.

For fixed \(x=h/J\), minimizing the Hamiltonian is exactly minimizing \(m_k-kx\) over these twelve cases. Comparing the twelve rational-affine lines leaves precisely the eight lines displayed under *Finding*. Their strict active intervals have the listed \(k\) values. At each critical point, sum \(c_k\) over all lines achieving the common minimum. In particular the four occupancies \(k=2,3,4,5\) coexist at zero field, yielding \(30+240+310+80=660\). The other six critical counts follow identically. Summing the exact coefficient counts for one-defect configurations by edge location gives the three edge-orbit totals stated above.

## Verification

Run `python3 verify_groetzsch.py` with standard Python 3; no optional packages or external data are used. The program independently (i) iterates over all \(3^{11}\) complete colorings, maintaining the complete bivariate coefficient table and single-defect edge supports, and (ii) computes the same table by the independent six-spin local-factor expansion. It asserts equality of **all** polynomial coefficients, not merely of the minima; then checks the twelve-row boundary table, seven critical multiplicities, eight strict regimes and zero-field edge-orbit totals. Both calculations use exact integers and exact rational arithmetic for field crossings.

## Relationship to prior work

The Grötzsch graph and its four-chromatic, triangle-free character are classical. Husfeldt (2015, p. 20, Fig. 11) illustrates a **four-label** randomized-rounding assignment with one monochromatic edge. That illustration is not a three-state Potts assignment and does not establish that three labels suffice with only one defect. Classical four-chromaticity gives the lower bound of one defect for three labels; the explicit three-state attaining configurations and their counts here follow from the complete coefficient evaluation. Chang and Shrock (2009), Chang and Shrock (2010), and Shrock and Xu (2010) develop field-dependent Potts partition functions and weighted proper colorings, while Ellis-Monaghan and Moffatt (2010) give a general graph-polynomial representation. They establish the **general formal machinery**, not the evaluated Grötzsch three-state magnetic ground-state table or the exact coexistence/edge-orbit multiplicities reported here.

A proper three-coloring polynomial vanishes identically for this four-chromatic graph. Consequently its weighted proper-coloring specializations alone cannot yield the nonzero one-defect ground-state multiplicities: the finite positive exchange-energy spectrum must be retained before taking the zero-temperature, fixed-field limit. The present claim concerns this explicitly evaluated finite case, not discovery of the underlying Potts representation or of the classical four-chromatic obstruction. A prior unindexed equivalent enumeration remains possible.

## Limitations

All field thresholds rely on equal positive antiferromagnetic bonds and a single global preferred-color field. Changing edge strengths or assigning distinct site fields can change the result. The theorem is for the one graph \(\mu(C_5)\); no formula for larger Mycielski graphs, no finite-temperature partition-function evaluation, and no bulk phase transition is claimed. Independent scientific audit and exhaustive historical-priority certification have not been performed.

## References

1. S.-C. Chang and R. Shrock, *Some Exact Results on the Potts Model Partition Function in a Magnetic Field*, arXiv:0907.0777, first submitted 2009-07-04. https://arxiv.org/html/0907.0777v2
2. S.-C. Chang and R. Shrock, *Weighted Graph Colorings*, arXiv:0908.2375, first submitted 2009-08-17. https://arxiv.org/abs/0908.2375
3. R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, arXiv:1009.1182, first submitted 2010-09-07. https://arxiv.org/abs/1009.1182
4. J. A. Ellis-Monaghan and I. Moffatt, *The Tutte-Potts connection in the presence of an external magnetic field*, arXiv:1005.5470, first submitted 2010-05-29. https://arxiv.org/html/1005.5470v2
5. T. Husfeldt, *Graph colouring algorithms*, in *Topics in Chromatic Graph Theory* (2015), pp. 277–303, especially p. 20, Fig. 11. https://thorehusfeldt.com/wp-content/uploads/2010/08/gca.pdf
