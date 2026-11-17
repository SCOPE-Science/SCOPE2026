# Exact complete expanded-evaluation binary16 logistic cycle census

## Finding

Let \(S\) be the 15,361 nonnegative IEEE-754 binary16 values between zero and one, including subnormals, with positive zero as the only zero encoding. Let \(R\) mean round-to-nearest, ties-to-even binary16. Define the *staged expanded* logistic update
\[
E(x)=R\bigl(R(4x)-R(4R(x^2))\bigr),\qquad x\in S.
\]
Every explicitly displayed \(R\) is a binary16 rounding step; all other operations inside its argument are exact, and there are no fusions or reassociations. The complete functional graph of \(E:S\to S\) has precisely six primitive cycles, with the following period, number of starting states in the basin (including the cycle), and least unsigned binary16 cycle encoding:

| Period | Basin | Least encoding |
| ---: | ---: | --- |
| 1 | 6,671 | `0x0000` |
| 1 | 33 | `0x3a00` |
| 4 | 91 | `0x3470` |
| 17 | 881 | `0x2480` |
| 25 | 3,648 | `0x2000` |
| 30 | 4,037 | `0x2400` |

No other periodic orbits exist. The maximum number of steps from an initial state to its first periodic state is 59; the sum of such first-entry times over every state is 242,447. Of the 15,361 initial values, exactly 8,657 eventually enter a nonfixed cycle. The complete successor vector, in unsigned 16-bit little-endian encoding order, has SHA-256 digest

`7dac595f8435d93aa3bea32a701ef4c9d19d30f0079195a63f5db7ca0353729c`.

The exact staged-factored and correctly-once-rounded logistic cycle/basin censuses at parameter four, including their respective 40- and 5-cycle spectra, were already published in *Rounding placement changes the complete binary16 logistic attractor census* (2026). They are **not new claims here**. The surviving additional result is the complete expanded-evaluation classification and its incompatible comparison to those two established finite maps.

## Domain and conventions

All 15,361 unsigned codes `0x0000` through `0x3c00` are counted once; negative zero, negative inputs, infinities and NaNs are excluded. Intermediate operands, up to four, are rounded in the IEEE nearest-even model; subnormal underflow is gradual. Basin proportions are for the uniform counting law on binary16 encodings, not for uniformly sampled real initial values. The claim concerns this exact staged expression, not an arbitrary compiler implementation or the infinite-precision logistic map.

## Proof and exhaustive certificate

Set \(U=2^{24}\). For an unsigned nonnegative binary16 code \(j\), let \(e=\lfloor j/1024\rfloor\), \(f=j\bmod1024\). Its exact scaled value is
\[
V(j)=Ux_j=\begin{cases}f,&e=0,\\(1024+f)2^{e-1},&e\ge1.\end{cases}
\]
The strictly increasing list \(V(j)\), \(0\le j\le\texttt{0x4400}\), contains every nonnegative binary16 value from zero through four on the same integer scale. Define \(\mathcal R(a/b)\) to be the code minimizing \(|bV(j)-a|\), with even least significand bit winning ties. For any \(j\in S\), put
\[
 a=\mathcal R(4V(j)),\qquad c=\mathcal R(V(j)^2/U),\qquad d=\mathcal R(4V(c)),\qquad E_j=\mathcal R(V(a)-V(d)).
\]
All arguments are in scaled units, with the convention that \(\mathcal R\) rounds the displayed rational quantity in those units. These are exact integer comparisons. Exhaustive evaluation establishes that all 15,361 resulting indices lie in `0x0000` through `0x3c00`.

Build the resulting successor array in increasing code order. To classify a finite functional graph, start at each unclassified vertex and follow its unique successor until a previously labelled vertex or a repetition in the current chain is reached. In the second case the repeated suffix is a new cycle; label it with first-entry distance zero. Label every remaining vertex in reverse path order by the successor's cycle and one greater distance. This induction visits every vertex, never omits an additional cycle, and gives exact basin memberships and first-entry times. Applying it to the specified integer successor array gives the six table rows above; their basins sum to \(6671+33+91+881+3648+4037=15361\). Independently recomputing the successor array and its digest corroborates the complete enumeration. This is an exhaustive finite-state certificate, not finite sampling used to justify a universal claim about real dynamics.

The originally supplied `verify.py` also recomputes the already published factored and once-rounded reference maps, plus this expanded map, with the same integer-rounding and functional-graph procedure. Its complete expanded-map cycle, basin and transient assertions are retained and reproducible without external numerical libraries. The earlier reference-map results serve as checks and comparisons, not new priority claims.

## Prior coverage and value

The published result *Rounding placement changes the complete binary16 logistic attractor census* (2026) computes **exactly** the staged-factored 40-cycle with basin 10,267 and once-rounded 5-cycle with basin 117, together with their fixed-point basins and edge digests. Its arithmetic formulas cover two of the original three tables, and those are now explicitly excluded from the contribution. *Two exact binary16 logistic cycle spectra under algebraically equivalent evaluation* (2026) also includes the once-rounded reference but uses a different completed-square evaluation for its comparison. Neither of those inspected papers states or implies the present staged-*expanded* graph: floating-point rounding prevents algebraic real identities from identifying successor functions. Corless (2024) earlier reported the factored 40-cycle, while Klöwer et al. (2023) investigated logistic dynamics under limited precision. The general finite-graph traversal technique is standard and not claimed as new.

The expanded staging \(R(R(4x)-R(4R(x^2)))\) is a natural, reproducible evaluation graph of the canonical polynomial \(4x-4x^2\). The exact complete basin vector and its additional primitive periods \(4,17,25,30\) make a nontrivial exact diagnostic for the impact of this particular rounding placement, supplementing the two known reference evaluations. The exact invariant concerns a practically standardized small floating-point space and a standard chaotic benchmark, not an arbitrary restricted numerical slice. The exhaustiveness of all starting encodings is its value beyond sampled trajectories. Unindexed earlier full enumeration of this specific expanded graph remains a priority risk.

## Limitations and references

No implication is asserted for binary32, other parameters, arbitrary compilers, hidden extended precision, stochastic rounding, or real dynamical invariant measures. The finite algorithm is a complete enumerative proof only for the specified map. The same-source published factored/once-rounded classification and all conventional background remain prior art.

- *Rounding placement changes the complete binary16 logistic attractor census* (2026): https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-rounding-placement-changes-the-complete-binary16-logistic-attrac--ec3a649c6929
- *Two exact binary16 logistic cycle spectra under algebraically equivalent evaluation* (2026): https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-two-exact-binary16-logistic-cycle-spectra-under-algebraically-eq--35a3ca4a276d
- M. Klöwer, P. V. Coveney, E. A. Paxton and T. N. Palmer, *Periodic orbits in chaotic systems simulated at low precision*, *Scientific Reports* **13** (2023), 11410, https://doi.org/10.1038/s41598-023-37004-4.
- R. M. Corless, *Floats for Philosophers: A Talk in Three Parts* (2024), https://rcorless.github.io/FloatsForPhilosophers.pdf.
