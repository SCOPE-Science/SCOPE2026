# Three-color Potts trapping and geometric rare-seed nucleation on the Petersen graph

## Finding

Let \(P=KG(5,2)\) be the Petersen graph: its ten vertices are the two-element subsets of \(\{0,1,2,3,4\}\), with an edge joining two disjoint subsets. Give each vertex one of three named colors \(0,1,2\). In the strict energy-descent ferromagnetic Potts dynamics defined below, the following is an exact classification.

There are **579 absorbing colorings**, and their complete labeled color-population census is

| Terminal color-population multiset | Number of colorings | Number of agreeing edges |
|---|---:|---:|
| \((10)\) | 3 | 15 |
| \((5,5)\) | 36 | 10 |
| \((5,3,2)\) | 360 | 8 |
| \((4,3,3)\) | 180 | 7 |

For uniformly independent initial colors, the exact terminal probability of each population is

| Terminal population | Probability |
|---|---|
| \((10)\) | \(2556244649164229716154537/3686384171559531241800000\) |
| \((5,5)\) | \(944017439434911275737811/7372768343119062483600000\) |
| \((5,3,2)\) | \(63219526594545615967/371517679169516880000\) |
| \((4,3,3)\) | \(1372/164025\) |

Thus the probability of **nonconsensus trapping** is
\[
\Pr(\text{nonconsensus absorption})
=\frac{1130139522395301525645463}{3686384171559531241800000}
\approx0.3065712822647.
\]

A sharp mixed-minority nucleation law holds when seven vertices initially carry color \(0\), two distinct vertices \(u,v\) carry color \(1\), and one remaining vertex \(w\) carries color \(2\). Write \(a=\mathbf1_{u\sim v}\), and \(b=\mathbf1_{w\sim u}+\mathbf1_{w\sim v}\). The nonconsensus absorption probability is exactly
\[
\Pr(\text{nonconsensus}\mid u,v,w)=
\begin{cases}
11/270,&(a,b)=(0,1),\\
0,&\text{otherwise}.
\end{cases}
\]
Moreover, when this exceptional event occurs its terminal population is always \((5,5)\): the singleton color is eliminated. The five possible geometric classes have labeled counts \(90,120,30,60,60\), respectively for \((a,b)=(0,0),(0,1),(0,2),(1,0),(1,1)\). For a uniformly sampled placement of the two color-\(1\) sites and single color-\(2\) site among the ten vertices, the nonconsensus absorption probability is therefore exactly \(11/810\).

## Assumptions and scope

Define the energy \(H(\sigma)=-\sum_{\{i,j\}\in E(P)}\mathbf1_{\sigma_i=\sigma_j}\), in units of positive ferromagnetic coupling. Every *ordered* single-vertex recoloring \((i,c)\), \(c\ne\sigma_i\), has rate one if it strictly lowers \(H\); otherwise its rate is zero. Different allowed recolorings at the same vertex each contribute rate one. In particular, energy-neutral recolorings are **rejected**, unlike in some zero-temperature Glauber or Metropolis conventions. There are no external fields, no spontaneous mutations, and all clocks have these constant rates.

The terminal census is over all \(3^{10}=59049\) labeled colorings. The full absorption law uses the uniform distribution on these colorings. The geometric nucleation law conditions on the exact \((7,2,1)\) initial populations with the colors named as above. The result concerns only this ten-vertex graph and this precise strictly cooling dynamics.

## Proof

Let \(S(\sigma)=\sum_{\{i,j\}\in E(P)}\mathbf1_{\sigma_i=\sigma_j}\). At vertex \(i\), write \(n_i(c)\) for its number of neighbors of color \(c\). Recoloring \(i\) from \(a\) to \(c\) increases \(S\) by \(n_i(c)-n_i(a)\). Thus a move is allowed precisely when this difference is strictly positive, and the integer \(S\in\{0,1,\ldots,15\}\) increases by at least one at every move. Every trajectory has at most fifteen accepted changes and is eventually absorbed; there are no transient recurrent cycles.

A coloring is absorbing exactly when \(n_i(\sigma_i)\ge n_i(c)\) for every vertex and every color. Because the graph is cubic, each stable vertex either has at least two same-color neighbors, or has exactly one neighbor of each color. This is an elementary local test without probabilistic approximation.

We now give a finite exhaustive exact proof of the two numerical assertions. Enumerate the vertices as lexicographically ordered two-subsets, construct the fifteen edges by disjointness, and enumerate the integer codes \(0,\ldots,3^{10}-1\) in base three. The local test just stated assigns each of the \(59049\) states to either a terminal population or a list \(M(\sigma)\) of allowed successor states. The resulting terminal counts are exactly \(3,36,360,180\) in the table order. These counts are not inferred from a sample: the entire finite state set is examined.

For each terminal type \(T\), define \(h_T(\sigma)\) as its eventual absorption probability. The preceding strict-increase property proves that these values are uniquely determined by the finite backward recurrence
\[
h_T(\sigma)=
\begin{cases}
\mathbf1_{\sigma\text{ is terminal of type }T},& M(\sigma)=\varnothing,\\
|M(\sigma)|^{-1}\sum_{\tau\in M(\sigma)}h_T(\tau),&M(\sigma)\ne\varnothing.
\end{cases}
\]
The denominator is the number of rate-one enabled recolorings, **not** the number of distinct enabled vertices. All arithmetic is exact over rational numbers. Evaluating the recurrence on all \(59049\) states, followed by averaging over them, gives the four stated fractions. The code `verify_kneser.py` implements a recursive memoized evaluation, and `verify_pentagonal.py` independently constructs the graph as a pentagon, pentagram and five spokes, applies the global energy-improvement condition, and evaluates states in decreasing \(S\)-order. Both generate the same exact fractions and terminal counts; `EXACT_RESULTS.json` contains the resulting fractions.

For the mixed-minority claim, fix the seven background-color sites, a two-site second-color set \(\{u,v\}\), and singleton \(w\). There are \(\binom{10}{2}\cdot8=360\) possibilities for the three named minority sites. Exhaustively applying the same exact recurrence to all these states and grouping by their two adjacency invariants gives

| \((a,b)\) | Placements | Exact nonconsensus probability for each placement |
|---|---:|---:|
| \((0,0)\) | 90 | \(0\) |
| \((0,1)\) | 120 | \(11/270\) |
| \((0,2)\) | 30 | \(0\) |
| \((1,0)\) | 60 | \(0\) |
| \((1,1)\) | 60 | \(0\) |

The graph has no triangles, so \((1,2)\) is impossible. The exact recurrence also assigns zero probability to the three-color absorbing types from every \((7,2,1)\) initial coloring. Averaging the one nonzero class gives \((120/360)(11/270)=11/810\). This establishes the claimed sharp selection rule with every initial placement included.

## Verification

Run `python verify_kneser.py` and `python verify_pentagonal.py` with Python 3 from the directory containing these embedded files. Each standalone script emits exact JSON. Compare the keys `terminal_counts`, `uniform_initial_absorption`, `three_seed_geometry`, `three_seed_721_freeze_mean`, and `all_freezing` with the accompanying `EXACT_RESULTS.json`. Both algorithms enumerate all \(59049\) configurations; they construct the graph and generate transitions in substantially different ways. The finite proof uses exact `fractions.Fraction`, not Monte Carlo, floating-point tolerance, partial sampling, or a timeout assumption.

## Relationship to prior work

Derrida, Bray and Godrèche (1994), and Derrida, Hakim and Pasquier (1995), study zero-temperature multi-color Potts coarsening and persistence on one-dimensional lattices. Their q-state domain-wall rules and calculated persistence exponents do not specify the Petersen-graph strictly cooling absorbing-chain law here. Godrèche and Luck (2004) analyze the metastable attractor landscape for Ising dynamics, predominantly on chains and planar lattices. Baek, Ha and Jeong (2011/2012) examine Ising-like trapping on random graphs, not this three-color exact kinetic distribution. Later low-temperature Potts tunneling work on tori likewise has different geometry and thermal transitions.

The established proper-three-coloring count of the Petersen graph (OEIS A296913) is an antiferromagnetic equilibrium coloring invariant, not a count of strictly cooling ferromagnetic local minima. An optical three-state Potts study includes the Petersen graph but uses an antiferromagnetic optimization objective and continuous oscillator kinetics, so its histograms do not determine this Markov chain. A previously established exact two-spin Petersen freezing law uses two colors and cannot imply the three-color absorbing families or the asymmetric \((7,2,1)\) nucleation probability.

## Limitations

The exact law depends on the *per-recoloring* rate-one convention and strict rejection of energy ties. It must not be substituted for conventional zero-temperature Glauber dynamics that permits neutral flips, finite-temperature Metropolis sampling, or synchronous majority rules. It proves nothing for larger cubic graphs, nonuniform couplings, external fields, other initial-color distributions beyond the indicated conditionings, or generalized update rates. A historical equivalent computation outside the examined indexed material may exist; the result has not received independent scientific validation.

## References

1. B. Derrida, A. J. Bray and C. Godrèche, “Non-trivial exponents in the zero temperature dynamics of the 1D Ising and Potts models,” *J. Phys. A* **27** (1994), L357–L361. https://doi.org/10.1088/0305-4470/27/11/002.
2. B. Derrida, V. Hakim and V. Pasquier, “Exact first-passage exponents of 1D domain growth: relation to a reaction diffusion model,” 1995, https://arxiv.org/abs/hep-th/9505066.
3. C. Godrèche and J. M. Luck, “Metastability in zero-temperature dynamics: Statistics of attractors,” 2004, https://arxiv.org/abs/cond-mat/0412077.
4. Y. Baek, M. Ha and H. Jeong, “Absorbing states of zero-temperature Glauber dynamics in random networks,” 2011 preprint, https://arxiv.org/abs/1112.5927.
5. G. Bet, A. Gallo and F. R. Nardi, “Critical Configurations and Tube of Typical Trajectories for the Potts and Ising Models with Zero External Field,” *J. Stat. Phys.* **184** (2021), art. 30. https://doi.org/10.1007/s10955-021-02814-1.
6. OEIS A296913, “Number of ways to properly color the Petersen graph using n colors,” https://oeis.org/A296913.
7. M. Honari-Latifpour and M.-A. Miri, “Optical Potts machine through networks of three-photon down-conversion oscillators,” *Nanophotonics* **9** (2020), 4199–4205. https://doi.org/10.1515/nanoph-2020-0256.
