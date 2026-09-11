# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Universal LOSS-vanishing at (tb,rot)=(7,0) for the trefoil: the admitted Hopf-1 LOSS gap is a priori impossible

## Theorem (certified vanishing cell)
Let $K=T(2,3)$ be the right-handed trefoil and let $L$ be any Legendrian
representative of $K$ with Thurston–Bennequin invariant $\mathrm{tb}(L)=7$
and rotation number $\mathrm{rot}(L)=0$ in any contact structure $\xi$ on
$S^3$ — tight or overtwisted, any Hopf invariant / $d_3$.
Then the Lisca–Ozsváth–Stipsicz–Szabó invariant satisfies
$$\mathrm{LOSS}(L)=0 \in \mathrm{HFK}^-(-S^3,K), \qquad \widehat{\mathrm{LOSS}}(L)=0 \in \widehat{\mathrm{HFK}}(-S^3,K).$$
In particular there is no pair $L_1,L_2$ of such knots at $(7,0)$ —
in the Hopf-1 overtwisted $S^3$ or in any contact $S^3$ — with
$\mathrm{LOSS}(L_1)\ne\mathrm{LOSS}(L_2)$. The LOSS-distinguishing half of
the admitted target is impossible; the sharp LOSS-collapse for this cell
is located at the Alexander-grading level.

## Background used
1. **LOSS Alexander grading** (Lisca–Ozsváth–Stipsicz–Szabó,
   *Heegaard Floer invariants of Legendrian knots in contact
   three-manifolds*, JEMS; cf. Ozsváth–Stipsicz–Szabó LOSS formula):
   for a null-homologous oriented Legendrian $L$ of smooth type $K$,
   the (minus) LOSS class lies in Alexander grading
   $$A(\mathrm{LOSS}(L))=\frac{\mathrm{tb}(L)-\mathrm{rot}(L)+1}{2}.$$
   The hat version is its image in the corresponding hat group in the
   same Alexander grading.
2. **Genus support bound** (Ozsváth–Szabó, *Holomorphic disks and knot
   invariants*): $\widehat{\mathrm{HFK}}(S^3,K,A)=0$ for $|A|>g(K)$,
   and likewise the minus complex in a fixed Alexander grading $A$
   with $|A|>g(K)$ is zero. Orientation reversal $-S^3$ does not change
   the groups.
3. **Trefoil data**: $g(T(2,3))=1$; the published hat table is rank $1$
   in each of $A\in\{-1,0,1\}$ and $0$ elsewhere. The contact host
   $(S^3,\xi)$ does not alter the smooth knot Floer group in which LOSS
   takes values.

## Proof
Fix any contact $S^3$ and any Legendrian $L$ of type $T(2,3)$ with
$(\mathrm{tb},\mathrm{rot})=(7,0)$. Parity check:
$\mathrm{tb}+\mathrm{rot}=7$ is odd, as required for a null-homologous
Legendrian knot, so no parity obstruction is claimed.
By (1),
$$A(\mathrm{LOSS}(L))=\frac{7-0+1}{2}=4.$$
By (2)–(3) with $g=1$, the target group
$\mathrm{HFK}^-(-S^3,T(2,3),A{=}4)$ is the zero group, and the hat group
in $A=4$ is zero since $4\notin\{-1,0,1\}$. A class in the zero group is
zero. Hence $\mathrm{LOSS}(L)=0$ and $\widehat{\mathrm{LOSS}}(L)=0$ for
every such $L$, in every contact $S^3$. Two zeros cannot differ, so no
LOSS-distinguished pair at $(7,0)$ exists. ∎

## Machine replay
`output/artifacts/verify_grading.py` recomputes $A=4$, checks parity,
checks $4$ against the trefoil support $\{-1,0,1\}$, and prints
`VERIFY_OK` (replayed in-lane).

## Why this is the sharp collapse location
The obstruction is independent of the presenting contact-surgery diagram,
of $d_3$/Hopf invariant, of bypass choices, and of Giroux torsion: it
depends only on the smooth knot type and $(\mathrm{tb},\mathrm{rot})$
through the grading formula plus the smooth genus bound. Any bypass
triangle whose endpoints both carry $(7,0)$ joins two zero-LOSS knots,
so no dividing-slope log in this cell can produce a LOSS gap. Recovery
within the fixed cell is impossible: orientation/sign variants keep
$\mathrm{rot}=0$ hence $A=4$; the mirror trefoil has symmetric support
$|A|\le 1$; changing the host contact structure does not change the
smooth $\mathrm{HFK}$ group. A nonzero LOSS witness would require a
different $(\mathrm{tb},\mathrm{rot})$ cell with $A\in\{-1,0,1\}$,
outside the exact target scope.

## Limitations (explicitly not claimed)
- This does **not** decide whether non-loose $(7,0)$ trefoils exist in
  Hopf-1 overtwisted $S^3$, nor whether any two such are Legendrian
  isotopic: isotopy via non-LOSS invariants (e.g. ruling, contact
  homology, Heegaard Floer contact class of surgeries) is left open.
- Existence of the named $(+1)$-surgery diagram for $(S^3,\xi_1)$ Hopf-1
  and of the bypass triangle at $(7,0)$ is not established here; the
  theorem moots them for LOSS purposes.
- $\mathrm{tor}=0$ and single-stabilization behavior are not computed;
  they are unnecessary for the vanishing conclusion.
- The theorem covers LOSS/hat-LOSS only, not the transverse push-off or
  plus-flavoured invariants.

## References
- Lisca–Ozsváth–Stipsicz–Szabó, Heegaard Floer invariants of Legendrian
  knots in contact three-manifolds (JEMS); LOSS definition, grading,
  naturality.
- Ozsváth–Szabó, Holomorphic disks and knot invariants; genus bound and
  trefoil $\widehat{\mathrm{HFK}}$ table ($g=1$, support $\{-1,0,1\}$).
- Etnyre–Min–Mukherjee, Non-loose torus knots (arXiv:2206.14848): coarse
  classification is coarse-only and records no fixed-$(7,0)$ LOSS verdict.
- Etnyre, On knots in overtwisted contact structures; Geiges–Onaran,
  Exceptional Legendrian torus knots: existence context, not the LOSS gap.
