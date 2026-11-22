# Arithmetic period inflation and Jordan-totient laws for cyclic difference lifts

## Finding

Fix an integer alphabet modulus \(\kappa\ge 2\) and stride \(d\ge 1\). On bi-infinite configurations over \(\mathbb Z/\kappa\mathbb Z\), define the permutative difference code
\[
(\eta x)_i=x_{i+d}-x_i\pmod{\kappa}.
\]
For any target word \(y=(y_0,\ldots,y_{n-1})\) of length \(n\ge1\), interpreted periodically, set \(g=\gcd(n,d)\), \(b=d/g\), and define its \(g\) cyclic residue sums
\[
S_r=\sum_{\substack{0\le j<n\\j\equiv r\pmod{g}}}y_j\pmod{\kappa}
\quad (0\le r<g),\qquad
m=\frac{\kappa}{\gcd(\kappa,S_0,\ldots,S_{g-1})}.
\]
Here the greatest common divisor uses arbitrary integer representatives of the residues, and \(m\) is their vector's additive order. For every integer \(t\ge1\), the number \(F_y(t)\) of periodic lifts of \(y\) fixed by spatial shift through \(nt\) coordinates is exactly
\[
\boxed{F_y(t)=
\begin{cases}
\kappa^{g\gcd(t,b)},&m\mid t/\gcd(t,b),\\
0,&\text{otherwise}.
\end{cases}}
\]
In particular the **least admissible period multiplier** is
\[
\boxed{t_*(y)=m\prod_{p\mid m}p^{v_p(b)},}
\]
where the product is over distinct prime divisors \(p\) of \(m\), with the empty product equal to one. Every one of the \(\kappa^d\) bi-infinite lifts is periodic with period dividing \(n\kappa b\).

When \(n\) is the *least* period of \(y\), the exact number of lifts with least period \(nt\) is
\[
\boxed{P_y(t)=\sum_{u\mid t}\mu(t/u)F_y(u),}
\]
and the number of spatial shift orbits lying above the orbit of \(y\), with lift least period \(nt\), is \(P_y(t)/t\). The only potentially nonzero \(P_y(t)\) have \(t\mid\kappa b\).

Finally, let the \(n\) target coordinates be independent uniform elements of \(\mathbb Z/\kappa\mathbb Z\), **without conditioning on primitive period**. For each divisor \(a\mid\kappa\), the probability that the least admissible multiplier is
\(a\prod_{p\mid a}p^{v_p(b)}\) equals the Jordan-totient mass
\[
\boxed{\Pr(m=a)=\frac{J_g(a)}{\kappa^g},\qquad
J_g(a)=a^g\prod_{p\mid a}(1-p^{-g}).}
\]
In particular, exactly a fraction \(\kappa^{-g}\) of all length-\(n\) targets admit an \(n\)-periodic lift. These are exact finite-length statements, not asymptotic approximations.

## Assumptions and scope

All moduli, strides and word lengths are arbitrary positive integers in the stated ranges; no primality, coprimality or mixing assumption is made. A target's displayed length need not be primitive for the fixed-point formula or the random-target law. The Möbius least-period and orbit formula **does** assume that the displayed length is the target's least period. A lift means a bi-infinite sequence satisfying the difference equation at every integer coordinate, not merely an arbitrary solution on a single finite ring.

## Proof

**1. Cyclic decomposition.** Fix \(t\ge1\) and put \(N=nt\). Periodic lifts fixed by shift \(N\) are precisely solutions of \(x_{i+d}-x_i=y_{i\bmod n}\) for \(i\in\mathbb Z/N\mathbb Z\). Translation by \(d\) partitions this finite cyclic group into
\[
G=\gcd(N,d)=g\gcd(t,b)=gh
\]
directed cycles, each containing \(N/G\) indices. Here \(h=\gcd(t,b)\) and \(\gcd(n/g,b)=1\).

**2. Compatibility of cycles.** A fixed cycle of translation by \(d\) is one residue class modulo \(G\), possibly visited in a different order. The sum of the periodically repeated target over that class equals \((t/h)S_r\), where \(r\) is its residue modulo \(g\). Indeed, for each original position \(j\bmod n\) in the class \(r\bmod g\), among its \(t\) repetitions exactly \(t/h\) positions fall into each of the \(h\) lifts of that class modulo \(G\): the repeated positions advance by \(n\), whose image modulo \(G/g=h\) is coprime to \(h\) because \(\gcd(n/g,b)=1\). Thus a cyclic difference recurrence is solvable exactly when all its target sums vanish, equivalently when \(m\mid t/h\). In the solvable case, each of the \(G\) disjoint cycles has precisely \(\kappa\) choices for the initial value, hence exactly \(\kappa^G\) solutions. This proves the first boxed identity.

**3. Least multiplier and complete orbit spectrum.** For a prime \(p\mid m\), the divisibility \(m\mid t/\gcd(t,b)\) requires and is equivalent, at \(p\), to \(v_p(t)\ge v_p(m)+v_p(b)\). There are no constraints at primes not dividing \(m\), proving the formula for \(t_*\). The difference recurrence uniquely extends any \(d\) initial symbols in both time directions, so the total number of lifts is \(\kappa^d\). At \(t=\kappa b\) we have \(h=b\), \(G=d\), and \(m\mid\kappa\), hence \(F_y(\kappa b)=\kappa^d\). All lifts therefore have an \(n\kappa b\)-period.

If \(y\) has least period \(n\), every lift's least period is a multiple of \(n\), because the code commutes with shifts. Consequently \(F_y(t)=\sum_{u\mid t}P_y(u)\), and Möbius inversion gives the displayed least-period formula. An orbit of length \(nt\) encounters the fixed indexed target \(y\) exactly \(t\) times, at shifts divisible by \(n\), so the number of such shift orbits is \(P_y(t)/t\). Since every lift period divides \(n\kappa b\), \(P_y(t)=0\) unless \(t\mid\kappa b\).

**4. Exact random-target law.** The \(g\) disjoint residue classes each contain at least one freely uniform target coordinate. Their sums \(S_r\) are therefore mutually independent and uniform in \(\mathbb Z/\kappa\mathbb Z\). For each divisor \(a\mid\kappa\), the number of vectors of additive order exactly \(a\) in this \(g\)-fold product is \(J_g(a)\): the subgroup killed by \(a\) has \(a^g\) elements, and Möbius inversion over divisors gives \(J_g(a)=\sum_{c\mid a}\mu(a/c)c^g\), equivalent to the displayed product. The order of \((S_r)_r\) is exactly \(m\), proving the mass formula and, at \(a=1\), the \(\kappa^{-g}\) same-period proportion. Distinct divisors \(a\) have distinct least-multiplier values, since the \(p\)-adic exponent of \(t_*\) is \(v_p(a)+v_p(b)\) when \(p\mid a\) and zero otherwise.

## Verification

Run `python3 checker.py` from the extracted package. The standard-library-only checker enumerates all periodic target words with primitive displayed period for 1,484 parameter/target cases; independently enumerates 81,090 complete finite preimage fibers; checks all divisor fixed-point and Möbius least-period counts; and confirms the Jordan-totient output distribution by enumerating every target on 95 further parameter triples. These finite checks support—but do not replace—the all-parameter proof above. Two exact examples: for \((\kappa,n,d,y)=(3,1,4,(1))\), the primitive lift populations at multipliers \(3,6,12\) are \(3,6,72\). For \((2,1,4,(1))\), all 16 lifts have least period \(8\).

## Relationship to prior work

Kang and Jäger's 2026 work studies finite permutative lifts of subshifts, including difference-type codes and associated prefix permutation dynamics. Its focus is minimality and unique ergodicity for aperiodic substitution systems, rather than the exact distribution of spatial period multipliers across finite cyclic targets. The present code is their natural difference-code family examined in the opposite, periodic full-shift regime. This result does not assert minimality of such lifts.

Mariot, Leporati, Dennunzio and Formenti (2017) give a general de Bruijn-graph method to compute preimage periods and multiplicities for surjective cellular automata, and specialize linear bipermutive automata via recurring sequences and finite-ring decompositions. Their general algorithm applies in principle to the difference code here, so computing preimage periods or establishing that they are multiples of the target period is **not** claimed as new. The distinction here is the explicit gcd-and-vector-order formula valid simultaneously for every modulus, stride, period and target, plus the exact unconditional Jordan-totient distribution and the direct all-period Möbius census. This is a restricted explicit classification, not a new general algorithm.

## Limitations

This class is a particularly simple additive family and the formula does not apply to arbitrary nonlinear permutative codes. The random-target law is unconditional: conditioning on the target's displayed length being primitive changes the distribution. More general finite-ring linear codes are algorithmically tractable by earlier methods, so any priority claim is restricted to these explicit all-parameter identities and their arithmetic distribution. The possibility of an unindexed historical equivalent remains. No independent mathematical audit has been performed.

## References

- Z. Kang and T. Jäger, *Lifts of strictly ergodic subshifts by permutative sliding block codes*, arXiv:2609.01140v1, first publicly submitted 2026-09-01, https://arxiv.org/abs/2609.01140.
- L. Mariot, A. Leporati, A. Dennunzio and E. Formenti, *Computing the periods of preimages in surjective cellular automata*, Natural Computing 16 (2017), 367–381, https://doi.org/10.1007/s11047-016-9586-x; author postprint https://lucamariot.org/files/papers/mldf_naco_2017_postprint.pdf.
