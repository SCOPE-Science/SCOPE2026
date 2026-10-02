# Szeged–Wiener equality for graphs with an \((n-2)\)-clique

## Status and provenance

The mathematics in this record is correct. An independent audit on 30 September 2026
found, however, that the original originality framing omitted an earlier SCOPE result.
The broader record

`2026/09/18/szeged-wiener-equality-clique-n-minus-two--a84aa8e708f8`

was committed at **2026-09-18 03:47:31 UTC** (commit
`c0fc87c28df975025d87707c9327bc68127a1d1c`) and already proved the same
\((n-2)\)-clique equality classification and the same three four-parameter formulas,
using the opposite convention for the two classes "adjacent to both" and "adjacent to
neither". This record, `2026/09/19/szeged-wiener-equality-near-complete-graphs--9ebf1703573f`, first appeared at
**2026-09-19 09:46:00 UTC**. It is therefore retained as a later independent
presentation/reproducibility package, not as a separate discovery. No priority or
dependence inference beyond the repository chronology is made.

## Theorem

Let \(G\) be a 2-connected graph of order \(n\ge10\) containing a clique
\(Q\cong K_{n-2}\). Let the two outside vertices be \(x,y\), and put
\[
A=N_Q(x)\setminus N_Q(y),\quad
B=N_Q(y)\setminus N_Q(x),\quad
C=N_Q(x)\cap N_Q(y),\quad
D=Q\setminus(N_Q(x)\cup N_Q(y)),
\]
with sizes \(a,b,c,d\). Then:

- if \(xy\in E(G)\),
  \[
  \eta(G)=8ab+2ac+3ad+2bc+3bd+4cd-4d;
  \]
- if \(xy\notin E(G)\) and \(c>0\),
  \[
  \eta(G)=5ab+2ac+2ad-2a+2bc+2bd-2b+4cd+2c-4d-2;
  \]
- if \(xy\notin E(G)\) and \(c=0\),
  \[
  \eta(G)=5ab+2ad-a+2bd-b-4d-3.
  \]

Consequently \(\eta(G)=2n\) if and only if, up to exchanging \(x,y\),

1. \(xy\in E(G)\), \((a,b,c,d)=(1,1,0,n-4)\); or
2. \(n=10\), \(xy\in E(G)\), \((a,b,c,d)=(1,0,1,6)\).

Thus for \(n\ge11\) the Zhang–Li equality family is the unique equality type
within \(\omega(G)\ge n-2\), while order 10 has one additional isomorphism type.

## Verification of the formulas

For clique edges, only \(x,y\) can distinguish the endpoints. Grouping clique
vertices by the four membership types gives the exact clique-edge contribution
\[
\binom{n-2}2+3ab+ac+ad+bc+bd+2cd.
\]
The remaining contributions are computed separately for \(xy\) present, \(xy\)
absent with a common clique neighbor, and \(xy\) absent without one. Subtracting
the corresponding Wiener index gives the three displayed formulas.

The two-connectivity conditions are exact: with \(xy\) present one needs
\(a+c\ge1\), \(b+c\ge1\), and \(a+b+c\ge2\); without \(xy\), one needs
\(a+c\ge2\) and \(b+c\ge2\). Substituting these into \(\eta(G)=2n\) reduces
the classification to elementary nonnegative-integer equations. The adjacent case
gives the infinite \((1,1,0,n-4)\) family and the unique order-10 exceptional
type; the nonadjacent cases have no solution of order at least 10.

The existing standard-library verifier in this record remains applicable. The
independent audit additionally reconstructed the graph from the four parameters and
checked the formulas directly from all-pairs distances and Szeged edge counts on a
finite exhaustive range, and separately enumerated the equality equation through
\(n=42\); it found exactly the two stated equality types.

## Relation to the earlier SCOPE theorem

The earlier 18 September record labels the class adjacent to neither outside vertex
by \(C_0\) and the class adjacent to both by \(D_0\). Its adjacent formula is
\[
8ab+3C_0(a+b)+2D_0(a+b)+4C_0D_0-4C_0.
\]
Substituting \(C_0=d\), \(D_0=c\) gives the first formula above exactly, and the
two nonadjacent formulas transform in the same way. The equality tuples likewise
become the two types above. Hence the scientific content of this record is a later
rederivation of an already-present SCOPE theorem.

## External literature context

Zhang and Li, arXiv:2609.20025 (17 September 2026), prove the \(2n\) lower bound,
construct equality examples, and explicitly pose characterization of all equality
cases. Bonamy–Knor–Lužar–Pinlou–Škrekovski (2017) prove the earlier \(2n-6\)
bound and classify that older equality case. These external sources do not alter the
internal-provenance correction above.

## Scientific value and limitations

After the provenance correction, this record remains useful as an alternate derivation
and reproducibility package for the high-clique theorem. Its value is corroborative,
not an independent advance beyond the earlier 18 September SCOPE record.

The theorem only treats graphs with clique number at least \(n-2\); the global
Zhang–Li equality problem remains open. Finite computation supports but does not
replace the symbolic proof. Very recent external parallel work remains possible.

## References

1. SCOPE record `2026/09/18/szeged-wiener-equality-clique-n-minus-two--a84aa8e708f8`,
   commit `c0fc87c28df975025d87707c9327bc68127a1d1c`.
2. L. Zhang and E. Li, *Improved Bounds on the Szeged-Wiener Gap and the BKLPS
   Conjecture*, arXiv:2609.20025 (2026).
3. M. Bonamy, M. Knor, B. Lužar, A. Pinlou, and R. Škrekovski,
   *On the difference between the Szeged and the Wiener index*,
   Applied Mathematics and Computation 312 (2017), 202–213.
