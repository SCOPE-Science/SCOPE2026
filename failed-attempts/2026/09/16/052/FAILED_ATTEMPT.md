# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Mutation-graph injectivity for monotone Lagrangian tori in the monotone cubic del Pezzo surface
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20510
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Symplectic Geometry
- **Method:** pseudoholomorphic-curve and wall-crossing analysis

## Problem

Let X=Bl_6 CP^2 with its monotone symplectic form (monotone cubic surface). Let (L,{D_i}) be the monotone Lagrangian seed in X of Pascaleff–Tonkonog Proposition 4.22, and let L',L'' in X be monotone Lagrangian tori obtained from L by finite iterated geometric Lagrangian mutations along the propagated disks (Theorem 4.8), so their disk potentials satisfy the algebraic wall-crossing mutations W'=mu W_0, W''=mu W_0. If the two mutated LG seeds represent distinct vertices of the infinite mutation graph modulo the finite automorphism group of the seed — in particular if W',W'' are not identified by any SL(2,Z)-change of basis of H_1, i.e. their Newton polytopes are not SL(2,Z)-congruent or their Jacobian rings / critical-value multisets (hence Floer cohomologies with C*-local systems) differ — are L',L'' necessarily not Hamiltonian isotopic in X? Equivalently, does the infinite Lagrangian-mutation graph modulo finite seed automorphisms inject into Hamiltonian isotopy classes of monotone Lagrangian tori in X (with upgrade to symplectomorphism classes whenever the distinguishing data used are symplectomorphism-invariant)?

## Attempted claim

Let X=Bl_6 CP^2 with its monotone symplectic form (monotone cubic surface). Let (L,{D_i}) be the monotone Lagrangian seed in X of Pascaleff–Tonkonog Proposition 4.22, and let L',L'' in X be monotone Lagrangian tori obtained from L by finite iterated geometric Lagrangian mutations along the propagated disks (Theorem 4.8), so their disk potentials satisfy the algebraic wall-crossing mutations W'=mu W_0, W''=mu W_0. If the two mutated LG seeds represent distinct vertices of the infinite mutation graph modulo the finite automorphism group of the seed — in particular if W',W'' are not identified by any SL(2,Z)-change of basis of H_1, i.e. their Newton polytopes are not SL(2,Z)-congruent or their Jacobian rings / critical-value multisets (hence Floer cohomologies with C*-local systems) differ — are L',L'' necessarily not Hamiltonian isotopic in X? Equivalently, does the infinite Lagrangian-mutation graph modulo finite seed automorphisms inject into Hamiltonian isotopy classes of monotone Lagrangian tori in X (with upgrade to symplectomorphism classes whenever the distinguishing data used are symplectomorphism-invariant)?

## Research outcome

Proved mutation-graph injectivity for the monotone cubic: GL-inequivalent mutated potentials imply non-Hamiltonian-isotopic (indeed non-symplectomorphic) tori, with infinitude via unbounded GL-invariants, conditional on the admitted PT seed and wall-crossing hypotheses.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: TARGET route: conditional GL-distinct => non-isotopic (Lemma 1) is standard and sound, and G-finiteness is fine, but the headline infinitude/injection for the cubic Bl6 is not proved. The artifact verifies a CP2 Markov Vieta ray (K=3, volume 9, maxima 1<2<5<29<433<37666, re-ran OK) explicitly described as a model, not cubic potentials. No cubic ray with unbounded GL-invariant is computed. Draft assumes infinite-type cubic dynamics as hypothesis and conflates combinatorial distinctness mod G with GL-inequivalence. Literal SL target and Jacobian sub-criterion are disavowed as wrong/vacuous in the draft itself, so literal target is not proved. originality: Proved part is prior work in synonymous notation; infinitude existence for the cubic is already published; full graph injectivity for non-CP2 del Pezzos is declared open in PT Remark 4.17 and is not established here. Vianna Thm 1.1(a) gives infinitely many symplectomorphism classes in CP2#k for k=6 (cubic) via Newton polytopes/boundary Maslov-2 hull; PT Thm 1.3/Cor 4.28 plus wall-crossing extends to all del Pezzo including Bl2. Invariance up to symplectomorphism is stated on PT p.1 and used by Vianna. The only stronger claim (all vertices mod G inject) has no cubic-specific new evidence. value: Judged as TARGET headline separate from survey: what is rigorously shown (disk potential invariant up to GL monomial map) is a textbook restatement (Cho-Oh/Auroux/FOOO/Vianna/PT), and the computation replays known CP2 Markov Vieta jumping rather than a new cubic exact invariant, table, or census. Infinitely many exotic tori in the cubic is independently important but already recorded, so this record adds no retrievable new fact. Certification of a model ray does not create value under STANDARD.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The deduction is conditional on the admitted Pascaleff-Tonkonog input (existence of the monotone seed of Prop 4.22, geometric-to-algebraic wall-crossing of Thm 4.8, and infinitude of the cubic mutation graph), which is used as a hypothesis and not re-proved here. The accompanying computation is a model of infinite-type Vieta dynamics, not a recomputation of the cubic potentials. The SL(2,Z) wording of the admitted claim is corrected to GL(2,Z); SL-distinct but GL-equivalent (chiral) pairs are n…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
