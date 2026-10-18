# PAV collapses exactly to SAV when a committee leaves one candidate unelected
## Finding
Let
\[
C
\]
be a candidate set with
\[
|C|=m\ge2,
\]
and let each voter \(i\) submit a nonempty approval set
\[
A_i\subseteq C.
\]
Fix committee size
\[
k=m-1.
\]

Under Satisfaction Approval Voting (SAV), a committee \(W\) has score
\[
\operatorname{SAV}(W)=\sum_i\frac{|W\cap A_i|}{|A_i|}.
\]

Under Proportional Approval Voting (PAV), a committee \(W\) has score
\[
\operatorname{PAV}(W)=\sum_i H_{|W\cap A_i|},
\]
where
\[
H_r=\sum_{j=1}^{r}\frac1j,\qquad H_0=0.
\]

Then SAV and PAV induce exactly the same weak ordering on all committees of size \(m-1\). In particular, they have exactly the same winning committees and exactly the same ties.

For a candidate \(c\), write
\[
W_c=C\setminus\{c\}
\]
and define its normalized approval support
\[
s(c)=\sum_{i:\,c\in A_i}\frac1{|A_i|}.
\]
Then
\[
\operatorname{SAV}(W_c)=n-s(c)
\]
and
\[
\operatorname{PAV}(W_c)=\sum_i H_{|A_i|}-s(c).
\]

Thus both rules rank one-vacancy committees solely by the same quantity \(s(c)\): a winning committee is obtained by omitting any candidate minimizing \(s(c)\).

This also gives a simple winner-determination regime for PAV. Although general PAV winner determination is NP-hard, when only one candidate is to be excluded, all PAV winners are found by computing the \(m\) normalized approval-support values and omitting a minimum-support candidate.

## Assumptions and scope
Approval ballots are nonempty.

The candidate set is finite, and the committee has exactly one vacancy:
\[
k=m-1.
\]

SAV and PAV are used in their standard approval-based multiwinner forms.

The statement concerns the complete winner correspondence and committee ordering, not merely one tie-broken outcome.

No claim is made that SAV and PAV coincide for arbitrary committee sizes. In general they are distinct rules with different objectives and computational behavior.

## Proof
Fix a voter \(i\), a candidate \(c\), and the one-vacancy committee
\[
W_c=C\setminus\{c\}.
\]

If
\[
c\notin A_i,
\]
then every approved candidate remains in \(W_c\), so
\[
|W_c\cap A_i|=|A_i|.
\]
The voter's SAV contribution is therefore
\[
1,
\]
and the PAV contribution is
\[
H_{|A_i|}.
\]

If
\[
c\in A_i,
\]
then exactly one approved candidate is omitted, so
\[
|W_c\cap A_i|=|A_i|-1.
\]
The SAV contribution is
\[
\frac{|A_i|-1}{|A_i|}
=
1-\frac1{|A_i|},
\]
while the PAV contribution is
\[
H_{|A_i|-1}
=
H_{|A_i|}-\frac1{|A_i|}.
\]

Hence for every voter,
\[
\operatorname{SAV}_i(W_c)
=
1-\mathbf 1_{\{c\in A_i\}}\frac1{|A_i|}
\]
and
\[
\operatorname{PAV}_i(W_c)
=
H_{|A_i|}
-\mathbf 1_{\{c\in A_i\}}\frac1{|A_i|}.
\]

Summing over voters gives
\[
\operatorname{SAV}(W_c)
=
n-
\sum_{i:\,c\in A_i}\frac1{|A_i|}
=
n-s(c),
\]
and
\[
\operatorname{PAV}(W_c)
=
\sum_i H_{|A_i|}
-
\sum_{i:\,c\in A_i}\frac1{|A_i|}
=
\sum_i H_{|A_i|}-s(c).
\]

The two committee-score vectors therefore differ by the same committee-independent constant
\[
\sum_i H_{|A_i|}-n.
\]
They induce identical pairwise comparisons and identical ties. Their winning committees are exactly the committees \(W_c\) for candidates \(c\) minimizing \(s(c)\).

## Verification
The embedded `verify_sav_pav_one_vacancy.py` uses only the Python standard library and exact rational arithmetic.

It checks the two per-ballot identities for every nonempty approval ballot through eight candidates and every possible omitted candidate.

It then independently exhausts every approval profile with two through four candidates and one through four voters, always using committee size \(m-1\). Across \(57160\) profiles it verifies:
- exact equality of the SAV and PAV winner sets;
- a committee-independent difference between their score vectors;
- exact agreement with the minimum-normalized-support characterization.

Run:

`python3 verify_sav_pav_one_vacancy.py`

The first output line must be `VERIFY_OK`.

The infinite statement is proved algebraically above; the finite replay is a consistency check rather than a substitute for that proof.

## Relationship to prior work
Brams and Kilgour introduced Satisfaction Approval Voting as a multiwinner approval rule in which each voter's unit weight is divided among approved candidates.

Aziz and collaborators study SAV and PAV together in one approval-based multiwinner framework. Their formal definitions are exactly the two objectives used here. They also prove that general PAV winner determination is NP-hard, even under strong restrictions on approval-set size, while SAV winner determination is polynomial-time.

The checked literature therefore already establishes the two rules, their distinct motivations, and their sharply different general computational complexity. The contribution here is the exact one-vacancy collapse: when the committee contains every candidate except one, the two objective functions differ only by a profile-dependent constant.

Targeted searches using SAV/PAV aliases, one-vacancy and all-but-one language, committee size \(m-1\), exact-winner equivalence, and near-full committees did not locate this identity or its winner-determination consequence.

## Limitations
The equivalence is specific to committees of size \(m-1\).

Empty approval ballots are excluded because the standard SAV denominator would be undefined.

The theorem concerns exact PAV, not sequential PAV or reweighted approval voting.

The result does not remove general PAV winner-determination hardness; it isolates one natural tractable boundary regime.

A specialized handbook remark, exercise, software optimization, or unindexed note could contain the same identity.

## References
1. S. J. Brams and D. M. Kilgour, “Satisfaction approval voting,” MPRA Paper 22709, posted 17 May 2010.
2. H. Aziz, S. Gaspers, J. Gudmundsson, S. Mackenzie, N. Mattei, and T. Walsh, “Computational Aspects of Multi-Winner Approval Voting,” arXiv:1407.3247, first submitted 11 July 2014.
