# A ten-wave nineteen-clock and exact majority basins on the cyclic tournament of order nineteen

## Finding: the exact basin and first-entry census

In the consecutive-offset tournament on \(\mathbb Z/19\mathbb Z\), with arcs \(i\to i+j\) for \(1\le j\le9\), use synchronous binary strict majority over out-neighbors. The contribution here is the **exact attraction-basin sizes and first-periodic-entry times** for all \(2^{19}=524{,}288\) labelled starting configurations. Every configuration reaches the recurrent set in at most four updates, and exactly 3,306 require all four. For the update map \(F\), this gives
\[
F^{23}=F^4,\qquad F^{22}\ne F^3.
\]
The least mask requiring four updates is 21391.

The recurrent set itself is prior-implied: the theorem of Nakar and Ron [2] and the rotating-frame identity below give the two unanimous equilibria and the ten period-nineteen block waves. These are the basin labels, not an independent originality claim. Each unanimous state attracts **137,903** labelled starting states. For each \(k\), the basin of the single temporal orbit of \(1^k0^{19-k}\), counting all phases, is as follows:

| Ones in the block \(k\) | Full orbit basin |
|---:|---:|
| 5 | 13,376 |
| 6 | 18,202 |
| 7 | 24,947 |
| 8 | 34,200 |
| 9 | 33,516 |
| 10 | 33,516 |
| 11 | 34,200 |
| 12 | 24,947 |
| 13 | 18,202 |
| 14 | 13,376 |

The complete first-entry table is:

| Least first-entry update | Eventually unanimous | Eventually period nineteen |
|---:|---:|---:|
| 0 | 2 | 190 |
| 1 | 90,744 | 161,120 |
| 2 | 142,956 | 85,272 |
| 3 | 38,798 | 1,900 |
| 4 | 3,306 | 0 |
| **Total** | **275,806** | **248,482** |

The equally regular Paley tournament at order nineteen provides a degree-matched baseline: it has nine out-neighbors at each vertex and uses the same update protocol, but its published census [1] has 516,764 initial states attracted to unanimity. The new quantitative comparison is 275,806 versus 516,764 out of the same 524,288 masks; the individual block-wave basins and the sharp four-step cutoff further specify the difference on the consecutive-offset graph. The Paley counts are not claimed as new.

## Model and conventions

Configurations are binary vectors on labelled vertices, indexed modulo nineteen. The deterministic update is
\[
F(x)_i=\mathbf 1\!\left\{\sum_{j=1}^9 x_{i+j}\ge5\right\}.
\]
There are no ties and no self-neighbors in \(F\). Masks encode \(x\) as \(\sum_{i=0}^{18}2^ix_i\). First entry is the least nonnegative iterate at which a periodic state is reached. The period is the least positive return time of that state. An orbit basin includes its recurrent states and all labelled initial configurations eventually reaching any phase of that orbit. There is no quotient by rotation, complement, or relabelling.

## Recurrent states as a corollary of centered majority

Write \((R_sx)_i=x_{i+s}\) and let \(M\) be the centered radius-four majority map using coordinates \(i-4,\ldots,i+4\). Translation invariance gives \(F=R_5 M=M R_5\), hence \(F^t=R_{5t}M^t\). If \(F^p x=x\), then \(M^{19p}x=F^{19p}x=x\), so every \(F\)-periodic state is temporally periodic under \(M\).

Nakar and Ron [2, Theorem 1 and Definition 9] show that a temporally periodic state of centered majority either consists of strongly stable runs of length at least \(r+1\), or is all weakly stable and has a spatial period strictly less than the ring size. On the prime-sized ring of nineteen, invariance under any nonzero rotation forces a constant word, so the latter case gives no additional states. For \(r=4\), any nonconstant state in the former case has alternating runs of length at least five. Four or more such runs would require at least twenty cells; thus there is exactly one run of each color. These are the rotations of \(a_k=1^k0^{19-k}\), \(5\le k\le14\). Each stays fixed under \(M\): any site in a run of length at least five sees at least five sites of its own color in its radius-four window. Constants are likewise fixed under \(M\). Therefore \(F(R_s a_k)=R_{s+5}a_k\), with period nineteen since 5 generates \(\mathbb Z/19\mathbb Z\) and the words are nonconstant. This classifies the recurrent states without basin enumeration.

## Exact enumeration of transients and basins

One independent way to reproduce the census is to enumerate in the centered frame, whose entry condition is simpler. Let \(A\) be the set of the two constants and all rotations of \(a_k\) for \(5\le k\le14\); let the class of a member be the length \(k\) of its one-run, with classes 0 and 19 for the constants. Since \(A\) and these classes are rotation invariant, \(F^t x\) first enters \(A\) at exactly the same \(t\) as \(M^t x\), in the same class. Every nonconstant class is a single temporal orbit for \(F\).

The finite sweep can be stated as follows, with all bit indices taken modulo nineteen:

```text
Build A and its class labels by rotating (1 << k) - 1, k = 5,...,14,
and include masks 0 and (1 << 19) - 1.
For each mask x from 0 to (1 << 19) - 1:
    s := sum of bits x[-4],...,x[4];  y := 0
    For i = 0,...,18:
        If s >= 5, set bit i of y.
        s := s - x[i-4] + x[i+5]
    M[x] := y
For each mask x from 0 to (1 << 19) - 1:
    y := x;  t := 0
    While y is not labelled and t < 4:
        y := M[y];  t := t + 1
    Require y to be labelled.
    Increment the basin total for class(y) and entry count for (t, period(class(y))).
```

Every membership requirement passes. The loops count each labelled input once at its earliest entry; the cutoff is checked on the full domain, not inferred from a sample. The table gives the exact populations. In the original vertex labels, the masks under \(F\) from 21391 are \(21391,401507,235520,1792,0\); none of the first four masks is recurrent. On \(A\), \(F^{19}\) is the identity. Off \(A\), equality \(F^{19}y=y\) would make \(y\) recurrent. Hence all states satisfy \(F^{23}x=F^4x\) and the 3,306 depth-four states are exactly the exceptions to \(F^{22}x=F^3x\).

## Reproduction with the supporting programs

`python3 verify_functional.py` constructs the out-neighbor successor of every mask, follows each component of the deterministic functional graph, identifies cycles by exact repetition, and propagates entry depths and basin assignments backward. It writes the exact census to standard output; `--json output_functional.json` also saves it to a file. It does not need the centered-rule theorem to find its recurrent set.

`c++ -std=c++17 -O2 -Wall -Wextra verify_direct.cpp -o verify_direct && ./verify_direct` reproduces the table using nine individual bit tests for each vertex's update and testing exact nineteen-update return for every state. It independently reports the number of failures of the predecessor identity and checks the Paley baseline using offsets generated as nonzero squares modulo nineteen. The preserved outputs are `output_functional.json` and `output_direct.txt`. The supporting computations are complete for this finite rule, not simulations intended to generalize to other orders.

## Prior coverage and limitations

The centered majority structure theorem [2] already implies the recurrent set as explained above; its qualitative transient restrictions do not give this exact basin table, entry-time histogram, or sharp order-nineteen cutoff. The prior Paley analysis [1] gives two unanimous fixed states, 342 primitive period-four cycles and 18 primitive period-nineteen cycles. Its attraction totals are respectively 516,764, 6,156 and 1,368, with sharp first-entry depth seven. It also rules out two-cycles in tournaments and nonunanimous fixed states in regular tournaments. Those facts are credited, not claimed here. The separate order-twenty-three comparison [3] reports an exact census for a different ring size and radius; its carousel also has depth four, but it does not give the order-nineteen attraction or first-entry counts.

This census concerns only the stated nineteen-site rule. It asserts no law for the depth, wave-basin populations, or consensus-versus-wave contrast at other orders. Prior coverage of the structural recurrent-set statement is explicit, and older unindexed computations of the remaining finite census cannot be ruled out.

## References

1. *A forbidden two-clock and the Paley-19 revival of majority oscillations*, [published result](https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-a-forbidden-two-clock-and-the-paley-19-revival-of-majority-oscil--13a06d889156/RESULT.md).
2. Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, [arXiv:2205.08972](https://arxiv.org/abs/2205.08972), Definitions 7–9 and Theorem 1.
3. *Two degree-matched tournaments separate into exclusive four- and twenty-three-step majority clocks*, [published result](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-two-degree-matched-tournaments-separate-into-exclusive-four-and--d6a7bd7d1f44/RESULT.md).
