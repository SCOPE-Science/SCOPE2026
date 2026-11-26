# Exact coincidence of exclusion and noncollision dynamics at the packing boundary

## Finding

Consider a set of \(n\ge3\) sites and \(2\le k\le n-1\) labeled particles. Each particle independently jumps from site \(i\) to distinct site \(j\) at rate \(q_{ij}>0\). Two natural collision-free processes are: (a) **exclusion**, which suppresses jumps onto occupied sites; (b) **noncollision conditioning**, the infinite-horizon limit of the independent-particle law conditioned to avoid collisions through time \(T\), as \(T\to\infty\). Set
\[
 w_{ij}=q_{ij}+q_{ji}\quad(i\ne j),\qquad d_i=\sum_{j\ne i}w_{ij}.
\]
The following are equivalent, for fixed \(n,k\):

1. Noncollision conditioning and exclusion have identical path laws from every collision-free labeled initial configuration.
2. The first-collision survival function of independent walkers is \(\Pr_x(\tau>t)=e^{-\lambda t}\) with the **same** \(\lambda>0\) for every collision-free initial configuration \(x\).
3. The induced symmetrized weight \(\kappa(S)=\sum_{\{i,j\}\subset S}w_{ij}\) is independent of the occupied \(k\)-set \(S\).
4. The following occupancy-dependent structural condition holds:
   - If \(2\le k\le n-2\), then **all** the \(w_{ij}\) are equal to one constant \(c>0\).
   - If \(k=n-1\), then **all** weighted degrees \(d_i\) are equal, without requiring the individual \(w_{ij}\) to be equal.

In the first case \(\lambda=c\binom{k}{2}\). In the second case \(\lambda=\frac{n-2}{2}d\), where \(d\) is the common weighted degree. For \(k=n-1\), the positive solutions form a relatively open cone of dimension \(\binom n2-n+1\) in the space of symmetrized edge weights, rather than the one-dimensional family forced at all lower occupancies. For \(n\ge4\) this contains genuinely nonuniform models.

There is an exact probabilistic refinement. Whenever the conditions hold, the original independent-walker process up to its first collision can be generated from a full exclusion trajectory by running an **independent** exponential clock of rate \(\lambda\) and, when it rings, choosing the pair of particle labels \(a<b\) with conditional probability
\[
 \Pr(J=\{a,b\}\mid Y_{\tau-}=x)
   =\frac{w_{x_a x_b}}{\lambda}.
\]
Thus collision time is independent of the exclusion trajectory, even at occupancy \(k=n-1\) with unequal \(w_{ij}\); the identity of the colliding pair can still be configuration-dependent. When all \(w_{ij}=c\), the pair mark is uniform over the \(\binom{k}{2}\) pairs and independent of that trajectory and the clock.

## Assumptions and scope

All rates \(q_{ij}\) are finite and strictly positive for every ordered pair \(i\ne j\); jumps of different particles are independent before the first collision. There are no self jumps. Initial sites are pairwise distinct. The exponential survival statement refers to the initial configuration, not an assertion that the independent walkers avoid collision with positive probability forever (they do not on this finite irreducible space). Noncollision conditioning means the standard finite-state \(Q\)-process: on each fixed time window, the limit as the conditioning horizon tends to infinity.

All formulas concern the **symmetrized** rates \(w_{ij}\), not symmetry of the directed generator: strong nonreversible circulation is allowed. For \(n=3\), the only allowed occupancy \(k=2=n-1\) has the weighted-degree condition, which in that case already forces constant \(w_{ij}\).

## Proof

**1. Generator and collision intensity.** Let \(\Omega\) be the finite set of ordered \(k\)-tuples of distinct sites, and let \(L_{\mathrm{ex}}\) be the conservative generator suppressing moves to occupied sites. The generator of the independent walkers killed at their first collision is
\[
 L_{\mathrm{kill}}=L_{\mathrm{ex}}-\operatorname{diag}(\kappa),
 \qquad
 \kappa(x)=\sum_{1\le a<b\le k}
       (q_{x_ax_b}+q_{x_bx_a})
       =\sum_{\{i,j\}\subset S(x)}w_{ij}.
\]
The first equality follows because for each occupied unordered pair, a collision jump can be made in either direction. The second is independent of labels. All allowed rates are strictly positive, hence the exclusion chain on ordered tuples is irreducible: with one spare site, successive moves into the spare site can realize transpositions and generate all placements, and additional spare sites cannot destroy connectivity.

**2. Equivalence with constant killing.** Since \(L_{\mathrm{kill}}\) is a finite irreducible Metzler matrix, its leading eigenvalue is simple, say \(-\rho\), with strictly positive right eigenvector \(h\). The limiting noncollision-conditioned chain is the Doob transform with off-diagonal rates
\[
 L_{\mathrm{nc}}(x,y)=L_{\mathrm{ex}}(x,y)\frac{h(y)}{h(x)}
 \qquad(x\ne y).
\]
If its law equals exclusion from every state, these off-diagonal rates agree. Positivity of every allowed exclusion transition and irreducibility force \(h\) to be constant throughout \(\Omega\). Therefore \(L_{\mathrm{kill}}\mathbf1=-\rho\mathbf1\), which is equivalent to \(\kappa\equiv\rho\). Conversely, if \(\kappa\equiv\lambda\), then
\[
 e^{tL_{\mathrm{kill}}}=e^{-\lambda t}e^{tL_{\mathrm{ex}}}.
\]
The killed semigroup gives both \(\Pr_x(\tau>t)=e^{-\lambda t}\) for all \(x\), and equality of the exclusion and conditioned-on-survival laws on every time interval \([0,t]\). Passing to longer conditioning horizons gives the same \(Q\)-process. Conversely, if the common exponential survival law holds, differentiating at \(t=0\) yields \(\kappa(x)=\lambda\) for each \(x\). Thus (1), (2), (3) are equivalent.

**3. Rigidity below one vacancy.** Suppose \(2\le k\le n-2\) and \(\kappa(S)\) is the same for all \(k\)-sets. For any distinct \(a,b\), let \(U\) be the other \(n-2\) sites. Comparing \(T\cup\{a\}\) with \(T\cup\{b\}\) for every \((k-1)\)-subset \(T\subset U\) gives
\[
 \sum_{u\in T}(w_{au}-w_{bu})=0.
\]
Because \(1\le k-1\le |U|-1\), swapping one element of \(T\) while retaining the others shows all the differences \(w_{au}-w_{bu}\) (as \(u\) varies in \(U\)) coincide. The displayed zero sum then forces each difference to be zero. Consequently, for every third site \(u\), all weights incident to \(u\) are equal. Symmetry \(w_{ij}=w_{ji}\) propagates this equality to all unordered site pairs, so \(w_{ij}=c\). The converse is immediate, and its common collision intensity is \(c\binom{k}{2}\).

**4. The last-vacancy exception.** If \(k=n-1\), every occupied set is the complement of one vacant site \(v\). With \(W=\sum_{i<j}w_{ij}\),
\[
 \kappa(\{1,\dots,n\}\setminus\{v\})=W-d_v.
\]
This is constant precisely when all \(d_v=d\). Since \(2W=nd\), its value is \((n-2)d/2\). The linear map from \(\binom n2\) undirected edge weights to \(n\) weighted degrees has full row rank for \(n\ge3\): if a linear combination of its rows vanishes, its coefficient on edge \(\{i,j\}\) is \(a_i+a_j=0\) for all \(i<j\), forcing every \(a_i=0\). Therefore equal degrees impose \(n-1\) independent linear conditions and leave dimension \(\binom n2-n+1\). Strict positivity picks a nonempty relatively open cone.

For an explicit nonuniform example take \(n=4\), put
\[
 w_{12}=w_{34}=3,\qquad
 w_{13}=w_{24}=2,\qquad
 w_{14}=w_{23}=1,
\]
and choose \(q_{ij}=w_{ij}/2\). Each weighted degree is \(6\). Three particles have the common collision rate \(6\) and identical exclusion and noncollision-conditioned laws, while two particles have collision intensities in \(\{1,2,3\}\) and the laws differ. For every \(n\ge4\) a positive uniform baseline can similarly be perturbed along a four-cycle by adding \(\varepsilon,-\varepsilon,\varepsilon,-\varepsilon\) to its consecutive edge weights; weighted degrees remain equal but the weights become nonuniform.

**5. Collision-clock representation.** For any fixed exclusion configuration \(x\), the independent walkers' aggregate suppressed transition rate onto occupied sites equals \(\kappa(x)\), and the suppressed transition rate involving the unordered label pair \(\{a,b\}\) is \(w_{x_ax_b}\). The standard competing-jump construction therefore gives the independent-walker path through its first collision by running an exclusion path and an additional killing mechanism with these rates. When \(\kappa\equiv\lambda\), this killing mechanism is a clock of constant intensity \(\lambda\), independent of the exclusion path. Given the path at its ringing time, selecting the label pair with probability \(w_{x_ax_b}/\lambda\) reproduces the correct individual pair-specific killing intensities. The formula is a probability distribution because its numerator sums to \(\lambda\). For uniform \(w\), all pair probabilities equal \(1/\binom{k}{2}\), independently of the path.

## Verification

The accompanying standalone Python program `verify.py` builds the \(k\)-subset versus edge incidence matrices exactly, computes their rational ranks for \(3\le n\le8\) and every admissible \(k\), and tests the kernel dimensions in the two regimes. It constructs positive degree-regular but nonuniform edge weights by four-cycle perturbation and checks their collision intensities. Independently, it constructs finite labeled exclusion and killed generators, computes the Perron Doob transform numerically and checks equality/inequality for uniform and nonuniform examples; in equality cases it verifies the finite-horizon killed-semigroup factorization by matrix exponentiation. The 45 tests reported in its execution passed. Matrix computations illustrate and detect mistakes in the finite examples; the infinite-horizon statement and all-parameter classification follow from the proof above, not from enumeration.

Run with `python verify.py` in a Python 3 environment containing NumPy, SciPy, and SymPy. The script has no external data dependencies.

## Relationship to prior work

Shiatis (2026), *Exclusion vs Noncolliding Dynamics in Markov Processes*, arXiv:2610.00741v1, Theorem 1.4, supplies the general exponential-martingale change of measure with configuration-dependent killing intensity. Its proof also identifies the Doob-transform off-diagonal rates (Lemma 2.2 and Proposition 2.1). Those general mechanisms are known and explicitly used here; they are **not** claimed as new. The result here instead provides a complete inverse classification on all strictly positive finite directed site generators, for each occupancy, identifying the exceptional density \(k=n-1\), the exact dimension of its anisotropic family, and the independent-clock versus pair-mark distinction. The inspected text does not state this classification or its packing-boundary example.

Johnston and Shiatis (2025), *The Integrable Snake Model*, arXiv:2501.15483v4, Theorem 2.9 and Section 7, develops a traffic-based change of measure for nearest-neighbor ASEP on a ring. Its special ring model does not provide the positive complete directed-rate inverse classification here. General finite-state Perron–Frobenius and incidence-matrix facts are background tools, not asserted as original results.

## Limitations

The result assumes all directed rates strictly positive and a finite set of sites. For sparse jump graphs the labeled exclusion state space may have multiple communicating classes, so extra hypotheses and distinct classifications may be necessary. The collision mark refers to the **unordered pair of particle labels**, not the direction of the collision jump. The conditional independence of the exponential clock applies to the canonical exclusion/killing coupling and need not imply any unrelated coupling property of arbitrary processes. The result does not determine stationary observables or long-time mixing rates of exclusion. While no directly matching inverse classification was found in the cited texts or targeted searches, an equivalent formulation in older interacting-particle or weighted-incidence literature remains possible; an independent audit has not been performed.

## References

1. R. Shiatis, *Exclusion vs Noncolliding Dynamics in Markov Processes*, arXiv:2610.00741v1 (first public 2026-09-30), https://arxiv.org/abs/2610.00741 ; especially Theorem 1.4, Proposition 2.1, Lemma 2.2 and Section 2.
2. S. G. G. Johnston and R. Shiatis, *The Integrable Snake Model*, arXiv:2501.15483v4 (2025), https://arxiv.org/abs/2501.15483 ; especially Theorem 2.9 and Section 7.
3. S. D. Jacka and G. O. Roberts, *Weak convergence of conditioned processes on a countable state space*, J. Appl. Probab. **32** (1995), 902–916. Background on conditioned Markov processes, cited in Reference 1.
