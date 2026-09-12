# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Jump-spectrum equality versus degree-spectrum separation — TARGET resolution

## Status
Complete TARGET resolution: the requested separating pair does not exist.
Equality of jump spectra forces equality of degree spectra for the stated class,
for the elementary reason that every computable structure has full degree spectrum.

## Definitions (as used in the target)
- For a countable structure $A$ with domain $\omega$, $DgSp(A) = \{{\bf d} :
  {\bf d}\ \text{computes a copy of } A\}$, i.e. there is $B \cong A$ with atomic
  diagram $D(B) \le_T {\bf d}$. Difference of spectra means some degree computes
  a copy of exactly one of the two structures (as the target parenthetical states).
- The jump spectrum is $DgSp(A)' = \{{\bf x}' : {\bf x} \in DgSp(A)\}$.
- Spectrum is upward-closed: if ${\bf d} \in DgSp(A)$ and ${\bf e} \ge {\bf d}$,
  then ${\bf e} \in DgSp(A)$, because ${\bf e}$ computes everything ${\bf d}$
  computes, hence computes the same copy.

## Lemma 1 (computable copy gives degree 0)
If $A$ is computable (has a computable copy with domain $\omega$), then
${\bf 0} \in DgSp(A)$.
*Proof.* Let $B_0 \cong A$ be computable. Its atomic diagram $D(B_0)$ is a
computable set, hence computed by every degree, in particular by ${\bf 0}$. ∎

## Lemma 2 (full spectrum)
If $A$ is computable, then $DgSp(A)$ is the set of all Turing degrees.
*Proof.* By Lemma 1, ${\bf 0} \in DgSp(A)$. By upward closure, every
${\bf e} \ge {\bf 0}$ — i.e. every Turing degree — lies in $DgSp(A)$.
Explicitly, if $\Phi^{{\bf 0}} = D(B_0)$ then for any ${\bf e}$ with witness
$\Gamma^{{\bf e}} = {\bf 0}$, $\Phi^{\Gamma^{{\bf e}}}$ computes the same copy,
ignoring the extra oracle power. ∎

## Theorem (answer to the target question)
Fix a prime $p$. Let $G,H$ be any computable reduced abelian $p$-groups of Ulm
length $\le \omega$ with divisible part $0$ (in fact, let $G,H$ be any two
computable structures at all). Then:
1. $DgSp(G) = DgSp(H) =$ the set of all Turing degrees.
2. $\{ {\bf x}' : {\bf x} \in DgSp(G)\} = \{{\bf x}' : {\bf x} \in DgSp(H)\}$
   $=$ the set of all jump degrees $\{ {\bf d}' : {\bf d}\ \text{a degree}\}$.
3. In particular there is NO pair $G,H$ in this class with equal jump spectra
   but distinct unrelativized spectra, and the implication "equality of jump
   spectra forces equality of degree spectra" holds for all such pairs
   (indeed with true consequent for every pair).

*Proof.* (1) is Lemma 2 applied twice. (2) follows by applying the jump map to
identical sets. (3) follows: the existential claim is refuted since any pair
has identical (full) unrelativized spectra, so no separating degree exists;
the universal implication holds vacuously-with-true-consequent. ∎

## Remarks
- No Ulm theory, jump inversion, or transfer via equivalence structures is needed.
  The hypotheses "reduced", "Ulm length $\le\omega$", "divisible part zero" play
  no role beyond delimiting the class; the argument uses only computability of
  $G$ and $H$, which is part of the hypothesis.
- The argument does not show anything about noncomputable groups, where spectra
  can be proper upward-closed cones or more complex sets and jump equality need
  not force spectrum equality. That is outside the stated target.
- Under the alternate "degree-of-a-copy" definition of spectrum, the same
  conclusion holds for these groups (finite ones have spectrum $\{{\bf 0}\}$ in
  that sense only if restricted to exact degrees, but the target's parenthetical
  fixes the "computes a copy" reading, under which the proof above is exact).

## Self-checks performed
1. Confirmed the target's parenthetical definition matches the "computes a copy"
   reading, so upward closure is immediate (oracle-ignoring functional).
2. Confirmed ${\bf 0}$-membership from computability hypothesis for both $G,H$.
3. Confirmed jump-set equality is set-equality of images of identical sets.
4. Checked quantifier structure: refuting the existential + proving the universal
   implication are the same full resolution the target allows ("either exhibits
   ... or proves that equality ... forces equality").
5. Checked no hidden relativization: jump spectrum uses the ordinary Turing jump
   on degrees, applied uniformly to both sides.
