# Exact period ten for ternary order-three negative orientable sequences

## Finding

Let \(M_3(3)\) be the largest period of a cyclic negative orientable sequence of order three over \(\mathbb{Z}_3\). Then

\[
\boxed{M_3(3)=10}.
\]

In particular, the cyclic word `0100112111` attains this maximum. Its ten cyclic length-three windows occupy ten different classes under reversal followed by additive negation. The new part is the sharp upper bound; the length-ten witness was previously published.

## Assumptions and scope

The alphabet is the additive group \(\mathbb{Z}_3=\{0,1,2\}\), with negation taken modulo three. For a cyclic word \(s_0\ldots s_{m-1}\) of positive period \(m\), indices are interpreted modulo \(m\). Its length-three windows are \(w_i=(s_i,s_{i+1},s_{i+2})\). Put \(J(a,b,c)=(-c,-b,-a)\). We require that each window appears at most once and that \(w_i\ne J(w_j)\) for every pair of indices, including coincident indices. Equivalently, no two windows share a class under the involution \(J\). This is the standard negative-orientability definition for alphabet size three and window order three.

A triple is fixed by \(J\) precisely when it is one of \(000,102,201\). The remaining \(24\) triples give \(12\) pairs, so every admissible period is at most \(12\).

## Proof

View a triple \((a,b,c)\) as a directed edge from vertex \((a,b)\) to vertex \((b,c)\) in the order-two ternary de Bruijn digraph. The window edges of a cyclic word form a directed closed trail; hence every vertex has even total incidence degree (loops counted twice), and every vertex cut has an even number of crossing edges.

The involution on the vertices induced by \(J\) is \(j(a,b)=(-b,-a)\). If a triple has endpoints \(u,v\), its partner under \(J\) has endpoints \(j(v),j(u)\). Thus, for each vertex fixed by \(j\), the parity of its incidence degree contributed by one edge is independent of the selected representative in a \(J\)-class. Likewise, for any vertex subset invariant under \(j\), an edge and its partner agree on whether they cross its boundary.

The three fixed vertices are \(F=(00,12,21)\). Take the invariant vertex cut \(T=\{02,10\}\). For each lexicographically minimal nonfixed \(J\)-orbit representative \(t\), let \(\sigma(t)\) be its incidence parity vector on \(F\), and let \(\kappa(t)\in\{0,1\}\) indicate whether its edge crosses \(T\). Direct endpoint inspection gives the following complete finite table; each row denotes an entire two-element \(J\)-orbit:

| Representative | \(\sigma\) on \((00,12,21)\) | \(\kappa\) |
| :--- | :---: | :---: |
| `001` | `100` | 0 |
| `002` | `100` | 1 |
| `010` | `000` | 1 |
| `011` | `000` | 0 |
| `012` | `010` | 0 |
| `021` | `001` | 1 |
| `022` | `000` | 1 |
| `101` | `000` | 1 |
| `111` | `000` | 0 |
| `112` | `010` | 0 |
| `121` | `011` | 0 |
| `211` | `001` | 0 |

The bitwise parity sum of all twelve \(\sigma\) vectors is \(011\). The sum of the twelve \(\kappa\) values is \(5\).

Suppose an admissible cyclic word had period \(12\). It would use exactly one triple from every nonfixed \(J\)-orbit. Its closed trail would consequently have five edges crossing \(T\), an odd number, contradicting closedness. Thus period \(12\) is impossible.

Suppose instead that an admissible cyclic word had period \(11\). Then it would use one edge from all but one of the twelve \(J\)-orbits. Even incidence degree at each of the three fixed vertices forces the omitted orbit's incidence parity vector to equal \(011\), because the all-orbit parity sum is \(011\). Inspection of the complete table shows that only the orbit represented by `121` has that vector. But its cut indicator is zero. Hence the eleven remaining orbit choices still contribute exactly five crossings of the invariant cut \(T\), again an impossibility for a closed trail. Thus period \(11\) is impossible.

For the lower bound, the word `0100112111` is a length-ten cyclic word. Its windows, in starting-position order, are

`010, 100, 001, 011, 112, 121, 211, 111, 110, 101`.

These are not fixed by \(J\), and their distinct orbit representatives are

`010, 002, 001, 011, 112, 121, 211, 111, 022, 101`.

All ten representatives differ, so the cyclic word is negative orientable. Combining existence with the exclusion of period \(11\), period \(12\), and all larger periods yields \(M_3(3)=10\).

## Verification

Run `python3 check.py` using Python's standard library. `check.py` independently constructs the \(27\) ternary triples, the twelve nonfixed \(J\)-orbits, the fixed-vertex incidence signatures and cut indicators, and the witness's cyclic windows. It additionally tests all \(3^{10}+3^{11}+3^{12}=767637\) labeled ternary cyclic words of lengths \(10\), \(11\), and \(12\) directly, without using the parity table for its acceptance criterion. The observed counts are \(320,0,0\), respectively. The recorded console output is `check.out`. The infinite sharp bound is established by the mathematical parity argument; the exhaustive experiments are independent finite consistency checks.

## Relationship to prior work

Mitchell and Wild, *New upper bounds for the period of a negative orientable sequence* (public preprint dated February 4, 2026), give the previous upper bound \(11\) for this particular alphabet and order. Their Table 2 records an attained period of \(10\) and upper bound \(11\), and their conclusion explicitly identifies the exact small-order maximum as unresolved. The current result closes precisely that one-unit gap, with an elementary invariant-cut obstruction not supplied by that theorem.

Mitchell and Wild, *Orientable and negative orientable sequences* (2024 preprint, subsequently published in 2025), describe a period-ten example, including `0100112111`, but their available upper bound does not exclude period eleven. Their March 2026 paper on asymptotically optimal constructions again supplies a period-ten ternary order-three construction; it gives no sharp matching bound for this parameter. The earlier work of Alhakim and collaborators supplies the definitions and general construction framework. None of those inspected results establishes the two-cut upper-bound argument here.

## Limitations

This is an exact theorem only for alphabet size three and window order three; it neither determines maximal periods for larger alphabets/orders nor claims to classify all period-ten maximizers. The exhibited length-ten word is previously known. The assessment of originality is limited to the cited primary texts and targeted record searches; unindexed or differently formulated earlier proofs remain possible. Independent scientific validation has not been performed.

## References

1. C. J. Mitchell and P. R. Wild, *New upper bounds for the period of a negative orientable sequence*, arXiv:2602.04433, first public version February 4, 2026, especially Table 2 and Section 4. https://arxiv.org/abs/2602.04433
2. C. J. Mitchell and P. R. Wild, *Constructing orientable and negative orientable sequences with asymptotically optimal period*, arXiv:2603.18646, March 19, 2026, Table 2 and Section 5.1. https://arxiv.org/html/2603.18646v1
3. C. J. Mitchell and P. R. Wild, *Orientable and negative orientable sequences*, arXiv:2409.00672 (2024); *Discrete Applied Mathematics* 377 (2025), 242–259, doi:10.1016/j.dam.2025.06.052.
4. A. Alhakim et al., *Orientable sequences over non-binary alphabets*, *Cryptography and Communications* 16 (2024), 1309–1326, doi:10.1007/s12095-024-00742-x.
