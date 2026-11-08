# Simultaneous Upper, Near, and Extended Justified Representation with Two Approval Ballots

## Finding

**Theorem.** In every approval-based multi-winner election in which voters submit at most two distinct nonempty approval ballots, every candidate is approved by at least one voter, and the number of available candidates is at least the target committee size, there is an exhaustive committee satisfying **justified upper quota (JUQ)**, **justified near quota (JNQ)**, and **extended justified representation plus (EJR+)** simultaneously. A committee can be constructed by counting the three possible candidate-support types and selecting a prescribed number from each type. The construction uses linear time in the explicit voter/candidate input, apart from reading the input.

This includes elections with overlapping, nonidentical approval ballots; it is not restricted to disjoint-party apportionment. It establishes exhaustive joint feasibility on a natural restricted domain, not for unrestricted approval elections.

## Assumptions and scope

Let \(N\) be a set of \(n\ge1\) voters, \(C\) a finite candidate set, and \(1\le k\le |C|\). Each voter \(i\) has a nonempty approval ballot \(A_i\subseteq C\). Assume \(A_i\) takes at most two distinct values and \(N(c)=\{i:c\in A_i\}\ne\varnothing\) for every candidate \(c\). A committee \(W\subseteq C\) is **exhaustive** when \(|W|=k\); a voter's satisfaction is \(s_i(W)=|A_i\cap W|\). Write \(q(S)=k|S|/n\) for a voter set \(S\).

We use the following exact definitions from Baychkov–Lackner–Maly–Nardi–Peters (2026):

* **EJR+:** no \(d\in C\setminus W\) and nonempty \(S\subseteq N(d)\) have \(s_i(W)<\lfloor q(S)\rfloor\) for **every** \(i\in S\).
* **JUQ:** no \(c\in W\), \(d\in C\setminus W\), and nonempty \(S\subseteq N(d)\) satisfy both \(s_i(W)>\lceil q(N(c))\rceil\) for **every** \(i\in N(c)\) and \(s_i((W\setminus\{c\})\cup\{d\})\le\lceil q(S)\rceil\) for **every** \(i\in S\).
* **JNQ:** no such \(c,d,S\) satisfy both
  \[s_i(W)-q(N(c))>\tfrac12\mathbf 1[d\notin A_i]\quad(i\in N(c))\]
  and
  \[q(S)-s_i(W)>\tfrac12\mathbf 1[c\notin A_i]\quad(i\in S).\]

If all voters have one ballot, the theorem is immediate: every candidate is approved by everyone and any \(k\) candidates give satisfaction \(k\). Otherwise, partition the voter set into positive-size types \(N_A,N_B\) of sizes \(n_A,n_B\), with distinct ballots. Each candidate has support either \(N_A\) alone (\(A\)-private), \(N_B\) alone (\(B\)-private), or all voters (common). Denote the respective inventories by \(u,v,w\). Let
\[Q=\frac{k n_A}{n_A+n_B},\qquad h=\lfloor Q\rfloor,\qquad z=\min(w,k).\]

**Construction.** Select \(z\) common candidates. If \(z=k\), finish. Otherwise every common candidate is selected, and \(t=k-z\) private candidates remain to be chosen. Put
\[L=\max(0,t-v),\qquad U=\min(u,t),\]
so the number \(a\) of selected \(A\)-private candidates can be any integer in \([L,U]\). Define the target
\[a_0=\begin{cases}h,&z\ge1,\\ \lfloor Q+\tfrac12\rfloor,&z=0,\end{cases}\qquad a=\min\{U,\max\{L,a_0\}\}.\]
Choose \(a\) arbitrary \(A\)-private candidates, \(b=t-a\) arbitrary \(B\)-private candidates, and the \(z\) common candidates. The resulting type satisfactions are
\[s_A=z+a,\qquad s_B=z+b=k-a.\]
The inventory inequality \(u+v+w\ge k\) guarantees \(L\le U\). No tie-breaking over voters is needed.

## Proof

If \(z=k\), the committee consists entirely of common candidates and every voter has satisfaction \(k\). Every EJR+ demand is met, and no selected candidate can witness a JUQ/JNQ violation because its full-support quota is \(k\). Thus assume \(z<k\).

We first record a support-type reduction. A nonempty subset of the supporters of an \(A\)-private candidate is entirely of type \(A\), and the maximum of its quotas is \(Q\). Likewise, a subset of \(B\)-private supporters has quota at most \(k-Q\). Whenever \(z<k\), no common candidate is unselected. Hence EJR+ holds precisely when \(s_A\ge\lfloor Q\rfloor\) whenever an \(A\)-private candidate is unselected, and \(s_B\ge\lfloor k-Q\rfloor\) whenever a \(B\)-private candidate is unselected. Indeed, reducing the witness subset only decreases its quota, and all voters of one type have identical satisfaction.

For JUQ or JNQ, a selected common candidate cannot be a donor: its supporter quota is \(k\), while every voter has satisfaction at most \(k\). A selected and an unselected candidate of the same private type cannot witness a violation: the relevant voters' satisfaction is unchanged by their swap, whereas JUQ requires simultaneous strict overrepresentation and satisfaction no greater than the upper quota; JNQ would require the same satisfaction to lie strictly on both sides of a quota not exceeding the full type quota. Thus only swaps between \(A\)-private and \(B\)-private candidates need consideration.

**Case 1: at least one common candidate is selected (\(z\ge1\)).** For an unclipped choice \(a=h\), the type satisfactions are \(s_A=z+h\) and \(s_B=k-h\). EJR+ follows from \(s_A\ge h\) and \(s_B\ge\lfloor k-Q\rfloor\). A selected \(B\)-private candidate cannot be a JUQ donor, because \(s_B=k-h=\lceil k-Q\rceil\). A selected \(A\)-private candidate cannot witness JUQ with an unselected \(B\)-private candidate: after this swap the type-\(B\) satisfaction is \(k-h+1>\lceil k-Q\rceil\), hence larger than the upper quota of every subset of \(N_B\). For JNQ, the type-\(B\) satisfaction is at or above its quota \(k-Q\), so it is not a recipient of an \(A\)-to-\(B\) swap. Conversely, the type-\(A\) satisfaction \(z+h\) is at or above \(Q\), because \(z\ge1\) and \(Q<h+1\); it cannot be the recipient of a \(B\)-to-\(A\) swap. Thus all three axioms hold.

If clipping gives \(a>h\), necessarily \(a=L=t-v\), so **all** \(B\)-private candidates are selected. An \(A\)-to-\(B\) witness is therefore impossible. A \(B\)-to-\(A\) witness is impossible because the selected \(B\)-private donor's voters have \(s_B=k-a<k-h=\lceil k-Q\rceil\) and \(s_B<k-Q\), violating the donor condition of both JUQ and JNQ. An unselected \(A\)-private candidate is EJR+-safe since \(s_A=z+a\ge h\); there is no unselected \(B\)-private candidate.

If clipping gives \(a<h\), necessarily \(a=U=\min(u,t)\). When \(a=u\), all \(A\)-private candidates are selected, while the \(A\)-private donors have \(s_A=z+a\le z+h-1\), but a simpler argument suffices: the only potential cross-type donor is \(A\), and a \(B\)-recipient has \(s_B=k-a>k-h=\lceil k-Q\rceil\ge k-Q\). It cannot be under its quota for either JUQ (after the swap it gains another unit) or JNQ. When \(a=t<h\), no \(B\)-private candidate is selected, \(s_A=k\), and \(s_B=z=k-t>k-h=\lceil k-Q\rceil\). Again a \(B\)-recipient cannot witness either axiom. In both subcases, EJR+ holds because any unselected \(B\)-private candidate has satisfaction at least \(k-h\ge\lfloor k-Q\rfloor\), and any unselected \(A\)-private candidate is absent (or, in the \(a=t\) subcase, all available private \(A\) candidates are selected since \(a=U=t\le u\) but extra \(A\) candidates may remain; their satisfaction is \(k\ge h\)).

**Case 2: no common candidate exists (\(z=0\)).** Now \(a+b=k\), and the unclipped target \(a_0=\lfloor Q+1/2\rfloor\) is a nearest integer to \(Q\). If \(a=a_0\), both type satisfactions differ from their quotas by at most \(1/2\). Consequently JNQ has no strictly overrepresented donor, both types meet their lower quotas (so EJR+), and neither exceeds its upper quota (so JUQ).

If \(a>a_0\), then \(a=L=k-v\) and every \(B\)-private candidate is selected. The selected \(B\)-private candidates are not over quota, because \(a\ge a_0+1>Q+1/2\), so \(k-a<k-Q-1/2\). No \(B\)-recipient is available, and any unselected \(A\)-private candidate has \(a\ge\lfloor Q\rfloor\). Thus all three axioms hold. Symmetrically, if \(a<a_0\), necessarily \(a=U=u\), all \(A\)-private candidates are selected, and selected \(A\)-private candidates are not above quota; any unselected \(B\)-private candidate receives \(b=k-a\ge\lfloor k-Q\rfloor\). Again all three axioms hold.

This covers every inventory and every integer committee size, including zero inventories and boundary quotas. The construction selects exactly \(k\) candidates and proves the theorem. \(\square\)

## Verification

The standalone `check.py` implements the construction using exact rational arithmetic. One checker literally enumerates **every nonempty voter subset** in the EJR+, JUQ, and JNQ definitions; another checks type-aggregated supporter subsets on a wider parameter range. Its deterministic run produced:

```
PASS: literal voter-subset cases 2457
PASS: extended type-aggregate cases 1110400
PASS: boundary example
```

Run `python check.py` with a standard Python 3 interpreter; no external packages are needed. These computations check the construction against the definitions at finite sizes; the proof above establishes the unbounded result.

A separation from **unjustified** upper quota shows why the weaker JUQ notion matters even here: with one voter of each type, \(k=2\), one common candidate, and one \(B\)-private candidate, the only exhaustive committee selects both; the type-\(B\) voter gets two approved winners against upper quota one. All three *justified* axioms nevertheless hold, since there is no unselected candidate.

## Relationship to prior work

Lackner and Nardi (2025) introduce upper-quota axioms and flag the near-quota direction. Baychkov, Lackner, Maly, Nardi and Peters (2026) formally define JUQ and JNQ, analyze their separate satisfiability, show simultaneous UQ/JNQ/EJR+ when **nonexhaustive** committees are allowed, and explicitly leave even **pairwise** compatibility open for exhaustive committees in general. Their statements do not imply the present exact-size joint theorem. Classical two-party apportionment is the special case with no common candidates; the present result also covers arbitrary overlap, for which simple lower/upper apportionment rounding does not directly decide all three justified axioms. The proof is constructive and specific to at most two approval ballots.

## Limitations

The theorem does **not** assert the three axioms are jointly feasible for three or more distinct ballots, nor does it resolve the unrestricted exhaustive-committee compatibility question. It assumes every candidate has a supporter, positive voter-type sizes when the two ballots differ, and \(k\le|C|\). The proof is mathematical but has not been independently audited. The exact calculation checks sample only finite cases and should not be mistaken for an exhaustive check of all input sizes.

## References

1. M. Lackner and O. Nardi, *Avoiding Overrepresentation: Upper Quota Axioms for Committee Voting*, M-PREF 2025 workshop, October 25, 2025. https://olinarr.github.io/files/publications/pdf/LacknerAndNardiMPREF2025.pdf
2. A. Baychkov, M. Lackner, J. Maly, O. Nardi, J. Peters, *Beyond Lower Quota: Avoiding Overrepresentation in Multi-Winner Voting*, arXiv:2606.19968v1, first posted June 18, 2026. https://arxiv.org/html/2606.19968v1
