# Parity-locked vacancy plateaux on antiferromagnetic spin-one circular ladders

## Finding

Let the graph be the circular ladder \(C_n\square K_2\) for any integer \(n\ge3\). Each vertex carries a spin in \(\{-1,0,1\}\), with positive antiferromagnetic leg coupling \(J>0\), positive rung coupling \(R>0\), zero longitudinal field and arbitrary real crystal field \(D\). With \(r=R/J\), \(d=D/J\), and \(K\) the number of occupied spins, its complete zero-temperature ground-state classification is as follows.

**Even circumference.** There are precisely two fully occupied bipartite checkerboard ground states for \(d<1+r/2\), exactly one all-vacant ground state for \(d>1+r/2\), and precisely those three states at equality. The ground energy divided by \(J\) is
\[
\min\{2nd-(2+r)n,\;0\}.
\]

**Odd circumference.** Define \(d_-=r/2\) and \(d_+=r/2+(n-2)/(n-1)\). The ground energy divided by \(J\) is exactly
\[
\min\{2nd-(2+r)n+4,\;(2n-2)d-(2+r)n+4+r,\;0\}.
\]
For \(d<d_-\), there are exactly \(2n\) fully occupied ground states, each with one frustrated horizontal bond on each rim at the same cyclic position and all rungs oppositely signed. For \(d_-<d<d_+\), there are exactly \(2n\) ground states having the two spins on **one entire rung vacant** and all other bonds oppositely signed. For \(d>d_+\), the all-vacant state is uniquely optimal. There are exactly \(4n\) states at \(d=d_-\) and \(2n+1\) at \(d=d_+\), with no further minimizing configurations. The intermediate interval has width \((n-2)/(n-1)\), independent of the positive rung coupling.

## Assumptions and scope

Write the spins as \(s_{a,i}\in\{-1,0,1\}\), where \(a\in\{0,1\}\), \(i\in\mathbb Z/n\mathbb Z\). Leg edges connect \((a,i)\) to \((a,i+1)\) and rungs connect \((0,i)\) to \((1,i)\). Each undirected bond is counted once; for \(n=3\) each rim is a simple triangle. The Hamiltonian is
\[
\mathcal H=J\sum_{a,i}s_{a,i}s_{a,i+1}+R\sum_i s_{0,i}s_{1,i}+D\sum_{a,i}s_{a,i}^{2}.
\]
The result is a finite-volume zero-temperature statement for every integer \(n\ge3\), every \(J,R>0\), and every \(D\in\mathbb R\); it does not invoke a thermodynamic limit. Ground-state counts refer to labeled vertices and distinct spin configurations (not to symmetry orbits). A spin zero is a vacancy.

## Proof

Set \(K=\sum_{a,i}s_{a,i}^{2}\) and \(z=2n-K\). Define the nonnegative frustrated-bond functional
\[
F=\sum_{a,i}(s_{a,i}+s_{a,i+1})^{2}
 +r\sum_i(s_{0,i}+s_{1,i})^{2}.
\]
Every vertex has weighted degree \(2+r\), so completing the square gives the exact identity
\[
\mathcal H/J=F/2+(d-1-r/2)K.\tag{1}
\]
On the connected prism, \(F=0\) implies either all spins vanish or every spin is nonzero and its neighbors have opposite signs. Consequently, in even circumference the only zero-cost configurations are the two checkerboards and the empty configuration; in odd circumference, only the empty configuration has \(F=0\).

**Even case.** At \(d=1+r/2\), identity (1) reduces to \(\mathcal H/J=F/2\), proving the three-way degeneracy above. For smaller \(d\), the maximum-occupancy zero-cost states, the two checkerboards, minimize (1) strictly; for larger \(d\), the empty configuration uniquely minimizes it. The stated energy follows.

**Odd case, first boundary.** At \(d_-=r/2\), identity (1) becomes \(\mathcal H/J=F/2-K\). We prove \(F+2z\ge8\) with equality precisely in the two claimed families. For \(z=0\), each occupied odd rim has at least one equal-spin bond with squared cost \(4\), so \(F\ge8\); equality requires exactly one such bond per rim and every rung to be opposite-signed, forcing the two rim defects to occupy the same position. There are \(2n\) configurations. For \(z=1\), the intact odd rim costs at least \(4\) and the other rim has two occupied–vacant boundary edges costing at least \(2\), hence \(F+2z\ge8\), with strict inequality because its one partially vacant rung has positive cost \(r>0\). For \(z=2\), if both zeros occur on the same rim, the other intact odd rim costs at least \(4\) and the interrupted rim has at least two occupied–vacant boundaries, so \(F\ge6\). If each rim has one zero, both rims have at least two boundary edges, so \(F\ge4\). Equality \(F=4\) demands all rungs have zero squared cost; since \(r>0\), the two vacant positions coincide, and the surviving even-length open ladder is the unique checkerboard up to overall sign. This gives another \(2n\) configurations. For \(z=3\), each rim either has occupied–vacant boundaries or is entirely occupied and odd-frustrated; inspection of these exhaustive cases gives total horizontal cost at least \(4\), whence \(F+2z\ge10\). For \(z=4\), equality would require \(F=0\), impossible with both occupied and vacant vertices on a connected graph. For \(z\ge5\), \(F+2z>8\). Thus \(\mathcal H/J\ge4-2n\), with exactly the \(4n\) specified equality cases.

**Odd case, second boundary.** At \(d_+=1+r/2-1/(n-1)\), (1) becomes \(\mathcal H/J=F/2-K/(n-1)\). We prove \(F\ge2K/(n-1)\), with equality only at the empty state and the single-vacant-rung checkerboards. If \(K=0\), both sides vanish. If \(1\le K\le n-1\), either both rims are partially occupied, contributing at least four horizontal boundary edges, or one rim is empty and the other is partially occupied, contributing at least two boundary edges plus strictly positive rung cost; either way \(F>2K/(n-1)\). For \(n\le K\le2n-2\), if both rims are partially occupied, they contribute at least four horizontal boundary edges, hence \(F\ge4\ge2K/(n-1)\). Equality forces \(K=2n-2\), one zero on each rim, both zeros on the same rung (because \(R>0\)), and all other bonds alternating. If instead one rim is fully occupied, its odd-cycle frustration costs at least \(4\), giving strict inequality (when the other rim is nonempty but partial it adds at least two boundaries). At \(K=2n-1\), an intact odd rim contributes at least \(4\) and the interrupted rim at least \(2\), so \(F\ge6>2K/(n-1)\). At \(K=2n\), both odd rims contribute at least \(8>2K/(n-1)\). This proves the exact upper-boundary states and energy zero.

Finally, each configuration's energy is affine in \(d\), with slope \(K\) between \(0\) and \(2n\). The two certified boundary minima and their slope extremizers force the fully occupied family below \(d_-\), the paired-vacancy family between \(d_-\) and \(d_+\), and the empty family above \(d_+\), all strictly away from the boundaries. The three displayed energy branches and every degeneracy follow.

## Verification

The standalone program `verify_prism_dp.py` performs an exact rational periodic nine-column-state dynamic programming calculation for 300 parameter triples, covering \(3\le n\le12\), five positive rung ratios and fields below, at and above each transition. `verify_prism_bruteforce.py` independently enumerates every one of the \(3^{2n}\) labeled spin configurations for 48 parameter triples on \(n=3,4,5,6\). Both check not merely the minimum energy, but also the occupancy-resolved multiplicities. All checks passed. The all-size conclusion is proved by the inequalities above; finite experiments alone would not prove it. These commands reproduce the checks using Python's standard library:
```
python verify_prism_dp.py
python verify_prism_bruteforce.py
```

## Relationship to prior work

The antiferromagnetic Blume–Capel vacancy model and frustrated periodic chains are established. Pawłowski (2007) considers a square-lattice antiferromagnetic Blume–Capel model. Boudreault, Owerre and Paranjape (2016) study the single periodic spin chain, including odd-length frustrated configurations; these results do not, by themselves, prove that two coupled rims lock all vacancy positions for every strictly positive rung coupling. Strečka, Michaud and Mila (2013) analyze a different quantum Ising–Heisenberg ladder Hamiltonian with rung Heisenberg exchange and additional diagonal inter-rung terms. An exactly solvable sawtooth-chain study (2016) treats another graph geometry. The present statement isolates the coupling-independent **width** of the intermediate zero-temperature vacancy phase and proves its exact labeled multiplicity throughout the two-leg family. It does not claim novelty for the individual-chain or general Blume–Capel model.

## Limitations

The classification requires identical positive antiferromagnetic leg couplings, a strictly positive common rung coupling, classical spins in \(\{-1,0,1\}\), zero magnetic field, and an exactly circular ladder. The limit \(R\downarrow0\) is singular for degeneracies: with fully decoupled odd rims the defects and vacancies move independently; our counts deliberately exclude \(R=0\). Temperature-dependent phases, random couplings, quantum transverse terms, interacting vacancies, nonuniform crystal fields and infinite-volume statistical mechanics are not addressed. Full historical-priority confirmation beyond inspected sources has not been performed, and independent validation remains outstanding.

## References

- G. Pawłowski, *Multiphase structure of finite-temperature phase diagram of the Blume–Capel model. Wang–Landau sampling method*, arXiv:cond-mat/0703299 (first posted 2007-03-12). https://arxiv.org/abs/cond-mat/0703299
- J. Strečka, F. Michaud and F. Mila, *Exact Ground States of Frustrated Spin-1 Ising-Heisenberg and Heisenberg Ladders in a Magnetic Field*, arXiv:1305.6703 (first posted 2013-05-29). https://arxiv.org/abs/1305.6703
- C. Boudreault, S. A. Owerre and M. B. Paranjape, *The phase-diagram of the Blume-Capel-Haldane-Ising spin chain*, arXiv:1601.06195 (first posted 2016-01-22). https://arxiv.org/abs/1601.06195
- *Exactly solvable antiferromagnetic Blume-Capel model on a sawtooth chain*, Physical Review E 93, 052151 (2016). https://doi.org/10.1103/PhysRevE.93.052151
