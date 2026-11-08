# Exact attractor size and pair geometry of four-run binary words

## Finding

Let \(a,b,c,d\) be arbitrary positive integers and define the binary word
\[
W_{a,b,c,d}=0^a1^b0^c1^d.
\]
For a finite word \(W\), a **string attractor** is a set \(\Gamma\) of positions such that every distinct nonempty contiguous factor of \(W\) has at least one occurrence containing a position of \(\Gamma\). Write \(\gamma(W)\) for its minimum cardinality.

**Theorem (sharp four-run phase diagram).** For all positive \(a,b,c,d\),
\[
\gamma(W_{a,b,c,d})=
\begin{cases}
3,& (a>c\ \text{and}\ d>b)\ \text{or}\ (c\ge a+2\ \text{and}\ b\ge d+2),\\
2,&\text{otherwise}.
\end{cases}
\]
The two strict obstruction regimes are disjoint. In particular, no four-run binary word ever needs more than three attracting positions.

For \(a,b,c,d\ge2\), there is an additional complete classification of **every two-position attractor**. Define six one-based positions
\[
p=a,\quad q=a+1,\quad L=a+b,\quad R=a+b+1,\quad r=a+b+c,\quad s=a+b+c+1.
\]
The following are all the possibilities; each listed pair is an attractor if and only if the corresponding condition holds:

| Attractor pair | Necessary and sufficient condition |
|---|---|
| \(\{p,L\}\) | \(a\ge c\) and \(b\ge d\) |
| \(\{L,r\}\) | \(c\ge a\) and \(d\le b\le d+1\) |
| \(\{q,R\}\) | \(a\le c\le a+1\) and \(b\ge d\) |
| \(\{R,s\}\) | \(c\ge a\) and \(d\ge b\) |

All four pairs are distinct in this parameter range. The exact number of two-position attractors is therefore the sum of the four condition indicators, an integer from zero to four. When it is positive, these are precisely the minimum attractors; when it is zero, the minimum size is three.

## Assumptions and scope

Positions are numbered from one, including both endpoints of their occurrences. Repetition exponents are positive integer run lengths and the alphabet is exactly \(\{0,1\}\). A factor is contiguous, not a scattered subsequence. Different occurrences of the same factor may be chosen when testing the attractor property. The size formula includes singleton runs, whereas the complete pair list assumes all four runs have length at least two. There is no claim about the number of minimum triples in the size-three regime.

## Proof

**1. The unique central transition and the four pair candidates.** The factor \(10\) has exactly one occurrence, in positions \(L,R\). Every occurrence of a factor containing at least two symbol changes must cross this transition: the word's changes are \(01\), \(10\), \(01\) in that order. Hence marking either \(L\) or \(R\) meets all factors with at least two changes, as well as the factor \(10\).

A two-position attractor must mark \(L\) or \(R\), because of the unique \(10\). Since both single-letter factors must be attracted and \(L\) is a one while \(R\) is a zero, the other mark must have the opposite symbol. Moreover, the factor \(01\) occurs only at positions \(p,q\) and \(r,s\). Neither \(L\) nor \(R\) belongs to those occurrences when all run lengths are at least two. If \(L\) is selected, the second mark, necessarily a zero, must be \(p\) or \(r\). If \(R\) is selected, the second mark, necessarily a one, must be \(q\) or \(s\). Thus the four displayed candidates exhaust all two-position attractors under the nondegeneracy assumption.

**2. Single-run factors.** The longest pure zero and pure one factors have lengths \(\max(a,c)\) and \(\max(b,d)\). The pair \(\{p,L\}\) can attract all pure factors only if \(a\ge c\) and \(b\ge d\), and these inequalities suffice for pure factors. The pair \(\{R,s\}\) similarly requires and suffices for \(c\ge a\), \(d\ge b\). For \(\{L,r\}\), the conditions are \(c\ge a\), \(b\ge d\); and for \(\{q,R\}\), they are \(c\ge a\), \(b\ge d\). These are necessary: a pure run longer than either marked run cannot have an occurrence containing the relevant mark.

**3. One-change factors.** Every such factor is of the form \(0^i1^j\), with \(i,j\ge1\), and crosses either the first or the last \(01\) boundary. At the first boundary it exists exactly when \(i\le a\), \(j\le b\); at the last exactly when \(i\le c\), \(j\le d\). At the first boundary, an occurrence contains \(p\) and \(q\) automatically; it contains \(L\) only when \(j=b\). At the last boundary an occurrence contains \(r\) and \(s\) automatically; it contains \(R\) only when \(i=c\).

Under \(a\ge c,b\ge d\), every one-change factor at the last boundary is reproduced at the first boundary, where it crosses \(p\); hence \(\{p,L\}\) attracts all such factors. Under \(c\ge a,d\ge b\), the symmetric argument at the last boundary proves sufficiency of \(\{R,s\}\).

For \(\{L,r\}\), pure-run coverage first demands \(c\ge a,b\ge d\). All factors crossing the last boundary contain \(r\). A first-boundary factor with \(j\le d\) also appears at the last boundary because \(c\ge a\), so it is covered by \(r\). If \(j>d\), it cannot appear at the last boundary; at the first it meets \(L\) only for \(j=b\). All such factors are covered if and only if there is no integer strictly between \(d\) and \(b\), namely \(b\le d+1\). This gives \(c\ge a\) and \(d\le b\le d+1\).

For \(\{q,R\}\), pure-run coverage first demands \(c\ge a,b\ge d\). All first-boundary factors meet \(q\). A last-boundary factor with \(i\le a\) also occurs at the first boundary, so is covered by \(q\). If \(i>a\), it is exclusive to the last boundary and meets \(R\) only when \(i=c\). Thus all such factors are covered if and only if \(c\le a+1\). This gives \(a\le c\le a+1\) and \(b\ge d\). Together with Step 1 and the central transition, these arguments prove the complete pair classification.

**4. A three-position upper bound without nondegeneracy.** Put \(L=a+b\). Choose a zero position \(Z=p\) if \(a\ge c\), and \(Z=r\) otherwise. Choose a one position \(O=q\) if \(b\ge d\), and \(O=s\) otherwise. Then \(\{L,Z,O\}\) is a string attractor (regardless of whether runs have length one): \(Z,O\) cover every pure run factor up to the maximum length of its symbol; \(L\) covers the unique \(10\) and every factor with at least two changes. For a one-change factor, if the first boundary is marked, it is covered there; if the first is not marked, then \(c>a\) and \(d>b\) force the last boundary to be marked and to reproduce every first-boundary one-change factor. More explicitly, the choices produce boundary coverage: when \(a\ge c\), \(p\) covers the first boundary; when \(b\ge d\), \(q\) covers the first boundary; when \(a<c\) and \(b<d\), \(s\) covers the last boundary and its run capacities dominate the first. In the mixed cases, \(p\) or \(q\) covers the first and \(r\) or \(s\) covers the last. Thus \(\gamma\le3\). No binary word containing both symbols can have a one-position attractor, since the single-letter factors \(0\) and \(1\) would demand two distinct marked positions.

**5. The exact phase diagram including singleton runs.** If \(a>c,d>b\), the unique occurrence of the maximal pure-zero factor \(0^a\) lies in the first run and the maximal pure-one factor \(1^d\) lies in the last run. Two marks forced into those separated runs cannot hit the unique central \(10\), so \(\gamma=3\).

If \(c\ge a+2,b\ge d+2\), then automatically \(b,c\ge3\). When the outer run lengths \(a\) or \(d\) equal one, the candidate-exhaustion argument still applies: the unique factor \(01\) can intersect the center \(L\) only when \(b=1\), and can intersect \(R\) only when \(c=1\). Both are impossible here. The four pair candidates thus remain exhaustive; all four fail the displayed conditions, proving \(\gamma=3\).

Conversely assume neither obstruction. If \(a>c\), then \(b\ge d\), and \(\{p,L\}\) works by the one-change and pure-factor arguments, valid for positive run lengths. If \(c\ge a\) and \(d\ge b\), then \(\{R,s\}\) works. In the remaining case \(c\ge a,b>d\), either \(c\le a+1\), when \(\{q,R\}\) works, or \(c\ge a+2\). The exclusion of the second obstruction then forces \(b\le d+1\), when \(\{L,r\}\) works. These sufficiency arguments hold unchanged for singleton outer runs (overlap with the central transition only helps). Hence outside the two obstruction regimes \(\gamma=2\). This completes both parts of the theorem.

## Verification

Run `python verify_four_runs.py` with Python 3 and no third-party packages. Its first implementation builds, for each distinct factor, the union of all positions in all occurrences and exhaustively tests every marker pair. For all \(1\le a,b,c,d\le6\) (1,296 quadruples), it compares existence of a pair to the theorem's phase diagram; for the 625 nondegenerate quadruples \(2\le a,b,c,d\le6\), it compares the entire list of pairs to the four formulas. A second, separately written check tests factors and occurrences directly, checking canonical three-position witnesses and pairs for 81 smallest quadruples and 100 further fixed-seed larger cases. The resulting output is:

```
FOUR_RUN_ATTRACTOR_VERIFY_OK phase_cases 1296 nondegenerate_exact_pair_cases 625 observed_pairs 1563 independent_direct_instances 181
```

Finite enumeration checks the derivation but does not prove statements for unbounded parameters; the proof above supplies the infinite argument. The four-run witness construction can be checked directly for arbitrary specified inputs independently of enumeration.

## Relationship to prior work

The introduction of string attractors and the structural problem of characterizing binary words with minimum attractor size two are discussed in *String Attractors and Combinatorics on Words* (2019) and in *A combinatorial view on string attractors* (2021). The 2026 work, originally submitted as *The Smallest String Attractors of Fibonacci and Period-Doubling Words* and subsequently extended to include Thue–Morse, investigates optimal attractors for distinguished morphic families. A known exact result for the periodic family \( (0^a1^b)^m \) contains the equal-run four-block case \(a=c,b=d\) at \(m=2\). The present theorem retains that covered specialization but additionally gives a complete four-independent-run-length phase diagram and all nondegenerate marker pairs, including unequal-run cases that the periodic family cannot imply. Neither the inspected statements nor the examined supporting sections of these works provide that phase diagram or pair classification. This is a best-knowledge comparison, not a claim of absolute publication priority.

## Limitations

The pair enumeration is stated only when all run lengths are at least two; singleton runs are included in the cardinality theorem. Four or more symbol changes, larger alphabets, and the number of optimal triples in the size-three region are not classified. A complete global historical-priority survey and independent mathematical validation have not been performed.

## References

- *The Smallest String Attractors of Fibonacci and Period-Doubling Words* (first public version 2026-02-18; later extended to Thue–Morse), https://arxiv.org/abs/2602.16152.
- *String Attractors and Combinatorics on Words* (2019), https://ceur-ws.org/Vol-2504/paper8.pdf.
- *A combinatorial view on string attractors* (2021), https://arpi.unipi.it/retrieve/e0d6c92f-ec13-fcf8-e053-d805fe0aa794/MRRRS_TCS2021.pdf.
