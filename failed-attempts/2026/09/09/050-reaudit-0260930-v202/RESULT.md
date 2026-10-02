# Class-resolved Hurwitz (2,3,7) generation profiles for PSL(2,13), PSL(2,27), PSL(2,29), with M11 non-Hurwitz control

## Context

Hurwitz (2,3,7)-generation links finite groups to Hurwitz surfaces, regular maps, and dessins via surface-group epimorphisms. Bare Hurwitz existence (e.g. Macbeath's criterion for PSL(2,q)) does not say *which* conjugacy classes of elements of order 7 participate in generating triples — the data actual epimorphisms need. This record gives the complete per-class-triple generation profile for PSL(2,13), PSL(2,27), PSL(2,29), plus the sporadic boundary control M11.

## Definitions

- G in {PSL(2,13), PSL(2,27), PSL(2,29)}; |G| = 1092, 9828, 12180.
- PSL(2,p) = SL(2,p)/{±I} with canonicalized representatives (p = 13, 29); PSL(2,27) uses GF(27) = F3[t]/(t^3+2t+1), same quotient.
- A (2,3,7) class-triple type is (2X,3Y,7Z), e.g. (2A,3A,7B).
- Frobenius constant N(2X,3Y,7Z) = number of ordered pairs (x,y) in 2X×3Y with xy in 7Z (obtained here by exact pair enumeration, mathematically equal to the character-table formula).
- A type GENERATES if some (equivalently, up to the checked conjugacy reduction, every representative) pair (x,y) of that type satisfies ⟨x,y⟩ = G.
- Base Hurwitz pair (A,B): |A|=2, |B|=3, |AB|=7. Witness for a type: (w2=A, w3) with w3 a word in {A,B,B⁻¹} of order 3 in the required 3-class and A·w3 of order 7 in the required 7-class, with ⟨A,w3⟩ = G by exact BFS.
- Genus g = 1 + |G|/84 (Riemann–Hurwitz for a Hurwitz action).

## Result

**(a) Class structures.** Each group has a unique involution class 2A. PSL(2,13) and PSL(2,29) have a unique class 3A of elements of order 3; PSL(2,27) has two classes 3A, 3B. Each group has exactly three classes 7A, 7B, 7C of elements of order 7.

**(b) Uniform generation.** Every (2,3,7) class-triple type generates G: all 3 types (2A,3A,7X) for PSL(2,13) and PSL(2,29); all 6 types (2A,3A/3B,7X) for PSL(2,27). No non-generating type with nonzero Frobenius constant occurs, so no maximal-subgroup elimination is needed.

**(c) Exact Frobenius constants (ordered-pair counts).** N = 2184 per type (PSL(2,13)); N = 24360 per type (PSL(2,29)); N = 9828 per type (PSL(2,27)).

**(d) Witnesses and genera.** For each type an explicit word pair (w2,w3) in a committed Hurwitz base pair attains |G| by exact BFS. Genera: g = 14 (PSL(2,13)), g = 118 (PSL(2,27)), g = 146 (PSL(2,29)).

PSL(2,13), |G|=1092, g=14. Base A=[[0,1],[12,0]], B=[[1,2],[5,11]]:

| type | N | verdict | w3 (w2=A) |
|---|---|---|---|
| (2A,3A,7A) | 2184 | GENERATES | B |
| (2A,3A,7B) | 2184 | GENERATES | ABABiABiA |
| (2A,3A,7C) | 2184 | GENERATES | BABiABiABABiABABiA |

PSL(2,29), |G|=12180, g=146. Base A=[[0,1],[28,0]], B=[[0,4],[7,1]]:

| type | N | verdict | w3 (w2=A) |
|---|---|---|---|
| (2A,3A,7A) | 24360 | GENERATES | B |
| (2A,3A,7B) | 24360 | GENERATES | BABABiABABiABABABiABABiABABiABi |
| (2A,3A,7C) | 24360 | GENERATES | ABiABABABiABABiABABABiABiABABiABiAB |

PSL(2,27), |G|=9828, g=118. Base A=[0,1,2,0], B=[1,0,9,1] over GF(27) (elements coded a0+3·a1+9·a2):

| type | N | verdict | w3 (w2=A) |
|---|---|---|---|
| (2A,3A,7A) | 9828 | GENERATES | B |
| (2A,3A,7B) | 9828 | GENERATES | ABiABABiABiABABABiABiABABABiABiABABiABi |
| (2A,3A,7C) | 9828 | GENERATES | ABiABABiABiABABiABiABABABiABiABABiABiABABiABi |
| (2A,3B,7A) | 9828 | GENERATES | Bi |
| (2A,3B,7B) | 9828 | GENERATES | ABABiABABABiABiABABABiABiABABABiABAB |
| (2A,3B,7C) | 9828 | GENERATES | ABABABiABiABABiABiABABABiABiABABiABiABABAB |

(Bi = B⁻¹; each w3 has order 3 in the named 3-class; A·w3 has order 7 in the named 7-class; ⟨A,w3⟩ has order |G|.)

**(e) M11 control.** |M11| = 7920 = 2⁴·3²·5·11; 7920 mod 7 = 3, so M11 has no element of order 7 (ATLAS M11 class list 1A,2A,3A,4A,5A,6A,8A,8B,11A,11B confirms) and admits no (2,3,7) triple — a fortiori not Hurwitz. Elementary boundary control paired with the census.

## Proof / evidence (exact computation)

- Enumeration of SL(2,p)/{±I} (p=13,29) and SL(2,27)/{±I}: 1092 / 12180 / 9828 elements; conjugation-BFS classes: 9 / 17 / 16 classes with class equations summing to |G|.
- Frobenius constants by exact ordered-pair counting, cross-checked fiber-count vs full |2A|×|3·| scan (agree).
- Generation verdicts exhaustive up to G-conjugacy: fiber {y : x0·y ∈ 7X} reduced to C_G(x0)-orbit representatives (2 reps/type for p=13,29 with |C|=12,28; 1 rep/type for q=27 with |C|=28); exact BFS subgroup order for each rep attains |G| in every case.
- Internal checks: Cayley-BFS closure attains |G|; |AB|=7 for each base pair; fiber sizes satisfy N/|2A| = reps × orbit size (24=2×12; 56=2×28; 28=1×28).
- Auditor independently re-ran p=13 and p=29 scripts end-to-end (identical verdicts/counts), re-ran the q=27 enumeration (identical classes/N/verdicts), and re-evaluated every exhibited word with separate matrix code: all w3 order 3, all A·w3 order 7 with traces covering the claimed classes, all subgroup BFS orders full.
- Originality diff: ATLAS L2(13)/L2(29) standard generators have ab=13/29 (no (2,3,7) word there); ATLAS L2(27) standard pair already has ab=7, so q27 novelty is the 6-type table + new words, not existence. Conder triangle-quotient lists record existence by genus/order, not class-triple tables.

## Limitations

- Frobenius constants via exact pair enumeration, not the character-table formula (mathematically equal, different audit trail).
- PSL(2,27) class labels (3A vs 3B, 7A/B/C) ordered by GF(27)-trace; may not match ATLAS labelling. Invariant content is labelling-independent.
- M11 control uses published ATLAS order/class data plus arithmetic, not an independent M11 computation.
- Uniform-generation outcome: no maximal-subgroup elimination logs exist for this window.
- Shipped verify_hurwitz_27.py covers classes/Frobenius/verdicts; the q27 word-search stage is not in the shipped script, though archived q27 words verify correct.

## Reproducibility

Python 3 stdlib only: `python3 output/artifacts/verify_hurwitz.py 13` (resp. `29`) replays the full PSL(2,p) census including word witnesses; `python3 output/artifacts/verify_hurwitz_27.py` replays the PSL(2,27) class/Frobenius/verdict enumeration. Machine JSON in `output/artifacts/hurwitz_psl2_{13,29,27}.json`. Runtimes: p=13 seconds; p=29 minutes; q=27 tens of minutes.

## References

- ATLAS v3 L2(13): https://brauer.maths.qmul.ac.uk/Atlas/v3/lin/L213/
- ATLAS v3 L2(29): https://brauer.maths.qmul.ac.uk/Atlas/v3/lin/L229/
- ATLAS v3 L2(27): https://brauer.maths.qmul.ac.uk/Atlas/v3/lin/L227/
- ATLAS v3 M11: https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/M11/
- Conder lists (triangle quotients / surface actions): https://www.math.auckland.ac.nz/~conder/
