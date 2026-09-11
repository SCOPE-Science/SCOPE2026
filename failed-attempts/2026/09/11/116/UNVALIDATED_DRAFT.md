# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Triple-interchanger Yang–Baxter hexagon coherence in Gray-categories

## Claim (TARGET)

In the free Gray-category on one 0-cell with distinct generating 2-cells
$A,B,C$ on the identity 1-cell, the clockwise triple-interchanger hexagon
composite $P$ equals the counterclockwise composite $Q$ as parallel 3-cells
with common source pasting $ABC$ and common target pasting $CBA$.

## 1. Setting

Work in the free Gray-category $\mathcal{G}$ on the 2-computad with a single
0-cell $\star$, a single generating 1-cell $I = \mathrm{id}\_\star$, and three
distinct generating 2-cells $A,B,C : I \Rightarrow I$.

- 2-cell pastings are words over $\{A,B,C\}$ (horizontal composites);
  concatenation is strictly associative, and whiskering by the identity 1-cell
  $I$ is strict. Write 3-cell (vertical) composition diagrammatically with
  $\cdot$ (apply left factor first).
- For 2-cells $X,Y$, the Gray interchanger is the generating invertible
  3-cell $\chi\_{X,Y} : XY \Rightarrow YX$. Whiskered instances are written
  $L \ast \chi\_{X,Y} \ast R : LX YR \Rightarrow LYXR$.

## 2. Gray axioms used

Only the following standard Gray-category laws are used (Gordon–Power–Street;
Gurski, *Coherence in Three-Dimensional Category Theory*; nLab
"Gray-category"; Forest–Mimram rewriting framework). All hold in the free
Gray-category by construction:

- **(H1) Compatibility, first argument:** for 2-cells $X,Y$ and fixed $C$,
  $\chi\_{XY,C} = (X \ast \chi\_{Y,C}) \cdot (\chi\_{X,C} \ast Y)$.
- **(H2)** The same law at other composites (instance used below):
  $\chi\_{BA,C} = (B \ast \chi\_{A,C}) \cdot (\chi\_{B,C} \ast A)$.
- **(N) Naturality in the first argument:** the family $\chi\_{- ,C}$ is
  natural with respect to 3-cells. Applied at the 3-cell
  $\Gamma = \chi\_{A,B} : AB \Rightarrow BA$ this gives the square
  $$(\chi\_{A,B} \ast C) \cdot \chi\_{BA,C}
    \ =\ \chi\_{AB,C} \cdot (C \ast \chi\_{A,B}),$$
  a 3-cell equality $ABC \Rightarrow CBA$ on both sides.
  (Whiskering sides are forced by boundary matching; verified in §4.)

No further coherence cells (4-cells, Squier conditions) are invoked.

## 3. The hexagon composites

Clockwise and counterclockwise composites (adjacent-swap words $s\_1s\_2s\_1$
and $s\_2s\_1s\_2$ for the longest element of $S\_3$):

| step | cell | type |
|---|---|---|
| $p\_1 = \chi\_{A,B}\ast C$ | $ABC \Rightarrow BAC$ | $P$ step 1 |
| $p\_2 = B\ast\chi\_{A,C}$ | $BAC \Rightarrow BCA$ | $P$ step 2 |
| $p\_3 = \chi\_{B,C}\ast A$ | $BCA \Rightarrow CBA$ | $P$ step 3 |
| $q\_1 = A\ast\chi\_{B,C}$ | $ABC \Rightarrow ACB$ | $Q$ step 1 |
| $q\_2 = \chi\_{A,C}\ast B$ | $ACB \Rightarrow CAB$ | $Q$ step 2 |
| $q\_3 = C\ast\chi\_{A,B}$ | $CAB \Rightarrow CBA$ | $Q$ step 3 |

$$P = p\_1 \cdot p\_2 \cdot p\_3 : ABC \Rightarrow CBA \qquad
  Q = q\_1 \cdot q\_2 \cdot q\_3 : ABC \Rightarrow CBA.$$

Both sides are non-identity three-step composites of distinct whiskered
generating interchangers; they are parallel 3-cells, so $P = Q$ is a genuine
contestable equality (not a type error, not a single-axiom collapse).

## 4. Proof ledger

1. **Compatibility (H2):** $\chi\_{BA,C} = p\_2 \cdot p\_3$.
   Both sides have type $BAC \Rightarrow CBA$; step boundaries match
   ($BAC \Rightarrow BCA \Rightarrow CBA$).
2. **Compatibility (H1):** $\chi\_{AB,C} = q\_1 \cdot q\_2$.
   Both sides have type $ABC \Rightarrow CAB$; boundaries match
   ($ABC \Rightarrow ACB \Rightarrow CAB$).
3. **Naturality (N)** at $\Gamma = \chi\_{A,B}$:
   $p\_1 \cdot \chi\_{BA,C} = \chi\_{AB,C} \cdot q\_3$
   (both sides $ABC \Rightarrow CBA$; boundary junctions
   $ABC \Rightarrow BAC \Rightarrow CBA$ and $ABC \Rightarrow CAB \Rightarrow CBA$).
4. **Substitution** of steps 1–2 into step 3:
   $$P = p\_1 \cdot (p\_2 \cdot p\_3) = p\_1 \cdot \chi\_{BA,C}
     = \chi\_{AB,C} \cdot q\_3 = (q\_1 \cdot q\_2) \cdot q\_3 = Q.$$

Hence $P = Q$ in the free Gray-category. The triple-overlap critical pair is
joinable; no Squier-type obstruction occurs at this hexagon. ∎

## 5. Machine check

`output/artifacts/verify_hexagon.py` (stdlib only) encodes words over
$\{A,B,C\}$, whiskered interchanger steps, and vertical composition; it asserts
every step's source/target, every chain junction, parallel boundaries of $P$
and $Q$ ($ABC \Rightarrow CBA$), well-typedness of each axiom side, and that
substituting (H1),(H2) into (N) yields $P = Q$ syntactically. Run:

```
python3 output/artifacts/verify_hexagon.py   # prints VERIFY_OK
```

## 6. Remarks

- The argument is the Joyal–Street Yang–Baxter derivation (hexagons +
  naturality of the braiding/interchanger at itself), transported to the Gray
  interchanger family; invertibility of $\chi$ is not needed, only the three
  displayed equations.
- This ledger decides the admitted target positively: a closed critical-pair
  confluence diagram for the named three-generator hexagon, which no cited
  source (Forest–Mimram, Gurski, Gray, nLab) carries out for generators
  $A,B,C$.
