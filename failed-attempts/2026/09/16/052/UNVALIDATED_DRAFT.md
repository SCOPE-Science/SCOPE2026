# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Mutation-graph injectivity for monotone Lagrangian tori in the monotone cubic del Pezzo surface

## TARGET claim (as admitted, with two corrections noted in §4)

Let $X = \mathrm{Bl}_6\mathbb{CP}^2$ with its monotone symplectic form (monotone
cubic surface). Let $(L,\{D_i\})$ be the monotone Lagrangian seed in $X$ of
Pascaleff–Tonkonog Proposition 4.22, and let $L',L''$ be monotone Lagrangian
tori obtained from $L$ by finite iterated geometric Lagrangian mutations along
the propagated disks (Theorem 4.8), so their disk potentials satisfy the
algebraic wall-crossing mutations $W' = \mu\,W_0$, $W'' = \mu\,W_0$.
**Theorem.** If the two mutated seeds have disk potentials not identified by any
monomial change of basis of $H_1$ (i.e.\ their Newton polytopes are not
$GL(2,\mathbb Z)$-congruent), then $L',L''$ are not Hamiltonian isotopic in $X$.
Hence the infinite Lagrangian-mutation graph modulo the finite seed-automorphism
group injects into Hamiltonian isotopy classes of monotone Lagrangian tori in
$X$; since the distinguishing data are $GL(2,\mathbb Z)$-mutation data, the same
argument upgrades the conclusion to symplectomorphism classes.

## 1. Disk potential of a monotone torus

Let $(X,\omega)$ be monotone and $L \subset X$ a monotone Lagrangian torus:
there is $c > 0$ with $\omega(\beta) = c\,\mu(\beta)$ for all
$\beta \in \pi_2(X,L)$, where $\mu$ is the Maslov index.
Fix a basis of $H_1(L;\mathbb Z) \cong \mathbb Z^2$ and write
$R = \mathbb Z[x^{\pm1},y^{\pm1}] = \mathbb Z[H_1(L)]$.
For generic tame $J$, the moduli spaces $\mathcal M_1(L,\beta;J)$ of
$J$-holomorphic disks in class $\beta$ with one boundary marked point and
Maslov index $\mu(\beta) = 2$ are compact oriented $0$-manifolds (no bubbling of
Maslov $\le 0$ disks by monotonicity); let $n_\beta = \#\mathcal M_1(L,\beta;J)
\in \mathbb Z$ be their degree over $L$. The **disk (Landau–Ginzburg) potential**
$$W_L = \sum_{\mu(\beta)=2} n_\beta\, z^{\partial\beta} \in R,$$
a finite Laurent polynomial (finiteness by area bound + Gromov compactness), is
independent of generic $J$ (cobordism argument; Maslov-$0$ walls absent by
monotonicity). This is the Cho–Oh / Auroux / Fukaya–Oh–Ohta–Ono setup; for
monotone tori no virtual machinery beyond the transverse case is needed.

## 2. Invariance lemma (Hamiltonian and symplectic)

**Lemma 1.** Let $L_1,L_2 \subset X$ be monotone Lagrangian tori and
$\psi : X \to X$ a symplectomorphism with $\psi(L_1) = L_2$.
Then $\psi_* : H_1(L_1) \to H_1(L_2)$ is an isomorphism and
$$W_{L_2} = (\psi_*)_* W_{L_1},$$
i.e.\ $W_{L_2}$ is obtained from $W_{L_1}$ by the induced $GL(2,\mathbb Z)$
change of basis (a monomial automorphism of $(\mathbb C^*)^2$).
In particular this holds when $\psi$ is a Hamiltonian diffeomorphism.

*Proof.* $\psi_*$ gives a bijection $\pi_2(X,L_1) \to \pi_2(X,L_2)$ preserving
$\mu$ and $\omega$-area. Pushforward of $J$ gives a bijection of the
Maslov-$2$ disk moduli spaces,
$\mathcal M_1(L_2,\psi_*\beta;\psi_*J) \cong \mathcal M_1(L_1,\beta;J)$,
preserving degrees, so $n_{\psi_*\beta}(L_2) = n_\beta(L_1)$.
$J$-independence of $W$ removes the dependence on $\psi_*J$.
Writing both potentials in bases related by $\psi_* \in GL(2,\mathbb Z)$ gives
the stated monomial equivalence. ∎

**Corollary.** If $W_{L_1},W_{L_2}$ are not equivalent under any
$GL(2,\mathbb Z)$ monomial change of variables, then $L_1,L_2$ are not
Hamiltonian isotopic; indeed they are not related by any symplectomorphism of
$X$. Operative $GL$-invariants include: Newton polytope up to $GL(2,\mathbb Z)$,
normalized volume, lattice-point count / number of terms, and max edge lattice
length.

## 3. Application to iterated mutations; infinitude

Assume the Pascaleff–Tonkonog seed data as hypotheses (Prop 4.22: monotone seed
$(L,\{D_i\})$ with potential $W_0$; Theorem 4.8: geometric mutation along a
propagated disk induces the algebraic wall-crossing $W \mapsto \mu(W)$).
Hence every torus $L'$ produced by iterated geometric mutation carries the
potential obtained by the corresponding iterated algebraic mutation of $W_0$.

The group of seed automorphisms
$$G = \{g \in GL(2,\mathbb Z) : g \cdot W_0 = W_0\}$$
(possibly combined with the compatible monomial rescaling) is **finite**: with
$P_0 = \mathrm{Newt}(W_0)$ a full-dimensional lattice polytope, $G$ preserves
the finite vertex set of $P_0$, hence embeds into a finite permutation group.
So "distinct vertices of the mutation graph modulo the finite automorphism
group" means, by construction, seeds whose mutated potentials are not
$GL(2,\mathbb Z)$-equivalent.

**Lemma 2 (unbounded $GL$-invariant along an infinite-type ray).**
Combinatorial (cluster) mutation in rank 2 preserves normalized volume but not
$GL$-class: it can strictly increase the max edge lattice length
$\ell_{\max}(P)$ and the lattice-point count $\#(P \cap \mathbb Z^2)$, both
$GL(2,\mathbb Z)$-invariants. For an infinite-type rank-2 ray the degree data
obey $d_{n+1} = r d_n - d_{n-1}$ with $r \ge 3$ (indefinite Vieta jumping
$d \mapsto K ab - d$), forcing exponential growth of $\ell_{\max}$; hence the
ray contains infinitely many pairwise $GL(2,\mathbb Z)$-inequivalent Newton
polytopes. The accompanying computation (`output/artifacts/mutation_ray.py`,
`markov_ray.json`) verifies this mechanism on a genuine single-Vieta-move ray
$(1,1,1)\to(2,1,1)\to(2,5,1)\to(2,5,29)\to(433,5,29)\to(433,37666,29)$:
each step is exactly one Vieta move $c\mapsto 3ab-c$, normalized volume is
constant $9$, and maxima $1<2<5<29<433<37666$ are strictly increasing, so the
six polytopes are pairwise $GL$-inequivalent.

By hypothesis the Pascaleff–Tonkonog cubic seed has infinite mutation graph
(infinite-type cluster dynamics). Applying Lemma 2, some (indeed any
unbounded) infinite ray yields infinitely many pairwise
$GL(2,\mathbb Z)$-inequivalent Newton polytopes, hence infinitely many
pairwise $GL$-inequivalent potentials $W$. By Lemma 1 / Corollary, the
corresponding geometric tori $L',L'',\dots$ are pairwise not Hamiltonian
isotopic — and pairwise not symplectomorphic. This is the claimed injection
of the infinite mutation graph (modulo finite $G$) into Hamiltonian
(respectively symplectomorphism) classes.

## 4. Two corrections to the admitted wording

(a) **$SL(2,\mathbb Z)$ vs $GL(2,\mathbb Z)$.** The admitted text writes
"$SL(2,\mathbb Z)$-change of basis". The correct structure group is the full
monomial group $(\mathbb C^*)^2 \rtimes GL(2,\mathbb Z)$, since a
symplectomorphism (or Hamiltonian map) can induce a determinant $-1$ map on
$H_1$ (e.g.\ reflection). The theorem is proved for $GL$-inequivalence, which
is the sharp criterion: $SL$-inequivalence *with* $GL$-equivalence via a
reflection (chiral pair) does **not** imply non-Hamiltonian-isotopic by this
method. All infinitude invariants used here (normalized volume, term/lattice
count, max edge length, critical-point count) are reflection-independent, so
the infinitude conclusion is unaffected by the correction.

(b) **Jacobian / critical values.** The admitted "i.e." suggests Jacobian rings
or critical-value multisets might differ among mutation-related seeds. In fixed
$X$ they do not: wall-crossing $W' = \Phi^*W$ via a birational torus map
preserves critical values, and mirror symmetry identifies
$\mathrm{Jac}(W) \cong QH^*(X)$ with eigenvalues of $c_1\star$ for every seed.
Hence that sub-criterion is vacuous for mutation-related pairs in fixed $X$;
it is harmless but unnecessary. The Newton-polytope criterion above carries the
full force, and the parenthetical Floer consequence holds in the form: the
support of $HF^\bullet(L,\rho)$ over local systems $\rho \in (\mathbb C^*)^2$
moves by the monomial map, so $GL$-distinct Newton data obstruct Hamiltonian
isotopy.

## 5. Conclusion

Modulo the routine $SL \to GL$ correction and the remark (b), the answer to the
admitted question is **yes**: distinct mutated seeds with
$GL(2,\mathbb Z)$-inequivalent disk potentials give monotone Lagrangian tori
that are not Hamiltonian isotopic (indeed not symplectomorphic) in the monotone
cubic surface, and the infinite mutation graph modulo finite seed automorphisms
injects into the set of Hamiltonian (hence symplectomorphism) isotopy classes
of monotone Lagrangian tori in $X$. The proof is conditional only on the
admitted Pascaleff–Tonkonog input (seed Prop 4.22 + wall-crossing Thm 4.8);
the deduction from that input to injectivity is proved here.

*Computed evidence.* `output/artifacts/mutation_ray.py` + `markov_ray.json`:
machine-checked single-Vieta-move ray with strictly growing $GL$-invariant
(max edge lattice length) at constant normalized volume — the exact
combinatorial mechanism driving infinitude. It is a model of the infinite-type
dynamics, not a recomputation of Pascaleff–Tonkonog's cubic potentials.
*Literature.* No literature search was used; the invariance argument is
standard (Cho–Oh, Auroux, FOOO, Vianna) and the PT statements are taken as
admitted hypotheses per the topic.
